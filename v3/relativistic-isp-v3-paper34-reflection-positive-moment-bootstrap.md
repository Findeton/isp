# Relativistic ISP V3 Paper 34: Reflection-Positive Moment Bootstrap

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Paper 33 closes the residual-score bootstrap at current-corpus level and
identifies a remaining creative possibility: perhaps reflection positivity,
used as a same-law noncommutative moment constraint on the actual
signed/residual block

$$
B_{\Gamma_1}^{N,j}=R_{\Gamma_1}^{N,j}\Sigma_{\Gamma_1}^{N,j},
$$

can cut the scalar ray

$$
B_{\Gamma_1}^{N,j}=cI_2
$$

without first computing the missing residual values.  This paper investigates
that possibility fully at the finite same-law level.

The answer is sharp.  Reflection positivity is a valid Barandes-aligned
constraint when it is imposed on finite record functions under the actual
adaptive law.  It gives finite semidefinite programs and finite dual
sum-of-squares certificates.  However, ordinary reflection-positive moment
positivity does not cut the scalar ray.  For every permitted scalar value
\(c\), the deterministic reflection-invariant law with \(B=cI_2\) extends to
all finite reflection-positive moment matrices.  Hence all RP/SOS
constraints built only from the current affine identities, gauge covariance,
heat data, recoupling data, pointwise envelopes, and passive moment
positivity remain non-closing.

The only RP routes that could still work are genuinely new same-law value
theorems:

1. an RP upper-moment inequality involving \(R\Sigma\);
2. a reflection-odd or orientation theorem for the live scalar;
3. a Schur-complement inequality with a licensed small diagonal;
4. a reflection-compatible structural coupling theorem;
5. a sign-coherent RP floor.

None is printed by the current corpus.  Thus Paper 34 closes the
reflection-positive bootstrap as another exact but currently non-sourcing
route.  The next breakthrough must still add new same-law quantitative
information, not merely more finite positivity.

## 0. Imports And Alignment Rule

### Import 0.1: Paper-33 Scalar Endpoint

Paper 33 proves that the current finite same-law bootstrap contains the
scalar ray

$$
B(c)=cI_2,
$$

with

$$
m=c(h_0+h_A),
\qquad
t=ca_N(h_0-h_A),
$$

and

$$
\lambda_+={m+t\over2},
\qquad
\lambda_-={m-t\over2}.
$$

Ordinary finite moment positivity, gauge covariance, recoupling identities,
and the printed heat-kernel data do not bound \(m,t\) below the scalar
envelope and do not orient a floor.

### Import 0.2: Paper-31 Same-Law Source Discipline

Paper 31's rule is still active: every source, moment, or representation
object must be a finite function of the same record law.  A source parameter
is a probe; it is not a new physical dynamics or a replacement measure.

### Import 0.3: Barandes Alignment

The primitive object is an indivisible stochastic record law.  Reflection
positivity may be used only as a constraint on actual record functions:

$$
\mathbf E^{act}[(\Theta F)F]\ge0.
$$

It is not a hidden Markov transfer matrix, not an off-law Euclidean path
measure, and not an extra beable.  Hilbert, Peter-Weyl, and operator symbols
are calculational representations of finite record functions.

## 1. The Reflection-Positive Moment Viewpoint

Reflection positivity is attractive because it can produce inequalities that
ordinary scalar positivity cannot see.  The hope is that a noncommutative
moment matrix involving \(B=R\Sigma\) and its reflected copy might force
smallness of \(m,t\), or else orient a floor.

### Definition 1.1: Finite Reflection-Positive Record Algebra

Fix \(N,j,L\).  A finite RP record algebra

$$
{\mathcal A}_{RP}^{N,j,L}
$$

is a finite real unital algebra of record functions containing:

1. the live block entries of \(B_{\Gamma_1}^{N,j}\);
2. the scalar functions \(m,t,\lambda_+,\lambda_-\);
3. the heat-bad projectors and singlet-adjoint channel projectors retained
   in Papers 30 through 33;
4. any declared low Peter-Weyl modes at cutoff \(L\);
5. any selector-stable record functions included in the worksheet.

A reflection is a linear involution

$$
\Theta:{\mathcal A}_{RP}^{N,j,L}\to{\mathcal A}_{RP}^{N,j,L}
$$

compatible with the licensed record reflection and with the declared
finite cutoff.

### Definition 1.2: RP Moment Matrix

For a finite list \(A_1,\ldots,A_s\in{\mathcal A}_{RP}^{N,j,L}\), define

$$
M_{ab}^{RP}
=
\mathbf E[(\Theta A_a)A_b].
$$

The RP constraint is

$$
M^{RP}\succeq0
$$

for every declared list.  A finite worksheet only contains finitely many
such lists, so the resulting constraint is semidefinite.

### Definition 1.3: RP Bootstrap Space

Let

$$
{\mathfrak L}_{RP}^{N,j,L}
$$

be the set of finite laws on the same record alphabet satisfying:

1. the Paper-33 bootstrap constraints;
2. all declared RP moment constraints \(M^{RP}\succeq0\);
3. all declared reflection covariance identities;
4. the same pointwise envelopes and finite cutoff conventions.

Write `P34-RP-RAYCUT(B_rem)` if this bootstrap proves

$$
\sup_{\nu\in{\mathfrak L}_{RP}^{N,j,L}}
\max\{|\mathbf E_\nu m|,|\mathbf E_\nu t|\}
\le B_{rem}
$$

cofinally with \(B_{rem}\) below the Branch-A scalar budget.

Write `P34-RP-FLOOR(M_*)` if the RP bootstrap proves a sign-coherent lower
floor for one of \(m,t,\lambda_+,\lambda_-\).

## 2. Finite RP/SOS Certificates

### Definition 2.1: RP/SOS Upper Certificate

A finite RP/SOS upper certificate for a scalar functional \(F\) is an
identity

$$
B_{rem}^2-F^2
=
\sum_i a_iC_i
+\sum_k\langle P_k,M_k^{RP}\rangle
+\sum_\ell\langle Q_\ell,M_\ell\rangle
+\sum_r s_r^2
+E_{tail},
$$

where \(C_i=0\) are licensed affine constraints,
\(P_k,Q_\ell\succeq0\), \(M_k^{RP}\succeq0\) are RP moment matrices,
\(M_\ell\succeq0\) are ordinary moment matrices, \(s_r^2\) are manifest
squares, and \(E_{tail}\) is an already licensed tail debit.

### Definition 2.2: RP/SOS Floor Certificate

A finite RP/SOS floor certificate has the same form with the oriented
functional \(F-M_*\) on the left, and with the sign convention licensed by
the Branch-A floor ledger.

### Theorem 2.3: Soundness Of RP/SOS Certificates

An RP/SOS upper certificate implies the corresponding upper bound for every
law in \({\mathfrak L}_{RP}^{N,j,L}\).  An RP/SOS floor certificate implies
the corresponding sign-coherent lower floor for every law in
\({\mathfrak L}_{RP}^{N,j,L}\).

Proof.

Evaluate the certificate under any admissible law.  The affine constraints
vanish.  The RP and ordinary moment terms are nonnegative because the
moment matrices and dual matrices are positive semidefinite.  The square
terms are nonnegative and the tail term is already licensed.  This gives the
upper or floor inequality exactly as in Paper 33, now with additional RP
positive terms.  `square`

### Corollary 2.4: RP Bootstrap Is Barandes-Aligned

The RP bootstrap is Barandes-aligned if every \(A_a\) is an actual finite
record function and \(\Theta\) is a licensed operation on record functions.

Proof.

The only expectations are \(\mathbf E[(\Theta A)B]\) under the same law.
No Markov factorization, off-law Euclidean measure, or hidden transfer
dynamics is introduced.  The RP matrix is a finite moment matrix of record
functions.  `square`

## 3. The All-Degree Scalar-Ray Test

The decisive test is whether the scalar ray from Paper 33 survives RP
moments.  If it survives, passive RP positivity cannot be the missing
theorem.

### Definition 3.1: Passive RP Worksheet

An RP worksheet is passive if its additional constraints are only:

1. RP moment positivity;
2. reflection covariance identities that are already satisfied by scalar
   intertwiners;
3. ordinary moment positivity;
4. affine identities already imported by Paper 33.

It does not include a new value inequality such as an RP upper moment bound,
an RP oddness condition on \(m,t\), or a sign-oriented floor.

### Lemma 3.2: Deterministic RP Moment Matrices Are Positive

Let \(\nu_x\) be a deterministic law at a record \(x\).  If \(\Theta\) fixes
the values of the declared scalar-ray observables at \(x\), then every RP
moment matrix is positive semidefinite.

Proof.

For any declared list \(A_1,\ldots,A_s\), set

$$
v_a=A_a(x).
$$

Since \(\Theta A_a\) has the same scalar-ray value as \(A_a\) at \(x\),

$$
M_{ab}^{RP}
=
(\Theta A_a)(x)A_b(x)
=
v_av_b.
$$

Thus \(M^{RP}=vv^T\succeq0\).  `square`

### Lemma 3.3: The Scalar Ray Has A Reflection-Invariant Extension

For every real \(c\) allowed by the Paper-33 envelope, there is a
deterministic same-record law \(\nu_c^{RP}\) extending the scalar-ray law
with

$$
B(c)=cI_2
$$

and satisfying every passive finite RP worksheet.

Proof.

Take the Paper-33 scalar-ray law and assign every additional worksheet
observable its scalar-compatible value.  For products, use multiplicative
evaluation at that record.  For reflected products, use the same scalar
value because \(I_2\) is fixed by every licensed scalar reflection and
recoupling operation.  The affine identities hold because they already held
in Paper 33 and scalar intertwiners commute with the declared channel
projections.  Ordinary moment matrices and RP moment matrices are
rank-one positive semidefinite by deterministic evaluation and Lemma 3.2.
`square`

### Theorem 3.4: Passive RP/SOS Does Not Cut The Scalar Ray

No passive finite RP worksheet proves `P34-RP-RAYCUT(B_rem)` for any

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

By Lemma 3.3, every allowed \(c\) gives an admissible RP law.  Along that
law, Paper 33 gives

$$
m=c(h_0+h_A),
\qquad
t=ca_N(h_0-h_A).
$$

Taking \(|c|=M_\beta\) and choosing the sign gives the displayed lower
range for the RP bootstrap supremum.  `square`

### Corollary 3.5: Passive RP/SOS Does Not Prove A Floor

No passive finite RP worksheet proves `P34-RP-FLOOR(M_*)` for any positive
sign-coherent floor on \(m,t,\lambda_+,\lambda_-\).

Proof.

If \(c\) is feasible, then \(-c\) is feasible by the same construction in
Lemma 3.3.  The four floor candidates are linear in \(c\).  Thus every
positive orientation is paired with an admissible law carrying the opposite
orientation.  `square`

### Corollary 3.6: Higher-Degree RP Moments Do Not Help Passively

Adding higher-degree monomials from the same passive algebra cannot change
Theorem 3.4.

Proof.

The deterministic scalar-ray extension evaluates every polynomial word at a
number.  Every ordinary or RP moment matrix built from finitely many such
words is still an outer product \(vv^T\).  Hence every finite degree passes.
`square`

## 4. Attempted RP Routes And Their Exact Failure Modes

The scalar-ray no-go does not say reflection positivity is useless.  It says
reflection positivity must be paired with a non-passive same-law theorem.
We now audit every plausible non-passive RP route.

### Route A: RP Upper-Moment Inequality

Define `P34-RP-UPMOM(C_RP,D_lic)` to mean that for every unit dual vector
\((\alpha,\zeta)\) in the norm dual to
\(\max\{|m|,|t|\}\),

$$
\mathbf E[(\alpha m+\zeta t)^2]
\le
C_{RP}(\alpha,\zeta)\mathbf E[D_{lic}],
$$

where \(D_{lic}\) is a licensed nonnegative debit already below the Branch-A
budget.

### Lemma 4.1: RP Upper-Moment Would Cut The Ray

If `P34-RP-UPMOM(C_RP,D_lic)` holds in a range where

$$
\sup_{\|(\alpha,\zeta)\|_*=1}
\sqrt{C_{RP}(\alpha,\zeta)\mathbf E[D_{lic}]}
<B_{rem},
$$

then `P34-RP-RAYCUT(B_rem)` holds.

Proof.

Choose \((\alpha,\zeta)\) to be the unit dual vector attaining the norm of
\((\mathbf E m,\mathbf E t)\).  Jensen gives

$$
|\alpha\mathbf E m+\zeta\mathbf E t|^2
\le
\mathbf E[(\alpha m+\zeta t)^2].
$$

Apply the upper-moment theorem and optimize over dual vectors.  `square`

### Proposition 4.2: RP Positivity Alone Does Not Source `RP-UPMOM`

The current corpus does not prove `P34-RP-UPMOM(C_RP,D_lic)` in a closing
range.

Proof.

Reflection positivity gives nonnegativity of matrices
\(\mathbf E[(\Theta A_a)A_b]\).  It gives Cauchy-Schwarz inequalities
between entries of the same positive matrix.  It does not upper-bound the
diagonal entry \(\mathbf E[(\alpha m+\zeta t)^2]\) by a separate licensed
small debit.  The deterministic scalar-ray laws in Lemma 3.3 satisfy all RP
positivity constraints while making this diagonal as large as the envelope
allows.  Therefore a closing `RP-UPMOM` theorem would be new same-law value
information.  `square`

### Route B: Reflection-Odd Scalar

Define `P34-RP-ODD(delta)` to mean that the actual reflection obeys

$$
\left|\mathbf E[\Theta V+V]\right|\le2\delta
$$

for every unit live scalar

$$
V=\alpha m+\zeta t.
$$

If \(\Theta V=-V\) exactly and the law is reflection invariant, then
\(\mathbf E[V]=0\).

### Lemma 4.3: Reflection-Oddness Would Close Smallness

If `P34-RP-ODD(delta)` holds, then

$$
\max\{|\mathbf E m|,|\mathbf E t|\}\le\delta
$$

up to the chosen dual norm convention.

Proof.

For every unit dual vector \(V=\alpha m+\zeta t\), reflection invariance
gives \(\mathbf E[\Theta V]=\mathbf E[V]\).  The oddness estimate gives
\(|2\mathbf E[V]|\le2\delta\).  Optimize over unit dual vectors.  `square`

### Proposition 4.4: Current Reflection Does Not Make The Scalar Ray Odd

The current corpus does not prove `P34-RP-ODD(delta)` in a closing range.

Proof.

The scalar ray is \(B=cI_2\).  Scalar intertwiners are fixed by the licensed
gauge, recoupling, and passive reflection operations.  Thus the natural
passive reflection sends \(cI_2\) to \(cI_2\), not to \(-cI_2\).  Any
theorem making \(m\) or \(t\) reflection-odd would therefore be a new
orientation theorem for the actual residual/signed factor, not a consequence
of the printed scalar reflection structure.  `square`

### Route C: RP Schur Complement With A Small Licensed Diagonal

Define `P34-RP-SCHUR(D_0,D_1,\epsilon)` to mean that a declared RP matrix
contains the block

$$
\begin{pmatrix}
\mathbf E[(\Theta X)X]&\mathbf E[(\Theta X)V]\\
\mathbf E[(\Theta V)X]&\mathbf E[(\Theta V)V]
\end{pmatrix}
\succeq0
$$

with

$$
\mathbf E[(\Theta X)X]\le D_0,
\qquad
\mathbf E[(\Theta V)V]\le D_1,
$$

and at least one of \(D_0,D_1\) licensed small enough to force the live
entry below \(\epsilon\).

### Lemma 4.5: Schur Complement Gives A Cross Bound

Under `P34-RP-SCHUR(D_0,D_1,epsilon)`,

$$
\left|\mathbf E[(\Theta X)V]\right|
\le
\sqrt{D_0D_1}.
$$

Proof.

This is the Cauchy-Schwarz inequality for a positive semidefinite
\(2\times2\) matrix.  `square`

### Proposition 4.6: The Needed Small Diagonal Is Not Printed

The current corpus does not source a closing Schur-complement RP route.

Proof.

RP positivity supplies the \(2\times2\) matrix inequality.  It does not
supply a small diagonal.  If \(V\) is the live scalar itself, the diagonal
\(\mathbf E[(\Theta V)V]\) is precisely a live second moment and is large on
the scalar-ray models.  If \(X\) is a licensed defect, the corpus has not
printed a same-law identity tying \(\mathbf E[(\Theta X)V]\) to \(m,t\) with
a small licensed \(\mathbf E[(\Theta X)X]\).  Thus Schur complement is a
valid certificate form but not a sourced theorem.  `square`

### Route D: Reflection-Compatible Structural Coupling

Define `P34-RP-STRUCTCOUPLE(sigma,epsilon)` to mean that the Paper-32
structural source observables are realized on the same adaptive law, have a
reflection-positive covariance determinant at least \(\sigma>0\), and their
first response columns equal \(m,t\) up to error \(\epsilon\).

### Proposition 4.7: Structural RP Coupling Is Exactly The Old Coupling Gate

`P34-RP-STRUCTCOUPLE` would close the scalar route if proved in a closing
range, but the current corpus does not source it.

Proof.

A positive RP covariance determinant is stronger than the Paper-32 Gram gate
only after the structural source is realized on the actual residual/signed
product.  Paper 32 and Paper 33 both prove that clean structural sources
alone see the heat channel rather than \(R\Sigma\).  Therefore the RP
version still requires the same missing coupling theorem, now with RP
covariance language.  `square`

### Route E: RP Floor

Define `P34-RP-FLOOR-WIT(M_*)` to mean that a finite RP/SOS dual functional
\(\Lambda\) satisfies:

1. \(\Lambda\) is nonnegative on all licensed affine, ordinary moment, and RP
   moment cones;
2. \(\Lambda\) evaluates a retained live floor functional above \(M_*\);
3. the sign orientation survives selector, endpoint, and tail debits.

### Proposition 4.8: RP Floor Is Valid But Unsourced

`P34-RP-FLOOR-WIT(M_*)` is a valid negative exit from adaptive Branch A, but
the current corpus does not print such a witness.

Proof.

Soundness follows from Theorem 2.3.  Non-sourcing follows from the symmetric
scalar-ray pair \(\nu_c^{RP},\nu_{-c}^{RP}\): all passive RP constraints are
invariant under \(c\mapsto -c\), while \(m,t,\lambda_+,\lambda_-\) change
sign.  A floor witness must therefore add a non-passive sign orientation,
and no such RP orientation is printed.  `square`

## 5. Reflection Positivity Versus Markov Transfer

One tempting move is to treat reflection positivity as if it produced a
contractive Markov transfer operator.  That is not allowed here.

### Proposition 5.1: RP Does Not Supply A Hidden Markov Semigroup

The finite RP moment constraint

$$
\mathbf E[(\Theta F)F]\ge0
$$

does not by itself imply a Markov factorization, a Dobrushin row, or a
spectral contraction for the adaptive law.

Proof.

Reflection positivity is a positivity condition on a bilinear form.  A
Markov factorization would require a declared intermediate record and a
stochastic kernel decomposition of the whole operation.  Barandes alignment
forbids inserting that division unless it is part of the stochastic record
law.  The current corpus explicitly treats Dobrushin rows, spectral
contraction, and bridge damping as separate same-law theorems.  Thus RP may
feed a finite moment certificate, but it cannot be promoted into a hidden
transfer dynamics.  `square`

### Corollary 5.2: OS-Style Reconstruction Is Not A Shortcut

An Osterwalder-Schrader style representation can be useful only after the
needed finite RP moments are already controlled.  It cannot replace the
missing same-law value theorem.

Proof.

OS reconstruction builds a Hilbert representation from reflection-positive
moments.  It does not upper-bound the particular live moment
\(\mathbf E[(\alpha m+\zeta t)^2]\), orient its sign, or populate residual
conditional weights unless those facts are present in the moment data.  In
this program representation objects are calculational, not additional
ontological input.  `square`

## 6. Complete Current-Corpus Verdict

### Theorem 6.1: Reflection-Positive Bootstrap Is Exact But Non-Closing

At fixed finite cutoff, the reflection-positive moment bootstrap is a sound,
Barandes-aligned finite SDP/SOS framework.  However, using only the current
corpus as input, it proves neither:

$$
\mathrm{P34\text{-}RP\text{-}RAYCUT}(B_{rem})
$$

in a closing range, nor

$$
\mathrm{P34\text{-}RP\text{-}FLOOR}(M_*).
$$

Proof.

Soundness and Barandes alignment are Theorem 2.3 and Corollary 2.4.
Non-closing upper bounds follow from Theorem 3.4.  Non-closing floors follow
from Corollary 3.5.  Higher-degree passive RP moments are covered by
Corollary 3.6.  Routes A through E are valid non-passive routes, but
Propositions 4.2, 4.4, 4.6, 4.7, and 4.8 show that none is sourced by the
current corpus.  `square`

### Corollary 6.2: Exact Remaining RP Theorems

The reflection-positive route can move adaptive Branch A only by proving at
least one of:

$$
\mathrm{P34\text{-}RP\text{-}UPMOM},
$$

or

$$
\mathrm{P34\text{-}RP\text{-}ODD},
$$

or

$$
\mathrm{P34\text{-}RP\text{-}SCHUR},
$$

or

$$
\mathrm{P34\text{-}RP\text{-}STRUCTCOUPLE},
$$

or

$$
\mathrm{P34\text{-}RP\text{-}FLOOR\text{-}WIT}.
$$

Each is a genuine same-law quantitative theorem about the actual
residual/signed block.  None is a consequence of passive RP positivity.

### Corollary 6.3: Nothing More To Extract From Passive RP/SOS

Within adaptive Branch A and the current corpus, there is no further
passive reflection-positive moment refinement to try.

Proof.

Any finite passive refinement adds finitely many words to
\({\mathcal A}_{RP}^{N,j,L}\), finitely many ordinary moment matrices, and
finitely many RP moment matrices.  Lemma 3.3 extends the deterministic
scalar-ray law to all such words, and Corollary 3.6 proves all such moment
matrices are positive.  Therefore no finite passive RP/SOS refinement can
exclude the scalar ray, orient it, or lower its envelope.  `square`

## 7. What Should Be Done After Paper 34

Paper 34 settles the reflection-positive bootstrap route at current-corpus
level.  The next rational moves are:

1. return to a genuinely new value theorem: residual score energy, residual
   Hessian, or conditional normalizer variance;
2. try a non-passive reflection theorem, especially `P34-RP-UPMOM` or
   `P34-RP-ODD`, but only if a concrete actual-law mechanism is found;
3. search for a sign-coherent floor using the finite RP/SOS dual cone;
4. exit adaptive Branch A and investigate Branch B/C if no same-law value or
   floor theorem appears.

The important negative lesson is also positive guidance:

$$
\text{reflection positivity is useful only when it supplies a new value
inequality or orientation.}
$$

It cannot be a substitute for the missing actual-law quantitative
information.
