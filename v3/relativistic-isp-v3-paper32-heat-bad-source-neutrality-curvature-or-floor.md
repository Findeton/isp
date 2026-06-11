# Relativistic ISP V3 Paper 32: Heat-Bad Source Neutrality, Curvature, Or Floor

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Paper 31 closed the source-response calculus.  The next primitive same-law
analytic input should be the heat-bad source theorem because it is the
narrowest live obstruction:
$$
\mathrm{P31\text{-}HKBAD\text{-}SRC\text{-}NEUT}(a,\rho)
\quad+\quad
\mathrm{P31\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
$$

This paper attacks that theorem directly.  The guiding change of viewpoint is
not to compute the missing heat-bad matrix entries.  Instead, for every
heat-bad dual source \(Q\), split the actual source observable into its
switch-odd and switch-even parts:
$$
V_Q
=
V_Q^{odd}
+
V_Q^{even}.
$$
If the actual finite law is invariant under the recoupling switch and
\(V_Q^{even}\) is small, then the source pressure is nearly even:
$$
\left|\Psi_Q(a)-\Psi_Q(-a)\right|
\le
2a\|V_Q^{even}\|_\infty.
$$
Thus the neutrality problem is exactly an even-defect problem.  This is the
main positive theorem of the paper.

The second half audits every route to the needed curvature bound.  The
universal finite bound is too coarse.  A closing curvature estimate would
require a same-law Poincare/log-Sobolev inequality, a Ward-Stein inverse
bound, a Peter-Weyl source-tail regularity theorem, or a direct finite-table
variance theorem for the actual adaptive law.  None is supplied by the
current corpus.

The final result is a closed trichotomy.  Heat-bad source smallness would
follow from:
$$
\mathrm{P32\text{-}HKBAD\text{-}EVENDEF}(\epsilon)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi),
$$
with debit
$$
\epsilon+{\chi a\over2}.
$$
If this cannot fit and the dual source slope is sign-coherent above budget,
the same object becomes a lower-floor witness.  The paper does not invent
the missing value theorem; it isolates the two sharp primitive inputs:
switch-even defect control and same-law source curvature.

The second pass sharpens the target further.  If the recoupling switch is
only quasi-invariant under the actual law, with switch RN oscillation
\(\omega\), the closing debit becomes
$$
\epsilon+{\omega\over2a}+{\chi a\over2},
$$
or, after optimizing the source scale,
$$
\epsilon+\sqrt{\omega\chi}.
$$
Thus the next concrete same-law inputs are switch RN oscillation, heat-bad
product thinness, and only then curvature.

## 0. Imports And Barandes Rule

### Import 0.1: Paper 30 Heat-Bad Object

Paper 30 defines the heat-bad projected weighted signed matrix
$$
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
:=
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$

The heat-bad absolute debit is the normalized trace-norm support function of
this matrix family.

### Import 0.2: Paper 31 Source Response

For every deterministic heat-bad dual test
$$
Q=\{Q_\Gamma\}_\Gamma,
\qquad
\|Q_\Gamma\|_{op}\le1,
$$
Paper 31 defines the same-law source observable
$$
V_Q^{N,j}(\omega;\delta)
$$
and pressure
$$
\Psi_Q^{N,j}(s;\delta)
=
\log
\mathbf E_{N,j}^{act}
\exp\left(sV_Q^{N,j}(\cdot;\delta)\right).
$$
The first response satisfies
$$
\partial_s\Psi_Q^{N,j}(0;\delta)
=
\mathbf E_{N,j}^{act}[V_Q^{N,j}(\cdot;\delta)].
$$

The direct heat-bad absolute theorem is equivalent to
$$
\limsup_{(N,j)}
\sup_Q
\partial_s\Psi_Q^{N,j}(0;\delta)
\le \mu.
$$

### Convention 0.3: No Source Becomes A Physical Law

The source parameter \(s\) is a deterministic generating-function parameter.
All physical claims are derivatives at \(s=0\) under the actual adaptive
finite law.  For \(s\ne0\), the expression
$$
\mathbf E^{act}e^{sV_Q}
$$
is only an algebraic finite moment.  It is not a hidden Markov process, not a
division event, not a comparison measure, and not a replacement Yang-Mills
law.

This is the Barandes-aligned guardrail of the paper.

## 1. The Heat-Bad Target

### Definition 1.1: Heat-Bad Source Neutrality

For \(a>0\) and \(\rho\ge0\),
`P32-HKBAD-SRC-NEUT(a,rho)` asserts that cofinally, for every admissible
heat-bad dual source \(Q\),
$$
\left|
\Psi_Q^{N,j}(a;\delta)
-
\Psi_Q^{N,j}(-a;\delta)
\right|
\le 2\rho.
$$

### Definition 1.2: Heat-Bad Source Curvature

For \(a>0\) and \(\chi\ge0\),
`P32-HKBAD-SRC-CURV(a,chi)` asserts that cofinally, for every admissible
heat-bad dual source \(Q\) and every \(|s|\le a\),
$$
\left|
{\partial^2\over\partial s^2}
\Psi_Q^{N,j}(s;\delta)
\right|
\le \chi.
$$

### Lemma 1.3: Neutrality Plus Curvature Pays The Heat-Bad Debit

If `P32-HKBAD-SRC-NEUT(a,rho)` and
`P32-HKBAD-SRC-CURV(a,chi)` hold, then
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}
\left(\delta,{\rho\over a}+{\chi a\over2}\right)
$$
holds.

Proof.

This is Paper 31 Lemma 3.3 applied to the heat-bad source family, plus the
Paper 30/Paper 31 trace-dual identification of the heat-bad debit. `square`

### Corollary 1.4: The Numerical Target

Let
$$
B_{A}^{rem}
$$
denote the remaining Branch-A heat-bad budget after all already licensed
debits.  The positive source route needs
$$
{\rho\over a}+{\chi a\over2}
<
B_A^{rem}.
$$

The rest of the paper tries to source \(\rho\) and \(\chi\), or else produce
a floor.

## 2. The Switch-Pressure Viewpoint

This is the main change of viewpoint.  The heat-bad object arose from a
recoupling switch.  Therefore the source pressure should be decomposed by
that switch, not by raw matrix entries.

### Definition 2.1: Switch Action On Actual Records

Let
$$
\mathsf S_{N,j}
$$
denote the finite recoupling-switch map on the retained full-block record
space whenever it is defined by the Paper-30 full-block switch package.

`P32-HKBAD-SWLAW` asserts that \(\mathsf S_{N,j}\) is a measure-preserving
involution of the actual finite law:
$$
\mathsf S_{N,j}^2=\mathrm{id},
\qquad
(\mathsf S_{N,j})_*\mathbf P_{N,j}^{act}
=
\mathbf P_{N,j}^{act}.
$$

This is not a new dynamics.  It is a finite symmetry of the actual retained
record law.

### Definition 2.2: Switch Odd And Even Parts Of A Source

For a heat-bad source observable \(V_Q\), define
$$
V_Q^{odd}
:=
{1\over2}
\left(
V_Q
-
V_Q\circ\mathsf S
\right),
$$
and
$$
V_Q^{even}
:=
{1\over2}
\left(
V_Q
+
V_Q\circ\mathsf S
\right).
$$

Thus
$$
V_Q=V_Q^{odd}+V_Q^{even},
$$
with
$$
V_Q^{odd}\circ\mathsf S=-V_Q^{odd},
\qquad
V_Q^{even}\circ\mathsf S=V_Q^{even}.
$$

### Lemma 2.3: Odd Sources Have Exactly Even Pressure

Assume `P32-HKBAD-SWLAW`.  If \(V_Q^{even}=0\), then
$$
\Psi_Q(a)=\Psi_Q(-a)
$$
for every real \(a\).

Proof.

By switch invariance,
$$
\mathbf E^{act}e^{aV_Q}
=
\mathbf E^{act}e^{aV_Q\circ\mathsf S}.
$$
If \(V_Q\circ\mathsf S=-V_Q\), the right side is
$$
\mathbf E^{act}e^{-aV_Q}.
$$
Taking logarithms proves the claim. `square`

### Lemma 2.4: The Even Defect Controls Source Neutrality

Assume `P32-HKBAD-SWLAW`.  For every heat-bad source \(Q\),
$$
\left|\Psi_Q(a)-\Psi_Q(-a)\right|
\le
2|a|\,\|V_Q^{even}\|_{\infty}.
$$

Proof.

Write \(V=O+E\), where \(O=V^{odd}\) and \(E=V^{even}\).  By switch
invariance and oddness of \(O\),
$$
\mathbf E e^{a(O+E)}
=
\mathbf E e^{a(-O+E)}.
$$
Therefore
$$
\Psi(a)-\Psi(-a)
=
\log\mathbf E e^{-aO+aE}
-
\log\mathbf E e^{-aO-aE}.
$$
For any two bounded observables \(A,B\),
$$
\left|
\log\mathbf E e^{A+B}
-
\log\mathbf E e^A
\right|
\le
\|B\|_\infty.
$$
Apply this twice with \(B=\pm aE\). `square`

### Definition 2.5: Heat-Bad Even-Defect Gate

`P32-HKBAD-EVENDEF(epsilon)` asserts that `P32-HKBAD-SWLAW` holds and,
cofinally, for every admissible heat-bad dual source \(Q\),
$$
\|V_Q^{even}\|_\infty\le\epsilon.
$$

### Theorem 2.6: Even-Defect Implies Source Neutrality

If `P32-HKBAD-EVENDEF(epsilon)` holds, then
$$
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}NEUT}(a,a\epsilon)
$$
holds for every \(a>0\).

Proof.

This is Lemma 2.4 uniformly over \(Q\). `square`

### Corollary 2.7: First Positive Closing Package

If `P32-HKBAD-EVENDEF(epsilon)` and
`P32-HKBAD-SRC-CURV(a,chi)` hold, then
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}
\left(\delta,\epsilon+{\chi a\over2}\right)
$$
holds.

Proof.

Theorem 2.6 gives \(\rho=a\epsilon\).  Substitute into Lemma 1.3. `square`

This is the cleanest positive route discovered in this paper:
$$
\boxed{
\text{heat-bad smallness}
\Leftarrow
\text{switch-even defect smallness}
+
\text{source curvature smallness}.
}
$$

## 3. What Is The Even Defect?

The even-defect theorem is useful only if it is narrower than the original
unknown matrix.  We now express it in the block notation.

### Definition 3.1: Switched Dual Source

For a dual test \(Q=\{Q_\Gamma\}\), define the switched dual test
$$
Q^{\mathsf S}_\Gamma
:=
U_\Gamma Q_\Gamma U_\Gamma^*
$$
with the same heat-bad projection convention.

This definition is only a bookkeeping action on deterministic probes.  It is
not a new source law.

### Lemma 3.2: Even Defect Is The Switch-Symmetric Part Of The Weighted Product

At the integrand level, the even part of the heat-bad source is the
trace-dual pairing of \(Q\) with the switch-symmetric part of
$$
P_{\Gamma,bad}^{HK}
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$

Equivalently, `P32-HKBAD-EVENDEF(epsilon)` is a uniform bound on the
switch-symmetric residual of the heat-bad weighted product.

Proof.

By definition,
$$
V_Q^{even}
=
{1\over2}
\left(
V_Q+V_Q\circ\mathsf S
\right).
$$
The switch action conjugates the finite block matrices and sends each source
probe to its switched dual.  Averaging \(V_Q\) with \(V_Q\circ\mathsf S\)
therefore projects the integrand onto the switch-symmetric component.  The
support restriction by \(P_{\Gamma,bad}^{HK}\) remains in place because
heat-bad components are defined by the finite recoupling/heat classifier.
`square`

### Proposition 3.3: Bare Signed Oddness Does Not Make The Even Defect Small

The current Paper-30 counterexample to bare signed parity also falsifies the
derivation of `P32-HKBAD-EVENDEF(epsilon)` from bare \(\Sigma\)-oddness alone.

Proof.

Paper 30 Lemma 140.1 gives finite matrices with
$$
U^*\Sigma U=-\Sigma
$$
but
$$
D\Sigma+U^*D\Sigma U\ne0.
$$
Set \(R=I\).  The weighted source observable is then not purely switch-odd
whenever \(D\) is not switch-invariant.  Thus the switch-even defect can be
nonzero even with exact bare signed parity. `square`

### Proposition 3.4: Residual Quasi-Invariance Alone Does Not Make The Even Defect Small

Exact invariance of \(R_\Gamma\) under the switch does not imply
`P32-HKBAD-EVENDEF(epsilon)` in a closing range.

Proof.

Again take the two-channel model with \(R=I\).  Residual quasi-invariance is
exact, but the heat mismatch gives
$$
D\Sigma+U^*D\Sigma U\ne0.
$$
Thus the even defect may be supported entirely by the heat mismatch. `square`

### Proposition 3.5: Heat Balance Alone Does Not Make The Even Defect Small

The heat-bad sector is precisely the sector where the heat operator is not
balanced in the required recoupling orbit.  Therefore heat balance alone
cannot prove the even-defect bound on \(P_{\Gamma,bad}^{HK}(\delta)\).

Proof.

On the heat-good projection, the operator range of the heat mismatch is
controlled by \(\delta\).  On the heat-bad projection, the definition supplies
no such smallness; Paper 30 proves the heat-bad classifier is nonempty in the
active diagnostic template.  Therefore no theorem using only heat-balance
labels can give a closing even-defect bound on the heat-bad projection.
`square`

### Theorem 3.6: Even-Defect Is A New Primitive Same-Law Theorem

`P32-HKBAD-EVENDEF(epsilon)` is not derivable from the current corpus in a
closing range.

Proof.

Proposition 3.3 excludes derivation from bare signed oddness.  Proposition
3.4 excludes derivation from residual quasi-invariance alone.  Proposition
3.5 excludes derivation from heat balance alone.  The current corpus has no
additional theorem controlling the switch-symmetric part of the product
\(D_\Gamma R_\Gamma\Sigma_\Gamma\) on the heat-bad projection. `square`

## 4. Curvature As Susceptibility

The second required input is curvature.

### Lemma 4.1: Curvature Is Exponential-Source Variance

For a heat-bad source observable \(V_Q\),
$$
\Psi_Q''(s)
=
\operatorname{Var}_{s,Q}(V_Q),
$$
where the right side denotes the algebraic variance in the finite
exponential moment ratio
$$
{\mathbf E^{act}[F e^{sV_Q}]\over \mathbf E^{act}[e^{sV_Q}]}.
$$

This ratio is not a new law; it is a finite derivative expression under the
actual law.

Proof.

Differentiate the finite logarithmic moment generating function twice.
`square`

### Lemma 4.2: Universal Oscillation Curvature Bound

If
$$
\operatorname{osc}(V_Q)\le L_Q,
$$
then for every \(s\),
$$
\Psi_Q''(s)\le {L_Q^2\over4}.
$$

Proof.

The variance of any real random variable with oscillation at most \(L_Q\) is
at most \(L_Q^2/4\), under any probability weighting. `square`

### Proposition 4.3: The Universal Bound Is Not A Closing Curvature Source

The bound in Lemma 4.2 is too coarse to close the heat-bad Branch-A budget
unless the current corpus already supplies a cofinal small oscillation bound
for every heat-bad dual source.

Proof.

The heat-bad source \(V_Q\) is a normalized trace-dual pairing with
\(\mathcal W_{\Gamma,bad}^{N,j}\).  A small oscillation bound for all \(Q\)
would itself be a uniform absolute control theorem for the same heat-bad
object.  Papers 30--31 prove that such a theorem is not contained in the
current corpus.  Therefore the universal oscillation estimate does not
source a new closing curvature bound. `square`

### Definition 4.4: Same-Law Source Poincare Input

`P32-HKBAD-SPI(C,L)` asserts that the actual finite law satisfies a
source-Poincare estimate for all heat-bad source observables:
$$
\operatorname{Var}_{s,Q}(V_Q)
\le
C\,\mathcal E_{s,Q}(V_Q,V_Q)
$$
for every \(|s|\le a\), and the corresponding Dirichlet form obeys
$$
\mathcal E_{s,Q}(V_Q,V_Q)\le L.
$$

Here \(\mathcal E_{s,Q}\) is not a Markov generator of a hidden dynamics.  It
is an admissible finite carré-du-champ or conditional-variance certificate
for the actual record law, if such a certificate is proved.

### Lemma 4.5: Source Poincare Gives Curvature

If `P32-HKBAD-SPI(C,L)` holds, then
$$
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,CL)
$$
holds.

Proof.

Combine Lemma 4.1 with the Poincare estimate. `square`

### Proposition 4.6: Source Poincare Is Not In The Current Corpus

The current corpus does not prove `P32-HKBAD-SPI(C,L)` with \(CL\) in a
closing range.

Proof.

Such an estimate is a same-law concentration theorem for the actual adaptive
finite law under all heat-bad source insertions.  Papers 25--31 repeatedly
isolate screened conditional influence, Dobrushin contraction, low-mode
spectral contraction, and Peter-Weyl tails as missing same-law analytic
inputs.  None supplies a finite Poincare/log-Sobolev constant for the
heat-bad source family. `square`

## 5. Ward-Stein Curvature Route

The next creative attempt is to avoid global concentration by using an
identity.  If the source derivative is a divergence, it can be small without
knowing the whole distribution.

### Definition 5.1: Heat-Bad Ward-Stein Certificate

`P32-HKBAD-WSTEIN(kappa)` asserts that for every heat-bad dual source \(Q\)
there are finite same-law vector fields \(X_\alpha\), scores \(S_\alpha\),
and a controlled inverse Stein solution \(G_Q\) such that
$$
V_Q-\mathbf E^{act}[V_Q]
=
\sum_\alpha X_\alpha G_{Q,\alpha},
$$
and
$$
\sum_\alpha
\mathbf E^{act}\left[
\left|G_{Q,\alpha}S_\alpha\right|
\right]
\le \kappa
$$
with the heat-bad ledger normalization.

### Lemma 5.2: Ward-Stein Certificate Bounds First Response

If `P32-HKBAD-WSTEIN(kappa)` holds, then
$$
\sup_Q|\partial_s\Psi_Q(0)|
\le \kappa.
$$

Proof.

Finite integration by parts gives
$$
\mathbf E^{act}[X_\alpha G_{Q,\alpha}]
=
-
\mathbf E^{act}[G_{Q,\alpha}S_\alpha].
$$
Sum over \(\alpha\) and use the certificate bound. `square`

### Proposition 5.3: Ward-Stein Would Bypass Curvature But Is Not Sourced

`P32-HKBAD-WSTEIN(kappa)` would be stronger than neutrality plus curvature,
but the current corpus does not prove it.

Proof.

The certificate requires an inverse divergence solution with norm control on
the exact heat-bad source observable.  Papers 20--31 contain finite
integration-by-parts identities and Ward-style bookkeeping, but no bounded
inverse Stein theorem for the actual adaptive heat-bad source family.  Such a
theorem would be new same-law value information. `square`

## 6. Peter-Weyl Curvature And Tail Route

The third attack is to source curvature by representation decay.

### Definition 6.1: Heat-Bad Source Peter-Weyl Split

For cutoff \(L\), decompose
$$
V_Q=V_{Q,\le L}+V_{Q,>L}
$$
into retained Peter-Weyl modes of the actual heat-bad source observable.

### Lemma 6.2: Low/Tail Curvature Bound

If
$$
\operatorname{Var}_{s,Q}(V_{Q,\le L})\le \chi_L
$$
and
$$
\|V_{Q,>L}\|_\infty\le \tau_L
$$
uniformly for \(|s|\le a\), then
$$
\Psi_Q''(s)
\le
2\chi_L+2\tau_L^2.
$$

Proof.

Use
$$
\operatorname{Var}(A+B)
\le
2\operatorname{Var}(A)+2\operatorname{Var}(B)
$$
and \(\operatorname{Var}(B)\le\|B\|_\infty^2\). `square`

### Definition 6.3: Heat-Bad Peter-Weyl Curvature Source

`P32-HKBAD-PWCURV(L,chi_L,tau_L)` asserts the two bounds in Lemma 6.2 for
the actual heat-bad source family.

### Proposition 6.4: Peter-Weyl Curvature Is Not Sourced By Existing Tail Tables

The current Paper-28/Paper-31 Peter-Weyl work does not prove
`P32-HKBAD-PWCURV` in a closing range.

Proof.

The existing Peter-Weyl audits prove that finite projection is meaningful
only when paired with a same-law tail theorem.  They do not prove finite-band
support, cofinal coefficient decay, or a uniform source-tail bound for the
actual heat-bad residual observable.  The heat-bad source split is therefore
valid but not closing. `square`

## 7. Direct Floor Geometry

If smallness cannot be proved, the same source body can produce a floor.

### Definition 7.1: Heat-Bad Dual Source Floor

`P32-HKBAD-DUALFLOOR(M)` asserts that there exists a deterministic cofinal
choice of heat-bad dual sources \(Q_{N,j}\) such that
$$
\liminf_{(N,j)}
\left|
\partial_s\Psi_{Q_{N,j}}^{N,j}(0;\delta)
\right|
\ge M,
$$
and the sign, retained-row, orientation, endpoint, and normalization
conventions match the Branch-A floor ledger.

### Lemma 7.2: Failure Of Absolute Smallness Gives A Dual Slope

If
$$
\limsup_{(N,j)}
\sup_Q
\partial_s\Psi_Q^{N,j}(0;\delta)
>
M,
$$
then there is a cofinal subsequence and deterministic dual choices
\(Q_{N,j}\) such that
$$
\partial_s\Psi_{Q_{N,j}}^{N,j}(0;\delta)>M
$$
along that subsequence.

Proof.

This is the definition of limsup and supremum.  At finite \((N,j)\), the
dual unit ball is compact in the retained finite matrix space, so the
supremum may be approximated by deterministic choices. `square`

### Proposition 7.3: Dual Slope Is Not Automatically A Branch-A Floor

The dual slope from Lemma 7.2 becomes a Branch-A falsifying floor only if the
chosen dual sources are sign-coherent in the retained physical ledger.

Proof.

Trace duality can choose \(Q\) to align with a matrix norm.  Branch-A floor
requires a sign-coherent retained scalar contribution in the same orientation
and normalization conventions as the positive budget.  An adversarial polar
dual is not automatically the physical floor scalar. `square`

### Theorem 7.4: Floor Route Is Valid But Not Sourced

The heat-bad floor route is conditionally valid and not proved by the current
corpus.

Proof.

Lemma 7.2 gives the dual-slope mechanism.  Proposition 7.3 gives the missing
coherence requirement.  Paper 30 and Paper 31 both record that no
sign-coherent heat-bad floor above the Branch-A budget has been proved.
`square`

## 8. The Heat-Bad Source Trichotomy

The previous sections combine into a precise trichotomy.

### Theorem 8.1: Heat-Bad Source Trichotomy

Fix a remaining Branch-A heat-bad budget \(B_A^{rem}\).  Exactly one of the
following must be established to settle the heat-bad source route:

1. **Positive even-defect/curvature closure:** prove
   `P32-HKBAD-EVENDEF(epsilon)` and `P32-HKBAD-SRC-CURV(a,chi)` with
   $$
   \epsilon+{\chi a\over2}<B_A^{rem}.
   $$
2. **Positive direct response closure:** prove directly that
   $$
   \limsup_{(N,j)}\sup_Q\partial_s\Psi_Q^{N,j}(0;\delta)<B_A^{rem}.
   $$
3. **Negative floor closure:** prove `P32-HKBAD-DUALFLOOR(M)` with
   $$
   M>B_A^{rem}
   $$
   in the Branch-A floor ledger.

Proof.

The first item closes by Corollary 2.7.  The second is the direct
source-response form of `P30-HKBAD-ABS`.  The third is the floor alternative
from Section 7.  If neither upper route is proved and the lower route is not
proved, the heat-bad source route remains undecided. `square`

### Corollary 8.2: Best New Positive Target

The best positive target is not generic source neutrality.  It is the sharper
pair
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}EVENDEF}(\epsilon)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
}
$$

This is narrower than the original matrix-value theorem because the odd
part of \(V_Q\) is harmless under a switch-invariant actual law.  Only the
switch-even defect and susceptibility remain.

## 9. Current-Corpus Verdict On Each Attempt

### Attempt 9.1: Exact Switch Oddness

Exact switch oddness would prove neutrality with \(\rho=0\).  It fails as a
current-corpus derivation because Paper 30 proves bare \(\Sigma\)-oddness is
not enough on heat-bad components.

Status: conditionally valid, not sourced.

### Attempt 9.2: Switch-Even Defect

Even-defect control is the best new theorem printed in this paper.  It is
strictly sharper than asking for all heat-bad entries.  However, the current
corpus does not bound the switch-even part of \(D_\Gamma R_\Gamma\Sigma_\Gamma\)
on \(P_{\Gamma,bad}^{HK}\).

Status: best primitive positive target, not sourced.

### Attempt 9.3: Universal Curvature

Universal boundedness gives a curvature bound, but not a closing one unless
the heat-bad source observable already has small oscillation.  That is
another form of the missing value theorem.

Status: proved but non-closing.

### Attempt 9.4: Source Poincare Or Log-Sobolev

A same-law Poincare/log-Sobolev theorem would close curvature.  It would be
a major analytic input for the actual adaptive law and is not in Papers
20--31.

Status: conditionally valid, not sourced.

### Attempt 9.5: Ward-Stein

A bounded inverse Ward/Stein certificate would bypass curvature and bound
the first source response directly.  No such inverse certificate is present
in the corpus.

Status: conditionally valid, not sourced.

### Attempt 9.6: Peter-Weyl Curvature/Tail

Peter-Weyl splitting is valid, but the needed same-law tail/regularity
estimate is exactly one of the primitive inputs left open by Papers 28 and
31.

Status: conditionally valid, not sourced.

### Attempt 9.7: Sign-Coherent Floor

A dual source floor is a valid negative exit if it is sign-coherent in the
Branch-A ledger.  The current corpus proves no such floor.

Status: conditionally valid, not sourced.

## 10. Final Theorem

### Theorem 10.1: Paper 32 Fully Settles The Heat-Bad Source Attack At The Current-Corpus Level

Paper 32 proves:

1. heat-bad source neutrality follows from switch-even defect control;
2. heat-bad source curvature is same-law susceptibility;
3. universal curvature is too coarse;
4. source Poincare/log-Sobolev, Ward-Stein, and Peter-Weyl curvature routes
   would close the needed curvature but are not sourced by Papers 20--31;
5. a sign-coherent source floor is a valid negative exit but is not sourced;
6. the best remaining positive theorem is
   $$
   \mathrm{P32\text{-}HKBAD\text{-}EVENDEF}(\epsilon)
   +
   \mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi)
   $$
   with
   $$
   \epsilon+{\chi a\over2}<B_A^{rem}.
   $$

Proof.

Items 1 and 6 are Theorem 2.6 and Corollary 2.7.  Item 2 is Lemma 4.1.  Item
3 is Proposition 4.3.  Item 4 is Sections 4--6.  Item 5 is Section 7.
`square`

### Corollary 10.2: What Should Be Attacked Next

Further pressure calculus will not move the obstruction.  The next direct
work should choose one of:

1. prove the heat-bad switch-even defect bound;
2. prove a same-law source Poincare/log-Sobolev bound for the heat-bad
   source family;
3. prove a bounded Ward-Stein inverse for the heat-bad source family;
4. prove a same-law Peter-Weyl regularity theorem strong enough to bound
   heat-bad source curvature;
5. prove a sign-coherent heat-bad lower floor.

The most promising positive order is:

1. `P32-HKBAD-EVENDEF(epsilon)`;
2. `P32-HKBAD-SPI(C,L)`;
3. `P32-HKBAD-WSTEIN(kappa)`;
4. `P32-HKBAD-PWCURV(L,chi_L,tau_L)`;
5. `P32-HKBAD-DUALFLOOR(M)`.

This is as far as Paper 32 can honestly go without a new actual-law analytic
theorem.  The creative reframing has isolated the right object: not the whole
heat-bad matrix, but its switch-even source defect and susceptibility.

## 11. Second Pass: Investigating The Primitive Target Itself

The previous sections identify the live primitive package
$$
\mathrm{P32\text{-}HKBAD\text{-}EVENDEF}(\epsilon)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
$$

We now attack that package directly.  The point is not to add another
placeholder.  The point is to find the precise finite object whose smallness
would constitute the new same-law value theorem.

There are two cases.

1. The recoupling switch is an exact symmetry of the actual retained finite
   law.  Then the curvature bound is only a harmless finite regularity
   condition, because the debit is
   $$
   \epsilon+{\chi a\over2}
   $$
   and \(a\) may be taken small after the finite curvature bound is known.
   In this case the real theorem is just the switch-even defect bound.
2. The switch is only quasi-invariant.  Then the Radon-Nikodym defect of the
   switch enters the source-pressure comparison.  The real theorem becomes a
   joint bound on the switch-even defect, the switch RN oscillation, and the
   source curvature.

This distinction is important.  It prevents us from spending effort on a
global curvature theorem if the switch defect is already the bottleneck.

## 12. Exact Switch Law Versus Switch RN Defect

### Definition 12.1: Heat-Bad Switch Quasi-Invariance

Let \(\mathsf S=\mathsf S_{N,j}\) be the retained full-block recoupling
switch whenever it is defined on the heat-bad source record space.  Let
$$
J_{\mathsf S}^{N,j}
:=
{d(\mathsf S_*\mathbf P_{N,j}^{act})\over d\mathbf P_{N,j}^{act}}
$$
on the retained finite record space.

`P32-HKBAD-SWQI(omega)` asserts that cofinally the switch is a finite
involution on the retained support and
$$
\operatorname{osc}\log J_{\mathsf S}^{N,j}
\le \omega
$$
on every retained heat-bad source block used by the dual test family.

The special case \(\omega=0\) is exact same-law switch invariance, up to a
constant density normalization, hence gives `P32-HKBAD-SWLAW`.

### Lemma 12.2: Switch RN Defect Adds A Source-Neutrality Debit

Assume `P32-HKBAD-SWQI(omega)` and
$$
\|V_Q^{even}\|_\infty\le\epsilon
$$
for every admissible heat-bad dual source \(Q\).  Then
$$
\left|\Psi_Q(a)-\Psi_Q(-a)\right|
\le
\omega+2a\epsilon.
$$
Equivalently,
$$
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}NEUT}
\left(a,a\epsilon+{\omega\over2}\right)
$$
holds.

Proof.

Write \(V=O+E\), where \(O\circ\mathsf S=-O\) and
\(E\circ\mathsf S=E\).  By the finite change of variables,
$$
\mathbf E^{act}e^{aV}
=
\mathbf E^{act}
\left[
J_{\mathsf S}e^{a(-O+E)}
\right].
$$
Compare this with
$$
\mathbf E^{act}e^{-aV}
=
\mathbf E^{act}e^{-aO-aE}.
$$
The bounded even defect changes the logarithm by at most \(2a\epsilon\).
The remaining multiplier \(J_{\mathsf S}\) changes any logarithmic moment by
at most \(\operatorname{osc}\log J_{\mathsf S}\), because under any tilted
finite probability measure the expectation of \(J_{\mathsf S}\) lies between
the minimum and maximum of \(J_{\mathsf S}\).  This proves the bound.
`square`

### Corollary 12.3: Quasi-Invariant Switch Closure Inequality

If `P32-HKBAD-SWQI(omega)`,
`P32-HKBAD-EVENDEF(epsilon)`, and
`P32-HKBAD-SRC-CURV(a,chi)` hold, then
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}
\left(
\delta,
\epsilon+{\omega\over 2a}+{\chi a\over2}
\right)
$$
holds.

Optimizing over \(a\) gives the model debit
$$
\epsilon+\sqrt{\omega\chi}.
$$

Proof.

Use Lemma 12.2 in Lemma 1.3.  The displayed optimization is the minimum of
\(\omega/(2a)+\chi a/2\). `square`

### Corollary 12.4: What To Prove First

The first investigation target is not curvature.  It is:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}SWQI}(\omega)
\quad\text{and}\quad
\mathrm{P32\text{-}HKBAD\text{-}EVENDEF}(\epsilon).
}
$$

If \(\omega=0\), any finite curvature bound can be made negligible by
choosing \(a\) small.  If \(\omega>0\), curvature matters only through the
product \(\omega\chi\).

## 13. Exact Even-Defect Integrand

We now print the actual finite matrix whose smallness is required.

For the switched operators, write
$$
\widetilde D_\Gamma:=U_\Gamma^*D_\Gamma U_\Gamma,
\qquad
\widetilde R_\Gamma:=U_\Gamma^*R_\Gamma U_\Gamma,
\qquad
\widetilde\Sigma_\Gamma:=U_\Gamma^*\Sigma_\Gamma U_\Gamma.
$$

The heat-bad weighted source matrix is
$$
\mathcal W_{\Gamma,bad}
=
P_{\Gamma,bad}^{HK}
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
\widetilde D_\Gamma\widetilde R_\Gamma\widetilde\Sigma_\Gamma
\right).
$$

The exact three-term decomposition is
$$
\mathcal W_{\Gamma,bad}
=
P_{\Gamma,bad}^{HK}
D_\Gamma R_\Gamma
\left(
\Sigma_\Gamma+\widetilde\Sigma_\Gamma
\right)
$$
$$
\quad+
P_{\Gamma,bad}^{HK}
D_\Gamma
\left(
\widetilde R_\Gamma-R_\Gamma
\right)
\widetilde\Sigma_\Gamma
$$
$$
\quad+
P_{\Gamma,bad}^{HK}
\left(
\widetilde D_\Gamma-D_\Gamma
\right)
\widetilde R_\Gamma
\widetilde\Sigma_\Gamma.
$$

Call these terms
$$
\mathcal W_{\Sigma,\Gamma}
\quad+\quad
\mathcal W_{R,\Gamma}
\quad+\quad
\mathcal W_{H,\Gamma}.
$$

The three terms have different meanings:

1. \(\mathcal W_{\Sigma,\Gamma}\) is the signed-parity defect.
2. \(\mathcal W_{R,\Gamma}\) is the residual/Jacobian switch defect.
3. \(\mathcal W_{H,\Gamma}\) is the heat-bad commutator defect.

This decomposition is the finite object-level version of the Paper-30
verdict.  The heat-bad problem is not one problem; it is a three-term
source defect with a hard heat-bad term.

### Lemma 13.1: Three-Term Source Bound

Define normalized trace-dual envelopes
$$
E_\Sigma^{N,j}
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}\|\mathcal W_{\Sigma,\Gamma}\|_1,
$$
$$
E_R^{N,j}
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}\|\mathcal W_{R,\Gamma}\|_1,
$$
and
$$
E_H^{N,j}
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}\|\mathcal W_{H,\Gamma}\|_1.
$$

If cofinally
$$
E_\Sigma^{N,j}\le\epsilon_\Sigma,
\qquad
E_R^{N,j}\le\epsilon_R,
\qquad
E_H^{N,j}\le\epsilon_H,
$$
then the heat-bad direct response satisfies
$$
\sup_Q|\partial_s\Psi_Q(0)|
\le
\epsilon_\Sigma+\epsilon_R+\epsilon_H.
$$

In particular, any corresponding pointwise switch-even defect bound may take
$$
\epsilon
=
\epsilon_\Sigma+\epsilon_R+\epsilon_H.
$$

Proof.

The trace-dual unit ball is the support function of the trace norm.  Apply
the triangle inequality to the three displayed terms and then take the
supremum over dual tests \(Q\). `square`

### Proposition 13.2: Which Term Is New

The current corpus already identifies the first two terms as known
primitive gates:

1. \(E_\Sigma\) is controlled by a heat-bad weighted signed-parity theorem,
   not by bare \(\Sigma\)-oddness.
2. \(E_R\) is controlled by heat-bad residual quasi-invariance.

The genuinely stubborn term is
$$
E_H
=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\left\|
P_{\Gamma,bad}^{HK}
\left(
\widetilde D_\Gamma-D_\Gamma
\right)
\widetilde R_\Gamma
\widetilde\Sigma_\Gamma
\right\|_1.
$$

On the heat-bad projection, \(\widetilde D_\Gamma-D_\Gamma\) is not small
by definition.  Therefore \(E_H\) can be small only through same-law control
of the product
$$
P_{\Gamma,bad}^{HK}\widetilde R_\Gamma\widetilde\Sigma_\Gamma,
$$
or through sign-coherent cancellation/floor information.

Proof.

The identification of \(E_\Sigma\) is Paper 30 Section 139.  The
identification of \(E_R\) is Paper 30 Section 142.  The last claim follows
because `HK-bad(delta)` means the heat diagonal is not balanced on the
component, so the operator norm of the heat mismatch is not controlled by
\(\delta\). `square`

## 14. Attempt A: Algebraic Cancellation

The most optimistic possibility is that the three-term defect vanishes
algebraically on the admissible heat-bad projection.

### Proposition 14.1: Exact Algebraic Cancellation Requires Three Exact Identities

Exact algebraic cancellation of \(\mathcal W_{\Gamma,bad}\) for all
admissible heat-bad blocks follows if all three identities hold:
$$
P_{\Gamma,bad}^{HK}
D_\Gamma R_\Gamma
\left(
\Sigma_\Gamma+\widetilde\Sigma_\Gamma
\right)=0,
$$
$$
P_{\Gamma,bad}^{HK}
D_\Gamma
\left(
\widetilde R_\Gamma-R_\Gamma
\right)
\widetilde\Sigma_\Gamma=0,
$$
and
$$
P_{\Gamma,bad}^{HK}
\left(
\widetilde D_\Gamma-D_\Gamma
\right)
\widetilde R_\Gamma
\widetilde\Sigma_\Gamma=0.
$$

The first is weighted signed parity, the second is residual switch
invariance, and the third is heat-bad product annihilation.

Proof.

This is the three-term decomposition of Section 13. `square`

### Proposition 14.2: Current Corpus Does Not Prove Algebraic Cancellation

The current corpus does not prove exact algebraic cancellation on the
heat-bad projection.

Proof.

Paper 30 Lemma 140.1 falsifies derivation from bare signed parity.  Paper 30
Proposition 142.4 falsifies derivation from residual quasi-invariance alone.
Paper 30 Corollary 135.5 and Sections 136--138 show that heat-bad support is
not representation-theoretically empty.  No current theorem proves
annihilation of
\(P_{\Gamma,bad}^{HK}\widetilde R_\Gamma\widetilde\Sigma_\Gamma\).
Therefore exact algebraic cancellation is not sourced. `square`

## 15. Attempt B: Quantitative Commutator Bound

The next possibility is not exact cancellation, but a small commutator
defect.

### Definition 15.1: Heat-Bad Product Thinness

`P32-HKBAD-PRODTHIN(tau)` asserts that cofinally
$$
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\left\|
P_{\Gamma,bad}^{HK}
\widetilde R_\Gamma
\widetilde\Sigma_\Gamma
\right\|_1
\le \tau.
$$

Let
$$
\Delta_D^{bad}
:=
\sup_{\Gamma}
\left\|
P_{\Gamma,bad}^{HK}
\left(
\widetilde D_\Gamma-D_\Gamma
\right)
P_{\Gamma,bad}^{HK}
\right\|_{op}.
$$

### Lemma 15.2: Product Thinness Bounds The Heat Term

If `P32-HKBAD-PRODTHIN(tau)` holds, then
$$
E_H^{N,j}
\le
\Delta_D^{bad}\tau
$$
cofinally.

Proof.

Use the operator-trace norm inequality
$$
\|AB\|_1\le\|A\|_{op}\|B\|_1
$$
with
\(A=P_{\Gamma,bad}^{HK}(\widetilde D_\Gamma-D_\Gamma)P_{\Gamma,bad}^{HK}\)
and \(B=P_{\Gamma,bad}^{HK}\widetilde R_\Gamma\widetilde\Sigma_\Gamma\).
`square`

### Proposition 15.3: Heat-Bad Product Thinness Is Exactly The Missing Value Input

`P32-HKBAD-PRODTHIN(tau)` is a genuine same-law value theorem.  It is not
proved by the current corpus.

Proof.

The heat mismatch \(\Delta_D^{bad}\) is finite and representation-theoretic.
The unknown factor is the actual same-law product
\(P_{\Gamma,bad}^{HK}\widetilde R_\Gamma\widetilde\Sigma_\Gamma\).  Papers
26--30 repeatedly prove that these actual residual/signed values are not
determined by finite labels, scalar worksheets, RN ratios, or representation
classification alone.  Therefore product thinness is precisely the missing
same-law information, now in its thinnest heat-bad form. `square`

## 16. Attempt C: Signed Average Cancellation Instead Of Pointwise Smallness

Pointwise even-defect smallness may be too strong.  A weaker theorem would
bound only the source response of the even component.

### Definition 16.1: Heat-Bad Even-Response Bound

`P32-HKBAD-EVENRESP(epsilon)` asserts that cofinally, for every heat-bad
dual source \(Q\),
$$
\left|
\mathbf E_{N,j}^{act}[V_Q^{even}]
\right|
\le\epsilon.
$$

### Lemma 16.2: Even-Response Is Sufficient At First Order

If `P32-HKBAD-SWLAW` and `P32-HKBAD-EVENRESP(epsilon)` hold, then
$$
\sup_Q|\partial_s\Psi_Q(0)|\le\epsilon.
$$

Proof.

Under exact switch invariance,
\(\mathbf E^{act}[V_Q^{odd}]=0\).  Since
\(V_Q=V_Q^{odd}+V_Q^{even}\), the first response is the expectation of the
even part. `square`

### Proposition 16.3: Even-Response Is Weaker But Still Unsourced

`P32-HKBAD-EVENRESP(epsilon)` is weaker than
`P32-HKBAD-EVENDEF(epsilon)`, but the current corpus does not prove it in a
closing range.

Proof.

The bound is an actual-law expectation of the same heat-bad even matrix
printed in Section 13.  It no longer asks for pointwise smallness, but it
still asks for a same-law signed/residual average on the heat-bad
projection.  Papers 30--31 prove only the source-response identity, not the
smallness of that response. `square`

## 17. Curvature After The Even-Defect Pass

The curvature problem should now be viewed through Corollary 12.3.

### Lemma 17.1: Exact Switch Law Makes Curvature A Secondary Issue

Assume exact switch law, hence \(\omega=0\).  If
`P32-HKBAD-EVENDEF(epsilon)` holds and the source family has any finite
cofinal curvature bound \(\chi<\infty\), then for every \(\eta>0\)
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}
(\delta,\epsilon+\eta)
$$
holds.

Proof.

By Corollary 2.7, the debit is \(\epsilon+\chi a/2\).  Choose
\(a<2\eta/\chi\). `square`

### Lemma 17.2: Quasi-Invariant Switch Law Needs The Product Margin

Assume only `P32-HKBAD-SWQI(omega)`.  If a finite curvature bound \(\chi\)
is available, then the optimized heat-bad debit is
$$
\epsilon+\sqrt{\omega\chi}.
$$

Thus a positive proof requires
$$
\epsilon+\sqrt{\omega\chi}<B_A^{rem}.
$$

Proof.

This is Corollary 12.3. `square`

### Proposition 17.3: Universal Curvature Helps Only After Switch Control

The universal oscillation curvature bound from Lemma 4.2 is useful only if
the switch RN oscillation \(\omega\) is already small enough.  Without a
small \(\omega\), universal curvature cannot turn the source route into a
closing theorem.

Proof.

With \(\omega>0\), the optimized debit contains
\(\sqrt{\omega\chi}\).  If \(\chi\) is merely the crude oscillation bound,
this term is controlled only by a same-law switch RN theorem strong enough
to make \(\omega\chi\) small.  No current paper supplies such a switch RN
oscillation bound on heat-bad blocks. `square`

## 18. Result Of The Primitive-Target Investigation

### Theorem 18.1: Sharp Primitive Heat-Bad Target After Investigation

The primitive heat-bad target is now the following finite same-law package:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}SWQI}(\omega)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}EVENDEF}(\epsilon)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
}
$$

It closes the heat-bad source route whenever
$$
\epsilon+{\omega\over2a}+{\chi a\over2}<B_A^{rem},
$$
or, after optimizing \(a\),
$$
\epsilon+\sqrt{\omega\chi}<B_A^{rem}.
$$

In the exact switch-law case \(\omega=0\), this reduces to
$$
\epsilon<B_A^{rem}.
$$

Proof.

The nonzero-\(\omega\) statement is Corollary 12.3.  The optimized form is
Lemma 17.2.  The exact switch-law specialization is Lemma 17.1. `square`

### Theorem 18.2: Current-Corpus Verdict On The Primitive Target

The current corpus does not prove the package in Theorem 18.1 in a closing
range.

More precisely:

1. exact switch law is not proved for the actual adaptive heat-bad retained
   law;
2. switch RN oscillation `P32-HKBAD-SWQI(omega)` is not proved in a small
   range;
3. the switch-even defect decomposes into signed-parity, residual
   quasi-invariance, and heat-bad product terms;
4. the heat-bad product term requires
   `P32-HKBAD-PRODTHIN(tau)` or an equivalent same-law value theorem;
5. even-response smallness is weaker than pointwise even-defect smallness
   but is still not sourced;
6. universal curvature is available only as a finite non-closing bound
   unless the switch RN oscillation is already small.

Proof.

Items 1 and 2 are the distinction made in Section 12 and the current-corpus
absence of a heat-bad switch RN theorem.  Items 3 and 4 are Section 13 and
Section 15.  Item 5 is Section 16.  Item 6 is Section 17. `square`

### Corollary 18.3: Next Concrete Attack Order

The next useful work should proceed in this order:

1. prove or sharply bound the actual switch RN oscillation
   `P32-HKBAD-SWQI(omega)`;
2. prove or sharply bound heat-bad product thinness
   `P32-HKBAD-PRODTHIN(tau)`;
3. if pointwise product thinness fails, try the weaker
   `P32-HKBAD-EVENRESP(epsilon)`;
4. only after one of the previous three succeeds, optimize curvature;
5. if the heat-bad product is large and sign-coherent, promote it to
   `P32-HKBAD-DUALFLOOR(M)`.

This is the positive path left by the investigation.  It is still Branch A,
still same-law, and still Barandes-aligned: every object is a deterministic
finite source, switch density, or trace-dual observable evaluated under the
actual adaptive finite law.

## 19. Attack On `P32-HKBAD-SWQI`

The switch RN problem can be made completely explicit by returning to the
finite DLR density of Paper 30 Section 11.  This is the first point where
the investigation gains actual quantitative content rather than another
name.

### Definition 19.1: Finite DLR Switch Hamiltonian Difference

On a retained parent DLR chart \(B\), write the actual finite conditional as
$$
dK_B^{par}(g\mid\eta)
=
{1\over Z(\eta)}
\exp\left(-{\mathcal H}_B^{N,j}(g,\eta)\right)\,dg,
$$
where
$$
{\mathcal H}_B^{N,j}(g,\eta)
=
-\sum_{p\cap B\ne\varnothing}
\log H_{t_p}(h_p(g,\eta))
+
V_{RPF}(g,\eta)
-
\log J_{tree}(g,\eta).
$$

Let \(\mathsf S\) be the retained heat-bad recoupling switch on the same
finite chart.  Define the switch Hamiltonian difference
$$
\Delta_{\mathsf S}{\mathcal H}_B^{N,j}(g,\eta)
:=
{\mathcal H}_B^{N,j}(\mathsf S g,\eta)
-
{\mathcal H}_B^{N,j}(g,\eta)
-
\log |\det D\mathsf S(g)|.
$$

For unitary recoupling switches on Haar coordinates,
\(|\det D\mathsf S|=1\), but the determinant is kept in the formula to make
the chart-dependence explicit.

### Lemma 19.2: Exact Formula For The Switch RN Oscillation

On every finite chart on which the switch is a bijection of the retained
support,
$$
\operatorname{osc}\log J_{\mathsf S}^{N,j}
=
\operatorname{osc}
\left(
-\Delta_{\mathsf S}{\mathcal H}_B^{N,j}
\right).
$$

Consequently `P32-HKBAD-SWQI(omega)` follows from the cofinal bound
$$
\operatorname{osc}
\Delta_{\mathsf S}{\mathcal H}_B^{N,j}
\le \omega
$$
on the retained heat-bad source support.

Proof.

The density of \(\mathsf S_*K_B^{par}\) at \(g\) is the density of
\(K_B^{par}\) at \(\mathsf S^{-1}g\), multiplied by the inverse chart
Jacobian.  Since \(\mathsf S\) is an involution on the retained support, the
log Radon-Nikodym derivative is the displayed Hamiltonian difference up to an
additive constant.  Oscillation removes the constant and the normalizer.
`square`

### Definition 19.3: Switch-DLR Envelope

Decompose
$$
\Delta_{\mathsf S}{\mathcal H}_B
=
\Delta_{\mathsf S}{\mathcal H}_{HK}
+
\Delta_{\mathsf S}V_{RPF}
-
\Delta_{\mathsf S}\log J_{tree}
-
\log|\det D\mathsf S|.
$$

Define
$$
\Omega_{SW}^{DLR,N,j}(B)
:=
\operatorname{osc}\Delta_{\mathsf S}{\mathcal H}_{HK}
+
\operatorname{osc}\Delta_{\mathsf S}V_{RPF}
+
\operatorname{osc}\Delta_{\mathsf S}\log J_{tree}
+
\operatorname{osc}\log|\det D\mathsf S|.
$$

### Lemma 19.4: Switch-DLR Envelope Sources `SWQI`

If cofinally
$$
\Omega_{SW}^{DLR,N,j}(B)\le\omega,
$$
then `P32-HKBAD-SWQI(omega)` holds.

Proof.

Use the triangle inequality for oscillations in Lemma 19.2. `square`

### Proposition 19.5: The Crude Switch-DLR Envelope Is Real But Non-Closing

The switch-DLR envelope is same-law and finite at fixed \((N,j)\), but the
current corpus does not prove it in a closing range.

Proof.

It is same-law because every term is read from the actual finite DLR
Hamiltonian of Paper 30 Definition 11.2.  It is finite at fixed \((N,j)\) by
compactness and positivity of the finite heat kernels on admissible charts.

It is not closing for the same structural reason as Paper 30 Sections 55--57.
The heat-kernel range component can be large in the small-time regime, and
the residual component
$$
\operatorname{osc}\Delta_{\mathsf S}V_{RPF}
$$
is exactly a same-law residual value/oscillation theorem.  Papers 26, 29,
30, and 31 prove that this residual oscillation is not supplied by finite
labels, scalar worksheets, or source-response identities alone. `square`

### Corollary 19.6: First Concrete Numerical Target

The first concrete target is now:
$$
\boxed{
\limsup_{(N,j)}
\Omega_{SW}^{DLR,N,j}(B_{HB})
\le \omega
}
$$
for the retained heat-bad source block \(B_{HB}\), with \(\omega\) small
enough that
$$
\epsilon+\sqrt{\omega\chi}<B_A^{rem}.
$$

This is strictly sharper than asking for the whole actual heat-bad matrix:
it asks only for the switch oscillation of the finite DLR Hamiltonian on the
retained heat-bad support.

## 20. Attack On `P32-HKBAD-PRODTHIN`

The second concrete target is product thinness:
$$
P_{\Gamma,bad}^{HK}\widetilde R_\Gamma\widetilde\Sigma_\Gamma
\quad\text{is small in normalized trace norm.}
$$

This is where the heat-bad route either becomes positive or turns into a
floor.

### Definition 20.1: Heat-Mismatch Nondegeneracy

For \(d_*>0\), `P32-HKBAD-HM-NONDEG(d_*)` asserts that on every retained
heat-bad component \(C\),
$$
s_{\min}
\left(
P_C(\widetilde D_\Gamma-D_\Gamma)P_C
\right)
\ge d_*,
$$
where \(s_{\min}\) is the least singular value on the support after quotienting
any declared zero channel.

The point of this definition is to separate two possibilities:

1. the heat-bad mismatch is genuinely nondegenerate, so small heat term means
   small product mass;
2. the mismatch has a null direction, so product mass may hide in that null
   direction and must be treated as a separate selector/floor issue.

### Lemma 20.2: Nondegenerate Heat Mismatch Makes Product Thinness Equivalent To Heat-Term Smallness

Assume `P32-HKBAD-HM-NONDEG(d_*)`.  Then
$$
d_*
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\left\|
P_{\Gamma,bad}^{HK}
\widetilde R_\Gamma\widetilde\Sigma_\Gamma
\right\|_1
\le
E_H^{N,j}.
$$

Together with Lemma 15.2, this gives the two-sided comparison
$$
d_*\tau
\le
E_H
\le
\Delta_D^{bad}\tau
$$
whenever the normalized product mass is \(\tau\).

Proof.

For a matrix \(A\) with least singular value at least \(d_*\),
\(\|AB\|_1\ge d_*\|B\|_1\).  Apply this on each retained heat-bad component
to
\(A=P_C(\widetilde D_\Gamma-D_\Gamma)P_C\) and
\(B=P_C\widetilde R_\Gamma\widetilde\Sigma_\Gamma\), then sum.
The upper bound is Lemma 15.2. `square`

### Proposition 20.3: Product Thinness Is Not A Cosmetic Restatement

Under heat-mismatch nondegeneracy, `P32-HKBAD-PRODTHIN(tau)` is equivalent,
up to explicit heat-mismatch constants, to smallness of the stubborn
heat-bad term \(E_H\).  Therefore it is the sharp positive theorem for the
heat-bad product branch.

Proof.

Lemma 20.2 gives the equivalence.  Since `HK-bad(delta)` means the heat
mismatch is not uniformly small, no heat-weight argument can make \(E_H\)
small unless the product mass itself is small or hidden in a null sector.
`square`

### Proposition 20.4: Current Corpus Does Not Prove Product Thinness

The current corpus does not prove `P32-HKBAD-PRODTHIN(tau)` in a closing
range.

Proof.

The theorem is a bound on
$$
P_{\Gamma,bad}^{HK}
\widetilde R_\Gamma\widetilde\Sigma_\Gamma,
$$
the actual residual/signed product on the heat-bad projection.  Paper 30
classifies the heat-bad projection and the heat weights.  Papers 26 and 29
show that actual residual density values and low-mode conditional weights
are not populated by the current finite labels or RN-ratio identities.
Paper 31 shows that source-response identities do not give smallness.  Thus
product thinness is not proved. `square`

## 21. Response-Only Fallback

If product thinness is too strong, the weaker route is to avoid pointwise
control and bound only the same-law average of the even defect.

### Definition 21.1: Heat-Bad Even-Response Functional

For each heat-bad dual source \(Q\), define
$$
\mathfrak e_{HB}^{N,j}(Q)
:=
\mathbf E_{N,j}^{act}[V_Q^{even}].
$$

This is the exact response of the switch-even component of the heat-bad
source.

### Lemma 21.2: Even-Response Is The Minimal Positive Average Theorem

Assume exact switch law.  Then
$$
\sup_Q|\partial_s\Psi_Q(0)|
=
\sup_Q|\mathfrak e_{HB}^{N,j}(Q)|.
$$

If only `P32-HKBAD-SWQI(omega)` holds, then the odd component may contribute
through the switch RN score, and a sufficient bound is
$$
\sup_Q|\partial_s\Psi_Q(0)|
\le
\sup_Q|\mathfrak e_{HB}^{N,j}(Q)|
+
{\omega\over 2a}
+
{\chi a\over2}
$$
under the same curvature hypothesis as Corollary 12.3.

Proof.

Under exact switch law, the expectation of every switch-odd finite
observable is zero.  Hence only \(V_Q^{even}\) contributes to the first
response.  The quasi-invariant statement is the same source-neutrality
argument as Lemma 12.2 followed by Lemma 1.3. `square`

### Proposition 21.3: Current Corpus Does Not Prove Even-Response Smallness

The current corpus does not prove
$$
\sup_Q|\mathfrak e_{HB}^{N,j}(Q)|\le\epsilon
$$
in a closing range.

Proof.

The functional \(\mathfrak e_{HB}^{N,j}(Q)\) is a same-law expectation of
the exact heat-bad even matrix from Section 13.  It is weaker than pointwise
product thinness, but it still requires actual signed/residual averaging on
the heat-bad projection.  No current Ward identity, Schwinger-Dyson identity,
Peter-Weyl tail theorem, Dobrushin contraction, or finite table in Papers
20--31 evaluates or bounds this average uniformly over trace-dual tests
\(Q\). `square`

## 22. Floor Fork For The Same Object

The same analysis also clarifies the negative route.

### Definition 22.1: Heat-Bad Product Floor

`P32-HKBAD-PRODFLOOR(M)` asserts that the heat-bad product term has a
sign-coherent retained lower bound:
$$
\liminf_{(N,j)}
\left|
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\operatorname{Re}\operatorname{Tr}
\left[
P_{\Gamma,bad}^{HK}
\left(
\widetilde D_\Gamma-D_\Gamma
\right)
\widetilde R_\Gamma\widetilde\Sigma_\Gamma
\right]
\right|
\ge M,
$$
with the same orientation, endpoint, retained-row, and normalization
conventions used by the Branch-A predebit ledger.

### Lemma 22.2: Product Floor Implies Heat-Bad Dual Floor

If `P32-HKBAD-PRODFLOOR(M)` holds, then
`P32-HKBAD-DUALFLOOR(M)` holds up to the already licensed signed-parity and
residual quasi-invariance debits.

Proof.

The product term is one of the three exact components of the heat-bad
source matrix in Section 13.  If its retained sign-coherent contribution is
bounded below and the other two terms are either licensed or subtracted as
debits, the same lower bound is a heat-bad dual floor in the Branch-A
ledger. `square`

### Proposition 22.3: The Floor Is Also Not Sourced

The current corpus proves no `P32-HKBAD-PRODFLOOR(M)` above the Branch-A
budget.

Proof.

Such a theorem is the lower-bound analogue of product thinness.  It requires
actual same-law sign-coherent values of
\(P_{\Gamma,bad}^{HK}(\widetilde D_\Gamma-D_\Gamma)
\widetilde R_\Gamma\widetilde\Sigma_\Gamma\).  The corpus has identified
this object but has not evaluated it. `square`

## 23. Final Result Of The SWQI/Product Pass

### Theorem 23.1: The Next Primitive Target Is Fully Reduced

After attacking the concrete next steps, the heat-bad source problem is
fully reduced to the following same-law finite alternatives.

Positive route:
$$
\mathrm{P32\text{-}HKBAD\text{-}SWQI}(\omega)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}PRODTHIN}(\tau)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi),
$$
plus the already separated signed-parity and residual switch debits, with
total debit fitting below \(B_A^{rem}\).

Weaker positive route:
$$
\mathrm{P32\text{-}HKBAD\text{-}SWQI}(\omega)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}EVENRESP}(\epsilon)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
$$

Negative route:
$$
\mathrm{P32\text{-}HKBAD\text{-}PRODFLOOR}(M).
$$

The current corpus proves none of these in a closing or falsifying range.

Proof.

`SWQI` is exactly the switch DLR Hamiltonian oscillation by Lemma 19.2.
`PRODTHIN` is the sharp pointwise theorem for the nondegenerate heat-bad
product by Lemma 20.2.  `EVENRESP` is the minimal average theorem by Lemma
21.2.  `PRODFLOOR` is the sign-coherent lower alternative by Lemma 22.2.
The current-corpus gaps are Propositions 19.5, 20.4, 21.3, and 22.3.
`square`

### Corollary 23.2: What Would Actually Count As Progress

Further recoupling labels, canonical tags, or source identities will not
move the heat-bad route.  Progress now means one of the following concrete
finite estimates:

1. a small switch-DLR Hamiltonian oscillation
   \(\Omega_{SW}^{DLR,N,j}(B_{HB})\);
2. small heat-bad product mass
   \(P_{\Gamma,bad}^{HK}\widetilde R_\Gamma\widetilde\Sigma_\Gamma\);
3. small heat-bad even response uniformly over trace-dual tests;
4. a sign-coherent product floor.

This is the end of the current positive push inside Paper 32.  The
obstruction is not mysterious anymore: it is the switch oscillation and the
actual same-law product mass on the heat-bad projection.

## 24. The Switch-Oscillation Trap

The previous section identifies `SWQI` as a finite DLR switch-Hamiltonian
oscillation.  We now ask whether the already desired residual
quasi-invariance can source it.  The answer is no: on heat-bad components,
small residual switch variation leaves the heat switch variation exposed.

### Definition 24.1: Heat Switch Oscillation Floor

For the retained heat-bad block \(B_{HB}\), define
$$
\Omega_{HK,SW}^{N,j}(B_{HB})
:=
\operatorname{osc}
\Delta_{\mathsf S}{\mathcal H}_{HK}^{N,j}
$$
on the same retained support used in `P32-HKBAD-SWQI`.

For \(h_*>0\), `P32-HKBAD-HKSW-FLOOR(h_*)` asserts
$$
\liminf_{(N,j)}
\Omega_{HK,SW}^{N,j}(B_{HB})
\ge h_*.
$$

### Lemma 24.2: Heat-Bad Components Force A Heat Switch Floor Unless The Switch Is Heat-Balanced

On any retained heat-bad component on which the recoupling switch exchanges
two heat weights whose logarithmic ratio has liminf at least \(h_*\), the
gate `P32-HKBAD-HKSW-FLOOR(h_*)` holds for that component.

In particular, the Paper-30 singlet/adjoint/two-index diagnostic supplies a
fixed positive heat mismatch on every connected retained component that
contains the two-index obstruction and is kept in the rank-diagonal
singlet/adjoint window.

Proof.

The heat part of the finite DLR Hamiltonian is the negative logarithm of the
heat-kernel weight.  If the switch exchanges two retained channel
contributions with heat weights \(w_\alpha\) and \(w_\beta\), the switch
Hamiltonian difference contains the value
$$
\log {w_\alpha\over w_\beta}.
$$
The oscillation over a support containing both switched values is at least
the absolute logarithmic ratio.  Paper 30 Lemma 132.2 and Lemma 135.4 prove
that the two-index obstruction gives a fixed positive mismatch on the
heat-bad components in the active balance window. `square`

### Definition 24.3: Residual-Jacobian Switch Remainder

Define
$$
Y_{\mathsf S}^{N,j}
:=
\Delta_{\mathsf S}V_{RPF}
-
\Delta_{\mathsf S}\log J_{tree}
-
\log|\det D\mathsf S|.
$$

Then
$$
\Delta_{\mathsf S}{\mathcal H}_B
=
\Delta_{\mathsf S}{\mathcal H}_{HK}
+
Y_{\mathsf S}.
$$

### Lemma 24.4: Small Residual/Jacobian Switch Variation Does Not Source `SWQI`

If `P32-HKBAD-HKSW-FLOOR(h_*)` holds and
$$
\operatorname{osc}Y_{\mathsf S}^{N,j}\le r
$$
cofinally, then every `SWQI` bound must satisfy
$$
\omega\ge h_*-r.
$$

Proof.

For bounded finite functions \(A,B\),
$$
\operatorname{osc}(A+B)
\ge
\operatorname{osc}(A)-\operatorname{osc}(B).
$$
Apply this with
\(A=\Delta_{\mathsf S}{\mathcal H}_{HK}\) and
\(B=Y_{\mathsf S}\). `square`

### Corollary 24.5: Residual Quasi-Invariance Is The Wrong Sign For `SWQI`

On heat-bad components with a positive heat switch floor, proving that
\(Y_{\mathsf S}\) is small does not prove `P32-HKBAD-SWQI(omega)` in a
small range.  It exposes the heat mismatch.

Thus the positive `SWQI` theorem requires a different same-law input:
the residual/Jacobian switch remainder must approximately counter-tilt the
heat switch difference.

### Definition 24.6: Heat-Residual Counter-Tilt

`P32-HKBAD-SWCOUNTER(kappa)` asserts that cofinally
$$
\operatorname{osc}
\left(
\Delta_{\mathsf S}{\mathcal H}_{HK}
+
Y_{\mathsf S}
\right)
\le \kappa
$$
on the retained heat-bad support.

Equivalently, the actual residual/Jacobian switch remainder cancels the heat
switch difference up to oscillation \(\kappa\).

### Lemma 24.7: Counter-Tilt Is Exactly `SWQI`

`P32-HKBAD-SWCOUNTER(kappa)` implies `P32-HKBAD-SWQI(kappa)`.  Conversely,
on the retained chart where the switch is an involutive bijection,
`P32-HKBAD-SWQI(kappa)` is exactly
`P32-HKBAD-SWCOUNTER(kappa)`.

Proof.

This is Lemma 19.2 and the definition
\(\Delta_{\mathsf S}{\mathcal H}_B
=\Delta_{\mathsf S}{\mathcal H}_{HK}+Y_{\mathsf S}\). `square`

### Proposition 24.8: Counter-Tilt Is Not Sourced By The Current Corpus

The current corpus does not prove `P32-HKBAD-SWCOUNTER(kappa)` in a closing
range.

Proof.

The theorem is a quantitative relation between the heat switch mismatch,
which is representation-theoretic, and the actual residual/Jacobian switch
remainder \(Y_{\mathsf S}\).  Papers 26 and 29 prove that the residual
Hamiltonian values are not populated by the current finite labels or RN-ratio
identities.  Paper 30 Sections 55--57 provide finite DLR range envelopes,
but those envelopes bound oscillations separately and do not prove
anti-correlation or counter-tilt.  Paper 31 source-response identities also
do not impose this relation.  Hence the counter-tilt theorem is a genuinely
new same-law value theorem. `square`

## 25. Null-Sector Audit For Product Thinness

Product thinness was compared to heat-term smallness under heat-mismatch
nondegeneracy.  We now close the loophole where the heat mismatch has a null
direction.

### Definition 25.1: Heat-Mismatch Null Product

Let
$$
\Pi_{\ker,\Gamma}^{HK}
$$
be the projection onto the kernel of
$$
P_{\Gamma,bad}^{HK}
\left(
\widetilde D_\Gamma-D_\Gamma
\right)
P_{\Gamma,bad}^{HK}
$$
inside the retained heat-bad component.

Define the normalized null-product mass
$$
N_{prod}^{N,j}
:=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\left\|
\Pi_{\ker,\Gamma}^{HK}
P_{\Gamma,bad}^{HK}
\widetilde R_\Gamma\widetilde\Sigma_\Gamma
\right\|_1.
$$

### Lemma 25.2: Product Thinness Splits Into Nondegenerate And Null Parts

Let \(d_*>0\) be a lower singular-value bound on the complement of
\(\Pi_{\ker,\Gamma}^{HK}\).  Then
$$
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\left\|
P_{\Gamma,bad}^{HK}
\widetilde R_\Gamma\widetilde\Sigma_\Gamma
\right\|_1
$$
is bounded above by
$$
{1\over d_*}E_H^{N,j}
+
N_{prod}^{N,j}
$$
up to the fixed finite projection convention.

Proof.

Decompose the product into the kernel and orthogonal complement of the heat
mismatch.  On the complement, invert the heat mismatch using the singular
value lower bound as in Lemma 20.2.  On the kernel, the heat mismatch gives
no information and the null-product mass remains. `square`

### Proposition 25.3: The Null Product Is Another Same-Law Value Gate

The current corpus does not prove \(N_{prod}^{N,j}\to0\) or any closing
bound for it.

Proof.

The null projection is finite representation data, but the product
\(\widetilde R_\Gamma\widetilde\Sigma_\Gamma\) on that null sector is the
same actual residual/signed product that appears throughout the heat-bad
source route.  No current paper proves its absence, smallness, or
sign-coherent lower floor. `square`

### Corollary 25.4: Product Thinness Is Fully Split

To prove `P32-HKBAD-PRODTHIN(tau)`, one must prove both:

1. small nondegenerate heat-term contribution \(E_H\);
2. small null-product mass \(N_{prod}\).

If the second is large and sign-coherent, the correct route is not positive
thinness but `P32-HKBAD-PRODFLOOR`.

## 26. Response-Only Ward Audit

The weakest positive route is even-response smallness.  Could a Ward or
Schwinger-Dyson identity force it?

### Definition 26.1: Heat-Bad Even Ward Source

`P32-HKBAD-EVEN-WARD(kappa)` asserts that for every heat-bad dual source
\(Q\), the even-response functional admits a finite same-law integration by
parts representation
$$
\mathfrak e_{HB}^{N,j}(Q)
=
\mathbf E_{N,j}^{act}[{\mathcal R}_{Ward,Q}^{N,j}],
$$
with
$$
\sup_Q
\left|
\mathbf E_{N,j}^{act}[{\mathcal R}_{Ward,Q}^{N,j}]
\right|
\le\kappa.
$$

The Ward remainder must be a deterministic finite-record observable under
the actual law.  It is not an auxiliary dynamics.

### Lemma 26.2: Even Ward Sources Even-Response

If `P32-HKBAD-EVEN-WARD(kappa)` holds, then
`P32-HKBAD-EVENRESP(kappa)` holds.

Proof.

This is Definition 26.1 and Definition 21.1. `square`

### Proposition 26.3: Current Corpus Does Not Prove The Even Ward Source

The current corpus does not prove `P32-HKBAD-EVEN-WARD(kappa)` in a closing
range.

Proof.

Papers 30 and 31 identify Ward/Stein routes as legitimate same-law
possibilities, but no paper constructs a bounded inverse or a Ward remainder
for the heat-bad even source family.  The heat-bad even source is precisely
the switch-symmetric part of the residual/signed product on the bad
projection.  A Ward identity for it would be new same-law analytic
information, not a consequence of recoupling labels or source-response
calculus. `square`

## 27. Final Endpoint After The Trap Audit

### Theorem 27.1: `SWQI` Requires Counter-Tilt, Not Residual Neutrality

On heat-bad components with a positive heat switch floor, the route
`P32-HKBAD-SWQI(omega)` cannot be sourced by proving residual/Jacobian switch
variation small.  It requires the stronger counter-tilt theorem
$$
\mathrm{P32\text{-}HKBAD\text{-}SWCOUNTER}(\omega),
$$
which says that the actual residual/Jacobian switch remainder cancels the
heat switch mismatch in oscillation.

Proof.

Lemma 24.4 proves the lower bound when the residual/Jacobian remainder is
small.  Lemma 24.7 proves that the exact positive theorem is counter-tilt.
`square`

### Theorem 27.2: Product Thinness Requires Nondegenerate Control Plus Null-Sector Control

`P32-HKBAD-PRODTHIN(tau)` is equivalent to small heat-term product on the
nondegenerate heat-mismatch complement plus small null-product mass.  The
current corpus proves neither the needed product smallness nor a
sign-coherent product floor.

Proof.

This is Lemma 20.2, Lemma 25.2, Proposition 25.3, and Proposition 22.3.
`square`

### Corollary 27.3: The Truly Live Theorems

After the trap audit, the live heat-bad primitive theorems are:

1. `P32-HKBAD-SWCOUNTER(omega)`: residual/Jacobian counter-tilt cancels the
   heat switch mismatch;
2. `P32-HKBAD-PRODTHIN(tau)` with null-sector control;
3. `P32-HKBAD-EVEN-WARD(kappa)` or another proof of even-response smallness;
4. `P32-HKBAD-PRODFLOOR(M)`.

This is the hardest honest endpoint of the heat-bad route.  The obstruction
is not just "we need values"; it is more structured: either the actual
residual/Jacobian term counter-tilts the heat mismatch, the heat-bad product
has little mass including its null sector, a Ward identity kills the
even-response, or the same object becomes a lower floor.

## 28. Counter-Tilt As An Anti-Heat Residual Atom Equation

The word "counter-tilt" can still sound qualitative.  It is not.  It is an
exact finite equation modulo constants.  This section turns it into a
residual-atom target.

### Lemma 28.1: Oscillation Is Distance From Constants

For a finite real function \(F\) on a retained support,
$$
\operatorname{osc}F\le\kappa
$$
if and only if there exists a constant \(c\) such that
$$
\|F-c\|_\infty\le{\kappa\over2}.
$$

Proof.

Take \(c=(\sup F+\inf F)/2\).  The converse is immediate. `square`

### Definition 28.2: Anti-Heat Residual Switch Equation

Let
$$
K_{\mathsf S}^{HK}
:=
\Delta_{\mathsf S}{\mathcal H}_{HK}
$$
and
$$
Y_{\mathsf S}
:=
\Delta_{\mathsf S}V_{RPF}
-
\Delta_{\mathsf S}\log J_{tree}
-
\log|\det D\mathsf S|.
$$

`P32-HKBAD-ANTIHEAT(omega)` asserts that cofinally, on the retained
heat-bad support, there is a constant \(c_{N,j}\) such that
$$
\left\|
Y_{\mathsf S}
+
K_{\mathsf S}^{HK}
-
c_{N,j}
\right\|_\infty
\le {\omega\over2}.
$$

This says that the residual/Jacobian switch remainder supplies the negative
of the heat switch mismatch, up to a supportwise constant and error
\(\omega/2\).

### Lemma 28.3: Anti-Heat Is Exactly Counter-Tilt

`P32-HKBAD-ANTIHEAT(omega)` is equivalent to
`P32-HKBAD-SWCOUNTER(omega)`.

Proof.

By Definition 24.6,
`SWCOUNTER(omega)` is
$$
\operatorname{osc}
\left(
Y_{\mathsf S}+K_{\mathsf S}^{HK}
\right)
\le\omega.
$$
Apply Lemma 28.1. `square`

### Definition 28.4: Residual Switch Atoms On The Heat-Bad Support

Let \(H_{RPF}^{N,j}\) be the Paper-26 residual Hamiltonian, and let
\(\Phi_A^{N,j}\) be its finite same-law Möbius atoms on a retained template.
For a switch \(\mathsf S\), define
$$
\Delta_{\mathsf S}\Phi_A^{N,j}
:=
\Phi_A^{N,j}\circ\mathsf S-\Phi_A^{N,j}.
$$

Let \({\mathcal A}_{HB}^{sw}\) be the finite family of residual atoms whose
support intersects the retained heat-bad switch block after the already
licensed endpoint, exact-entry, and non-RPF removals.

### Lemma 28.5: Counter-Tilt Is A Residual Atom Sum

Modulo constants and already licensed endpoint/Jacobian terms,
`P32-HKBAD-SWCOUNTER(omega)` requires
$$
\left\|
K_{\mathsf S}^{HK}
+
\sum_{A\in{\mathcal A}_{HB}^{sw}}
\Delta_{\mathsf S}\Phi_A^{N,j}
-
c_{N,j}
\right\|_\infty
\le {\omega\over2}
$$
on the retained heat-bad support.

Proof.

Paper 26 and Paper 29 identify the nonconstant residual Hamiltonian with the
finite Möbius atom sum.  Constants vanish under switch differences and under
oscillation.  Endpoint and exact-entry pieces are already removed or
licensed by the active Branch-A ledger.  Substituting the atom expansion of
the residual/Jacobian switch remainder into Lemma 28.3 gives the displayed
condition. `square`

### Definition 28.6: Anti-Heat Atom Source

`P32-HKBAD-ANTIHEAT-ATOM(omega)` asserts the atom-sum estimate in Lemma 28.5
with the same retained support, constants, and licensed removals.

### Theorem 28.7: `SWCOUNTER` Is Exactly An Anti-Heat Atom Source

After the closed endpoint, exact-entry, and non-RPF removals,
$$
\mathrm{P32\text{-}HKBAD\text{-}SWCOUNTER}(\omega)
$$
is equivalent to
$$
\mathrm{P32\text{-}HKBAD\text{-}ANTIHEAT\text{-}ATOM}(\omega).
$$

Proof.

This is Lemma 28.3 plus Lemma 28.5. `square`

### Proposition 28.8: Current Corpus Does Not Source Anti-Heat Atoms

The current corpus does not prove `P32-HKBAD-ANTIHEAT-ATOM(omega)` in a
closing range.

Proof.

Papers 23, 26, and 29 prove formal residual atoms and their equality with
RPF residual atoms.  They also prove that formal Möbius inversion is not
value population.  The anti-heat theorem requires numerical atom values,
or at least a cofinal uniform approximation of their switched sum to the
negative heat switch mismatch.  No current paper supplies such values,
oscillation bounds, or a Ward identity forcing this relation. `square`

## 29. Small Residual Atoms Falsify Counter-Tilt

The anti-heat formulation also gives a useful negative test.  If all live
residual switch atoms are small, counter-tilt cannot happen on a heat-bad
component with a heat floor.

### Definition 29.1: Residual Switch Atom Envelope

For \(r\ge0\), `P32-HKBAD-SWATOM-SMALL(r)` asserts that cofinally
$$
\left\|
\sum_{A\in{\mathcal A}_{HB}^{sw}}
\Delta_{\mathsf S}\Phi_A^{N,j}
-
c_{N,j}^{R}
\right\|_\infty
\le r
$$
for some constant \(c_{N,j}^{R}\) on the retained heat-bad support.

### Lemma 29.2: Small Residual Atoms Leave The Heat Floor Exposed

If `P32-HKBAD-HKSW-FLOOR(h_*)` and
`P32-HKBAD-SWATOM-SMALL(r)` hold, then every counter-tilt bound satisfies
$$
\omega\ge h_*-2r
$$
up to the already licensed Jacobian and endpoint remainders.

Proof.

By Lemma 28.5, counter-tilt is small only if the atom switch sum cancels the
heat switch mismatch modulo constants.  If the atom switch sum has distance
at most \(r\) from constants, its oscillation contribution can reduce the
heat oscillation by at most \(2r\).  Apply
\(\operatorname{osc}(A+B)\ge\operatorname{osc}(A)-\operatorname{osc}(B)\).
`square`

### Corollary 29.3: Counter-Tilt Requires Large Structured Residual Atoms

On heat-bad components with \(h_*>0\), a positive `SWCOUNTER(omega)` theorem
with \(\omega\ll h_*\) requires residual atoms whose switched sum has
order-\(h_*\) anti-heat structure.  It is not enough for residual atoms to be
small, local, endpoint-additive, or generic.

## 30. Tension Between Counter-Tilt And Product Thinness

The positive heat-bad route now asks for two different things:

1. residual atoms must be large and structured enough to counter-tilt the
   heat mismatch in the switch RN oscillation;
2. the residual/signed product must be small enough on the heat-bad
   projection to satisfy product thinness or even-response.

These are not logically contradictory, but they are a real fine-tuning
requirement.

### Definition 30.1: Counter-Tilt/Product Compatibility

`P32-HKBAD-CT-PROD-COMP(omega,tau)` asserts that the same actual residual
atom family simultaneously satisfies:

1. `P32-HKBAD-ANTIHEAT-ATOM(omega)`;
2. `P32-HKBAD-PRODTHIN(tau)`, including null-sector control.

### Lemma 30.2: Compatibility Is Sufficient For The Positive Heat-Bad Branch

Assume the signed-parity and residual-switch debits already separated in
Section 13 are paid by \(\epsilon_\Sigma\) and \(\epsilon_R\).  If
`P32-HKBAD-CT-PROD-COMP(omega,tau)` and
`P32-HKBAD-SRC-CURV(a,chi)` hold, then the heat-bad contribution is bounded
by
$$
\epsilon_\Sigma+\epsilon_R+\Delta_D^{bad}\tau
+
{\omega\over2a}
+
{\chi a\over2},
$$
up to the null-sector convention of Section 25.

Proof.

The product-thinness term bounds the heat-bad product contribution by Lemma
15.2 and Section 25.  The anti-heat atom term is `SWCOUNTER`, hence `SWQI`,
by Theorem 28.7 and Lemma 24.7.  Insert the `SWQI` debit into Corollary
12.3 and add the already separated signed/residual debits. `square`

### Proposition 30.3: Compatibility Is Not Sourced By The Current Corpus

The current corpus does not prove
`P32-HKBAD-CT-PROD-COMP(omega,tau)` in a closing range.

Proof.

The first clause is the anti-heat atom source of Theorem 28.7.  The second
clause is product thinness with null-sector control from Theorem 27.2.  Each
is unsourced separately.  No current theorem correlates them on the same
actual residual atom family. `square`

## 31. Final Endpoint After The Anti-Heat Pass

### Theorem 31.1: The Live Positive Theorem Is Compatibility, Not A Single Estimate

The positive heat-bad route now requires a compatibility theorem:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}CT\text{-}PROD\text{-}COMP}
(\omega,\tau)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
}
$$

Equivalently, the same actual residual atom family must both:

1. counter-tilt the heat switch mismatch; and
2. leave small residual/signed product mass on the heat-bad projection.

The current corpus does not prove this compatibility theorem.

Proof.

The necessity of counter-tilt is Theorem 27.1 and Theorem 28.7.  The product
thinness/null-sector requirement is Theorem 27.2.  The sufficient combined
bound is Lemma 30.2.  The current-corpus non-derivation is Proposition 30.3.
`square`

### Corollary 31.2: What Would Be A Genuine Breakthrough Here

A real positive breakthrough inside this route would be one of:

1. a same-law anti-heat atom theorem proving that residual atoms cancel the
   heat switch mismatch on heat-bad components;
2. a same-law product-thinness theorem proving that the same atoms do not
   carry product mass after the signed/residual projection;
3. a structural theorem explaining why both are compatible, for example a
   Ward identity whose exact divergence produces counter-tilt while its
   transverse component cancels in the product source;
4. a sign-coherent product floor proving that this route is impossible and
   adaptive Branch A is falsified.

This is the sharpest current endpoint.  It is creative in the right sense:
the impossible value table has become a precise anti-heat residual atom
equation plus a product compatibility test.  But it is still a primitive
same-law analytic theorem, not a consequence of the existing bookkeeping.

## 32. Compatibility Geometry: The Product-Visible Quotient

We can now make the compatibility test finite and sharp.  The question is
whether the anti-heat residual atom field can be hidden from the product
seminorm.  If yes, the positive route remains plausible.  If no, counter-tilt
forces product mass.

### Definition 32.1: Heat-Bad Residual Atom Field Space

For fixed \((N,j)\), let
$$
{\mathcal V}_{HB}^{N,j}
$$
be the finite real vector space spanned by the switched residual atom sums
$$
X
=
\sum_{A\in{\mathcal A}_{HB}^{sw}}
\Delta_{\mathsf S}\Phi_A^{N,j}
$$
restricted to the retained heat-bad support.

Let
$$
{\mathcal C}_{HB}^{N,j}
$$
be the subspace of constants plus already licensed endpoint, Jacobian, and
non-RPF remainders.  Define the quotient
$$
\overline{\mathcal V}_{HB}^{N,j}
:=
{\mathcal V}_{HB}^{N,j}/{\mathcal C}_{HB}^{N,j}.
$$

The heat switch mismatch determines a target class
$$
\mathfrak k_{HB}^{N,j}
:=
\left[
K_{\mathsf S}^{HK}
\right]
\in
\overline{\mathcal V}_{HB}^{N,j}
$$
whenever it lies in the same retained observable span, and otherwise in the
finite ambient quotient generated by adjoining \(K_{\mathsf S}^{HK}\).

### Definition 32.2: Product Seminorm On The Quotient

For a quotient class \([X]\), define
$$
\|[X]\|_{prod}
:=
\inf_{C\in{\mathcal C}_{HB}^{N,j}}
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma {1\over2}
\left\|
P_{\Gamma,bad}^{HK}
\widetilde R_\Gamma(X+C)
\widetilde\Sigma_\Gamma
\right\|_1,
$$
where \(\widetilde R_\Gamma(X+C)\) denotes the residual/Jacobian product
induced by the atom field \(X+C\) in the retained heat-bad source block.

This is a seminorm because product-null directions may exist.

### Definition 32.3: Anti-Heat Product Distance

For \(\omega\ge0\), define
$$
d_{prod}^{N,j}(\omega)
:=
\inf
\left\{
\|[X]\|_{prod}
:
\|[X]+\mathfrak k_{HB}^{N,j}\|_{\infty,quot}
\le {\omega\over2}
\right\}.
$$

Here \(\|\cdot\|_{\infty,quot}\) is the quotient \(L^\infty\)-distance modulo
constants and already licensed remainders.

### Lemma 32.4: Compatibility Is Exactly Small Anti-Heat Product Distance

`P32-HKBAD-CT-PROD-COMP(omega,tau)` holds if and only if cofinally
$$
d_{prod}^{N,j}(\omega)\le \tau
$$
with the same retained support and null-sector conventions.

Proof.

The constraint
$$
\|[X]+\mathfrak k_{HB}^{N,j}\|_{\infty,quot}\le{\omega\over2}
$$
is exactly the anti-heat atom equation of Theorem 28.7.  The objective
\(\|[X]\|_{prod}\) is exactly the product-thinness mass on the same residual
atom field, quotienting the already licensed directions.  Taking the
infimum is the finite compatibility problem. `square`

### Definition 32.5: Hidden Anti-Heat Direction

`P32-HKBAD-HIDDEN-ANTIHEAT(omega,tau)` asserts that cofinally
$$
d_{prod}^{N,j}(\omega)\le\tau.
$$

This is not a new theorem distinct from compatibility.  It is the geometric
normal form of compatibility: the anti-heat target must be close to a
product-null or product-small direction.

### Corollary 32.6: Positive Route In Geometric Form

The positive route closes if
`P32-HKBAD-HIDDEN-ANTIHEAT(omega,tau)` and
`P32-HKBAD-SRC-CURV(a,chi)` hold with
$$
\epsilon_\Sigma+\epsilon_R+\Delta_D^{bad}\tau
+
{\omega\over2a}
+
{\chi a\over2}
<
B_A^{rem}.
$$

Proof.

Use Lemma 32.4 in Lemma 30.2. `square`

## 33. Product-Visible Heat Gives A No-Go Test

The same geometry also gives a way to falsify the positive route.

### Definition 33.1: Product Visibility Of The Heat Target

For \(c_{vis}>0\) and \(h_*>0\),
`P32-HKBAD-VISHEAT(c_vis,h_*)` asserts that cofinally every quotient class
\([X]\) satisfying
$$
\|[X]+\mathfrak k_{HB}^{N,j}\|_{\infty,quot}
\le {h_*\over4}
$$
also satisfies
$$
\|[X]\|_{prod}\ge c_{vis}h_*.
$$

In words: any residual atom field capable of counter-tilting a positive
heat mismatch is visible to the product seminorm.

### Lemma 33.2: Visibility Gives Incompatibility Below Threshold

If `P32-HKBAD-VISHEAT(c_vis,h_*)` holds and
\(\omega\le h_*/2\), then
$$
d_{prod}^{N,j}(\omega)\ge c_{vis}h_*
$$
cofinally.  Hence `P32-HKBAD-CT-PROD-COMP(omega,tau)` is impossible whenever
$$
\tau<c_{vis}h_*.
$$

Proof.

If \(\omega\le h_*/2\), then the anti-heat constraint gives quotient error
at most \(h_*/4\).  Apply Definition 33.1. `square`

### Definition 33.3: Product-Visible Floor

`P32-HKBAD-VISPROD-FLOOR(M)` asserts that the product-visible component in
Definition 33.1 is sign-coherent in the Branch-A retained ledger and has
lower bound \(M\).

### Lemma 33.4: Visible Product Floor Falsifies The Positive Heat-Bad Route

If `P32-HKBAD-VISPROD-FLOOR(M)` holds with \(M>B_A^{rem}\), then the
positive heat-bad Branch-A route cannot absorb the heat-bad sector.

Proof.

This is the product-floor theorem of Section 22 applied to the visible
component forced by counter-tilt.  Sign coherence promotes product mass to a
retained lower floor. `square`

### Proposition 33.5: Current Corpus Proves Neither Hidden Nor Visible Heat

The current corpus proves neither
`P32-HKBAD-HIDDEN-ANTIHEAT(omega,tau)` in a closing range nor
`P32-HKBAD-VISHEAT(c_vis,h_*)` with a sign-coherent floor.

Proof.

Both statements require the finite product seminorm of the actual switched
residual atom fields on the heat-bad support.  Papers 23, 26, and 29 prove
the formal atom identity but not atom values.  Paper 30 prints the finite DLR
representation and range envelopes but not the product-null geometry of the
actual residual atom span.  Paper 31 proves source-response identities but
not these quotient distances.  Therefore neither the hidden-direction
positive theorem nor the visible-floor negative theorem is sourced. `square`

## 34. Final Endpoint After The Compatibility Geometry

### Theorem 34.1: Branch-A Heat-Bad Compatibility Is A Finite Quotient-Distance Problem

The positive heat-bad route is now equivalent to proving a finite quotient
distance estimate:
$$
\boxed{
d_{prod}^{N,j}(\omega)\le\tau
}
$$
cofinally, together with the source curvature bound and the already separated
signed/residual debits.

The negative route is to prove product visibility and sign coherence:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}VISHEAT}(c_{vis},h_*)
\quad+\quad
\mathrm{P32\text{-}HKBAD\text{-}VISPROD\text{-}FLOOR}(M).
}
$$

Proof.

The positive equivalence is Lemma 32.4 and Corollary 32.6.  The negative
route is Lemma 33.2 and Lemma 33.4. `square`

### Corollary 34.2: What To Compute Next

The next concrete finite worksheet is not another row label table.  It is
the product-visible quotient worksheet:

1. construct \(\overline{\mathcal V}_{HB}^{N,j}\);
2. print the heat target class \(\mathfrak k_{HB}^{N,j}\);
3. print or bound the product seminorm \(\|\cdot\|_{prod}\);
4. compute or bound the distance \(d_{prod}^{N,j}(\omega)\);
5. if the distance is too large, test sign coherence for
   `P32-HKBAD-VISPROD-FLOOR`.

This is the most compressed form of the obstruction currently available.
It makes the Feynman-style change of viewpoint precise: stop asking for the
whole law, and ask whether the anti-heat direction is hidden from the
product seminorm of the actual residual atom geometry.

## 35. The Quotient-Distance Worksheet As A Finite Convex Program

The quotient-distance formulation is useful only if it can be made into a
finite, auditable row calculation.  This section fixes that calculation.

Fix a retained row \((N,j)\), a Peter-Weyl cutoff \(L\), and the heat-bad
support convention already used in Papers 30 and 31.  Let
$$
{\mathcal A}_{HB}^{N,j,L}
$$
be the finite set of switched residual atom labels retained in the row.  An
atom field is a vector
$$
x=(x_\alpha)_{\alpha\in{\mathcal A}_{HB}^{N,j,L}}
$$
in the finite real vector space \(E_{HB}^{N,j,L}\).

The licensed directions form a finite subspace
$$
C_{HB}^{N,j,L}\subset E_{HB}^{N,j,L}
$$
generated by:

1. constants;
2. endpoint-normalization directions;
3. already licensed Jacobian directions;
4. non-RPF remainders;
5. source directions whose debit has already been charged in Papers 30 and
   31.

Let
$$
Q_{HB}^{N,j,L}:E_{HB}^{N,j,L}\to
\overline E_{HB}^{N,j,L}:=
E_{HB}^{N,j,L}/C_{HB}^{N,j,L}
$$
be the quotient map, and let
$$
k_{HB}^{N,j,L}:=Q_{HB}^{N,j,L}K_{\mathsf S}^{HK}
$$
be the finite heat target vector.

### Definition 35.1: Finite Product Seminorm Matrix Data

For each retained polymer/product block \(\Gamma\), define the finite linear
operator
$$
A_\Gamma^{N,j,L}:E_{HB}^{N,j,L}\to{\mathcal T}_\Gamma^{N,j,L}
$$
by
$$
A_\Gamma^{N,j,L}x
:=
P_{\Gamma,bad}^{HK}\,
\widetilde R_\Gamma(x)\,
\widetilde\Sigma_\Gamma .
$$

The row product seminorm is
$$
p_{N,j,L}(Qx)
:=
\inf_{c\in C_{HB}^{N,j,L}}
\sum_\Gamma w_\Gamma^{N,j,L}
{1\over2}
\left\|
A_\Gamma^{N,j,L}(x+c)
\right\|_1,
$$
where
$$
w_\Gamma^{N,j,L}:={1\over Z_B^{N,j}(\eta)}
$$
with the same row normalization as Definition 32.2.

This is exactly \(\|\cdot\|_{prod}\) on the finite cutoff row.

### Definition 35.2: Finite Quotient Distance

For \(\omega\ge0\), define
$$
d_{prod}^{N,j,L}(\omega)
:=
\inf
\left\{
p_{N,j,L}(Qx):
\|Qx+k_{HB}^{N,j,L}\|_{\infty,quot}
\le{\omega\over2}
\right\}.
$$

The cofinal distance in Definition 32.3 is sourced by a cutoff scheme if
$$
\limsup_{L\to\infty}d_{prod}^{N,j,L}(\omega)
\le d_{prod}^{N,j}(\omega)
$$
with no loss beyond the already licensed Peter-Weyl tail.

### Lemma 35.3: The Finite Distance Is A Convex Program

At fixed \((N,j,L)\), \(d_{prod}^{N,j,L}(\omega)\) is the value of a finite
convex optimization problem.  If the retained matrices are printed with
rational interval entries, then both upper and lower certificates are
finitely checkable.

Proof.

The constraint
$$
\|Qx+k_{HB}^{N,j,L}\|_{\infty,quot}
\le{\omega\over2}
$$
is a finite family of linear inequalities after choosing a quotient gauge.
For each \(\Gamma\), the map \(x\mapsto A_\Gamma^{N,j,L}x\) is linear and
the trace norm is convex.  Hence the objective is convex, and the infimum
over the finite licensed subspace \(C_{HB}^{N,j,L}\) is still convex.

For checkability, represent each trace-norm bound by the standard Hermitian
dilation:
$$
\|M\|_1\le t
\quad\Longleftrightarrow\quad
\exists U,V\succeq0:
\begin{pmatrix}
U & M\\
M^* & V
\end{pmatrix}\succeq0,\qquad
{1\over2}\operatorname{tr}(U+V)\le t .
$$
Thus a rational interval upper certificate consists of \(x,c,U_\Gamma,V_\Gamma\)
and slack margins; a lower certificate is a dual feasible functional.  Every
entry is finite. `square`

## 36. Positive Certificate: Hidden Anti-Heat

### Definition 36.1: `P32-HKBAD-QDIST-UP(omega,tau,L,delta)`

`P32-HKBAD-QDIST-UP(omega,tau,L,delta)` asserts that the row admits explicit
finite data \(x,c,\{U_\Gamma,V_\Gamma\}_\Gamma\) such that:

1. \(c\in C_{HB}^{N,j,L}\);
2. the anti-heat constraint holds with margin:
   $$
   \|Q(x+c)+k_{HB}^{N,j,L}\|_{\infty,quot}
   \le{\omega\over2}-\delta;
   $$
3. for every \(\Gamma\),
   $$
   \begin{pmatrix}
   U_\Gamma & A_\Gamma^{N,j,L}(x+c)\\
   A_\Gamma^{N,j,L}(x+c)^* & V_\Gamma
   \end{pmatrix}\succeq0;
   $$
4. the product objective obeys
   $$
   \sum_\Gamma w_\Gamma^{N,j,L}
   {1\over4}\operatorname{tr}(U_\Gamma+V_\Gamma)
   \le \tau-\delta .
   $$

### Lemma 36.2: Upper Certificate Sources Hidden Anti-Heat

If `P32-HKBAD-QDIST-UP(omega,tau,L,delta)` holds cofinally and the
Peter-Weyl tail is already licensed below \(\delta\), then
`P32-HKBAD-HIDDEN-ANTIHEAT(omega,tau)` holds.

Proof.

The certificate gives a feasible point for the finite quotient-distance
program with objective at most \(\tau-\delta\).  The cutoff tail uses at most
\(\delta\), by hypothesis, and the licensed directions are killed by the
quotient.  Therefore \(d_{prod}^{N,j}(\omega)\le\tau\) cofinally. `square`

### Remark 36.3: Why This Is Barandes-Aligned

The certificate is not a hidden Markov assumption.  It uses only:

1. actual row atom fields;
2. deterministic finite source transformations;
3. exact quotienting of licensed directions;
4. finite trace-norm inequalities.

There is no inserted stochastic time process and no conditional independence
postulate.  The record law remains the actual pushed-forward SEL/RPF law.

## 37. Negative Certificate: Product Visibility And Floor

The same finite program has a dual certificate.  This is the clean way to
prove that anti-heat is impossible without paying product mass.

### Definition 37.1: Dual Product Functional

A dual product functional is a linear functional
$$
\Lambda:\overline E_{HB}^{N,j,L}\to\mathbb R
$$
such that
$$
|\Lambda(Qx)|\le p_{N,j,L}(Qx)
$$
for every \(x\in E_{HB}^{N,j,L}\).

It is heat-visible at level \(h_*\) if
$$
|\Lambda(k_{HB}^{N,j,L})|\ge h_* .
$$

### Lemma 37.2: Dual Visibility Lower Bound

If there is a dual product functional \(\Lambda\) with
\(|\Lambda(k_{HB}^{N,j,L})|\ge h_*\), then for every feasible anti-heat field
with
$$
\|Qx+k_{HB}^{N,j,L}\|_{\infty,quot}\le {h_*\over4\|\Lambda\|_{\infty,*}},
$$
one has
$$
p_{N,j,L}(Qx)\ge {3h_*\over4}.
$$

Proof.

By dual feasibility,
$$
p_{N,j,L}(Qx)\ge |\Lambda(Qx)|.
$$
Also
$$
\Lambda(Qx)
=-\Lambda(k_{HB}^{N,j,L})
+\Lambda(Qx+k_{HB}^{N,j,L}).
$$
The second term is bounded by the quotient \(L^\infty\) error times
\(\|\Lambda\|_{\infty,*}\).  The stated constraint makes this error at most
\(h_*/4\).  Hence \(p_{N,j,L}(Qx)\ge 3h_*/4\). `square`

### Definition 37.3: `P32-HKBAD-QDIST-DUAL-FLOOR(M,L,delta)`

`P32-HKBAD-QDIST-DUAL-FLOOR(M,L,delta)` asserts that a dual product functional
\(\Lambda\) exists with:

1. dual feasibility margin \(\delta\);
2. heat visibility margin \(\delta\);
3. sign coherence with the Branch-A retained ledger;
4. induced product floor at least \(M+\delta\).

### Lemma 37.4: Dual Floor Falsifies The Positive Route

If `P32-HKBAD-QDIST-DUAL-FLOOR(M,L,delta)` holds cofinally, the Peter-Weyl tail
is licensed below \(\delta\), and \(M>B_A^{rem}\), then the positive heat-bad
route is falsified.

Proof.

Dual feasibility gives product visibility.  Sign coherence turns the visible
product mass into a retained lower floor.  Since the floor exceeds the
remaining Branch-A budget, it cannot be absorbed. `square`

## 38. Row-Decidability Theorem

### Theorem 38.1: Fixed-Row Heat-Bad Compatibility Is Certificate-Decidable

At fixed \((N,j,L)\), exactly one of the following three outcomes can be
reported by a finite certificate search to any prescribed rational tolerance
\(\varepsilon>0\):

1. an upper certificate proving
   $$
   d_{prod}^{N,j,L}(\omega)\le\tau+\varepsilon;
   $$
2. a dual lower certificate proving
   $$
   d_{prod}^{N,j,L}(\omega)\ge\tau-\varepsilon;
   $$
3. an explicit undecided interval of width at most \(2\varepsilon\).

Moreover, if the interval lies wholly below the Branch-A budget after the
curvature and tail debits, the positive route closes at that row.  If it lies
wholly above a sign-coherent product floor exceeding \(B_A^{rem}\), the
positive route is falsified at that row.

Proof.

The finite quotient-distance program is convex and finite-dimensional by
Lemma 35.3.  Standard primal-dual separation gives approximate upper and
lower certificates for the optimum whenever the row matrices and quotient
maps are printed with rational intervals.  The only non-row issue is the
cofinal cutoff tail; this is already separated as a Peter-Weyl tail debit.
Thus the fixed-row problem is certificate-decidable to any rational tolerance.
The two consequences follow by Corollary 32.6 and Lemma 37.4. `square`

### Corollary 38.2: What Is Still Missing

Paper 32 has not proved a closing upper or lower certificate.  It has proved
that no further naming of finite labels is needed.  The missing object is
concrete:

1. print \(E_{HB}^{N,j,L}\), \(C_{HB}^{N,j,L}\), and \(Q_{HB}^{N,j,L}\);
2. print the heat target vector \(k_{HB}^{N,j,L}\);
3. print the operators \(A_\Gamma^{N,j,L}\);
4. solve or bound the finite quotient-distance program;
5. lift the row certificate through the already licensed tail.

That is the next live mathematical/computational theorem.  It either finds
the hidden anti-heat direction or proves that heat is product-visible and
therefore becomes a floor obstruction.

## 39. The Row-Print Theorem

Corollary 38.2 names five tasks.  The first thing to settle is whether those
tasks are a disguised request for the whole adaptive law, or whether they are
a smaller finite same-law data problem.  The answer is smaller.

### Definition 39.1: Heat-Bad Quotient Rowprint

For a cutoff row \((N,j,L)\), `P32-HKBAD-ROWPRINT(N,j,L,epsilon_data)`
asserts that the following finite interval data are printed with total
operator-entry uncertainty at most \(\epsilon_{data}\):

1. the retained atom label set
   $$
   {\mathcal A}_{HB}^{N,j,L};
   $$
2. a basis for the atom vector space
   $$
   E_{HB}^{N,j,L};
   $$
3. a generating matrix for the licensed subspace
   $$
   C_{HB}^{N,j,L};
   $$
4. a quotient gauge, equivalently a finite matrix for
   $$
   Q_{HB}^{N,j,L}:E_{HB}^{N,j,L}\to\overline E_{HB}^{N,j,L};
   $$
5. the heat target vector
   $$
   k_{HB}^{N,j,L}=Q_{HB}^{N,j,L}K_{\mathsf S}^{HK};
   $$
6. the product operators
   $$
   A_\Gamma^{N,j,L}:E_{HB}^{N,j,L}\to{\mathcal T}_\Gamma^{N,j,L};
   $$
7. the normalization weights \(w_\Gamma^{N,j,L}\);
8. a Peter-Weyl omitted-mode tail bound for every entry that is not retained.

This is the exact data needed by the finite convex program of Section 35.
It is not a request for all conditional probabilities.  It is a request for
the quotient-visible coordinates of the actual heat-bad residual atom field.

### Definition 39.2: Rowprint Construction Map

Define the deterministic construction map
$$
\mathfrak R_{HB}^{N,j,L}
:
\left(
\Phi_A^{N,j},
K_{\mathsf S}^{HK},
P_{\Gamma,bad}^{HK},
\Sigma_\Gamma,
\mathcal L_{closed}
\right)
\longmapsto
\left(
E,C,Q,k,A_\Gamma,w_\Gamma
\right)
$$
as follows.

1. `Atom support`: take \({\mathcal A}_{HB}^{N,j,L}\) to be the retained
   Paper-26/Paper-29 residual atom supports that enter the Paper-30 heat-bad
   full-block projection.
2. `Vector space`: let \(E\) be the real span of those atom-coordinate
   functions.
3. `Licensed subspace`: let \(C\) be the span of constants, exact-entry
   central quotient rows, endpoint-normalization rows, Jacobian rows already
   paid in the Paper-30 ledger, and the Paper-31 source rows already charged.
4. `Quotient`: compute \(Q\) by finite row reduction of the generator matrix
   of \(C\).
5. `Heat target`: project the finite heat switch mismatch \(K_{\mathsf S}^{HK}\)
   through \(Q\).
6. `Product operators`: for each \(\Gamma\), insert each atom basis vector into
   the retained residual/Jacobian product slot and project by
   \(P_{\Gamma,bad}^{HK}\), giving the columns of \(A_\Gamma\).
7. `Weights`: import \(w_\Gamma=1/Z_B^{N,j}(\eta)\) from the same normalized
   block ledger.

Every operation is finite once the atom values and residual/Jacobian product
entries are available as same-law intervals.

### Lemma 39.3: Rowprint Is Strictly Weaker Than Full Atom Population

`P32-HKBAD-ROWPRINT(N,j,L,epsilon_data)` is implied by the Paper-26 primitive
residual source package on a template containing the heat-bad row, but it is
strictly weaker than full `P26-ACTATOM-POP`.

Proof.

The implication is direct: `P26-ACTATOM-POP` prints all active atom values on
the chosen finite template, so in particular it prints the atom values that
survive the heat-bad quotient and product projection.  The structural pieces
\(P_{\Gamma,bad}^{HK}\), \(\Sigma_\Gamma\), and the licensed ledger are
already finite Paper-30/Paper-31 data.  The construction map
\(\mathfrak R_{HB}^{N,j,L}\) then prints \(E,C,Q,k,A_\Gamma,w_\Gamma\).

The converse fails because `ROWPRINT` discards every atom coordinate killed
by the quotient and every atom coordinate invisible to the heat-bad product
operators.  Full atom population also asks for conditional rows, Dobrushin
rows, bridge rows, and unrelated Peter-Weyl projections.  Therefore rowprint
is a narrower theorem. `square`

### Theorem 39.4: Rowprint Plus One Certificate Settles The Row

Assume `P32-HKBAD-ROWPRINT(N,j,L,epsilon_data)` and an omitted-mode tail
bound \(\epsilon_{tail}\).

1. If the printed intervals admit `P32-HKBAD-QDIST-UP(omega,tau,L,delta)`
   with
   $$
   \epsilon_{data}+\epsilon_{tail}<\delta,
   $$
   then the positive heat-bad row closes.
2. If the printed intervals admit
   `P32-HKBAD-QDIST-DUAL-FLOOR(M,L,delta)` with
   $$
   \epsilon_{data}+\epsilon_{tail}<\delta
   \quad\text{and}\quad
   M>B_A^{rem},
   $$
   then the positive heat-bad row is falsified by a floor.

Proof.

The rowprint supplies the finite matrices of Section 35 with interval
uncertainty.  If the certificate margin exceeds the interval and tail error,
the certified inequality survives interval widening and cutoff lifting.
The positive case is Lemma 36.2.  The negative case is Lemma 37.4. `square`

## 40. What The Existing Corpus Already Prints

The rowprint theorem separates structural data from actual same-law values.
This matters: most of the rowprint is already closed.

### Proposition 40.1: Structural Rowprint Is Closed

For every fixed \((N,j,L)\), the current corpus prints the following
structural pieces of `P32-HKBAD-ROWPRINT`:

1. the heat-bad component classifier \(P_{\Gamma,bad}^{HK}\) from Paper 30;
2. the heat switch mismatch \(K_{\mathsf S}^{HK}\);
3. the formal residual atom supports from Papers 23, 26, and 29;
4. the licensed subspace generated by constants, exact-entry central
   quotients, endpoint rows, and already charged Jacobian/source rows;
5. the quotient construction \(Q\), once the finite generators are listed;
6. the block normalization convention \(w_\Gamma=1/Z_B^{N,j}(\eta)\).

Proof.

Paper 30 Sections 135--147 print the heat-bad projection, exact heat-bad
debit, and source-response form of the heat-bad object.  Paper 26 imports
the formal residual atom identity and proves finite atom existence.  Paper 29
identifies the primitive residual atoms with the literal RPF residual atoms
after the same central-entry quotient.  The licensed directions are precisely
the directions already charged before Paper 32 begins.  Row reduction is a
finite algebraic operation on the printed generators. `square`

### Proposition 40.2: Numerical Product Rowprint Is Not Closed

The current corpus does not print the product operator intervals
\(A_\Gamma^{N,j,L}\) sharply enough to decide the quotient-distance program
in a closing or falsifying range.

Proof.

The columns of \(A_\Gamma\) require the actual residual/Jacobian product
response of each retained atom basis vector on the heat-bad projection.
Paper 26 proves that formal Möbius atom existence is not numerical atom
population.  Paper 29 proves that primitive residual atoms and literal RPF
atoms are the same nonconstant atoms, but that their values remain
unpopulated.  Paper 30 proves that the heat-bad projection is finite and
that representation data alone do not bound the actual signed/residual mass
on that projection.  Therefore the structural rowprint is closed, but the
actual product-entry rowprint is not. `square`

### Corollary 40.3: The New Primitive Is Smaller Than Before

The next primitive theorem is not full adaptive-law reconstruction.  It is
the narrower rowprint value theorem:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}PRODENTRY}
(L,\epsilon_{data})
}
$$
which asserts that the entries of the finitely many heat-bad product
operators \(A_\Gamma^{N,j,L}\), after quotienting licensed directions, are
printed with uncertainty \(\epsilon_{data}\).

It can be sourced in two ways:

1. directly, by computing the actual heat-bad residual/Jacobian product
   entries;
2. indirectly, by proving a source-response identity that bounds the same
   entries without listing them one by one.

The second route is the only route that looks meaningfully more imaginative
than the original atom-value table.

## 41. Direct Product-Entry Source And Its No-Go Boundary

### Definition 41.1: `P32-HKBAD-PRODENTRY(L,epsilon_data)`

`P32-HKBAD-PRODENTRY(L,epsilon_data)` asserts that cofinally, for every
retained \(\Gamma\) and every basis atom \(e_\alpha\in E_{HB}^{N,j,L}\), the
actual matrix
$$
A_\Gamma^{N,j,L}e_\alpha
$$
is printed as a rational interval matrix of total trace-norm uncertainty at
most \(\epsilon_{data}\), after all licensed quotient directions are removed.

### Lemma 41.2: Product Entries Source Rowprint

Structural rowprint plus `P32-HKBAD-PRODENTRY(L,epsilon_data)` implies
`P32-HKBAD-ROWPRINT(N,j,L,epsilon_data)`.

Proof.

By Proposition 40.1 all non-product structural data are already printed.
The only missing data are the columns of \(A_\Gamma\), and those are exactly
the product-entry intervals. `square`

### Proposition 41.3: Current-Corpus No-Go For Direct Product Entries

The current corpus does not prove `P32-HKBAD-PRODENTRY(L,epsilon_data)` with
\(\epsilon_{data}\) in any closing or falsifying range.

Proof.

If `P32-HKBAD-PRODENTRY` were available with closing precision, then the
finite quotient-distance program could be run and would produce either an
upper certificate, a lower certificate, or a narrow undecided interval by
Theorem 38.1.  But Paper 26 proves that actual residual atom values are not
populated by formal Möbius inversion; Paper 30 proves that heat-bad
signed/residual product mass is not determined by representation data; and
Paper 31 proves source-response identities but not the required source
curvature/neutrality constants.  Hence direct product-entry population is a
new same-law quantitative theorem, not a consequence of the current corpus.
`square`

## 42. Indirect Source: Quotient-Response Certificate

The direct route asks for matrix entries.  The more promising route asks only
for their action on the finite dual cone of the quotient-distance program.

### Definition 42.1: `P32-HKBAD-QRESP(L,epsilon_data)`

`P32-HKBAD-QRESP(L,epsilon_data)` asserts that for every dual product
functional \(\Lambda\) appearing in the finite quotient-distance dual search,
the same-law source pressure
$$
\Psi_\Lambda^{N,j}(s)
:=
\log \mathbf E_{N,j}^{act}
\left[
\exp(sV_\Lambda^{N,j})
\right]
$$
has a certified first response at \(s=0\) with error at most
\(\epsilon_{data}\), where \(V_\Lambda^{N,j}\) is the deterministic finite
observable obtained by pairing \(\Lambda\) with the heat-bad quotient product
slot.

### Lemma 42.2: Quotient Response Sources The Dual Side

If `P32-HKBAD-QRESP(L,epsilon_data)` holds, then every dual lower certificate
used in `P32-HKBAD-QDIST-DUAL-FLOOR` can be checked without printing all
columns of \(A_\Gamma\).

Proof.

A dual certificate uses \(A_\Gamma\) only through the paired functionals
\(\Lambda(A_\Gamma e_\alpha)\) and the heat target pairing
\(\Lambda(k_{HB})\).  These are exactly first responses of deterministic
finite source observables \(V_\Lambda\) under the actual row law.  Thus
certified responses replace explicit matrix-column values for the dual
search. `square`

### Lemma 42.3: Quotient Response Also Gives A Targeted Upper Search

If the upper certificate ansatz is restricted to a finite-dimensional
candidate family \(X_\theta\), then `P32-HKBAD-QRESP(L,epsilon_data)` applied
to the finite polar tests of that family checks the upper certificate without
printing the full \(A_\Gamma\).

Proof.

For a fixed candidate family, the trace-norm objective is the supremum over
polar dual tests evaluated on \(A_\Gamma X_\theta\).  Since the family is
finite-dimensional and the certificate uses finitely many rational interval
tests, quotient responses evaluate precisely the required pairings. `square`

### Proposition 42.4: The Best Next Positive Attack

The best next positive theorem is not full product-entry population but the
quotient-response theorem:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}QRESP}(L,\epsilon_{data})
}
$$
combined with either:

1. a primal candidate family for hidden anti-heat; or
2. a dual floor/search family for product visibility.

This is genuinely narrower than the original actual-law value problem.  It
asks only for source responses against the finite polar tests that the
quotient-distance certificate actually uses.

Proof.

`P32-HKBAD-PRODENTRY` prints all quotient-visible product columns.  In
contrast, `QRESP` prints only the pairings selected by the certificate
search.  Lemmas 42.2 and 42.3 show that those pairings are sufficient for the
dual and restricted-primal searches.  Therefore `QRESP` is the sharper
positive target. `square`

## 43. Endpoint Of The Corollary 38.2 Attack

### Theorem 43.1: Corollary 38.2 Reduces To Product-Entry Or Quotient-Response Data

The five tasks in Corollary 38.2 have the following status.

1. \(E_{HB}^{N,j,L}\), \(C_{HB}^{N,j,L}\), and \(Q_{HB}^{N,j,L}\) are
   structurally finite and sourced by Papers 23, 26, 29, 30, and 31.
2. \(k_{HB}^{N,j,L}\) is structurally finite and sourced by the Paper-30
   heat switch mismatch after quotienting.
3. The product operators \(A_\Gamma^{N,j,L}\) require new same-law product
   entry information, unless replaced by the narrower quotient-response
   theorem.
4. Once product entries or quotient responses are available, the finite
   quotient-distance program is certificate-decidable by Theorem 38.1.
5. Tail lifting is already separated as a Peter-Weyl omitted-mode certificate;
   it is not a new label problem.

Therefore the next live theorem is exactly one of:
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}PRODENTRY}(L,\epsilon_{data})
}
$$
or
$$
\boxed{
\mathrm{P32\text{-}HKBAD\text{-}QRESP}(L,\epsilon_{data}).
}
$$

The current corpus proves neither in closing range.

Proof.

Items 1 and 2 are Proposition 40.1.  Item 3 is Proposition 40.2.  Item 4 is
Theorem 38.1.  Item 5 is the tail clause already isolated in Sections 35--38.
The two boxed targets are Corollary 40.3 and Proposition 42.4.  The
current-corpus non-derivation follows from Proposition 41.3 and from the
absence of the required Paper-31 source-response constants for the quotient
polar tests. `square`

### Corollary 43.2: Next Work Package

The next work package should attack `P32-HKBAD-QRESP` first.  It is the
smallest positive target now visible:

1. choose a finite polar test family from the quotient-distance SDP;
2. define its deterministic same-law observables \(V_\Lambda\);
3. try to prove switch neutrality for those observables only;
4. try to prove curvature for those observables only;
5. if either fails, use the same polar family to search for a dual floor.

This keeps the Feynman-style reframing alive.  We do not ask for the whole
law, and we do not ask for every atom value.  We ask for the source response
of exactly the finite quotient tests that can decide hidden anti-heat versus
product-visible floor.

## 44. Polar-Only Source Response

The quotient-response theorem should not quantify over every heat-bad dual
test from Paper 30.  It only needs the polar tests that can appear in a
certificate search for the finite quotient-distance program.

### Definition 44.1: Certificate Polar Family

For a row \((N,j,L)\), let
$$
{\mathcal P}_{HB}^{N,j,L}
$$
be the finite rational polar family generated by:

1. the dual feasible functionals used in
   `P32-HKBAD-QDIST-DUAL-FLOOR`;
2. the trace-norm polar matrices used by a declared finite primal candidate
   family \(X_\theta\);
3. the heat-target evaluation functionals \(\Lambda(k_{HB})\);
4. the quotient \(L^\infty\)-constraint normals appearing in the
   anti-heat feasibility test.

The family is finite because the row, cutoff, quotient gauge, primal ansatz,
and dual search body are finite.

### Definition 44.2: Polar Source Observable

For \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\), define
$$
V_\Lambda^{N,j,L}(\omega)
$$
to be the deterministic finite record observable obtained by pairing
\(\Lambda\) with the heat-bad quotient product slot.  Equivalently,
$$
\mathbf E_{N,j}^{act}
\left[
V_\Lambda^{N,j,L}
\right]
=
\Lambda\!\left(A^{N,j,L}_{HB}\right),
$$
where \(A^{N,j,L}_{HB}\) denotes the finite collection of product operators
\(\{A_\Gamma^{N,j,L}\}_\Gamma\) after quotienting the licensed directions.

Define the same-law polar pressure
$$
\Psi_\Lambda^{N,j,L}(s)
:=
\log
\mathbf E_{N,j}^{act}
\left[
\exp\left(sV_\Lambda^{N,j,L}\right)
\right].
$$

### Lemma 44.3: Polar First Response Identity

For every \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\),
$$
{\partial\over\partial s}
\Psi_\Lambda^{N,j,L}(0)
=
\Lambda\!\left(A^{N,j,L}_{HB}\right).
$$

Proof.

The row law is finite after the retained cutoff.  Differentiating the finite
log moment-generating function at \(s=0\) gives
$$
\Psi_\Lambda'(0)
=
{\mathbf E[V_\Lambda e^0]\over \mathbf E[e^0]}
=
\mathbf E[V_\Lambda].
$$
The last term is the defining pairing. `square`

### Definition 44.4: Polar Quotient Response Gate

`P32-HKBAD-QRESP-POLAR(L,epsilon_data)` asserts that cofinally, for every
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\),
$$
\left|
{\partial\over\partial s}
\Psi_\Lambda^{N,j,L}(0)
\right|
\le \epsilon_{data}
$$
after subtracting the declared target value of the certificate pairing.

This is the operational form of `P32-HKBAD-QRESP`: it bounds precisely the
source slopes that the quotient-distance certificate needs.

### Lemma 44.5: Polar Response Implies `QRESP`

`P32-HKBAD-QRESP-POLAR(L,epsilon_data)` implies
`P32-HKBAD-QRESP(L,epsilon_data)`.

Proof.

The definition of `QRESP` asks for certified first responses for the dual and
restricted primal polar tests used by the certificate.  These tests are
exactly \({\mathcal P}_{HB}^{N,j,L}\). `square`

## 45. Polar Neutrality And Curvature

### Definition 45.1: Polar Source Neutrality

For \(a>0\) and \(\rho\ge0\),
`P32-HKBAD-QPOLAR-NEUT(L,a,rho)` asserts that cofinally, for every
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\),
$$
\left|
\Psi_\Lambda^{N,j,L}(a)
-
\Psi_\Lambda^{N,j,L}(-a)
\right|
\le 2\rho .
$$

### Definition 45.2: Polar Source Curvature

For \(a>0\) and \(\chi\ge0\),
`P32-HKBAD-QPOLAR-CURV(L,a,chi)` asserts that cofinally, for every
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\) and every \(|s|\le a\),
$$
\left|
{\partial^2\over\partial s^2}
\Psi_\Lambda^{N,j,L}(s)
\right|
\le\chi .
$$

### Lemma 45.3: Polar Neutrality Plus Curvature Sources `QRESP`

If `P32-HKBAD-QPOLAR-NEUT(L,a,rho)` and
`P32-HKBAD-QPOLAR-CURV(L,a,chi)` hold, then
`P32-HKBAD-QRESP-POLAR(L,epsilon_data)` holds with
$$
\epsilon_{data}
=
{\rho\over a}+{\chi a\over2}.
$$

Proof.

Apply the Paper-31 source calculus to the finite source family
\({\mathcal P}_{HB}^{N,j,L}\).  For each \(\Lambda\), write
\(\Psi=\Psi_\Lambda^{N,j,L}\).  Then
$$
\Psi(a)-\Psi(-a)
=
2a\Psi'(0)
+
\int_{-a}^{a}(\Psi'(t)-\Psi'(0))\,dt .
$$
The curvature bound controls the integral by \(\chi a^2\), and the
neutrality bound controls the left side by \(2\rho\).  Divide by \(2a\) and
take the supremum over \(\Lambda\). `square`

### Corollary 45.4: Optimized Polar Debit

If \(\rho\) and \(\chi\) are independent of \(a\), the optimized polar
response debit is
$$
\epsilon_{data}^{opt}
=
\sqrt{2\rho\chi}.
$$

## 46. Switch-Odd Route To Polar Neutrality

The natural positive route is still switch oddness, but now only for the
finite polar family, not for every heat-bad dual probe.

### Definition 46.1: Polar Switch Even Defect

Let \(\mathsf S_{N,j}\) be the Paper-30 heat-bad recoupling switch.  For
\(\eta\ge0\) and \(\omega_S\ge0\),
`P32-HKBAD-QPOLAR-SWODD(L,eta,omega_S)` asserts that cofinally, for every
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\):

1. the switch Radon-Nikodym oscillation obeys
   $$
   \operatorname{osc}
   \log {d(\mathsf S_{N,j})_*\nu_{N,j}^{act}\over d\nu_{N,j}^{act}}
   \le \omega_S;
   $$
2. the polar observable is switch-odd up to defect \(\eta\):
   $$
   \left\|
   V_\Lambda^{N,j,L}\circ\mathsf S_{N,j}
   +
   V_\Lambda^{N,j,L}
   \right\|_\infty
   \le \eta .
   $$

### Lemma 46.2: Polar Switch-Oddness Gives Neutrality

If `P32-HKBAD-QPOLAR-SWODD(L,eta,omega_S)` holds, then
`P32-HKBAD-QPOLAR-NEUT(L,a,rho)` holds with
$$
\rho={\omega_S+a\eta\over2}.
$$

Proof.

Fix \(\Lambda\).  Write \(V=V_\Lambda^{N,j,L}\) and
\(J=\log d(\mathsf S_*\nu)/d\nu\).  By change of variables,
$$
\mathbf E e^{aV}
=
\mathbf E e^{aV\circ\mathsf S+J}.
$$
The assumptions give
$$
aV\circ\mathsf S+J
\le
-aV+a\eta+\omega_S .
$$
Therefore
$$
\Psi_\Lambda(a)
\le
\Psi_\Lambda(-a)+a\eta+\omega_S .
$$
The reverse inequality follows by applying the same argument with \(a\) and
\(-a\) interchanged.  Hence
$$
\left|\Psi_\Lambda(a)-\Psi_\Lambda(-a)\right|
\le a\eta+\omega_S
=2\rho .
$$
Take the supremum over the finite polar family. `square`

## 47. Curvature Routes For Polar Tests

### Definition 47.1: Polar Oscillation Bound

`P32-HKBAD-QPOLAR-OSC(L,R)` asserts that cofinally, for every
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\),
$$
\operatorname{osc} V_\Lambda^{N,j,L}\le R .
$$

### Lemma 47.2: Oscillation Gives A Universal But Usually Coarse Curvature Bound

If `P32-HKBAD-QPOLAR-OSC(L,R)` holds, then
`P32-HKBAD-QPOLAR-CURV(L,a,chi)` holds with
$$
\chi={R^2\over4}.
$$

Proof.

For real scalar \(V\), the second derivative of
\(\log\mathbf E e^{sV}\) is the variance of \(V\) under the tilted finite
law.  A random variable of oscillation \(R\) has variance at most \(R^2/4\).
`square`

### Definition 47.3: Polar Ward Curvature

`P32-HKBAD-QPOLAR-WARD(L,epsilon_W,chi_W)` asserts that the polar source
family admits a same-law Ward/Stein identity of the form
$$
{\partial\over\partial s}
\Psi_\Lambda^{N,j,L}(0)
=
\mathbf E_{N,j}^{act}
\left[
\mathcal W_\Lambda^{N,j,L}
\right],
$$
with
$$
\left|
\mathbf E_{N,j}^{act}
\left[
\mathcal W_\Lambda^{N,j,L}
\right]
\right|
\le\epsilon_W
$$
and tilted covariance remainder bounded by \(\chi_W\) for all
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\).

### Lemma 47.4: Polar Ward Route Sources `QRESP`

If `P32-HKBAD-QPOLAR-WARD(L,epsilon_W,chi_W)` holds, then
`P32-HKBAD-QRESP-POLAR(L,epsilon_data)` holds with
$$
\epsilon_{data}=\epsilon_W
$$
for direct first-response use, and with the stronger interval debit
\(\epsilon_W+\chi_W a/2\) when the Ward identity is only established on a
source interval of radius \(a\).

Proof.

The first displayed identity replaces the source slope by a Ward remainder.
The stated expectation bound gives the direct response estimate.  If the
identity is established along a source segment rather than exactly at zero,
the curvature remainder is paid by the same integral estimate as Lemma 45.3.
`square`

### Proposition 47.5: Current-Corpus Status Of Polar Curvature

The current corpus proves only the finite oscillation curvature bound for
the polar family.  It does not prove a closing polar Ward, log-Sobolev,
small-variance, or Peter-Weyl-tail curvature theorem.

Proof.

The polar observables are finite actual-record functions, so some rowwise
oscillation bound exists.  But Papers 20--31 do not print a cofinal bound
small enough for the heat-bad budget, nor a Ward/Stein inverse specialized to
the polar quotient tests, nor a log-Sobolev or Peter-Weyl regularity theorem
for the tilted polar source family.  Thus the universal curvature estimate
is available, but it is not a closing theorem. `square`

## 48. Polar Floor Route

If the polar response is not small, the same family should be used as a
floor detector.

### Definition 48.1: Polar Floor Witness

`P32-HKBAD-QPOLAR-FLOOR(L,M,delta)` asserts that cofinally there exists
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\) such that:

1. the first response is sign-coherent in the retained Branch-A ledger;
2. the response survives the licensed quotient and Peter-Weyl tail with
   margin \(\delta\);
3. the retained lower contribution is at least \(M+\delta\):
   $$
   \left|
   {\partial\over\partial s}
   \Psi_\Lambda^{N,j,L}(0)
   \right|
   \ge M+\delta .
   $$

### Lemma 48.2: Polar Floor Falsifies The Positive Heat-Bad Route

If `P32-HKBAD-QPOLAR-FLOOR(L,M,delta)` holds with \(M>B_A^{rem}\), then the
positive heat-bad Branch-A route is falsified.

Proof.

The polar functional is one of the dual product-visible tests.  If its
response is sign-coherent and exceeds the remaining retained budget after
tail and quotient margins, the heat-bad contribution cannot be absorbed by
the positive debit ledger.  This is Lemma 37.4 applied to a concrete polar
dual witness. `square`

## 49. Endpoint Of The `QRESP` Attack

### Theorem 49.1: `QRESP` Is Reduced To Three Polar Primitive Inputs

The quotient-response route is fully reduced to the following alternatives.

Positive closure follows from either:

1. polar switch-oddness plus polar curvature:
   $$
   \mathrm{P32\text{-}HKBAD\text{-}QPOLAR\text{-}SWODD}(L,\eta,\omega_S)
   +
   \mathrm{P32\text{-}HKBAD\text{-}QPOLAR\text{-}CURV}(L,a,\chi),
   $$
   with
   $$
   {\omega_S+a\eta\over2a}
   +
   {\chi a\over2}
   \le \epsilon_{data};
   $$
2. a direct polar Ward route:
   $$
   \mathrm{P32\text{-}HKBAD\text{-}QPOLAR\text{-}WARD}
   (L,\epsilon_W,\chi_W),
   $$
   with the resulting \(\epsilon_{data}\) inside the row certificate margin.

Negative/floor closure follows from:
$$
\mathrm{P32\text{-}HKBAD\text{-}QPOLAR\text{-}FLOOR}(L,M,\delta),
\qquad
M>B_A^{rem}.
$$

The current corpus proves none of these in a closing range.

Proof.

The first positive route is Lemma 46.2 followed by Lemma 45.3.  The second is
Lemma 47.4.  The floor route is Lemma 48.2.  Proposition 47.5 records the
absence of a closing curvature theorem; Paper 30's heat-bad audit records
that weighted switch oddness and residual/signed product control are not
sourced by existing finite labels; Paper 31 records that source-response
identities do not by themselves give smallness.  Therefore the route is
reduced but not closed by the current corpus. `square`

### Corollary 49.2: What To Do Next

The next concrete task is to instantiate \({\mathcal P}_{HB}^{N,j,L}\) for a
small cutoff \(L\) and run the polar test in three passes:

1. compute the switch-even defect \(\eta\) of each polar observable;
2. compute or bound its curvature/oscillation profile;
3. if the positive inequality fails, test the largest polar response for
   sign-coherent floor behavior.

This is the narrowest live version of the heat-bad problem presently in the
corpus.  More finite labels are not expected to help unless they reduce
\({\mathcal P}_{HB}^{N,j,L}\), lower the switch-even defect, or produce a
Ward identity for these exact polar observables.

## 50. Route I: Polar Switch-Oddness Plus Curvature

We now explore the first route of Theorem 49.1.  It is not the old heat-bad
weighted-oddness theorem over every dual probe.  It asks only whether the
certificate polar family is nearly odd under the recoupling switch.

### Definition 50.1: Polar Switch Defect Table

For \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\), define the switch-even defect
$$
E_\Lambda^{sw}
:=
V_\Lambda^{N,j,L}
+
V_\Lambda^{N,j,L}\circ\mathsf S_{N,j}.
$$

The polar switch defect table is the finite list
$$
\mathcal E_{pol}^{N,j,L}
:=
\left\{
\operatorname{osc}J_{\mathsf S}^{N,j},
\|E_\Lambda^{sw}\|_\infty,
\operatorname{osc}V_\Lambda^{N,j,L}
:
\Lambda\in{\mathcal P}_{HB}^{N,j,L}
\right\},
$$
where
$$
J_{\mathsf S}^{N,j}
:=
\log {d(\mathsf S_{N,j})_*\nu_{N,j}^{act}\over d\nu_{N,j}^{act}} .
$$

### Lemma 50.2: The Defect Table Gives A Closing Number

Assume the table bounds
$$
\operatorname{osc}J_{\mathsf S}^{N,j}\le\omega_S,\qquad
\|E_\Lambda^{sw}\|_\infty\le\eta,\qquad
\operatorname{osc}V_\Lambda^{N,j,L}\le R
$$
for all \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\).  Then
`P32-HKBAD-QRESP-POLAR(L,epsilon_data)` holds with
$$
\epsilon_{data}
\le
{\omega_S\over2a}
+
{\eta\over2}
+
{R^2a\over8}
$$
for every \(a>0\).

If \(R>0\), the optimized bound is
$$
\epsilon_{data}
\le
{\eta\over2}
+
{R\sqrt{\omega_S}\over2}.
$$

Proof.

Lemma 46.2 gives polar neutrality with
\(\rho=(\omega_S+a\eta)/2\).  Lemma 47.2 gives curvature
\(\chi=R^2/4\).  Substitute these into Lemma 45.3:
$$
{\rho\over a}+{\chi a\over2}
=
{\omega_S\over2a}
+
{\eta\over2}
+
{R^2a\over8}.
$$
Optimizing over \(a\) gives \(a=2\sqrt{\omega_S}/R\) and the displayed
value. `square`

### Corollary 50.3: Exact Polar Oddness Is A Real Positive Theorem

If cofinally
$$
\omega_S=0,\qquad \eta=0,
$$
then the polar response vanishes:
$$
\Psi_\Lambda'(0)=0
$$
for every \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\).  Hence `QRESP` closes
with \(\epsilon_{data}=0\), modulo the already separated tail.

Proof.

With \(\omega_S=\eta=0\), Lemma 46.2 gives exact evenness of every polar
pressure.  Differentiating at zero gives zero first response. `square`

### Proposition 50.4: Current-Corpus Status Of Route I

The current corpus does not prove the Route-I closing bound.

More precisely:

1. the switch defect table is finite and well-defined;
2. exact or small \(\omega_S\) is a genuine same-law switch quasi-invariance
   theorem for the actual adaptive row;
3. exact or small \(\eta\) is a genuine weighted polar oddness theorem;
4. the universal curvature bound from \(R\) is available but is generally
   non-closing unless the actual polar oscillation table is small;
5. Papers 20--31 do not print closing values of \(\omega_S,\eta,R\) for the
   certificate polar family.

Proof.

The table is finite by Definition 44.1.  The Radon-Nikodym oscillation is the
same same-law switch quantity already isolated in Sections 19--24.  The
switch-even defect is a polar projection of the Paper-30 weighted heat-bad
oddness object; Paper 30 proves that bare signed parity does not control it
on heat-bad two-channel blocks.  Curvature from \(R\) is Lemma 47.2, but the
current corpus gives no cofinal small \(R\) theorem for these actual polar
observables.  Thus Route I is valid and narrower than the all-probe route,
but it is not proved by the current corpus. `square`

### Remark 50.5: Why Route I Is Not Yet Falsified

Route I is not false merely because the all-probe heat-bad weighted oddness
route was unsourced.  The polar family may avoid some bad directions.  To
falsify Route I at a fixed row, one must instantiate
\({\mathcal P}_{HB}^{N,j,L}\) and prove that at least one certificate-needed
polar observable has unavoidable large switch-even defect or curvature.
Without that instantiated polar table, the route remains a valid but
unsourced positive theorem.

## 51. Route II: Polar Ward Or Stein Identity

The second route tries to avoid the neutrality/curvature balance by proving
a direct Ward/Stein identity for the polar source slopes.

### Definition 51.1: Polar Ward Operator

For \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\), a polar Ward package consists of
a finite same-law differential/difference operator \(\mathcal D_\Lambda\), a
finite potential \(G_\Lambda\), and a remainder
\(\mathcal R_\Lambda^{Ward}\) such that
$$
V_\Lambda^{N,j,L}
=
\mathcal D_\Lambda G_\Lambda
+
\mathcal R_\Lambda^{Ward}
$$
as finite record observables after the same quotient and retained-row
conventions.

The package is admissible only if the integration-by-parts identity
$$
\mathbf E_{N,j}^{act}
\left[
\mathcal D_\Lambda G_\Lambda
\right]
=0
$$
is proved under the actual adaptive law, not under a substitute reference
law.

### Lemma 51.2: Polar Ward Remainder Gives `QRESP`

If an admissible polar Ward package satisfies
$$
\left|
\mathbf E_{N,j}^{act}
\left[
\mathcal R_\Lambda^{Ward}
\right]
\right|
\le\epsilon_W
$$
for every \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\), then
`P32-HKBAD-QRESP-POLAR(L,epsilon_W)` holds.

Proof.

By Lemma 44.3,
$$
\Psi_\Lambda'(0)
=
\mathbf E[V_\Lambda].
$$
Substitute the Ward decomposition and use the actual-law integration by
parts:
$$
\mathbf E[V_\Lambda]
=
\mathbf E[\mathcal D_\Lambda G_\Lambda]
+
\mathbf E[\mathcal R_\Lambda^{Ward}]
=
\mathbf E[\mathcal R_\Lambda^{Ward}].
$$
The claimed bound follows. `square`

### Definition 51.3: `P32-HKBAD-QPOLAR-WARD-EXACT(L,epsilon_W)`

`P32-HKBAD-QPOLAR-WARD-EXACT(L,epsilon_W)` asserts that cofinally every
\(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\) admits an admissible polar Ward
package with
$$
\left|
\mathbf E_{N,j}^{act}
\left[
\mathcal R_\Lambda^{Ward}
\right]
\right|
\le\epsilon_W .
$$

### Lemma 51.4: Exact Polar Ward Implies The Ward Route Of Theorem 49.1

`P32-HKBAD-QPOLAR-WARD-EXACT(L,epsilon_W)` implies
`P32-HKBAD-QPOLAR-WARD(L,epsilon_W,0)` and therefore sources `QRESP` with
\(\epsilon_{data}=\epsilon_W\).

Proof.

This is Lemma 51.2 in the notation of Definition 47.3. `square`

### Proposition 51.5: Current-Corpus Status Of Route II

The current corpus does not prove `P32-HKBAD-QPOLAR-WARD-EXACT` in a closing
range.

Proof.

Papers 30 and 31 print legitimate Ward/Stein templates: finite compact-group
Stein operators, source derivative dictionaries, and several conditional
Ward routes.  But Paper 30 repeatedly records that the useful Ward/Stein
closures require actual residual score pairings, low-mode Stein tables, or
tail estimates not printed by the current corpus.  Paper 32 Section 26
already proves that the even-response Ward source is not currently sourced.
The polar family is smaller, so a polar Ward theorem remains plausible, but
it still requires a new admissible actual-law integration-by-parts package
for these exact quotient polar observables.  No such package is presently
printed. `square`

### Remark 51.6: The Only Plausible Positive Ward Move

The promising Ward move is not to build a universal heat-bad Ward inverse.
It is to instantiate \({\mathcal P}_{HB}^{N,j,L}\), solve a finite Stein
equation only for those polar observables, and then test whether the actual
residual score pairings cancel or are tail-small.  This is finite and
Barandes-aligned, but it is new same-law quantitative work.

## 52. Route III: Polar Floor

The third route is the honest negative branch: if a certificate polar
observable is large and sign-coherent, it should be used to falsify the
positive Branch-A heat-bad route.

### Definition 52.1: Signed Polar Ledger Class

For \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\), let
$$
\operatorname{sgnled}(\Lambda)
\in\{+,-,0,\star\}
$$
be the retained ledger sign classification:

1. \(+\): the response contributes positively to the retained Branch-A
   predebit after quotient and tail lifting;
2. \(-\): the response contributes negatively;
3. \(0\): the response is killed by a licensed quotient or endpoint row;
4. \(\star\): the sign is not certified by the current retained ledger.

This sign classification is part of the floor theorem.  It is not implied by
a trace norm lower bound.

### Definition 52.2: Polar Floor Table

The polar floor table is the finite list
$$
\mathcal F_{pol}^{N,j,L}
:=
\left\{
\operatorname{sgnled}(\Lambda),
\Psi_\Lambda'(0),
\epsilon_{\Lambda,tail},
\epsilon_{\Lambda,quot}
:
\Lambda\in{\mathcal P}_{HB}^{N,j,L}
\right\}.
$$

### Lemma 52.3: Floor Table Criterion

If there exists \(\Lambda\in{\mathcal P}_{HB}^{N,j,L}\) such that
$$
\operatorname{sgnled}(\Lambda)\in\{+,-\},
$$
and
$$
\left|\Psi_\Lambda'(0)\right|
-
\epsilon_{\Lambda,tail}
-
\epsilon_{\Lambda,quot}
\ge M
>
B_A^{rem},
$$
then `P32-HKBAD-QPOLAR-FLOOR(L,M,delta)` holds for some
\(\delta>0\), and the positive Branch-A heat-bad route is falsified.

Proof.

The certified sign means the response survives in the retained predebit
ledger instead of cancelling with an endpoint, quotient, or orientation
partner.  The tail and quotient margins give a retained lower bound of at
least \(M\).  Lemma 48.2 then falsifies the positive route. `square`

### Proposition 52.4: Current-Corpus Status Of Route III

The current corpus does not prove a polar floor above the Branch-A budget.

Proof.

Paper 30 proves that a heat-bad floor would falsify Branch A, but it also
proves that neither the direct heat-bad floor nor the signed/bridge lower
floors are sourced by the existing representation, selector, or finite label
data.  The polar family narrows the search, but a floor still requires two
new same-law facts: a lower bound on an actual polar response and a retained
ledger sign-coherence certificate.  Paper 31 source-response calculus
identifies such slopes as possible floor witnesses, but does not evaluate
them.  Hence Route III is valid but unsourced. `square`

### Remark 52.5: Floor Route Is The Correct Fallback

If Route I or II produces a large polar response rather than a small one, the
right next step is not to discard the computation.  The same response should
be pushed through the floor table.  In this sense the polar program is
two-sided: every evaluated polar slope either helps the positive certificate,
or becomes a candidate lower-floor witness.

## 53. Final Verdict On The Three Polar Routes

### Theorem 53.1: The Three Polar Routes Are Fully Classified At Current-Corpus Level

For the finite certificate polar family \({\mathcal P}_{HB}^{N,j,L}\):

1. Route I, `QPOLAR-SWODD + QPOLAR-CURV`, is a valid positive theorem.  It
   closes with debit
   $$
   {\omega_S\over2a}+{\eta\over2}+{\chi a\over2},
   $$
   or with
   $$
   {\eta\over2}+{R\sqrt{\omega_S}\over2}
   $$
   under the universal oscillation curvature bound \(\chi=R^2/4\).  The
   current corpus does not print closing \(\omega_S,\eta,R\).
2. Route II, `QPOLAR-WARD`, is a valid positive theorem if an admissible
   actual-law Ward package is printed for the polar observables.  The current
   corpus does not print such a package.
3. Route III, `QPOLAR-FLOOR`, is the valid negative theorem if a polar slope
   is sign-coherent and exceeds \(B_A^{rem}\) after quotient and tail
   margins.  The current corpus does not print such a floor witness.

Therefore the three routes have been explored and reduced to concrete
finite same-law tasks.  None is closed by the current corpus, but none is
mere bookkeeping either: each gives a precise next computation on the same
finite polar family.

Proof.

Route I is Lemma 50.2 and Proposition 50.4.  Route II is Lemma 51.4 and
Proposition 51.5.  Route III is Lemma 52.3 and Proposition 52.4. `square`

### Corollary 53.2: Next Concrete Computational Worksheet

The next worksheet is now unambiguous:

1. instantiate \({\mathcal P}_{HB}^{N,j,L}\) at the smallest nontrivial
   cutoff;
2. print \(\operatorname{osc}J_{\mathsf S}\), \(\|E_\Lambda^{sw}\|_\infty\),
   and \(\operatorname{osc}V_\Lambda\) for every polar observable;
3. solve the finite Stein equation for the same observables, if the switch
   route misses the budget;
4. evaluate the largest polar slopes against the signed ledger for the floor
   route;
5. only then decide whether Paper 32 has a positive heat-bad close, a
   negative floor close, or a genuinely open same-law polar-value obstruction.

This is the narrowest useful continuation.  It is not a call for more
canonical labels.

## 54. The Smallest Nontrivial Polar Worksheet

This section carries out Corollary 53.2.  The aim is to stop speaking
globally about an unknown same-law response and isolate the smallest block
where the obstruction already appears.

The minimal block is the Paper-30 singlet-adjoint crossing block.  In the
basis

$$
|0\rangle,\qquad |A\rangle,
$$

Paper 30 prints the crossing involution

$$
U_N
=
\begin{pmatrix}
a_N & b_N\\
b_N & -a_N
\end{pmatrix},
\qquad
a_N={1\over N},
\qquad
b_N={\sqrt{N^2-1}\over N}.
$$

Thus

$$
U_N^*=U_N,\qquad U_N^2=I.
$$

The heat-reference diagonal on the same block is

$$
D_{\Gamma_1}^{HK}
=
\begin{pmatrix}
h_0&0\\
0&h_A
\end{pmatrix},
\qquad
h_0=1,
\qquad
h_A=(N^2-1)e^{-t_p\lambda_{HK}N}.
$$

The actual same-law residual input is not this heat diagonal.  It is the
actual residual/signed product on the same adaptive pushed-forward law:

$$
B_{\Gamma_1}^{N,j}:=
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}.
$$

The corresponding weighted bridge matrix is

$$
A_{\Gamma_1}^{N,j}
:=
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}.
$$

The polar even defect is

$$
\Pi_+^{U_N}(A_{\Gamma_1}^{N,j})
:=
{1\over2}\left(
A_{\Gamma_1}^{N,j}
+U_NA_{\Gamma_1}^{N,j}U_N
\right).
$$

The finite polar worksheet is therefore the datum

$$
\mathcal T_{\min}^{pol}(N,j)
=
\left(
a_N,b_N,h_0,h_A,
B_{\Gamma_1}^{N,j},
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j})
\right).
$$

The first four entries are structural and already printed.  The heat-bad
status of the block is also already known from Paper 30: singlet/adjoint
transport into the two-index sector is heat-bad for small balance tolerance,
and the singlet-adjoint block is the lowest crossing block where heat
noncommutation is visible.  The only unprinted entry is

$$
B_{\Gamma_1}^{N,j}=R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}.
$$

### Definition 54.1: Minimal Polar Source Theorem

The primitive theorem

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}BTABLE}(\varepsilon)
$$

means that the actual adaptive pushed-forward law determines a finite interval
matrix

$$
\mathcal B_{\Gamma_1}^{N,j}(\varepsilon)
\ni B_{\Gamma_1}^{N,j}
$$

whose induced interval for the polar even defect has width at most
\(\varepsilon\) in trace norm.

The theorem

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}QRESP}(\varepsilon)
$$

is the equivalent polar form: for every \(2\times2\) test matrix \(Q\) with
\(\|Q\|_{op}\le1\), the same law sources

$$
\operatorname{Tr}
\left[
Q\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j})
\right]
$$

to error at most \(\varepsilon\).

### Lemma 54.2: Worksheet Reduction

On the smallest heat-bad crossing block, every one of the three polar routes
from Theorem 53.1 is decided by the same finite object
\(B_{\Gamma_1}^{N,j}\), equivalently by
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}QRESP}\).

Proof.

The structural matrices \(U_N\) and \(D_{\Gamma_1}^{HK}\) are already fixed.
For any proposed bridge certificate, the polar obstruction enters through the
linear functional

$$
B\mapsto
\operatorname{Tr}
\left[
Q\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
\right].
$$

Thus route I asks whether these functionals are small, route II asks whether
they can be represented by a same-law Ward/Stein response, and route III asks
whether one of them has a sign-coherent lower floor.  No further structural
label can change this finite linear dependence.  `square`

## 55. Route I On The Minimal Block: Weighted Switch-Oddness

The route-I hope is that the crossing involution makes the heat-bad bridge
nearly odd.  On the minimal block this becomes an exact matrix equation.

### Definition 55.1: Minimal Weighted Switch-Oddness

For \(\eta\ge0\), write

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}SWODD}(\eta)
$$

for the estimate

$$
\left\|
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}
\right)
\right\|_1
\le \eta.
$$

The word "weighted" matters.  Bare oddness of \(B_{\Gamma_1}^{N,j}\) is not
enough, because \(D_{\Gamma_1}^{HK}\) does not commute with \(U_N\) unless
\(h_0=h_A\).

### Lemma 55.2: The Minimal Leakage Identity

Assume the optimistic Paper-30 switch-odd model

$$
B_{\Gamma_1}^{N,j}
=
\Sigma_{\mathrm{odd}}
:=
\begin{pmatrix}
b_N&-a_N\\
-a_N&-b_N
\end{pmatrix}.
$$

Then

$$
U_N\Sigma_{\mathrm{odd}}U_N=-\Sigma_{\mathrm{odd}},
$$

but

$$
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}\Sigma_{\mathrm{odd}}
\right)
=
{(h_0-h_A)b_N\over2}I_2.
$$

Consequently

$$
\left\|
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}\Sigma_{\mathrm{odd}}
\right)
\right\|_1
=
|h_0-h_A|b_N.
$$

Proof.

The first identity is the Paper-30 crossing-odd computation.  Multiplying by
the noncentral heat diagonal produces a commutator defect.  Direct matrix
multiplication gives the displayed scalar multiple of the identity.  Its
trace norm is the sum of the two singular values, hence \(|h_0-h_A|b_N\).
`square`

### Corollary 55.3: Route-I Current-Corpus Verdict

Route I is not proved by the existing corpus.  It is also not refuted as a
statement about the actual adaptive law.  What is refuted is the simpler
argument

$$
U_NB_{\Gamma_1}^{N,j}U_N\approx-B_{\Gamma_1}^{N,j}
\quad\Longrightarrow\quad
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j})\approx0.
$$

The correct target is weighted switch-oddness after insertion of
\(D_{\Gamma_1}^{HK}\).  To close route I one must source
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}SWODD}(\eta)\) with \(\eta\)
below the bridge margin.  More labels do not affect this requirement.

## 56. Route II On The Minimal Block: Ward Or Stein Response

Route II tries to avoid direct evaluation of \(B_{\Gamma_1}^{N,j}\) by
representing the polar functional as a same-law response.

For each test matrix \(Q\) with \(\|Q\|_{op}\le1\), define

$$
V_Q(B)
:=
\operatorname{Tr}
\left[
Q\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
\right].
$$

A minimal Ward theorem would provide a same-law source operator
\(\mathcal L_{N,j}^{src}\), a finite potential \(G_Q\), and a residual
\(\mathcal R_Q\) such that

$$
V_Q(B_{\Gamma_1}^{N,j})
=
\mathcal L_{N,j}^{src}G_Q
+\mathcal R_Q
$$

and

$$
\left|
\mathbf E_{\mu_{N,j}^{ad}}
\mathcal R_Q
\right|
\le\varepsilon
$$

uniformly over the minimal polar tests.

### Definition 56.1: Minimal Polar Ward Theorem

The assertion

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD}(\varepsilon)
$$

means exactly the preceding representation with \(\varepsilon\)-small
same-law residual for every minimal polar test \(Q\).

### Lemma 56.2: What Route II Would Buy

If

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD}(\varepsilon)
$$

holds and the source operator is centered under the actual adaptive law, then

$$
\left|
\mathbf E_{\mu_{N,j}^{ad}}
V_Q(B_{\Gamma_1}^{N,j})
\right|
\le\varepsilon
$$

for every minimal polar test \(Q\).  Hence route II implies
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}SWODD}(\eta)\) at
\(\eta\le C_{\min}\varepsilon\), where \(C_{\min}\) is the finite
polar-duality constant of the two-dimensional block.

Proof.

The centered source term has expectation zero.  The residual has expectation
bounded by \(\varepsilon\).  Taking the finite supremum over the polar tests
recovers the trace-norm defect up to the fixed finite duality constant.
`square`

### Corollary 56.3: Route-II Current-Corpus Verdict

Route II is the cleanest conceptual route, but it is still a primitive
same-law value theorem.  The corpus contains the structural source-response
reframing and the finite polar reduction, but it does not yet contain the
Ward/Stein residual estimate

$$
\mathbf E_{\mu_{N,j}^{ad}}\mathcal R_Q=O(\varepsilon)
$$

for the actual adaptive law.  Thus route II remains open exactly at
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD}\).

## 57. Route III On The Minimal Block: Sign-Coherent Floor

Route III is the negative/floor route.  It proves that the heat-bad bridge is
not small, and therefore that the attempted positive branch must fail unless
some external floor is already large enough to close confinement by another
gate.

### Definition 57.1: Minimal Polar Floor

For \(M>0\), write

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}FLOOR}(M)
$$

if there exists a minimal polar test \(Q_*\), chosen from the same finite
worksheet and not from outside the adaptive law, such that

$$
\operatorname{sgn}(Q_*)\,
\mathbf E_{\mu_{N,j}^{ad}}
\operatorname{Tr}
\left[
Q_*
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j})
\right]
\ge M.
$$

The sign is part of the theorem.  A large absolute value is not enough; the
bridge floor must be sign-coherent with the confinement ledger.

### Lemma 57.2: The Optimistic Floor Scale

In the optimistic switch-odd model of Lemma 55.2, the natural floor scale is

$$
M_{\mathrm{opt}}(N,t_p)
=
|h_0-h_A|b_N.
$$

At adjoint balance, \(h_A=1\), so this particular floor vanishes.  Away from
adjoint balance it can be large, but then the sign-coherence and compatibility
with the active SEL2 law still have to be proved.

Proof.

Lemma 55.2 computes the trace norm of the even defect exactly.  The floor
scale is the polar dual value of that trace norm.  At adjoint balance the two
diagonal heat weights are equal on this two-channel block, so the displayed
quantity is zero.  `square`

### Corollary 57.3: Route-III Current-Corpus Verdict

Route III is not closed by current data.  Paper 30 gives the right floor
mechanism, and the minimal worksheet identifies the first possible floor
functional.  But the actual adaptive law has not supplied either

$$
\left|
\mathbf E_{\mu_{N,j}^{ad}}
V_{Q_*}(B_{\Gamma_1}^{N,j})
\right|
\ge M
$$

or the required sign coherence.  Therefore the floor route is open at the
same finite table \(B_{\Gamma_1}^{N,j}\), not at a new combinatorial layer.

## 58. Verdict Of The Minimal Polar Worksheet

The smallest nontrivial heat-bad worksheet has now been instantiated.  It
does not close the obstruction, but it localizes it sharply.

### Theorem 58.1: Minimal Polar Localization

On the singlet-adjoint crossing block, all three live polar routes reduce to
the following actual-law finite value problem:

$$
\boxed{
B_{\Gamma_1}^{N,j}
=
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}
\quad\hbox{under the active adaptive pushed-forward law.}
}
$$

More precisely:

1. Route I closes positively if the weighted even defect
   \(\|\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j})\|_1\) is below the
   bridge margin.
2. Route II closes positively if a same-law Ward/Stein representation sources
   all minimal polar functionals of
   \(\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j})\) with residual below
   the bridge margin.
3. Route III closes negatively, or transfers to a floor gate, if a
   sign-coherent polar functional gives a lower floor above the required
   threshold.

No additional finite labels, selector refinements, or heat-bad taxonomy can
decide these alternatives without new same-law value information.

Proof.

Sections 54 through 57 compute the structural matrices and reduce each route
to a finite family of linear functionals of \(B_{\Gamma_1}^{N,j}\).  The only
unprinted object is the actual residual/signed product itself, or equivalently
its same-law polar responses.  Hence every route is decided by that finite
value datum.  `square`

### Corollary 58.2: The Next Mathematical Target

The next theorem should be attacked in the following precise form:

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}BTABLE}(\varepsilon)
\quad\hbox{or}\quad
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD}(\varepsilon)
\quad\hbox{or}\quad
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}FLOOR}(M).
$$

This is a deliberately small target: a \(2\times2\) same-law value theorem on
the active adaptive SEL2 pushed-forward law.  If this smallest worksheet
cannot be sourced, the larger heat-bad bridge problem cannot be closed inside
Branch A by structural refinements alone.

## 59. Explicit Two-Channel Polar Algebra

The previous section reduces the obstruction to the \(2\times2\) product
\(B_{\Gamma_1}^{N,j}\).  This section computes the exact linear map from that
product to the polar even defect.

Write

$$
B_{\Gamma_1}^{N,j}
=
\begin{pmatrix}
\beta_{00}&\beta_{0A}\\
\beta_{A0}&\beta_{AA}
\end{pmatrix}.
$$

Set

$$
r_0:=h_0\beta_{00},
\qquad
r_A:=h_A\beta_{AA},
\qquad
s:=h_0\beta_{0A}+h_A\beta_{A0}.
$$

Thus

$$
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}
=
\begin{pmatrix}
r_0&h_0\beta_{0A}\\
h_A\beta_{A0}&r_A
\end{pmatrix}.
$$

The two scalar combinations that survive the \(U_N\)-even projection are

$$
m:=r_0+r_A,
\qquad
t:=a_N(r_0-r_A)+b_Ns.
$$

### Lemma 59.1: Rank-Two Compression Of The Polar Defect

For every \(2\times2\) matrix \(B_{\Gamma_1}^{N,j}\),

$$
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}
\right)
=
{m\over2}I_2+{t\over2}U_N.
$$

Equivalently,

$$
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}
\right)
=
{1\over2}
\begin{pmatrix}
m+a_Nt&b_Nt\\
b_Nt&m-a_Nt
\end{pmatrix}.
$$

Proof.

Direct multiplication gives

$$
U_ND_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}U_N
=
\begin{pmatrix}
a_N^2r_0+a_Nb_Ns+b_N^2r_A&
a_Nb_N(r_0-r_A)+b_N^2s-h_0\beta_{0A}\\
a_Nb_N(r_0-r_A)+b_N^2s-h_A\beta_{A0}&
b_N^2r_0-a_Nb_Ns+a_N^2r_A
\end{pmatrix}.
$$

Adding \(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}\), dividing by two, and using
\(a_N^2+b_N^2=1\) yields

$$
\begin{pmatrix}
{m+a_Nt\over2}&{b_Nt\over2}\\
{b_Nt\over2}&{m-a_Nt\over2}
\end{pmatrix}.
$$

This is \((mI_2+tU_N)/2\).  `square`

### Corollary 59.2: Only Two Scalar Responses Matter

The minimal polar worksheet does not require four independent same-law
entries.  It requires the two scalar same-law responses

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

The antisymmetric weighted off-diagonal combination

$$
h_0\beta_{0A}-h_A\beta_{A0}
$$

is invisible to the minimal \(U_N\)-even polar defect.

### Corollary 59.3: Exact Trace-Norm Formula

If \(m,t\) are real, then

$$
\left\|
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}
\right)
\right\|_1
=
\max\{|m|,|t|\}.
$$

More generally, since \(I_2\) and \(U_N\) commute and \(U_N^2=I_2\),

$$
\left\|
\Pi_+^{U_N}
\left(
D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}
\right)
\right\|_1
=
{1\over2}\left(|m+t|+|m-t|\right)
$$

for complex \(m,t\) as well.

Proof.

The eigenprojections of \(U_N\) are

$$
P_\pm={1\over2}(I_2\pm U_N).
$$

Lemma 59.1 gives

$$
{m\over2}I_2+{t\over2}U_N
=
{m+t\over2}P_+
+{m-t\over2}P_-.
$$

The displayed trace-norm formula follows.  For real \(m,t\), the elementary
identity

$$
{1\over2}\left(|m+t|+|m-t|\right)=\max\{|m|,|t|\}
$$

finishes the proof.  `square`

### Corollary 59.4: The Optimistic Switch-Odd Model Revisited

For the Paper-30 optimistic model

$$
B_{\Gamma_1}^{N,j}
=
\Sigma_{\mathrm{odd}}
=
\begin{pmatrix}
b_N&-a_N\\
-a_N&-b_N
\end{pmatrix},
$$

one has

$$
m=b_N(h_0-h_A),
\qquad
t=0.
$$

Thus the leakage in Lemma 55.2 is exactly the identity-mode response \(m\).
The crossing-mode response \(t\) cancels, but the heat-weighted identity mode
does not.

## 60. The Minimal Ward Attempt

The rank-two compression makes the Ward route sharper.  Instead of trying to
source all entries of \(B_{\Gamma_1}^{N,j}\), one only has to source \(m\)
and \(t\).

Define the two minimal polar observables

$$
V_I(B):=
\operatorname{Tr}
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)=m,
$$

and

$$
V_U(B):=
\operatorname{Tr}
\left[
U_N\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
\right]=t.
$$

Then every minimal polar response is a deterministic linear combination of
\(V_I\) and \(V_U\).

### Definition 60.1: Two-Scalar Minimal Ward Package

The theorem

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD2}(\varepsilon)
$$

means that there exist same-law source operators
\(\mathcal L_{N,j}^{src}\), finite potentials \(G_I,G_U\), and residuals
\(\mathcal R_I,\mathcal R_U\) such that

$$
V_I=\mathcal L_{N,j}^{src}G_I+\mathcal R_I,
\qquad
V_U=\mathcal L_{N,j}^{src}G_U+\mathcal R_U,
$$

with the source terms centered under the active adaptive law and

$$
\left|
\mathbf E_{\mu_{N,j}^{ad}}\mathcal R_I
\right|
\le\varepsilon,
\qquad
\left|
\mathbf E_{\mu_{N,j}^{ad}}\mathcal R_U
\right|
\le\varepsilon.
$$

### Lemma 60.2: Ward2 Is Equivalent To Minimal Polar Ward

At the two-channel cutoff,

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD2}(\varepsilon)
$$

implies

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD}(C_2\varepsilon),
$$

where \(C_2\) is the fixed finite duality constant for the two-dimensional
polar test family.  Conversely, minimal polar Ward implies Ward2 with the
same order of error after testing against \(I_2\) and \(U_N\).

Proof.

Lemma 59.1 shows that the polar defect lies in the span of \(I_2\) and
\(U_N\).  Hence every polar test only evaluates \(m\) and \(t\).  Testing
against \(I_2\) and \(U_N\) recovers \(m\) and \(t\), and finite-dimensional
duality supplies the constant \(C_2\).  `square`

### Proposition 60.3: Gauge Ward Identities Alone Do Not Source Ward2

The existing gauge/Haar Ward identities in the corpus do not imply
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}WARD2}(\varepsilon)\).

Proof.

The two surviving observables \(V_I\) and \(V_U\) are scalar intertwiners on
the already gauge-invariant singlet-adjoint block.  Infinitesimal gauge
variation kills non-invariant directions, but it does not force a scalar
intertwiner coefficient to vanish.  Algebraically, the family

$$
B=cI_2
$$

is compatible with the same finite gauge covariance constraints for every
scalar \(c\), while

$$
m=c(h_0+h_A),
\qquad
t=ca_N(h_0-h_A).
$$

Unless extra actual-law response information fixes \(c\), gauge Ward
identities cannot bound \(m\) or \(t\).  Therefore Ward2 is a genuine new
same-law analytic input, not a consequence of the current structural Ward
ledger.  `square`

### Corollary 60.4: What Would Count As A Positive Ward Breakthrough

A positive Ward breakthrough must be stronger than gauge invariance.  It must
produce an actual-law centered source equation for the scalar pair

$$
(m,t)
$$

itself.  The smallest acceptable theorem is therefore:

$$
\left|
\mathbf E_{\mu_{N,j}^{ad}}m
\right|
\le\varepsilon,
\qquad
\left|
\mathbf E_{\mu_{N,j}^{ad}}t
\right|
\le\varepsilon,
$$

or the same bounds with a controlled finite tail and a cofinal selector.

## 61. The Exact Positive And Negative Two-Scalar Tests

The explicit algebra gives a clean decision table.

### Theorem 61.1: Two-Scalar Branch-A Test

At the minimal heat-bad crossing block:

1. the positive switch/curvature route needs

   $$
   |m|\le\eta,
   \qquad
   |t|\le\eta,
   $$

   with \(\eta\) below the remaining bridge budget after curvature and tail;

2. the Ward route needs a same-law centered source theorem for \(m\) and
   \(t\);

3. the floor route needs a sign-coherent lower bound for either \(m\), \(t\),
   or a polar combination \((m+t)/2\), \((m-t)/2\) in the \(U_N\)-eigenbasis.

Proof.

The first item is Corollary 59.3.  The second is Lemma 60.2.  The third is
the dual trace-norm representation in the \(U_N\)-eigenbasis:

$$
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
=
{m+t\over2}P_+
+{m-t\over2}P_-.
$$

Thus any lower floor is a sign-coherent lower bound on one of these two
eigenchannel amplitudes, or on a deterministic polar recombination of them.
`square`

### Corollary 61.2: The New Smallest Primitive Target

The target is now smaller than `MINPOL-BTABLE`.  It is the two-scalar theorem

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE}(\varepsilon):
\qquad
(m,t)\hbox{ are sourced to error }\varepsilon.
$$

It has three useful exits:

$$
\mathrm{MTABLE\text{-}SMALL},
\qquad
\mathrm{MTABLE\text{-}WARD},
\qquad
\mathrm{MTABLE\text{-}FLOOR}.
$$

This is the smallest currently visible same-law value theorem inside Branch
A.  It is not a label theorem, not a comparison-measure theorem, and not a
heat-kernel substitution.

## 62. Current-Corpus Verdict After The Explicit Algebra

The explicit computation is a real simplification, but it is not yet a
closure theorem.

### Theorem 62.1: Minimal Two-Scalar Source Gap

The current corpus does not prove any of

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}SMALL},
\qquad
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}WARD},
\qquad
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}FLOOR}.
$$

Proof.

Papers 23 through 31 provide the selector law, residual atom identities,
finite-table reductions, source-response dictionary, and heat-bad polar
certificate structure.  None prints the actual scalar values \(m,t\), none
prints a centered source equation for them with small residual, and none
prints a retained ledger sign for a lower floor in the \(I_2,U_N\) polar
directions.  Proposition 60.3 also shows that ordinary gauge/Haar Ward
identities cannot fill the gap, because \(m,t\) are scalar intertwiner
coefficients rather than non-invariant directions.  Hence the two-scalar
source gap remains.  `square`

### Corollary 62.2: Best Next Attack

The next positive attempt should attack \(m\) and \(t\) directly, in this
order:

1. try to derive a non-gauge Ward/Stein identity for the scalar pair from the
   adaptive selector source itself;
2. if that fails, try to prove sign-coherent lower floor for \(m\), \(t\), or
   \((m\pm t)/2\);
3. if both fail, record that the heat-bad polar route is closed at
   current-corpus level and move the global program to the next primitive
   same-law analytic input.

This keeps the program Barandes-aligned: all objects remain deterministic
finite source probes evaluated under the same actual adaptive law, with no
hidden Markov process and no replacement heat-kernel measure.

## 63. Source Pressures For The Two Scalars

The scalar compression from Section 59 makes the next source-response target
fully explicit.  Define the two same-law scalar observables

$$
M_{\Gamma_1}^{N,j}:=m,
\qquad
T_{\Gamma_1}^{N,j}:=t.
$$

Here \(M,T\) denote the raw finite observables before expectation.  The
lowercase \(m,t\) of the finite table are recovered by actual-law expectation
whenever \(B_{\Gamma_1}^{N,j}\) is interpreted as the averaged table.  The
compression of Lemma 59.1 is linear, so it applies in either convention.

At fixed \((N,j)\), define the two-parameter source pressure

$$
\Psi_{MT}^{N,j}(s,u)
:=
\log
\mathbf E_{\mu_{N,j}^{ad}}
\exp\left\{
sM_{\Gamma_1}^{N,j}
+uT_{\Gamma_1}^{N,j}
\right\}.
$$

This is a same-law pressure in the Paper-31 sense.  The parameters \(s,u\)
are deterministic probes.  They do not define a substitute dynamics.

### Lemma 63.1: First Responses Are Exactly The Two Missing Scalars

At fixed \((N,j)\),

$$
\partial_s\Psi_{MT}^{N,j}(0,0)
=
\mathbf E_{\mu_{N,j}^{ad}}M_{\Gamma_1}^{N,j},
$$

and

$$
\partial_u\Psi_{MT}^{N,j}(0,0)
=
\mathbf E_{\mu_{N,j}^{ad}}T_{\Gamma_1}^{N,j}.
$$

Proof.

This is Lemma 1.2 of Paper 31 applied to the two-observable family
\((M_{\Gamma_1}^{N,j},T_{\Gamma_1}^{N,j})\).  `square`

### Lemma 63.2: Curvature Is The Two-Scalar Covariance Matrix

The Hessian of \(\Psi_{MT}^{N,j}\) at the origin is

$$
\nabla^2\Psi_{MT}^{N,j}(0,0)
=
\begin{pmatrix}
\operatorname{Var}(M)&\operatorname{Cov}(M,T)\\
\operatorname{Cov}(T,M)&\operatorname{Var}(T)
\end{pmatrix},
$$

where all covariances are under \(\mu_{N,j}^{ad}\).

Proof.

This is Lemma 1.3 of Paper 31.  `square`

### Definition 63.3: Two-Scalar Source Smallness

For \(\eta\ge0\), write

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}SMALL}(\eta)
$$

if

$$
\left|
\partial_s\Psi_{MT}^{N,j}(0,0)
\right|
\le\eta,
\qquad
\left|
\partial_u\Psi_{MT}^{N,j}(0,0)
\right|
\le\eta
$$

cofinally on the active adaptive law, with the already separated
Peter-Weyl/tail lift.

This is exactly the positive scalar source theorem needed by Route I.

## 64. Minimal Scalar Centering Attempt

The most promising positive route would be a same-law involution that makes
\((M,T)\) odd, or nearly odd, while paying only a controlled
Radon-Nikodym defect.

### Definition 64.1: Scalar Centering Involution

For \(\omega,\eta\ge0\), write

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}CENTER}(\omega,\eta)
$$

if there exists a measurable involution \(\mathscr S\) of the actual finite
adaptive probability space such that:

1. its Radon-Nikodym logarithm satisfies

   $$
   \left\|
   \log {d(\mathscr S_*\mu_{N,j}^{ad})\over d\mu_{N,j}^{ad}}
   \right\|_\infty
   \le\omega;
   $$

2. the two scalar observables are nearly odd:

   $$
   \left|M\circ\mathscr S+M\right|\le\eta,
   \qquad
   \left|T\circ\mathscr S+T\right|\le\eta.
   $$

### Lemma 64.2: Centering Involution Gives Source Smallness

If

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}CENTER}(\omega,\eta)
$$

holds and \(M,T\) are normalized to \(\|M\|_\infty,\|T\|_\infty\le1\), then

$$
\left|
\mathbf E_{\mu_{N,j}^{ad}}M
\right|
\le {\eta\over2}+{e^\omega-1\over2},
\qquad
\left|
\mathbf E_{\mu_{N,j}^{ad}}T
\right|
\le {\eta\over2}+{e^\omega-1\over2}.
$$

Proof.

For a scalar \(X\in\{M,T\}\),

$$
\mathbf E[X]
=
{1\over2}\mathbf E[X+X\circ\mathscr S]
+{1\over2}\left(\mathbf E[X]-\mathbf E[X\circ\mathscr S]\right).
$$

The first term has absolute value at most \(\eta/2\).  The second term is
controlled by the RN oscillation:

$$
\left|
\mathbf E_\mu X-\mathbf E_{\mathscr S_*\mu}X
\right|
\le
\mathbf E_\mu
\left|
1-{d(\mathscr S_*\mu)\over d\mu}
\right|
\le e^\omega-1
$$

for \(\|X\|_\infty\le1\).  The displayed estimate follows.  For unnormalized
finite worksheets the right-hand side is multiplied by the relevant scalar
range.  `square`

### Proposition 64.3: The Known Crossing Switch Cannot Center \(M,T\)

The Paper-30 crossing involution \(U_N\) does not supply
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}CENTER}\).

Proof.

The quantities \(M,T\) are precisely the coefficients of the \(U_N\)-even
projection

$$
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
=
{M\over2}I_2+{T\over2}U_N.
$$

Conjugating by \(U_N\) fixes both basis elements \(I_2\) and \(U_N\):

$$
U_NI_2U_N=I_2,
\qquad
U_NU_NU_N=U_N.
$$

Therefore the known crossing switch fixes the two scalar coefficients of the
even projection rather than changing their sign.  It can define the
projection; it cannot center the projection it has already made even.
`square`

### Proposition 64.4: Selector Relabeling Alone Cannot Center \(M,T\)

Any involution that only relabels licensed selector names, while preserving
the numerical block product \(B_{\Gamma_1}^{N,j}\), cannot prove
\(\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}CENTER}\) unless \(M,T\) are
already small.

Proof.

The scalar pair \(M,T\) is a deterministic function of the numerical matrix
\(B_{\Gamma_1}^{N,j}\) and the structural constants \(a_N,b_N,h_0,h_A\).
If a relabeling does not change that numerical matrix, then
\(M\circ\mathscr S=M\) and \(T\circ\mathscr S=T\).  The near-odd conditions
become

$$
|2M|\le\eta,
\qquad
|2T|\le\eta.
$$

Thus relabeling proves no new centering theorem; it only restates the desired
smallness.  `square`

### Corollary 64.5: What A New Centering Symmetry Would Have To Do

A successful centering theorem must be a genuine same-law transformation of
the actual residual/signed product, not a recoupling conjugation or selector
renaming.  It must change the scalar pair approximately as

$$
(M,T)\mapsto(-M,-T)
$$

while paying a small actual-law RN defect.  No such transformation is printed
in Papers 20 through 31.

## 65. Minimal Scalar Ward No-Go At Current-Corpus Level

The Ward route remains meaningful, but the explicit scalar algebra tells us
what kind of Ward identity would be required.

### Theorem 65.1: Current Ward Data Do Not Determine \(M,T\)

The current corpus does not imply a centered source equation for
\((M,T)\).

Proof.

There are three available structural sources:

1. gauge/Haar invariance;
2. crossing recoupling;
3. selector admissibility/relabeling.

Gauge/Haar invariance was already ruled out in Proposition 60.3: \(M,T\) are
scalar intertwiner coefficients, and scalar intertwiner coefficients are not
forced to vanish by infinitesimal gauge invariance.

Crossing recoupling was ruled out in Proposition 64.3: \(M,T\) are the
coefficients of the \(U_N\)-even projection and are fixed, not negated, by
the known crossing switch.

Selector relabeling was ruled out in Proposition 64.4: if the numerical
matrix \(B_{\Gamma_1}^{N,j}\) is unchanged, the scalar pair is unchanged.

No other same-law transformation or Stein operator is printed by the current
corpus with a residual estimate on this scalar pair.  Hence the Ward route is
not closed at current-corpus level.  `square`

### Corollary 65.2: The Ward Exit Is A New Analytic Input

The precise missing Ward theorem is

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}WARD}(\varepsilon):
\qquad
\left|
\mathbf E_{\mu_{N,j}^{ad}}M
\right|
+\left|
\mathbf E_{\mu_{N,j}^{ad}}T
\right|
\le\varepsilon,
$$

sourced by a non-gauge same-law Stein identity or a new centering involution
with controlled RN defect.

This is not supplied by the existing Barandes-aligned bookkeeping.  It is a
primitive same-law analytic theorem.

## 66. Two-Scalar Floor Test

If the two scalars cannot be centered, the same algebra gives the exact floor
tests.

Define the \(U_N\)-eigenchannel amplitudes

$$
\lambda_+
:=
{M+T\over2},
\qquad
\lambda_-
:=
{M-T\over2}.
$$

Then

$$
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
=
\lambda_+P_+
+\lambda_-P_-.
$$

### Definition 66.1: Two-Scalar Floor

For \(M_*>0\), write

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}FLOOR}(M_*)
$$

if one of the four signed scalar functionals

$$
M,\qquad T,\qquad \lambda_+,\qquad \lambda_-
$$

has a retained Branch-A ledger sign and actual-law expectation at least
\(M_*\) after quotient and tail margins.

### Lemma 66.2: Large Unsigned Defect Produces A Floor Candidate, Not A Floor

If

$$
\left\|
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
\right\|_1
\ge 2M_*,
$$

then at least one of \(|\lambda_+|\) or \(|\lambda_-|\) is at least
\(M_*\).  However this gives only an unsigned floor candidate.  To become a
Branch-A floor theorem, the sign must be retained in the licensed ledger.

Proof.

The trace norm is

$$
|\lambda_+|+|\lambda_-|.
$$

If the sum is at least \(2M_*\), then one term is at least \(M_*\).  The
second statement is the signed-ledger condition from the Paper-30 and
Paper-32 floor routes: absolute size alone does not determine whether the
term survives with the needed confinement sign.  `square`

### Proposition 66.3: Current-Corpus Floor Verdict

The current corpus does not prove

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}FLOOR}(M_*).
$$

Proof.

Sections 59 through 61 identify the only possible minimal floor functionals:
\(M,T,\lambda_+,\lambda_-\).  Papers 20 through 31 do not print their
actual-law expectations and do not print a retained sign-coherence theorem
for any of them.  Therefore the floor route is sharpened, but not closed.
`square`

## 67. Endpoint Of The \(M,T\) Attack

The two-scalar attack has explored the three exits promised in Corollary
62.2.

### Theorem 67.1: The Minimal Scalar Route Is Settled At Current-Corpus Level

At the smallest heat-bad polar block:

1. source pressures for \(M,T\) are well-defined and their first derivatives
   are exactly the two missing scalar values;
2. the known crossing switch cannot center \(M,T\), because \(M,T\) are the
   coefficients of the \(U_N\)-even projection;
3. gauge/Haar Ward identities cannot center \(M,T\), because \(M,T\) are
   scalar intertwiner coefficients;
4. selector relabeling cannot center \(M,T\) unless it already changes the
   numerical matrix \(B_{\Gamma_1}^{N,j}\);
5. the floor route is exactly the sign-coherent lower-bound problem for
   \(M,T,\lambda_+,\lambda_-\).

Thus the minimal scalar route is not closed positively or negatively by the
current corpus.  The remaining theorem is genuinely new same-law quantitative
information:

$$
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}SMALL}
\quad\hbox{or}\quad
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}WARD}
\quad\hbox{or}\quad
\mathrm{P32\text{-}HKBAD\text{-}MINPOL\text{-}MTABLE\text{-}FLOOR}.
$$

Proof.

Items 1 through 5 are Lemma 63.1, Proposition 64.3, Theorem 65.1,
Proposition 64.4, and Proposition 66.3.  `square`

### Corollary 67.2: Strategic Consequence

Inside Paper 32, further progress requires a new actual-law quantitative
theorem for the two scalar source responses \(M,T\).  If that theorem is not
available, the rational next step is not more heat-bad algebra.  It is to
move to a different primitive same-law analytic input from the Paper-31 menu:
low-mode source response gap, mixed RN-MIXAMP Ward/curvature control,
nonlinear source-Dobrushin upgrade, connected source-cumulant decay,
same-law Peter-Weyl regularity/tail, or sign-coherent lower floor.

## 68. Same-Law Peter-Weyl Regularity/Tail As The Next Input

Rather than start a new paper, we continue here with the next primitive input
from Corollary 67.2: same-law Peter-Weyl regularity and tail.  This route is
worth testing because it is not another attempt to recover an exact hidden
value.  It asks whether compact-group regularity of the actual finite DLR
integrand can control omitted high representations.

The tail obstruction occurs in several places:

1. Paper 28 needs a same-law Peter-Weyl tail for the RN-MIXAMP conditional
   transfer.
2. Paper 29 needs tail control before low-mode entries can be promoted to a
   full residual value theorem.
3. Paper 30 needs residual-score Peter-Weyl tails in its signed/bridge
   Ward and low-mode-plus-tail routes.
4. Earlier sections of this paper need the already separated omitted-mode
   tail before a finite quotient or polar certificate can be lifted.

All of these demands have the same logical form: a finite Peter-Weyl
projection is honest only if the complement is controlled under the same
actual adaptive law.

### Definition 68.1: Common Same-Law Peter-Weyl Tail

Let \(G^m\) be the finite compact-group chart for a retained row.  Let
\(\Pi_{\le L}\) be the Peter-Weyl projection onto tensor representations with
declared Casimir cutoff at most \(L\).  For a finite family of actual-law
observables \({\mathcal F}^{N,j}\), define

$$
\mathfrak T_L^{N,j}({\mathcal F})
:=
\sup_{F\in{\mathcal F}^{N,j}}
\left\|
(I-\Pi_{\le L})F
\right\|_{\mathcal N},
$$

where \(\|\cdot\|_{\mathcal N}\) is the norm demanded by the live route:
operator norm, trace-dual norm, \(L^2\) score-pairing norm, or scalar source
response norm.

The theorem

$$
\mathrm{P32\text{-}SLAW\text{-}PWTAIL}(L,r_L;{\mathcal F})
$$

asserts

$$
\limsup_{(N,j)}
\mathfrak T_{L(N,j)}^{N,j}({\mathcal F})
\le r_L.
$$

This is the common tail theorem behind the Paper-28, Paper-29, Paper-30, and
Paper-32 tail clauses.

### Definition 68.2: Common Fourier Source Tail

Equivalently, for each Peter-Weyl matrix coefficient probe
\(D_{\lambda,mn}^F\) associated to \(F\in{\mathcal F}^{N,j}\), define

$$
\Psi_{\lambda,mn,F}^{PW}(s)
:=
\log
\mathbf E_{\mu_{N,j}^{ad}}
\exp\left\{
sD_{\lambda,mn}^F
\right\}.
$$

The source-tail theorem is the summability of first responses:

$$
\sum_{C_2(\lambda)>L}
w_\lambda
\sup_{F,m,n}
\left|
\partial_s
\Psi_{\lambda,mn,F}^{PW}(0)
\right|
\le r_L.
$$

This is exactly the Paper-31 source-response form of Peter-Weyl tail decay.

## 69. A Real Positive Sufficient Theorem: Sobolev Tail

The compact-group route is not empty.  It has a clean positive theorem: if
the actual finite DLR observables have cofinal Sobolev regularity, their
Peter-Weyl tails decay.

Let \(\Delta\) be the positive Laplace-Casimir operator on the finite
compact-group chart \(G^m\).  Let \(\Lambda_{L+1}\) be the first Casimir
eigenvalue above the cutoff.

### Definition 69.1: Same-Law Sobolev Regularity

For \(q>0\) and \(A<\infty\), write

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}(q,A;{\mathcal F})
$$

if

$$
\limsup_{(N,j)}
\sup_{F\in{\mathcal F}^{N,j}}
\left\|
(I+\Delta)^{q/2}F
\right\|_{2,\mu_{N,j}^{ad}}
\le A.
$$

The Sobolev norm is computed on the actual finite DLR chart and with the
actual finite density.  No comparison heat law is substituted.

### Lemma 69.2: Sobolev Regularity Implies \(L^2\) Tail

If

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}(q,A;{\mathcal F})
$$

holds and the actual \(L^2\) norm is uniformly equivalent to Haar \(L^2\) on
the retained chart with equivalence constant \(C_\rho\), then

$$
\left\|
(I-\Pi_{\le L})F
\right\|_{2,\mu_{N,j}^{ad}}
\le
C_\rho A(1+\Lambda_{L+1})^{-q/2}
$$

cofinally, uniformly for \(F\in{\mathcal F}^{N,j}\).

Proof.

In the Peter-Weyl basis,

$$
\left\|
(I-\Pi_{\le L})F
\right\|_2^2
\le
(1+\Lambda_{L+1})^{-q}
\left\|
(I+\Delta)^{q/2}F
\right\|_2^2.
$$

The same estimate in the actual \(L^2\) norm follows from the declared
uniform equivalence between actual and Haar \(L^2\).  `square`

### Lemma 69.3: Analytic Regularity Gives Exponential Tail

If the same-law observables extend to a fixed complex tube in the compact
group complexification with uniformly bounded analytic norm, then their
Peter-Weyl coefficients obey an exponential Casimir tail of the form

$$
\mathfrak T_L^{N,j}({\mathcal F})
\le
A e^{-c\sqrt{\Lambda_{L+1}}}
$$

in the corresponding coefficient norm.

Proof.

This is the standard compact-group Paley-Wiener principle: analytic
continuation to a fixed tube gives exponential decay of Peter-Weyl
coefficients.  The statement is included only as a conditional theorem.  The
fixed tube and uniform analytic norm must be proved for the actual adaptive
DLR observables.  `square`

### Corollary 69.4: Positive Export

Either

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}(q,A;{\mathcal F})
$$

with \(q\) large enough, or a uniform analytic theorem as in Lemma 69.3,
would source the omitted-mode tail used by Papers 28 through 32.  In
particular it would convert finite low-mode or finite polar certificates into
full certificates, provided the retained low-mode body has already beaten its
margin.

## 70. Why Heat-Kernel Smoothness Alone Does Not Source The Tail

The tempting thought is that every retained row contains heat kernels, so
Peter-Weyl decay should be automatic.  This is false at the level needed
here.

### Proposition 70.1: Heat Reference Tail Is Not Actual Residual Tail

The heat-kernel factor supplies Casimir damping for the clean heat reference
rows.  It does not by itself prove
\(\mathrm{P32\text{-}SLAW\text{-}PWTAIL}\) for the actual adaptive residual
observables.

Proof.

The live observables are not just the heat-kernel density.  They include,
depending on the route, conditional ratios, central-entry divisions,
normalizations, residual Hamiltonians, signed bridge factors, Jacobian
factors, selector restrictions, logarithms, and residual-score derivatives.
Schematically, the finite DLR integrand has the form

$$
\rho^{N,j}
=
\left(\prod_p H_{t_p}(h_p)\right)
e^{-V_{RPF}^{N,j}}
J_{tree}^{N,j}
\times
\hbox{selector and normalization factors}.
$$

Multiplication by \(e^{-V_{RPF}}\), division by conditional normalizers, and
application of residual-score derivatives can create or amplify high
Peter-Weyl coefficients.  Heat damping of the clean factor transfers only if
one proves a same-law multiplier theorem bounding the residual and selector
factors in the relevant Sobolev or analytic norm.  No such theorem is printed
in the current corpus.  `square`

### Proposition 70.2: Finite Dimensionality Is Not A Cofinal Tail Bound

At each fixed retained row, every actual observable has a finite
Peter-Weyl expansion if an explicit cutoff is imposed.  This does not imply a
cofinal tail theorem.

Proof.

The confinement argument needs a cutoff schedule whose omitted tail is small
uniformly along the cofinal selector.  Fixed-row finiteness gives no control
on how the Sobolev norm, analytic tube, or coefficient mass grows with
\((N,j)\).  The obstruction is therefore not finite existence of a
decomposition; it is cofinal quantitative regularity.  `square`

## 71. Same-Law Multiplier Route And Its Missing Inputs

There is one plausible route to a positive theorem: prove that the non-heat
factors are tame multipliers on Peter-Weyl Sobolev spaces.

### Definition 71.1: Residual Multiplier Tameness

For \(q>0\) and \(B<\infty\), write

$$
\mathrm{P32\text{-}SLAW\text{-}MULT}(q,B)
$$

if multiplication by every actual residual/Jacobian/selector factor appearing
in the live observables has Sobolev operator norm at most \(B\) on
\(H^q(G^m)\), cofinally on the active adaptive law.

### Lemma 71.2: Multiplier Tameness Transfers Heat Tail

Assume:

1. the clean heat-kernel factor has Sobolev or analytic tail
   \(\mathfrak T_L^{HK}\le r_L^{HK}\);
2. `P32-SLAW-MULT(q,B)` holds for the residual/Jacobian/selector factors;
3. all conditional normalizers are bounded away from zero by \(Z_*>0\).

Then the actual observables generated by multiplying the clean heat factor by
those residual factors obey

$$
\mathfrak T_L^{act}
\le
C(B,Z_*)r_L^{HK}
+\mathrm{Comm}_L(q,B),
$$

where \(\mathrm{Comm}_L(q,B)\) is the standard projection-commutator tail
from multiplying then projecting.  If the multiplier family is uniformly
smooth enough that \(\mathrm{Comm}_L(q,B)\to0\), then
`P32-SLAW-PWTAIL` follows.

Proof.

Write the actual observable as \(MF_{HK}/Z\), where \(M\) is the product of
residual, Jacobian, selector, and score factors.  The multiplier bound gives
\(\|MF\|_{H^q}\le B\|F\|_{H^q}\).  The lower normalizer bound pays the
division by \(Z\).  Apply Lemma 69.2 to \(MF/Z\).  If the proof is carried
out by comparing projected heat tails before and after multiplication, the
usual commutator term appears; uniform smoothness makes it vanish with the
cutoff.  `square`

### Proposition 71.3: Multiplier Tameness Is Not Sourced

The current corpus does not prove `P32-SLAW-MULT(q,B)` in any closing range.

Proof.

Papers 28 through 31 identify the residual Hamiltonian, residual-score,
bridge, and selector factors as actual same-law finite objects.  They do not
bound their cofinal Sobolev multiplier norms, analytic tubes, projection
commutators, or normalizer lower constants in the strength required by
Lemma 71.2.  The finite DLR localization from Paper 30 makes the theorem
well-posed, but not automatically true.  `square`

## 72. Floor Alternative For High Peter-Weyl Tails

Failure of a tail theorem does not automatically prove confinement failure
or success.  A high-mode tail can also become a lower-floor witness if it is
large with the correct sign.

### Definition 72.1: High-Mode Tail Floor

For \(M_*>0\), write

$$
\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR}(M_*)
$$

if a deterministic cofinal family of high-mode Peter-Weyl probes
\(D_{\lambda,mn}^{F}\), with \(C_2(\lambda)>L(N,j)\), has retained
sign-coherent source slope

$$
\left|
\partial_s\Psi_{\lambda,mn,F}^{PW}(0)
\right|
\ge M_*
$$

after quotient, orientation, normalization, and tail ledger conventions are
applied.

### Proposition 72.2: Current-Corpus Tail Floor Verdict

The current corpus does not prove
\(\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR}(M_*)\).

Proof.

The source-response calculus identifies high-mode coefficients as first
responses.  It does not evaluate their sign, orientation, or retained
ledger contribution.  Papers 28 through 30 explicitly distinguish failure of
tail smallness from a sign-coherent lower floor.  No current paper prints a
deterministic high-mode coefficient with the required retained sign and
lower bound.  `square`

## 73. Verdict On The Same-Law Peter-Weyl Tail Route

### Theorem 73.1: Peter-Weyl Tail Route Is Reduced To Regularity Or Floor

Inside Paper 32, the same-law Peter-Weyl route has the following exact
status.

1. A cofinal Sobolev theorem or uniform analytic theorem for the actual
   adaptive observables would source a Peter-Weyl tail.
2. Heat-kernel smoothness alone does not source the actual residual tail.
3. The plausible transfer theorem requires residual multiplier tameness,
   projection-commutator control, and normalizer lower bounds.
4. None of those regularity inputs is printed by the current corpus.
5. A high-mode sign-coherent floor would be a valid negative/floor exit, but
   no such floor witness is printed either.

Therefore the Peter-Weyl tail route is not closed positively or negatively by
the current corpus.  Its live primitive theorem is

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}
\quad\hbox{or}\quad
\mathrm{P32\text{-}SLAW\text{-}MULT}
\quad\hbox{or}\quad
\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR}.
$$

Proof.

Items 1 through 5 are Lemmas 69.2 and 69.3, Propositions 70.1 and 70.2,
Lemma 71.2, Proposition 71.3, and Proposition 72.2.  `square`

### Corollary 73.2: Strategic Consequence

Paper 32 has now pursued two primitive same-law analytic inputs after the
source-response reframing:

1. the heat-bad minimal scalar route, reduced to \(M,T\);
2. the same-law Peter-Weyl tail route, reduced to actual regularity,
   multiplier tameness, or a high-mode floor.

Both are honest analytic targets, and neither is supplied by the current
corpus.  The next positive push should therefore choose whether to attack
actual Sobolev/multiplier regularity directly, or move to another primitive
input: nonlinear source-Dobrushin, connected source-cumulant decay, or mixed
RN-MIXAMP Ward/curvature control.

## 74. The Six-Gate Peter-Weyl Transfer Worksheet

We now investigate the exact six targets needed to turn clean heat-kernel
damping into an actual same-law Peter-Weyl tail:

1. same-law Sobolev regularity;
2. residual multiplier tameness;
3. conditional normalizer lower bounds;
4. projection commutator control;
5. residual-score regularity;
6. high-mode sign-coherent floor.

The clean heat tail can be used only after these gates are made explicit.

### Definition 74.1: Six-Gate Transfer Package

For a finite family \({\mathcal F}^{N,j}\) of actual observables, define

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}XFER}
(q,A,B,Z_*,c_L,\sigma_L)
$$

to mean the conjunction of:

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}(q,A;{\mathcal F}),
$$

$$
\mathrm{P32\text{-}SLAW\text{-}MULT}(q,B),
$$

$$
\mathrm{P32\text{-}SLAW\text{-}ZNORM}(Z_*),
$$

$$
\mathrm{P32\text{-}SLAW\text{-}COMM}(q,c_L),
$$

and, when Ward/score insertions are present,

$$
\mathrm{P32\text{-}SLAW\text{-}SCORE\text{-}SOB}(q,\sigma_L).
$$

The sixth gate is the alternative

$$
\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR}(M_*),
$$

which closes negatively rather than transferring heat damping.

### Theorem 74.2: Six-Gate Transfer Theorem

Assume the clean heat-kernel family has tail \(r_L^{HK}\).  If

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}XFER}
(q,A,B,Z_*,c_L,\sigma_L)
$$

holds and \(c_L+\sigma_L\to0\) along the selected cutoff schedule, then the
actual family obeys

$$
\mathfrak T_L^{act}
\le
{C_qB\over Z_*}r_L^{HK}
+c_L+\sigma_L.
$$

In particular, if the right-hand side lies below the live tail budget, the
same-law Peter-Weyl tail gate closes.

Proof.

The clean tail is first multiplied by the residual/Jacobian/selector factors.
The multiplier bound pays \(B\).  The lower normalizer bound pays \(Z_*^{-1}\).
The projection commutator pays \(c_L\).  If score insertions are present, the
score Sobolev/tail gate pays \(\sigma_L\).  Lemmas 69.2 and 71.2 then give
the displayed estimate.  `square`

### Corollary 74.3: Current-Corpus Six-Gate Status

The current corpus does not prove the six-gate transfer package.  Sections
75 through 80 identify exactly where each gate stands.

## 75. Gate 1: Same-Law Sobolev Regularity

The first target is the direct Sobolev theorem.

### Definition 75.1: Route-Specific Sobolev Target

For the heat-bad, RN-MIXAMP, signed-bridge, and residual-score routes, let
\({\mathcal F}_{route}^{N,j}\) be the corresponding actual observable family.
The target is

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}
(q,A;{\mathcal F}_{route}).
$$

### Lemma 75.2: What Would Prove Gate 1

Gate 1 follows if the actual finite DLR density \(\rho^{N,j}\) and all route
observables \(F\in{\mathcal F}_{route}^{N,j}\) obey a cofinal derivative
bound

$$
\sup_{|\alpha|\le q}
\left\|
X^\alpha F
\right\|_{2,\mu_{N,j}^{ad}}
\le A_q
$$

for a \(q\) exceeding the dimension-dependent summability threshold.

Proof.

On compact Lie groups, Sobolev norms are equivalent to finite sums of
left-invariant derivative norms.  The Peter-Weyl Laplacian is the
Casimir.  Thus the displayed derivative bound is the Sobolev bound of
Definition 69.1.  `square`

### Proposition 75.3: Gate 1 Is Not Sourced

The current corpus does not prove Gate 1.

Proof.

Papers 28 through 31 define the relevant actual observables and source
coefficients, but do not bound their cofinal left-invariant derivatives.
Paper 30 gives finite DLR localization, which makes the derivative problem
well-defined at a fixed row.  It does not bound \(X^\alpha V_{RPF}\),
\(X^\alpha\log J_{tree}\), selector boundary derivatives, conditional ratio
derivatives, or logarithmic normalizer derivatives uniformly along the
cofinal selector.  Therefore the Sobolev regularity theorem remains a new
same-law analytic input.  `square`

## 76. Gate 2: Residual Multiplier Tameness

The second target is the one that decides whether heat damping transfers
through the actual residual law.

### Definition 76.1: Route Multiplier Family

Let \({\mathcal M}_{route}^{N,j}\) be the finite family of multipliers
appearing in the route:

$$
e^{-V_{RPF}^{N,j}},
\qquad
J_{tree}^{N,j},
\qquad
\hbox{selector indicators or smooth selector weights},
\qquad
\hbox{conditional ratio factors},
\qquad
\hbox{logarithmic residual factors}.
$$

Gate 2 is

$$
\mathrm{P32\text{-}SLAW\text{-}MULT}(q,B):
\qquad
\|M f\|_{H^q}\le B\|f\|_{H^q}
$$

for every \(M\in{\mathcal M}_{route}^{N,j}\), cofinally.

### Lemma 76.2: Smooth Multiplier Criterion

If \(q>d/2\), where \(d=\dim(G^m)\), and

$$
\sup_{M\in{\mathcal M}_{route}^{N,j}}
\|M\|_{H^q}
\le B_q
$$

cofinally, then Gate 2 holds with a constant depending only on \(q,d,B_q\).

Proof.

For \(q>d/2\), \(H^q(G^m)\) is a Banach algebra and multiplication by an
\(H^q\) function is bounded on \(H^q\).  This is the standard compact
Sobolev multiplier theorem.  `square`

### Proposition 76.3: Gate 2 Is Not Sourced

The current corpus does not prove Gate 2.

Proof.

The residual factors are known as finite actual functions, but their Sobolev
multiplier norms are not bounded.  In particular, the corpus does not prove
cofinal \(H^q\) bounds for \(e^{-V_{RPF}}\), \(J_{tree}\), conditional ratio
factors, or selector weights after the adaptive SEL2 pushforward.  Sharp
finite labels and finite DLR localization do not imply Sobolev multiplier
tameness.  `square`

## 77. Gate 3: Conditional Normalizer Lower Bounds

The third target is the lower bound preventing conditional division from
amplifying high modes.

### Definition 77.1: Normalizer Gate

Let \(Z_B^{N,j}(\eta)\) denote the route's finite conditional normalizer.
For \(Z_*>0\), write

$$
\mathrm{P32\text{-}SLAW\text{-}ZNORM}(Z_*)
$$

if

$$
\liminf_{(N,j)} Z_B^{N,j}(\eta)\ge Z_*.
$$

### Lemma 77.2: Anchored Log Lower Bound

If the residual multiplier \(M\) satisfies

$$
\log M\ge -K
$$

cofinally relative to the normalized clean heat density, then

$$
Z_B^{N,j}(\eta)\ge e^{-K}
$$

after normalization of the clean heat conditional.

Proof.

With the clean heat density normalized,

$$
Z_B^{N,j}(\eta)
=
\mathbf E_{HK}[M].
$$

The log lower bound gives \(M\ge e^{-K}\) pointwise.  Taking expectation
under the normalized clean heat conditional gives the result.  A pure
oscillation bound would also suffice only if paired with an anchored
reference value for \(M\); oscillation alone is merely relative.  `square`

### Proposition 77.3: Gate 3 Is Not Sourced

The current corpus does not prove Gate 3 in a useful cofinal range.

Proof.

At each fixed row, compactness and positivity give \(Z_B^{N,j}(\eta)>0\).
The confinement argument needs a cofinal lower bound.  Current papers do not
bound the full residual multiplier below, and do not pair its oscillation
with an anchored reference value, once conditional ratios, selector
restrictions, logarithms, and Jacobians are included.  Therefore fixed-row
positivity is not the needed theorem.  `square`

## 78. Gate 4: Projection Commutator Control

The fourth target pays the fact that multiplication and Peter-Weyl projection
do not commute.

### Definition 78.1: Projection-Commutator Gate

For route multipliers \(M\) and clean functions \(F\), define

$$
\mathfrak C_L^{N,j}(M,F)
:=
\left\|
(I-\Pi_{\le L})(M\Pi_{\le L/2}F)
\right\|_{\mathcal N}.
$$

Write

$$
\mathrm{P32\text{-}SLAW\text{-}COMM}(q,c_L)
$$

if

$$
\limsup_{(N,j)}
\sup_{M,F}
\mathfrak C_L^{N,j}(M,F)
\le c_L,
\qquad
c_L\to0.
$$

### Lemma 78.2: Commutator Control From Multiplier Tail

If \(M\) has Peter-Weyl tail

$$
\|(I-\Pi_{\le L/2})M\|_{H^q}\le \epsilon_L
$$

and low modes multiply with the standard Clebsch-Gordan cutoff rule, then

$$
\mathfrak C_L^{N,j}(M,F)
\le C_q\epsilon_L\|F\|_{H^q}.
$$

Proof.

Split \(M=\Pi_{\le L/2}M+(I-\Pi_{\le L/2})M\).  The product of the two low
pieces has Peter-Weyl support below \(L\) up to the fixed Clebsch-Gordan
bookkeeping convention, so it is removed by \(I-\Pi_{\le L}\).  The remaining
term is controlled by the \(H^q\) algebra bound and the tail
\(\epsilon_L\).  `square`

### Proposition 78.3: Gate 4 Is Not Sourced

The current corpus does not prove Gate 4.

Proof.

Gate 4 requires a tail theorem for the multipliers themselves, or a direct
commutator estimate.  Papers 28 through 31 do not print multiplier
Peter-Weyl decay, and Sections 75 through 76 show that neither Sobolev
regularity nor multiplier tameness is currently sourced.  Therefore the
commutator gate remains open.  `square`

## 79. Gate 5: Residual-Score Regularity

The fifth target is needed whenever the proof uses Ward or Stein score
insertions.

### Definition 79.1: Residual-Score Sobolev Gate

Let the residual score family be

$$
{\mathcal S}^{N,j}
=
\left\{
X_{\ell,a}V_{RPF}^{N,j},
\,
X_{\ell,a}\log J_{tree}^{N,j},
\,
X_{\ell,a}\log Z_B^{N,j}
\right\}_{\ell,a}.
$$

Write

$$
\mathrm{P32\text{-}SLAW\text{-}SCORE\text{-}SOB}(q,\sigma_L)
$$

if the Peter-Weyl complement of all score pairings contributes at most
\(\sigma_L\), cofinally, with \(\sigma_L\to0\).

### Lemma 79.2: Score Regularity From One More Derivative

If \(V_{RPF}^{N,j}\), \(\log J_{tree}^{N,j}\), and \(\log Z_B^{N,j}\) have
uniform \(H^{q+1}\) bounds, then their first left-invariant derivatives have
uniform \(H^q\) bounds.  Consequently Gate 5 follows from Gate 1 at one
higher derivative order, applied to the residual logarithmic factors.

Proof.

Left-invariant differentiation maps \(H^{q+1}\) continuously into \(H^q\).
Apply Lemma 69.2 to the resulting score functions.  `square`

### Proposition 79.3: Gate 5 Is Not Sourced

The current corpus does not prove Gate 5.

Proof.

Paper 30 identifies the residual-score pairings and proves that a score-tail
theorem would imply the corresponding Ward smallness.  It also records that
the residual-score tail is not printed.  The present paper explains why:
one needs cofinal \(H^{q+1}\) or analytic control of the residual logarithmic
factors.  That derivative regularity is not supplied by Papers 20 through
31.  `square`

## 80. Gate 6: High-Mode Sign-Coherent Floor

The sixth target is the negative/floor exit.

### Definition 80.1: High-Mode Floor Witness Package

For \(M_*>0\), write

$$
\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR\text{-}PKG}(M_*)
$$

if there exists a deterministic high-mode probe \(D_{\lambda,mn}^{F}\) such
that:

1. \(C_2(\lambda)>L(N,j)\);
2. its actual source slope has magnitude at least \(M_*\);
3. its sign is retained through quotient, orientation, endpoint, and
   normalizer ledgers;
4. it contributes to the same Branch-A predebit rather than cancelling in a
   signed bridge or Ward pairing.

### Lemma 80.2: Floor Package Implies Tail Floor

If

$$
\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR\text{-}PKG}(M_*)
$$

holds, then

$$
\mathrm{P32\text{-}SLAW\text{-}PWTAIL\text{-}FLOOR}(M_*)
$$

holds.

Proof.

Definition 80.1 is Definition 72.1 with the sign-survival clauses expanded.
`square`

### Proposition 80.3: Gate 6 Is Not Sourced

The current corpus does not prove Gate 6.

Proof.

The corpus has repeatedly separated large unsigned tails from retained
sign-coherent floors.  It does not print a high-mode coefficient, its sign,
its quotient/endpoint survival, and its contribution to the Branch-A predebit
in one certified package.  Therefore no high-mode tail floor is currently
sourced.  `square`

## 81. Final Verdict On The Six Gates

### Theorem 81.1: Six-Gate Investigation Closed At Current-Corpus Level

The six targets have the following current status:

1. `P32-SLAW-PW-SOB` is a valid positive theorem, but unsourced.
2. `P32-SLAW-MULT` is the necessary transfer gate from clean heat damping to
   actual residual observables, but unsourced.
3. `P32-SLAW-ZNORM` is required for conditional divisions, and fixed-row
   positivity does not give the needed cofinal lower bound.
4. `P32-SLAW-COMM` follows from multiplier tail control, but is unsourced.
5. `P32-SLAW-SCORE-SOB` follows from one higher derivative of residual
   logarithmic factors, but is unsourced.
6. `P32-SLAW-PWTAIL-FLOOR-PKG` would close negatively, but is unsourced.

Consequently the complete positive transfer package

$$
\mathrm{P32\text{-}SLAW\text{-}PW\text{-}SOB}
\quad+\quad
\mathrm{P32\text{-}SLAW\text{-}MULT}
\quad+\quad
\mathrm{P32\text{-}SLAW\text{-}ZNORM}
\quad+\quad
\mathrm{P32\text{-}SLAW\text{-}COMM}
\quad+\quad
\mathrm{P32\text{-}SLAW\text{-}SCORE\text{-}SOB}
$$

is not proved by the current corpus.  The negative floor package is also not
proved.

Proof.

Items 1 through 6 are Propositions 75.3, 76.3, 77.3, 78.3, 79.3, and 80.3.
`square`

### Corollary 81.2: Strategic Consequence

The Peter-Weyl route is now as sharp as the \(M,T\) route: it has a precise
finite same-law theorem, and that theorem is genuinely analytic.  More
finite labels do not prove cofinal Sobolev regularity, multiplier tameness,
normalizer lower bounds, commutator decay, score regularity, or a high-mode
floor.  A positive continuation must pick one of those analytic theorems and
prove it from actual Yang-Mills finite-DLR structure, or move to a different
primitive input such as nonlinear source-Dobrushin or connected cumulant
decay.

## 82. Local Source-Dobrushin As The Next Primitive Input

We now test nonlinear source-Dobrushin, but only in the local sense relevant
to the already live observables.  We do not assert global mixing of the full
Yang-Mills measure.  The target is a finite influence matrix for the source
observables that have survived the reductions:

$$
{\mathcal O}_{live}^{N,j}
=
\{M,T,\lambda_+,\lambda_-\}
\cup
{\mathcal P}_{HB}^{N,j,L}
\cup
{\mathcal F}_{PW}^{N,j,L}.
$$

Here \({\mathcal P}_{HB}^{N,j,L}\) denotes the finite polar family from
Sections 39 through 53, and \({\mathcal F}_{PW}^{N,j,L}\) denotes the finite
Peter-Weyl probes retained in Sections 68 through 81.

### Definition 82.1: Boundary Source Family

Let \({\mathcal B}_{bd}^{N,j}\) be the finite family of deterministic
boundary probes allowed by the active adaptive law: retained endpoint
record perturbations, boundary plaquette source probes, and selector-admissible
boundary scalar probes.  Each \(G_y\in{\mathcal B}_{bd}^{N,j}\) is normalized
by

$$
\|G_y\|_{bd}\le1.
$$

For \(O_i\in{\mathcal O}_{live}^{N,j}\) and \(G_y\in{\mathcal B}_{bd}^{N,j}\),
define the same-law mixed source pressure

$$
\Psi_{i,y}^{N,j}(s,t)
:=
\log
\mathbf E_{\mu_{N,j}^{ad}}
\exp\{sO_i+tG_y\}.
$$

The infinitesimal source influence is

$$
I_{i,y}^{lin}
:=
\sup_{\|G_y\|_{bd}\le1}
\left|
\partial_s\partial_t\Psi_{i,y}^{N,j}(0,0)
\right|.
$$

By Paper 31, this is the covariance
\(\sup|\operatorname{Cov}_{\mu_{N,j}^{ad}}(O_i,G_y)|\).

### Definition 82.2: Local Source-Dobrushin Row

For row weights \(w_{i,y}(a)\ge0\), define

$$
D_{loc}^{N,j}(a)
:=
\sup_i
\sum_y
w_{i,y}(a)\,
\Gamma_{i,y}^{N,j},
$$

where \(\Gamma_{i,y}^{N,j}\) is the nonlinear boundary-segment influence

$$
\Gamma_{i,y}^{N,j}
:=
\sup_{\eta_y(r)}
\int_0^1
\left|
{d\over dr}
\mathbf E_{\mu_{N,j}^{ad}(\cdot\mid \eta_y(r))}
O_i
\right|\,dr.
$$

The supremum is over admissible finite boundary paths changing only the
\(y\)-boundary record.  The local source-Dobrushin theorem is

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LOCAL}(q,a):
\qquad
\limsup_{(N,j)}D_{loc}^{N,j}(a)\le q<1.
$$

This is intentionally local: it controls only the live source-observable
family, not every observable of the full gauge measure.

## 83. Conditional Theorem From Local Dobrushin

The local source-Dobrushin theorem is useful because it turns finite boundary
responses into a convergent Neumann expansion for the live source family.

### Lemma 83.1: Boundary Variation Formula

Along any smooth finite boundary path \(\eta_y(r)\),

$$
{d\over dr}
\mathbf E_{\mu(\cdot\mid\eta_y(r))}O_i
=
\operatorname{Cov}_{\mu(\cdot\mid\eta_y(r))}
\left(
O_i,\dot H_y(r)
\right),
$$

where \(\dot H_y(r)\) is the derivative of the conditional log-density with
respect to the boundary path.

Proof.

Differentiate the finite conditional expectation.  The derivative of the
normalizer subtracts the mean score, leaving covariance with the log-density
derivative.  This is the same finite score identity used in Paper 30 and
the mixed source dictionary of Paper 31.  `square`

### Theorem 83.2: Local Source-Dobrushin Bounds Live Responses

If

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LOCAL}(q,a)
$$

holds with \(q<1\), then the cumulative boundary response of every live
observable is bounded by

$$
\sum_{n\ge0}q^n={1\over1-q}
$$

times the corresponding local source magnitude.  In particular, local
source perturbations cannot produce unbounded amplification of
\(M,T\), the polar probes, or the retained Peter-Weyl probes.

Proof.

The row bound says that one boundary-to-live response step has weighted norm
at most \(q\).  Iterating the finite influence matrix gives the Neumann
series

$$
I+\Gamma+\Gamma^2+\cdots,
$$

which converges in row norm when \(q<1\).  This is the finite local version
of the Dobrushin comparison argument and uses only the declared live
observable family.  `square`

### Corollary 83.3: Conditional Positive Use

If the local source magnitudes of the \(M,T\) and polar/Peter-Weyl probes are
below their respective budgets after multiplication by \(1/(1-q)\), then the
corresponding Paper-32 route closes.  Thus local Dobrushin can support:

1. \(M,T\) smallness;
2. polar response smallness;
3. bounded source curvature for the polar family;
4. controlled retained Peter-Weyl source responses.

It still requires the strict row \(q<1\).

## 84. Infinitesimal Source-Dobrushin And The Curvature Upgrade

Paper 31 already identifies the infinitesimal row.  The issue is the
nonlinear upgrade from the origin to a full boundary segment.

### Definition 84.1: Infinitesimal Local Row

Define

$$
D_{lin}^{N,j}(a)
:=
\sup_i
\sum_y
w_{i,y}(a)I_{i,y}^{lin}.
$$

The infinitesimal theorem is

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LIN}(q,a):
\qquad
\limsup_{(N,j)}D_{lin}^{N,j}(a)\le q<1.
$$

### Definition 84.2: Boundary Curvature Upgrade

For \(K\ge0\), write

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}CURV}(K,a)
$$

if, along every admissible boundary segment,

$$
\left|
{d\over dr}
\operatorname{Cov}_{\mu(\cdot\mid\eta_y(r))}
(O_i,\dot H_y(r))
\right|
\le K
$$

in the weighted row norm.

### Lemma 84.3: Linear Row Plus Curvature Gives Local Dobrushin

If

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LIN}(q_0,a)
$$

and

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}CURV}(K,a)
$$

hold, then

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LOCAL}(q_0+K/2,a)
$$

holds after the standard unit-speed normalization of boundary paths.

Proof.

Integrate the derivative of the covariance along the boundary segment.
The endpoint average of a function whose initial value is bounded by \(q_0\)
and whose slope is bounded by \(K\) is bounded by \(q_0+K/2\) on a unit
segment.  Apply this in the weighted row norm.  `square`

### Proposition 84.4: The Curvature Upgrade Is Not Sourced

The current corpus does not prove the curvature upgrade in a closing range.

Proof.

Papers 31 and 32 define source pressures and mixed derivatives, but do not
bound the third-order source derivatives or boundary-segment covariance
variation needed in Definition 84.2.  Fixed finite differentiability at a row
is not a cofinal \(K\)-bound, and the available oscillation estimates are too
coarse for the strict \(q<1\) margin.  `square`

## 85. Finite-DLR Envelope Route

The local row can also be upper-bounded by a finite DLR log-ratio envelope.
This gives a concrete but usually coarse sufficient condition.

### Definition 85.1: Local DLR Log-Ratio Envelope

For a live observable \(O_i\) and boundary site \(y\), define

$$
\Delta_{i,y}^{DLR,N,j}
:=
\sup_{\eta_y,\eta'_y}
\operatorname{osc}_{O_i}
\log
{d\mu_{N,j}^{ad}(\cdot\mid\eta_y)
\over
d\mu_{N,j}^{ad}(\cdot\mid\eta'_y)}.
$$

Here \(\operatorname{osc}_{O_i}\) means the oscillation relevant to the
observable scale used in the live route.

### Lemma 85.2: DLR Envelope Bounds Local Influence

For normalized \(\operatorname{osc}(O_i)\le1\),

$$
\Gamma_{i,y}^{N,j}
\le
e^{\Delta_{i,y}^{DLR,N,j}}-1.
$$

Consequently a sufficient condition for
\(\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LOCAL}(q,a)\) is

$$
\sup_i
\sum_y
w_{i,y}(a)
\left(e^{\Delta_{i,y}^{DLR,N,j}}-1\right)
\le q<1
$$

cofinally.

Proof.

The total variation distance between two conditional measures is bounded by
the \(L^1\) distance of the RN derivative from one, and a log-ratio
oscillation \(\Delta\) gives the coarse bound \(e^\Delta-1\).  Multiplying
by the normalized observable oscillation gives the displayed influence
bound.  `square`

### Proposition 85.3: The DLR Envelope Is Not Closing In The Current Corpus

The current corpus does not prove the DLR-envelope row below one.

Proof.

Paper 30's finite-DLR localization makes \(\Delta_{i,y}^{DLR,N,j}\)
well-defined.  It does not prove a cofinal weighted row bound below one for
the live observables.  The coarse exponential envelope also sees rare
boundary log-ratio spikes and can be much larger than the actual signed or
averaged source response.  Therefore this route is valid but unsourced in a
closing range.  `square`

## 86. Floor Alternative For Local Source-Dobrushin

Failure of local Dobrushin is not itself a floor.  It becomes useful only if
the large response is sign-coherent in the retained ledger.

### Definition 86.1: Local Dobrushin Floor

For \(M_*>0\), write

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}FLOOR}(M_*)
$$

if there exist \(O_i\), a boundary path \(\eta_y(r)\), and a retained sign
orientation such that

$$
\int_0^1
{d\over dr}
\mathbf E_{\mu(\cdot\mid\eta_y(r))}O_i
\,dr
\ge M_*
$$

after quotient, endpoint, normalization, and branch-ledger signs are applied.

### Proposition 86.2: Current-Corpus Floor Verdict

The current corpus does not prove
\(\mathrm{P32\text{-}SRC\text{-}DOB\text{-}FLOOR}(M_*)\).

Proof.

The corpus does not print a specific live observable, boundary path, and
retained sign orientation producing a lower bound.  A failed strict
Dobrushin sufficient condition may reflect coarse envelopes, cancellation,
or an overlarge path family rather than a sign-coherent predebit floor.
`square`

## 87. Verdict On Local Source-Dobrushin

### Theorem 87.1: Local Source-Dobrushin Route Is Fully Classified

The local source-Dobrushin route has the following status.

1. `P32-SRC-DOB-LOCAL(q,a)` with \(q<1\) would bound cumulative live-source
   responses by \(1/(1-q)\).
2. The infinitesimal row `P32-SRC-DOB-LIN` is only a first-response theorem;
   it needs `P32-SRC-DOB-CURV` to control finite boundary segments.
3. A finite-DLR log-ratio envelope is a valid sufficient condition, but the
   current corpus does not prove its weighted row below one.
4. Failure of local Dobrushin is not a floor unless
   `P32-SRC-DOB-FLOOR` is printed.

Thus the local source-Dobrushin route is reduced to

$$
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}LOCAL}
\quad\hbox{or}\quad
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}CURV}
\quad\hbox{or}\quad
\mathrm{P32\text{-}SRC\text{-}DOB\text{-}FLOOR}.
$$

None of these is sourced by the current corpus.

Proof.

Items 1 through 4 are Theorem 83.2, Lemma 84.3, Proposition 84.4,
Lemma 85.2, Proposition 85.3, and Proposition 86.2.  `square`

### Corollary 87.2: Strategic Consequence

Paper 32 has now investigated three primitive same-law analytic inputs:

1. minimal heat-bad scalar values \(M,T\);
2. same-law Peter-Weyl regularity/tail;
3. local source-Dobrushin.

All three are precise.  None is closed by the current corpus.  The remaining
untried primitive inputs from the Paper-31 menu are connected source-cumulant
decay and mixed RN-MIXAMP Ward/curvature control.

## 88. Mixed RN-MIXAMP Ward/Curvature As The Next Primitive Input

We now attack mixed RN-MIXAMP Ward/curvature control, but still inside Paper
32.  This route is narrower than a full Dobrushin theorem.  It asks whether
the particular doubly centered mixed amplitude that appears in the
Paper-27 row can be controlled by a finite same-law Ward identity and a
curvature estimate.

The Barandes rule remains unchanged.  Sources are deterministic generating
parameters.  Ward vector fields are finite changes of variables in the
actual finite adaptive integral.  No comparison measure, hidden Markov
process, or replacement heat-kernel law is introduced.

### Import 88.1: Frozen RN-MIXAMP Row

Paper 27 freezes the weighted mixed row

$$
{\mathfrak D}_{mix}^{N,j}(a)
:=
\sup_x
\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
q_{RN}^{N,j}(x,y).
$$

The direct RN-MIXAMP source is

$$
\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SMALL}(a,q):
\qquad
{\mathfrak D}_{mix}^{N,j}(a)\le q<1
$$

cofinally.  Paper 27 proves that this closes adaptive Branch A through the
direct Dobrushin gate.

### Definition 88.2: Mixed Source Pressure With Residual Tilt

For each live ordered pair \((x,y)\), let \(A_x\) and \(B_y\) be the two
endpoint probes used by the RN-MIXAMP row, and let \(R_{xy}\) be the
doubly centered residual mixed observable after the endpoint-additive
cancellations of Papers 26 through 31.  Define

$$
\Psi_{xy}^{N,j}(s,t,z)
:=
\log
\mathbf E_{\mu_{N,j}^{ad}}
\exp\{sA_x+tB_y+zR_{xy}\}.
$$

The actual mixed response at residual tilt \(z\) is

$$
M_{xy}^{N,j}(z)
:=
\partial_s\partial_t
\Psi_{xy}^{N,j}(0,0,z).
$$

The RN-MIXAMP row is controlled if the normalized, endpoint-centered
version of \(M_{xy}^{N,j}(1)\) has weighted row norm below one.

### Lemma 88.3: Endpoint-Additive Terms Are Invisible

If

$$
R_{xy}=r_x(A_x)+r_y(B_y)+c+R_{xy}^{dc},
$$

where \(R_{xy}^{dc}\) is doubly centered, then the mixed source response sees
only \(R_{xy}^{dc}\).

Proof.

Differentiate once in \(s\) and once in \(t\).  The derivative in \(t\) kills
terms depending only on \(A_x\), while the derivative in \(s\) kills terms
depending only on \(B_y\).  Constants are killed by either derivative.  This
is the Paper-31 RN-MIXAMP cancellation written in source language.  `square`

## 89. Finite Ward Identity For The Actual Adaptive Law

We next write the exact finite Ward identity.  This identity is real, but it
does not by itself make the RN-MIXAMP row small.  The hard part is whether
the RN-MIXAMP mixed observable lies in the Ward-controlled span with a small
actual score defect.

### Definition 89.1: Actual Ward Score

At fixed \((N,j)\), write the finite actual adaptive density as

$$
d\mu_{N,j}^{ad}
=
Z^{-1}e^{-H_{act}^{N,j}}d\lambda,
$$

where \(d\lambda\) is the finite Haar/chart/reference volume used in the
regularized DLR integral.  For a smooth compactly supported or compact-group
vector field \(X\), define the actual Ward score

$$
S_X^{N,j}
:=
XH_{act}^{N,j}
-
\operatorname{div}_{\lambda}X.
$$

The actual Hamiltonian decomposes schematically as

$$
H_{act}^{N,j}
=
H_{HK}^{N,j}
+H_{res}^{N,j}
+H_{Jac}^{N,j}
+H_{sel}^{N,j}
+H_{end}^{N,j}
+H_{norm}^{N,j}.
$$

Thus \(S_X^{N,j}\) contains heat, residual, Jacobian, selector, endpoint, and
normalizer scores.  A gauge/Haar Ward identity controls only the pieces on
which \(X\) is an exact symmetry.

### Lemma 89.2: Same-Law Ward Integration By Parts

For every finite test \(F\),

$$
\mathbf E_{\mu_{N,j}^{ad}}[XF]
=
\mathbf E_{\mu_{N,j}^{ad}}[F S_X^{N,j}].
$$

Proof.

Use the finite divergence theorem with density
\(Z^{-1}e^{-H_{act}}d\lambda\):

$$
\int XF\,e^{-H_{act}}d\lambda
=
\int F(XH_{act}-\operatorname{div}_{\lambda}X)e^{-H_{act}}d\lambda.
$$

Divide by \(Z\).  This is an identity inside the actual law, not a
comparison-law assertion.  `square`

### Definition 89.3: RN-MIXAMP Ward Span

For \(\epsilon_{span}\ge0\), write

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD\text{-}SPAN}
(\epsilon_{span})
$$

if every normalized RN-MIXAMP mixed test \(W_{xy}^{RN}\) can be written,
after licensed endpoint-additive and retained-row terms are removed, as

$$
W_{xy}^{RN}
=
\sum_{\ell=1}^{m_{xy}}
c_{\ell,xy}X_{\ell,xy}F_{\ell,xy}
+E_{xy}^{span},
$$

with weighted row error

$$
\sup_x
\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
|E_{xy}^{span}|
\le
\epsilon_{span}.
$$

The vector fields \(X_{\ell,xy}\), tests \(F_{\ell,xy}\), and coefficients
\(c_{\ell,xy}\) must be finite, deterministic, selector-admissible, and
already licensed by the actual adaptive finite chart.

### Definition 89.4: RN-MIXAMP Ward Defect

For \(\epsilon_{Ward}\ge0\), write

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARDDEF}(\epsilon_{Ward})
$$

if the Ward-score side obeys

$$
\sup_x
\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
\left|
\sum_{\ell}
c_{\ell,xy}
\mathbf E_{\mu_{N,j}^{ad}}
[F_{\ell,xy}S_{X_{\ell,xy}}^{N,j}]
\right|
\le
\epsilon_{Ward}
$$

cofinally.

### Theorem 89.5: Ward Span Plus Ward Defect Gives RN-MIXAMP Smallness

If

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD\text{-}SPAN}
(\epsilon_{span})
$$

and

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARDDEF}(\epsilon_{Ward})
$$

hold with

$$
\epsilon_{span}+\epsilon_{Ward}<1
$$

after the Paper-27 normalization, then
\(\mathrm{P27\text{-}RN\text{-}MIXAMP\text{-}SMALL}(a,q)\) holds for
some \(q<1\).

Proof.

Apply Lemma 89.2 to each \(X_{\ell,xy}F_{\ell,xy}\).  The licensed
endpoint-additive and retained-row terms are already charged outside the
RN-MIXAMP row.  The remaining weighted row is bounded by the span error plus
the Ward-score side.  If the sum is below one, the Paper-27 row is strict.
`square`

## 90. Residual-Tilt Curvature Route

The Ward identity may be easiest at residual tilt \(z=0\), where some clean
heat or Haar cancellations can be visible.  The actual RN-MIXAMP row lives at
\(z=1\).  The curvature route asks whether the mixed response can be
transported from \(z=0\) to \(z=1\) without exceeding the Paper-27 budget.

### Definition 90.1: Ward Base Bound

For \(\epsilon_0\ge0\), write

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD0}(\epsilon_0)
$$

if

$$
\sup_x
\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
|M_{xy}^{N,j}(0)|
\le
\epsilon_0
$$

cofinally, after endpoint-centering and normalization.

### Definition 90.2: Residual-Tilt Mixed Curvature

For \(\chi\ge0\), write

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}TILTCURV}(\chi)
$$

if

$$
\sup_x
\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
\int_0^1
\left|
{d\over dz}
M_{xy}^{N,j}(z)
\right|\,dz
\le
\chi
$$

cofinally.

### Lemma 90.3: Tilt Curvature Transfers Ward Smallness

If

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD0}(\epsilon_0)
$$

and

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}TILTCURV}(\chi)
$$

hold with

$$
\epsilon_0+\chi<1,
$$

then the Paper-27 RN-MIXAMP row is strict.

Proof.

For each \((x,y)\),

$$
M_{xy}^{N,j}(1)
=
M_{xy}^{N,j}(0)
+
\int_0^1 {d\over dz}M_{xy}^{N,j}(z)\,dz.
$$

Take the weighted row norm and apply the two assumed bounds.  `square`

### Lemma 90.4: The Curvature Is A Third Source Derivative

At finite \((N,j)\),

$$
{d\over dz}M_{xy}^{N,j}(z)
=
\partial_s\partial_t\partial_z
\Psi_{xy}^{N,j}(0,0,z).
$$

Thus the tilt curvature is a connected three-source cumulant under the
\(zR_{xy}\)-tilted finite probe.

Proof.

Differentiate the finite pressure.  The third derivative of a logarithmic
moment generating function is the connected third cumulant of the three
source observables.  `square`

## 91. Current-Corpus Audit Of The Mixed Ward Route

The exact Ward identity has been printed, but the positive theorem still
needs one of two nontrivial packages:

$$
\mathrm{WARD\text{-}SPAN}
+
\mathrm{WARDDEF}
\quad\hbox{or}\quad
\mathrm{WARD0}
+
\mathrm{TILTCURV}.
$$

We now audit whether the current corpus supplies either package.

### Proposition 91.1: Gauge/Haar Ward Identities Do Not Source Ward Span

The current gauge/Haar Ward identities do not prove
`P32-RNMIXAMP-WARD-SPAN`.

Proof.

Gauge/Haar Ward identities apply to exact infinitesimal changes of variables
in the finite group coordinates.  The RN-MIXAMP mixed test is a scalar
record object after adaptive selection, endpoint-centering, residual
normalization, and RPF quotienting.  The current papers do not print vector
fields \(X_{\ell,xy}\) and tests \(F_{\ell,xy}\) whose Ward derivatives span
that doubly centered scalar object with a closing weighted row error.

This is the same obstruction that appeared in the \(m,t\) scalar worksheet:
structural covariance does not determine scalar intertwiner coefficients.
Here, structural gauge covariance does not by itself make the mixed
RN-MIXAMP scalar a Ward derivative.  `square`

### Proposition 91.2: The Ward Defect Is Not Sourced

The current corpus does not prove
`P32-RNMIXAMP-WARDDEF(epsilon)` in a closing range.

Proof.

The Ward score \(S_X^{N,j}\) contains the residual Hamiltonian, Jacobian,
selector, endpoint, and normalizer score terms.  Papers 20 through 31
identify these terms and their bookkeeping roles, but they do not prove a
cofinal weighted row bound for the expectations
\(\mathbf E[F_{\ell,xy}S_{X_{\ell,xy}}]\) on the RN-MIXAMP live family.
Clean Haar invariance can cancel only the exact symmetry part.  It does not
bound the actual residual and selector score defect.  `square`

### Proposition 91.3: Tilt Curvature Is Not Sourced

The current corpus does not prove
`P32-RNMIXAMP-TILTCURV(chi)` in a closing range.

Proof.

Lemma 90.4 identifies tilt curvature with a connected third source
cumulant.  Papers 31 and 32 define such cumulants, and the Peter-Weyl and
local-Dobrushin passes give conditional routes to bound them.  They do not
print a cofinal weighted row estimate for the specific RN-MIXAMP tilted
third cumulant.  Universal oscillation bounds are too coarse for the strict
Paper-27 row margin.  `square`

## 92. Floor Alternative For Mixed RN-MIXAMP Ward/Curvature

If the mixed Ward route cannot make the row small, the useful negative
alternative is not "Ward failed."  The useful negative alternative is a
sign-coherent lower floor for the same mixed object.

### Definition 92.1: Mixed RN-MIXAMP Ward Floor

For \(M_*>0\), write

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD\text{-}FLOOR}(M_*)
$$

if there exist retained signs \(\sigma_{xy}\in\{-1,1\}\), compatible with the
Branch-A ledger, such that

$$
\liminf_{(N,j)}
\sup_x
\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
\sigma_{xy}M_{xy}^{N,j}(1)
\ge
M_*.
$$

The same definition may be expressed on the Ward-score side if
`WARD-SPAN` is exact, replacing \(M_{xy}^{N,j}(1)\) by the corresponding
\(\sum_\ell c_{\ell,xy}\mathbf E[F_{\ell,xy}S_{X_{\ell,xy}}]\).

### Proposition 92.2: Current-Corpus Floor Verdict

The current corpus does not prove
`P32-RNMIXAMP-WARD-FLOOR(M_*)`.

Proof.

No current paper prints a retained sign orientation and a cofinal lower
bound for the actual mixed RN-MIXAMP source response or for the corresponding
Ward-score defect.  A failed Ward smallness theorem may be caused by
uncontrolled signs, coarse envelopes, missing span data, or curvature rather
than by a sign-coherent retained lower bound.  `square`

## 93. Verdict On Mixed RN-MIXAMP Ward/Curvature

### Theorem 93.1: Mixed RN-MIXAMP Ward/Curvature Route Is Fully Classified

The mixed RN-MIXAMP Ward/curvature route has the following exact status.

1. `P32-RNMIXAMP-WARD-SPAN + P32-RNMIXAMP-WARDDEF` would source the
   Paper-27 strict RN-MIXAMP row if their combined budget is below one.
2. `P32-RNMIXAMP-WARD0 + P32-RNMIXAMP-TILTCURV` would source the same row by
   transporting a Ward base estimate from residual tilt \(z=0\) to \(z=1\).
3. The curvature term is a connected third source cumulant.
4. Gauge/Haar Ward identities alone do not prove the needed span, defect
   bound, or curvature bound.
5. The negative route is the sign-coherent floor
   `P32-RNMIXAMP-WARD-FLOOR`.

Thus the route is reduced to

$$
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD\text{-}SPAN}
+
\mathrm{P32\text{-}RNMIXAMP\text{-}WARDDEF}
\quad\hbox{or}\quad
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD0}
+
\mathrm{P32\text{-}RNMIXAMP\text{-}TILTCURV}
\quad\hbox{or}\quad
\mathrm{P32\text{-}RNMIXAMP\text{-}WARD\text{-}FLOOR}.
$$

None is sourced by the current corpus.

Proof.

Items 1 and 2 are Theorem 89.5 and Lemma 90.3.  Item 3 is Lemma 90.4.
Items 4 and 5 are Propositions 91.1 through 92.2.  `square`

### Corollary 93.2: Strategic Consequence

Paper 32 has now investigated four primitive same-law analytic inputs after
the source-response reframing:

1. minimal heat-bad scalar values \(M,T\);
2. same-law Peter-Weyl regularity/tail;
3. local source-Dobrushin;
4. mixed RN-MIXAMP Ward/curvature control.

All four are precise.  None is closed by the current corpus.  The only
untried primitive input from the Paper-31 menu is now connected
source-cumulant decay for the retained defect/Mobius activity family.

## 94. Connected Source-Cumulant Decay As The Final Primitive Input

We now attack the last untried primitive input from Paper 31: connected
source-cumulant decay.  This is the most global of the remaining Paper-31
inputs, so we keep it narrow.  The target is not "all cumulants of the
Yang-Mills law decay."  The target is only the retained defect/Mobius family
that appears in the Paper-23, Paper-29, and Paper-31 defect-polymer route.

### Definition 94.1: Retained Defect/Mobius Source Family

Let

$$
{\mathcal A}_{def}^{N,j}
=
\{A_\alpha^{N,j}\}_{\alpha\in V_{def}^{N,j}}
$$

be the finite retained defect/Mobius observable family after:

1. endpoint-additive rows are removed;
2. licensed retained rows are charged;
3. selector-admissible quotient labels are fixed;
4. the remaining support is measured in the RPF defect graph
   \(G_{def}^{N,j}\).

Each \(A_\alpha^{N,j}\) is a bounded same-law scalar observable on the actual
adaptive finite DLR space.

For a finite connected set
\(\Gamma\subset V_{def}^{N,j}\), define the connected source cumulant

$$
\kappa_\Gamma^{N,j}
:=
\left.
\prod_{\alpha\in\Gamma}\partial_{s_\alpha}
\log
\mathbf E_{\mu_{N,j}^{ad}}
\exp\left\{
\sum_{\beta\in\Gamma}s_\beta A_\beta^{N,j}
\right\}
\right|_{\mathbf s=0}.
$$

By Paper 31, this is the actual connected cumulant of the listed defect
observables.

### Definition 94.2: KP-Weighted Connected-Cumulant Norm

For \(a>0\), define

$$
{\mathfrak K}_{def}^{N,j}(a)
:=
\sup_{\alpha\in V_{def}^{N,j}}
\sum_{\Gamma\ni\alpha}
e^{a|\Gamma|}
\left|
\kappa_\Gamma^{N,j}
\right|,
$$

where the sum is over connected defect supports \(\Gamma\) in
\(G_{def}^{N,j}\).

The connected source-KP theorem is

$$
\mathrm{P32\text{-}CONN\text{-}SRC\text{-}KP}(q,a):
\qquad
\limsup_{(N,j)}
{\mathfrak K}_{def}^{N,j}(a)
\le q<1.
$$

The strict constant \(1\) is a normalized placeholder for the Paper-23/Paper-29
KP margin.  In applications, \(q<1\) means below the already frozen
Branch-A KP budget after all finite entropy and slack charges are paid.

## 95. Cumulant Decay Implies The Defect-Polymer Theorem

The value of connected cumulants is that they are already polymer activities.
No hidden process is being introduced; this is the finite moment-cumulant
identity read as a cluster expansion on the actual defect record family.

### Lemma 95.1: Defect Activities Are Connected Source Cumulants

For every connected defect support \(\Gamma\), the defect polymer activity
assigned by the Paper-31 source calculus is

$$
W_\Gamma^{N,j}
=
\kappa_\Gamma^{N,j}
$$

after the already licensed endpoint-additive and retained-row terms are
removed.

Proof.

This is the logarithmic moment-generating identity for connected cumulants.
The source family is finite at fixed \((N,j)\), so the finite
moment-cumulant expansion is exact.  The endpoint and retained rows have
already been subtracted before Definition 94.1.  `square`

### Theorem 95.2: Connected Source-KP Closes The Defect-Polymer Route

If

$$
\mathrm{P32\text{-}CONN\text{-}SRC\text{-}KP}(q,a)
$$

holds with \(q<1\) in the Paper-23/Paper-29 KP budget, then the retained
defect-polymer expansion is absolutely convergent and supplies the defect
polymer-value theorem needed by Paper 29.

Proof.

By Lemma 95.1 the polymer activities are the connected cumulants
\(\kappa_\Gamma^{N,j}\).  Definition 94.2 is exactly the KP weighted activity
norm on connected supports.  A strict subcritical bound gives the standard
finite KP cluster expansion with uniform absolute convergence.  Paper 29
then imports that defect-polymer theorem to source the primitive residual
defect values.  `square`

### Corollary 95.3: Export To Primitive Residual Values

`P32-CONN-SRC-KP(q,a)` implies the Paper-29 defect-polymer value source, and
therefore reopens the primitive residual value route after the retained row
class is fixed.

Proof.

This is Theorem 95.2 followed by the Paper-29 implication from the
defect-polymer theorem to primitive residual defect values.  `square`

## 96. Exports To The Other Paper-32 Obstructions

Connected source-cumulant decay also feeds the other Paper-32 routes, but
only through explicit finite projection constants.  We record the exact
conditional exports.

### Definition 96.1: Projection Constants From Defect Cumulants

Let \(C_{RN}^{N,j}\), \(C_{DOB}^{N,j}\), and \(C_{PW}^{N,j}\) be the smallest
finite constants such that the relevant RN-MIXAMP tilted third cumulants,
local source-Dobrushin curvature cumulants, and retained Peter-Weyl score
cumulants are bounded by the defect cumulant norm:

$$
\begin{aligned}
\|{\rm RN\ tilt\ cumulants}\|
&\le C_{RN}^{N,j}{\mathfrak K}_{def}^{N,j}(a),\\
\|{\rm DOB\ curvature\ cumulants}\|
&\le C_{DOB}^{N,j}{\mathfrak K}_{def}^{N,j}(a),\\
\|{\rm PW\ score\ cumulants}\|
&\le C_{PW}^{N,j}{\mathfrak K}_{def}^{N,j}(a).
\end{aligned}
$$

These constants are not assumed to be small.  They must be printed or
bounded by a finite same-law projection theorem.

### Proposition 96.2: RN-MIXAMP Tilt Curvature Export

If `P32-CONN-SRC-KP(q,a)` holds and

$$
\limsup_{(N,j)} C_{RN}^{N,j}q
\le
\chi
$$

with \(\epsilon_0+\chi<1\), then the
`P32-RNMIXAMP-WARD0 + P32-RNMIXAMP-TILTCURV` route closes.

Proof.

Lemma 90.4 identifies tilt curvature as a connected third source cumulant.
The projection constant \(C_{RN}^{N,j}\) converts the defect cumulant norm
into the RN-MIXAMP tilted third-cumulant norm.  The rest is Lemma 90.3.
`square`

### Proposition 96.3: Local Source-Dobrushin Curvature Export

If `P32-CONN-SRC-KP(q,a)` holds and

$$
\limsup_{(N,j)} C_{DOB}^{N,j}q
\le
K,
$$

then the connected-cumulant theorem supplies the curvature half of
`P32-SRC-DOB-CURV(K,a)`.

Proof.

The derivative of a boundary/interior covariance along a finite boundary
segment is a connected third cumulant involving the live observable, the
boundary score, and the segment score.  The projection constant \(C_{DOB}\)
is precisely the finite comparison from that family to the retained defect
cumulant norm.  `square`

### Proposition 96.4: Peter-Weyl Score-Cumulant Export

If `P32-CONN-SRC-KP(q,a)` holds and \(C_{PW}^{N,j}q\) is summable in the
retained Peter-Weyl tail weights, then the connected-cumulant theorem supplies
the residual-score cumulant part of `P32-SLAW-SCORE-SOB`.

Proof.

The residual-score Sobolev gate needs one higher source derivative on the
actual residual logarithmic factors.  Those higher derivatives are connected
cumulants.  The finite constant \(C_{PW}\) records whether the retained
defect family dominates the relevant Peter-Weyl score probes.  `square`

## 97. Current-Corpus Audit Of Connected Source-KP

The connected-cumulant route is now exact.  We audit whether it is sourced by
the current corpus.

### Proposition 97.1: Moment-Cumulant Identities Do Not Give Decay

The finite moment-cumulant identity does not prove
`P32-CONN-SRC-KP(q,a)`.

Proof.

The identity in Lemma 95.1 expresses activities as cumulants.  It does not
bound those cumulants.  In Paper 23 this distinction was already decisive:
finite Bell-number ceilings and moment-cumulant expansions give existence,
not exponential connected decay or KP smallness.  `square`

### Proposition 97.2: Clean KP Does Not Transfer Automatically

The clean heat-kernel KP estimates do not imply
`P32-CONN-SRC-KP(q,a)` for the actual adaptive defect family.

Proof.

The retained defect/Mobius family is defined after the actual adaptive
`SEL2` pushforward, selector, residual, Jacobian, endpoint, and normalizer
operations.  Clean heat-kernel KP activity controls a reference or licensed
clean ledger only when a transfer theorem identifies the actual defect
activities with that clean ledger.  Papers 23 and 29 explicitly record this
as a missing transfer package, not as an available theorem.  `square`

### Proposition 97.3: Defect Dobrushin Would Source It But Is Not Printed

The Paper-29 defect Dobrushin theorem would imply connected source-KP, but
the current corpus does not print the required defect conditional influence
matrix.

Proof.

Paper 29 proves that a strict defect Dobrushin row gives exponential decay
of connected defect cumulants and an absolutely convergent defect polymer
expansion.  The same paper proves that the actual defect conditional
influence matrix is not populated by the current corpus.  Therefore this is
a valid route, but not a sourced estimate.  `square`

### Proposition 97.4: Projection Exports Are Also Unsourced

The current corpus does not prove closing bounds for
\(C_{RN}^{N,j}\), \(C_{DOB}^{N,j}\), or \(C_{PW}^{N,j}\).

Proof.

Sections 90, 84, and 81 identify the target cumulant families, but no current
paper prints finite domination constants from those families to the retained
defect/Mobius cumulant norm.  Without those constants, connected source-KP
does not automatically export to RN-MIXAMP tilt curvature, local
source-Dobrushin curvature, or Peter-Weyl score regularity.  `square`

## 98. Floor Alternative For Connected Source-KP

Failure of cumulant decay is useful only if it produces a retained,
sign-coherent lower floor.

### Definition 98.1: Connected Cumulant Floor

For \(M_*>0\), write

$$
\mathrm{P32\text{-}CONN\text{-}SRC\text{-}FLOOR}(M_*)
$$

if there exists a cofinal family of connected defect supports
\({\mathcal G}^{N,j}\) and retained signs
\(\sigma_\Gamma\in\{-1,1\}\) such that

$$
\liminf_{(N,j)}
\sum_{\Gamma\in{\mathcal G}^{N,j}}
e^{a|\Gamma|}
\sigma_\Gamma
\kappa_\Gamma^{N,j}
\ge
M_*,
$$

after all endpoint, retained-row, quotient, and Branch-A ledger signs are
applied.

### Proposition 98.2: Current-Corpus Floor Verdict

The current corpus does not prove
`P32-CONN-SRC-FLOOR(M_*)`.

Proof.

No paper prints a cofinal sign orientation and lower bound for retained
defect connected cumulants.  A failure to prove a KP upper bound could come
from missing estimates, coarse supports, nonoptimal projection constants, or
cancellation, not necessarily from a sign-coherent retained lower floor.
`square`

## 99. Final Verdict On Connected Source-Cumulant Decay

### Theorem 99.1: Connected Source-Cumulant Route Is Fully Classified

The connected source-cumulant route has the following exact status.

1. `P32-CONN-SRC-KP(q,a)` would source the defect-polymer route and reopen
   primitive residual value extraction.
2. With additional finite projection constants, it can also source
   RN-MIXAMP tilt curvature, local source-Dobrushin curvature, and
   Peter-Weyl residual-score cumulants.
3. Moment-cumulant identities give exact activities but not decay.
4. Clean KP does not transfer to the actual adaptive defect family without a
   new transfer theorem.
5. Defect Dobrushin would source the cumulant theorem, but the needed defect
   influence matrix is not printed.
6. The negative route is the sign-coherent connected cumulant floor
   `P32-CONN-SRC-FLOOR`.

Thus the connected source-cumulant route is reduced to

$$
\mathrm{P32\text{-}CONN\text{-}SRC\text{-}KP}
\quad\hbox{or}\quad
\mathrm{P32\text{-}CONN\text{-}SRC\text{-}PROJ}
\quad\hbox{or}\quad
\mathrm{P32\text{-}CONN\text{-}SRC\text{-}FLOOR}.
$$

Here `P32-CONN-SRC-PROJ` abbreviates the required finite projection constants
\(C_{RN},C_{DOB},C_{PW}\) when the cumulant theorem is exported to another
route.  None of these is sourced by the current corpus.

Proof.

Items 1 and 2 are Theorem 95.2 and Propositions 96.2 through 96.4.  Items 3
through 5 are Propositions 97.1 through 97.4.  Item 6 is Proposition 98.2.
`square`

### Corollary 99.2: Paper-31 Primitive Menu Exhausted Inside Paper 32

Paper 32 has now investigated the Paper-31 primitive same-law analytic menu:

1. heat-bad source neutrality/curvature, reduced to \(M,T\) and floor;
2. same-law Peter-Weyl regularity/tail;
3. local source-Dobrushin;
4. mixed RN-MIXAMP Ward/curvature;
5. connected source-cumulant decay.

Each route now has a precise positive theorem, a precise current-corpus
non-sourcing verdict, and a precise floor alternative.  The attack surface
has been reduced, but not closed: the next actual proof must supply one new
same-law quantitative theorem from this finite menu.  More finite labels,
source rewrites, or structural covariance alone will not move adaptive
Branch A.

## 100. Post-Menu Attack Plan: Ward/Stein Range Or Dual Floor

The Paper-31 menu is now exhausted as a list of reductions.  The next useful
move should not be another source dictionary.  The right change of viewpoint
is:

$$
\hbox{do not compute the missing values directly;}
\qquad
\hbox{ask whether the live obstruction is a finite Ward/Stein derivative.}
$$

If it is, then the actual value is controlled by a Ward score defect.  If it
is not, then a finite dual functional separates the obstruction from the
Ward/Stein range, and that dual functional is the natural floor candidate.

This is the narrowest positive strategy left inside Paper 32 because it
targets the live scalar objects directly:

1. the minimal heat-bad scalar pair \(M,T\);
2. the eigenchannel floor candidates \(\lambda_+,\lambda_-\);
3. the mixed RN-MIXAMP row observables \(W_{xy}^{RN}\);
4. the retained defect/Mobius cumulant probes needed by source-KP.

### Plan 100.1: Five Concrete Attacks

The five attacks to run, in this order, are:

1. **Joint Ward/Stein range test.**  Build the finite actual-law Ward/Stein
   range generated by admissible vector fields \(X\) and finite tests \(F\).
   Test whether \(M,T\) and the mixed RN-MIXAMP probes lie in that range
   modulo licensed endpoint/retained rows.
2. **Residual score defect bound.**  If the range test passes, bound the
   actual Ward score pairings
   \(\mathbf E[F S_X]\) in the same weighted row norm.
3. **Residual-tilt curvature bound.**  If exact range at \(z=1\) is too hard,
   prove a clean-base identity at \(z=0\) and control the connected third
   cumulant that transports \(z=0\) to \(z=1\).
4. **Projection/tail split.**  If finite Ward/Stein range closes only at a
   cutoff \(L\), combine a finite range certificate with one of the
   same-law Peter-Weyl tail packages from Sections 68 through 81.
5. **Dual floor search.**  If the Ward/Stein range misses the live
   obstruction, print the separating dual and test whether its sign is
   retained in the Branch-A ledger.

All five attacks are same-law.  They use deterministic finite sources,
finite changes of variables, and derivatives at source strength zero under
\(\mu_{N,j}^{ad}\).  No hidden Markov dynamics or substitute heat-kernel law
is being introduced.

## 101. Finite Joint Ward/Stein Module

We now begin executing Attack 1.  At fixed \((N,j,L)\), define the live
finite vector space

$$
{\mathcal V}_{live}^{N,j,L}
:=
\operatorname{span}
\left(
M,T,\lambda_+,\lambda_-,
\{W_{xy}^{RN}\}_{(x,y)\in E_{RN}^{N,j,L}},
{\mathcal P}_{HB}^{N,j,L},
{\mathcal F}_{PW}^{N,j,L}
\right)
/
{\mathcal L}_{lic}^{N,j,L},
$$

where \({\mathcal L}_{lic}^{N,j,L}\) is the licensed subspace of
endpoint-additive, retained-row, selector-relabeling, and already charged
finite-table directions.

### Definition 101.1: Actual Ward/Stein Module

Let \({\mathcal X}_{adm}^{N,j,L}\) be the finite family of admissible vector
fields in the actual adaptive chart: compact-group/Haar fields,
selector-admissible chart fields, and residual-coordinate fields whose
finite divergence and score are defined in the actual DLR integral.

Let \({\mathcal F}_{adm}^{N,j,L}\) be the finite family of admissible tests
needed to span the live observables at cutoff \(L\).  Define the finite
Ward/Stein module

$$
{\mathcal W}_{WS}^{N,j,L}
:=
\operatorname{span}
\left\{
[XF]:
X\in{\mathcal X}_{adm}^{N,j,L},
F\in{\mathcal F}_{adm}^{N,j,L}
\right\}
\subset
{\mathcal V}_{live}^{N,j,L}.
$$

Here \([XF]\) denotes the class modulo \({\mathcal L}_{lic}^{N,j,L}\).

### Definition 101.2: Joint Ward/Stein Range Distance

Let

$$
{\mathcal O}_{target}^{N,j,L}
:=
\operatorname{span}
\left(
M,T,\lambda_+,\lambda_-,
\{W_{xy}^{RN}\}_{(x,y)\in E_{RN}^{N,j,L}}
\right)
\subset
{\mathcal V}_{live}^{N,j,L}.
$$

For a norm \(\|\cdot\|_{A}\) equal to the active Branch-A weighted row plus
heat-bad scalar budget norm, define

$$
d_{WS}^{N,j,L}
:=
\sup_{\|O\|_{A,*}\le1,\ O\in{\mathcal O}_{target}^{N,j,L}}
\inf_{W\in{\mathcal W}_{WS}^{N,j,L}}
\|O-W\|_{A}.
$$

The positive finite range theorem is

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RANGE}(L,\epsilon):
\qquad
d_{WS}^{N,j,L}\le\epsilon
$$

cofinally, with \(\epsilon\) below the remaining scalar and RN-MIXAMP
budgets after Ward score defects and tails are paid.

### Lemma 101.3: The Range Test Is Finite Linear Algebra

At fixed \((N,j,L)\), `P32-JOINT-WS-RANGE` is decided by a finite linear
program or singular-value computation.

Proof.

All spaces in Definitions 101.1 and 101.2 are finite-dimensional after the
finite adaptive chart, selector labels, live RN edge list, and Peter-Weyl
cutoff \(L\) are fixed.  The distance from a finite target set to a finite
span in a declared norm is a finite convex optimization problem.  In a
Hilbert norm it is an orthogonal projection problem; in the active row norm
it is a linear program after the usual trace-dual polarization.  `square`

## 102. Conditional Closure From Joint Ward/Stein Range

The range test alone is not enough.  It converts the live obstruction into
Ward score pairings.  We still need those pairings to be small.

### Definition 102.1: Joint Ward Score Defect

For \(\delta\ge0\), write

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}DEFECT}(\delta)
$$

if every range certificate

$$
O
=
\sum_\ell c_\ell X_\ell F_\ell
+E
$$

with \(\|E\|_A\le\epsilon\) satisfies

$$
\left|
\sum_\ell c_\ell
\mathbf E_{\mu_{N,j}^{ad}}
[F_\ell S_{X_\ell}^{N,j}]
\right|
\le\delta
$$

in the active weighted Branch-A norm.

### Theorem 102.2: Joint Ward/Stein Range Plus Defect Closes The Live Row

If

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RANGE}(L,\epsilon)
$$

and

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}DEFECT}(\delta)
$$

hold with

$$
\epsilon+\delta+\operatorname{Tail}_{PW}(L)
<
B_A^{rem},
$$

then the combined minimal heat-bad scalar and mixed RN-MIXAMP Ward/Stein
route closes within Branch A.

Proof.

For each live target \(O\), choose a range certificate
\(O=\sum_\ell c_\ell X_\ell F_\ell+E\).  Same-law Ward integration by parts
gives

$$
\mathbf E[O]
=
\sum_\ell c_\ell
\mathbf E[F_\ell S_{X_\ell}]
+
\mathbf E[E].
$$

The first term is bounded by the Ward score defect, the second by the range
error, and the omitted modes by the already separated Peter-Weyl tail.  If
their sum is below the remaining Branch-A budget, the live scalar/RN-MIXAMP
obstruction is absorbed.  `square`

## 103. Dual Certificate When The Range Test Fails

If the range test fails, the failure itself is useful only if it supplies a
retained sign-coherent floor.  The finite quotient makes that precise.

### Definition 103.1: Joint Ward/Stein Dual

A joint Ward/Stein dual certificate is a finite linear functional
\(\Lambda\in({\mathcal V}_{live}^{N,j,L})^*\) such that

$$
\Lambda(W)=0
\quad\hbox{for all}\quad
W\in{\mathcal W}_{WS}^{N,j,L},
$$

and

$$
\Lambda(O_{target})\ge M
$$

for a retained target \(O_{target}\in{\mathcal O}_{target}^{N,j,L}\).

It is a floor certificate only if the sign of \(\Lambda(O_{target})\) is
retained by the Branch-A ledger after endpoint, quotient, and tail charges.

### Lemma 103.2: Separation Is Automatic At Fixed Row

If \(d_{WS}^{N,j,L}>M\), then there exists a dual functional \(\Lambda\) of
norm one that annihilates \({\mathcal W}_{WS}^{N,j,L}\) and sees the target
at least \(M\).

Proof.

This is finite-dimensional Hahn-Banach separation, or linear-program duality
in the active row norm.  The finite quotient by \({\mathcal L}_{lic}\) is
already included in \({\mathcal V}_{live}\).  `square`

### Proposition 103.3: Separation Is Not Yet A Floor

The current corpus does not prove that the separating functional from Lemma
103.2 is sign-coherent in the Branch-A ledger.

Proof.

Sections 66, 92, and 98 all reached the same point: a large unsigned or
quotient-separated obstruction is not automatically a retained floor.  The
dual must survive the licensed signs after endpoint and selector
normalization.  No current paper prints that sign-retention theorem for the
joint Ward/Stein dual.  `square`

## 104. First Execution: Structural Ward Module Is Too Small

We can already execute the first negative subtest.  Let
\({\mathcal W}_{gauge}^{N,j,L}\) be the submodule generated only by
compact-group Haar/gauge vector fields and tests whose scores are exact
gauge-divergence terms.

### Theorem 104.1: Gauge/Haar Ward Range Does Not Contain The Live Scalars

The classes of \(M,T,\lambda_+,\lambda_-\) do not lie in
\({\mathcal W}_{gauge}^{N,j,L}\) unless their scalar coefficients are already
zero in the finite quotient.

Proof.

The minimal heat-bad scalar observables are scalar intertwiner coefficients
of the \(U_N\)-even projection

$$
\Pi_+^{U_N}(D_{\Gamma_1}^{HK}B)
=
{M\over2}I_2+{T\over2}U_N.
$$

Gauge/Haar Ward derivatives generate non-scalar orbit directions or exact
divergences.  They annihilate invariant scalar classes rather than
determining their numerical coefficients.  This is the scalar-intertwiner
obstruction of Proposition 60.3 and Theorem 65.1, now stated as a range
claim: if a scalar class is in the pure gauge Ward range, then every
gauge-invariant dual functional annihilating gauge derivatives must also
annihilate it.  The dual functionals extracting \(M,T,\lambda_+,\lambda_-\)
do not vanish unless those coefficients are already zero.  `square`

### Corollary 104.2: The Positive Ward/Stein Move Must Use Residual Scores

The joint Ward/Stein breakthrough cannot come from pure gauge/Haar Ward
identities.  It must use at least one of:

1. residual-coordinate vector fields whose scores contain the actual RPF
   residual;
2. selector-source vector fields that change the numerical block product,
   not merely its label;
3. a finite Stein inverse for the live scalar/RN-MIXAMP observables with a
   controlled actual score defect;
4. a dual certificate that becomes a retained floor.

This is the first executed attack: the structural Ward submodule is
discarded.  The next executable target is the residual-score Ward/Stein
module

$$
{\mathcal W}_{res}^{N,j,L}
:=
\operatorname{span}\{[XF]: X\hbox{ differentiates actual residual/selector
coordinates}\}.
$$

The live theorem is now

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESRANGE}
\quad+\quad
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESDEFECT}
\quad\hbox{or}\quad
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}DUALFLOOR}.
$$

## 105. Immediate Next Worksheet

The next worksheet, if Paper 32 continues, should instantiate
\({\mathcal W}_{res}^{N,j,L}\) at the smallest live block:

1. basis \(I_2,U_N\) for the heat-bad scalar sector;
2. the minimal RN-MIXAMP edge family touching the same block;
3. residual/selector coordinate vector fields that actually change
   \(B_{\Gamma_1}^{N,j}\);
4. Ward scores \(S_X=XH_{act}-\operatorname{div}X\) split into heat,
   residual, Jacobian, selector, endpoint, and normalizer pieces;
5. a primal range certificate or a dual separating functional.

This is the concrete Feynman-style reframing: make the hidden value a
natural response of a finite operator.  If the finite operator range contains
the live obstruction and the score defect is small, we close positively.  If
the range misses and the dual sign is retained, we close negatively.  If
neither happens, the remaining gap is no longer conceptual; it is the
specific residual-score value theorem

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESDEFECT}
$$

on the actual adaptive law.

## 106. Residual/Selector Jacobian For The Smallest Live Block

We now instantiate the residual/selector range problem at the smallest live
block.  The target is the numerical block product

$$
B_{\Gamma_1}^{N,j}
=
R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j},
$$

seen through the four scalar functionals

$$
M,\qquad T,\qquad \lambda_+,\qquad \lambda_-.
$$

The residual/selector Ward module can move these scalars only if its vector
fields change the numerical product \(B_{\Gamma_1}^{N,j}\), not merely the
name of the selected row.

### Definition 106.1: Residual/Selector Coordinates

Let \(\theta=(\theta_1,\ldots,\theta_r)\) be a finite coordinate system for
the residual/selector degrees of freedom touching the block \(\Gamma_1\) at
cutoff \(L\).  These coordinates include only same-law finite variables:
residual atom coordinates, smooth selector weights or selector-admissible
chart coordinates, and local normalization coordinates already present in
the actual adaptive DLR integral.

Define the live scalar map

$$
\Phi_{\Gamma_1}^{N,j,L}(\theta)
:=
\left(
M(\theta),
T(\theta),
\lambda_+(\theta),
\lambda_-(\theta),
\{W_{xy}^{RN}(\theta)\}_{(x,y)\in E_{RN}(\Gamma_1,L)}
\right).
$$

Its residual/selector Jacobian is

$$
J_{res}^{N,j,L}
:=
D_\theta \Phi_{\Gamma_1}^{N,j,L}.
$$

### Definition 106.2: Residual Range Rank Gate

For \(\epsilon\ge0\), write

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESRANGE}(L,\epsilon)
$$

if the quotient range of \(J_{res}^{N,j,L}\), after licensed endpoint and
retained-row directions are removed, is \(\epsilon\)-dense in the active live
target norm.

Equivalently, every live target functional has a finite residual/selector
coordinate vector field \(X_v=v\cdot\nabla_\theta\) and test \(F_v\) whose
class \(X_vF_v\) approximates that target to error \(\epsilon\).

### Lemma 106.3: Residual Range Is A Finite Rank Test

At fixed \((N,j,L)\), `P32-JOINT-WS-RESRANGE` is exactly the finite rank or
least-singular-value test for \(J_{res}^{N,j,L}\) in the quotient norm.

Proof.

The finite residual/selector coordinates, live scalar map, licensed
subspace, and RN edge list are all finite at fixed \((N,j,L)\).  The image
of \(J_{res}^{N,j,L}\) is therefore a finite-dimensional subspace of the
live quotient.  Distance from the target unit ball to that image is the
least residual of a finite linear system, or its linear-program analogue in
the active row norm.  `square`

## 107. Selector-Only Directions Are Still Tautological

The first residual/selector subtest is selector-only.  This is the same trap
seen in the \(M,T\) centering attempt, now stated as a Jacobian result.

### Definition 107.1: Selector-Only Tangent Subspace

Let \(T_{sel}^{label}\subset T_\theta\) be the tangent subspace of
residual/selector directions that change only selector names, row labels, or
admissible bookkeeping labels while leaving the numerical block product
\(B_{\Gamma_1}^{N,j}\) and the normalized mixed RN-MIXAMP values unchanged.

### Proposition 107.2: Selector-Only Directions Have Zero Live Jacobian

For every \(v\in T_{sel}^{label}\),

$$
J_{res}^{N,j,L}v=0
$$

in the live quotient.

Proof.

By definition, \(v\) leaves the numerical values of
\(B_{\Gamma_1}^{N,j}\) unchanged.  The scalars \(M,T,\lambda_+,\lambda_-\)
are deterministic linear functionals of that numerical product and the
fixed structural constants \(a_N,b_N,h_0,h_A\).  Therefore their directional
derivatives along \(v\) vanish.  The same selector-only direction also
leaves the normalized mixed RN-MIXAMP values unchanged by assumption, so the
RN part of \(\Phi_{\Gamma_1}\) has zero derivative.  `square`

### Corollary 107.3: Positive Range Requires Numerical Residual Motion

`P32-JOINT-WS-RESRANGE` cannot be proved by selector relabeling.  It needs
residual or selector-coordinate directions that change the numerical
block product or the actual doubly centered RN-MIXAMP scalar values.

This removes another tempting but non-moving option from the attack surface.

## 108. Residual Score Defect For Moving Directions

Suppose the rank gate succeeds because residual coordinates genuinely move
the live target.  Ward integration by parts then transfers the target value
to actual score pairings.  These score pairings are the next quantitative
object.

### Definition 108.1: Residual/Selector Ward Score

For a residual/selector coordinate vector field \(X_v=v\cdot\nabla_\theta\),
define

$$
S_v^{N,j}
:=
X_vH_{act}^{N,j}
-
\operatorname{div}_{\lambda}X_v.
$$

Using the actual Hamiltonian split from Section 89,

$$
S_v^{N,j}
=
S_{v,HK}^{N,j}
+S_{v,res}^{N,j}
+S_{v,Jac}^{N,j}
+S_{v,sel}^{N,j}
+S_{v,end}^{N,j}
+S_{v,norm}^{N,j}.
$$

The heat, endpoint-additive, and already retained pieces may be charged only
when they are licensed by earlier papers.  The live new term is the combined
actual residual/selector score

$$
S_{v,new}^{N,j}
:=
S_{v,res}^{N,j}
+S_{v,Jac}^{N,j}
+S_{v,sel}^{N,j}
+S_{v,norm}^{N,j}
$$

after endpoint-additive cancellations and retained-row charges.

### Definition 108.2: Residual Score Defect Gate

For \(\delta\ge0\), write

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESDEFECT}(\delta)
$$

if every residual-range certificate

$$
O
=
\sum_\ell c_\ell X_{v_\ell}F_\ell+E
$$

with \(\|E\|_A\le\epsilon\) satisfies

$$
\left|
\sum_\ell c_\ell
\mathbf E_{\mu_{N,j}^{ad}}
[F_\ell S_{v_\ell,new}^{N,j}]
\right|
\le \delta
$$

in the active Branch-A norm.

### Theorem 108.3: Residual Range Plus Residual Defect Closes The Joint Route

If

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESRANGE}(L,\epsilon)
$$

and

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESDEFECT}(\delta)
$$

hold with

$$
\epsilon+\delta+\operatorname{Tail}_{PW}(L)
<
B_A^{rem},
$$

then the post-menu joint Ward/Stein route closes positively.

Proof.

This is Theorem 102.2 applied to the residual/selector submodule.  Licensed
heat, endpoint, and retained-row score pieces are already charged.  The only
unlicensed contribution is \(S_{v,new}\), bounded by the residual score
defect gate.  `square`

## 109. Current-Corpus Audit Of The Residual/Selector Route

The residual/selector range route has now separated its two required inputs:
rank and score.

### Proposition 109.1: The Residual Rank Gate Is Not Printed

The current corpus does not prove
`P32-JOINT-WS-RESRANGE(L,epsilon)` in a closing range.

Proof.

Papers 23, 26, 29, 30, and 32 define the formal residual atoms, selector
labels, block products, and live scalar projections.  They do not print the
finite Jacobian \(J_{res}^{N,j,L}\), its quotient rank, or a least-singular
value lower bound showing that residual/selector coordinate fields span the
live scalar and RN-MIXAMP target directions.  Selector-only directions were
just shown to have zero live Jacobian.  Therefore the rank gate remains a
new finite same-law row theorem.  `square`

### Proposition 109.2: The Residual Score Defect Is Not Printed

The current corpus does not prove
`P32-JOINT-WS-RESDEFECT(delta)` in a closing range.

Proof.

The score \(S_{v,new}\) contains precisely the actual residual, Jacobian,
selector, and normalizer derivatives that earlier audits isolated as missing:
primitive residual values in Paper 29, residual mixed tilt in Paper 30,
residual multiplier and score regularity in Sections 68 through 81, and
Ward-score defects in Sections 89 through 93.  None of those papers prints a
cofinal active-norm bound for
\(\mathbf E[F_\ell S_{v_\ell,new}]\) on the residual/selector vector fields
needed by the rank certificate.  `square`

### Proposition 109.3: Rank Failure Is Not Yet A Floor

If `P32-JOINT-WS-RESRANGE` fails, finite duality produces a separating
functional, but the current corpus does not prove
`P32-JOINT-WS-DUALFLOOR`.

Proof.

This is the same signed-ledger issue as Proposition 103.3.  A dual
functional separating the live target from the residual/selector Ward range
is a floor candidate only if its sign survives endpoint, selector, quotient,
retained-row, and tail ledgers.  That sign-retention theorem is not printed.
`square`

## 110. Verdict On The Residual/Selector Ward-Stein Execution

### Theorem 110.1: Residual/Selector Ward-Stein Route Is Fully Classified

The residual/selector Ward-Stein route has the following status.

1. Selector-only directions have zero live Jacobian and cannot move
   \(M,T,\lambda_\pm\) or the normalized RN-MIXAMP values.
2. The positive route requires the finite rank theorem
   `P32-JOINT-WS-RESRANGE`.
3. If the rank theorem holds, closure also requires the score theorem
   `P32-JOINT-WS-RESDEFECT`.
4. If the rank theorem fails, finite duality gives a separator, but a floor
   requires the sign-retention theorem `P32-JOINT-WS-DUALFLOOR`.
5. None of the three live gates is sourced by the current corpus.

Thus the post-menu Ward-Stein route is reduced to

$$
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESRANGE}
\quad+\quad
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}RESDEFECT}
\quad\hbox{or}\quad
\mathrm{P32\text{-}JOINT\text{-}WS\text{-}DUALFLOOR}.
$$

Proof.

Items 1 through 4 are Proposition 107.2, Theorem 108.3, Propositions 109.1
through 109.3, and finite duality from Lemma 103.2.  Item 5 is the
current-corpus audit in Section 109.  `square`

### Corollary 110.2: What Actually Remains

The creative reframing has worked in the following sense: the missing value
problem is no longer amorphous.  It is either:

1. a finite residual/selector Jacobian rank theorem;
2. a same-law residual score-defect bound;
3. or a sign-coherent dual floor.

It has not yet produced a closure theorem.  To move beyond Paper 32, one
must print actual finite data for \(J_{res}^{N,j,L}\), actual score-defect
estimates for the corresponding vector fields, or the dual floor sign.

## 111. Executing The Five-Step Residual-Range Worksheet

We now execute the five steps promised after Corollary 110.2, staying at the
smallest live block.  The goal is to see whether the obstruction is still
conceptual or has become a finite table.

The answer is mixed and useful:

1. the heat-bad scalar sector has a completely explicit block-entry
   Jacobian;
2. that scalar Jacobian has full rank onto the two-dimensional scalar target
   \((M,T)\);
3. the eigenchannel targets \(\lambda_\pm\) add no extra rank because they
   are linear combinations of \(M,T\);
4. the RN-MIXAMP edge part requires derivative data not printed by the
   current corpus;
5. even in the scalar sector, the score-defect bound is a genuine actual-law
   residual score theorem.

This is progress: the rank obstruction is no longer mysterious in the scalar
sector.  The remaining positive obstruction is score-defect control, plus
the unprinted RN-MIXAMP derivative rows.

## 112. Step 1: Instantiate The Smallest Worksheet

The smallest worksheet is the Paper-30/Paper-32 singlet-adjoint crossing
block.  Write

$$
B_{\Gamma_1}^{N,j}
=
\begin{pmatrix}
\beta_{00}&\beta_{0A}\\
\beta_{A0}&\beta_{AA}
\end{pmatrix}.
$$

The structural constants are

$$
a_N={1\over N},
\qquad
b_N={\sqrt{N^2-1}\over N},
\qquad
h_0=1,
$$

with \(h_A\) the adjoint heat weight already used in Sections 54 through 60.
The scalar targets are

$$
M=m,
\qquad
T=t,
\qquad
\lambda_+={m+t\over2},
\qquad
\lambda_-={m-t\over2}.
$$

The minimal RN-MIXAMP edge family touching the same block is denoted

$$
E_{RN}(\Gamma_1,L).
$$

For each \((x,y)\in E_{RN}(\Gamma_1,L)\), the corresponding normalized
doubly centered mixed row is \(W_{xy}^{RN}\).

## 113. Step 2: Print The Block-Entry Coordinates

For the scalar part of the residual/selector rank test, take formal
block-entry coordinates

$$
\theta_{blk}
:=
(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA}).
$$

These are not yet asserted to be admissible actual residual coordinates.
They are the envelope coordinates for the numerical block product.  Any
actual residual/selector coordinate system that changes the block product
maps into these coordinates by a finite Jacobian.

The scalar map is

$$
\Phi_{scal}(\theta_{blk})
:=
(m,t,\lambda_+,\lambda_-).
$$

By Corollary 59.2,

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

Thus the block-entry worksheet is fully explicit.

## 114. Step 3: Compute The Scalar Jacobian Columns

With columns ordered as
\((\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA})\), the scalar Jacobian is

$$
J_{scal}
=
\begin{pmatrix}
h_0&0&0&h_A\\
a_Nh_0&b_Nh_0&b_Nh_A&-a_Nh_A\\
{(1+a_N)h_0\over2}&{b_Nh_0\over2}&{b_Nh_A\over2}&{(1-a_N)h_A\over2}\\
{(1-a_N)h_0\over2}&-{b_Nh_0\over2}&-{b_Nh_A\over2}&{(1+a_N)h_A\over2}
\end{pmatrix}.
$$

The first row is \(dm\), the second is \(dt\), and the last two are
\(d\lambda_+\) and \(d\lambda_-\).

### Lemma 114.1: Scalar Jacobian Rank

For \(N>1\) and \(h_0h_A\ne0\),

$$
\operatorname{rank}J_{scal}=2.
$$

Moreover the image is exactly the two-dimensional scalar target
\(\operatorname{span}\{m,t\}\), and \(\lambda_\pm\) add no independent rank.

Proof.

The last two rows are

$$
d\lambda_+={1\over2}(dm+dt),
\qquad
d\lambda_-={1\over2}(dm-dt),
$$

so the rank is the rank of the first two rows.  The first two rows are
independent: the \(\beta_{0A}\) column of \(dm\) is zero, while the
\(\beta_{0A}\) column of \(dt\) is \(b_Nh_0\), which is nonzero for \(N>1\)
and \(h_0\ne0\).  Hence the rank is two.  `square`

### Corollary 114.2: Scalar Range Passes In The Block-Entry Envelope

If the actual residual/selector coordinates can realize arbitrary
block-entry variations modulo licensed rows, then the scalar part of
`P32-JOINT-WS-RESRANGE` passes at the minimal block.

Proof.

Lemma 114.1 says the formal block-entry image already covers the scalar
target \((m,t)\).  Since \(\lambda_\pm\) are linear combinations of \(m,t\),
the entire scalar target is covered.  `square`

This is an important simplification.  The scalar rank obstruction is gone in
the block-entry envelope.  What remains is admissibility of those directions
under the actual residual/selector chart and the score-defect bound.

## 115. Step 4: Decide The Full Joint Rank

The full joint target also includes RN-MIXAMP rows.  Define the missing
RN derivative matrix

$$
K_{RN}^{blk}
:=
\left(
{\partial W_{xy}^{RN}\over\partial\beta_{00}},
{\partial W_{xy}^{RN}\over\partial\beta_{0A}},
{\partial W_{xy}^{RN}\over\partial\beta_{A0}},
{\partial W_{xy}^{RN}\over\partial\beta_{AA}}
\right)_{(x,y)\in E_{RN}(\Gamma_1,L)}.
$$

The block-entry joint Jacobian is

$$
J_{joint}^{blk}
=
\begin{pmatrix}
J_{scal}\\
K_{RN}^{blk}
\end{pmatrix}.
$$

### Proposition 115.1: Current-Corpus Joint Rank Verdict

The scalar part of the rank test passes in the block-entry envelope, but the
full joint rank is not decided by the current corpus because
\(K_{RN}^{blk}\) is not printed.

Proof.

The scalar statement is Corollary 114.2.  For the full joint statement one
must know how the normalized doubly centered RN-MIXAMP rows change under the
same block-entry variations.  Papers 26 through 32 identify those rows and
their source meaning, but they do not print the derivative matrix
\(K_{RN}^{blk}\) for the minimal live edge family.  Therefore the finite rank
test has been reduced to a concrete missing table rather than solved.  `square`

### Definition 115.2: RN Block-Derivative Table

The exact finite table now needed is

$$
\mathrm{P32\text{-}RN\text{-}BLKDER}(L):
\qquad
K_{RN}^{blk}\hbox{ is printed with quotient-normalized error }o(1).
$$

If `P32-RN-BLKDER(L)` is printed, the full joint rank of
\(J_{joint}^{blk}\) is decidable by finite row reduction.

## 116. Step 5: Attack The Score Defect In The Scalar Sector

Because the scalar block-entry rank passes formally, we can write explicit
Ward-Stein certificates for \(m\) and \(t\) in block-entry coordinates.  Let
\(\beta\) denote the vector of four block entries and let \(\ell_m,\ell_t\)
be the coefficient vectors for \(m=\ell_m\cdot\beta\) and
\(t=\ell_t\cdot\beta\):

$$
\ell_m=(h_0,0,0,h_A),
$$

and

$$
\ell_t=(a_Nh_0,b_Nh_0,b_Nh_A,-a_Nh_A).
$$

For \(\ell\in\{\ell_m,\ell_t\}\), define the constant block-entry vector
field

$$
X_\ell:=\ell\cdot\nabla_\beta
$$

and the finite quadratic test

$$
F_\ell(\beta):=
{(\ell\cdot\beta)^2\over 2\|\ell\|_2^2}.
$$

Then

$$
X_\ell F_\ell=\ell\cdot\beta.
$$

Thus \(m\) and \(t\) are exact block-entry Ward derivatives.

### Lemma 116.1: Scalar Values Are Exact Score Pairings In The Envelope

If the block-entry vector fields \(X_{\ell_m}\) and \(X_{\ell_t}\) are
admissible actual residual/selector vector fields, then

$$
\mathbf E[m]
=
\mathbf E[F_{\ell_m}S_{\ell_m}],
\qquad
\mathbf E[t]
=
\mathbf E[F_{\ell_t}S_{\ell_t}],
$$

where

$$
S_\ell=X_\ell H_{act}-\operatorname{div}X_\ell.
$$

Proof.

The identity \(X_\ell F_\ell=\ell\cdot\beta\) gives \(m\) or \(t\).  Apply
the same-law Ward integration-by-parts identity of Lemma 89.2.  `square`

### Definition 116.2: Scalar Residual Score Defect

For \(\delta\ge0\), write

$$
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta)
$$

if the new residual/selector score parts satisfy

$$
\left|
\mathbf E[F_{\ell_m}S_{\ell_m,new}]
\right|
+
\left|
\mathbf E[F_{\ell_t}S_{\ell_t,new}]
\right|
\le\delta
$$

cofinally after all licensed heat, endpoint, retained-row, and tail charges.

### Proposition 116.3: Scalar Rank Reduces The Positive Route To Score Defect

In the block-entry envelope, the minimal heat-bad scalar route closes if
`P32-SCAL-RESDEFECT(delta)` holds with \(\delta\) below the remaining scalar
budget.

Proof.

Corollary 114.2 gives scalar range.  Lemma 116.1 writes the scalar values as
score pairings.  Licensed score pieces are already charged, so the new term
is exactly the residual/selector score defect in Definition 116.2.  `square`

### Proposition 116.4: The Score Defect Is Not Sourced By The Current Corpus

The current corpus does not prove `P32-SCAL-RESDEFECT(delta)` in a closing
range.

Proof.

The score \(S_{\ell,new}\) contains derivatives of the actual residual
Hamiltonian, Jacobian, selector weights, and normalizers along block-entry
directions.  Papers 29 and 30 identify these as the live residual value and
mixed-tilt obstructions; Sections 68 through 81 identify the corresponding
residual multiplier and score-regularity obstructions.  None prints the
expectations \(\mathbf E[F_{\ell_m}S_{\ell_m,new}]\) and
\(\mathbf E[F_{\ell_t}S_{\ell_t,new}]\) or a cofinal bound on them.  `square`

## 117. Five-Step Worksheet Verdict

### Theorem 117.1: Residual-Range Worksheet Is Completed At Current-Corpus Level

The five-step worksheet has the following status.

1. The smallest block and scalar/RN target family are instantiated.
2. The block-entry coordinates \(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA}\)
   are printed.
3. The scalar Jacobian columns are printed explicitly.
4. The scalar rank passes in the block-entry envelope; the full joint rank is
   undecided until `P32-RN-BLKDER(L)` is printed.
5. The scalar Ward-Stein range reduces positive closure to
   `P32-SCAL-RESDEFECT(delta)`, which is not sourced by the current corpus.

Thus the next concrete data theorem is exactly

$$
\mathrm{P32\text{-}RN\text{-}BLKDER}(L)
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta),
$$

or else a dual floor obtained from the finite rank failure once the RN block
derivative table is printed.

Proof.

Items 1 through 5 are Sections 112 through 116.  `square`

### Corollary 117.2: What The Five Steps Bought Us

The five-step push did reduce the attack surface again.  The minimal scalar
rank problem is solved; it is not the obstruction.  The obstruction is now
one of three concrete same-law data inputs:

1. admissibility of the block-entry vector fields as actual residual/selector
   directions;
2. the RN block-derivative table \(K_{RN}^{blk}\);
3. the scalar residual score-defect bound.

No further source-response reformulation is needed for this worksheet.

## 118. The Hidden Prerequisite Behind `P32-RN-BLKDER`

The previous worksheet deliberately used the four block entries

$$
\beta=(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA})
$$

as if they were coordinates.  That is legitimate for scalar algebra, but it
is not automatically legitimate for the actual RN-MIXAMP row.  The RN row is
not defined as a polynomial in \(\beta\).  It is a normalized, endpoint-
centered conditional response of the actual adaptive law.

Therefore the expression

$$
{\partial W_{xy}^{RN}\over\partial\beta_{ab}}
$$

is meaningful only after one of the following finite facts is proved:

1. the RN row factors through the block entries \(\beta\); or
2. a canonical actual residual/selector lift of block-entry variations is
   chosen, and its score cost is controlled.

This section attacks that hidden prerequisite.

### Definition 118.1: Block-Entry Map And RN Row Map

At fixed \((N,j,L)\), let \(\theta\in\Theta_{res}^{N,j,L}\) denote the actual
finite residual/selector coordinates touching \(\Gamma_1\).  Define

$$
B_{blk}(\theta)
:=
(\beta_{00}(\theta),\beta_{0A}(\theta),
\beta_{A0}(\theta),\beta_{AA}(\theta))
\in\mathbb R^4,
$$

and

$$
W_{RN}(\theta)
:=
\{W_{xy}^{RN}(\theta)\}_{(x,y)\in E_{RN}(\Gamma_1,L)}.
$$

The derivative data available at the actual coordinate level are

$$
D_\theta B_{blk},
\qquad
D_\theta W_{RN}.
$$

The block-entry derivative \(K_{RN}^{blk}\) exists canonically only if these
two derivatives are compatible.

## 119. Block-Entry Admissibility

### Definition 119.1: `P32-BLKFIELD-ADM`

Write

$$
\mathrm{P32\text{-}BLKFIELD\text{-}ADM}(L,\sigma,C_S)
$$

if, cofinally and at cutoff \(L\), the actual residual/selector chart admits
a finite linear lift

$$
R_{blk}^{N,j,L}:\mathbb R^4\to T_\theta\Theta_{res}^{N,j,L}
$$

such that

$$
D_\theta B_{blk}\,R_{blk}=I_4
$$

up to quotient error \(o(1)\), the least singular value of
\(D_\theta B_{blk}\) on the selected lift is at least \(\sigma>0\), and the
new residual/selector Ward scores of the lifted unit vectors obey the
cofinal envelope \(C_S\).

This is the precise version of saying that
\(\partial_{\beta_{00}},\partial_{\beta_{0A}},
\partial_{\beta_{A0}},\partial_{\beta_{AA}}\) are actual admissible vector
fields rather than formal coordinates.

### Lemma 119.2: Scalar Rank Needs `P32-BLKFIELD-ADM`

The scalar rank result of Lemma 114.1 becomes an actual Ward-Stein certificate
only after `P32-BLKFIELD-ADM` is supplied.

Proof.

Lemma 114.1 proves rank in the formal \(\beta\)-space.  A Ward-Stein
certificate in the actual law must be a vector field on the actual finite
integration variables \(\theta\).  Such a vector field exists for every
formal \(\beta\)-direction exactly when the lift \(R_{blk}\) exists with
controlled quotient error.  `square`

### Proposition 119.3: Current Corpus Does Not Prove `P32-BLKFIELD-ADM`

The present corpus does not prove `P32-BLKFIELD-ADM`.

Proof.

Sections 106 through 110 define the actual residual/selector coordinate map
and prove that selector-only directions have zero live Jacobian.  Sections
111 through 117 compute the formal block-entry scalar Jacobian.  No section
prints \(D_\theta B_{blk}\), proves that it has rank four on actual
residual/selector directions, or gives a controlled right inverse
\(R_{blk}\).  Hence block-entry admissibility remains a finite same-law data
theorem.  `square`

## 120. When Is `P32-RN-BLKDER` A Canonical Table?

### Definition 120.1: RN Block Factorization

Write

$$
\mathrm{P32\text{-}RN\text{-}BETA\text{-}FACTOR}(L)
$$

if there exists a finite map

$$
\widehat W_{RN}^{blk}:\mathbb R^4\to
\mathbb R^{E_{RN}(\Gamma_1,L)}
$$

such that

$$
W_{RN}(\theta)
=
\widehat W_{RN}^{blk}(B_{blk}(\theta))
$$

after licensed endpoint-additive, retained-row, and quotient errors.

Equivalently,

$$
D_\theta W_{RN}v=0
\qquad
\hbox{whenever}
\qquad
D_\theta B_{blk}v=0
$$

in the active quotient.  Thus every actual residual/selector direction that
leaves the four block entries unchanged must also leave the normalized
RN-MIXAMP row unchanged.

### Lemma 120.2: Chain Rule For The RN Block-Derivative Table

Assume `P32-BLKFIELD-ADM(L,sigma,C_S)` and
`P32-RN-BETA-FACTOR(L)`.  Then the canonical table
`P32-RN-BLKDER(L)` is

$$
K_{RN}^{blk}
=
D_\theta W_{RN}\,R_{blk}
=
D\widehat W_{RN}^{blk}.
$$

It is independent of the chosen controlled lift \(R_{blk}\).

Proof.

If \(R_{blk}\) and \(R'_{blk}\) are two right inverses, then
\(R_{blk}-R'_{blk}\) takes values in \(\ker D_\theta B_{blk}\).  By
`P32-RN-BETA-FACTOR`, \(D_\theta W_{RN}\) vanishes on that kernel.  Hence
\(D_\theta W_{RN}R_{blk}=D_\theta W_{RN}R'_{blk}\).  The chain rule gives the
displayed formula.  `square`

### Definition 120.3: RN Kernel-Separation Obstruction

Write

$$
\mathrm{P32\text{-}RN\text{-}KERSEP}(L,\eta)
$$

if there is an actual residual/selector vector \(v\) such that

$$
D_\theta B_{blk}v=0,
$$

but

$$
\|D_\theta W_{RN}v\|_{RN}\ge\eta
$$

in the normalized RN row norm.

### Proposition 120.4: Kernel Separation Falsifies Canonical `P32-RN-BLKDER`

If `P32-RN-KERSEP(L,eta)` holds for some \(\eta>0\), then
`P32-RN-BETA-FACTOR(L)` fails, and `P32-RN-BLKDER(L)` is not a canonical
block-entry table.

Proof.

`P32-RN-BETA-FACTOR` requires \(D_\theta W_{RN}\) to vanish on
\(\ker D_\theta B_{blk}\).  `P32-RN-KERSEP` supplies a vector in that kernel
on which \(D_\theta W_{RN}\) is nonzero.  `square`

## 121. Current-Corpus Attack On Factorization

The natural hope was that the four block entries already encode the local RN
row.  Papers 26 through 31 warn against that hope: RN-MIXAMP rows are actual
conditional ratios and endpoint-centered mixed responses, while the heat-bad
block entries are only four scalar projections of the residual/signed block.

### Proposition 121.1: RN Factorization Is Not Proved By The Current Corpus

The current corpus does not prove `P32-RN-BETA-FACTOR(L)`.

Proof.

Papers 26 and 27 define RN-MIXAMP values by actual mixed bridge amplitudes
and weighted conditional rows.  Paper 29 proves that RN-MIXAMP ratio data do
not determine low-mode conditional entries, because conditional normalizers
and endpoint factors can change data invisible to a reduced mixed table.
Paper 32 Sections 88 through 93 re-express the RN row as a mixed
source-response and show that endpoint-additive terms cancel, but they do not
prove that all remaining doubly centered residual responses are functions of
the four block entries \(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA}\).
Therefore no factor map \(\widehat W_{RN}^{blk}\) is printed.  `square`

### Proposition 121.2: Formal Dimension Heuristic Favors Kernel Separation

If the actual residual/selector tangent space touching \(\Gamma_1\) contains
a live doubly centered RN direction independent of the four heat-bad block
functionals, then `P32-RN-KERSEP(L,eta)` holds for some \(\eta>0\).

Proof.

The map \(D_\theta B_{blk}\) has rank at most four.  A live doubly centered
RN direction independent of the four heat-bad functionals can be adjusted by
subtracting a linear combination of four block-moving directions so that its
block-entry derivative vanishes while its RN derivative remains nonzero.
This adjusted direction lies in \(\ker D_\theta B_{blk}\) and has nonzero
RN derivative.  After normalization, the derivative has size \(\eta>0\) on
the finite worksheet.  `square`

### Proposition 121.3: Current Corpus Does Not Prove Kernel Separation Either

The current corpus also does not prove `P32-RN-KERSEP(L,eta)`.

Proof.

Proposition 121.2 identifies a plausible route to kernel separation, but it
requires printing an actual live doubly centered RN tangent direction and
checking its independence from the four heat-bad block functionals.  Papers
26 through 32 isolate such RN rows as live value objects, but do not print
their actual residual-coordinate derivatives.  `square`

## 122. The Correct Finite Fork

The attempt to print `P32-RN-BLKDER(L)` has therefore exposed one more finite
gate.  The correct finite fork is not simply "print \(K_{RN}^{blk}\)."  It is

$$
\mathrm{P32\text{-}BLKFIELD\text{-}ADM}
\quad+\quad
\left(
\mathrm{P32\text{-}RN\text{-}BETA\text{-}FACTOR}
\quad\hbox{or}\quad
\mathrm{P32\text{-}RN\text{-}KERSEP}
\right).
$$

If the factorization side holds, the block-entry derivative table is
canonical and the joint rank can be decided in the four-entry envelope.  If
kernel separation holds, the four-entry envelope is too small and the rank
test must be moved back to the full residual Jacobian \(J_{res}^{N,j,L}\).

### Theorem 122.1: Finite Fork Reduction

At fixed \((N,j,L)\), exactly one of the following must be sourced to proceed
with the finite joint-rank attack:

1. `P32-BLKFIELD-ADM + P32-RN-BETA-FACTOR`, giving a canonical
   `P32-RN-BLKDER(L)` table and a finite row-reduction test for
   \(J_{joint}^{blk}\);
2. `P32-RN-KERSEP`, showing that the block-entry envelope is not rich enough
   for the RN rows and forcing the full residual-coordinate rank test
   `P32-JOINT-WS-RESRANGE`;
3. a sign-coherent dual floor for the live scalar/RN target if the resulting
   rank test fails.

Proof.

Definition 119.1 is necessary to realize block-entry directions as actual
Ward vector fields.  Definition 120.1 is necessary and sufficient for the RN
row to have a canonical derivative with respect to those four entries.
Lemma 120.2 prints the derivative once these two conditions hold.  Proposition
120.4 shows that a kernel-separating direction falsifies the block-entry
factorization and therefore sends the rank problem to the full residual
Jacobian.  If either finite rank test fails, the dual separation theorem of
Section 103 supplies the corresponding floor target.  `square`

## 123. Verdict Of The Finite Derivative Attack

### Theorem 123.1: `P32-RN-BLKDER` Is Reduced, Not Printed

The present pass does not print `P32-RN-BLKDER(L)`.  It proves that printing
that table requires the sharper finite package

$$
\mathrm{P32\text{-}BLKFIELD\text{-}ADM}
\quad+\quad
\mathrm{P32\text{-}RN\text{-}BETA\text{-}FACTOR}.
$$

The current corpus proves neither this package nor its kernel-separation
alternative.

Proof.

`P32-BLKFIELD-ADM` is not proved by Proposition 119.3.
`P32-RN-BETA-FACTOR` is not proved by Proposition 121.1.
`P32-RN-KERSEP` is not proved by Proposition 121.3.  Therefore the finite
derivative attack has reduced the live task to three sharper finite same-law
data theorems, but has not closed the RN rank fork.  `square`

### Corollary 123.2: What Should Be Tried Next

The next executable target inside Paper 32 is now one of:

1. print \(D_\theta B_{blk}\) and prove `P32-BLKFIELD-ADM`;
2. print a factorization proof `P32-RN-BETA-FACTOR`, then compute
   \(K_{RN}^{blk}=D_\theta W_{RN}R_{blk}\);
3. print a kernel-separating RN direction `P32-RN-KERSEP`, then abandon the
   four-entry envelope and decide the full residual rank gate;
4. if the relevant rank gate fails, construct the sign-coherent dual floor.

This is still finite, but it is no longer mere scalar algebra.  It is the
finite actual-law derivative problem for the residual/selector coordinates.

## 124. Do Not Overpay: Scalar Admissibility Is Only Rank Two

The previous fork asked for the full four-entry block lift
`P32-BLKFIELD-ADM`.  That is necessary if we insist on a canonical
four-entry RN block-derivative table.  It is not necessary for the minimal
heat-bad scalar route.  The scalar polar defect only sees

$$
s_{blk}(\theta):=(m(\theta),t(\theta)).
$$

Thus the scalar route should not pay for the antisymmetric invisible
direction or for block-entry directions needed only by RN rows.

### Definition 124.1: Scalar Field Admissibility

Write

$$
\mathrm{P32\text{-}SCALFIELD\text{-}ADM}(L,\sigma,C_S)
$$

if, cofinally and at cutoff \(L\), the actual residual/selector chart admits
a finite linear lift

$$
R_{scal}^{N,j,L}:\mathbb R^2\to T_\theta\Theta_{res}^{N,j,L}
$$

such that

$$
D_\theta s_{blk}\,R_{scal}=I_2
$$

up to quotient error \(o(1)\), with least singular value at least
\(\sigma>0\), and with the new residual/selector Ward scores of the lifted
unit vectors bounded by \(C_S\).

Equivalently, the two formal directions \(m\) and \(t\) are actual admissible
same-law Ward directions, even if the full four-entry block chart is not.

### Lemma 124.2: Full Block Admissibility Implies Scalar Admissibility

`P32-BLKFIELD-ADM(L,sigma,C_S)` implies
`P32-SCALFIELD-ADM(L,sigma',C'_S)` with explicit constants depending only on
\(h_0,h_A,a_N,b_N\).

Proof.

The scalar map \(s_{blk}\) is the fixed linear map from
\(\beta=(\beta_{00},\beta_{0A},\beta_{A0},\beta_{AA})\) to \(m,t\) printed
in Section 113.  Compose the block right inverse \(R_{blk}\) with any
right inverse of this \(2\times4\) scalar map.  Lemma 114.1 proves the scalar
map has rank two for \(N>1\) and \(h_0h_A\ne0\).  The constants are finite
because the matrix entries are finite structural numbers.  `square`

### Lemma 124.3: Scalar Admissibility Is Sufficient For The Minimal
Heat-Bad Scalar Route

The scalar Ward-Stein certificates for \(m\) and \(t\) require only
`P32-SCALFIELD-ADM`, not full `P32-BLKFIELD-ADM`.

Proof.

Sections 114 through 116 use the vectors \(\ell_m\) and \(\ell_t\) only to
produce \(m\) and \(t\) as Ward derivatives.  If actual lifted vector fields
exist directly for the two scalar directions, the same proof applies with
those lifted fields.  The antisymmetric block direction and any RN-only block
direction never enter the minimal scalar polar defect.  `square`

### Corollary 124.4: The Scalar Attack Surface Is Smaller Than The RN Attack
Surface

For the scalar heat-bad route, the correct admissibility target is
`P32-SCALFIELD-ADM + P32-SCAL-RESDEFECT`, not the stronger
`P32-BLKFIELD-ADM + P32-RN-BETA-FACTOR`.

The stronger block/RN package is needed only for the joint scalar-plus-RN
rank route.

## 125. How To Source `P32-SCALFIELD-ADM`

The scalar admissibility gate can be sourced in exactly two same-law ways:
configuration Jacobian rank, or source-response rank.

### Definition 125.1: Scalar Configuration Jacobian Gate

Write

$$
\mathrm{P32\text{-}SCAL\text{-}CONFJAC}(L,\sigma,C_S)
$$

if the actual integration/chart variables \(\omega\) touching \(\Gamma_1\)
carry pointwise functions \(m(\omega),t(\omega)\) whose finite Jacobian

$$
G_{scal}^{conf}:=D_\omega(m,t)
$$

has a two-dimensional right inverse with least singular value at least
\(\sigma\), and whose corresponding actual Ward scores obey \(C_S\).

This is the literal Ward route: move the finite records themselves.

### Definition 125.2: Scalar Source-Response Matrix Gate

Let \(\{h_A^{N,j}\}_{A\in{\mathcal A}_{scal}(L)}\) be the retained primitive
residual or defect atoms touching the scalar heat-bad block.  Define the
source-response matrix

$$
C_{scal}^{src}(A)
:=
\left(
\partial_{s_A}\mathbf E_{N,j}^{act,s}[m]\big|_{s=0},
\partial_{s_A}\mathbf E_{N,j}^{act,s}[t]\big|_{s=0}
\right).
$$

Write

$$
\mathrm{P32\text{-}SCAL\text{-}SRCMAT}(L,\sigma,C_S)
$$

if the span of these columns has rank two with least singular value at least
\(\sigma\), and if the source-curvature/score remainder needed to convert
the source response back into the same-law scalar Ward estimate is bounded by
\(C_S\).

This is not a hidden Markov dynamics.  It is the Paper-31 source-response
calculus applied to the actual pushed-forward law at source value zero.

### Lemma 125.3: Configuration Jacobian Sources Scalar Admissibility

`P32-SCAL-CONFJAC(L,sigma,C_S)` implies
`P32-SCALFIELD-ADM(L,sigma,C_S)`.

Proof.

The right inverse for \(G_{scal}^{conf}\) gives actual vector fields on the
finite integration/chart variables whose derivatives of \(m,t\) are the two
coordinate unit vectors.  The Ward-score envelope is included in the
definition.  `square`

### Lemma 125.4: Source Matrix Is A Different Route, Not A Free Ward Lift

`P32-SCAL-SRCMAT` does not by itself imply `P32-SCALFIELD-ADM`.

Proof.

`P32-SCALFIELD-ADM` is a statement about vector fields on the actual finite
integration variables.  `P32-SCAL-SRCMAT` is a statement about derivatives
of expectations under finite source tilts evaluated at the actual law.  The
two are connected only after a source-Ward or curvature theorem controls the
source remainder.  Without that theorem, the source matrix is quantitative
same-law value information, not an admissible coordinate lift.  `square`

## 126. Current-Corpus Audit Of Scalar Admissibility

### Proposition 126.1: `P32-SCAL-CONFJAC` Is Not Printed

The current corpus does not prove `P32-SCAL-CONFJAC(L,sigma,C_S)`.

Proof.

Paper 32 prints the algebraic map from \(B_{\Gamma_1}^{N,j}\) to \(m,t\).
Papers 23, 26, and 29 print formal residual atom identities.  None prints
pointwise functions \(m(\omega),t(\omega)\) on a finite actual integration
chart together with their gradients, a two-dimensional right inverse, and
the corresponding residual/selector Ward-score envelope.  `square`

### Proposition 126.2: `P32-SCAL-SRCMAT` Is Not Printed

The current corpus does not prove `P32-SCAL-SRCMAT(L,sigma,C_S)`.

Proof.

The source-response columns in Definition 125.2 are connected scalar
cumulants between \(m,t\) and retained primitive residual or defect atoms.
Sections 94 through 99 of this paper show that connected source-cumulant
decay and its projection exports are not sourced by the current corpus.
Paper 31 proves the source-response identities but not the needed first
slopes or curvature envelopes.  `square`

### Theorem 126.3: Scalar Admissibility Is Reduced To Two Sharp Inputs

The scalar heat-bad admissibility route is now exactly reduced to

$$
\mathrm{P32\text{-}SCAL\text{-}CONFJAC}
\quad\hbox{or}\quad
\mathrm{P32\text{-}SCAL\text{-}SRCMAT},
$$

plus the already isolated score-defect target
`P32-SCAL-RESDEFECT(delta)`.

The current corpus proves neither scalar admissibility input.

Proof.

Lemmas 125.3 and 125.4 classify the two ways to make the scalar directions
actual.  Propositions 126.1 and 126.2 audit the current corpus.  The
residual score-defect remains Definition 116.2.  `square`

### Corollary 126.4: What This Pass Bought Us

The finite admissibility problem has been sharpened:

1. full four-entry `P32-BLKFIELD-ADM` is unnecessary for the minimal scalar
   route;
2. scalar closure needs only two actual directions, \(m\) and \(t\);
3. those directions must be sourced either by a configuration Jacobian theorem
   or by a source-response matrix theorem with curvature/score control;
4. neither theorem is in the current corpus.

Thus the next positive scalar theorem should attack
`P32-SCAL-CONFJAC` or `P32-SCAL-SRCMAT`, not the whole four-entry block
admissibility package.

## 127. Attack On The Configuration-Jacobian Route

The configuration-Jacobian route would be the most concrete route if it
worked: move actual finite records \(\omega\), watch \(m,t\) move, and apply
the Ward identity.  But \(m,t\) were introduced as entries of a same-law
residual/signed block table, not as already printed pointwise coordinate
functions.  This section separates the missing pointwise lift from the rank
calculation.

### Definition 127.1: Scalar Pointwise Lift

Write

$$
\mathrm{P32\text{-}SCAL\text{-}POINTLIFT}(L,\varepsilon)
$$

if the actual finite integration chart touching \(\Gamma_1\) carries
measurable same-law functions

$$
m_{\Gamma_1}^{pt}(\omega),
\qquad
t_{\Gamma_1}^{pt}(\omega),
$$

such that their finite same-law averages or conditional table entries recover
the scalar block responses \(m,t\) up to error \(\varepsilon\), and such that
the lift is compatible with the retained-row, endpoint, selector, and
normalizer conventions used in the adaptive pushed-forward law.

This is not an additional state variable.  It is a demand that the already
defined scalar table entries be represented by actual finite observables on
the same adaptive record space.

### Lemma 127.2: Configuration Jacobian Requires Pointwise Lift

`P32-SCAL-CONFJAC(L,sigma,C_S)` implies
`P32-SCAL-POINTLIFT(L,o(1))`.

Proof.

The definition of `P32-SCAL-CONFJAC` contains the pointwise functions
\(m(\omega),t(\omega)\) and differentiates them with respect to the actual
finite chart variables.  Therefore a pointwise lift of the scalar table
entries is a prerequisite, not a consequence.  `square`

### Definition 127.3: Pointwise Scalar Jacobian Package

If `P32-SCAL-POINTLIFT` holds, the actual configuration-Jacobian worksheet is
the finite matrix

$$
G_{pt}^{scal}
:=
D_\omega(m_{\Gamma_1}^{pt},t_{\Gamma_1}^{pt}),
$$

plus:

1. a rank-two lower bound for \(G_{pt}^{scal}\);
2. a controlled right inverse \(R_{pt}^{scal}\);
3. the Ward score of the two lifted vector fields
   \(R_{pt}^{scal}e_m,R_{pt}^{scal}e_t\);
4. a quotient error comparing the pointwise-lift route to the scalar block
   responses used in Section 59.

## 128. Can The Current Corpus Source The Pointwise Lift?

There are three apparent ways to source `P32-SCAL-POINTLIFT`.

1. **Atom-value lift:** express \(m,t\) as finite sums of pointwise primitive
   residual atoms and signed selector factors.
2. **Group-coordinate lift:** express \(m,t\) directly as smooth functions of
   the finite group/chart variables in the adaptive integral.
3. **Free-coordinate lift:** append \(m,t\) as formal coordinates.

The third option is not allowed unless those coordinates are proven to be
measurable functions of the same finite records.  Otherwise it is an
external variable, not a Barandes-aligned same-law observable.

### Proposition 128.1: Atom-Value Lift Is Not Sourced

The current corpus does not prove the atom-value lift version of
`P32-SCAL-POINTLIFT`.

Proof.

Papers 23, 26, and 29 prove finite Möbius existence and identify primitive
residual atoms with literal RPF residual atoms.  Paper 26 Lemma 12.6 proves
that Möbius inversion is not numerical population: it does not print the
actual residual function values.  Paper 29 proves that primitive residual
row identities still require endpoint weights, normalizers, and defect tails.
Thus the corpus does not express the scalar block responses \(m,t\) as a
printed finite pointwise atom sum with controlled error.  `square`

### Proposition 128.2: Group-Coordinate Lift Is Not Sourced

The current corpus does not prove the group-coordinate lift version of
`P32-SCAL-POINTLIFT`.

Proof.

The group/chart variables are present in the finite adaptive integral, but no
section prints formulas for \(R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}\) as
pointwise smooth functions of those variables together with derivatives,
normalizer terms, selector derivatives, and score bounds.  Sections 118
through 123 explicitly found that even the four-entry block derivative table
requires a lift/factorization theorem.  Therefore the group-coordinate lift
is an admissible future theorem, not a current proof.  `square`

### Proposition 128.3: Free Coordinates Are Not Same-Law Data

Appending \(m,t\) as independent coordinates does not prove
`P32-SCAL-CONFJAC`.

Proof.

If \(m,t\) are appended without a measurable map from the actual adaptive
record space, then the new coordinates are not observables of the same
pushed-forward law.  Ward integration by parts would then be applied to an
enlarged comparison object rather than to the actual finite law.  That would
violate the no-smuggling discipline used throughout Papers 23 through 32.
`square`

## 129. Configuration-Jacobian Verdict

### Theorem 129.1: `P32-SCAL-CONFJAC` Is Closed As A Current-Corpus Route

The current corpus does not prove `P32-SCAL-CONFJAC(L,sigma,C_S)` by any of
the available configuration-Jacobian mechanisms.

Proof.

By Lemma 127.2, configuration Jacobian requires a pointwise lift.  Proposition
128.1 rules out the currently available atom-value lift.  Proposition 128.2
rules out the currently available group-coordinate lift.  Proposition 128.3
rules out formal free coordinates as not same-law data.  Hence the
configuration-Jacobian route is closed negative at current-corpus level.
`square`

### Corollary 129.2: The Remaining Positive Scalar Route Is Source-Matrix

Inside the current Paper-32 scalar-admissibility fork, the remaining positive
route is

$$
\mathrm{P32\text{-}SCAL\text{-}SRCMAT}(L,\sigma,C_S)
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}RESDEFECT}(\delta),
$$

or else a sign-coherent scalar floor.  A future proof of
`P32-SCAL-CONFJAC` would have to bring genuinely new pointwise actual-law
data, equivalent in strength to an atom-value or group-coordinate lift.

## 130. Starting The Source-Matrix Route

The source-matrix route asks whether \(m,t\) respond independently to finite
source tilts of retained primitive residual or defect atoms.  This is a more
natural same-law question than the configuration-Jacobian route: it does not
pretend that \(m,t\) are free coordinates.  It asks how the actual scalar
table changes under finite deformations of the same adaptive law.

### Definition 130.1: Scalar Source Columns

For a retained source atom \(h_A\), define

$$
\mathcal C_A^{m}
:=
\partial_{s_A}m^{act,s}\big|_{s=0},
\qquad
\mathcal C_A^{t}
:=
\partial_{s_A}t^{act,s}\big|_{s=0}.
$$

Here \(m^{act,s},t^{act,s}\) are the scalar block responses computed from the
same finite adaptive law after the source tilt \(e^{s_Ah_A}\), with all
endpoint and normalizer conventions retained.

The scalar source matrix is

$$
C_{scal}^{src}
:=
\begin{pmatrix}
\mathcal C_{A_1}^{m}&\cdots&\mathcal C_{A_k}^{m}\\
\mathcal C_{A_1}^{t}&\cdots&\mathcal C_{A_k}^{t}
\end{pmatrix}.
$$

### Lemma 130.2: Rank-Two Source Matrix Is The Correct Linear Test

If \(C_{scal}^{src}\) has rank two with least singular value at least
\(\sigma>0\), then the source tilts can independently move the scalar pair
\((m,t)\) at first order.

Proof.

This is finite linear algebra: the image of the \(2\times k\) matrix is the
first-order source-response span of the scalar pair.  Rank two means that
image is all of \(\mathbb R^2\), and the least singular value gives the
condition number of a right inverse.  `square`

### Definition 130.3: Source Curvature Remainder

For source coefficients \(u=(u_A)\), define the second-order scalar source
curvature envelope

$$
\mathcal R_{scal}^{src}(\rho)
:=
\sup_{\|u\|\le\rho}
\left\|
(m^{act,u},t^{act,u})
-(m,t)
-C_{scal}^{src}u
\right\|.
$$

The source-matrix route needs a cofinal \(\rho\) and curvature envelope with
\(\mathcal R_{scal}^{src}(\rho)\) below the remaining scalar budget after the
linear correction.

### Proposition 130.4: Source-Matrix Route Reduces To Rank Plus Curvature

`P32-SCAL-SRCMAT(L,sigma,C_S)` is equivalent to the conjunction of:

1. a printed retained source list \(\{h_A\}_{A\in{\mathcal A}_{scal}(L)}\);
2. a printed scalar source matrix \(C_{scal}^{src}\);
3. a rank-two lower bound on \(C_{scal}^{src}\);
4. a source-curvature/score envelope \(\mathcal R_{scal}^{src}\) below the
   active budget.

Proof.

Definitions 125.2, 130.1, and 130.3 unpack exactly the data required by
`P32-SCAL-SRCMAT`.  Lemma 130.2 is the rank part.  The curvature/score
envelope is the finite same-law control needed to convert first-order source
movement into the scalar Ward estimate without leaving the actual law.
`square`

### Proposition 130.5: Current Corpus Does Not Print The Source Matrix

The current corpus does not print \(C_{scal}^{src}\).

Proof.

Paper 31 proves the formal source-response calculus, but not the scalar
source slopes \(\mathcal C_A^m,\mathcal C_A^t\).  Sections 94 through 99 of
this paper show that connected source-cumulant decay and projection exports
remain unsourced.  Therefore neither the entries nor the rank of
\(C_{scal}^{src}\) are currently printed.  `square`

### Corollary 130.6: Next Live Theorem

The next live scalar theorem is the finite same-law source-rank theorem

$$
\mathrm{P32\text{-}SCAL\text{-}SRC\text{-}RANK}(\sigma)
$$

together with the curvature theorem

$$
\mathrm{P32\text{-}SCAL\text{-}SRC\text{-}CURV}(\rho,\varepsilon).
$$

If either theorem fails in a sign-coherent way, the scalar route should pivot
to the corresponding floor.  Otherwise these two theorems are the most
economical remaining positive scalar attack.

## 131. Source-Rank Worksheet

We now execute the finite rank part of the source-matrix route.  The goal is
not to estimate curvature yet.  The goal is only to decide whether source
tilts can move the two scalar responses \(m,t\) in two independent first-
order directions.

### Definition 131.1: Retained Scalar Source List

Let

$$
{\mathcal A}_{scal}^{N,j,L}
$$

be the retained finite list of primitive residual or defect source atoms that
touch the minimal heat-bad scalar block after:

1. endpoint-additive rows are removed;
2. already retained/licensed rows are charged;
3. selector-relabeling directions are quotiented out;
4. atoms invisible to the scalar pair \(m,t\) are placed in the zero class.

For each \(A\in{\mathcal A}_{scal}^{N,j,L}\), define the source column

$$
C_A
:=
\begin{pmatrix}
\mathcal C_A^m\\
\mathcal C_A^t
\end{pmatrix}
=
\begin{pmatrix}
\partial_{s_A}m^{act,s}\big|_{s=0}\\
\partial_{s_A}t^{act,s}\big|_{s=0}
\end{pmatrix}.
$$

This column is a derivative of the actual scalar table under a finite
same-law source tilt.  It is not inferred from labels alone.

### Definition 131.2: Scalar Source Determinant

For two retained sources \(A,B\), define

$$
\Delta_{A,B}^{scal}
:=
\det(C_A,C_B)
=
\mathcal C_A^m\mathcal C_B^t
-\mathcal C_B^m\mathcal C_A^t.
$$

Write

$$
\mathrm{P32\text{-}SCAL\text{-}SRC\text{-}DET}(A,B;\Delta,M_C)
$$

if

$$
|\Delta_{A,B}^{scal}|\ge\Delta>0,
\qquad
\max\{\|C_A\|_2,\|C_B\|_2\}\le M_C<\infty.
$$

### Lemma 131.3: Determinant Criterion For Source Rank

If `P32-SCAL-SRC-DET(A,B;Delta,M_C)` holds, then
`P32-SCAL-SRC-RANK(sigma)` holds with

$$
\sigma\ge{\Delta\over 2M_C}.
$$

Proof.

Let \(C_{A,B}\) be the \(2\times2\) matrix with columns \(C_A,C_B\).  Its
least singular value obeys

$$
s_{\min}(C_{A,B})
=
{|\det C_{A,B}|\over s_{\max}(C_{A,B})}.
$$

The largest singular value is at most the Frobenius norm, hence at most
\(\|C_A\|_2+\|C_B\|_2\le2M_C\).  The displayed bound follows.  Since
\(C_{A,B}\) is a submatrix of \(C_{scal}^{src}\), the full source matrix has
least nonzero two-dimensional lower bound at least this amount on the
selected two-source subspace.  `square`

### Definition 131.4: Scalar Source Rank Gap

For \(\sigma>0\), write

$$
\mathrm{P32\text{-}SCAL\text{-}SRC\text{-}RANK\text{-}GAP}(\sigma)
$$

if every retained pair \(A,B\) either has

$$
|\Delta_{A,B}^{scal}|<\sigma
$$

or has a column-norm/curvature cost too large to fit inside the scalar
Branch-A budget.

This is a finite negative rank statement.  It is stronger than merely saying
that rank has not been proved.

## 132. Channel Split Of Scalar Source Columns

The retained scalar source list has a useful finite channel split.  This is
bookkeeping, but it prevents us from paying for dead columns.

### Definition 132.1: Scalar Source Channel Classes

Partition

$$
{\mathcal A}_{scal}^{N,j,L}
=
{\mathcal A}_0
\sqcup
{\mathcal A}_m
\sqcup
{\mathcal A}_t
\sqcup
{\mathcal A}_{mix}
$$

as follows:

1. \(A\in{\mathcal A}_0\) if \(C_A=0\) in the scalar quotient;
2. \(A\in{\mathcal A}_m\) if \(C_A=(\mathcal C_A^m,0)^T\) with
   \(\mathcal C_A^m\ne0\);
3. \(A\in{\mathcal A}_t\) if \(C_A=(0,\mathcal C_A^t)^T\) with
   \(\mathcal C_A^t\ne0\);
4. \(A\in{\mathcal A}_{mix}\) if both components may be present after all
   endpoint-additive, retained-row, and selector quotient cancellations.

Endpoint-additive and selector-only sources belong to \({\mathcal A}_0\)
after the licensed quotient is applied.

### Lemma 132.2: Zero And One-Channel Sources Cannot Prove Rank Alone

The classes \({\mathcal A}_0\), \({\mathcal A}_m\) alone, or
\({\mathcal A}_t\) alone cannot prove `P32-SCAL-SRC-RANK`.

Proof.

Columns in \({\mathcal A}_0\) vanish.  Columns in \({\mathcal A}_m\) lie on
the \(m\)-axis; columns in \({\mathcal A}_t\) lie on the \(t\)-axis.  Any
single axis has rank at most one.  `square`

### Lemma 132.3: The Minimal Positive Rank Pattern

`P32-SCAL-SRC-RANK` follows if either:

1. there exist \(A\in{\mathcal A}_m\), \(B\in{\mathcal A}_t\) with both
   nonzero components bounded below and column costs bounded above; or
2. there exist two sources in
   \({\mathcal A}_m\cup{\mathcal A}_t\cup{\mathcal A}_{mix}\) whose determinant
   satisfies Definition 131.2.

Proof.

The first case gives a diagonal \(2\times2\) determinant.  The second case is
Lemma 131.3.  `square`

## 133. Current-Corpus Attack On Source Rank

We now ask whether the current corpus prints any determinant pair.

### Proposition 133.1: Endpoint And Selector Structure Only Removes Columns

The endpoint-additive and selector-only structural results do not prove
`P32-SCAL-SRC-RANK`.

Proof.

Endpoint-additive cancellations and selector-only quotienting place sources
in \({\mathcal A}_0\).  Removing zero columns simplifies the matrix but does
not create two independent nonzero columns.  `square`

### Proposition 133.2: Channel Labels Do Not Print Nonzero Components

The channel split of Definition 132.1 does not by itself prove that any
\(\mathcal C_A^m\) or \(\mathcal C_A^t\) is bounded away from zero.

Proof.

The split records which components are allowed by the quotient and symmetry
bookkeeping.  It does not evaluate the same-law source derivative of the
actual scalar table.  Paper 31 proves that source derivatives are exact
targets, not automatic numerical estimates.  `square`

### Proposition 133.3: No Determinant Pair Is Printed

The current corpus does not prove
`P32-SCAL-SRC-DET(A,B;Delta,M_C)` for any retained pair \(A,B\) with
\(\Delta>0\) in the closing range.

Proof.

Sections 124 through 130 define the scalar source-matrix route.  Sections
94 through 99 show that connected source-cumulant decay and projection
exports are not sourced.  Paper 31 supplies the derivative dictionary but
does not print the scalar source slopes.  Therefore no pair of retained
source columns has a printed determinant lower bound.  `square`

### Proposition 133.4: The Rank Gap Is Not Printed Either

The current corpus does not prove
`P32-SCAL-SRC-RANK-GAP(sigma)` in a sign-coherent closing range.

Proof.

Failure to print a positive determinant is not the same as proving all
determinants are small or too costly.  A rank-gap theorem would need upper
bounds on every determinant pair, or a structural collinearity theorem for
all retained source columns, plus the corresponding scalar floor sign.  No
such determinant upper table or sign-coherent floor is printed.  `square`

## 134. Source-Rank Verdict

### Theorem 134.1: Source Rank Is Decided By A Finite Determinant Table

At fixed \((N,j,L)\), the scalar source-rank fork is exactly:

1. print a determinant pair
   `P32-SCAL-SRC-DET(A,B;Delta,M_C)`, which implies
   `P32-SCAL-SRC-RANK(Delta/(2M_C))`;
2. print `P32-SCAL-SRC-RANK-GAP(sigma)` plus a sign-coherent scalar floor;
3. otherwise the scalar source-rank route remains open but unsourced.

Proof.

The matrix \(C_{scal}^{src}\) is finite.  Rank two is equivalent to the
existence of a nonzero \(2\times2\) minor.  Lemma 131.3 turns a quantitative
minor into a least-singular-value lower bound.  Definition 131.4 is the
finite quantitative negation needed for a rank-gap route.  `square`

### Theorem 134.2: Current-Corpus Source-Rank Verdict

The current corpus proves neither `P32-SCAL-SRC-RANK(sigma)` nor
`P32-SCAL-SRC-RANK-GAP(sigma)` in a closing range.

Proof.

Positive rank is not proved by Proposition 133.3.  The negative rank gap is
not proved by Proposition 133.4.  Hence the rank worksheet is fully reduced
to a finite determinant table, but not closed by existing results.  `square`

### Corollary 134.3: What Should Be Attacked Next

The next useful scalar move is not curvature.  Curvature matters only after a
rank-two source matrix is printed.  The next theorem should be one of:

$$
\mathrm{P32\text{-}SCAL\text{-}SRC\text{-}DET}(A,B;\Delta,M_C),
$$

for an explicit retained source pair \(A,B\), or

$$
\mathrm{P32\text{-}SCAL\text{-}SRC\text{-}RANK\text{-}GAP}(\sigma)
$$

together with a sign-coherent scalar floor.

Thus Paper 32 has converted the source-rank problem into an explicit finite
minor problem.  More source labels or symmetry classes will not decide it
without actual same-law source-column values.

## 135. Structural Source Tomography

The determinant route above still asks for source columns attached to retained
residual atoms.  A different viewpoint is possible: do not ask for many atom
columns.  Ask whether the two scalar responses \(m,t\) are conjugate to two
natural finite structural knobs on the singlet-adjoint block itself.

This is the finite analogue of changing coordinates until the hard quantity
is a response coefficient rather than a hidden table entry.

### Definition 135.1: Two-Knob Structural Block Source

Let

$$
P_I:=I_2,
\qquad
P_U:=U_N.
$$

For source parameters \((\alpha,\zeta)\) define the formal structural
channel deformation

$$
S_{\alpha,\zeta}
:=
\exp(\alpha P_I+\zeta P_U).
$$

At the level of the minimal block, the desired source observable is the
finite support pairing

$$
V_{\alpha,\zeta}^{str}
:=
\operatorname{Tr}
\left[
(\alpha P_I+\zeta P_U)
\Pi_+^{U_N}
\left(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}\right)
\right].
$$

The corresponding structural pressure is

$$
\Phi_{str}^{N,j}(\alpha,\zeta)
:=
\log
\mathbf E_{N,j}^{act}
\exp\left(V_{\alpha,\zeta}^{str}\right).
$$

This definition is only a formal target until the observable
\(V_{\alpha,\zeta}^{str}\) is represented as a finite same-law observable on
the actual adaptive record space.  That representation is the first gate
below.

### Definition 135.2: Structural Source Realization

Write

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}ID}(\varepsilon)
$$

if \(V_{\alpha,\zeta}^{str}\) is realized by a finite actual-law source
observable, with the same endpoint, selector, normalizer, and retained-row
conventions as the adaptive law, and

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

cofinally.  Lemma 59.1 gives the compression

$$
\Pi_+^{U_N}
\left(D_{\Gamma_1}^{HK}B_{\Gamma_1}^{N,j}\right)
=
{m\over2}I_2+{t\over2}U_N.
$$

The factor \(1/2\) in this compression is exactly canceled by
\(\operatorname{Tr}(I_2I_2)=\operatorname{Tr}(U_N^2)=2\).
The gate says that the two scalar table entries have become first
derivatives of a finite same-law structural pressure.

### Lemma 135.3: Realized Structural Sources Recover The Scalar Pair

If `P32-SCAL-STRUCTSRC-ID(epsilon)` holds, then the scalar table
\((m,t)\) is recovered from the structural source gradient up to error
\(\varepsilon\).

Proof.

Differentiate Definition 135.1 at \((0,0)\).  Since
\(\operatorname{Tr}(I_2I_2)=2\), \(\operatorname{Tr}(U_N^2)=2\), and
\(\operatorname{Tr}(U_N)=0\), Lemma 59.1 gives

$$
\partial_\alpha V_{\alpha,\zeta}^{str}\big|_0=m,
\qquad
\partial_\zeta V_{\alpha,\zeta}^{str}\big|_0=t.
$$

Definition 135.2 is exactly the same identity after same-law realization and
the declared normalization convention.  `square`

## 136. Gram Rank And Rigidity

If the two structural knobs are realized, the next rank object is not an
arbitrary source-column table.  It is the Hessian of one finite pressure.

### Definition 136.1: Structural Gram Matrix

Assuming `P32-SCAL-STRUCTSRC-ID`, define

$$
G_{str}^{N,j}
:=
\nabla^2_{\alpha,\zeta}\Phi_{str}^{N,j}(0,0)
=
\begin{pmatrix}
\partial_{\alpha\alpha}^2\Phi_{str}&
\partial_{\alpha\zeta}^2\Phi_{str}\\
\partial_{\zeta\alpha}^2\Phi_{str}&
\partial_{\zeta\zeta}^2\Phi_{str}
\end{pmatrix}_{(0,0)}.
$$

Equivalently, after realization,

$$
G_{str}^{N,j}
=
\operatorname{Cov}_{N,j}^{act}
\left(
\begin{pmatrix}
V_I\\
V_U
\end{pmatrix}
\right),
$$

where \(V_I=\partial_\alpha V_{\alpha,\zeta}^{str}|_0\) and
\(V_U=\partial_\zeta V_{\alpha,\zeta}^{str}|_0\).

Write

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}(\sigma,M)
$$

if

$$
\det G_{str}^{N,j}\ge\sigma^2>0,
\qquad
\|G_{str}^{N,j}\|_{op}\le M<\infty
$$

cofinally.

### Lemma 136.2: Gram Positivity Gives Source Rank

If `P32-SCAL-STRUCTSRC-ID(epsilon)` and
`P32-SCAL-STRUCTSRC-GRAM(sigma,M)` hold with \(\varepsilon\) below the
scalar tolerance, then the structural two-knob source supplies the rank part
of the scalar source-matrix route.

Proof.

The two structural columns are the derivatives of the scalar source gradient
with respect to \(\alpha\) and \(\zeta\).  These columns are the columns of
\(G_{str}\).  The determinant lower bound gives rank two, and the operator
upper bound gives a finite right-inverse norm exactly as in Lemma 131.3.
The realization error is paid in the scalar tolerance.  `square`

### Definition 136.3: Structural Rigidity/Floor Alternative

Write

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}RIGIDFLOOR}(M_*)
$$

if \(\det G_{str}=0\) cofinally and the resulting finite linear relation

$$
aV_I+bV_U=c
$$

is sign-coherent in the Branch-A scalar ledger and forces

$$
\max\{|m|,|t|\}\ge M_*.
$$

This is the negative side of tomography.  Degenerate Gram geometry is useful
only if the forced relation has a sign and magnitude that reaches the scalar
floor.

### Lemma 136.4: Gram Degeneracy Alone Is Not A Floor

The condition \(\det G_{str}=0\) does not by itself prove
`P32-SCAL-STRUCTSRC-RIGIDFLOOR`.

Proof.

A singular covariance matrix says that some finite linear combination of the
realized structural observables is almost surely constant.  The constant may
be zero, may have the wrong sign, or may be assigned to an already licensed
ledger.  A lower floor additionally needs sign coherence and a magnitude
bound in the Branch-A scalar ledger.  `square`

## 137. Clean Structural Sources Do Not Yet Realize \(m,t\)

The obvious implementation of the structural source is to deform only the
clean heat diagonal \(D_{\Gamma_1}^{HK}\).  That is not enough.

### Definition 137.1: Clean Channel Source

A clean channel source is a source that changes only

$$
D_{\Gamma_1}^{HK}
$$

or the structural channel factors \(I_2,U_N\), while leaving the actual
residual/signed product

$$
B_{\Gamma_1}^{N,j}=R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}
$$

unrepresented in the finite observable being differentiated.

### Proposition 137.2: Clean Channel Sources See The Wrong Object

Clean channel sources do not prove `P32-SCAL-STRUCTSRC-ID`.

Proof.

The scalar pair \(m,t\) is not a function of the heat diagonal alone.  By
Corollary 59.2,

$$
m=h_0\beta_{00}+h_A\beta_{AA},
$$

and

$$
t
=
a_N(h_0\beta_{00}-h_A\beta_{AA})
+b_N(h_0\beta_{0A}+h_A\beta_{A0}),
$$

where the \(\beta\)-entries are entries of
\(B_{\Gamma_1}^{N,j}=R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j}\).  A clean
source that varies only \(D_{\Gamma_1}^{HK}\) differentiates the clean
channel weights, not the residual/signed product entries.  Therefore it can
recover \(m,t\) only after an additional coupling theorem identifies the
clean channel derivative with the weighted residual product.  `square`

### Definition 137.3: Structural Coupling Theorem

Write

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon)
$$

if the clean structural source can be coupled to the actual residual/signed
product so that the realized finite observable differs from
\(V_{\alpha,\zeta}^{str}\) by at most \(\varepsilon\) in the source-gradient
norm.

This is the precise theorem needed to turn clean structural tomography into
actual scalar tomography.

## 138. Current-Corpus Verdict On Structural Tomography

### Proposition 138.1: Structural Coupling Is Not Printed

The current corpus does not prove
`P32-SCAL-STRUCTSRC-COUPLE(epsilon)` in a closing range.

Proof.

Papers 30 through 32 print the clean heat diagonal, the recoupling matrix
\(U_N\), and the algebraic compression from \(B_{\Gamma_1}\) to \(m,t\).
They do not print a same-law identity coupling a clean channel deformation to
the actual residual/signed product \(R_{\Gamma_1}\Sigma_{\Gamma_1}\).
Earlier atom-value and residual-value audits, especially Papers 26, 29, and
31, identify this product as exactly the missing actual-law value object.
`square`

### Proposition 138.2: The Structural Gram Is Not Printed

The current corpus does not prove
`P32-SCAL-STRUCTSRC-GRAM(sigma,M)`.

Proof.

The Gram matrix is a covariance matrix of the realized structural observables
\((V_I,V_U)\).  Since the realization/coupling theorem is not printed, the
observables themselves are not available as finite same-law objects with the
needed normalization.  Consequently their covariance determinant is also not
printed.  `square`

### Proposition 138.3: The Rigidity/Floor Alternative Is Not Printed

The current corpus does not prove
`P32-SCAL-STRUCTSRC-RIGIDFLOOR(M_*)`.

Proof.

No paper prints a singular structural Gram relation together with a
sign-coherent scalar lower bound for \(m,t\).  Lemma 136.4 shows that
singularity alone would not be enough even if it were known.  `square`

### Theorem 138.4: Structural Tomography Is A Valid New Route But Not A
Current-Corpus Proof

The structural tomography route is valid and Barandes-aligned in the
following conditional form:

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}
$$

sources the rank half of the scalar route, while
`P32-SCAL-STRUCTSRC-RIGIDFLOOR` is the negative exit.  The current corpus
proves none of these three primitive inputs.

Proof.

The route is same-law because all derivatives are taken at source value zero
inside the actual finite pushed-forward law.  Lemma 136.2 proves the positive
rank implication.  Definition 136.3 is the floor exit.  Propositions 138.1,
138.2, and 138.3 audit the current corpus.  `square`

### Corollary 138.5: What The Viewpoint Bought Us

The new viewpoint did not magically populate \(m,t\), but it improved the
shape of the next theorem.  Instead of searching through many retained atom
columns, one may try to prove the two-knob structural coupling and Gram
theorem:

$$
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}COUPLE}(\varepsilon)
\quad+\quad
\mathrm{P32\text{-}SCAL\text{-}STRUCTSRC\text{-}GRAM}(\sigma,M).
$$

This is the most compact positive scalar source target currently visible in
Paper 32.  Its obstruction is also clear: clean structural knobs alone see
the heat channel, not the actual residual/signed product.
