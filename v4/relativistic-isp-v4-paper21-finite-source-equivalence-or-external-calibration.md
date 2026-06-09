# Relativistic ISP V4 Paper 21: Finite Source Equivalence Or External Calibration

Author: Felix Robles Elvira

## 0. Purpose

Paper 20 ended at a theory-completion boundary:

$$
\boxed{
\hbox{stop squeezing support; either print the finite source table or add
the finite source-equivalence law.}
}
$$

Paper 21 investigates both options.

The two moves are:

$$
\boxed{
\begin{array}{ll}
\mathrm{Feynman}:&\hbox{build and test the smallest bridge laboratories},\\
\mathrm{Einstein}:&\hbox{ask whether finite source equivalence is a
principled law or value-smuggling}.
\end{array}
}
$$

This paper does not pretend to extract missing numerical source data from
the current corpus.  Its job is sharper:

$$
\boxed{
\hbox{decide what kind of new input would honestly complete the theory.}
}
$$

## 1. Imports From Paper 20

The finite bridge graph has readout vertices:

$$
\boxed{
s_0,\ s_1,\ s_2
}
$$

and directed edges:

$$
\boxed{
01:s_0\to s_1,\qquad
12:s_1\to s_2,\qquad
02:s_0\to s_2.
}
$$

The corrected value one-form is:

$$
\boxed{
\ell=(\ell_{01},\ell_{12},\ell_{02})
}
$$

where:

$$
\boxed{
\ell_{ij}
=
\widetilde L_A(i\to j).
}
$$

The triangle defect is:

$$
\boxed{
\Omega_{012}
=
\ell_{01}+\ell_{12}-\ell_{02}.
}
$$

The scalar potential condition is:

$$
\boxed{
\ell=B\Phi,
}
$$

where:

$$
\boxed{
B\Phi
=
\left(
\Phi(s_1)-\Phi(s_0),
\Phi(s_2)-\Phi(s_1),
\Phi(s_2)-\Phi(s_0)
\right).
}
$$

The curved/holonomy condition is:

$$
\boxed{
\ell=B\Phi+{\mathcal A}^{hol},
\qquad
\oint_{012}{\mathcal A}^{hol}=H(012).
}
$$

Paper 20 proved:

$$
\boxed{
\begin{array}{c|c}
\Omega_{012}=0 & \hbox{flat potential bridge}\\
\Omega_{012}\ne0\hbox{ and }H(012)=\Omega_{012}\hbox{ licensed} &
\hbox{curved holonomy bridge}\\
\Omega_{012}\ne0\hbox{ and no licensed }H &
\hbox{split/no-go}
\end{array}
}
$$

## 2. The No-Squeeze Boundary

The current corpus does not print:

$$
\boxed{
\ell_{01},\quad \ell_{12},\quad \ell_{02},
\quad
\zeta_{01},\quad \zeta_{12},\quad \zeta_{02},
\quad
H(012).
}
$$

Therefore the current corpus cannot decide the bridge verdict numerically.

The only honest new inputs are:

$$
\boxed{
\begin{array}{ll}
\mathrm{D}:&\hbox{new finite source data},\\
\mathrm{L}:&\hbox{a new finite source law}.
\end{array}
}
$$

The rest of this paper tests both.

## 3. Feynman Investigation: The Triangle Test Bench

The Feynman test bench deliberately uses numbers.  Its purpose is not to
prove physical truth.  It checks whether the Paper-20 classifier behaves
correctly when the missing data are actually supplied.

Set:

$$
\boxed{
s_0=0,\qquad s_1=1,\qquad s_2=2.
}
$$

Use the trivial operational reference correction:

$$
\boxed{
\rho^{op}_{ij,+}/\rho^{op}_{ij,-}=1.
}
$$

Set the Stein tube to zero in the toy laboratory:

$$
\boxed{
\zeta_{01}=\zeta_{12}=\zeta_{02}=0.
}
$$

Thus the verdict is controlled entirely by:

$$
\boxed{
\Omega_{012}.
}
$$

## 4. Feynman Test F1: Flat Potential Success

Choose:

$$
\boxed{
\ell_{01}=\frac12,
\qquad
\ell_{12}=\frac13,
\qquad
\ell_{02}=\frac56.
}
$$

Then:

$$
\boxed{
\Omega_{012}
=
\frac12+\frac13-\frac56
=0.
}
$$

The potential is:

$$
\boxed{
\Phi(s_0)=0,
\qquad
\Phi(s_1)=\frac12,
\qquad
\Phi(s_2)=\frac56.
}
$$

Check:

$$
\boxed{
B\Phi
=
\left(
\frac12,\frac13,\frac56
\right)
=
\ell.
}
$$

The verdict is:

$$
\boxed{
\mathrm{F1}=\mathrm{FLAT}.
}
$$

### Weight Realization

One may realize the toy GR/SM weights by:

$$
\boxed{
W_0=1,
\qquad
W_1=e^{1/2},
\qquad
W_2=e^{5/6}.
}
$$

Then:

$$
\boxed{
\log(W_1/W_0)=\frac12,\quad
\log(W_2/W_1)=\frac13,\quad
\log(W_2/W_0)=\frac56.
}
$$

So F1 is internally consistent.

## 5. Feynman Test F2: Curved Holonomy Success

Choose:

$$
\boxed{
\ell_{01}=\frac12,
\qquad
\ell_{12}=\frac13,
\qquad
\ell_{02}=\frac34.
}
$$

Then:

$$
\boxed{
\Omega_{012}
=
\frac12+\frac13-\frac34
=
\frac1{12}.
}
$$

The scalar potential bridge fails.  But define a licensed cycle source:

$$
\boxed{
H(012)=\frac1{12}.
}
$$

Set:

$$
\boxed{
\Phi(s_0)=0,
\qquad
\Phi(s_1)=\frac12,
\qquad
\Phi(s_2)=\frac56.
}
$$

and:

$$
\boxed{
{\mathcal A}^{hol}_{01}=0,
\qquad
{\mathcal A}^{hol}_{12}=0,
\qquad
{\mathcal A}^{hol}_{02}=-\frac1{12}.
}
$$

Then:

$$
\boxed{
B\Phi+{\mathcal A}^{hol}
=
\left(
\frac12,\frac13,\frac34
\right)
=
\ell.
}
$$

The cycle integral is:

$$
\boxed{
\oint_{012}{\mathcal A}^{hol}
=
0+0-\left(-\frac1{12}\right)
=
\frac1{12}
=
H(012).
}
$$

The verdict is:

$$
\boxed{
\mathrm{F2}=\mathrm{CURVED}
\quad\hbox{if }H(012)\hbox{ is independently licensed.}
}
$$

## 6. Feynman Test F3: Split/External Calibration

Use the same edge values as F2:

$$
\boxed{
\ell_{01}=\frac12,
\qquad
\ell_{12}=\frac13,
\qquad
\ell_{02}=\frac34.
}
$$

Then:

$$
\boxed{
\Omega_{012}=\frac1{12}\ne0.
}
$$

But now do not print a licensed \(H(012)\).  Then the curved repair is not
available.

The verdict is:

$$
\boxed{
\mathrm{F3}=\mathrm{SPLIT}.
}
$$

This means the three edge ratios may still be used as an external calibrated
source, but they have not been derived from the finite readout geometry.

## 7. Feynman Test F4: Noisy Approximate Flatness

Choose:

$$
\boxed{
\ell_{01}=\frac12,
\qquad
\ell_{12}=\frac13,
\qquad
\ell_{02}=\frac56+\epsilon.
}
$$

Then:

$$
\boxed{
\Omega_{012}=-\epsilon.
}
$$

With tolerance \(\tau_B\), the finite verdict is:

$$
\boxed{
\begin{array}{c|c}
|\epsilon|\le\tau_B & \mathrm{FLAT\ at\ tolerance}\\
|\epsilon|>\tau_B & \mathrm{not\ flat\ at\ tolerance}
\end{array}
}
$$

The refinement question is:

$$
\boxed{
\epsilon_n\to0
\quad\hbox{or}\quad
\epsilon_n\to h\ne0
\quad\hbox{or}\quad
\epsilon_n\hbox{ wanders}.
}
$$

Thus:

$$
\boxed{
\begin{array}{c|c}
\epsilon_n\to0 & \hbox{continuum flatness}\\
\epsilon_n\to h\ne0 & \hbox{stable curvature candidate}\\
\epsilon_n\hbox{ wanders} & \hbox{noise or incomplete source}
\end{array}
}
$$

## 8. Feynman Test F5: Repeated-Edge Sufficiency

Before a triangle, one can test repeated-edge well-definedness.

Print two edges:

$$
\boxed{
e:s_0\to s_1,
\qquad
f:s_0\to s_1.
}
$$

Choose:

$$
\boxed{
\ell_e=\frac12,
\qquad
\ell_f=\frac12+\delta.
}
$$

Then:

$$
\boxed{
D_{rep}(e,f)=\ell_e-\ell_f=-\delta.
}
$$

The finite verdict is:

$$
\boxed{
\begin{array}{c|c}
|\delta|\le\tau_A & \hbox{readout survives repeated-edge scalarity}\\
|\delta|>\tau_A & \hbox{readout }Y\hbox{ is insufficient or curved}
\end{array}
}
$$

This test is cheap and should precede the triangle when repeated edges are
available.

## 9. Feynman Investigation Verdict

The toy lab gives a complete sanity check:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{input pattern} & \hbox{verdict}\\
\hline
\mathrm{F1} & \Omega=0 & \mathrm{FLAT}\\
\mathrm{F2} & \Omega=h,\ H=h\hbox{ licensed} & \mathrm{CURVED}\\
\mathrm{F3} & \Omega=h,\ H\hbox{ absent} & \mathrm{SPLIT}\\
\mathrm{F4} & \Omega=-\epsilon & \hbox{tolerance/refinement decision}\\
\mathrm{F5} & D_{rep}=-\delta & \hbox{readout sufficiency test}
\end{array}
}
$$

So the classifier is not the problem.  The problem is the absence of a real
licensed value source instance.

## 10. What The Feynman Route Can And Cannot Prove

The Feynman route can prove:

$$
\boxed{
\hbox{the bridge classifier works on explicit finite data.}
}
$$

It can also falsify:

$$
\boxed{
\hbox{a proposed readout }Y\hbox{ as a scalar source if repeated-edge or
cycle defects persist.}
}
$$

It cannot prove:

$$
\boxed{
\hbox{the current corpus already contains the missing value source.}
}
$$

For that, one must print actual instrument/GCR/GRSM data, not toy data.

## 11. Einstein Investigation: Candidate Source-Equivalence Law

The Einstein move is to ask whether the missing input should be a new law.

The candidate law is:

$$
\boxed{
\hbox{source-equivalent finite paths carry equal value, up to licensed
finite curvature.}
}
$$

We call it:

$$
\boxed{
\mathrm{V4P21\text{-}FINITE\text{-}SOURCE\text{-}EQUIVALENCE}.
}
$$

## 12. Definition: Source-Equivalent Paths

Let \(G_Y\) be a licensed finite readout graph.  A path is a finite sequence
of readout edges:

$$
\boxed{
\gamma=e_1e_2\cdots e_k.
}
$$

Its boundary is:

$$
\boxed{
\partial\gamma=(\gamma^-,\gamma^+).
}
$$

Two paths \(\gamma\) and \(\gamma'\) are source-equivalent if:

$$
\boxed{
\partial\gamma=\partial\gamma'
}
$$

and all licensed source records not represented by the path agree between
the two path preparations.

This last clause is the anti-smuggling clause.  If a hidden source record
differs, the paths are not source-equivalent.

## 13. Candidate Law: Flat Version

The flat finite source-equivalence law says:

$$
\boxed{
\gamma\sim_Y\gamma'
\quad\Longrightarrow\quad
\sum_{e\in\gamma}\ell_e
=
\sum_{e\in\gamma'}\ell_e.
}
$$

Equivalently, every closed source-equivalent loop has zero value:

$$
\boxed{
\oint_C\ell=0.
}
$$

### Theorem 13.1: Flat Source Equivalence Gives A Potential

If the flat finite source-equivalence law holds on a connected graph, then
there exists:

$$
\boxed{
\Phi:{\mathcal Y}\to{\mathbb R}
}
$$

such that:

$$
\boxed{
\ell=B\Phi.
}
$$

Proof.  Flat source equivalence says every cycle integral of \(\ell\)
vanishes.  By Paper 20's graph exactness theorem, \(\ell\) is exact. \(\square\)

## 14. Candidate Law: Curved Version

The curved finite source-equivalence law allows an additive loop source:

$$
\boxed{
H:{\mathcal Z}_1(G_Y)\to{\mathbb R}.
}
$$

It says:

$$
\boxed{
\oint_C\ell=H(C)
}
$$

for every licensed source loop \(C\).

The license conditions are:

$$
\boxed{
\begin{array}{ll}
\mathrm{H1}:&H\hbox{ is declared before residual fitting},\\
\mathrm{H2}:&H(C^{-1})=-H(C),\\
\mathrm{H3}:&H(C_1+C_2)=H(C_1)+H(C_2),\\
\mathrm{H4}:&H\hbox{ has operational/GCR/GRSM meaning},\\
\mathrm{H5}:&H\hbox{ is stable under the declared refinement}.
\end{array}
}
$$

### Theorem 14.1: Curved Source Equivalence Gives A Connection

If the curved finite source-equivalence law holds, then there exist
\(\Phi\) and \({\mathcal A}^{hol}\) such that:

$$
\boxed{
\ell=B\Phi+{\mathcal A}^{hol},
\qquad
\oint_C{\mathcal A}^{hol}=H(C).
}
$$

Proof.  Choose any one-cochain \({\mathcal A}^{hol}\) with the licensed
cycle integrals \(H(C)\) on a cycle basis.  Then
\(\ell-{\mathcal A}^{hol}\) has zero cycle integrals, so it is exact:

$$
\boxed{
\ell-{\mathcal A}^{hol}=B\Phi.
}
$$

Thus the source law is a finite connection law. \(\square\)

## 15. Smuggling Tests For The Einstein Law

The source-equivalence law is acceptable only if it does not hide the answer.

### Test E1: Predeclaration

The readout graph, source records, and equivalence relation must be declared
before computing:

$$
\boxed{
\Omega_C.
}
$$

If equivalence is chosen after seeing the defect, the law is value-smuggling.

### Test E2: Nontrivial Falsifiability

The law must be able to fail.  A legitimate finite source-equivalence law
must allow a table with:

$$
\boxed{
\gamma\sim_Y\gamma'
\quad\hbox{but}\quad
\sum_{\gamma}\ell-\sum_{\gamma'}\ell\ne0
}
$$

to falsify the flat version.

If no possible finite table can falsify it, it is a definition, not a law.

### Test E3: Product Composition

For independent graphs \(G_1,G_2\), source values must add:

$$
\boxed{
\ell_{G_1\times G_2}
=
\ell_{G_1}+\ell_{G_2}.
}
$$

Holonomies must also add:

$$
\boxed{
H_{G_1\times G_2}(C_1+C_2)
=
H_{G_1}(C_1)+H_{G_2}(C_2).
}
$$

Failure of product composition means the law is not compatible with the
least-bias update structure inherited from Paper 19.

### Test E4: Coarse-Graining Consistency

If a graph is coarse-grained by a licensed map:

$$
\boxed{
\pi:G_Y\to G_{\bar Y},
}
$$

then path equivalence must descend:

$$
\boxed{
\gamma\sim_Y\gamma'
\quad\Longrightarrow\quad
\pi\gamma\sim_{\bar Y}\pi\gamma'
}
$$

unless the coarse-graining explicitly discards a licensed curvature/source
record.

### Test E5: No Row-Label Repackaging

The law may not use:

$$
\boxed{
Y(q)=\hbox{the row label of }q
}
$$

as a source.  That would make every value source trivial.

## 16. Einstein Law Audit

The finite source-equivalence law passes the audit only if:

$$
\boxed{
\begin{array}{c|c}
\hbox{test} & \hbox{required status}\\
\hline
\mathrm{E1} & \hbox{predeclared}\\
\mathrm{E2} & \hbox{falsifiable}\\
\mathrm{E3} & \hbox{product-compatible}\\
\mathrm{E4} & \hbox{coarse-graining-compatible}\\
\mathrm{E5} & \hbox{not a row-label disguise}
\end{array}
}
$$

The current corpus does not yet print enough physical source data to verify
all five tests for a specific \(Y\).  Therefore:

$$
\boxed{
\mathrm{V4P21\text{-}FINITE\text{-}SOURCE\text{-}EQUIVALENCE}^{cur}
=
\mathrm{LAW\text{-}CANDIDATE}.
}
$$

It is not proven by the current corpus.  It is also not refuted.  It is a
clean possible new law.

## 17. What The Einstein Law Would Buy

If adopted, finite source equivalence gives:

$$
\boxed{
\hbox{intrinsic value source}
\Longrightarrow
\hbox{potential or connection}.
}
$$

Thus the Paper-20 classification becomes structural, not merely procedural.

But the law still does not give numerical values.  It says only that the
numbers must come from:

$$
\boxed{
\Phi
\quad\hbox{or}\quad
(\Phi,{\mathcal A}^{hol}).
}
$$

So the final numerical source still requires either:

$$
\boxed{
\hbox{boundary values of }\Phi
}
$$

or:

$$
\boxed{
\hbox{cycle values }H(C).
}
$$

This is acceptable if those boundary or cycle values have independent
physical meaning.  It is smuggling if they are fitted only to reproduce the
GR/SM table.

## 18. External Calibration Option

If finite source equivalence is not adopted, the honest completion is:

$$
\boxed{
\hbox{GR/SM calibrated value source is external licensed input.}
}
$$

Then:

$$
\boxed{
\ell_{ij}
=
\log
\frac{W_{ij,+}^{GRSM}}{W_{ij,-}^{GRSM}}
-
\log
\frac{\rho_{ij,+}^{op}}{\rho_{ij,-}^{op}}
}
$$

is not derived from GCR readout.  It is supplied by the calibrated physical
theory.

This is not a failure of consistency.  It is a failure of intrinsic closure.

## 19. Decision Matrix

The two investigations give the following decision matrix:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{choice} & \hbox{what it gives} & \hbox{remaining burden}\\
\hline
\hbox{Feynman table} &
\hbox{decides flat/curved/split for printed data} &
\hbox{must print real data}\\
\hbox{Einstein law} &
\hbox{forces potential/connection form} &
\hbox{must justify law and print boundary/cycle values}\\
\hbox{external GR/SM} &
\hbox{supplies value ratios directly} &
\hbox{not intrinsic ISP closure}
\end{array}
}
$$

## 20. Paper 21 Verdict

The Feynman investigation is complete:

$$
\boxed{
\hbox{the classifier works on explicit finite data and cleanly separates
flat, curved, split, noisy, and repeated-edge cases.}
}
$$

The Einstein investigation is complete:

$$
\boxed{
\hbox{finite source equivalence is a coherent candidate law, but not proved
by the current corpus.}
}
$$

The honest final status is:

$$
\boxed{
\begin{array}{c|c}
\hbox{route} & \hbox{status}\\
\hline
\hbox{Feynman/source-table route} & \hbox{valid method; awaits real table}\\
\hbox{Einstein/source-equivalence route} & \hbox{valid law candidate; awaits
adoption or proof}\\
\hbox{support-only route} & \hbox{closed by no-squeeze no-go}
\end{array}
}
$$

## 21. Recommendation

Do not continue trying to derive values from support alone.

The next real step should be one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{R1}:&\hbox{adopt finite source equivalence as a new axiom and audit
it against E1--E5},\\
\mathrm{R2}:&\hbox{treat GR/SM calibration as external licensed source
input},\\
\mathrm{R3}:&\hbox{produce actual instrument/GCR bridge data and run Paper
20's table}.
\end{array}
}
$$

The most principled order is:

$$
\boxed{
\mathrm{R1}\quad\hbox{then}\quad\mathrm{R3}.
}
$$

That means: decide whether finite source equivalence is an acceptable law of
the theory, then demand real bridge data to instantiate it.

## 22. Testing The Einstein Law Against The Feynman Lab

The Einstein law must survive the same toy cases without becoming
unfalsifiable.

### Test 22.1: Flat Toy

For F1:

$$
\boxed{
\ell=\left(\frac12,\frac13,\frac56\right),
\qquad
\Omega=0.
}
$$

The flat law predicts:

$$
\boxed{
\ell=B\Phi.
}
$$

This is true with:

$$
\boxed{
\Phi=(0,\frac12,\frac56).
}
$$

So F1 supports the flat version.

### Test 22.2: Curved Toy With Predeclared Holonomy

For F2:

$$
\boxed{
\ell=\left(\frac12,\frac13,\frac34\right),
\qquad
\Omega=\frac1{12}.
}
$$

The flat law is falsified.  The curved law survives only if:

$$
\boxed{
H(012)=\frac1{12}
}
$$

was licensed independently.

Then:

$$
\boxed{
\ell=B\Phi+{\mathcal A}^{hol}.
}
$$

So F2 supports the curved version only under predeclared holonomy.

### Test 22.3: Curved Toy With Post-Hoc Holonomy

If \(H(012)\) is declared only after computing:

$$
\boxed{
\Omega=\frac1{12},
}
$$

then:

$$
\boxed{
H(012):=\Omega
}
$$

is not a law.  It is a repair label.

The verdict is:

$$
\boxed{
\mathrm{SMUGGLING}.
}
$$

This is the key anti-cheat result: the curved law is admissible only if the
cycle source is printed before the residual is used.

### Test 22.4: Split Toy

F3 has:

$$
\boxed{
\Omega=\frac1{12}
}
$$

and no licensed \(H\).  Therefore finite source equivalence gives:

$$
\boxed{
\mathrm{flat\ law\ falsified,\ curved\ law\ unavailable}.
}
$$

The result is:

$$
\boxed{
\mathrm{SPLIT}.
}
$$

Thus the Einstein law is falsifiable.  It does not automatically save every
table.

## 23. No-Free-Numbers Theorem

Even if finite source equivalence is adopted, it does not calculate the
values by itself.

### Theorem 23.1: Source Equivalence Is A Form Law, Not A Number Law

Assume finite source equivalence.  On a connected three-vertex triangle, the
flat law implies:

$$
\boxed{
\ell=B\Phi.
}
$$

But \(\Phi(s_1)-\Phi(s_0)\) and \(\Phi(s_2)-\Phi(s_0)\) remain free until
boundary/source values are printed.

In the curved case:

$$
\boxed{
\ell=B\Phi+{\mathcal A}^{hol}
}
$$

but the boundary values of \(\Phi\) and the cycle value \(H(012)\) remain
free until licensed source data print them.

Proof.  In the flat triangle, setting:

$$
\boxed{
\Phi(s_0)=0,\quad \Phi(s_1)=a,\quad \Phi(s_2)=c
}
$$

gives:

$$
\boxed{
\ell=(a,c-a,c)
}
$$

for arbitrary \(a,c\).  The law constrains \(\ell_{02}=\ell_{01}+\ell_{12}\),
but it does not choose \(a\) or \(c\).  In the curved case, an additional
free cycle value \(H(012)\) remains. \(\square\)

### Consequence 23.2

Finite source equivalence can close the ontology:

$$
\boxed{
\hbox{value is potential or connection.}
}
$$

It cannot close the numerical table without:

$$
\boxed{
\hbox{boundary potential data or cycle curvature data.}
}
$$

This is why Paper 21 cannot honestly declare complete value closure from the
law alone.

## 24. Three Possible Axiom Packages

The Einstein route now has three possible strengths.

### Package A: Flat Source Equivalence

Declare:

$$
\boxed{
\oint_C\ell=0
\quad\hbox{for every licensed source loop }C.
}
$$

This forces:

$$
\boxed{
\ell=B\Phi.
}
$$

Advantage: simplest intrinsic ontology.

Risk: falsified by stable nonzero bridge cycles.

### Package B: Curved Source Equivalence

Declare:

$$
\boxed{
\oint_C\ell=H(C)
}
$$

with independently licensed \(H\).

This forces:

$$
\boxed{
\ell=B\Phi+{\mathcal A}^{hol}.
}
$$

Advantage: can absorb real finite value curvature.

Risk: becomes unfalsifiable if \(H\) is allowed post hoc.

### Package C: External Calibration

Declare:

$$
\boxed{
\ell\hbox{ is supplied by GR/SM calibration.}
}
$$

Advantage: honest and immediately usable if GR/SM data print.

Risk: does not prove intrinsic ISP value closure.

## 25. Final Paper 21 Decision

Both ideas have now been investigated.

The Feynman idea succeeds as a classifier test:

$$
\boxed{
\hbox{explicit finite tables produce the advertised FLAT, CURVED, and SPLIT
outcomes.}
}
$$

The Einstein idea succeeds as a form principle:

$$
\boxed{
\hbox{finite source equivalence forces potential or connection form.}
}
$$

But neither idea magically prints the missing physical values.

Thus the final Paper-21 conclusion is:

$$
\boxed{
\begin{array}{ll}
\mathrm{YES}:&\hbox{we have a coherent finite source-law candidate},\\
\mathrm{YES}:&\hbox{we have a working finite classifier},\\
\mathrm{NO}:&\hbox{the current corpus does not yet contain the source
numbers}.
\end{array}
}
$$

The clean next choice is:

$$
\boxed{
\hbox{adopt Package A or B as ontology, or explicitly use Package C as
external calibration.}
}
$$

## 26. Source Primitive Decision

We now fold the proposed Paper-22 source-primitive decision into the current
paper.  The issue is no longer Route A versus Route B.  The issue is:

$$
\boxed{
\hbox{what kind of object is allowed to supply value information?}
}
$$

The candidate primitives are:

$$
\boxed{
\begin{array}{ll}
\mathrm{P1}:&\hbox{external GR/SM calibration},\\
\mathrm{P2}:&\hbox{flat finite source equivalence},\\
\mathrm{P3}:&\hbox{curved finite source equivalence},\\
\mathrm{P4}:&\hbox{operational instrument/GCR source table},\\
\mathrm{P5}:&\hbox{boundary/action/variational source law}.
\end{array}
}
$$

Each primitive must be tested by the same audit:

$$
\boxed{
\begin{array}{ll}
\mathrm{A1}:&\hbox{predeclared},\\
\mathrm{A2}:&\hbox{falsifiable},\\
\mathrm{A3}:&\hbox{composition-compatible},\\
\mathrm{A4}:&\hbox{coarse-graining-compatible},\\
\mathrm{A5}:&\hbox{noncircular},\\
\mathrm{A6}:&\hbox{numerically useful}.
\end{array}
}
$$

## 27. Primitive P1: External GR/SM Calibration

P1 declares:

$$
\boxed{
\ell_{ij}
=
\log
\frac{W_{ij,+}^{GRSM}}{W_{ij,-}^{GRSM}}
-
\log
\frac{\rho_{ij,+}^{op}}{\rho_{ij,-}^{op}}.
}
$$

Audit:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS} & \hbox{if GR/SM rule is declared before query}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{can disagree with instrument/GCR bridge}\\
\mathrm{A3} & \mathrm{PASS/OPEN} & \hbox{depends on GR/SM product sector}\\
\mathrm{A4} & \mathrm{PASS/OPEN} & \hbox{depends on calibration under reduction}\\
\mathrm{A5} & \mathrm{PASS} & \hbox{not a row-label rename if physically calibrated}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints numbers once GR/SM data are supplied}
\end{array}
}
$$

Verdict:

$$
\boxed{
\mathrm{P1}\hbox{ is usable but external.}
}
$$

It completes value control, but not intrinsic ISP value closure.

## 28. Primitive P2: Flat Finite Source Equivalence

P2 declares:

$$
\boxed{
\oint_C\ell=0
\quad\hbox{for licensed source loops}.
}
$$

Thus:

$$
\boxed{
\ell=B\Phi.
}
$$

Audit:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS} & \hbox{can be declared as a law}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{stable nonzero }\Omega_C\hbox{ falsifies it}\\
\mathrm{A3} & \mathrm{PASS} & \hbox{potentials add under products}\\
\mathrm{A4} & \mathrm{PASS/OPEN} & \hbox{coarse-graining must preserve source records}\\
\mathrm{A5} & \mathrm{PASS} & \hbox{if }Y\hbox{ is not a row label}\\
\mathrm{A6} & \mathrm{FAIL} & \hbox{does not print boundary values of }\Phi
\end{array}
}
$$

Verdict:

$$
\boxed{
\mathrm{P2}\hbox{ is an admissibility/form law, not a numerical source.}
}
$$

It is the cleanest Einstein ontology, but it cannot by itself compute the
edge ratios.

## 29. Primitive P3: Curved Finite Source Equivalence

P3 declares:

$$
\boxed{
\oint_C\ell=H(C)
}
$$

with independently licensed \(H\).  Thus:

$$
\boxed{
\ell=B\Phi+{\mathcal A}^{hol}.
}
$$

Audit:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS/FAIL} & \hbox{passes only if }H\hbox{ is predeclared}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{wrong }H\hbox{ falsifies it}\\
\mathrm{A3} & \mathrm{PASS} & \hbox{additive holonomies compose}\\
\mathrm{A4} & \mathrm{PASS/OPEN} & \hbox{coarse-graining must transport }H\\
\mathrm{A5} & \mathrm{PASS/FAIL} & \hbox{fails if }H\hbox{ is residual-fitting}\\
\mathrm{A6} & \mathrm{PARTIAL} & \hbox{prints cycle values if }H\hbox{ is physical}
\end{array}
}
$$

Verdict:

$$
\boxed{
\mathrm{P3}\hbox{ is admissible only with an independently licensed }H.
}
$$

It is the best ontology if stable nonzero bridge curvature appears.

## 30. Primitive P4: Operational Instrument/GCR Source Table

P4 declares that finite records print:

$$
\boxed{
Y,\quad
\ell_{01},\ell_{12},\ell_{02},
\quad
\zeta_{01},\zeta_{12},\zeta_{02}.
}
$$

Audit:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS/OPEN} & \hbox{depends on instrument/GCR protocol}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{repeated-edge and cycle tests can fail}\\
\mathrm{A3} & \mathrm{OPEN} & \hbox{must prove product behavior of records}\\
\mathrm{A4} & \mathrm{OPEN} & \hbox{must prove readout stability under reduction}\\
\mathrm{A5} & \mathrm{OPEN} & \hbox{must exclude row-label repackaging}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints numbers if actual}
\end{array}
}
$$

Verdict:

$$
\boxed{
\mathrm{P4}\hbox{ is the Feynman number source, but current corpus has not
printed it.}
}
$$

It is the most empirical route.

## 31. Primitive P5: Boundary/Action/Variational Source Law

P5 declares that a finite boundary or action principle prints the source
potential or holonomy:

$$
\boxed{
\Phi=\Phi_{\partial/action}
\quad\hbox{or}\quad
H=H_{\partial/action}.
}
$$

Audit:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS} & \hbox{if boundary/action law is declared first}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{wrong predictions can fail bridge tests}\\
\mathrm{A3} & \mathrm{PASS/OPEN} & \hbox{depends on additivity/locality of action}\\
\mathrm{A4} & \mathrm{PASS/OPEN} & \hbox{depends on boundary reduction law}\\
\mathrm{A5} & \mathrm{PASS} & \hbox{if not fitted to row labels}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints numbers if law is explicit}
\end{array}
}
$$

Verdict:

$$
\boxed{
\mathrm{P5}\hbox{ would be ideal, but no such explicit finite law is printed
in the current corpus.}
}
$$

This is a possible future Einstein route.

## 32. Comparative Decision Table

The source primitive audit gives:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{primitive} & \hbox{ontology} & \hbox{numbers} & \hbox{current status}\\
\hline
\mathrm{P1} & \hbox{external calibration} & \hbox{yes if GR/SM prints} &
\mathrm{ADMISSIBLE\ EXTERNAL}\\
\mathrm{P2} & \hbox{flat potential form} & \hbox{no} &
\mathrm{ADMISSIBLE\ FORM}\\
\mathrm{P3} & \hbox{curved connection form} & \hbox{cycle values only if }H &
\mathrm{CONDITIONAL}\\
\mathrm{P4} & \hbox{operational/GCR data} & \hbox{yes if printed} &
\mathrm{OPEN}\\
\mathrm{P5} & \hbox{boundary/action law} & \hbox{yes if explicit} &
\mathrm{OPEN}
\end{array}
}
$$

## 33. Provisional Source Primitive Decision

The cleanest decision is a two-layer answer:

$$
\boxed{
\begin{array}{ll}
\hbox{admissibility layer}:&
\hbox{finite source equivalence},\\
\hbox{numerical layer}:&
\hbox{GR/SM calibration or instrument/GCR table}.
\end{array}
}
$$

That is:

$$
\boxed{
\mathrm{P2/P3}\hbox{ govern the allowed form, while }\mathrm{P1/P4/P5}
\hbox{ must print the numbers.}
}
$$

This avoids two mistakes.

First, it avoids pretending that support alone produces values:

$$
\boxed{
\hbox{support-only value closure remains false.}
}
$$

Second, it avoids pretending that GR/SM calibration is intrinsic ISP closure:

$$
\boxed{
\hbox{external calibration is allowed, but labeled external.}
}
$$

## 34. Einstein/Feynman Synthesis

Einstein supplies the form:

$$
\boxed{
\ell=B\Phi
\quad\hbox{or}\quad
\ell=B\Phi+{\mathcal A}^{hol}.
}
$$

Feynman demands the numbers:

$$
\boxed{
\Phi(s_i),\quad H(C),\quad \ell_{ij},\quad \zeta_{ij}.
}
$$

The synthesis is:

$$
\boxed{
\hbox{value law = source-equivalence form + licensed numerical source.}
}
$$

## 35. Final Current-Paper Verdict

The current paper now decides the source primitive question as far as the
corpus permits:

$$
\boxed{
\begin{array}{ll}
\mathrm{DECISION\ 1}:&
\hbox{adopt finite source equivalence as an admissibility principle},\\
\mathrm{DECISION\ 2}:&
\hbox{do not treat it as a number-producing law},\\
\mathrm{DECISION\ 3}:&
\hbox{allow GR/SM calibration as external source input},\\
\mathrm{DECISION\ 4}:&
\hbox{keep instrument/GCR bridge table as the intrinsic completion target},\\
\mathrm{DECISION\ 5}:&
\hbox{park boundary/action law until explicit finite formula is printed}.
\end{array}
}
$$

The remaining open problem is now extremely specific:

$$
\boxed{
\hbox{print a licensed numerical source: }\Phi,\ H,\ \ell,\hbox{ or an
instrument/GCR table.}
}
$$

That is the real frontier.
