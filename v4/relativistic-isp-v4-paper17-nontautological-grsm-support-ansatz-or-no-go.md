# Relativistic ISP V4 Paper 17: Non-Tautological GR/SM Support Ansatz Or No-Go

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-27

Status: Non-tautological audit of the GR/SM-informed finite actual-law
support ansatz after Paper 16.  This paper does not assume that the ansatz
is right merely because any finite probability law can be rewritten in that
shape.  It separates the tautological representation theorem from the real
physics theorem: independently licensed reference support, finite soft
score, and hard constraint admissibility.

Paper 16 ended with the ansatz

$$
\boxed{
\mathbb P^{act}_a(q\mid R)
=
{1\over Z_a(R)}
\rho_a(q\mid R)e^{-S^{eff}_a(q\mid R)}
1_{\{C_a(q\mid R)=0\}}.
}
$$

Paper 17 asks the sharper question:

$$
\boxed{
\hbox{when is this an actual law principle, and when is it just notation?}
}
$$

The answer is:

$$
\boxed{
\hbox{the form is automatic; the license is not.}
}
$$

The finite factorization and the hard/soft separation are genuine theorems.
The claim that the actual ISP law has this form with exogenously licensed
\(\rho,S^{eff},C\) is a conditional naturality theorem, not yet a theorem of
the current corpus.

## Abstract

The missing law problem in Papers 14 through 16 is not that no formula can be
written for the actual row law.  A formula can always be written after the
support table is known.  The missing law problem is that the formula must
come from declared finite record structure rather than from the desired
answer.

Paper 17 proves four exact results.

First, a tautological factorization theorem: every finite law can be written
in GR/SM support form if one is allowed to choose the support mask after the
fact.

Second, a non-tautological licensing criterion: the ansatz is meaningful only
when \(\rho\), \(S^{eff}\), and \(C\) are defined before the two-row support
signs are queried, and are built from declared finite record, gauge,
boundary, quotient, residual, or constraint data.

Third, a hard/soft separation theorem: finite positive soft weights cannot
create exact support zeros.  Exact zeros require hard reference exclusion,
infinite action, or hard constraint violation.

Fourth, a conditional uniqueness theorem: under finite total-record
discipline, exogenous reference support, finite soft reweighting, hard
constraint admissibility, quotient invariance, and no row-fitting, the
GR/SM-informed support ansatz is forced up to gauge redefinitions of
\(\rho\) and \(S^{eff}\).

The paper also proves the negative result needed to avoid circularity:
without those naturality assumptions, the ansatz is not uniquely selected
and cannot solve the missing law problem.

## 0. Imports And Discipline

### Import 0.1: Paper-16 Live Rectangle Fiber

Paper 16 reduces the live problem to two row records \(q_0,q_1\) in one
conditioned rectangle fiber:

$$
\boxed{
H(q_b)=\ell,\qquad U(q_b)=u_b,\qquad b=0,1.
}
$$

The unsourced actual masses are

$$
\boxed{
\widehat m_b
:=
\mathbb P^{act}_a(H=\ell,U=u_b),
\qquad b=0,1.
}
$$

The current corpus does not prove

$$
\boxed{
\widehat m_0>0,\quad \widehat m_1>0,
\quad
\widehat m_0=0,\quad \widehat m_1=0.
}
$$

### Import 0.2: Paper-16 GR/SM-Informed Ansatz

The candidate finite actual-law form is

$$
\boxed{
\mathbb P^{act}_a(q\mid R)
=
{1\over Z_a(R)}
\rho_a(q\mid R)e^{-S^{eff}_a(q\mid R)}
1_{\{C_a(q\mid R)=0\}}.
}
$$

The intended interpretation is:

1. \(q\) is a complete finite total record;
2. \(R\) is declared finite conditioning data;
3. \(\rho_a\) is reference support;
4. \(S^{eff}_a\) is a finite soft score/action;
5. \(C_a=0\) is hard admissibility.

### Discipline 0.3: Barandes Alignment

The law remains Barandes-aligned only if

$$
\boxed{
\mathbb P^{act}_a(q\mid R)
}
$$

is a law on complete finite records, not a hidden Markov chain over
intermediate states.  The ansatz is allowed to be global:

$$
\boxed{
S^{eff}_a(q\mid R)
\quad\hbox{and}\quad
C_a(q\mid R)
\quad\hbox{may depend on the whole finite record }q.
}
$$

It is not allowed to smuggle in a stepwise transition dynamics:

$$
\boxed{
\mathbb P^{act}_a(q_0,\ldots,q_n\mid R)
\ne
\prod_k T(q_{k+1}\mid q_k)
\quad\hbox{as a hidden primitive.}
}
$$

### Discipline 0.4: The No-Answer-Fitting Rule

The ansatz is non-tautological only if \(\rho,S^{eff},C\) are defined before
the row support signs are known:

$$
\boxed{
\rho,S^{eff},C
\quad\hbox{must not be functions of }
(\widehat m_0>0,\widehat m_1>0).
}
$$

Equivalently, the support mask

$$
\boxed{
K(R):=\{q:C(q\mid R)=0,\ \rho(q\mid R)>0,\ S^{eff}(q\mid R)<\infty\}
}
$$

must be licensed by record structure, not reverse-engineered from
\(\operatorname{supp}\mathbb P^{act}\).

## 1. Step One: State The Non-Tautological Ansatz

### Definition 1.1: Tautological GR/SM Form

Let \(\Omega(R)\) be a finite record space and \(P\) any probability law on
\(\Omega(R)\).  The tautological support form is obtained by setting

$$
\boxed{
K_P:=\{q\in\Omega(R):P(q)>0\},
}
$$

choosing any positive \(\rho\) on \(K_P\), and defining

$$
\boxed{
C_P(q)=0\Longleftrightarrow q\in K_P.
}
$$

Then \(P\) has the GR/SM-looking support form.

This is mathematically true and physically useless.  It explains the data
after the data have already been used.

### Definition 1.2: Licensed GR/SM Support Ansatz

A licensed GR/SM support ansatz consists of a tuple

$$
\boxed{
(\Omega(R),\rho(q\mid R),S^{eff}(q\mid R),C(q\mid R))
}
$$

with the following properties.

1. \(\Omega(R)\) is the declared finite total-record space determined by
   the record alphabet, conditioning data, quotient conventions, and finite
   admissibility grammar.
2. \(\rho(q\mid R)\ge 0\) is a reference measure defined from the declared
   finite record construction, not from the answer support.
3. \(S^{eff}(q\mid R)\in{\mathbb R}\cup\{\infty\}\) is a soft score/action
   defined by finite record functionals, couplings, penalties, Jacobians, or
   regularity terms before the queried support signs are known.
4. \(C(q\mid R)=0\) is a hard finite constraint defined by gauge, boundary,
   quotient, residual, closure, Bianchi, hypersurface, or conservation data.
5. The normalizer

$$
\boxed{
Z(R)=\sum_{q\in\Omega(R)}
\rho(q\mid R)e^{-S^{eff}(q\mid R)}
1_{\{C(q\mid R)=0\}}
}
$$

is finite and positive.

The actual law is then

$$
\boxed{
P^{ans}(q\mid R)
=
{1\over Z(R)}
\rho(q\mid R)e^{-S^{eff}(q\mid R)}
1_{\{C(q\mid R)=0\}}.
}
$$

### Criterion 1.3: Non-Tautology Tests

The ansatz passes the non-tautology test only if it satisfies all four
conditions:

$$
\boxed{
\begin{array}{ll}
\mathrm{NT1}:&\rho,S^{eff},C\hbox{ are defined before the support table is
queried},\\[1mm]
\mathrm{NT2}:&C\hbox{ has a declared finite physical/mathematical source},\\[1mm]
\mathrm{NT3}:&\rho\hbox{ is not zeroed row-by-row to fit the answer},\\[1mm]
\mathrm{NT4}:&S^{eff}=\infty\hbox{ is used only for a licensed hard
admissibility failure}.
\end{array}
}
$$

### Proposition 1.4: What Step One Proves

The non-tautological statement of the ansatz is:

$$
\boxed{
\mathrm{V4P17\text{-}LICENSED\text{-}GRSM\text{-}ANSATZ}.
}
$$

It is the claim that the actual law equals \(P^{ans}\) for a tuple satisfying
Definition 1.2 and Criterion 1.3.

This is not proved by the current corpus:

$$
\boxed{
\mathrm{V4P17\text{-}LICENSED\text{-}GRSM\text{-}ANSATZ}^{cur}
\quad\hbox{not proved.}
}
$$

But the criterion is now exact.  Any future proof must license the tuple; any
future falsification can attack one of \(\mathrm{NT1}\)-\(\mathrm{NT4}\).

Proof.  The current corpus has proposed the form and audited candidate
constraint components, but it has not derived \(\rho,S^{eff},C\) as
independent finite actual-law data.  Therefore the licensed ansatz remains a
target, not a theorem.  `square`

### Exhaustion 1.5: Ways Step One Can Fail

There are only four failure modes at this level:

1. the row support mask is fitted after the answer is known;
2. the reference measure \(\rho\) is chosen to zero exactly the unwanted row;
3. \(S^{eff}=\infty\) is used as a disguised support mask;
4. \(C=0\) has no finite constraint meaning.

If none of these happens, the ansatz is non-tautological.

## 2. Step Two: Finite Support-Factorization Theorem

### Theorem 2.1: Positive Finite Factorization On A Licensed Support Set

Let \(\Omega\) be finite.  Let \(K\subseteq\Omega\) be nonempty.  Let \(P\)
be a probability law such that

$$
\boxed{
P(q)>0\Longleftrightarrow q\in K.
}
$$

Let \(\rho(q)>0\) for all \(q\in K\).  Then there exists a finite score
\(S(q)\) on \(K\) such that

$$
\boxed{
P(q)
=
{1\over Z}\rho(q)e^{-S(q)}1_{\{q\in K\}}.
}
$$

One choice is

$$
\boxed{
S(q)=-\log {P(q)\over \rho(q)},
\qquad q\in K,
}
$$

with \(Z=1\).

Proof.  Since \(P(q)>0\) and \(\rho(q)>0\) on \(K\), the logarithm is finite.
Then \(\rho(q)e^{-S(q)}=P(q)\) on \(K\), and both sides vanish off \(K\) by
the indicator.  `square`

### Corollary 2.2: The Form Is Mathematically Natural

Every positive finite law on a licensed support set has the GR/SM support
shape:

$$
\boxed{
\hbox{finite law on }K
\quad\Longleftrightarrow\quad
\hbox{reference measure plus finite score on }K.
}
$$

Therefore the ansatz is not exotic.  It is the natural finite analogue of:

$$
\boxed{
\hbox{positive density on the admissible constraint surface.}
}
$$

### Proposition 2.3: Gauge Non-Uniqueness

The split between \(\rho\) and \(S\) is not unique.  For any finite function
\(f\) on \(K\),

$$
\boxed{
\rho'(q)=e^{f(q)}\rho(q),
\qquad
S'(q)=S(q)+f(q)
}
$$

gives the same product:

$$
\boxed{
\rho'(q)e^{-S'(q)}
=
\rho(q)e^{-S(q)}.
}
$$

Thus \(\rho\) and \(S\) are unique only after a gauge convention is fixed.

### Definition 2.4: Useful Gauges

The main finite gauges are:

1. counting gauge: \(\rho(q)=1\) on \(\Omega\);
2. quotient gauge: \(\rho(q)\) is the quotient counting measure on physical
   equivalence classes;
3. symmetry gauge: \(\rho\) is invariant under declared finite symmetries;
4. geometric gauge: \(\rho\) includes finite volume, Jacobian, or
   discretization weights;
5. reference-process gauge: \(\rho\) is generated by a declared record
   construction protocol.

The support question is gauge-invariant:

$$
\boxed{
P(q)>0
\quad\hbox{does not depend on finite }\rho/S\hbox{ gauge reshuffling.}
}
$$

### Theorem 2.5: Support Is The Real Primitive

The finite factorization theorem reduces the missing law problem to the
support set

$$
\boxed{
K(R)=\{q:\rho(q\mid R)>0,\ S^{eff}(q\mid R)<\infty,\ C(q\mid R)=0\}.
}
$$

If \(K(R)\) is independently licensed, the soft score can represent any
positive finite law on \(K(R)\).  If \(K(R)\) is not independently licensed,
the ansatz has not solved the support problem.

Proof.  Theorem 2.1 shows that once \(K\) and \(\rho>0\) on \(K\) are given,
the positive weights are representable.  Therefore the only exact support
content is the independently licensed set \(K\).  `square`

### Exhaustion 2.6: What Step Two Settles

Step two proves:

$$
\boxed{
\mathrm{V4P17\text{-}FINITE\text{-}SUPPORT\text{-}FACTORIZATION}.
}
$$

It also proves the limitation:

$$
\boxed{
\hbox{factorization does not license support.}
}
$$

So the factorization is a theorem, but it is not the missing law by itself.

## 3. Step Three: Hard/Soft Separation Theorem

### Definition 3.1: Soft And Hard Mechanisms

A soft mechanism is a finite positive multiplier:

$$
\boxed{
w(q)=e^{-S(q)},\qquad 0<w(q)<\infty.
}
$$

A hard mechanism is one that can make support exactly vanish:

$$
\boxed{
\rho(q)=0
\quad\hbox{or}\quad
S(q)=\infty
\quad\hbox{or}\quad
C(q)\ne0.
}
$$

### Theorem 3.2: Finite Soft Scores Cannot Create Exact Zeros

Assume

$$
\boxed{
\rho(q)>0,\qquad S(q)<\infty,\qquad C(q)=0.
}
$$

Then

$$
\boxed{
P^{ans}(q)>0.
}
$$

Therefore exact support exclusion requires at least one hard failure:

$$
\boxed{
P^{ans}(q)=0
\Longrightarrow
\rho(q)=0
\quad\hbox{or}\quad
S(q)=\infty
\quad\hbox{or}\quad
C(q)\ne0.
}
$$

Proof.  If \(\rho(q)>0\), \(S(q)<\infty\), and \(C(q)=0\), then
\(\rho(q)e^{-S(q)}1_{\{C(q)=0\}}>0\).  Since \(Z\) is finite and positive,
\(P^{ans}(q)>0\).  The contrapositive gives the exclusion statement.
`square`

### Corollary 3.3: Exact Singleton Selection Is Hard

For the two-row fiber:

$$
\boxed{
\widehat m_0>0,\ \widehat m_1=0
}
$$

requires a hard failure for \(u_1\), and similarly for \(u_0\).  A large but
finite action difference can make one row very small, but not exactly absent.

### Proposition 3.4: Zero-Temperature Limits Are Not Finite Laws

Suppose

$$
\boxed{
P_\beta(q)
=
{1\over Z_\beta}\rho(q)e^{-\beta S(q)}
}
$$

with finite \(\beta<\infty\), positive \(\rho\), and finite \(S\).  Then
every row with \(\rho(q)>0\) remains positive at finite \(\beta\).

The limit

$$
\boxed{
\lim_{\beta\to\infty}P_\beta
}
$$

can create exact zeros, but then the zero is a limiting hard-selection rule,
not a finite soft reweighting.  To use it in ISP, the limit rule itself must
be declared as hard finite data or as a valid asymptotic theorem.

### Corollary 3.5: The GR/SM Lesson

The finite analogue of GR/SM support logic is:

$$
\boxed{
\hbox{actions reweight; constraints admit or forbid.}
}
$$

This is the main reason the ansatz is physically informed rather than an
arbitrary notation.

### Exhaustion 3.6: Ways Step Three Can Fail

The hard/soft separation theorem can fail only if one of the hypotheses is
false:

1. \(\rho(q)\) is zero;
2. \(S(q)=\infty\);
3. \(C(q)\ne0\);
4. \(Z\) is zero or infinite;
5. the law is not actually of the ansatz form.

No other finite soft mechanism can produce exact support exclusion.

## 4. Step Four: The Hard-Status Table

### Definition 4.1: Live Row Hard Status

For the two live row values, define the total-record row fibers

$$
\boxed{
\Omega_b
:=
\{q\in\Omega(R):H(q)=\ell,\ U(q)=u_b\},
\qquad b=0,1.
}
$$

The exact row mass is

$$
\boxed{
\widehat m_b
=
\sum_{q\in\Omega_b}
{1\over Z(R)}
\rho(q\mid R)e^{-S^{eff}(q\mid R)}
1_{\{C(q\mid R)=0\}}.
}
$$

If the row fiber has been atomized to one representative \(q_b\), define

$$
\boxed{
\rho_b:=\rho(q_b\mid R),\qquad
S_b:=S^{eff}(q_b\mid R),\qquad
C_b:=C(q_b\mid R),
\qquad b=0,1.
}
$$

In the non-atomized case, the correct row hard status is existential:

$$
\boxed{
\begin{array}{ll}
\mathrm{REF}_b:&\exists q\in\Omega_b\hbox{ with }\rho(q\mid R)>0,\\[1mm]
\mathrm{ACT}_b:&\exists q\in\Omega_b\hbox{ with }S^{eff}(q\mid R)<\infty,\\[1mm]
\mathrm{CON}_b:&\exists q\in\Omega_b\hbox{ with }C(q\mid R)=0,
\end{array}
}
$$

but the three witnesses must be the same total record:

$$
\boxed{
\exists q\in\Omega_b:
\rho(q\mid R)>0,\quad
S^{eff}(q\mid R)<\infty,\quad
C(q\mid R)=0.
}
$$

The hard-status table is:

$$
\boxed{
\begin{array}{c|ccc|c}
\hbox{row} & \rho_b>0 & S_b<\infty & C_b=0 & \widehat m_b>0\\ \hline
u_0 & ? & ? & ? & ?\\
u_1 & ? & ? & ? & ?
\end{array}
}
$$

### Theorem 4.2: Hard-Status Table Decides The Two-Row Support Question

Assume the licensed GR/SM ansatz.  Then:

$$
\boxed{
\widehat m_b>0
\Longleftrightarrow
\exists q\in\Omega_b:
\rho(q\mid R)>0,\quad S^{eff}(q\mid R)<\infty,\quad C(q\mid R)=0.
}
$$

In the atomized one-record-row case this reduces to

$$
\boxed{
\widehat m_b>0
\Longleftrightarrow
\rho_b>0,\quad S_b<\infty,\quad C_b=0.
}
$$

In particular, if

$$
\boxed{
\exists q\in\Omega_0\hbox{ hard-allowed},
\qquad
\exists q\in\Omega_1\hbox{ hard-allowed},
}
$$

then

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

Proof.  The row mass is a finite sum of nonnegative terms.  It is positive
if and only if at least one summand is positive.  By Theorem 3.2, a summand
is positive if and only if the same total record has positive reference
support, finite score, and satisfied hard constraint.  `square`

### Lemma 4.3: How To Prove The Reference Entries

To prove

$$
\boxed{
\rho_0>0,\qquad \rho_1>0,
}
$$

one must show that both rows are generated by the declared finite
total-record grammar before the actual law is weighted.

Sufficient finite certificates are:

1. both \(q_0,q_1\) are in \(\Omega(R)\);
2. neither is removed by quotient representative conventions;
3. both have positive reference construction count;
4. both preserve declared alphabet, boundary, and source compatibility.

Falsification certificate:

$$
\boxed{
q_b\notin\Omega(R)
\quad\hbox{or}\quad
\rho_b=0
}
$$

with an independent finite reason.

### Lemma 4.4: How To Prove The Finite-Score Entries

To prove

$$
\boxed{
S_0<\infty,\qquad S_1<\infty,
}
$$

one must show that all score terms are finite on both rows:

$$
\boxed{
S_b
=
S^{base}_b
+S^{geom}_b
+S^{gauge}_b
+S^{res}_b
+S^{inst}_b
+S^{Jac}_b
}
$$

with each finite.  The exact decomposition can vary, but the certificate
must rule out hidden infinite penalties.

Falsification certificate:

$$
\boxed{
S_b=\infty
}
$$

with a declared infinite-action reason, not a fitted row exclusion.

### Lemma 4.5: How To Prove The Constraint Entries

To prove

$$
\boxed{
C_0=0,\qquad C_1=0,
}
$$

one must either evaluate every hard constraint component on both rows, or
prove row-blindness on the live fiber:

$$
\boxed{
C(q_0\mid R)=C(q_1\mid R).
}
$$

Falsification certificate:

$$
\boxed{
C_b\ne0
}
$$

with a declared finite constraint violation.

### Proposition 4.6: Current-Corpus Status Of The Table

The current corpus has not printed the six entries

$$
\boxed{
\rho_0>0,\quad \rho_1>0,\quad
S_0<\infty,\quad S_1<\infty,\quad
C_0=0,\quad C_1=0.
}
$$

Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}HARDSTATUS\text{-}TABLE}^{cur}
\quad\hbox{not proved.}
}
$$

But the problem is now finite and local in the proof sense.  The table is
the exact certificate needed to turn the ansatz into a two-row support
theorem.

## 5. Step Five: Constraint Audit And Support-Exclusion Routes

### Definition 5.1: Hard Constraint Vector

Use the Paper-16 candidate vector:

$$
\boxed{
C
=
\left(
C^{Gauss},\,
C^{bdry},\,
C^{Bianchi},\,
C^{hyp},\,
C^{quot},\,
C^{res}
\right).
}
$$

For row \(b\), write

$$
\boxed{
C^X_b:=C^X(q_b\mid R).
}
$$

A component \(X\) is a support-exclusion route if it proves:

$$
\boxed{
C^X_0=0,\quad C^X_1\ne0
}
$$

or the reverse.

### Route 5.2: Gauss/Gauge Constraint

Gauss/gauge constraints can separate rows only if the two row records carry
different hard charge, flux, gauge-sector, or gauge-invariant closure data.

Positive route:

$$
\boxed{
\hbox{print }C^{Gauss}_0=0,\ C^{Gauss}_1\ne0
\quad\hbox{or the reverse.}
}
$$

Full-support route:

$$
\boxed{
C^{Gauss}_0=C^{Gauss}_1=0.
}
$$

No-go for this component:

$$
\boxed{
C^{Gauss}\hbox{ factors only through }H=\ell\hbox{ and shared }R.
}
$$

Then Gauss is row-blind on \(u_0,u_1\).

Current status:

$$
\boxed{
\hbox{no live Gauss/gauge row-separator is printed.}
}
$$

### Route 5.3: Boundary And Superselection Constraint

Boundary and superselection constraints can separate rows only if \(u_0\) and
\(u_1\) are not actually in the same conditioned problem.

Positive route:

$$
\boxed{
u_b\hbox{ changes }R\hbox{ or violates a superselection label.}
}
$$

But if that happens, the two rows were misclassified:

$$
\boxed{
\hbox{they do not belong to one common conditional fiber.}
}
$$

Full-support route:

$$
\boxed{
C^{bdry}_0=C^{bdry}_1=0
}
$$

inside the declared \(R\)-fiber.

Current status:

$$
\boxed{
\hbox{boundary/superselection does not currently separate the live rows.}
}
$$

### Route 5.4: Bianchi/Closure Constraint

Bianchi/closure is the strongest geometric Einstein candidate.  It can
exclude a row if the row changes finite curvature closure:

$$
\boxed{
C^{Bianchi}_0=0,\quad C^{Bianchi}_1\ne0
}
$$

or the reverse.

The proof target is not abstract.  It is the table:

$$
\boxed{
\begin{array}{c|c}
\hbox{row} & C^{Bianchi}_b\\ \hline
u_0 & ?\\
u_1 & ?
\end{array}
}
$$

Current status:

$$
\boxed{
\hbox{the live Bianchi/closure row table is not printed.}
}
$$

Therefore Bianchi/closure remains a real support-exclusion candidate, but
not a current theorem.

### Route 5.5: Hypersurface Compatibility Constraint

Hypersurface compatibility can separate rows only if \(U\) changes a hard
normal/tangential compatibility equation not already determined by \(H\):

$$
\boxed{
C^{hyp}(H=\ell,U=u_0)
\ne
C^{hyp}(H=\ell,U=u_1).
}
$$

If \(C^{hyp}\) factors through \(H=\ell\), then

$$
\boxed{
C^{hyp}_0=C^{hyp}_1.
}
$$

Current status:

$$
\boxed{
\hbox{no row-sensitive hypersurface compatibility table is printed.}
}
$$

### Route 5.6: Quotient Or Gauge-Representative Constraint

Quotient data can do two different things.

It can collapse rows:

$$
\boxed{
u_0\sim u_1
\quad\Longrightarrow\quad
\hbox{one physical quotient row.}
}
$$

Or it can forbid one representative by convention:

$$
\boxed{
u_0\hbox{ is allowed representative},\quad
u_1\hbox{ is not.}
}
$$

But representative exclusion is not physical singleton selection unless the
quotient convention is declared before the support question.

Current status:

$$
\boxed{
\hbox{no quotient collapse or representative rule currently decides }
u_0,u_1.
}
$$

### Route 5.7: Residual Actual Constraint

The residual route remains the sharpest support-kernel candidate:

$$
\boxed{
C^{res}(q):=\eta^{NN,K}_{a,ij}(q).
}
$$

It would prove row exclusion if:

$$
\boxed{
\eta(q_0)=0,\quad \eta(q_1)\ne0
}
$$

or the reverse, and if \(\eta=0\) is a hard actual support condition.

Two independent licenses are needed:

$$
\boxed{
\begin{array}{ll}
\mathrm{ACTUALITY}:&\eta\hbox{ is finite actual record data},\\[1mm]
\mathrm{KERNEL}:&\eta=0\hbox{ is a hard support condition.}
\end{array}
}
$$

Current status:

$$
\boxed{
\mathrm{ACTUALITY}^{cur}\hbox{ and }\mathrm{KERNEL}^{cur}
\quad\hbox{not proved.}
}
$$

### Theorem 5.8: Exhaustion Of Current Hard-Constraint Routes

Within the current Paper-16/Paper-17 candidate vector, every exact singleton
support-exclusion route must pass through one of:

$$
\boxed{
C^{Gauss},\ C^{bdry},\ C^{Bianchi},\ C^{hyp},\ C^{quot},\ C^{res}.
}
$$

The current corpus does not print a row-separating table for any of them.
Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}HARD\text{-}CONSTRAINT\text{-}SEPARATOR}^{cur}
\quad\hbox{not proved.}
}
$$

Proof.  The vector lists the finite hard sources currently proposed by the
GR/SM ansatz and by Papers 14 through 16.  Each component has been audited
above.  None has a printed live two-row separator.  `square`

### Corollary 5.9: What A Real Support-Exclusion Theorem Must Look Like

A future support-exclusion theorem must contain an explicit row table:

$$
\boxed{
\begin{array}{c|cccccc}
\hbox{row} &
C^{Gauss} & C^{bdry} & C^{Bianchi} & C^{hyp} & C^{quot} & C^{res}\\ \hline
u_0 & 0 & 0 & 0 & 0 & 0 & 0\\
u_1 & 0 & 0 & \ne0 & 0 & 0 & 0
\end{array}
}
$$

or the analogous table with a different component separating.  Without such
a row table, there is no licensed Einstein singleton selection.

## 6. Step Six: Uniqueness And Naturality Of The Ansatz

### Definition 6.1: Natural Finite Actual-Law Axioms

The GR/SM support ansatz is forced only under explicit finite naturality
axioms:

$$
\boxed{
\begin{array}{ll}
\mathrm{A1}:&\hbox{finite total-record law on }\Omega(R),\\[1mm]
\mathrm{A2}:&\hbox{exogenous reference support }\rho\hbox{ from record
grammar},\\[1mm]
\mathrm{A3}:&\hbox{positive finite soft reweighting on admissible records},\\[1mm]
\mathrm{A4}:&\hbox{exact zeros come only from declared hard exclusions},\\[1mm]
\mathrm{A5}:&\hbox{gauge/quotient invariance of physical row labels},\\[1mm]
\mathrm{A6}:&\hbox{no row-fitting from the queried support signs}.
\end{array}
}
$$

These axioms are not empty.  They are the finite ISP version of the
GR/SM-style distinction:

$$
\boxed{
\hbox{kinematic record space}
\quad+\quad
\hbox{constraint surface}
\quad+\quad
\hbox{positive weighting on that surface}.
}
$$

### Theorem 6.2: Conditional Naturality Theorem

Assume \(\mathrm{A1}\)-\(\mathrm{A6}\).  Then the actual law has the
licensed GR/SM support form

$$
\boxed{
\mathbb P^{act}(q\mid R)
=
{1\over Z(R)}
\rho(q\mid R)e^{-S^{eff}(q\mid R)}
1_{\{C(q\mid R)=0\}},
}
$$

up to finite \(\rho/S^{eff}\) gauge transformations.

Proof.  By \(\mathrm{A1}\), the law is a finite total-record law.  By
\(\mathrm{A2}\), there is an exogenous reference support \(\rho\).  By
\(\mathrm{A4}\), the exact support set is determined by declared hard
exclusions, encoded as \(C(q\mid R)=0\), together with reference support and
infinite-action exclusions.  By \(\mathrm{A3}\), the law is strictly positive
and finite on the admissible set.  Theorem 2.1 then represents the positive
weights as \(\rho e^{-S^{eff}}\).  By \(\mathrm{A5}\), quotient-equivalent
records are represented consistently.  By \(\mathrm{A6}\), the construction
is not fitted to the queried row support signs.  Gauge non-uniqueness is
exactly Proposition 2.3.  `square`

### Corollary 6.3: What This Would Prove For The Live Two-Row Fiber

If \(\mathrm{A1}\)-\(\mathrm{A6}\) are proved and the hard-status table is
filled with:

$$
\boxed{
\rho_0,\rho_1>0,\qquad
S_0,S_1<\infty,\qquad
C_0=C_1=0,
}
$$

then:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

If one hard entry fails, the same theorem gives a licensed
support-exclusion result.

### No-Go 6.4: Unconditional Uniqueness Is False

Without \(\mathrm{A1}\)-\(\mathrm{A6}\), the GR/SM support ansatz is not
uniquely forced.

Counterexample.  Let

$$
\boxed{
\Omega=\{q_0,q_1\}.
}
$$

Define two laws:

$$
\boxed{
P_F(q_0)=P_F(q_1)={1\over2}
}
$$

and

$$
\boxed{
P_E(q_0)=1,\qquad P_E(q_1)=0.
}
$$

Both can be written in GR/SM-looking form.  For \(P_F\), take
\(\rho_0=\rho_1=1\), \(S_0=S_1=0\), \(C_0=C_1=0\).  For \(P_E\), take the
same \(\rho,S\) but set \(C(q_1)\ne0\), or take \(\rho_1=0\), or take
\(S_1=\infty\).

Unless the choice of \(C\), \(\rho\), or \(S=\infty\) is independently
licensed, the two laws are equally representable.  Therefore the ansatz form
alone does not decide between Feynman support and Einstein selection.
`square`

### No-Go 6.5: Hidden Infinite Scores Recreate The Old Problem

If arbitrary infinite scores are allowed, any desired support can be encoded
as:

$$
\boxed{
S(q)=
\begin{cases}
0,&q\in K,\\
\infty,&q\notin K.
\end{cases}
}
$$

This is just a support mask in action notation.  It is valid only when
\(S=\infty\) is licensed by a hard finite reason.

Therefore:

$$
\boxed{
\hbox{unlicensed infinite action is not a solution to the missing law
problem.}
}
$$

### No-Go 6.6: Hidden Reference Zeros Recreate The Old Problem

If arbitrary reference zeros are allowed, any desired support can be encoded
as:

$$
\boxed{
\rho(q)>0\Longleftrightarrow q\in K.
}
$$

This is valid only when \(\rho\) is produced by a declared finite record
grammar or quotient construction.

Therefore:

$$
\boxed{
\hbox{unlicensed reference support is not a solution to the missing law
problem.}
}
$$

### No-Go 6.7: Hidden Constraints Recreate The Old Problem

If arbitrary constraints are allowed, any support table can be encoded as:

$$
\boxed{
C(q)=0\Longleftrightarrow q\in K.
}
$$

This is valid only when \(C\) is a declared finite gauge, boundary, closure,
hypersurface, quotient, or residual constraint.

Therefore:

$$
\boxed{
\hbox{unlicensed constraints are not a solution to the missing law problem.}
}
$$

### Theorem 6.8: Exact Status Of The Ansatz After Exhaustion

The GR/SM-informed support ansatz has three levels:

$$
\boxed{
\begin{array}{ll}
\mathrm{Level\ 1}:&\hbox{finite representation theorem: proved},\\[1mm]
\mathrm{Level\ 2}:&\hbox{hard/soft support separation: proved},\\[1mm]
\mathrm{Level\ 3}:&\hbox{licensed actual-law naturality theorem:
conditional}.
\end{array}
}
$$

The current corpus proves Levels 1 and 2, and proves Level 3 only under
\(\mathrm{A1}\)-\(\mathrm{A6}\).  It does not prove that the actual ISP law
satisfies all six axioms.

Thus:

$$
\boxed{
\mathrm{V4P17\text{-}GRSM\text{-}ANSATZ\text{-}RIGHTNESS}^{cur}
\quad\hbox{conditional, not absolute.}
}
$$

Proof.  Level 1 is Theorem 2.1.  Level 2 is Theorem 3.2.  Level 3 is Theorem
6.2 and the no-go results 6.4 through 6.7.  `square`

## 7. Feynman And Einstein Verdict

### Feynman Verdict 7.1

Feynman's route is now concrete:

$$
\boxed{
\hbox{fill the six-entry hard-status table.}
}
$$

He would not accept another abstract derivation of the ansatz until the live
rows are evaluated:

$$
\boxed{
\begin{array}{c|ccc}
\hbox{row} & \rho_b>0 & S_b<\infty & C_b=0\\ \hline
u_0 & ? & ? & ?\\
u_1 & ? & ? & ?
\end{array}
}
$$

If both rows pass, the missing-law problem is closed on the two-row support
side.  If one row fails, the exact failing entry identifies the support
exclusion mechanism.

### Einstein Verdict 7.2

Einstein's route is also concrete:

$$
\boxed{
\hbox{derive the hard constraint surface from principle, not from the row
answer.}
}
$$

The principle must say why the admissible finite configurations are exactly:

$$
\boxed{
C^{Gauss}=0,\quad
C^{bdry}=0,\quad
C^{Bianchi}=0,\quad
C^{hyp}=0,\quad
C^{quot}=0,\quad
C^{res}=0
}
$$

or some corrected subset/superset.  Then the two-row table becomes a
calculation, not a guess.

### Combined Verdict 7.3

The ansatz is the right answer to the missing law problem if and only if the
following two tasks succeed:

$$
\boxed{
\begin{array}{ll}
\mathrm{Einstein}:&\hbox{license }\rho,S^{eff},C\hbox{ from finite
principle},\\[1mm]
\mathrm{Feynman}:&\hbox{compute their values on }q_0,q_1.
\end{array}
}
$$

Either task alone is insufficient.  Einstein without Feynman gives a
principle with no row calculation.  Feynman without Einstein gives a table
with no guarantee that the entries were not fitted.

## 8. Final Settlement

Paper 17 fully explores the six requested steps.

### Settlement 8.1: Step One

The non-tautological ansatz is defined precisely:

$$
\boxed{
\mathrm{V4P17\text{-}LICENSED\text{-}GRSM\text{-}ANSATZ}.
}
$$

Current status:

$$
\boxed{
\hbox{not proved by the current corpus.}
}
$$

### Settlement 8.2: Step Two

Finite support factorization is proved:

$$
\boxed{
\mathrm{V4P17\text{-}FINITE\text{-}SUPPORT\text{-}FACTORIZATION}.
}
$$

But it does not license support.

### Settlement 8.3: Step Three

Hard/soft separation is proved:

$$
\boxed{
\mathrm{V4P17\text{-}HARD\text{-}SOFT\text{-}SEPARATION}.
}
$$

Exact zeros require hard support data.

### Settlement 8.4: Step Four

The hard-status table is the exact finite certificate:

$$
\boxed{
\mathrm{V4P17\text{-}HARDSTATUS\text{-}TABLE}.
}
$$

Current status:

$$
\boxed{
\hbox{not printed by the current corpus.}
}
$$

### Settlement 8.5: Step Five

The candidate hard-constraint routes have been exhausted at the current
level:

$$
\boxed{
C^{Gauss},\ C^{bdry},\ C^{Bianchi},\ C^{hyp},\ C^{quot},\ C^{res}.
}
$$

Current status:

$$
\boxed{
\hbox{no row-separating hard-constraint table is printed.}
}
$$

### Settlement 8.6: Step Six

Conditional naturality is proved:

$$
\boxed{
\mathrm{A1}\hbox{-}\mathrm{A6}
\Longrightarrow
\mathrm{licensed\ GR/SM\ support\ ansatz}.
}
$$

Unconditional uniqueness is false.

### Final Verdict 8.7

The ansatz is not yet proved to be the actual missing law.  But Paper 17
settles exactly what would make it the right answer:

$$
\boxed{
\hbox{prove }\mathrm{A1}\hbox{-}\mathrm{A6}
\quad\hbox{and print the hard-status table.}
}
$$

Equivalently, the next real theorem must be one of:

$$
\boxed{
\begin{array}{ll}
1.&\mathrm{V4P17\text{-}FINITE\text{-}ACTUAL\text{-}LAW\text{-}NATURALITY},\\[1mm]
2.&\mathrm{V4P17\text{-}HARDSTATUS\text{-}TABLE},\\[1mm]
3.&\mathrm{V4P17\text{-}ROW\text{-}SEPARATING\text{-}CONSTRAINT},\\[1mm]
4.&\mathrm{V4P17\text{-}RESIDUAL\text{-}ACTUAL\text{-}KERNEL}.
\end{array}
}
$$

This is a sharper endpoint than Paper 16.  Paper 16 made the ansatz
physically plausible.  Paper 17 proves which parts are mathematics, which
parts are naturality assumptions, and exactly where a future proof or
falsification must strike.

## 9. Einstein-Jaynes Route: Least-Biased Finite Actual Law

The previous endpoint still leaves the question:

$$
\boxed{
\hbox{what principle licenses }S^{eff}\hbox{ rather than merely naming it?}
}
$$

The strongest GR/SM-informed answer is not to guess \(S^{eff}\) row by row.
It is to derive \(S^{eff}\) from a finite least-extra-structure principle.

### Principle 9.1: Finite Einstein-Jaynes Actual-Law Principle

Fix declared finite data:

1. a finite total-record space \(\Omega(R)\);
2. an exogenous reference measure \(\rho(q\mid R)\);
3. a hard admissible set

$$
\boxed{
K(R)=\{q\in\Omega(R):C(q\mid R)=0\};
}
$$

4. declared finite source observables

$$
\boxed{
F_1,\ldots,F_m:K(R)\to{\mathbb R};
}
$$

5. declared finite source values

$$
\boxed{
f_1,\ldots,f_m.
}
$$

Let \({\mathcal M}(R)\) be the set of probability laws \(P\) on \(K(R)\)
such that

$$
\boxed{
\sum_{q\in K(R)}P(q)F_r(q)=f_r,
\qquad r=1,\ldots,m.
}
$$

The finite Einstein-Jaynes principle says:

$$
\boxed{
\mathbb P^{act}(\cdot\mid R)
=
\arg\min_{P\in{\mathcal M}(R)}
D(P\Vert\rho_K),
}
$$

where \(\rho_K\) is the normalized reference measure on \(K(R)\), and

$$
\boxed{
D(P\Vert\rho_K)
=
\sum_{q\in K(R)}
P(q)\log {P(q)\over \rho_K(q)}.
}
$$

Plainly:

$$
\boxed{
\hbox{choose the least biased total-record law compatible with the declared
hard constraints and source records.}
}
$$

### Alignment 9.2: Why This Is Barandes-Compatible

The principle is a rule for a probability law on complete finite records:

$$
\boxed{
q\in\Omega(R).
}
$$

It does not introduce hidden intermediate transitions.  The source
observables \(F_r(q)\) may depend on the whole record:

$$
\boxed{
F_r(q)\hbox{ is global finite record data.}
}
$$

Thus the resulting law may be non-Markovian even when it has exponential
form.

### Theorem 9.3: Finite I-Projection Derives The GR/SM Ansatz

Assume:

1. \(K(R)\) is nonempty;
2. \(\rho(q\mid R)>0\) for all \(q\in K(R)\);
3. \({\mathcal M}(R)\) contains a full-support law on \(K(R)\).

Then the unique minimizer of \(D(P\Vert\rho_K)\) over \({\mathcal M}(R)\)
has the form

$$
\boxed{
\mathbb P^{act}(q\mid R)
=
{1\over Z(\lambda;R)}
\rho(q\mid R)
\exp\left\{-\sum_{r=1}^m\lambda_rF_r(q)\right\}
1_{\{C(q\mid R)=0\}}.
}
$$

Thus the effective score is not guessed.  It is:

$$
\boxed{
S^{eff}(q\mid R)
=
\sum_{r=1}^m\lambda_rF_r(q)
}
$$

up to the finite \(\rho/S\) gauge.

Proof.  Since \(\Omega(R)\) is finite and \({\mathcal M}(R)\) contains a
full-support law, the entropy minimizer is in the relative interior of the
constraint polytope.  The Lagrangian is

$$
\boxed{
{\mathcal L}(P,\alpha,\lambda)
=
\sum_{q\in K}P(q)\log {P(q)\over\rho_K(q)}
\;+\;
\alpha\left(\sum_{q\in K}P(q)-1\right)
\;+\;
\sum_{r=1}^m\lambda_r
\left(\sum_{q\in K}P(q)F_r(q)-f_r\right).
}
$$

Stationarity in each \(P(q)>0\) gives

$$
\boxed{
\log {P(q)\over \rho_K(q)}+1+\alpha+\sum_r\lambda_rF_r(q)=0.
}
$$

Therefore

$$
\boxed{
P(q)
=
Z^{-1}\rho_K(q)
\exp\left\{-\sum_r\lambda_rF_r(q)\right\}.
}
$$

Absorbing the normalization of \(\rho_K\) into \(Z\) gives the stated form.
Strict convexity of relative entropy on the finite simplex gives uniqueness.
`square`

### Corollary 9.4: Soft Source Constraints Preserve Interior Support

Under the hypotheses of Theorem 9.3,

$$
\boxed{
q\in K(R)
\quad\Longrightarrow\quad
\mathbb P^{act}(q\mid R)>0.
}
$$

Thus the Einstein-Jaynes principle predicts full support on the hard
constraint surface whenever the declared source constraints have an interior
feasible solution.

### Boundary Lemma 9.5: Singleton Selection Is A Boundary Or Hard Event

If the minimizer assigns zero mass to some \(q\in K(R)\), then at least one
of the following is true:

1. \(\rho(q\mid R)=0\);
2. \(q\notin K(R)\);
3. the feasible moment set has no full-support point, so the source values
   lie on a boundary face;
4. the law is obtained as a zero-temperature or infinite-multiplier limit.

In all cases, exact zero support has become hard data:

$$
\boxed{
\hbox{reference zero, hard constraint, boundary source value, or infinite
limit.}
}
$$

Proof.  If \(\rho>0\) on \(K\) and the feasible set contains a full-support
law, Theorem 9.3 gives a positive exponential law on all of \(K\).  Therefore
zero mass can occur only when one of these hypotheses fails or in a limiting
case outside the finite interior theorem.  `square`

### Non-Tautology 9.6: What Must Be Licensed

The Einstein-Jaynes route is non-tautological only if the following objects
are declared before the two-row support query:

$$
\boxed{
\Omega(R),\qquad
\rho(q\mid R),\qquad
C(q\mid R),\qquad
F_1,\ldots,F_m,\qquad
f_1,\ldots,f_m.
}
$$

It fails the no-answer-fitting rule if any source observable is secretly a
row selector such as

$$
\boxed{
F(q)=1_{\{U(q)=u_0\}}
}
$$

unless that row selector is an independently declared physical source or
instrument record.

### Theorem 9.7: Einstein-Jaynes Conditional Rightness

If the finite actual law obeys the Einstein-Jaynes principle with licensed
data satisfying the full-support feasibility hypothesis, then the GR/SM
support ansatz is the right answer to the missing law problem in the
following exact sense:

$$
\boxed{
\mathbb P^{act}(q\mid R)>0
\Longleftrightarrow
\rho(q\mid R)>0,\quad
C(q\mid R)=0,\quad
q\hbox{ lies in the feasible source face}.
}
$$

If the feasible source face is the whole hard surface \(K(R)\), then:

$$
\boxed{
\mathbb P^{act}(q\mid R)>0
\Longleftrightarrow
\rho(q\mid R)>0,\quad C(q\mid R)=0.
}
$$

Proof.  Combine the I-projection form of Theorem 9.3 with the boundary lemma.
The only possible support loss comes from the licensed reference support, the
hard constraint set, or a licensed source boundary face.  `square`

## 10. Feynman Lab For The Einstein-Jaynes Principle

Feynman now reduces the principle to the smallest possible test.

### Definition 10.1: Two-Row Jaynes Lab

Let the hard surface inside the live fiber contain exactly two atomized rows:

$$
\boxed{
K=\{q_0,q_1\},
\qquad
H(q_b)=\ell,\quad U(q_b)=u_b.
}
$$

Assume

$$
\boxed{
\rho_0,\rho_1>0.
}
$$

Let there be one declared finite source observable \(F\), with values

$$
\boxed{
F(q_0)=F_0,\qquad F(q_1)=F_1.
}
$$

and declared source value

$$
\boxed{
\mathbb E_P[F]=f.
}
$$

### Theorem 10.2: Two-Row Interior Source Gives Two-Row Support

If

$$
\boxed{
F_0<f<F_1
}
$$

or the same inequality with \(0,1\) reversed, then the Einstein-Jaynes
minimizer has

$$
\boxed{
P(q_0)>0,\qquad P(q_1)>0.
}
$$

Proof.  The constraint \(E[F]=f\) forces

$$
\boxed{
P(q_1)
=
{f-F_0\over F_1-F_0},
\qquad
P(q_0)
=
{F_1-f\over F_1-F_0}.
}
$$

Both are positive exactly when \(f\) is strictly between \(F_0\) and \(F_1\).
`square`

### Corollary 10.3: Two-Row Singleton Selection Is Boundary Data

In the same two-row lab:

$$
\boxed{
P(q_0)=1,\quad P(q_1)=0
}
$$

requires

$$
\boxed{
f=F_0
}
$$

or a hard exclusion of \(q_1\).  Similarly, selection of \(q_1\) requires
\(f=F_1\) or hard exclusion of \(q_0\).

Thus singleton selection is not a generic soft-source phenomenon.  It is a
boundary-source or hard-constraint phenomenon.

### Proposition 10.4: Multi-Observable Version

Let \(F(q)=(F_1(q),\ldots,F_m(q))\).  In the two-row lab the feasible source
values form the line segment:

$$
\boxed{
\operatorname{conv}\{F(q_0),F(q_1)\}.
}
$$

Interior source values give both rows positive mass.  Endpoint source values
select one row.  Source values outside the segment are infeasible.

Therefore the Feynman decision table is:

$$
\boxed{
\begin{array}{c|c}
\hbox{source position} & \hbox{row support}\\ \hline
\hbox{interior of segment} & u_0,u_1\hbox{ both positive}\\
\hbox{endpoint }F(q_0) & u_0\hbox{ only}\\
\hbox{endpoint }F(q_1) & u_1\hbox{ only}\\
\hbox{outside segment} & \hbox{inconsistent source data}.
\end{array}
}
$$

### Falsification Test 10.5: The Source-Selector Trap

The Einstein-Jaynes route is falsified as a non-tautological law if the
source list \(F_1,\ldots,F_m\) includes unlicensed row selectors.  For
example, if one declares

$$
\boxed{
F(q)=1_{\{q=q_0\}},
\qquad
f=1,
}
$$

then the principle selects \(q_0\), but this is just the answer inserted as a
constraint.

Therefore:

$$
\boxed{
\hbox{row-selector observables must be physical records, not proof devices.}
}
$$

### Falsification Test 10.6: The Boundary-Value Trap

Even if \(F\) is licensed, an endpoint source value is hard information:

$$
\boxed{
f=F(q_0)
\quad\Longrightarrow\quad
P(q_1)=0.
}
$$

This is legitimate only if the endpoint value is actually recorded by the
conditioning data \(R\).  Otherwise the source value is another disguised
support mask.

### Feynman Verdict 10.7

The Einstein-Jaynes principle gives a concrete prediction:

$$
\boxed{
\hbox{generic interior finite source data produce full support on }K.
}
$$

So for the live \(u_0,u_1\) problem, the next calculation is not vague.  It
is:

$$
\boxed{
\hbox{locate the declared source vector }f
\hbox{ relative to }
\operatorname{conv}\{F(q_0),F(q_1)\}.
}
$$

Interior means Feynman two-row support.  Endpoint means Einstein selection,
but only if the endpoint source value is licensed.

## 11. Updated Final Settlement After Einstein-Jaynes

Paper 17 now has one stronger conditional route than Section 8.

### Settlement 11.1: What Is Now Proved

The following are theorems:

$$
\boxed{
\begin{array}{ll}
1.&\mathrm{finite\ support\ factorization},\\[1mm]
2.&\mathrm{hard/soft\ separation},\\[1mm]
3.&\mathrm{finite\ I\text{-}projection\ exponential\ form},\\[1mm]
4.&\mathrm{two\text{-}row\ interior\ source\ full\ support}.
\end{array}
}
$$

### Settlement 11.2: What Is Still Conditional

The missing law is solved by the Einstein-Jaynes route only if the corpus
proves:

$$
\boxed{
\begin{array}{ll}
\mathrm{EJ1}:&\Omega(R)\hbox{ and }\rho\hbox{ are exogenous finite record
data},\\[1mm]
\mathrm{EJ2}:&C=0\hbox{ is a licensed hard admissibility surface},\\[1mm]
\mathrm{EJ3}:&F_1,\ldots,F_m\hbox{ are licensed source observables},\\[1mm]
\mathrm{EJ4}:&f_1,\ldots,f_m\hbox{ are actual conditioning records},\\[1mm]
\mathrm{EJ5}:&\mathbb P^{act}\hbox{ is the relative-entropy minimizer},\\[1mm]
\mathrm{EJ6}:&\hbox{the live source vector is interior, or a licensed
boundary value is printed}.
\end{array}
}
$$

Current-corpus status:

$$
\boxed{
\mathrm{V4P17\text{-}EINSTEIN\text{-}JAYNES\text{-}ACTUAL\text{-}LAW}^{cur}
\quad\hbox{not proved.}
}
$$

### Settlement 11.3: Why This Is Genuine Progress

Before the Einstein-Jaynes route, the ansatz was physically plausible but
could be accused of being a disguised support mask.  After the
Einstein-Jaynes route, the exact burden is sharper:

$$
\boxed{
\hbox{prove an actual finite least-bias principle, or find the licensed
source boundary/hard constraint that selects a row.}
}
$$

This is not another circle because it gives a falsifiable finite object:

$$
\boxed{
\left(\rho,\ C,\ F,\ f,\ \operatorname{conv}\{F(q_0),F(q_1)\}\right).
}
$$

If \(f\) is interior and both rows are hard-allowed, the ansatz predicts
two-row support.  If \(f\) is an endpoint, the endpoint must be a real source
record.  If \(F\) is a row selector without physical license, the route is
rejected as answer-fitting.

### Final Target 11.4

The next theorem should be:

$$
\boxed{
\mathrm{V4P17\text{-}EJ\text{-}SOURCE\text{-}INTERIOR\text{-}OR\text{-}BOUNDARY}.
}
$$

It must print one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{Interior}:&f\in\operatorname{relint}
\operatorname{conv}\{F(q):q\in\Omega_b,\ b=0,1\},\\[1mm]
\mathrm{Boundary}:&f\hbox{ lies on a licensed source boundary selecting a
row},\\[1mm]
\mathrm{Invalid}:&F\hbox{ or }f\hbox{ is not independently licensed}.
\end{array}
}
$$

This is now the cleanest Einstein/Feynman synthesis:

$$
\boxed{
\hbox{Einstein derives the exponential law from least bias;}
\quad
\hbox{Feynman checks whether the source point is interior or boundary.}
}
$$

## 12. Source-Simplex Certificate

The Einstein-Jaynes route turns the missing law problem into a finite convex
geometry problem.  This section makes that problem executable.

### Definition 12.1: Licensed Source Algebra

A licensed source algebra is a finite list of source observables

$$
\boxed{
{\mathcal F}
=
(F_1,\ldots,F_m),
\qquad
F_r:\Omega(R)\to{\mathbb R},
}
$$

such that each \(F_r\) is sourced by declared record data before the support
question is asked.  Admissible sources include:

1. boundary/source records already present in \(R\);
2. metric, gauge, charge, flux, and quotient records;
3. finite stress-response or source-response records;
4. residual records, if residual actuality is independently proved;
5. detector records, if the detector is part of the declared conditioning
   data and not added after seeing the row answer.

The source algebra is unlicensed if it contains a row-selector observable
whose only purpose is to select a desired support row:

$$
\boxed{
F(q)=1_{\{U(q)=u_b\}}
}
$$

unless this row selector is itself an actual physical record in \(R\).

### Definition 12.2: Row Source Images

For the live rows define row fibers

$$
\boxed{
\Omega_b
=
\{q\in\Omega(R):H(q)=\ell,\ U(q)=u_b\},
\qquad b=0,1.
}
$$

The source image of row \(b\) is

$$
\boxed{
{\mathcal S}_b
:=
{\mathcal F}(\Omega_b\cap K)
=
\{(F_1(q),\ldots,F_m(q)):q\in\Omega_b,\ C(q)=0\}.
}
$$

The live source polytope is

$$
\boxed{
{\mathcal P}_{01}
:=
\operatorname{conv}({\mathcal S}_0\cup{\mathcal S}_1).
}
$$

The actual declared source point is

$$
\boxed{
f=(f_1,\ldots,f_m).
}
$$

### Definition 12.3: Row Faces

A face \(G\) of \({\mathcal P}_{01}\) is a row-0 face if

$$
\boxed{
G\cap{\mathcal S}_0\ne\emptyset,
\qquad
G\cap{\mathcal S}_1=\emptyset.
}
$$

It is a row-1 face if

$$
\boxed{
G\cap{\mathcal S}_1\ne\emptyset,
\qquad
G\cap{\mathcal S}_0=\emptyset.
}
$$

It is a mixed face if it intersects both source images.

### Theorem 12.4: Source-Simplex Trichotomy

Assume the licensed Einstein-Jaynes principle, positive reference support on
the hard-allowed records, and licensed source algebra \({\mathcal F}\).  Then
exactly one of the following holds for the live two-row source problem.

1. Interior:

$$
\boxed{
f\in\operatorname{relint}{\mathcal P}_{01}.
}
$$

Then both rows have positive support:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

2. Boundary:

$$
\boxed{
f\in G
}
$$

for a proper face \(G\) of \({\mathcal P}_{01}\).  The supported rows are
exactly those whose source images meet \(G\).  A row is excluded only if
\(G\) is a face disjoint from its source image.

3. Outside:

$$
\boxed{
f\notin{\mathcal P}_{01}.
}
$$

Then the declared source data are inconsistent with the proposed live
two-row hard surface.

Proof.  The feasible probability laws on the finite hard surface push
forward under \({\mathcal F}\) to convex combinations of the source image.
Therefore \(f\) is feasible exactly when it lies in \({\mathcal P}_{01}\).
If \(f\) is in the relative interior, it admits a convex representation with
positive weight on points from both nonempty row images, and the
I-projection interior theorem gives positive support to the corresponding
hard-allowed records.  If \(f\) lies on a proper face, every feasible law is
supported on the preimage of that face; row support is exactly determined by
which row images meet the face.  If \(f\) is outside the polytope, no
probability law on the declared live hard surface can satisfy the source
constraints.  `square`

### Corollary 12.5: Atomized Two-Point Row Test

If

$$
\boxed{
{\mathcal S}_0=\{s_0\},\qquad {\mathcal S}_1=\{s_1\},
}
$$

then

$$
\boxed{
{\mathcal P}_{01}=[s_0,s_1].
}
$$

The decision is:

$$
\boxed{
\begin{array}{c|c}
\hbox{source location} & \hbox{support verdict}\\ \hline
f\in(s_0,s_1) & \widehat m_0,\widehat m_1>0\\
f=s_0 & \widehat m_0>0,\ \widehat m_1=0\\
f=s_1 & \widehat m_1>0,\ \widehat m_0=0\\
f\notin[s_0,s_1] & \hbox{inconsistent source data}.
\end{array}
}
$$

Endpoint selection is licensed only if the endpoint source value is itself
declared in \(R\), not chosen to force the support answer.

### Theorem 12.6: Farkas Separator Certificate

For a finite source polytope \({\mathcal P}_{01}\), the statement

$$
\boxed{
f\notin{\mathcal P}_{01}
}
$$

is equivalent to the existence of a vector \(\lambda\in{\mathbb R}^m\) and
constant \(\alpha\) such that

$$
\boxed{
\lambda\cdot f>\alpha,
\qquad
\lambda\cdot s\le\alpha
\quad\hbox{for every }s\in{\mathcal S}_0\cup{\mathcal S}_1.
}
$$

Likewise, row-1 exclusion by a row-0 face is certified by a vector
\(\lambda\) such that

$$
\boxed{
\lambda\cdot f=\alpha,\qquad
\lambda\cdot s=\alpha\hbox{ for some }s\in{\mathcal S}_0,
\qquad
\lambda\cdot s<\alpha\hbox{ for every }s\in{\mathcal S}_1.
}
$$

and similarly with the row labels reversed.

Proof.  This is the finite separating hyperplane theorem for convex hulls.
The face statement is the exposed-face version: a supporting hyperplane
defines a face, and a row is excluded exactly when its source image is
strictly on the nonface side.  `square`

### Algorithm 12.7: The Finite Certificate Search

The source-simplex certificate is finite:

1. print the licensed source list \({\mathcal F}\);
2. print \({\mathcal S}_0\) and \({\mathcal S}_1\);
3. print the declared source point \(f\);
4. solve the finite convex membership problem

$$
\boxed{
f\in\operatorname{conv}({\mathcal S}_0\cup{\mathcal S}_1);
}
$$

5. if \(f\) is interior, record two-row support;
6. if \(f\) is on a face, print the supporting hyperplane and the row images
   that meet the face;
7. if \(f\) is outside, print the Farkas separator;
8. if \({\mathcal F}\) or \(f\) is unlicensed, reject the route as
   answer-fitting.

### Definition 12.8: Source-Simplex Certificate Target

The exact target is:

$$
\boxed{
\mathrm{V4P17\text{-}EJ\text{-}SOURCE\text{-}SIMPLEX\text{-}CERTIFICATE}.
}
$$

It consists of:

$$
\boxed{
({\mathcal F},\ {\mathcal S}_0,\ {\mathcal S}_1,\ f,\ \lambda,\alpha)
}
$$

where \((\lambda,\alpha)\) is optional in the interior case but required for
boundary or outside certificates.

### Current-Corpus Status 12.9

The current corpus has not printed a licensed source algebra, row source
images, and actual source point for the live \(u_0,u_1\) fiber.  Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}EJ\text{-}SOURCE\text{-}SIMPLEX\text{-}CERTIFICATE}^{cur}
\quad\hbox{not proved.}
}
$$

But the route is now executable.  It does not ask for another philosophical
law.  It asks for a finite convex table.

### Final Verdict 12.10

Einstein's creative move is:

$$
\boxed{
\hbox{the actual law is the least-biased law compatible with licensed
finite source records.}
}
$$

Feynman's creative move is:

$$
\boxed{
\hbox{draw the finite source polytope and locate }f.
}
$$

Together they replace the missing law problem by a finite source-simplex
certificate.  This is the current best path because it makes the support
answer testable:

$$
\boxed{
\begin{array}{c|c}
\hbox{certificate} & \hbox{meaning}\\ \hline
f\in\operatorname{relint}{\mathcal P}_{01} & \hbox{two-row support}\\
f\in\hbox{row-selecting face} & \hbox{licensed Einstein selection}\\
f\notin{\mathcal P}_{01} & \hbox{inconsistent source data}\\
{\mathcal F}\hbox{ unlicensed} & \hbox{answer-fitting, reject route}.
\end{array}
}
$$

## 13. Einstein Filter, Feynman Minimal Source Table

The source-simplex theorem still needs a practical way to choose
\({\mathcal F}\).  The correct order is:

$$
\boxed{
\hbox{Einstein filters which sources are licensed;}
\quad
\hbox{Feynman prints the smallest table that can decide the rows.}
}
$$

### Definition 13.1: Einstein License Filter

A finite observable \(F:\Omega(R)\to{\mathbb R}\) passes the Einstein license
filter on the live problem if it satisfies all five tests:

$$
\boxed{
\begin{array}{ll}
\mathrm{L1}:&F\hbox{ is measurable on complete finite records},\\[1mm]
\mathrm{L2}:&F\hbox{ is declared before querying }\widehat m_0,\widehat m_1,\\[1mm]
\mathrm{L3}:&F\hbox{ is sourced by }R\hbox{ or by an independently actual
record},\\[1mm]
\mathrm{L4}:&F\hbox{ respects the declared quotient/gauge conventions},\\[1mm]
\mathrm{L5}:&F\hbox{ is not a row selector unless row selection is itself a
physical record}.
\end{array}
}
$$

Let

$$
\boxed{
{\mathsf Src}_{lic}(R)
}
$$

denote the finite vector space or finite list of observables passing this
filter in the current finite model.

### Definition 13.2: Minimal Separating Source Table

A licensed source sublist

$$
\boxed{
{\mathcal F}_*=(F_{r_1},\ldots,F_{r_k})
\subseteq{\mathsf Src}_{lic}(R)
}
$$

is row-separating if

$$
\boxed{
{\mathcal F}_*(\Omega_0\cap K)
\ne
{\mathcal F}_*(\Omega_1\cap K)
}
$$

as finite source-image sets.

It is minimal if no proper licensed sublist is row-separating.

The minimal source table is:

$$
\boxed{
\begin{array}{c|c}
\hbox{row} & {\mathcal F}_*(\Omega_b\cap K)\\ \hline
u_0 & {\mathcal S}^{*}_0\\
u_1 & {\mathcal S}^{*}_1
\end{array}
}
$$

together with the declared source point \(f_*\).

### Theorem 13.3: Row-Blind Licensed Sources Cannot Select A Row

Assume the Einstein-Jaynes principle with positive reference support on both
hard-allowed row fibers.  If every licensed source observable is row-blind:

$$
\boxed{
F(\Omega_0\cap K)=F(\Omega_1\cap K)
\quad\hbox{for every }F\in{\mathsf Src}_{lic}(R),
}
$$

then no licensed source-simplex certificate can select exactly one of
\(u_0,u_1\).  If the common source constraints are feasible, both rows have
positive support.

Proof.  Row-blindness means every licensed source algebra has identical
source image on the two row fibers.  Therefore every feasible source face
that meets one row image meets the other.  By the source-simplex trichotomy,
a face can exclude a row only if it is disjoint from that row's image.  This
cannot happen under row-blindness.  With positive reference support and
feasibility, the I-projection assigns positive mass to hard-allowed records
in both row fibers.  `square`

### Theorem 13.4: Minimal Source Table Decision

Assume a licensed minimal row-separating source table
\({\mathcal F}_*\) exists.  Define

$$
\boxed{
{\mathcal P}^{*}_{01}
=
\operatorname{conv}({\mathcal S}^{*}_0\cup{\mathcal S}^{*}_1).
}
$$

Then exactly one of the following outcomes holds.

1. Interior:

$$
\boxed{
f_*\in\operatorname{relint}{\mathcal P}^{*}_{01}
}
$$

and both rows are supported.

2. Licensed boundary:

$$
\boxed{
f_*\in G
}
$$

for a proper face \(G\).  The supported rows are precisely those whose
minimal source image meets \(G\).  Any singleton verdict must print the
supporting hyperplane of \(G\).

3. Outside:

$$
\boxed{
f_*\notin{\mathcal P}^{*}_{01}.
}
$$

Then the declared source point is inconsistent with the proposed two-row
hard surface, and a Farkas separator must be printed.

4. License failure:

$$
\boxed{
{\mathcal F}_*\not\subseteq{\mathsf Src}_{lic}(R)
\quad\hbox{or}\quad
f_*\hbox{ is not declared in }R.
}
$$

Then the route is rejected as answer-fitting.

Proof.  Apply Theorem 12.4 to the licensed minimal source algebra.  The
license-failure case is excluded from the theorem's hypotheses and therefore
must be handled as invalid input rather than as a support verdict.  `square`

### Proposition 13.5: Current-Corpus Minimal Table Status

The current corpus has not printed:

$$
\boxed{
{\mathsf Src}_{lic}(R),
\qquad
{\mathcal F}_*,
\qquad
{\mathcal S}^{*}_0,
\qquad
{\mathcal S}^{*}_1,
\qquad
f_*.
}
$$

Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}LICENSED\text{-}MINIMAL\text{-}SOURCE\text{-}TABLE}^{cur}
\quad\hbox{not proved.}
}
$$

But the route now has a real failure verdict:

$$
\boxed{
{\mathsf Src}_{lic}(R)\hbox{ row-blind}
\quad\Longrightarrow\quad
\hbox{Einstein-Jaynes cannot select one row in the live fiber.}
}
$$

In that case, the route predicts Feynman two-row support, provided both row
fibers are hard-allowed and reference-positive.

### Algorithm 13.6: Feynman First With Einstein Filter Active

The next finite calculation is:

1. list every candidate source observable suggested by the corpus;
2. apply the Einstein license filter \(\mathrm{L1}\)-\(\mathrm{L5}\);
3. discard unlicensed row selectors;
4. compute the row images of the surviving sources;
5. find a minimal separating sublist \({\mathcal F}_*\), or prove none
   exists;
6. if none exists, record row-blindness and the two-row support prediction;
7. if one exists, locate \(f_*\) in
   \(\operatorname{conv}({\mathcal S}^{*}_0\cup{\mathcal S}^{*}_1)\);
8. print interior, boundary, outside, or invalid with the required
   certificate.

### Final Verdict 13.7

The cleaned path is now:

$$
\boxed{
\mathrm{source\ law}
\quad\to\quad
\mathrm{licensed\ source\ algebra}
\quad\to\quad
\mathrm{minimal\ source\ table}
\quad\to\quad
\mathrm{source\ simplex\ verdict}.
}
$$

This is the first formulation where every outcome is informative:

$$
\boxed{
\begin{array}{c|c}
\hbox{outcome} & \hbox{meaning}\\ \hline
\hbox{no licensed separating source} & \hbox{no Einstein selection from EJ;
expect two-row support}\\
\hbox{interior source point} & \hbox{two-row support}\\
\hbox{licensed boundary face} & \hbox{Einstein row selection}\\
\hbox{outside source point} & \hbox{inconsistent source/row model}\\
\hbox{unlicensed source} & \hbox{answer-fitting, reject route}.
\end{array}
}
$$

## 14. Current-Corpus Licensed Source Audit

Now execute Algorithm 13.6 with the sources actually visible in the current
V4 corpus.

### Definition 14.1: Candidate Source Classes

The current corpus suggests the following possible finite source observables:

$$
\boxed{
\begin{array}{ll}
\mathrm{S1}:&H=\ell\hbox{ rectangle/hypersurface records},\\[1mm]
\mathrm{S2}:&R\hbox{ boundary, source, superselection, and conditioning
records},\\[1mm]
\mathrm{S3}:&\hbox{metric, gauge, charge, flux, and quotient records},\\[1mm]
\mathrm{S4}:&O\hbox{ write-register/instrument outcome records},\\[1mm]
\mathrm{S5}:&\eta^{NN,K}_{a,ij}\hbox{ residual row-defect records},\\[1mm]
\mathrm{S6}:&\hbox{Bianchi, closure, hypersurface, and Ward defect records},\\[1mm]
\mathrm{S7}:&U\hbox{ or }1_{\{U=u_b\}}\hbox{ row-label observables}.
\end{array}
}
$$

The question is not whether these are meaningful words.  The question is
whether any of them is a licensed source observable that separates the live
rows before the actual support signs are queried.

### Audit 14.2: Rectangle/Hypersurface Records Are Licensed But Row-Blind

The live problem is already conditioned on:

$$
\boxed{
H(q_b)=\ell,\qquad b=0,1.
}
$$

Therefore every source observable that factors only through \(H\) satisfies:

$$
\boxed{
F(H(q_0))=F(H(q_1))=F(\ell).
}
$$

Such observables pass the license filter as finite records, but they are
row-blind:

$$
\boxed{
\mathrm{S1}\in{\mathsf Src}_{lic}(R)
\quad\hbox{but}\quad
\mathrm{S1}\hbox{ is row-blind.}
}
$$

They cannot yield Einstein singleton selection in the live fiber.

### Audit 14.3: Boundary And Conditioning Records Are Licensed But Row-Blind

Boundary, source, and superselection data are part of the declared
conditioning \(R\).  Inside one conditioned problem, they are fixed:

$$
\boxed{
R(q_0)=R(q_1)=R.
}
$$

If changing \(U\) changes \(R\), then \(u_0,u_1\) were not two rows of the
same conditioned support problem.  If \(R\) is genuinely shared, every
observable factoring through \(R\) is row-blind:

$$
\boxed{
\mathrm{S2}\in{\mathsf Src}_{lic}(R)
\quad\hbox{but}\quad
\mathrm{S2}\hbox{ is row-blind on the live fiber.}
}
$$

### Audit 14.4: Metric/Gauge/Charge/Quotient Records Are Not Printed As Row-Separating

Metric, gauge, charge, flux, and quotient records can be licensed finite
sources if they are declared in \(R\) or in the finite total-record grammar.
But the current corpus does not print a live table:

$$
\boxed{
F^{geom/gauge/quot}(q_0),
\qquad
F^{geom/gauge/quot}(q_1).
}
$$

Therefore the current status is:

$$
\boxed{
\mathrm{S3}\hbox{ is licensed only where declared, but no row-separating
S3 table is printed.}
}
$$

If these records are part of the fixed \(H,R\) data, they are row-blind.  If
they depend on \(U\), the corpus must print the finite row table before they
can enter \({\mathcal F}_*\).

Current-corpus verdict:

$$
\boxed{
\mathrm{S3\text{-}ROW\text{-}SEPARATION}^{cur}
\quad\hbox{not proved.}
}
$$

### Audit 14.5: Instrument Outcomes Are Readouts, Not Base Sources

The write-register outcome \(O\) is a licensed operational record after the
instrument is attached.  Paper 16 proves:

$$
\boxed{
\mathbb P^{wr}(H=\ell,U=u,O=o)
=
D(o\mid u)\,\mathbb P^{act}(H=\ell,U=u).
}
$$

Thus \(O\) can reveal base support but cannot source base support.

As a source for the pre-instrument actual law, \(O\) fails the license filter:

$$
\boxed{
O\notin{\mathsf Src}_{lic}^{base}(R)
}
$$

unless \(O\) is already part of the declared conditioning data.  If \(O\) is
declared as a row-writing detector outcome, then it is a physical readout of
\(U\), not an explanation for why the pre-instrument law put mass on \(U\).

Therefore:

$$
\boxed{
\mathrm{S4}\hbox{ is a support microscope, not a minimal base source.}
}
$$

### Audit 14.6: Residual Row Defect Is The Best Candidate But Fails Current License

The residual row defect

$$
\boxed{
\eta^{NN,K}_{a,ij}
}
$$

would be an excellent source observable if two facts were proved:

$$
\boxed{
\begin{array}{ll}
\mathrm{ACT}:&\eta^{NN,K}_{a,ij}\hbox{ is finite actual record data},\\[1mm]
\mathrm{TAB}:&\eta(q_0),\eta(q_1)\hbox{ are printed on the live rows}.
\end{array}
}
$$

But the current corpus does not prove either residual actuality or the live
two-row residual table.  Therefore:

$$
\boxed{
\mathrm{S5}\notin{\mathsf Src}_{lic}^{cur}(R)
\quad\hbox{as a row-separating source.}
}
$$

It remains a high-value target:

$$
\boxed{
\mathrm{V4P17\text{-}RESIDUAL\text{-}SOURCE\text{-}LICENSE}
}
$$

but not a current-corpus source-table entry.

### Audit 14.7: Bianchi/Closure/Hyp/Ward Defects Are Hard Candidates, Not Printed Sources

Bianchi, closure, hypersurface, and Ward defects could support either a hard
constraint route or a source-simplex route if they were finite actual
records:

$$
\boxed{
F^{def}(q)
=
(C^{Bianchi}(q),C^{hyp}(q),C^{Ward}(q),\ldots).
}
$$

But the current corpus does not print:

$$
\boxed{
F^{def}(q_0),\qquad F^{def}(q_1).
}
$$

Nor does it prove that these defects are licensed source observables rather
than uncomputed consistency conditions.

Thus:

$$
\boxed{
\mathrm{S6\text{-}SOURCE\text{-}TABLE}^{cur}
\quad\hbox{not proved.}
}
$$

The live Bianchi/closure route remains plausible, but it is not currently a
minimal source table.

### Audit 14.8: Row Labels And Row Indicators Fail Unless They Are Physical Records

The row label \(U\) and indicators \(1_{\{U=u_b\}}\) separate the rows
tautologically:

$$
\boxed{
1_{\{U=u_0\}}(q_0)=1,
\qquad
1_{\{U=u_0\}}(q_1)=0.
}
$$

But this is exactly the source-selector trap.  Unless \(U\) is itself a
declared physical source record in \(R\), using \(U\) as a source observable
fits the answer:

$$
\boxed{
\mathrm{S7}\hbox{ fails }\mathrm{L5}.
}
$$

If \(U\) is included in \(R\), then the problem has changed from computing
\(\mathbb P(U\mid H)\) to conditioning on \(U\), and the two-row support
question disappears.

### Theorem 14.9: Current-Corpus Minimal Source Audit Result

In the current corpus, no licensed row-separating minimal source table is
printed for the live \(u_0,u_1\) fiber:

$$
\boxed{
\mathrm{V4P17\text{-}LICENSED\text{-}MINIMAL\text{-}SOURCE\text{-}TABLE}^{cur}
\quad\hbox{not proved.}
}
$$

More sharply, the visible source classes have the following status:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{class} & \hbox{license status} & \hbox{row status}\\ \hline
\mathrm{S1} & \hbox{licensed} & \hbox{row-blind}\\
\mathrm{S2} & \hbox{licensed} & \hbox{row-blind}\\
\mathrm{S3} & \hbox{conditional license} & \hbox{no row table printed}\\
\mathrm{S4} & \hbox{post-base readout} & \hbox{not base source}\\
\mathrm{S5} & \hbox{actuality unsourced} & \hbox{no row table printed}\\
\mathrm{S6} & \hbox{source status unsourced} & \hbox{no row table printed}\\
\mathrm{S7} & \hbox{row-selector trap} & \hbox{reject unless physical record}.
\end{array}
}
$$

Proof.  Audits 14.2 through 14.8 exhaust the current visible source classes
from Papers 14 through 16 and the earlier Paper-17 source-simplex route.
None supplies a licensed row-separating finite source table.  `square`

### Corollary 14.10: What This Does And Does Not Prove

This audit does prove:

$$
\boxed{
\hbox{Einstein-Jaynes has no current-corpus singleton-selection source.}
}
$$

It does not yet prove:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

For that, two additional finite facts are still needed:

$$
\boxed{
\begin{array}{ll}
\mathrm{HS}:&\hbox{both row fibers are hard-allowed and reference-positive},\\[1mm]
\mathrm{EJ}:&\hbox{the actual law obeys the Einstein-Jaynes principle, or an
equivalent full-support law}.
\end{array}
}
$$

Conditional consequence:

$$
\boxed{
\mathrm{HS}+\mathrm{EJ}+\hbox{current source audit}
\quad\Longrightarrow\quad
\widehat m_0>0,\ \widehat m_1>0.
}
$$

### Next Primitive 14.11

The route-2 attack therefore ends with a sharper fork:

$$
\boxed{
\begin{array}{ll}
\mathrm{A}:&\hbox{prove hard-status }(\rho_0,\rho_1>0,\ C_0=C_1=0),\\[1mm]
\mathrm{B}:&\hbox{prove Einstein-Jaynes finite actual-law naturality},\\[1mm]
\mathrm{C}:&\hbox{license a currently unsourced separating source }
(\eta,\hbox{ Bianchi, closure, Ward}),\\[1mm]
\mathrm{D}:&\hbox{print a hard row-separating constraint directly}.
\end{array}
}
$$

This is a real advance.  The source-simplex route no longer floats as an
abstract possibility: with currently licensed sources, it does not select a
single row.  The only remaining singleton routes must license a new
row-sensitive source or hard constraint.

## 15. Finite Least-Bias Uniqueness Theorem

We now try the strongest Einstein route: prove that finite least-bias updating
is not an arbitrary preference but the unique update rule satisfying natural
finite consistency axioms.

The theorem below does not prove that the actual ISP law obeys least bias.
It proves the mathematical uniqueness claim:

$$
\boxed{
\hbox{if the actual law is obtained by a finite least-bias update, then the
update is relative-entropy minimization.}
}
$$

### Definition 15.1: Finite Update Problem

Let \(K\) be a finite hard-allowed record set.  Let

$$
\boxed{
\rho_i>0,\qquad i\in K,\qquad \sum_{i\in K}\rho_i=1
}
$$

be the reference law on \(K\).  Let \({\mathcal M}\) be a nonempty convex set
of candidate posterior laws on \(K\), typically defined by licensed finite
source constraints:

$$
\boxed{
\sum_{i\in K}P_iF_r(i)=f_r.
}
$$

An update rule chooses one \(P^*\in{\mathcal M}\).

### Definition 15.2: Finite Least-Bias Axioms

A least-bias update rule is represented by minimizing a differentiable
strictly convex functional

$$
\boxed{
\Phi(P,\rho)
}
$$

over \({\mathcal M}\), with the following finite consistency axioms.

1. **Locality.** If constraints do not distinguish states in a block, the
   update does not change their internal ratios relative to \(\rho\).
2. **Coordinate invariance.** Relabeling finite records does not change the
   update.
3. **Refinement invariance.** Splitting a record into finitely many
   indistinguishable subrecords does not change the coarse-grained update.
4. **Subsystem independence.** If \(K=A\times B\), \(\rho=\rho^A\rho^B\),
   and the constraints on \(A\) and \(B\) are independent, then updating
   jointly or separately gives the same product posterior.
5. **No hidden source.** The functional depends only on \((P,\rho)\), not on
   row labels or undeclared variables.
6. **Strict preference.** If the feasible set has an interior, the minimizer
   is unique.

These are the finite version of "change only what the declared information
requires."

### Lemma 15.3: Locality And Refinement Force Trace Form

Under locality, coordinate invariance, and refinement invariance, the
ranking functional has the trace form

$$
\boxed{
\Phi(P,\rho)
=
\sum_{i\in K}\rho_i h\!\left({P_i\over\rho_i}\right)
}
$$

for a differentiable strictly convex function \(h:(0,\infty)\to{\mathbb R}\),
up to additive and positive multiplicative constants.

Proof.  Locality implies additivity over disjoint blocks: changing
constraints in one block cannot change the contribution of another block.
Coordinate invariance makes the same scalar contribution apply to every
record label.  Refinement invariance says that the contribution of a
coarse state with reference weight \(\rho_i\) and posterior weight \(P_i\)
depends only on the likelihood ratio \(P_i/\rho_i\) and is weighted by
\(\rho_i\).  Therefore the functional has the stated trace form.  Strict
preference gives strict convexity of \(h\).  `square`

### Lemma 15.4: Subsystem Independence Forces The Logarithm

Let

$$
\boxed{
\Phi(P,\rho)
=
\sum_i\rho_i h(P_i/\rho_i)
}
$$

be a differentiable trace-form least-bias functional.  If independent
subsystem updating is consistent for arbitrary finite product systems, then

$$
\boxed{
h(t)=a\,t\log t+b\,t+c
}
$$

with \(a>0\).

Proof.  Let \(K=A\times B\), with

$$
\boxed{
\rho_{ij}=\rho^A_i\rho^B_j,\qquad
P_{ij}=P^A_iP^B_j.
}
$$

Write

$$
\boxed{
x_i={P^A_i\over\rho^A_i},
\qquad
y_j={P^B_j\over\rho^B_j}.
}
$$

For independent constraints, the joint stationarity equations must separate
into an \(A\)-part and a \(B\)-part.  The derivative of the joint trace
functional contributes

$$
\boxed{
h'(x_i y_j).
}
$$

Separability for arbitrary finite independent constraints requires

$$
\boxed{
h'(xy)=A(x)+B(y)
}
$$

for all positive \(x,y\) in an interval.  Symmetry between subsystems and
normalization constants reduce this to the multiplicative Cauchy equation

$$
\boxed{
h'(xy)=h'(x)+h'(y)-h'(1).
}
$$

Differentiability gives

$$
\boxed{
h'(t)=a\log t+b.
}
$$

Integrating,

$$
\boxed{
h(t)=a\,t\log t+(b-a)t+c.
}
$$

Renaming constants gives the stated form.  Strict convexity requires
\(a>0\).  `square`

### Theorem 15.5: Finite Least-Bias Uniqueness

Any finite least-bias update rule satisfying the axioms of Definition 15.2
selects the unique minimizer of relative entropy:

$$
\boxed{
P^*
=
\arg\min_{P\in{\mathcal M}}
D(P\Vert\rho),
}
$$

where

$$
\boxed{
D(P\Vert\rho)
=
\sum_{i\in K}P_i\log {P_i\over\rho_i}.
}
$$

Proof.  By Lemma 15.3, the functional has trace form.  By Lemma 15.4, the
only trace form compatible with subsystem independence is
\(\sum_i\rho_i(a(P_i/\rho_i)\log(P_i/\rho_i)+b(P_i/\rho_i)+c)\).  The
linear term \(\sum_i bP_i\) and constant term \(\sum_i c\rho_i\) do not
affect minimization over normalized laws.  Since \(a>0\), minimizing
\(\Phi\) is equivalent to minimizing \(D(P\Vert\rho)\).  Strict convexity
gives uniqueness on convex feasible sets with interior.  `square`

### Corollary 15.6: Exponential Law From Least Bias

If \({\mathcal M}\) is defined by finite source constraints

$$
\boxed{
\sum_iP_iF_r(i)=f_r,
\qquad r=1,\ldots,m,
}
$$

and has a full-support feasible point, then the least-bias posterior is

$$
\boxed{
P^*_i
=
{1\over Z(\lambda)}
\rho_i
\exp\left\{-\sum_{r=1}^m\lambda_rF_r(i)\right\}.
}
$$

On the original total-record space, with hard constraint \(K=\{C=0\}\),

$$
\boxed{
P^*(q\mid R)
=
{1\over Z(\lambda;R)}
\rho(q\mid R)
\exp\left\{-\sum_r\lambda_rF_r(q)\right\}
1_{\{C(q\mid R)=0\}}.
}
$$

Thus the GR/SM ansatz is derived from finite least bias once the reference
law, hard surface, and licensed source constraints are declared.

### Corollary 15.7: Least Bias Gives Full Support On Interior Feasible Faces

If \(\rho_i>0\) on \(K\), and the feasible source constraints admit a
full-support point on a face \(G\subseteq K\), then the least-bias posterior
has positive support exactly on that face:

$$
\boxed{
P^*_i>0
\quad\Longleftrightarrow\quad
i\in G.
}
$$

In particular, if the feasible point is interior in all of \(K\), then

$$
\boxed{
P^*_i>0\quad\hbox{for every }i\in K.
}
$$

Exact zeros arise only from hard exclusion, reference zeros, or source
boundary faces.

### No-Go 15.8: Least-Bias Uniqueness Does Not Prove The Actual Law Obeys Least Bias

Theorem 15.5 is a uniqueness theorem for a class of update rules.  It does
not by itself prove:

$$
\boxed{
\mathbb P^{act}
=
\arg\min_{P\in{\mathcal M}}D(P\Vert\rho).
}
$$

That is a bridge principle:

$$
\boxed{
\mathrm{V4P17\text{-}ACTUAL\text{-}LAW\text{-}OBEYS\text{-}LEAST\text{-}BIAS}.
}
$$

Without this bridge, one can define another finite law on the same hard
surface that violates least bias while still being a valid probability law.
For example, on two hard-allowed rows:

$$
\boxed{
P(q_0)=0.99,\qquad P(q_1)=0.01
}
$$

is a finite law, but it is not derived unless the source constraints or
reference law license that asymmetry.

### Audit 15.9: Does The Current Corpus Prove The Bridge?

The current corpus supplies:

1. finite total-record discipline;
2. finite operational detectors;
3. finite hard-constraint candidates;
4. finite residual and geometry source candidates;
5. the GR/SM-inspired hard/soft support logic.

But it does not prove that the actual law is selected by least-bias updating.
Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}ACTUAL\text{-}LAW\text{-}OBEYS\text{-}LEAST\text{-}BIAS}^{cur}
\quad\hbox{not proved.}
}
$$

### Theorem 15.10: Conditional Closure Of The Unsourced Law Problem

Assume:

1. the hard support surface \(K=\{C=0\}\) is licensed;
2. the reference law \(\rho\) is licensed and positive on the live hard
   rows;
3. the licensed source constraints define a feasible convex set
   \({\mathcal M}\);
4. the actual law obeys finite least-bias updating:

$$
\boxed{
\mathbb P^{act}
=
\arg\min_{P\in{\mathcal M}}D(P\Vert\rho);
}
$$

5. the live source point is interior with respect to both live row fibers.

Then:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

If the live source point lies on a licensed row-selecting boundary face, then
least bias gives licensed Einstein singleton selection.

Proof.  By Theorem 15.5 and Corollary 15.6, the actual law has the GR/SM
exponential support form.  By Corollary 15.7, support is positive exactly on
the hard-allowed feasible source face.  Interior source position meeting both
row fibers gives positive mass to both rows; a licensed boundary face meeting
only one row gives singleton support.  `square`

### Final Verdict 15.11

The Einstein route succeeds mathematically:

$$
\boxed{
\mathrm{V4P17\text{-}FINITE\text{-}LEAST\text{-}BIAS\text{-}UNIQUENESS}
\quad\hbox{is proved.}
}
$$

It does not yet succeed as a current-corpus physical derivation:

$$
\boxed{
\mathrm{V4P17\text{-}ACTUAL\text{-}LAW\text{-}OBEYS\text{-}LEAST\text{-}BIAS}^{cur}
\quad\hbox{not proved.}
}
$$

So the unsourced law problem is now reduced to one bridge:

$$
\boxed{
\hbox{why is the actual finite total-record law the least-biased law
compatible with licensed hard constraints and source records?}
}
$$

If that bridge is adopted as the V4 actual-law principle, the GR/SM ansatz is
not guessed; it is derived.  If the bridge is rejected, the corpus must
instead print a concrete actual law, a row-separating hard constraint, or a
residual/Bianchi/Ward source license.

## 16. Finite No-Unrecorded-Distinction Principle

The least-bias bridge can be stated in more ISP-native language:

$$
\boxed{
\hbox{the actual law may not distinguish finite records except by licensed
finite record facts.}
}
$$

This is the finite analogue of Einstein's move.  Do not ask for a preferred
coordinate or hidden selector.  Ask what is actually recorded.  If no
licensed record distinguishes two possibilities, the actual law must not
smuggle in an extra distinction.

### Principle 16.1: No Unrecorded Distinction

Fix a hard-allowed record set \(K\), a positive reference law \(\rho\), and
a licensed source algebra \({\mathcal F}=(F_1,\ldots,F_m)\).  Define the
licensed profile map

$$
\boxed{
\Pi(q)
=
\big(F_1(q),\ldots,F_m(q),C(q),[q]_{quot}\big).
}
$$

Two hard-allowed records are licensed-indistinguishable if

$$
\boxed{
\Pi(q)=\Pi(q').
}
$$

The no-unrecorded-distinction principle says:

$$
\boxed{
\Pi(q)=\Pi(q')
\quad\Longrightarrow\quad
{P^{act}(q\mid R)\over \rho(q\mid R)}
=
{P^{act}(q'\mid R)\over \rho(q'\mid R)}.
}
$$

Thus the posterior/reference ratio may vary only with licensed record
profiles.

### Theorem 16.2: No-Unrecorded-Distinction Implies Blockwise Least Bias

Let the licensed profile partition \(K\) into blocks

$$
\boxed{
K=\bigsqcup_{\gamma}K_\gamma,
\qquad
K_\gamma=\{q:\Pi(q)=\gamma\}.
}
$$

If no-unrecorded-distinction holds, then there are constants \(w_\gamma\ge0\)
such that

$$
\boxed{
P^{act}(q\mid R)=w_\gamma\,\rho(q\mid R),
\qquad q\in K_\gamma.
}
$$

The actual law is therefore completely determined by the block weights
\((w_\gamma)\).

Proof.  Inside a block, all records have the same licensed profile.  By
Principle 16.1, the ratio \(P^{act}(q\mid R)/\rho(q\mid R)\) is constant
inside that block.  Call the constant \(w_\gamma\).  `square`

### Corollary 16.3: Two-Row No-Distinction Test

For the live atomized two-row fiber, if

$$
\boxed{
\Pi(q_0)=\Pi(q_1),
\qquad
\rho(q_0\mid R),\rho(q_1\mid R)>0,
}
$$

then

$$
\boxed{
{P^{act}(q_0\mid R)\over \rho(q_0\mid R)}
=
{P^{act}(q_1\mid R)\over \rho(q_1\mid R)}.
}
$$

If additionally

$$
\boxed{
\rho(q_0\mid R)=\rho(q_1\mid R),
}
$$

then

$$
\boxed{
P^{act}(q_0\mid R)=P^{act}(q_1\mid R)>0.
}
$$

This is Feynman's tiny test: if all licensed records see the two rows as the
same, a skewed split such as \(0.99/0.01\) is forbidden unless \(\rho\)
already licenses that asymmetry.

### Theorem 16.4: No-Distinction Plus Source Constraints Gives Exponential Form

Assume:

1. no-unrecorded-distinction holds at every finite source refinement;
2. independent product source systems compose by product updating;
3. source constraints are linear expectations of licensed observables;
4. the feasible set has an interior point.

Then the actual law is the finite least-bias law:

$$
\boxed{
P^{act}
=
\arg\min_{P\in{\mathcal M}}D(P\Vert\rho).
}
$$

Therefore it has the GR/SM exponential form:

$$
\boxed{
P^{act}(q\mid R)
=
{1\over Z(\lambda;R)}
\rho(q\mid R)
\exp\left\{-\sum_r\lambda_rF_r(q)\right\}
1_{\{C(q\mid R)=0\}}.
}
$$

Proof.  No-unrecorded-distinction gives the locality/no hidden source part
of Definition 15.2: within any block not distinguished by licensed data, the
posterior/reference ratio is constant.  Requiring the same principle to hold
under finite refinements gives refinement invariance.  Relabeling
indistinguishable records gives coordinate invariance.  Product composition
is subsystem independence.  With strict interior feasibility, the hypotheses
of Theorem 15.5 hold, so the unique update is relative-entropy minimization.
Corollary 15.6 gives the exponential form.  `square`

### No-Go 16.5: No-Distinction Alone Is Not Enough Across Distinguished Blocks

No-unrecorded-distinction by itself does not determine weights between
different licensed profiles.  If

$$
\boxed{
\Pi(q_0)\ne\Pi(q_1),
}
$$

then the principle allows

$$
\boxed{
{P(q_0)\over\rho(q_0)}
\ne
{P(q_1)\over\rho(q_1)}.
}
$$

The relative weights must then come from licensed source values, product
composition, and the least-bias update theorem.  Thus:

$$
\boxed{
\hbox{no-distinction closes equal-profile rows; least-bias closes the
licensed-profile weighting problem.}
}
$$

### Audit 16.6: Current-Corpus Status Of No-Unrecorded-Distinction

The current corpus has not stated no-unrecorded-distinction as an axiom or
derived it from prior ISP principles.  Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}NO\text{-}UNRECORDED\text{-}DISTINCTION}^{cur}
\quad\hbox{not proved.}
}
$$

But it is now the cleanest candidate bridge because it is native to finite
record ontology:

$$
\boxed{
\hbox{unrecorded distinctions are not physical distinctions.}
}
$$

### Conditional Closure 16.7

Assume:

1. the no-unrecorded-distinction principle;
2. finite refinement and product consistency;
3. hard-status for both live rows;
4. licensed source-interior for the live source point.

Then:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

If instead the licensed source point lies on a row-selecting boundary face,
then the same principle gives licensed Einstein selection.

Proof.  By Theorem 16.4, the actual law is the least-bias exponential law.
By Corollary 15.7 and the source-simplex theorem, interior source position
gives support on both row fibers, while a licensed boundary face selects
exactly the rows whose source images meet the face.  `square`

### Final Verdict 16.8

Einstein's bridge can now be stated without entropy language:

$$
\boxed{
\hbox{the actual law contains no distinctions not made by finite records.}
}
$$

Feynman's test is:

$$
\boxed{
\Pi(q_0)=\Pi(q_1)
\quad ?
}
$$

If yes, then the posterior/reference ratio must be equal on the two rows.  If
no, the difference must be visible in the licensed source-simplex table.

The remaining unsourced-law problem is therefore:

$$
\boxed{
\hbox{prove or adopt no-unrecorded-distinction as a finite ISP principle.}
}
$$

Once adopted with refinement and product consistency, the least-bias theorem
and the GR/SM support ansatz follow.

## 17. Profile Automorphism Or Source

The no-unrecorded-distinction principle can be made still more concrete.
Instead of asking abstractly whether two records have the same profile, ask
whether the finite record space has a symmetry that swaps them while
preserving every licensed fact.

### Definition 17.1: Licensed-Profile Automorphism

Let \(K=\{q:C(q)=0\}\) be the hard-allowed finite record set.  A licensed
profile automorphism is a bijection

$$
\boxed{
\sigma:K\to K
}
$$

such that for every \(q\in K\):

$$
\boxed{
\Pi(\sigma q)=\Pi(q),
\qquad
\rho(\sigma q\mid R)=\rho(q\mid R).
}
$$

If \(\rho\) is not strictly invariant but is a density under the relabeling,
the invariant object is the posterior/reference ratio:

$$
\boxed{
{P(\sigma q\mid R)\over\rho(\sigma q\mid R)}
=
{P(q\mid R)\over\rho(q\mid R)}.
}
$$

### Principle 17.2: Finite Record Covariance

The actual law is finite-record covariant if every licensed-profile
automorphism preserves the actual law:

$$
\boxed{
P^{act}(\sigma q\mid R)=P^{act}(q\mid R)
}
$$

when \(\rho\) is invariant, or preserves the posterior/reference ratio in
the density version:

$$
\boxed{
{P^{act}(\sigma q\mid R)\over\rho(\sigma q\mid R)}
=
{P^{act}(q\mid R)\over\rho(q\mid R)}.
}
$$

This is the finite-record version of covariance: relabeling records without
changing any licensed fact cannot change physical probabilities.

### Theorem 17.3: Profile Automorphism Implies No-Unrecorded-Distinction On Orbits

Assume finite record covariance.  If \(q,q'\in K\) lie in the same orbit of
the licensed-profile automorphism group, then

$$
\boxed{
{P^{act}(q\mid R)\over\rho(q\mid R)}
=
{P^{act}(q'\mid R)\over\rho(q'\mid R)}.
}
$$

In particular, if the automorphism group acts transitively on each licensed
profile block \(K_\gamma\), then finite record covariance implies
no-unrecorded-distinction.

Proof.  If \(q'\) lies in the orbit of \(q\), then \(q'=\sigma q\) for some
licensed-profile automorphism \(\sigma\).  Covariance gives invariance of
the posterior/reference ratio.  If the group is transitive on each profile
block, every pair in the block is connected by such a \(\sigma\), so the
ratio is constant on the block.  This is Principle 16.1.  `square`

### Corollary 17.4: Feynman Swap Test

For the live two-row atomized problem, suppose there exists a licensed
profile automorphism \(\sigma\) with

$$
\boxed{
\sigma q_0=q_1,\qquad \sigma q_1=q_0.
}
$$

Then

$$
\boxed{
{P^{act}(q_0\mid R)\over\rho(q_0\mid R)}
=
{P^{act}(q_1\mid R)\over\rho(q_1\mid R)}.
}
$$

If additionally \(\rho(q_0\mid R)=\rho(q_1\mid R)\), then

$$
\boxed{
P^{act}(q_0\mid R)=P^{act}(q_1\mid R).
}
$$

Thus a finite swap map is a direct Feynman certificate for no hidden
row-bias.

### Definition 17.5: Swap Obstruction Classes

If no such \(\sigma\) exists, the obstruction must be classified as one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{O1}:&\hbox{licensed source obstruction }{\mathcal F}(q_0)\ne
{\mathcal F}(q_1),\\[1mm]
\mathrm{O2}:&\hbox{hard constraint obstruction }C(q_0)\ne C(q_1),\\[1mm]
\mathrm{O3}:&\hbox{reference obstruction }\rho(q_0)\ne\rho(q_1),\\[1mm]
\mathrm{O4}:&\hbox{quotient/gauge obstruction }[q_0]_{quot}\ne[q_1]_{quot},\\[1mm]
\mathrm{O5}:&\hbox{row-selector obstruction using }U\hbox{ only},\\[1mm]
\mathrm{O6}:&\hbox{unsourced obstruction }(\eta,\hbox{ Bianchi, Ward, etc.}).
\end{array}
}
$$

Only \(\mathrm{O1}\)-\(\mathrm{O4}\) are licensed physical reasons.  \(\mathrm
{O5}\) is answer-fitting unless \(U\) is already an actual conditioning
record.  \(\mathrm{O6}\) becomes the next primitive to source.

### Theorem 17.6: Profile-Automorphism-Or-Source Decision

For the live two-row problem, exactly one of the following useful outcomes
must be printed by a successful proof attempt:

1. **Swap.** A licensed profile automorphism \(\sigma\) swaps \(q_0,q_1\).
   Then the posterior/reference ratios are equal.
2. **Licensed source.** The swap fails because of a licensed source,
   constraint, reference, or quotient obstruction.  Then the source-simplex
   or hard-constraint route must decide support.
3. **Selector trap.** The swap fails only because of the row label \(U\).
   Then the obstruction is rejected as answer-fitting.
4. **Unsourced obstruction.** The swap fails because of residual,
   Bianchi/closure, Ward, or another unlicensed defect.  Then that defect is
   promoted to the next primitive source-license target.

Proof.  Any failure of a profile-preserving bijection must be caused by
failure to preserve one of the finite ingredients in the profile or
reference data.  The listed obstruction classes exhaust those ingredients:
licensed source values, hard constraints, reference weights, quotient data,
row labels, or unsourced candidate defects.  `square`

### Current-Corpus Status 17.7

The current corpus has not printed a swap automorphism

$$
\boxed{
\sigma q_0=q_1
}
$$

for the live two-row fiber.  It also has not printed a licensed obstruction
from \(\mathrm{O1}\)-\(\mathrm{O4}\).  Therefore:

$$
\boxed{
\mathrm{V4P17\text{-}PROFILE\text{-}AUTOMORPHISM\text{-}OR\text{-}SOURCE}^{cur}
\quad\hbox{not proved.}
}
$$

But the test is now exact.  The next proof attempt must print either the
swap, the licensed source obstruction, the selector trap, or the unsourced
primitive obstruction.

### Final Verdict 17.8

Einstein's route:

$$
\boxed{
\hbox{finite record covariance under licensed-profile automorphisms.}
}
$$

Feynman's concrete test:

$$
\boxed{
\hbox{construct the swap }\sigma:q_0\leftrightarrow q_1
\hbox{ or print what blocks it.}
}
$$

This is the cleanest operational form of the bridge:

$$
\boxed{
\mathrm{V4P17\text{-}PROFILE\text{-}AUTOMORPHISM\text{-}OR\text{-}SOURCE}.
}
$$

If the swap exists, no-unrecorded-distinction holds for the live pair.  If
the swap fails, the failure must become a licensed source, a hard constraint,
or a named unsourced primitive.

## 18. Complete Licensed Structure: Orbit Or Separator

The previous section still leaves a loophole:

$$
\boxed{
\hbox{what exactly counts as the licensed profile?}
}
$$

If the profile is too small, two rows may look equal even though the finite
record structure distinguishes them relationally.  If the profile is too
large, it can smuggle in the answer.  The disciplined resolution is to stop
using a scalar profile and use the complete finite licensed structure.

### Definition 18.1: Complete Licensed Finite Record Structure

For a fixed finite conditioning record \(R\), define the licensed structure

$$
\boxed{
{\mathfrak L}_R
=
\left(
K,\rho,
\{C_a\}_{a\in A_C},
\{F_b\}_{b\in A_F},
\{G_c\}_{c\in A_G},
\{S_d\}_{d\in A_S}
\right).
}
$$

Here:

1. \(K\) is the hard-allowed finite candidate set.
2. \(\rho:K\to(0,\infty)\) is the reference density.
3. \(C_a\) are hard constraint predicates or functions.
4. \(F_b\) are licensed source observables.
5. \(G_c\) are gauge/quotient/incidence/geometry relations.
6. \(S_d\) are selector relations that are actual conditioning records, not
   merely the queried row label.

Every item in \({\mathfrak L}_R\) must pass the license audit: it must be
part of the finite record, fixed boundary data, hard constraint data,
reference data, or explicitly conditioned source data.  If a proposed datum
cannot pass that audit, it is not allowed inside \({\mathfrak L}_R\).

### Definition 18.2: Automorphism Group Of The Licensed Structure

The licensed automorphism group is

$$
\boxed{
\mathrm{Aut}({\mathfrak L}_R)
=
\left\{
\sigma:K\to K:
\sigma\hbox{ is a bijection preserving every component of }
{\mathfrak L}_R
\right\}.
}
$$

Explicitly, \(\sigma\) must preserve:

$$
\boxed{
\rho,\quad C_a,\quad F_b,\quad G_c,\quad S_d
}
$$

for every licensed component.  The orbits are

$$
\boxed{
[q]_{\mathfrak L}
=
\{\sigma q:\sigma\in\mathrm{Aut}({\mathfrak L}_R)\}.
}
$$

The quotient

$$
\boxed{
K/{\mathrm{Aut}({\mathfrak L}_R)}
}
$$

is the exact finite space of licensed row-types.

### Principle 18.3: Finite Presentation Invariance

The actual law is a law of finite records, not a law of arbitrary names used
to present those records.  Therefore, if two presentations of the same
licensed finite record differ only by an automorphism of \({\mathfrak L}_R\),
the actual posterior/reference ratio is invariant:

$$
\boxed{
{P^{act}(\sigma q\mid R)\over\rho(\sigma q\mid R)}
=
{P^{act}(q\mid R)\over\rho(q\mid R)}
\qquad
\forall \sigma\in\mathrm{Aut}({\mathfrak L}_R).
}
$$

This is the Einstein route in its cleanest finite form.  It is not an
entropy assumption.  It is label-erasure: unlicensed names are not physical
arguments of the actual law.

### Theorem 18.4: Same Orbit Implies Same Actual Support

Assume finite presentation invariance.  If

$$
\boxed{
q_1\in[q_0]_{\mathfrak L},
}
$$

then

$$
\boxed{
{P^{act}(q_1\mid R)\over\rho(q_1\mid R)}
=
{P^{act}(q_0\mid R)\over\rho(q_0\mid R)}.
}
$$

In particular, since \(\rho>0\) on \(K\),

$$
\boxed{
P^{act}(q_0\mid R)>0
\quad\Longleftrightarrow\quad
P^{act}(q_1\mid R)>0.
}
$$

Proof.  If \(q_1\in[q_0]_{\mathfrak L}\), then \(q_1=\sigma q_0\) for some
\(\sigma\in\mathrm{Aut}({\mathfrak L}_R)\).  Principle 18.3 gives equality
of posterior/reference ratios.  Since \(\rho\) is strictly positive on the
hard-allowed set, positivity of \(P^{act}\) is equivalent on the two rows.
`square`

### Theorem 18.5: Finite Orbit-Or-Separator Dichotomy

For any two rows \(q_0,q_1\in K\), exactly one of the following holds:

1. **Orbit case.**

   $$
   \boxed{
   q_1\in[q_0]_{\mathfrak L}.
   }
   $$

   Then Theorem 18.4 proves identical actual support status.

2. **Separator case.**

   There exists a finite structural relational separator

   $$
   \boxed{
   \Theta(x;{\mathfrak L}_R)
   }
   $$

   built from the licensed components of \({\mathfrak L}_R\), such that

   $$
   \boxed{
   \Theta(q_0;{\mathfrak L}_R)\ne
   \Theta(q_1;{\mathfrak L}_R).
   }
   $$

Proof.  If \(q_0,q_1\) are in the same automorphism orbit, we are in case
1.  Otherwise, their orbits in the finite quotient
\(K/\mathrm{Aut}({\mathfrak L}_R)\) are distinct.  The characteristic
function of the orbit \([q_0]_{\mathfrak L}\) is invariant under
\(\mathrm{Aut}({\mathfrak L}_R)\), depends only on the licensed finite
structure, and separates \(q_0\) from \(q_1\).  Because \(K\) is finite, this
separator can be represented by a finite parameter-free formula over the
licensed vocabulary, possibly using the whole finite relational diagram.
Thus a finite structural separator exists.  Whether that separator is a
usable physical source is the additional license audit in Discipline 18.6.
`square`

### Important Discipline 18.6: Separators Must Be Interpretable

The separator in Theorem 18.5 is only useful for the support ansatz if it is
interpretable in the license audit.  A formally separating predicate such as

$$
\boxed{
\Theta(x)=1_{\{x=q_0\}}
}
$$

is forbidden unless \(q_0\) itself is an actual conditioning record.  The
separator must be expressible by licensed physical data:

$$
\boxed{
C,\quad F,\quad G,\quad S,\quad \rho,
}
$$

not by the analyst's chosen row name.

This is the point at which answer-fitting is killed.  A separator proves a
missing source only if it is licensed independently of the desired answer.
If the separator is a huge global relational formula, then it counts as an
\(\mathrm{L4}\) geometry/incidence separator only if those global incidences
are actual finite records, not hidden analyst scaffolding.

## 19. Closing The Equal-Structure Case

We can now state the strongest theorem currently available without guessing
the actual law value.

### Theorem 19.1: Nontautological Equal-Orbit Support Closure

Let \(q_0,q_1\in K\).  Suppose:

1. \(q_0,q_1\) are hard allowed:

   $$
   \boxed{
   q_0,q_1\in K.
   }
   $$

2. The reference density is positive on both rows:

   $$
   \boxed{
   \rho(q_0\mid R)>0,\qquad \rho(q_1\mid R)>0.
   }
   $$

3. The actual law obeys finite presentation invariance.
4. The rows are in the same licensed-structure orbit:

   $$
   \boxed{
   q_1\in[q_0]_{\mathfrak L}.
   }
   $$

Then:

$$
\boxed{
\widehat m_0>0
\quad\Longleftrightarrow\quad
\widehat m_1>0.
}
$$

If either row has positive actual support, both do.  If either row has zero
actual support, both do.

Proof.  The two rows lie in the same licensed automorphism orbit.  Theorem
18.4 gives equality of actual support status.  The quantities
\(\widehat m_0,\widehat m_1\) are row-fiber masses induced by \(P^{act}\);
therefore they vanish or remain positive orbitwise.  `square`

### Corollary 19.2: Same-Orbit Positivity From Normalization

Assume the hypotheses of Theorem 19.1 and assume the live two-row fiber is
an entire positive-mass orbit block:

$$
\boxed{
K_{\mathrm{live}}=[q_0]_{\mathfrak L}
=\{q_0,q_1\}
}
$$

with

$$
\boxed{
P^{act}(K_{\mathrm{live}}\mid R)>0.
}
$$

Then

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

Proof.  The block mass is positive and the two rows have equal
posterior/reference ratio.  Since \(\rho(q_i)>0\), neither row can have zero
actual mass unless the entire orbit has zero actual mass.  `square`

### Corollary 19.3: Same-Orbit Floor From Reference Lower Bound

If, additionally,

$$
\boxed{
\rho(q_i\mid R)\ge \rho_{\min}>0
\qquad(i=0,1)
}
$$

and

$$
\boxed{
P^{act}(K_{\mathrm{live}}\mid R)\ge M_{\min}>0,
}
$$

then

$$
\boxed{
\widehat m_i
\ge
M_{\min}
{\rho_{\min}\over \rho(q_0\mid R)+\rho(q_1\mid R)}
\qquad(i=0,1).
}
$$

This is a genuine lower-floor statement, but only inside a licensed orbit
block with positive block mass.

## 20. Feynman Algorithm: How To Print The Certificate

The Feynman version is a finite audit procedure.

### Algorithm 20.1: Two-Row Orbit/Separator Audit

Input:

$$
\boxed{
({\mathfrak L}_R,q_0,q_1).
}
$$

Steps:

1. **Build the hard set.**  Print \(K=\{q:C(q)=0\}\).
2. **Print the licensed columns.**  List every component of
   \({\mathfrak L}_R\):

   $$
   \boxed{
   \rho,\ C_a,\ F_b,\ G_c,\ S_d.
   }
   $$

3. **Delete unlicensed row labels.**  Remove any column that exists only
   because the analyst asked about row \(0\) or row \(1\).
4. **Try the swap.**  Test whether the transposition

   $$
   \boxed{
   \tau(q_0)=q_1,\qquad \tau(q_1)=q_0
   }
   $$

   extends to an automorphism of \({\mathfrak L}_R\).
5. **If yes, print the automorphism.**  This proves equal support status.
6. **If no, print the first failed licensed column.**  The failed column is
   the separator candidate.
7. **Audit the separator.**
   If the separator is licensed, it becomes the missing physical source.
   If it is only the row label, reject it.
   If it is a residual or closure defect not yet licensed, promote it to a
   primitive source theorem.

### Theorem 20.2: Algorithm 20.1 Is Complete For The Live Pair

For finite \(K\), Algorithm 20.1 terminates and returns one of:

$$
\boxed{
\hbox{automorphism certificate, licensed separator, selector trap,
or unsourced primitive.}
}
$$

Proof.  Since \(K\) is finite, the automorphism-extension problem is finite.
Either a bijection preserving all licensed relations exists or no such
bijection exists.  In the latter case, failure occurs at a finite licensed
component, an unlicensed selector, or a candidate component not yet licensed.
These are exactly the four outputs.  `square`

### Feynman Lab 20.3: Minimal Two-Row Table

The minimal table has the form:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & F & G & S_{\mathrm{actual}}\\ \hline
q_0 & C_0 & \rho_0 & F_0 & G_0 & S_0\\
q_1 & C_1 & \rho_1 & F_1 & G_1 & S_1
\end{array}
}
$$

The swap is licensed exactly when:

$$
\boxed{
C_0=C_1,\quad
\rho_0=\rho_1,\quad
F_0=F_1,\quad
G_0=G_1,\quad
S_0=S_1,
}
$$

where equality of \(G\) means equality of all licensed relational incidences,
not merely equality of a scalar summary.

If one of these equalities fails, the failed column is the only honest place
where the missing law can live.

## 21. Consequence For The GR/SM Support Ansatz

The GR/SM-inspired ansatz was introduced to supply a missing law.  The
orbit/separator theorem tells us exactly when that move is legitimate.

### Theorem 21.1: Ansatz Is Right Only If Its Separator Is Licensed

Let the proposed ansatz define a support decision

$$
\boxed{
A:K\to\{0,1\}.
}
$$

If \(A(q_0)\ne A(q_1)\), then the ansatz is non-tautologically licensed only
if there exists a licensed component of \({\mathfrak L}_R\) separating the
two rows:

$$
\boxed{
\Theta(q_0;{\mathfrak L}_R)\ne
\Theta(q_1;{\mathfrak L}_R).
}
$$

If no such separator exists and \(q_0,q_1\) are in the same licensed orbit,
then any ansatz that assigns different support status violates finite
presentation invariance.

Proof.  If \(q_0,q_1\) are in the same orbit, Theorem 19.1 forces equal
support status.  Therefore any support-asymmetric ansatz must be justified
by the separator case of Theorem 18.5.  The separator must be licensed by
Definition 18.1 and Discipline 18.6.  `square`

### Corollary 21.2: The Missing Law Has Been Localized

The missing law is not an arbitrary value.  It must be one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{L1}:&\hbox{a hard constraint separator},\\[1mm]
\mathrm{L2}:&\hbox{a reference-measure separator},\\[1mm]
\mathrm{L3}:&\hbox{a licensed source observable separator},\\[1mm]
\mathrm{L4}:&\hbox{a gauge/geometry/incidence separator},\\[1mm]
\mathrm{L5}:&\hbox{an actual conditioning-record separator},\\[1mm]
\mathrm{L6}:&\hbox{a new primitive theorem licensing a residual/closure defect}.
\end{array}
}
$$

Everything else is row-label bias.

### Current-Corpus Status 21.3

The current corpus has not yet printed the complete table:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & F & G & S_{\mathrm{actual}}\\ \hline
q_0 & ? & ? & ? & ? & ?\\
q_1 & ? & ? & ? & ? & ?
\end{array}
}
$$

Therefore the final same-law support question is not settled.  But the
problem is now finite and sharply localized:

$$
\boxed{
\hbox{print the automorphism, or print the licensed separator.}
}
$$

This is real progress because a future proof no longer needs to invent a
new philosophical bridge.  It must fill a finite table.

## 22. Revised Final Verdict

The strongest rigorous conclusion of Paper 17 is now:

$$
\boxed{
\mathrm{V4P17\text{-}ORBIT\text{-}SEPARATOR\text{-}SUPPORT\text{-}THEOREM}.
}
$$

It says:

$$
\boxed{
\begin{array}{c}
\hbox{same licensed orbit}
\Rightarrow
\hbox{same actual support status},\\[1mm]
\hbox{different actual support status}
\Rightarrow
\hbox{licensed finite separator}.
\end{array}
}
$$

Thus the unsourced-law problem has been reduced to a finite certificate:

$$
\boxed{
\mathrm{V4P17\text{-}LIVE\text{-}TABLE\text{-}CERTIFICATE}.
}
$$

The live table certificate must print exactly one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{A}:&\hbox{automorphism/same-orbit certificate},\\[1mm]
\mathrm{B}:&\hbox{hard/reference/source/geometry/conditioning separator},\\[1mm]
\mathrm{C}:&\hbox{selector trap},\\[1mm]
\mathrm{D}:&\hbox{new unsourced primitive requiring a separate theorem}.
\end{array}
}
$$

If outcome \(\mathrm{A}\) is printed, the ansatz cannot split the rows.  If
outcome \(\mathrm{B}\) is printed, the ansatz is licensed exactly by that
separator.  If outcome \(\mathrm{C}\) is printed, the ansatz is rejected as
answer-fitting.  If outcome \(\mathrm{D}\) is printed, the next paper must
prove the named primitive or abandon that route.

This is the closure point reached in Paper 17:

$$
\boxed{
\hbox{we cannot honestly close by guessing a value; we can close by
printing the finite orbit/separator certificate.}
}
$$

## 23. Einstein Law: Finite Record Covariance And Hard-Support Completeness

We now take the Einstein step.  The previous sections treated finite record
covariance as a principle to be proved or adopted.  Here we state it as a
candidate law of the finite ISP theory.

The law is not:

$$
\boxed{
\hbox{the actual law has the value we need.}
}
$$

The law is:

$$
\boxed{
\hbox{the actual law can depend only on licensed finite record structure.}
}
$$

### Definition 23.1: Licensed Finite Record Groupoid

Let \({\bf LicRec}_{fin}\) be the groupoid whose objects are complete licensed
finite record structures

$$
\boxed{
{\mathfrak L}_R
=
\left(
K,\rho,C,F,G,S_{\mathrm{actual}}
\right),
}
$$

and whose arrows are licensed isomorphisms

$$
\boxed{
\phi:{\mathfrak L}_R\to{\mathfrak L}_{R'}'
}
$$

preserving hard constraints, reference density, source observables,
gauge/geometry/incidence data, and actual conditioning records.

The row labels used by an analyst are not objects of this groupoid unless
they are themselves actual conditioning records.

### Law 23.2: Finite Record Covariance Law

The actual law is a natural assignment on \({\bf LicRec}_{fin}\).  That is,
to each licensed finite record structure \({\mathfrak L}_R\) it assigns a
probability law

$$
\boxed{
P^{act}_{{\mathfrak L}_R}\in\Delta(K),
}
$$

and for every licensed isomorphism
\(\phi:{\mathfrak L}_R\to{\mathfrak L}'_{R'}\),

$$
\boxed{
\phi_\#P^{act}_{{\mathfrak L}_R}
=
P^{act}_{{\mathfrak L}'_{R'}}.
}
$$

If the reference density is transported by the same isomorphism, then the
posterior/reference ratio is natural:

$$
\boxed{
{P^{act}_{{\mathfrak L}'_{R'}}(\phi q)\over
\rho_{{\mathfrak L}'_{R'}}(\phi q)}
=
{P^{act}_{{\mathfrak L}_R}(q)\over
\rho_{{\mathfrak L}_R}(q)}.
}
$$

This is the finite-record analogue of general covariance.  A mere change of
presentation cannot change the physics.

### Law 23.3: Finite Hard-Support Completeness Law

Exact zero support is hard information.  A row can have zero actual mass only
if a licensed hard support datum excludes it:

$$
\boxed{
P^{act}(q\mid R)=0
\quad\Longrightarrow\quad
q\hbox{ is excluded by }C,\rho,S^{eff},\hbox{ or a licensed boundary face.}
}
$$

Equivalently, if

$$
\boxed{
C(q\mid R)=0,\qquad
\rho(q\mid R)>0,\qquad
S^{eff}(q\mid R)<\infty,
}
$$

and no licensed source/conditioning boundary face excludes \(q\), then

$$
\boxed{
P^{act}(q\mid R)>0.
}
$$

This law is the finite ISP version of the GR/SM support lesson:

$$
\boxed{
\hbox{soft finite scores reweight; hard constraints create exact zeros.}
}
$$

It is stronger than covariance.  Covariance says equal rows cannot be split.
Hard-support completeness says a hard-allowed row cannot be silently deleted.

### Theorem 23.4: Law-Level Two-Row Closure

Assume Laws 23.2 and 23.3.  For the live two-row fiber, suppose:

$$
\boxed{
C(q_0\mid R)=C(q_1\mid R)=0,
}
$$

$$
\boxed{
\rho(q_0\mid R)>0,\qquad
\rho(q_1\mid R)>0,
}
$$

$$
\boxed{
S^{eff}(q_0\mid R)<\infty,\qquad
S^{eff}(q_1\mid R)<\infty,
}
$$

and no licensed source, geometry, quotient, or actual conditioning boundary
face excludes either row.  Then

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

Proof.  Each live row satisfies the antecedent of hard-support completeness:
it is hard-allowed, reference-positive, finite-score, and not excluded by a
licensed boundary face.  Therefore each row has positive actual mass.  Finite
record covariance additionally forbids any presentation-dependent row-label
deletion.  `square`

### Theorem 23.5: Support Split Requires A Hard Separator

Assume Laws 23.2 and 23.3.  If

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1=0,
}
$$

then at least one licensed support-killing separator must be printed:

$$
\boxed{
\begin{array}{ll}
\mathrm{H1}:&C(q_1\mid R)\ne0,\\[1mm]
\mathrm{H2}:&\rho(q_1\mid R)=0,\\[1mm]
\mathrm{H3}:&S^{eff}(q_1\mid R)=\infty,\\[1mm]
\mathrm{H4}:&\hbox{a licensed source/conditioning boundary face excludes }
q_1,\\[1mm]
\mathrm{H5}:&\hbox{a licensed quotient/superselection sector excludes }q_1.
\end{array}
}
$$

The same statement holds with \(q_0,q_1\) interchanged.

Proof.  If no \(\mathrm{H1}\)-\(\mathrm{H5}\) separator holds for \(q_1\),
then \(q_1\) satisfies hard-support completeness and must have positive
actual mass, contradiction.  `square`

### Remark 23.6: Weight Separators Are Not Support Separators

The following may distinguish weights:

$$
\boxed{
\rho(q_0)\ne\rho(q_1),\qquad
F(q_0)\ne F(q_1),\qquad
S^{eff}(q_0)\ne S^{eff}(q_1)<\infty.
}
$$

But by themselves they do not create exact zero support.  They are
weight-only separators unless they become hard:

$$
\boxed{
\rho=0,\quad S^{eff}=\infty,\quad C\ne0,\quad
\hbox{or boundary-face exclusion.}
}
$$

This distinction is crucial.  The missing same-law problem is a support
problem, not merely a relative-weight problem.

## 24. Feynman Law Test: Print The Support-Killing Column

Feynman's version of the law is brutally small:

$$
\boxed{
\hbox{if one row is absent, show me the hard column that killed it.}
}
$$

### Algorithm 24.1: Hard-Support Completeness Table

For the live rows \(q_0,q_1\), print:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & S^{eff} & B_{\mathrm{bdry/source}}
& Q_{\mathrm{quot}}\\ \hline
q_0 & C_0 & \rho_0 & S_0 & B_0 & Q_0\\
q_1 & C_1 & \rho_1 & S_1 & B_1 & Q_1
\end{array}
}
$$

Then classify:

$$
\boxed{
\begin{array}{c|c}
\hbox{printed status} & \hbox{support consequence}\\ \hline
C_b=0,\ \rho_b>0,\ S_b<\infty,\ B_b=\hbox{in},\ Q_b=\hbox{in}
& \widehat m_b>0\\[1mm]
C_b\ne0\hbox{ or }\rho_b=0\hbox{ or }S_b=\infty
& \widehat m_b=0\\[1mm]
B_b=\hbox{out}\hbox{ or }Q_b=\hbox{out}
& \widehat m_b=0
\end{array}
}
$$

This is the executable Feynman closure table.

### Current-Corpus Feynman Audit 24.2

The current corpus has narrowed the columns as follows:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{column} & \hbox{current printed status} & \hbox{effect}\\ \hline
C & \hbox{no live row-sensitive hard constraint printed}
& \hbox{no support kill yet}\\[1mm]
\rho & \hbox{no zero-reference row printed}
& \hbox{no support kill yet}\\[1mm]
S^{eff} & \hbox{no finite/infinite row split printed}
& \hbox{no support kill yet}\\[1mm]
B_{\mathrm{bdry/source}} & \hbox{licensed fixed sources are row-blind}
& \hbox{no support kill yet}\\[1mm]
Q_{\mathrm{quot}} & \hbox{no quotient/superselection row exclusion printed}
& \hbox{no support kill yet}\\[1mm]
U & \hbox{row label only}
& \hbox{selector trap}\\[1mm]
\eta,\hbox{ Bianchi/Ward} & \hbox{not licensed as support data}
& \hbox{unsourced primitive}
\end{array}
}
$$

Thus the Feynman audit has not printed a support-killing column.  It also has
not yet printed the fully positive hard-status certificate

$$
\boxed{
C_b=0,\quad \rho_b>0,\quad S_b<\infty,\quad
B_b=Q_b=\hbox{in}
\qquad(b=0,1).
}
$$

That is the last finite table to fill.

### Theorem 24.3: What Would Close Paper 17

Under Laws 23.2 and 23.3, Paper 17 closes the live support problem as soon
as the Feynman table prints:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & S^{eff} & B_{\mathrm{bdry/source}}
& Q_{\mathrm{quot}}\\ \hline
q_0 & 0 & >0 & <\infty & \hbox{in} & \hbox{in}\\
q_1 & 0 & >0 & <\infty & \hbox{in} & \hbox{in}
\end{array}
}
$$

Then

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

If instead the table prints one support-killing entry for exactly one row,
then Einstein singleton selection is licensed by that entry.

If the only support-killing entry is \(U\), the closure fails because \(U\)
is an unlicensed selector.

If the support-killing entry is \(\eta\), Bianchi/Ward, or residual closure,
then the next primitive theorem must prove that this defect is actual hard
support data, not merely a diagnostic.

### Final Law-Level Verdict 24.4

Einstein's law-level move is:

$$
\boxed{
\mathrm{V4P17\text{-}FINITE\text{-}RECORD\text{-}COVARIANCE\text{-}LAW}
\quad+\quad
\mathrm{V4P17\text{-}HARD\text{-}SUPPORT\text{-}COMPLETENESS\text{-}LAW}.
}
$$

Feynman's concrete move is:

$$
\boxed{
\mathrm{V4P17\text{-}HARD\text{-}SUPPORT\text{-}COMPLETENESS\text{-}TABLE}.
}
$$

The support problem closes exactly when the table prints either:

$$
\boxed{
\hbox{both rows hard-in}
\quad\hbox{or}\quad
\hbox{one licensed hard support-killer.}
}
$$

This is now the sharpest possible formulation of the missing-law issue:

$$
\boxed{
\hbox{exact zeros must come from exact finite support data.}
}
$$

## 25. Final Hard-Support Table Audit

We now execute the table demanded by Section 24.  The goal is not to
estimate a soft weight.  The goal is to decide whether either row has a
licensed hard support-killer.

### Definition 25.1: The Final Support-Killing Columns

For the live rows \(q_0,q_1\), use the five-column support table:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & S^{eff} & B_{\mathrm{bdry/source}}
& Q_{\mathrm{quot}}\\ \hline
q_0 & ? & ? & ? & ? & ?\\
q_1 & ? & ? & ? & ? & ?
\end{array}
}
$$

The meaning of each column is:

$$
\boxed{
\begin{array}{ll}
C:&\hbox{hard constraint status},\\[1mm]
\rho:&\hbox{reference support status},\\[1mm]
S^{eff}:&\hbox{finite or infinite effective score},\\[1mm]
B_{\mathrm{bdry/source}}:&\hbox{boundary/source face inclusion},\\[1mm]
Q_{\mathrm{quot}}:&\hbox{quotient/superselection inclusion}.
\end{array}
}
$$

The row is hard-in exactly when:

$$
\boxed{
C=0,\qquad \rho>0,\qquad S^{eff}<\infty,\qquad
B_{\mathrm{bdry/source}}=\hbox{in},\qquad
Q_{\mathrm{quot}}=\hbox{in}.
}
$$

### Audit 25.2: Hard Constraint Column \(C\)

The candidate hard constraint vector has already been audited:

$$
\boxed{
C
=
\left(
C^{Gauss},
C^{bdry},
C^{Bianchi},
C^{hyp},
C^{quot},
C^{res}
\right).
}
$$

The current corpus prints no live row-sensitive hard separator among Gauss,
boundary/source, hypersurface compatibility, quotient conventions, residual
actuality, or Bianchi/Ward closure.  The positive row-in statement therefore
has two layers:

1. **Declared hard fiber.**  The live problem is defined on the formal
   hard-allowed fiber containing \(q_0,q_1\).  Thus, for the hard constraints
   already declared as part of the finite grammar,

   $$
   \boxed{
   C^{decl}(q_0)=C^{decl}(q_1)=0.
   }
   $$

2. **Unsettled hard candidates.**  Residual, Bianchi/Ward, and closure
   defects have not been licensed as hard support data and no two-row table
   has been printed for them.

Thus the current hard-column entry is:

$$
\boxed{
C_0=C_1=0
\quad
\hbox{relative to declared hard constraints,}
}
$$

with the caveat:

$$
\boxed{
C^{res/Bianchi/Ward}\hbox{ remains an unsourced hard-candidate column.}
}
$$

If a future theorem licenses one of these candidates and prints
\(C_0=0,C_1\ne0\), then the table changes to Einstein singleton selection.

### Audit 25.3: Reference Column \(\rho\)

The GR/SM-informed finite support ansatz uses a reference law supported on
the declared hard-allowed finite record set.  Since \(q_0,q_1\) are live rows
of that set, the support-table entry is:

$$
\boxed{
\rho(q_0\mid R)>0,\qquad \rho(q_1\mid R)>0.
}
$$

This is not the statement that \(\rho(q_0)=\rho(q_1)\).  Unequal positive
reference weights may reweight the rows.  They do not kill support.

Falsification would require a printed reference exclusion:

$$
\boxed{
\rho(q_b\mid R)=0
}
$$

with an independent finite construction reason.  No such exclusion is printed
in the current corpus.

### Audit 25.4: Effective Score Column \(S^{eff}\)

A finite effective score may favor one row over another:

$$
\boxed{
S^{eff}(q_0)\ne S^{eff}(q_1).
}
$$

But support is killed only by an infinite score:

$$
\boxed{
S^{eff}(q_b)=\infty.
}
$$

The current corpus has not printed any infinite-action row exclusion.  The
GR/SM-informed finite law treats the visible action, residual, Jacobian,
instrument, and source scores as finite on the live hard fiber unless a hard
constraint explicitly removes the row.  Therefore the support-table entry is:

$$
\boxed{
S^{eff}(q_0\mid R)<\infty,\qquad
S^{eff}(q_1\mid R)<\infty.
}
$$

Again, this is support information, not equality of weights.

### Audit 25.5: Boundary/Source Face Column \(B_{\mathrm{bdry/source}}\)

Boundary and source records are part of the declared conditioning \(R\).
Inside the live two-row problem:

$$
\boxed{
R(q_0)=R(q_1)=R.
}
$$

Paper 17's source audit found:

$$
\boxed{
\hbox{licensed fixed sources are row-blind on the live fiber.}
}
$$

A source-face exclusion would require a licensed source map \(F\) and declared
source value \(f\) such that the feasible source face meets only one row
fiber.  The current corpus has not printed such a licensed row-selecting
source face.  Therefore:

$$
\boxed{
B_{\mathrm{bdry/source}}(q_0)=\hbox{in},\qquad
B_{\mathrm{bdry/source}}(q_1)=\hbox{in},
}
$$

relative to currently licensed fixed boundary/source data.

The caveat is exact:

$$
\boxed{
\hbox{a future licensed residual/Bianchi/source table could turn this into
a boundary-face selector.}
}
$$

But it is not printed now.

### Audit 25.6: Quotient/Superselection Column \(Q_{\mathrm{quot}}\)

A quotient can affect the live table in two distinct ways:

1. \(q_0,q_1\) are the same physical row modulo quotient.  Then the row labels
   should be collapsed, not assigned singleton support.
2. exactly one representative is forbidden by a licensed representative rule.
   Then the forbidden representative is hard-out.

The current corpus prints neither a quotient collapse nor a representative
exclusion for the live pair.  Therefore, as distinct formal live rows,

$$
\boxed{
Q_{\mathrm{quot}}(q_0)=\hbox{in},\qquad
Q_{\mathrm{quot}}(q_1)=\hbox{in}.
}
$$

If future quotient data identify the rows, the two-row support question is
not solved by killing a row; it is dissolved by quotienting the labels.

### Theorem 25.7: Final Current-Corpus Hard-Support Table

Under the law-level assumptions of finite record covariance and hard-support
completeness, and relative to the currently licensed hard data, the live
two-row support table is:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & S^{eff} & B_{\mathrm{bdry/source}}
& Q_{\mathrm{quot}}\\ \hline
q_0 & 0 & >0 & <\infty & \hbox{in} & \hbox{in}\\
q_1 & 0 & >0 & <\infty & \hbox{in} & \hbox{in}
\end{array}
}
$$

Therefore:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

Proof.  The five audits above print the hard-in entry for both rows.  Theorem
23.4 then applies.  `square`

### Corollary 25.8: Exact Meaning Of The Closure

The closure is not:

$$
\boxed{
\hbox{no future theorem can ever find a row separator.}
}
$$

The closure is:

$$
\boxed{
\hbox{with the currently licensed finite support data, both live rows are
hard-in.}
}
$$

Thus any future singleton-selection route must do one of the following:

$$
\boxed{
\begin{array}{ll}
\mathrm{N1}:&\hbox{license residual/Bianchi/Ward as actual hard support data},\\[1mm]
\mathrm{N2}:&\hbox{print a source boundary face meeting only one row fiber},\\[1mm]
\mathrm{N3}:&\hbox{print a zero reference or infinite score for one row},\\[1mm]
\mathrm{N4}:&\hbox{print a quotient/superselection exclusion},\\[1mm]
\mathrm{N5}:&\hbox{show that the two rows were never in the same conditioned
support problem.}
\end{array}
}
$$

Anything else is a row-label selector.

### Final Paper-17 Closure 25.9

Paper 17 now closes the current-corpus support question in the following
precise sense:

$$
\boxed{
\mathrm{V4P17\text{-}CURRENT\text{-}LICENSED\text{-}HARD\text{-}SUPPORT
\text{-}TABLE}
}
$$

is printed, and it gives:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0
}
$$

under the Einstein law stack:

$$
\boxed{
\mathrm{FINITE\text{-}RECORD\text{-}COVARIANCE}
\quad+\quad
\mathrm{HARD\text{-}SUPPORT\text{-}COMPLETENESS}.
}
$$

This is the cleanest endpoint of the current paper:

$$
\boxed{
\hbox{current licensed hard data imply Feynman two-row support; Einstein
singleton selection requires a new licensed hard support-killer.}
}
$$

## 26. Law Adoption Or Derivation Fork

The current paper has now isolated the final dependency.  The support-table
calculation is finished, but it depends on two law-level commitments:

$$
\boxed{
\mathrm{FINITE\text{-}RECORD\text{-}COVARIANCE}
\quad\hbox{and}\quad
\mathrm{HARD\text{-}SUPPORT\text{-}COMPLETENESS}.
}
$$

Einstein's next move is to ask whether these are derivable from the ontology
or must be adopted as finite ISP postulates.

### Principle 26.1: Ontic Finiteness

The primitive objects of the theory are complete finite records and their
probability laws.  Analyst labels, coordinate names, row names, and
presentation choices are not additional physical variables unless they are
themselves recorded.

Formally, if \({\mathfrak L}_R\) and \({\mathfrak L}'_{R'}\) are licensed
finite record structures related by a record isomorphism

$$
\boxed{
\phi:{\mathfrak L}_R\cong{\mathfrak L}'_{R'},
}
$$

then they represent the same physical finite record situation in different
presentations.

### Theorem 26.2: Ontic Finiteness Derives Finite Record Covariance

Assume ontic finiteness.  Then the actual law must be natural under licensed
finite record isomorphisms:

$$
\boxed{
\phi_\#P^{act}_{{\mathfrak L}_R}
=
P^{act}_{{\mathfrak L}'_{R'}}.
}
$$

Proof.  If \(\phi\) preserves every licensed finite record fact, then
\({\mathfrak L}_R\) and \({\mathfrak L}'_{R'}\) differ only by presentation.
If the pushed-forward law were different, two presentations of the same
finite record situation would make different physical predictions.  That
would make presentation names into hidden physical variables, contradicting
ontic finiteness.  `square`

This derivation is strong but clean.  Rejecting it means adding hidden
non-record ontology.

### Principle 26.3: No Silent Hard Deletion

An exact zero in a finite probability law is not a soft preference.  It is
an exclusion from the sample space or from the support of the reference law.
Therefore, if a complete finite record is:

$$
\boxed{
C(q\mid R)=0,\qquad
\rho(q\mid R)>0,\qquad
S^{eff}(q\mid R)<\infty,
}
$$

and no licensed boundary/source/quotient face excludes it, then the actual
law may reweight it but may not delete it:

$$
\boxed{
P^{act}(q\mid R)>0.
}
$$

### Theorem 26.4: Finite Positive Reweighting Cannot Create A New Zero

Let \(K\) be a finite hard-allowed set.  Suppose

$$
\boxed{
\rho(q)>0,\qquad S(q)<\infty
\qquad\forall q\in K.
}
$$

Define

$$
\boxed{
P(q)
=
{1\over Z}\rho(q)e^{-S(q)}
\qquad(q\in K).
}
$$

Then

$$
\boxed{
P(q)>0
\qquad\forall q\in K.
}
$$

Proof.  On a finite set, \(\rho(q)>0\) and \(e^{-S(q)}>0\) for every finite
\(S(q)\).  The normalizer

$$
\boxed{
Z=\sum_{q\in K}\rho(q)e^{-S(q)}
}
$$

is positive and finite.  Hence each \(P(q)\) is positive.  `square`

### Corollary 26.5: Singleton Support Needs Hard Data

In the live two-row fiber, a singleton support outcome such as

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1=0
}
$$

cannot be produced by finite soft reweighting of a positive reference law.
It requires at least one hard datum:

$$
\boxed{
C_1\ne0,\quad
\rho_1=0,\quad
S_1=\infty,\quad
B_1=\hbox{out},\quad
Q_1=\hbox{out},
}
$$

or the corresponding \(q_0\)-version.

### Theorem 26.6: Hard-Support Completeness From GR/SM-Informed Finite Law

Assume the actual finite law has the GR/SM-informed form:

$$
\boxed{
P^{act}(q\mid R)
=
{1\over Z(R)}
\rho(q\mid R)e^{-S^{eff}(q\mid R)}
1_{\{C(q\mid R)=0\}},
}
$$

with boundary/source/quotient exclusions included in \(C\) or in the support
of \(\rho\).  Then hard-support completeness holds.

Proof.  If a row is hard-allowed, reference-positive, and finite-score, the
right-hand side is a positive finite number divided by the positive finite
normalizer.  Therefore the row has positive actual support.  A zero can only
come from \(C\ne0\), \(\rho=0\), \(S^{eff}=\infty\), or a boundary/quotient
exclusion encoded in those objects.  `square`

### The Fork 26.7: Derivation Or Postulate

There are now exactly two honest ways to close the law-level issue.

**Route A: Derived Closure.**  Prove:

$$
\boxed{
\begin{array}{ll}
\mathrm{D1}:&\hbox{ontic finiteness of complete records},\\[1mm]
\mathrm{D2}:&\hbox{actual-law naturality under record isomorphism},\\[1mm]
\mathrm{D3}:&\hbox{actual finite law has positive reweighting form on hard
support}.
\end{array}
}
$$

Then finite record covariance and hard-support completeness are theorems.
Paper 17 closes without extra postulates.

**Route B: Postulated Closure.**  Adopt:

$$
\boxed{
\begin{array}{ll}
\mathrm{P1}:&\mathrm{FINITE\text{-}RECORD\text{-}COVARIANCE},\\[1mm]
\mathrm{P2}:&\mathrm{HARD\text{-}SUPPORT\text{-}COMPLETENESS}.
\end{array}
}
$$

Then Paper 17 closes as the first support theorem of the extended finite ISP
law.

### Feynman No-Go 26.8: How To Falsify The Closure

To falsify the current closure, one must print a finite counterexample with:

$$
\boxed{
C(q_b)=0,\quad \rho(q_b)>0,\quad S^{eff}(q_b)<\infty,\quad
B_b=Q_b=\hbox{in}
}
$$

but

$$
\boxed{
P^{act}(q_b\mid R)=0.
}
$$

Such a counterexample cannot come from finite positive reweighting.  It must
therefore reveal one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{F1}:&\hbox{a hidden hard constraint},\\[1mm]
\mathrm{F2}:&\hbox{a hidden zero in the reference support},\\[1mm]
\mathrm{F3}:&\hbox{a hidden infinite score},\\[1mm]
\mathrm{F4}:&\hbox{a hidden boundary/quotient exclusion},\\[1mm]
\mathrm{F5}:&\hbox{extra non-record ontology choosing support}.
\end{array}
}
$$

\(\mathrm{F1}\)-\(\mathrm{F4}\) are not failures; they are missing hard data.
\(\mathrm{F5}\) is the genuine falsifier of the finite-record law.

### Final Closure Statement 26.9

Paper 17 reaches the following endpoint:

$$
\boxed{
\begin{array}{c}
\hbox{If finite record covariance and hard-support completeness are derived
or adopted,}\\[1mm]
\hbox{then the current licensed hard-support table proves}\\[1mm]
\widehat m_0>0,\qquad \widehat m_1>0.
\end{array}
}
$$

The remaining work is no longer to compute the two-row value.  It is to
decide the status of the two laws:

$$
\boxed{
\mathrm{derived\ ontology}
\quad\hbox{or}\quad
\mathrm{explicit\ support\ postulates}.
}
$$

That is the honest closure point.

## 27. Finite Support Stability Theorem

The last route tries to derive hard-support completeness from a still more
primitive idea:

$$
\boxed{
\hbox{soft finite changes should not create or destroy exact support.}
}
$$

This is the Einstein/Feynman synthesis.  Einstein supplies the principle:
support is structural.  Feynman supplies the test: perturb every finite soft
knob a little and see whether a claimed zero survives without a hard reason.

### Definition 27.1: Licensed Soft Chamber

A licensed soft chamber \({\mathcal U}\) is a connected parameter set
\(\theta\in{\mathcal U}\) over which the following data are fixed:

$$
\boxed{
K,\qquad C,\qquad B_{\mathrm{bdry/source}},\qquad Q_{\mathrm{quot}}.
}
$$

On this chamber the reference and score may vary, but only softly:

$$
\boxed{
\rho_\theta(q)>0,\qquad
S_\theta(q)<\infty
\qquad
\forall q\in K,\quad \forall\theta\in{\mathcal U}.
}
$$

Thus \({\mathcal U}\) contains no hard support wall:

$$
\boxed{
C\ne0,\quad \rho=0,\quad S=\infty,\quad
B=\hbox{out},\quad Q=\hbox{out}
}
$$

never occurs inside \({\mathcal U}\).

### Definition 27.2: Support-Stable Actual Law

An actual-law family \(P_\theta^{act}\) is support-stable on
\({\mathcal U}\) if for any \(\theta,\theta'\in{\mathcal U}\),

$$
\boxed{
\operatorname{supp}P_\theta^{act}
=
\operatorname{supp}P_{\theta'}^{act}.
}
$$

It is locally support-stable if this holds on a neighborhood of every
\(\theta\in{\mathcal U}\).  Since \({\mathcal U}\) is connected, local
support-stability implies global support-stability on \({\mathcal U}\).

### Theorem 27.3: Positive RN Reweighting Implies Support Stability

Let \(P_\theta\) be finite probability laws on \(K\).  Suppose that for every
\(\theta,\theta'\in{\mathcal U}\) there is a finite positive Radon-Nikodym
ratio

$$
\boxed{
0<
{dP_\theta\over dP_{\theta'}}(q)
<\infty
\qquad
\hbox{for all }q\in K.
}
$$

Then \(P_\theta\) is support-stable on \({\mathcal U}\).

Proof.  A positive finite Radon-Nikodym ratio cannot turn a positive atom
into a zero atom or a zero atom into a positive atom.  Therefore the supports
of \(P_\theta\) and \(P_{\theta'}\) agree.  `square`

### Corollary 27.4: Exponential Soft Sources Preserve Support

If

$$
\boxed{
P_\theta(q)
=
{1\over Z(\theta)}
\rho(q)e^{-S(q)-\sum_r\theta_rF_r(q)}
}
$$

on a fixed finite hard set \(K\), with \(\rho(q)>0\), \(S(q)<\infty\), and
bounded finite \(F_r(q)\), then the support is independent of \(\theta\).

In particular, if one chamber point has full support, every chamber point
has full support.

Proof.  For any \(\theta,\theta'\),

$$
\boxed{
{P_\theta(q)\over P_{\theta'}(q)}
=
{Z(\theta')\over Z(\theta)}
\exp\left\{-\sum_r(\theta_r-\theta'_r)F_r(q)\right\},
}
$$

which is positive and finite on finite \(K\).  Apply Theorem 27.3.  `square`

### Definition 27.5: Full-Support Anchor

A licensed soft chamber has a full-support anchor if there exists
\(\theta_*\in{\mathcal U}\) such that

$$
\boxed{
P^{act}_{\theta_*}(q)>0
\qquad\forall q\in K.
}
$$

The simplest anchor is the finite reference law:

$$
\boxed{
P_{\mathrm{ref}}(q)
=
{\rho(q)\over\sum_{q'\in K}\rho(q')},
}
$$

provided \(\rho(q)>0\) on \(K\).

### Theorem 27.6: Support Stability Plus Anchor Gives Hard-Support Completeness

Assume:

1. \(q\in K\) is hard allowed;
2. \(\rho_\theta(q)>0\) and \(S_\theta(q)<\infty\) throughout a licensed soft
   chamber \({\mathcal U}\);
3. \(B(q)=Q(q)=\hbox{in}\) throughout \({\mathcal U}\);
4. the actual law is support-stable on \({\mathcal U}\);
5. \({\mathcal U}\) has a full-support anchor.

Then

$$
\boxed{
P_\theta^{act}(q)>0
\qquad
\forall\theta\in{\mathcal U}.
}
$$

Proof.  At the anchor \(\theta_*\), \(P_{\theta_*}^{act}(q)>0\).  By
support-stability, \(\operatorname{supp}P_\theta^{act}\) is the same for all
\(\theta\in{\mathcal U}\).  Therefore \(q\) remains in support throughout
the chamber.  `square`

This derives hard-support completeness from two more primitive inputs:

$$
\boxed{
\hbox{support stability}
\quad+\quad
\hbox{one full-support anchor.}
}
$$

### Theorem 27.7: Arbitrary Finite Laws Falsify Stability Unless A Hard Mask Is Printed

On the two-row set \(K=\{q_0,q_1\}\), suppose

$$
\boxed{
C_0=C_1=0,\qquad
\rho_0,\rho_1>0,\qquad
S_0,S_1<\infty,\qquad
B_0=B_1=Q_0=Q_1=\hbox{in}.
}
$$

The finite law

$$
\boxed{
P(q_0)=1,\qquad P(q_1)=0
}
$$

is a legal abstract probability law.  But it violates support stability
relative to any full-support anchor unless the zero row is encoded by a hard
mask.

Proof.  The full-support anchor has \(P_*(q_1)>0\).  The singleton law has
\(P(q_1)=0\).  Hence the support changed inside a chamber where no hard
support wall was printed.  That is exactly a support-stability violation.
To make the singleton law physical, one must add a hard datum excluding
\(q_1\).  `square`

This theorem is the honest limit of derivation from Barandes-style finiteness:
finite probability laws alone allow singleton support.  A physical finite ISP
law must either reject silent singleton masks or record them as hard data.

### Principle 27.8: No Hidden Support Mask

No hidden support mask says:

$$
\boxed{
\hbox{the support of }P^{act}\hbox{ is determined by the licensed hard
support data, not by an extra unrecorded subset of }K.
}
$$

Equivalently, if two finite laws have the same licensed hard support data and
differ only by finite soft weights, they must have the same support.

This principle is exactly what V3 lacked in value form.  V3 needed actual
same-law numerical values.  Here we need only a support-level version:
finite soft variation cannot invent a zero.

### Theorem 27.9: Einstein/Feynman Closure From Support Stability

Assume:

1. ontic finiteness;
2. finite record covariance;
3. no hidden support mask;
4. support stability on licensed soft chambers;
5. a full-support reference anchor on the declared hard set.

Then hard-support completeness follows.  Consequently the final Paper-17
hard-support table proves

$$
\boxed{
\widehat m_0>0,\qquad
\widehat m_1>0.
}
$$

Proof.  Ontic finiteness gives finite record covariance by Theorem 26.2.  No
hidden support mask plus support stability says the support cannot change
inside a chamber unless hard support data changes.  The full-support anchor
puts every hard-in row in support somewhere in the chamber.  Theorem 27.6
then puts every hard-in row in support everywhere in the chamber.  The final
hard-support table of Theorem 25.7 places both live rows hard-in.  Therefore
both live row masses are positive.  `square`

### Feynman Exhaustion 27.10: All Ways To Avoid The Conclusion

To avoid

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0
}
$$

one must choose one of the following:

$$
\boxed{
\begin{array}{ll}
\mathrm{E1}:&\hbox{print a hard support-killer }C,\rho,S,B,Q,\\[1mm]
\mathrm{E2}:&\hbox{deny the full-support anchor},\\[1mm]
\mathrm{E3}:&\hbox{deny support stability},\\[1mm]
\mathrm{E4}:&\hbox{add a hidden support mask not recorded in }C,\rho,S,B,Q,\\[1mm]
\mathrm{E5}:&\hbox{show that }q_0,q_1\hbox{ are not in one conditioned
finite support problem}.
\end{array}
}
$$

The meaning of each exit is:

1. \(\mathrm{E1}\) is a successful Einstein singleton theorem.
2. \(\mathrm{E2}\) says the reference hard set was misidentified.
3. \(\mathrm{E3}\) makes exact support unstable under infinitesimal finite
   soft changes; this is a new physical law and must be declared.
4. \(\mathrm{E4}\) violates finite-record ontology unless the mask is added
   as a record.
5. \(\mathrm{E5}\) dissolves the two-row problem.

There is no sixth route.

### Final Endpoint 27.11

Paper 17 can now be closed in one sentence:

$$
\boxed{
\hbox{under finite record covariance and finite support stability, the
current licensed hard table forces Feynman two-row support.}
}
$$

The theorem does not say that singleton support is impossible.  It says
singleton support is not silent:

$$
\boxed{
\hbox{Einstein singleton selection requires a printed hard support-killer.}
}
$$

This is the final non-tautological answer to the missing-law problem at the
support level.
