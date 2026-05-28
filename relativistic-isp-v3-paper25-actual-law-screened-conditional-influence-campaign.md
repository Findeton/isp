# Relativistic ISP V3 Paper 25: Actual-Law Screened Conditional Influence Campaign For Adaptive Branch A

Author: Felix Robles Elvira

Status: completed Branch-A actual-law source and truth-status audit.  Paper
25 is not a summary and not another certificate over the closed Paper-23 body
\({\mathcal M}_{56}\).  It executes the five Branch-A routes exported after
Paper 24:

1. direct cofinal actual-law Dobrushin rows;
2. same-law screened conditional shells;
3. same-law Peter-Weyl step contraction;
4. Peter-Weyl tail/projection control;
5. actual-law bridge damping.

The result is sharp but not a confinement proof.  Each route has an exact
positive theorem that would close adaptive Branch A if its same-law source
were supplied.  The current V3 corpus supplies none of the five sources, and
also does not supply a lower-floor theorem falsifying adaptive Branch A.
Thus Paper 25 is finished as a five-route source audit and a five-route
truth-status pass: the missing object is not bookkeeping, not a closed-body
certificate, and not an off-law heat-kernel analogy.  It is new actual-law
scalar information.  Without that information, the current corpus neither
proves nor falsifies the actual truth of any of the five Branch-A options.

## 0. Barandes-Aligned Boundary

The primitive object in this paper is the same whole-process finite scalar
record law used in Papers 20--24.  No argument below introduces:

1. a continuum Yang-Mills measure with confinement already built in;
2. a Wilson-loop area law;
3. a mass gap;
4. a gauge-fixed Markov subprocess;
5. an off-record heat-kernel replacement law;
6. an ontic flux-tube or sheet variable.

All conditionals, oscillations, Dobrushin rows, Peter-Weyl expansions, and
screening constants are scalar functions of the pushed-forward adaptive
`SEL2` record law.  Group and representation language is bookkeeping for
finite scalar functions, not a change of ontology.

## 1. Import Contract From Papers 23 And 24

### Definition 1.1: Actual Adaptive Law

Let

```math
\nu_{N,j}^{act}
```

denote the adaptive high-\(\alpha\), large-\(N\), pushed-forward `SEL2` scalar
law selected in Paper 23.  It lives on the finite scalar record space used to
evaluate the RPF source rows.  The cofinal index \((N,j)\) is always taken on
the same selector as Paper 23 unless explicitly stated otherwise.

### Import 1.2: Paper-23 Dobrushin Closure

Paper 23 Theorem 33.3 proves:

```math
\mathrm{P23\text{-}RPF\text{-}DOB\text{-}ROW}(q,a),\quad q<1,\ a>0
\quad\Longrightarrow\quad
\mathrm{P23\text{-}RPF\text{-}TRANS0}.
```

Thus any actual-law weighted Dobrushin row below one closes adaptive Branch A
on the exact-CE branch.

### Import 1.3: Paper-23 Screened Influence Closure

Paper 23 Theorem 34.5 and Corollary 34.6 prove that screened conditional
influence closes the Dobrushin row if the optimized margin

```math
\mu-h_{sh}>
\log\left(1+{AC_{sh}\over4}\right)
```

holds.

### Import 1.4: Paper-24 Export

Paper 24 Corollary 12.2 proves that the next positive proof cannot be another
universal full-object certificate over the closed body
\({\mathcal M}_{56}\).  It must add new actual-law scalar information, source
a Peter-Weyl tail, prove bridge damping, prove screened conditional
influence or a direct Dobrushin row, or return to Branch B/C.

This paper executes that option and then, in Sections 10--14, exhausts the
other four Branch-A options that remain after Paper 24.

## 2. Actual-Law Conditional Row

### Definition 2.1: One-Site Conditional Kernels

For a site or finite scalar block \(x\), write

```math
K_x^{N,j}(\cdot\mid\eta)
```

for the conditional law of the \(x\)-record under \(\nu_{N,j}^{act}\), given
the outside configuration \(\eta\).  This is a regular conditional
probability on a finite scalar space; no continuum disintegration is being
used.

### Definition 2.2: Conditional Oscillation

For \(x\ne y\), define the sharp conditional influence

```math
J_{xy}^{N,j}
:=
\sup_{\eta,\eta':\,\eta_{z}=\eta'_{z}\ \forall z\ne y}
\left\|K_x^{N,j}(\cdot\mid\eta)
-K_x^{N,j}(\cdot\mid\eta')\right\|_{TV}.
```

Equivalently, if \(\Delta_{xy}^{N,j}\) denotes the conditional
log-likelihood oscillation used in Paper 23 Section 34, then

```math
J_{xy}^{N,j}
\le
\tanh(\Delta_{xy}^{N,j}/4)
\le
\Delta_{xy}^{N,j}/4.
```

The last inequality is exactly the Paper-23 Lemma 34.3 estimate.

### Definition 2.3: Weighted Sharp Row

For \(a>0\), let

```math
\mathfrak D_{sharp}^{N,j}(a)
:=
\sup_x\sum_{y\ne x} e^{a d_{RPF}(x,y)}J_{xy}^{N,j}.
```

The cofinal sharp row is

```math
\mathfrak D_{sharp}^{cof}(a)
:=
\limsup_{(N,j)}
\mathfrak D_{sharp}^{N,j}(a)
```

along the adaptive `SEL2` cofinal selector.

### Definition 2.4: Actual Dobrushin Source

`P25-RPF-ACTUAL-DOB(q,a)` is the assertion

```math
\mathfrak D_{sharp}^{cof}(a)\le q<1.
```

It is the actual-law form of `P23-RPF-DOB-ROW(q,a)`.

## 3. Direct Dobrushin Closure

### Theorem 3.1: Actual Dobrushin Row Closes Adaptive Branch A

If `P25-RPF-ACTUAL-DOB(q,a)` holds for some \(q<1\) and \(a>0\), then

```math
\mathrm{P23\text{-}RPF\text{-}TRANS0}
```

holds.  Consequently adaptive Branch A closes on the exact-CE branch.

Proof.

By Definition 2.4, `P25-RPF-ACTUAL-DOB(q,a)` is precisely the same-law
instance of `P23-RPF-DOB-ROW(q,a)` for the actual adaptive pushed-forward
scalar law.  Paper 23 Theorem 33.3 gives `P23-RPF-TRANS0`. `square`

### Corollary 3.2: What A Negative Direct Row Means

If

```math
\inf_{a>0}\mathfrak D_{sharp}^{cof}(a)\ge1,
```

then the direct Dobrushin route fails.  This does not by itself falsify
adaptive Branch A.

Proof.

This is Paper 23 Theorem 33.5 in actual-law notation.  Dobrushin is a
sufficient row-contraction criterion.  Failure of this criterion does not
exclude a different same-law cluster mechanism.  Branch failure would require
an additional same-record lower floor forcing

```math
\overline\Lambda_{13}^{RPF}\ge M_*.
```

`square`

## 4. Screened Conditional Influence

### Definition 4.1: Actual Screen Source

`P25-RPF-ACTUAL-SCREEN(A,mu,h_sh,C_sh)` is the assertion that, cofinally in
\((N,j)\),

```math
\sup_x
\sum_{y:d_{RPF}(x,y)=r}
\Delta_{xy}^{N,j}
\le
A C_{sh}e^{-(\mu-h_{sh})r}
```

for every \(r\ge1\), with constants independent of \(N,j\).

This is weaker than literal atomwise decay.  It controls the already-averaged
conditional response of the actual law.

### Theorem 4.2: Screened Influence Gives A Weighted Row

Assume `P25-RPF-ACTUAL-SCREEN(A,mu,h_sh,C_sh)`.  If there exists \(a>0\) with

```math
\delta:=\mu-h_{sh}-a>0
```

and

```math
Q_{scr}(a)
:=
{A C_{sh}\over4}
{e^{-\delta}\over1-e^{-\delta}}
<1,
```

then `P25-RPF-ACTUAL-DOB(Q_scr(a),a)` holds.

Proof.

Using \(J_{xy}^{N,j}\le\Delta_{xy}^{N,j}/4\),

```math
\mathfrak D_{sharp}^{N,j}(a)
\le
{1\over4}
\sup_x\sum_{r\ge1}
e^{ar}
\sum_{y:d(x,y)=r}\Delta_{xy}^{N,j}.
```

Insert the screened shell bound and sum the geometric series:

```math
\mathfrak D_{sharp}^{cof}(a)
\le
{A C_{sh}\over4}
\sum_{r\ge1}e^{-(\mu-h_{sh}-a)r}
=Q_{scr}(a).
```

`square`

### Corollary 4.3: Optimized Screened Closure Test

If `P25-RPF-ACTUAL-SCREEN(A,mu,h_sh,C_sh)` holds and

```math
\mu-h_{sh}>
\log\left(1+{AC_{sh}\over4}\right),
```

then adaptive Branch A closes on the exact-CE branch.

Proof.

Let \(a\downarrow0\) in Theorem 4.2.  This is Paper 23 Corollary 34.6, then
Theorem 3.1. `square`

## 5. Peter-Weyl Step Route

### Definition 5.1: Actual Peter-Weyl Step Source

`P25-RPF-ACTUAL-HKPW-STEP(theta,B_step,h_path,C_path)` is the same-law
assertion that every conditional response
\(L_{x\leftarrow y}^{N,j}\) admits a finite Peter-Weyl path expansion on the
actual adaptive scalar records, with:

1. nontrivial modes mapped to nontrivial modes;
2. nontrivial-mode oscillation contracted by at most \(\theta<1\) per step;
3. endpoint and norm-conversion cost at most \(B_{step}\);
4. admissible path count bounded by \(C_{path}e^{h_{path}r}\).

Equivalently,

```math
\Delta_{xy}^{N,j}
\le
B_{step}
\sum_{\gamma:x\leadsto y}\theta^{|\gamma|}
```

on the actual pushed-forward scalar law.

### Theorem 5.2: Step Source Closes Under The Sharp Margin

If `P25-RPF-ACTUAL-HKPW-STEP(theta,B_step,h_path,C_path)` holds and

```math
-\log\theta-h_{path}
>
\log\left(1+{B_{step}C_{path}\over4}\right),
```

then adaptive Branch A closes on the exact-CE branch.

Proof.

Paper 23 Theorem 35.4 turns the step source into
`P25-RPF-ACTUAL-SCREEN` with

```math
A=B_{step},\qquad C_{sh}=C_{path},
\qquad \mu-h_{sh}=-\log\theta-h_{path}.
```

The displayed inequality is exactly the optimized screened closure condition
of Corollary 4.3. `square`

### Corollary 5.3: Heat-Kernel Parametrization

If the actual finite Peter-Weyl transfer has

```math
\theta
=
B_0e^{-t_*C_{gap}/2}+\kappa_{res},
```

then it is enough that

```math
-\log\left(B_0e^{-t_*C_{gap}/2}+\kappa_{res}\right)
-h_{path}
>
\log\left(1+{B_{step}C_{path}\over4}\right).
```

This is not an off-law heat-kernel assumption.  It is a finite scalar
statement about the actual adaptive conditionals.

## 6. Current-Source Audit

The positive chain is now exact.  We must decide whether the current V3
corpus proves one of its sources.

### Lemma 6.1: Paper-16 Heat-Kernel Rows Do Not Transfer Automatically

Paper 16 supplies heat-kernel analytic row constants on its declared
whole-process law.  It does not by itself prove
`P25-RPF-ACTUAL-HKPW-STEP`, `P25-RPF-ACTUAL-SCREEN`, or
`P25-RPF-ACTUAL-DOB` for \(\nu_{N,j}^{act}\).

Proof.

The needed conditionals are those of the adaptive high-\(\alpha\), large-\(N\)
`SEL2` pushed-forward law.  A row estimate on a different heat-kernel
record-law tower has the correct analytic shape, but Papers 20--24 repeatedly
require same-law transfer before such constants may be spent.  No previous
paper prints the finite conditional transfer identity from the Paper-16
analytic row to \(\nu_{N,j}^{act}\). `square`

### Lemma 6.2: The CE Block Factor Is Not A Free Screening Source

The exact CE/character-expansion block law does not by itself imply
`P25-RPF-ACTUAL-SCREEN`.

Proof.

CE identifies how selected block coefficients are evaluated under the same
scalar law.  It does not bound the conditional variation of one residual RPF
record when a distant record is changed.  Spending CE as screening would
double-count an exact-entry identity as a propagation estimate. `square`

### Lemma 6.3: Projection/Tail Splits Return To The Tail Gate

A finite Peter-Weyl projection can prove a finite-dimensional row estimate
only after the complement is bounded.  Without a same-law tail theorem
(`PWBAND`, `PWDECAY`, `KTAIL`, or an equivalent cofinal table), the projection
route does not prove `P25-RPF-ACTUAL-DOB`.

Proof.

The Dobrushin row uses the full conditional kernel.  A finite projection
controls only \(\Pi_{\le L}K_x\Pi_{\le L}\).  The omitted complement can carry
conditional variation unless the actual law supplies a tail bound.  Thus the
projection route is not independent of the tail source exported by Paper 24.
`square`

### Lemma 6.4: Bridge Damping Is A Different Missing Source

A bridge-damping theorem on the actual law may close adaptive Branch A, but
it is not already contained in screened conditional influence.

Proof.

Bridge damping controls propagation through minimal-edge bridge structures or
the full signed Hamiltonian.  Screened conditional influence controls
conditional variation rows.  Either can imply a usable RPF source, but the
current corpus does not prove a formal implication from the closed Paper-23
data alone. `square`

### Lemma 6.5: Paper-24 Certificate Witnesses Do Not Decide Screening

The Paper-24 witness family proves that \({\mathcal M}_{56}\) is too large for
a universal closing certificate.  It does not prove that the actual adaptive
law has \(\mathfrak D_{sharp}^{cof}(a)\ge1\).

Proof.

The witness family lives inside the closed scalar body and is used to refute
universal certificates over that body.  The actual pushed-forward law is one
element of the body.  A body witness against a universal certificate is not a
same-law lower bound on the actual conditional row. `square`

## 7. Current-Corpus Non-Derivability

### Theorem 7.1: Current Corpus Does Not Prove The Actual Dobrushin Row

From the scalar source package closed in Papers 20--24, one cannot infer that
there exist \(a>0\) and \(q<1\) with

```math
\mathfrak D_{sharp}^{cof}(a)\le q.
```

Proof.

Paper 23 Lemma 33.6 prints the decisive mechanism: the closed non-RPF
ledgers allow residual completions that preserve all already spent scalar
constraints while changing the sharp conditional row.  Some completions make
the row small; others make it exceed any proposed strict \(q<1\).  Paper 24
then proves that the closed full-object body is too large for a universal
certificate.  Therefore the current closed data do not determine the actual
Dobrushin row.  Only a new same-law theorem about
\(\nu_{N,j}^{act}\), or a direct cofinal row computation, can prove it.
`square`

### Theorem 7.2: Current Corpus Does Not Prove Screened Influence

The current V3 corpus does not prove
`P25-RPF-ACTUAL-SCREEN(A,mu,h_sh,C_sh)` with the optimized closing margin.

Proof.

Any proof using only the closed scalar information of Papers 20--24 would
hold for every residual completion satisfying that closed information.  Paper
23 Lemma 33.6 gives completions preserving the closed non-RPF ledgers while
violating any proposed strict screened row margin, and Paper 24 Theorem 12.1
shows that the closed body remains too large for a universal closing
certificate.  Hence the current corpus does not prove the actual screened
source. `square`

### Theorem 7.3: Current Corpus Does Not Falsify The Actual Dobrushin Route

The current V3 corpus also does not prove

```math
\inf_{a>0}\mathfrak D_{sharp}^{cof}(a)\ge1.
```

Nor does it prove the stronger same-record lower floor

```math
\overline\Lambda_{13}^{RPF}\ge M_*.
```

Proof.

Again by Paper 23 Lemma 33.6, admissible residual completions can make the
sharp row small while preserving the closed non-RPF ledgers.  Therefore the
closed data cannot imply the lower bound \(\inf_a\mathfrak D\ge1\).  The
predebit lower floor would be stronger still, and Paper 24 did not print it;
it printed only a witness against universal certificates over the old body.
`square`

## 8. Sharp Replacement Targets

The first-stage reduction leaves the following Branch-A proof-producing
same-law targets.  They are the five non-Branch-B/C possibilities in
Corollary 9.2 below.

### Target 8.1: Direct Cofinal Row Table

Print finite row values for the actual adaptive conditionals:

```math
\mathfrak D_{sharp}^{N,j}(a)
=
\sup_x\sum_{y\ne x}e^{a d(x,y)}J_{xy}^{N,j},
```

then prove a cofinal bound below one for some \(a>0\).  This is the most
literal route.

### Target 8.2: Screened Shell Theorem

Prove

```math
\sup_x
\sum_{d(x,y)=r}\Delta_{xy}^{N,j}
\le
A C_{sh}e^{-(\mu-h_{sh})r}
```

with

```math
\mu-h_{sh}>
\log\left(1+{AC_{sh}\over4}\right).
```

This route may use cancellation, conditional averaging, activity suppression,
or Peter-Weyl damping, but it must be on the actual law.

### Target 8.3: Peter-Weyl Step Contraction

Prove `P25-RPF-ACTUAL-HKPW-STEP(theta,B_step,h_path,C_path)` with

```math
-\log\theta-h_{path}
>
\log\left(1+{B_{step}C_{path}\over4}\right).
```

This is the cleanest finite representation-theoretic version of screened
conditional influence.

### Target 8.4: Peter-Weyl Tail/Projection Source

Prove one of:

```math
\mathrm{P25\text{-}RPF\text{-}ACTUAL\text{-}PWBAND}(L_0),
\qquad
\mathrm{P25\text{-}RPF\text{-}ACTUAL\text{-}PWDECAY}(A,t),
```

or print an explicit cofinal tail table

```math
\kappa_{PW}^{N,j}(L(N,j))\to0.
```

This makes the finite projection route honest.  Without it, a projected
Dobrushin or bridge table controls only the truncated object.

### Target 8.5: Actual-Law Bridge Damping

Prove a cofinal bridge damping source on the actual law:

```math
\mathrm{P25\text{-}RPF\text{-}ACTUAL\text{-}BRIDGEDAMP}(D)
```

with the corresponding tail budget small enough for the Paper-23 bridge gate.
This route controls true bridge amplitudes directly rather than conditional
rows.

### Target 8.6: Negative Lower Floor

If the route actually fails, print the actual-law lower floor

```math
\inf_{a>0}\mathfrak D_{sharp}^{cof}(a)\ge1
```

and, to falsify adaptive Branch A rather than only this sufficient route,
also print

```math
\overline\Lambda_{13}^{RPF}\ge M_*.
```

## 9. First-Stage Completion Verdict

### Theorem 9.1: Paper-25 First-Stage Completion Theorem

The first stage of Paper 25 settles the actual-law screened conditional
influence campaign at the level of the current V3 corpus:

1. a direct actual-law Dobrushin row below one closes adaptive Branch A;
2. a screened conditional influence theorem with the optimized margin closes
   adaptive Branch A;
3. a same-law Peter-Weyl step contraction with the sharp path-entropy margin
   closes adaptive Branch A;
4. the current Papers 20--24 do not prove any of these sources;
5. the current Papers 20--24 also do not prove the lower-floor theorem needed
   to falsify this route or adaptive Branch A.

Proof.

Items 1--3 are Theorems 3.1, 4.2--4.3, and 5.2.  Items 4--5 are Theorems
7.1--7.3. `square`

### Corollary 9.2: Export To The Five-Route Branch-A Audit

The remaining Branch-A positive proof must be one of the following:

1. a direct cofinal actual-law Dobrushin row table;
2. a same-law screened shell theorem;
3. a same-law Peter-Weyl step contraction beating path entropy;
4. a Peter-Weyl tail theorem that makes the finite projection route honest;
5. an actual-law bridge-damping theorem;
6. a return to Paper-22 Branch B or Branch C.

The rest of Paper 25 investigates the first five possibilities.  The sixth
is not Branch A and is therefore left as the parked Paper-22 Branch-B/C
alternative.

## 10. Route I: Direct Cofinal Actual-Law Dobrushin Row Table

The direct row table is the most literal route.  It asks for no geometric
envelope and no representation-theoretic explanation.  It only asks whether
the actual cofinal conditional influence matrix has a weighted row norm below
one.

### Definition 10.1: Finite Row Table

For fixed \((N,j)\) and \(a>0\), define

```math
{\mathcal R}_{DOB}^{N,j}(a)
:=
\left\{
\left(x,y,d_{RPF}(x,y),J_{xy}^{N,j},
e^{a d_{RPF}(x,y)}J_{xy}^{N,j}\right):
x\ne y
\right\}.
```

The row value is

```math
D_{DOB}^{N,j}(a)
:=
\sup_x\sum_{y\ne x}e^{a d_{RPF}(x,y)}J_{xy}^{N,j}.
```

This is the same number as \(\mathfrak D_{sharp}^{N,j}(a)\).

### Lemma 10.2: Fixed-Row Decidability

For every fixed \((N,j)\) and rational \(a>0\), the table
\({\mathcal R}_{DOB}^{N,j}(a)\) is a finite same-law scalar object.

Proof.

The adaptive row is finite.  Each conditional kernel
\(K_x^{N,j}(\cdot\mid\eta)\) is a finite conditional probability under
\(\nu_{N,j}^{act}\).  Total variation distances, graph distances, and finite
weighted sums are therefore finite scalar functions of that same law.
`square`

### Theorem 10.3: Direct Row Table Positive Closure

If there exist \(a>0\) and \(q<1\) such that cofinally

```math
D_{DOB}^{N,j}(a)\le q,
```

then adaptive Branch A closes on the exact-CE branch.

Proof.

The displayed cofinal row bound is `P25-RPF-ACTUAL-DOB(q,a)`.  Apply
Theorem 3.1. `square`

### Proposition 10.4: Current-Corpus Direct Row Verdict

The current corpus does not print a cofinal direct row table with
\(D_{DOB}^{N,j}(a)\le q<1\), and it does not print a cofinal lower table with
\(\inf_aD_{DOB}^{cof}(a)\ge1\).

Proof.

Fixed-row decidability is Lemma 10.2.  Cofinal contraction is stronger.  Paper
23 Lemma 33.6 gives residual completions preserving the closed non-RPF
ledgers while changing the sharp conditional row.  Therefore the closed
Papers 20--24 neither imply a strict row below one nor a strict lower floor
above or at one.  A real proof must compute or bound the actual
\(\nu_{N,j}^{act}\) conditionals cofinally. `square`

### Verdict 10.5: Route I Exhausted Relative To The Current Corpus

The direct row route is fully reduced to an explicit same-law numerical
problem:

```math
\boxed{
\exists a>0:\quad
\limsup_{(N,j)}D_{DOB}^{N,j}(a)<1.
}
```

The current corpus proves fixed-row legitimacy but not the cofinal inequality.
It also does not falsify it.

## 11. Route II: Same-Law Screened Shell Theorem

Screening is the structured version of the direct row route.  Instead of
printing every \(J_{xy}\), it tries to show that the shell sums decay faster
than shell entropy.

### Definition 11.1: Actual Shell Functional

For \(r\ge1\), define

```math
S_r^{N,j}
:=
\sup_x
\sum_{y:d_{RPF}(x,y)=r}
\Delta_{xy}^{N,j}.
```

The screen source is exactly a bound

```math
S_r^{N,j}
\le
A C_{sh}e^{-(\mu-h_{sh})r}
```

cofinally and uniformly in \(r\).

### Theorem 11.2: Screened Shell Positive Closure

If the bound of Definition 11.1 holds and

```math
\mu-h_{sh}>
\log\left(1+{AC_{sh}\over4}\right),
```

then adaptive Branch A closes.

Proof.

This is Corollary 4.3. `square`

### Lemma 11.3: Counting Is Not Screening

Finite shell entropy, finite canonical labels, and finite row decidability do
not imply the screened shell theorem.

Proof.

Those facts bound the number of terms in a shell or make them enumerable.
They do not bound the conditional oscillation \(\Delta_{xy}^{N,j}\) of any
surviving term.  The residual-tail completion mechanism of Paper 23 can keep
the same finite labels and closed non-RPF ledgers while assigning non-small
conditional influence to a surviving RPF mixed component. `square`

### Lemma 11.4: CE And Heat-Kernel Entries Are Not Screening

The central-entry heat-kernel factor and exact `BC/CE` identities do not
prove the screened shell theorem for the RPF residual.

Proof.

The RPF residual is defined after the exact central-entry division.  A
damping estimate for the divided central factor has already been spent in the
exact-entry ledger.  To spend it again as residual screening would
double-charge.  What is missing is a same-law estimate on the conditional
variation of the residual itself. `square`

### Proposition 11.5: Current-Corpus Screened Shell Verdict

The current corpus does not prove a screened shell source with the closing
margin, and it does not prove a matching lower-floor theorem.

Proof.

Lemmas 11.3 and 11.4 rule out the available structural sources.  Paper 23
Lemma 33.6 gives residual completions with small or large shell influence
while preserving the closed source package.  Hence the closed data cannot
decide the screened shell inequality. `square`

### Verdict 11.6: Route II Exhausted Relative To The Current Corpus

The route is reduced to the primitive same-law estimate

```math
\boxed{
S_r^{N,j}
\le
A C_{sh}e^{-(\mu-h_{sh})r},
\qquad
\mu-h_{sh}>
\log(1+AC_{sh}/4).
}
```

No existing finite-counting, CE, or imported heat-kernel theorem proves it.

## 12. Route III: Same-Law Peter-Weyl Step Contraction

The Peter-Weyl step route tries to explain screening by finite
representation damping along conditional-response paths.

### Definition 12.1: Edge Transfer Test

For a declared finite Peter-Weyl cutoff \(L\), let

```math
\Pi_{\le L}T_{e,\zeta}^{N,j}\Pi_{\le L}
```

be the centered nontrivial-mode edge transfer matrix of the actual adaptive
conditional response on edge \(e\) and environment label \(\zeta\).  Define

```math
\Theta_L^{N,j}
:=
\sup_{e,\zeta}
\left\|\Pi_{\le L}T_{e,\zeta}^{N,j}\Pi_{\le L}\right\|_{osc\to osc},
```

and let \(\Kappa_L^{N,j}\) denote the omitted nontrivial-mode tail in the same
conditional-response norm.

### Definition 12.2: Step Pass Source

`P25-RPF-ACTUAL-STEP-PASS(theta,B,h,C)` asserts that there is a cofinal cutoff
schedule \(L(N,j)\) such that

```math
\limsup_{(N,j)}
\left(\Theta_{L(N,j)}^{N,j}+\Kappa_{L(N,j)}^{N,j}\right)
\le\theta<1,
```

and the centered response admits a same-law path expansion with endpoint cost
\(B\) and path count \(Ce^{hr}\).

### Theorem 12.3: Step Pass Positive Closure

If `P25-RPF-ACTUAL-STEP-PASS(theta,B,h,C)` holds and

```math
-\log\theta-h>
\log\left(1+{BC\over4}\right),
```

then adaptive Branch A closes.

Proof.

The pass source is exactly `P25-RPF-ACTUAL-HKPW-STEP(theta,B,h,C)`.  Apply
Theorem 5.2. `square`

### Proposition 12.4: Current-Corpus Step Verdict

The current corpus proves fixed-row matrix legitimacy but does not prove
`P25-RPF-ACTUAL-STEP-PASS` with the closing margin.

Proof.

Paper 23 Lemma 35.6 and Theorem 35.8 already isolate the missing source:
finite Peter-Weyl batteries, heat-kernel tail estimates on declared clean
rows, and rowwise matrix construction do not print a cofinal centered
spectral gap for the actual adaptive residual conditionals.  Paper 23 Section
36 further shows that fixed-row matrices are legitimate same-law objects, but
that cofinal `EDGE-SPEC`, `EDGE-PATH`, and the corresponding tail control are
not consequences of compactness or finite truncation. `square`

### Verdict 12.5: Route III Exhausted Relative To The Current Corpus

The route is reduced to a concrete finite-matrix campaign:

```math
\boxed{
\Theta_L^{N,j}+\Kappa_L^{N,j}
\le\theta
\quad\text{cofinally, with}\quad
-\log\theta-h>\log(1+BC/4).
}
```

The current papers license the matrices.  They do not supply the cofinal
spectral contraction, path expansion, or tail estimate.

## 13. Route IV: Peter-Weyl Tail/Projection Control

Projection is useful only if the omitted Peter-Weyl complement is controlled
on the same actual law.

### Definition 13.1: Actual Conditional Tail

For a cutoff \(L\), define

```math
\kappa_{PW}^{N,j}(L)
:=
\sup_{x,y}
\left\|
(I-\Pi_{\le L}^{xy})C_0^{m,N,j}(x,y)
\right\|_{edge},
```

using the same minimal-edge residual Hamiltonian and edge norm as Paper 23
Sections 48 and 55.

### Definition 13.2: Actual Tail Sources

`P25-RPF-ACTUAL-PWBAND(L0)` asserts cofinal exact finite-band support:

```math
(I-\Pi_{\le L_0}^{xy})C_0^{m,N,j}=0.
```

`P25-RPF-ACTUAL-PWDECAY(A,t)` asserts cofinal uniform decay:

```math
\kappa_{PW}^{N,j}(L)
\le
A\exp(-t\lambda_{L+1}^{xy})
```

for all sufficiently large \(L\).  A direct tail table is any cofinal
schedule \(L(N,j)\) with \(\kappa_{PW}^{N,j}(L(N,j))\to0\).

### Theorem 13.3: Tail Source Makes Projection Honest

Any of the three sources in Definition 13.2 supplies the tail side needed by
the projected signed, projected bridge, or projected row routes.  In
particular, if the projected finite table satisfies its Paper-23 scalar
margin and the tail budget is small enough for that margin, then
`P23-RPF-TRANS0` holds.

Proof.

This is Paper 23 Lemmas 55.3 and 55.6, plus the projected closure theorems in
Sections 41--54.  Exact finite-band gives zero tail.  Uniform decay or a
direct tail table gives a cofinal cutoff with arbitrarily small tail.  The
remaining finite projected table is then an honest same-law finite object
with the complement paid. `square`

### Proposition 13.4: Current-Corpus Tail Verdict

The current corpus does not prove `P25-RPF-ACTUAL-PWBAND(L0)`,
`P25-RPF-ACTUAL-PWDECAY(A,t)`, or a direct cofinal tail table for
\(C_0^{m,N,j}\).

Proof.

Paper 23 Proposition 55.4 proves that finite scalar records do not imply
finite Peter-Weyl band support, because conditioning, central-entry division,
logarithms, normalization, and anchoring do not preserve finite spectral
support.  Paper 23 Propositions 55.8 and 55.9 then audit the existing sources:
heat-kernel/Casimir estimates apply to declared heat-kernel or clean rows,
not to the actual adaptive minimal-edge residual Hamiltonian, and bounded
collar/degree-tail tables are not Peter-Weyl coefficient decay.  No direct
cofinal tail table is printed. `square`

### Verdict 13.5: Route IV Exhausted Relative To The Current Corpus

The tail route is reduced to exactly:

```math
\boxed{
\mathrm{PWBAND}(L_0)
\quad\text{or}\quad
\mathrm{PWDECAY}(A,t)
\quad\text{or}\quad
\kappa_{PW}^{N,j}(L(N,j))\to0
}
```

for the actual adaptive residual Hamiltonian.  The current corpus supplies
none of these.

## 14. Route V: Actual-Law Bridge Damping

Bridge damping controls true bridge amplitudes directly.  It is different
from screening: it bounds the minimal-edge bridge Hamiltonian rather than the
full conditional influence row.

### Definition 14.1: Actual Bridge Damping Source

Let \({\mathcal U}_{br,0}^{N,j}(x,y)\) be the true-bridge table of Paper 23
Section 49, and let

```math
d_A^{br}(x,y)=\delta_\square(A;x,y)
```

be the same-law bridge amplitude.  `P25-RPF-ACTUAL-BRIDGEDAMP(D)` asserts
that there is a finite type map \(\tau\) and same-law bridge statistic
\(\ell(A)\) such that

```math
d_A^{br}(x,y)
\le
a_{\tau(A)}e^{-m_{\tau(A)}\ell(A)}
```

and

```math
\operatorname*{ess\,sup}_{x,y}
\sum_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)}
a_{\tau(A)}e^{-m_{\tau(A)}\ell(A)}
\le D
```

cofinally.

### Theorem 14.2: Bridge Damping Positive Closure

Assume `P25-RPF-ACTUAL-BRIDGEDAMP(D)` and a same-law tail source
`P25-RPF-ACTUAL-KTAIL(kappa)`.  If

```math
\kappa<B_*^{edge},
\qquad
D<D_{\mathrm{crit}}(\kappa),
```

then adaptive Branch A closes.

Proof.

This is Paper 23 Proposition 50.5 in Paper-25 notation.  Bridge damping
implies the bridge-amplitude source, hence the minimal bridge bound, and the
tail-paid scalar gate closes `P23-RPF-TRANS0`. `square`

### Lemma 14.3: Counting Bridges Is Not Damping

Finite bridge-table cardinality, finite canonical labels, and rowwise
decidability do not imply `P25-RPF-ACTUAL-BRIDGEDAMP(D)` in the closing
range.

Proof.

These data count or label true bridges.  They do not bound
\(\delta_\square(A;x,y)\).  Paper 23 Lemma 50.6 shows that residual-tail
completions can preserve the closed non-RPF ledgers and the same finite row
labels while assigning \(O(1)\) mixed four-point amplitude to a surviving
bridge row. `square`

### Proposition 14.4: Current-Corpus Bridge Verdict

The current corpus proves the finite bridge-amplitude table row by row, but
does not prove actual bridge damping in the closing range and does not supply
the required tail source.

Proof.

Paper 23 Definition 50.1 and Lemma 50.3 make the bridge-amplitude table a
finite same-law row object.  Paper 23 Proposition 50.7 proves that the
current corpus does not bound those amplitudes by a useful damping theorem:
there is no same-law conditional spectral gap, literal bridge-decay theorem,
or signed bridge cancellation theorem for the actual adaptive residual law.
Section 13 of this paper also shows that the required `KTAIL` input is not
currently sourced. `square`

### Verdict 14.5: Route V Exhausted Relative To The Current Corpus

The bridge route is reduced to the two-source package

```math
\boxed{
\mathrm{P25\text{-}RPF\text{-}ACTUAL\text{-}BRIDGEDAMP}(D)
+
\mathrm{P25\text{-}RPF\text{-}ACTUAL\text{-}KTAIL}(\kappa),
\qquad
D<D_{\mathrm{crit}}(\kappa).
}
```

The bridge rows are finite and legitimate.  Their cofinal damping and the
tail budget are not supplied by the current papers.

## 15. Final Five-Route Exhaustion Theorem

### Theorem 15.1: Branch-A Source Audit Completion

Relative to the current V3 corpus, the five Branch-A routes of Corollary 9.2
are fully investigated:

1. direct Dobrushin row tables are finite rowwise but not bounded cofinally
   below one;
2. screened shell estimates would close the branch but are not implied by
   finite labels, CE, or imported heat-kernel rows;
3. Peter-Weyl step matrices are legitimate fixed-row objects but no cofinal
   centered contraction, path expansion, and tail control are proved;
4. Peter-Weyl projection requires `PWBAND`, `PWDECAY`, or a direct cofinal
   tail table, none of which is supplied for the actual residual Hamiltonian;
5. bridge damping would close with a tail budget, but bridge amplitudes and
   the common tail budget remain unsourced.

Moreover, the current corpus does not prove a lower-floor theorem strong
enough to falsify adaptive Branch A.

Proof.

Items 1--5 are Verdicts 10.5, 11.6, 12.5, 13.5, and 14.5.  The missing
lower-floor statement is Theorem 7.3. `square`

### Corollary 15.2: Exact Post-Paper-25 Frontier

After Paper 25, adaptive Branch A is not closed and not falsified.  It is
parked behind a genuinely new same-law scalar theorem:

```math
\begin{array}{c}
\exists a>0:\ \mathfrak D_{sharp}^{cof}(a)<1,\\[2mm]
\text{or}\quad
S_r^{N,j}\le AC_{sh}e^{-(\mu-h_{sh})r}
\text{ with the strict screened margin},\\[2mm]
\text{or}\quad
\Theta_L+\Kappa_L
\text{ beats path entropy cofinally},\\[2mm]
\text{or}\quad
\kappa_{PW}^{N,j}(L(N,j))\to0
\text{ with a passing projected table},\\[2mm]
\text{or}\quad
\mathrm{BRIDGEDAMP}(D)+\mathrm{KTAIL}(\kappa)
\text{ passes the bridge gate}.
\end{array}
```

These are not five bookkeeping tasks.  They are five forms of new information
about the actual adaptive pushed-forward scalar law.

### Corollary 15.3: Paper-25 Freeze

Paper 25 is finished as a Branch-A source audit.  It does not prove continuum
Yang-Mills confinement.  It proves exactly why the surviving Branch-A routes
cannot be advanced by reusing the closed Paper-20--24 bookkeeping and why the
next proof, if it stays in Branch A, must be a new actual-law numerical,
tail, spectral, screening, or bridge theorem.

## 16. Truth-Status Investigation Of The Five Options

Corollary 15.2 lists five actual-law statements.  Section 15 proves that the
current corpus does not derive them as source theorems.  This section asks the
stronger question: can the current corpus prove that any of them is actually
true or actually false for the adaptive pushed-forward `SEL2` law?

The answer is no for all five.  This is not a retreat to vagueness.  It is a
same-law theorem-level boundary: Papers 20--24 do not contain enough scalar
information to decide the truth values.  A future proof may of course decide
one of them by adding actual-law row values, tail values, or a new analytic
theorem.

### Definition 16.1: The Five Truth Statements

Let:

```math
{\mathsf T}_1
:=
\left[
\exists a>0:\ \mathfrak D_{sharp}^{cof}(a)<1
\right],
```

```math
{\mathsf T}_2
:=
\left[
\exists A,\mu,h_{sh},C_{sh}:
S_r^{N,j}\le AC_{sh}e^{-(\mu-h_{sh})r}
\ \text{cofinally, and}\
\mu-h_{sh}>\log(1+AC_{sh}/4)
\right],
```

```math
{\mathsf T}_3
:=
\left[
\exists \theta,B,h,C:
\Theta_L+\Kappa_L\le\theta\ \text{cofinally, and}\
-\log\theta-h>\log(1+BC/4)
\right],
```

```math
{\mathsf T}_4
:=
\left[
\kappa_{PW}^{N,j}(L(N,j))\to0
\ \text{and a projected finite table passes its scalar gate}
\right],
```

and

```math
{\mathsf T}_5
:=
\left[
\mathrm{BRIDGEDAMP}(D)+\mathrm{KTAIL}(\kappa)
\ \text{passes the bridge gate}
\right].
```

These are statements about the actual adaptive pushed-forward scalar law,
not about a separate model.

### Definition 16.2: Current-Corpus Decision

A statement \({\mathsf T}\) is **currently proved true** if it follows from
the exact same-law results of Papers 20--25.  It is **currently proved false**
if the same corpus proves its negation on the actual adaptive law.  It is
**currently undecided** if neither proof exists and the closed scalar body
admits same-law residual completions preserving all already spent ledgers
while making the statement true in one completion and false in another.

Current undecidability is not physical falsity.  It says only that the present
finite scalar records do not decide the actual law.

### Proposition 16.3: Truth Status Of \({\mathsf T}_1\)

\({\mathsf T}_1\), the direct Dobrushin row option, is currently undecided.

Proof.

Positive attempt.  The fixed-row table exists by Lemma 10.2, and
Theorem 10.3 would close the branch if a cofinal value below one were printed.
No such value is printed.

Negative attempt.  To prove \(\neg{\mathsf T}_1\), one must show
\(\mathfrak D_{sharp}^{cof}(a)\ge1\) for every \(a>0\).  To falsify adaptive
Branch A rather than only the Dobrushin route, one also needs the lower floor
\(\overline\Lambda_{13}^{RPF}\ge M_*\).  Theorem 7.3 proves that this lower
floor is not available.

Independence mechanism.  Paper 23 Lemma 33.6 gives residual completions
preserving the closed non-RPF ledgers with tiny rapidly decaying residual
tails, making a strict Dobrushin row possible, and completions with
long-range residual interactions that make every proposed strict row fail.
Thus the current corpus proves neither \({\mathsf T}_1\) nor
\(\neg{\mathsf T}_1\). `square`

### Proposition 16.4: Truth Status Of \({\mathsf T}_2\)

\({\mathsf T}_2\), the screened shell option, is currently undecided.

Proof.

Positive attempt.  Theorem 11.2 proves that \({\mathsf T}_2\) would close
adaptive Branch A.  But finite shell counting, canonical labels, and exact
`BC/CE` do not bound the shell oscillations \(S_r^{N,j}\), by Lemmas 11.3
and 11.4.

Negative attempt.  To prove \(\neg{\mathsf T}_2\), one would need a lower
bound showing that every possible screened-margin quadruple
\((A,\mu,h_{sh},C_{sh})\) fails for the actual shell sums.  No such shell
lower table is printed.

Independence mechanism.  The same residual-tail mechanism as in Lemma 33.6
can be chosen exponentially decaying in \(r\), producing a completion
compatible with a screened shell theorem, or can place non-small conditional
oscillation on growing shells, defeating every fixed screened margin while
preserving the closed non-RPF ledgers.  Hence the current corpus proves
neither \({\mathsf T}_2\) nor \(\neg{\mathsf T}_2\). `square`

### Proposition 16.5: Truth Status Of \({\mathsf T}_3\)

\({\mathsf T}_3\), the Peter-Weyl step-contraction option, is currently
undecided.

Proof.

Positive attempt.  Theorem 12.3 proves that a cofinal step contraction with
the path-entropy margin closes Branch A.  Fixed-row matrices
\(\Pi_{\le L}T_{e,\zeta}\Pi_{\le L}\) are same-law finite objects by
Definition 12.1.

The missing positive data are exactly the three cofinal clauses: a centered
spectral contraction, a residual edge-path expansion, and the tail bound
\(\Kappa_L\).  Paper 23 Lemmas 35.6, 35.7, 36.8, and 36.9 show that finite
Peter-Weyl truncation, compactness, and the central heat-kernel factor do not
provide those clauses.

Negative attempt.  To prove \(\neg{\mathsf T}_3\), one would need to show
that every finite cutoff schedule and every admissible path expansion fails
the scalar margin on the actual law.  The current corpus prints no such
cofinal lower bound on \(\Theta_L+\Kappa_L\) and no theorem excluding all
same-law path expansions.

Independence mechanism.  Residual completions with strong local smoothing and
edge-local path generation can make a step source true.  Residual completions
with almost deterministic copying across an RPF edge, or with high-order
jump interactions not generated by the declared edge graph, make the
contraction or path clause fail.  These completions are compatible with the
closed non-RPF ledgers.  Thus the current corpus proves neither
\({\mathsf T}_3\) nor \(\neg{\mathsf T}_3\). `square`

### Proposition 16.6: Truth Status Of \({\mathsf T}_4\)

\({\mathsf T}_4\), the Peter-Weyl tail plus passing projected table option,
is currently undecided.

Proof.

Positive attempt.  Theorem 13.3 proves that a cofinal tail source makes the
projection route honest, and the projected finite table can then be tested
against its scalar gate.  Paper 23 Lemmas 55.3 and 55.6 show exactly how
`PWBAND`, `PWDECAY`, or a direct tail profile would supply the needed
`KTAIL` input.

The current corpus does not prove any of those tail sources for the actual
minimal-edge residual Hamiltonian.  Proposition 55.4 shows finite records do
not imply finite band support, and Propositions 55.8--55.9 show that existing
heat-kernel/Casimir and bounded-collar estimates do not transfer to this
actual tail.

Negative attempt.  To prove \(\neg{\mathsf T}_4\), one must rule out all
cofinal cutoff schedules and all projected finite-table passes.  The current
corpus does not print high-mode lower bounds for
\(\kappa_{PW}^{N,j}(L)\), nor does it print a lower-floor obstruction for
every projected table.

Independence mechanism.  A residual completion may be finite-band or have
rapid Peter-Weyl coefficient decay, making the tail side true.  Another
completion may place surviving true-bridge mixed variation in arbitrarily
high modes with slow tail decay, defeating every proposed cofinal tail
profile.  Both preserve the closed non-RPF ledgers.  Therefore the current
corpus proves neither \({\mathsf T}_4\) nor \(\neg{\mathsf T}_4\). `square`

### Proposition 16.7: Truth Status Of \({\mathsf T}_5\)

\({\mathsf T}_5\), the bridge-damping plus tail option, is currently
undecided.

Proof.

Positive attempt.  Theorem 14.2 proves that
`BRIDGEDAMP(D)+KTAIL(kappa)` closes the branch under the Paper-23 bridge
gate.  The bridge amplitude table is finite rowwise and same-law by Paper 23
Definition 50.1.

The missing positive data are the cofinal damping of the actual true-bridge
amplitudes and the common tail source.  Lemma 14.3 and Proposition 14.4 show
that finite bridge labels do not bound amplitudes, and Section 13 shows that
the tail side is not currently sourced.

Negative attempt.  To prove \(\neg{\mathsf T}_5\), one must show that no
finite bridge type map, no same-law bridge statistic, and no admissible
tail schedule can make the bridge gate pass on the actual law.  The current
corpus prints no such universal lower bound on bridge amplitudes or tails.

Independence mechanism.  A completion with exponentially damped true-bridge
amplitudes and small Peter-Weyl tail can make \({\mathsf T}_5\) true.  A
completion with an \(O(1)\) surviving bridge amplitude or high-mode
true-bridge tail can make it false.  Paper 23 Lemma 50.6 and Section 55 show
that the closed ledgers do not exclude either behavior.  Hence the current
corpus proves neither \({\mathsf T}_5\) nor \(\neg{\mathsf T}_5\). `square`

### Theorem 16.8: Five-Option Truth-Status Theorem

For each \(i=1,\dots,5\), the current V3 corpus proves neither
\({\mathsf T}_i\) nor \(\neg{\mathsf T}_i\) for the actual adaptive
pushed-forward `SEL2` law.  What it proves is current-corpus
undecidability: the closed scalar records do not determine the truth value of
any of the five Branch-A options.

Proof.

Apply Propositions 16.3--16.7. `square`

### Corollary 16.9: What Would Settle The Actual Truth

The actual truth of the five options can only be settled by adding one of the
following same-law objects:

1. the cofinal sharp row values \(D_{DOB}^{N,j}(a)\);
2. the cofinal shell values \(S_r^{N,j}\);
3. the cofinal step matrices, path expansion, and tail values
   \(\Theta_L,\Kappa_L\);
4. the cofinal Peter-Weyl tail profile of \(C_0^{m,N,j}\) plus projected
   finite-table values;
5. the cofinal bridge-amplitude/damping table plus the common tail profile.

A proof using any of these would be Barandes-aligned because it remains on
the same pushed-forward scalar law.  A proof that imports a continuum
Yang-Mills measure, an off-law heat-kernel subprocess, or an unrecorded
Markov factor would not settle the Paper-25 problem.

### Corollary 16.10: Final Paper-25 Freeze

Paper 25 has now investigated all five Branch-A options from Corollary 15.2
both positively and negatively.  None is proved true by the current corpus;
none is proved false by the current corpus; all five are reduced to explicit
new actual-law scalar data.  This is the rigorous endpoint of Paper 25.
