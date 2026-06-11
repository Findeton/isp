# Relativistic ISP V3 Paper 26: Actual-Law Finite-Template Data Extraction, Atom Values, Residual Source, RN Ratios, RN-MIXAMP, And Evaluation For Adaptive Branch A

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: completed finite-template worksheet, atom-value source campaign,
residual-source ledger, `SEL2` RN-ratio bypass audit, minimal-edge RN-ratio
attempt, RN-MIXAMP value campaign, and data-gap verdict.  Paper 26 is not a
summary.  It takes the five actual-law Branch-A options frozen in Paper 25
and asks for the most concrete possible object: a finite same-law worksheet
on a chosen adaptive template from which all five frontier quantities can be
computed.

The result is decisive about the method.  A populated worksheet would decide
the five Paper-25 gates by finite scalar arithmetic.  The current Papers
20--25 do not populate that worksheet cofinally for the actual adaptive
pushed-forward `SEL2` law.  Paper 26 then attacks the first natural repair
inside the same paper: populate the exact residual atom values
\(\Phi_A^{N,j}\).  Paper 23 already gives the formal same-law Möbius atom
identity, but the current corpus does not supply the cofinal numerical
atom-value table or the uniform atom oscillation bounds needed by the
worksheet.  Paper 26 then unwinds the exact residual density
\(H_{RPF}^{N,j}\) itself and proves that sourcing it would populate the atoms
and the local conditional worksheet.  The same pass also proves that the
current corpus does not print the primitive density table needed to do this
cofinally.  Finally, Paper 26 tries the sharper ratio-only bypass: instead of
asking for the whole Radon-Nikodym density \(p_{N,j}\), ask only for the
four-point conditional log-ratios that survive one-site and normalization
cancellation.  This would populate the mixed conditional rows, but the current
corpus does not print those ratio values either.  The minimal-edge attempt
shows why: after all endpoint-additive, outside-only, and exact-entry `CE`
terms cancel, the RN-ratio source is exactly the surviving mixed `CleanRPF`
or true-bridge amplitude table.  Paper 26 then attacks that table directly as
`RN-MIXAMP(D)`: it prints the value table, repeats the structural-zero sweep,
states the exact smallness tests that would close Branch A, and states the
lower-floor route that would falsify Branch A.  The current corpus supplies
neither the required smallness values nor the lower floor.  Therefore Paper 26
does not prove confinement and does not falsify adaptive Branch A.  It proves
the exact data gaps:

```math
\mathrm{P26\text{-}ACTLAW\text{-}DATA\text{-}GAP}
\quad\text{and}\quad
\mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP}
\quad\text{and}\quad
\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE\text{-}GAP}
\quad\text{and}\quad
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}GAP}
\quad\text{and}\quad
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}ATTEMPT\text{-}GAP}
\quad\text{and}\quad
\mathrm{P26\text{-}RN\text{-}MIXAMP\text{-}VALUE\text{-}GAP}.
```

The next progress, if the program stays in Branch A, must supply actual
finite conditional probabilities, actual residual Hamiltonian coefficients,
mixed `SEL2` RN-ratios, actual atom values or atom oscillation bounds, or a
theorem that evaluates them.

## 0. Barandes-Aligned Boundary

Every object in this paper is a finite scalar record of the same adaptive
pushed-forward `SEL2` law.  The paper does not introduce:

1. a continuum Yang-Mills probability measure;
2. a Wilson-loop area-law input;
3. an off-law heat-kernel subprocess;
4. a gauge-fixed Markov factor;
5. a latent physical sheet or flux-tube variable;
6. an unrecorded conditional independence assumption.

The goal is finite and modest: extract actual scalar row values from the
declared whole-process law, or prove that the current papers have not supplied
enough information to do so.

## 1. Import Contract From Paper 25

Paper 25 Corollary 16.10 freezes five Branch-A truth statements:

```math
{\mathsf T}_1,\ldots,{\mathsf T}_5.
```

They are, respectively:

1. a strict cofinal Dobrushin row
   \(\exists a>0:\mathfrak D_{sharp}^{cof}(a)<1\);
2. a screened shell bound \(S_r\le AC_{sh}e^{-(\mu-h_{sh})r}\) with the
   strict screened margin;
3. a Peter-Weyl step contraction
   \(\Theta_L+\Kappa_L\le\theta\) beating path entropy;
4. a Peter-Weyl tail profile \(\kappa_{PW}^{N,j}(L(N,j))\to0\) together with
   a passing projected table;
5. `BRIDGEDAMP(D)+KTAIL(kappa)` passing the bridge gate.

Paper 25 proves that the current closed scalar corpus decides none of these.
Paper 26 asks whether a concrete finite-template extraction can decide them.

## 2. Template Ladder

### Definition 2.1: Admissible Template

An admissible template \({\mathfrak T}^{N,j}\) is a finite set of scalar
records containing:

1. a rooted live pair \((x,y)\);
2. every scalar record needed to evaluate the local adaptive conditional law
   around \((x,y)\);
3. the declared exact-entry `BC/CE` scalar records used by the residual law;
4. all true-bridge flags and amplitudes touching \((x,y)\);
5. the finite Peter-Weyl channels retained at cutoff \(L\);
6. enough outside labels \(\zeta\) to condition on the Markov blanket used by
   the template.

No template is admissible unless it is evaluated under the actual
\(\nu_{N,j}^{act}\).

### Definition 2.2: Template Ladder

Use the conservative ladder:

| label | template | purpose |
|---|---|---|
| \({\mathfrak T}_0^{edge}\) | minimal live rooted two-site RPF edge plus blanket | cheapest possible row and edge-matrix test |
| \({\mathfrak T}_1^{edge}\) | one-action-range rooted local template | catches adjacent action/collar leakage |
| \({\mathfrak T}_{BTQ}^{edge}\) | bounded-collar quotient template | removes stagnant bounded-collar cycles already identified |
| \({\mathfrak T}_{99}^{edge}\) | full over-refined Paper-21/Paper-23 carrier | complete finite cover, maximal bookkeeping cost |

The order is part of the method: do not pay the entropy of a larger template
unless the smaller template fails because it genuinely omits a needed actual
record.

## 3. The Paper-26 Worksheet

### Definition 3.1: Actual Template Law

For an admissible template \({\mathfrak T}\), write

```math
\nu_{{\mathfrak T}}^{N,j}
:=
\left(\pi_{\mathfrak T}\right)_*\nu_{N,j}^{act}
```

for the finite marginal of the actual adaptive law on the template records.
For an outside label \(\zeta\), let

```math
p_{\mathfrak T}^{N,j}(\omega\mid\zeta)
```

be the conditional probability of the inside template state \(\omega\).

### Definition 3.2: Full Worksheet

For cutoff \(L\), define

```math
{\mathcal W}_{26}^{N,j}({\mathfrak T},L)
```

to be the finite table consisting of:

1. the inside state set \(\Omega_{\mathfrak T}^{N,j}\);
2. all outside labels \(\zeta\) retained by the template;
3. the exact conditional weights
   \(p_{\mathfrak T}^{N,j}(\omega\mid\zeta)\);
4. the one-site conditional kernels \(K_x,K_y\);
5. the two-site conditional kernels \(K_{xy}\);
6. conditional influence entries \(J_{uv}^{N,j}\) and oscillations
   \(\Delta_{uv}^{N,j}\) for all template sites \(u,v\);
7. screened shell sums \(S_r^{N,j}\);
8. centered Peter-Weyl bases and Gram matrices at cutoff \(L\);
9. truncated edge matrices
   \(\Pi_{\le L}T_{e,\zeta}^{N,j}\Pi_{\le L}\);
10. truncation tails \(\Kappa_L^{N,j}\) and
    \(\kappa_{PW}^{N,j}(L)\);
11. true-bridge amplitudes \(d_A^{br}(x,y)\);
12. every scalar gate value from Paper 25.

This worksheet is finite for fixed \((N,j,{\mathfrak T},L)\).

### Lemma 3.3: Fixed Worksheet Finiteness

If \({\mathfrak T}\) is admissible and \(L<\infty\), then
\({\mathcal W}_{26}^{N,j}({\mathfrak T},L)\) is a finite scalar object.

Proof.

The template has finitely many scalar records and the retained Peter-Weyl
battery has finitely many channels.  Conditional probabilities, total
variation distances, oscillations, finite sums, Gram matrices, matrix norms,
and bridge amplitudes are finite algebraic or variational functions on this
finite table. `square`

### Definition 3.4: Populated Worksheet Source

`P26-ACTLAW-WORKSHEET({\mathfrak T},L)` asserts that the entries of
\({\mathcal W}_{26}^{N,j}({\mathfrak T},L)\) are printed or bounded
cofinally on the actual adaptive law with constants independent of the row
except through the declared cutoff schedule.

## 4. Extraction Of The Five Frontier Quantities

### Definition 4.1: Dobrushin Row Extractor

From \({\mathcal W}_{26}\), compute

```math
D_{DOB}^{N,j}(a;{\mathfrak T})
:=
\sup_{u\in{\mathfrak T}}
\sum_{v\ne u}
e^{a d_{RPF}(u,v)}
J_{uv}^{N,j}.
```

If \({\mathfrak T}\) is a complete row cover, this is the actual
\(D_{DOB}^{N,j}(a)\).  If \({\mathfrak T}\) is local, it is a lower or local
component unless a cover theorem sums the templates.

### Definition 4.2: Screened Shell Extractor

For \(r\ge1\), compute

```math
S_r^{N,j}({\mathfrak T})
:=
\sup_{u\in{\mathfrak T}}
\sum_{\substack{v\in{\mathfrak T}\\d(u,v)=r}}
\Delta_{uv}^{N,j}.
```

A complete cover plus shell-count ledger turns this into the Paper-25
screened shell quantity.

### Definition 4.3: Step Extractor

For the centered nontrivial Peter-Weyl edge matrices in the worksheet, compute

```math
\Theta_L^{N,j}({\mathfrak T})
:=
\sup_{e,\zeta}
\left\|\Pi_{\le L}T_{e,\zeta}^{N,j}\Pi_{\le L}\right\|_{osc\to osc}.
```

The step candidate is

```math
\Theta_L^{N,j}({\mathfrak T})+\Kappa_L^{N,j}({\mathfrak T}).
```

### Definition 4.4: Tail Extractor

Compute

```math
\kappa_{PW}^{N,j}(L;{\mathfrak T})
:=
\sup_{x,y}
\left\|
(I-\Pi_{\le L}^{xy})C_0^{m,N,j}(x,y)
\right\|_{edge}
```

on the actual minimal-edge residual Hamiltonian represented in the template.

### Definition 4.5: Bridge Extractor

For every true bridge \(A\) in the template, compute

```math
d_A^{br}(x,y)=\delta_\square(A;x,y).
```

Then compute the damping-test sum

```math
D_{br}^{N,j}({\mathfrak T})
:=
\operatorname*{ess\,sup}_{x,y}
\sum_{A\in{\mathcal U}_{br,0}^{N,j}(x,y)\cap{\mathfrak T}}
d_A^{br}(x,y).
```

## 5. Decisive Gate Theorem

### Theorem 5.1: A Populated Complete Worksheet Decides Branch-A Gates

Assume a cofinal family of populated complete worksheets

```math
{\mathcal W}_{26}^{N,j}({\mathfrak T}(N,j),L(N,j)).
```

Then the five Paper-25 Branch-A options are decidable by finite scalar tests:

1. if \(D_{DOB}^{N,j}(a)\le q<1\) cofinally for some \(a>0\), Branch A closes;
2. if \(S_r^{N,j}\le AC_{sh}e^{-(\mu-h_{sh})r}\) with the screened margin,
   Branch A closes;
3. if \(\Theta_L+\Kappa_L\le\theta\) with the step margin, Branch A closes;
4. if \(\kappa_{PW}^{N,j}(L(N,j))\to0\) and the projected finite table passes,
   Branch A closes;
5. if `BRIDGEDAMP(D)+KTAIL(kappa)` passes the bridge gate, Branch A closes.

If all five fail and the same worksheet also prints
\(\overline\Lambda_{13}^{RPF}\ge M_*\), adaptive Branch A is falsified.

Proof.

Items 1--5 are Paper 25 Theorems 3.1, 4.3, 5.2, 13.3, and 14.2.  The
falsification clause is Paper 25 Theorem 7.3 and Corollary 16.9: failure of
sufficient gates is not enough; the same-record lower floor is also required.
`square`

## 6. Minimal Live-Edge Worksheet

### Definition 6.1: Minimal Template Hamiltonian

For \({\mathfrak T}_0^{edge}\), let \(\zeta\) be the outside blanket label and
let \(u,v\) be the live endpoint records.  The formal template density is

```math
p_{0}^{N,j}(u,v\mid\zeta)
=
{1\over Z_{0}^{N,j}(\zeta)}
\exp\left\{
H_{0}^{N,j}(u,v;\zeta)
\right\},
```

where

```math
H_{0}^{N,j}(u,v;\zeta)
:=
\sum_{\substack{
A\in{\mathcal U}_{RPF,clean}^{N,j}\\
A\cap\{x,y\}\ne\varnothing
}}
\Phi_A^{N,j}(\omega_A^{u,v,\zeta}).
```

This is not a model replacement.  It is the formal conditional density of the
actual row restricted to the minimal live template.

### Lemma 6.2: What The Minimal Template Prints

\({\mathfrak T}_0^{edge}\) prints the formal expressions for:

1. \(K_x,K_y,K_{xy}\);
2. \(J_{xy}\) and \(\Delta_{xy}\);
3. the centered Peter-Weyl edge matrices;
4. the local bridge amplitudes meeting the edge.

Proof.

All four are finite functions of the density in Definition 6.1.  Substitute
that density into the definitions of conditional kernels, total variation,
oscillation, Gram matrices, and bridge amplitudes. `square`

### Proposition 6.3: Minimal Template Is Formal, Not Numerically Populated

The current Papers 20--25 do not populate
\({\mathcal W}_{26}^{N,j}({\mathfrak T}_0^{edge},L)\) cofinally.

Proof.

Definition 6.1 expresses every needed value in terms of the actual atom
values \(\Phi_A^{N,j}(\omega_A^{u,v,\zeta})\), normalization constants, and
conditional weights under \(\nu_{N,j}^{act}\).  Papers 20--25 define these
objects structurally and prove many identities and inequalities around them,
but they do not print their cofinal numerical values or sharp bounds on the
minimal live template.  Paper 25 Theorem 16.8 proves that the closed scalar
body admits completions with different truth values for the five gates.
Therefore the minimal worksheet is formally printed but not populated.
`square`

## 7. Template Enlargement Audit

### Lemma 7.1: Enlarging A Template Does Not Create Missing Values

If a smaller template fails only because actual conditional weights or atom
values are not populated, then enlarging to a bigger template does not by
itself populate them.

Proof.

Template enlargement adds scalar records and outside labels.  It may remove a
locality error or expose a missing interaction, but it cannot assign values to
the conditional probabilities of the actual law.  Those values must come from
\(\nu_{N,j}^{act}\) or a theorem about it. `square`

### Proposition 7.2: Ladder Verdict

The templates

```math
{\mathfrak T}_1^{edge},
\qquad
{\mathfrak T}_{BTQ}^{edge},
\qquad
{\mathfrak T}_{99}^{edge}
```

are legitimate finite same-law templates, but the current corpus does not
populate their Paper-26 worksheets cofinally.

Proof.

Paper 21 and Paper 23 license the finite carriers, canonical labels, BTQ
quotients, and rowwise finite tables.  Those results prove finiteness and
admissibility.  By Lemma 7.1, however, a larger finite carrier does not
produce the missing actual conditional probabilities, Peter-Weyl tails, or
bridge amplitudes.  The same Paper-25 truth-status obstruction remains.
`square`

## 8. Why Existing Sources Do Not Populate The Worksheet

### Lemma 8.1: Exact `BC/CE` Is Not A Conditional Table

Exact `BC/CE` identities identify legal block coefficients and central-entry
normalizations.  They do not print the conditional kernels
\(K_x(\cdot\mid\eta)\) of the residual adaptive law.

Proof.

The worksheet needs conditional probabilities after conditioning on an
outside template label.  `BC/CE` supplies exact algebraic evaluation rules for
selected block coefficients, not all conditional weights of the residual
finite law. `square`

### Lemma 8.2: Paper-16/Paper-19 Heat-Kernel Rows Do Not Populate It

Heat-kernel analytic rows from Papers 16 and 19 do not populate
\({\mathcal W}_{26}\) for \(\nu_{N,j}^{act}\).

Proof.

Those rows are real same-law rows for their declared heat-kernel towers.  The
Paper-26 worksheet is evaluated under the adaptive `SEL2` pushed-forward law
after exact `CE` division and RPF residualization.  No previous paper prints
the transfer identity equating those conditionals or tails. `square`

### Lemma 8.3: Finite Labels Are Not Values

Canonical labels, bounded collars, finite quotients, and rowwise finite
automata do not populate the worksheet values.

Proof.

They identify which entries must be read and prevent entropy from becoming
unbounded.  They do not assign numerical probabilities, oscillations, matrix
norms, spectral tails, or bridge amplitudes. `square`

### Lemma 8.4: Paper-24 Witnesses Do Not Populate The Actual Law

The Paper-24 witness family does not provide worksheet values for
\(\nu_{N,j}^{act}\).

Proof.

Paper 24 works over the closed scalar body \({\mathcal M}_{56}\) and shows
that body is too large for a universal certificate.  A witness inside the
body is not an identification of the actual element of the body selected by
the adaptive law. `square`

## 9. The Data-Gap Theorem

### Definition 9.1: Actual-Law Data Gap

`P26-ACTLAW-DATA-GAP` is the assertion that the current Papers 20--25 do not
print, bound, or otherwise determine a cofinal populated worksheet

```math
{\mathcal W}_{26}^{N,j}({\mathfrak T}(N,j),L(N,j))
```

for any template ladder choice sufficient to evaluate the five Paper-25
frontier gates.

### Theorem 9.2: Paper-26 Data-Gap Verdict

`P26-ACTLAW-DATA-GAP` holds.

Proof.

The worksheet is finite and decisive by Lemma 3.3 and Theorem 5.1.  The
minimal live template is formal but not populated by Proposition 6.3.
Template enlargement does not create the missing values by Lemma 7.1 and
Proposition 7.2.  The available source classes fail to populate the worksheet
by Lemmas 8.1--8.4.  Therefore no cofinal populated worksheet is supplied by
the current corpus. `square`

### Corollary 9.3: Consequence For Branch A

After Paper 26, adaptive Branch A remains neither closed nor falsified.  It
is no longer blocked by abstract gate ambiguity.  It is blocked by missing
actual-law data:

```math
\left\{
p_{\mathfrak T}^{N,j}(\omega\mid\zeta),
\Phi_A^{N,j}(\omega_A),
\Kappa_L^{N,j},
\kappa_{PW}^{N,j}(L),
d_A^{br}(x,y)
\right\}
```

cofinally on the adaptive `SEL2` law.

## 10. What Would Count As A Completed Future Evaluation

### Definition 10.1: Paper-26 Pass Package

A future pass package consists of:

1. a cofinal template schedule \({\mathfrak T}(N,j)\);
2. a cutoff schedule \(L(N,j)\);
3. a populated worksheet \({\mathcal W}_{26}^{N,j}\);
4. one passing Paper-25 scalar gate.

Then `P23-RPF-TRANS0` holds and adaptive Branch A closes.

### Definition 10.2: Paper-26 Negative Package

A future negative package consists of:

1. a populated worksheet;
2. proof that all five Paper-25 gates fail on the actual law;
3. the same-record lower floor
   \[
   \overline\Lambda_{13}^{RPF}\ge M_*.
   \]

Then adaptive Branch A is falsified as a route to the Paper-20 gate.

### Corollary 10.3: No Middle Claim

A rowwise formal worksheet without cofinal populated values is neither a pass
nor a falsification.

Proof.

This is exactly the distinction between Lemma 3.3 and Theorem 9.2. `square`

## 11. Completion Theorem

### Theorem 11.1: Paper-26 Completion

Paper 26 completes the actual-law finite-template data extraction campaign:

1. it defines the finite worksheet needed to evaluate all five Paper-25
   Branch-A gates;
2. it proves that a populated complete worksheet would decide those gates by
   finite scalar arithmetic;
3. it prints the minimal live-edge conditional density formally;
4. it proves that neither the minimal template nor larger Paper-21/Paper-23
   carriers are populated cofinally by the current corpus;
5. it proves `P26-ACTLAW-DATA-GAP`.

Proof.

Items 1--2 are Sections 3--5.  Item 3 is Section 6.  Item 4 is Sections 6--8.
Item 5 is Theorem 9.2. `square`

### Corollary 11.2: First Export After The Worksheet Pass

The next move should not be another abstract Branch-A gate paper.  It must do
one of the following:

1. supply actual adaptive `SEL2` conditional probabilities on a finite
   template;
2. supply exact atom values \(\Phi_A^{N,j}\) on the live template;
3. supply a cofinal Peter-Weyl tail profile for the residual Hamiltonian;
4. supply actual true-bridge amplitude/damping values;
5. leave Branch A and return to the parked Branch-B or Branch-C theorem
   packages.

Paper 26 now attacks item 2 internally.

## 12. Actual Atom-Value Source Campaign Inside Paper 26

The first repair to try is the most local one: fill the residual atom values
that the worksheet needs.  This section records what is already closed and
what is not.

### Definition 12.1: Formal RPF Atom Identity

Fix a finite live adaptive template \({\mathfrak T}^{N,j}\), a reference
inside configuration \(\omega^0\), and a finite active atom support
\(A\subset{\mathfrak T}^{N,j}\).  Let

```math
H_{RPF}^{N,j}(\omega)
```

denote the exact finite residual log-density contribution of the adaptive
`RPF` law on the template, after the declared `BC/CE` exact-entry division
and under the same pushed-forward scalar law \(\nu_{N,j}^{act}\).  The
formal residual atom is the finite Möbius difference

```math
\Phi_A^{N,j}(\omega_A)
:=
\sum_{B\subseteq A}(-1)^{|A|-|B|}
H_{RPF}^{N,j}\!\left(\omega_B,\omega^0_{A\setminus B}\right),
```

with the usual centering convention used in Paper 23.  Equivalently, the
family \(\{\Phi_A^{N,j}\}\) is the unique centered finite interaction
decomposition of the actual residual log-density on the chosen finite
template.

This is a same-law object.  No external heat-kernel measure, continuum
Yang-Mills measure, or Wilson-loop confinement assumption is introduced.

### Lemma 12.2: Formal Atom Existence Is Already Closed

Paper 23 already closes the formal identity: for every finite adaptive
template on which \(H_{RPF}^{N,j}\) is a finite scalar function, the Möbius
atoms \(\Phi_A^{N,j}\) exist and reconstruct the residual density.

Proof.

This is finite Möbius inversion on a finite product record space.  Paper 23
prints the literal atom definition and the reconstruction identity for the
actual residual density.  The operation is algebraic and takes place after
the same-law push-forward, so it is Barandes-aligned: it manipulates finite
observable records rather than adding a hidden continuum state. `square`

### Definition 12.3: Atom-Value Population Source

For a template ladder \({\mathfrak T}(N,j)\), write

```math
\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})
```

for the assertion that the current source corpus supplies, cofinally in
\((N,j)\), the following finite data under \(\nu_{N,j}^{act}\):

1. every active support \(A\) touching the template row;
2. every admissible local state \(\omega_A\) needed by the conditional
   kernels, influence rows, screened shells, bridge rows, and projected
   Peter-Weyl rows;
3. the exact values, or rigorous upper/lower intervals, of
   \(\Phi_A^{N,j}(\omega_A)\);
4. the row oscillations
   \[
   \operatorname{osc}_{u,v}\Phi_A^{N,j}
   \]
   whenever they enter \(J_{uv}^{N,j}\), \(\Delta_{uv}^{N,j}\), bridge
   damping, or screened conditional influence;
5. a tail certificate for all active supports not retained by the finite
   template, if the chosen template is not full.

The point of the definition is not that the atoms are finite; that is already
known.  The point is whether their actual values are populated sharply enough
to run the Paper-26 worksheet.

### Lemma 12.4: Atom Values Would Populate The Local Conditional Part

Assume \(\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})\), and assume
the base finite reference weights and normalizing constants for the template
conditionals are printed or bounded to the same precision.  Then the
conditional weights

```math
p_{\mathfrak T}^{N,j}(\omega\mid\zeta),
```

the kernels \(K_x,K_y,K_{xy}\), the conditional influence entries
\(J_{uv}^{N,j}\), and the screened shell sums \(S_r^{N,j}\) are finite
computations.

Proof.

On a finite template, the conditional log-density is the finite sum of the
base log-weight and all residual atoms touching the inside records, with
outside labels held fixed.  Exponentiation and normalization over the finite
inside state set produce \(p_{\mathfrak T}^{N,j}(\omega\mid\zeta)\).  The
one-site and two-site kernels are finite marginal and conditional sums.  The
influence and shell rows are finite suprema and finite sums of the resulting
kernel differences. `square`

### Lemma 12.5: Atom Values Alone Do Not Automatically Populate Every Row

\(\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})\) populates the
local conditional and influence rows, but it does not by itself populate a
Peter-Weyl tail profile or a true-bridge amplitude table unless those objects
are explicitly reduced to the same atom values with certified error bounds.

Proof.

The Peter-Weyl rows require spectral coefficients or projected matrix entries
of the residual transfer operation.  The bridge rows require the actual
bridge flags and damping amplitudes.  Both may be computable from atom values
on a sufficiently rich finite template, but only after an additional finite
projection or bridge-reduction identity is printed.  Pointwise atom values do
not imply those identities for free. `square`

### Lemma 12.6: Möbius Inversion Is Not Numerical Population

The Paper-23 Möbius identity does not prove
\(\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})\).

Proof.

The identity says that, given the exact finite residual function
\(H_{RPF}^{N,j}\), the atom values are finite alternating sums of its values.
It does not print or bound those values cofinally for the actual adaptive
`SEL2` law.  Algebraic definability is therefore strictly weaker than
worksheet population. `square`

### Lemma 12.7: Clean Coefficients Do Not Transfer Without A Same-Law Row Map

Paper-16 clean projective/covariance coefficients and Paper-20 heat-kernel
coefficient rows do not prove
\(\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})\) for the adaptive
`SEL2` law.

Proof.

Those coefficients live in their declared source laws.  The adaptive
worksheet is evaluated after exact scalar selection, `CE` division, and RPF
residualization.  A transfer would require a rowwise same-law identity
identifying the imported coefficient with the corresponding adaptive residual
atom value or oscillation.  Papers 20--25 do not print such an identity for a
cofinal live template. `square`

### Lemma 12.8: Finite Labels Do Not Supply Atom Values

Canonical labels, bounded-collar reductions, and finite active-support
automata do not prove
\(\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})\).

Proof.

They decide which atom slots may be present and can reduce the number of
slots that must be inspected.  They do not evaluate the actual residual
Hamiltonian on those slots.  A finite list of labels is not a finite list of
values. `square`

### Theorem 12.9: Atom-Value Data-Gap Verdict

The current Papers 20--25 prove

```math
\mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP}.
```

That is: they do not prove
\(\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})\) for any cofinal
template schedule sufficient to decide the Paper-25 Branch-A gates.

Proof.

Formal atom existence is closed by Lemma 12.2.  The missing statement is
cofinal value population.  Möbius inversion does not provide values without
the residual function values by Lemma 12.6.  Imported clean coefficients do
not transfer to adaptive atoms without a same-law row map by Lemma 12.7.
Finite labels and carrier reductions do not assign values by Lemma 12.8.
Therefore the current corpus supplies no cofinal populated atom-value table
for the adaptive worksheet. `square`

### Corollary 12.10: What The Atom Campaign Settles

The atom route is now exactly classified:

1. formal residual atoms \(\Phi_A^{N,j}\) exist on every finite adaptive
   template;
2. they reconstruct the actual finite residual density when that density is
   known;
3. their actual cofinal values and oscillation bounds are not supplied by the
   current papers;
4. atom-value population would be a genuine new same-law source theorem, not
   another notation change.

## 13. Completion After The Atom-Value Campaign

### Theorem 13.1: Paper-26 Completion After Atom Values

Paper 26 completes the actual-law finite-template data extraction and
atom-value source campaign:

1. it defines the finite worksheet needed to evaluate all five Paper-25
   Branch-A gates;
2. it proves that a populated complete worksheet would decide those gates by
   finite scalar arithmetic;
3. it prints the minimal live-edge conditional density formally;
4. it proves that neither the minimal template nor larger Paper-21/Paper-23
   carriers are populated cofinally by the current corpus;
5. it proves \(\mathrm{P26\text{-}ACTLAW\text{-}DATA\text{-}GAP}\);
6. it imports the Paper-23 formal atom identity and proves
   \(\mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP}\).

Proof.

Items 1--5 are Theorem 11.1.  Item 6 is Section 12. `square`

### Corollary 13.2: Export After The Atom-Value Campaign

The next continuation should not re-prove that atoms exist.  It must supply
one of the following genuinely new inputs:

1. actual adaptive `SEL2` conditional probabilities on a finite template;
2. actual residual density values \(H_{RPF}^{N,j}\), hence atom values
   \(\Phi_A^{N,j}\), with cofinal oscillation bounds;
3. a same-law Peter-Weyl projection and tail theorem for the residual
   transfer operation;
4. actual true-bridge amplitude/damping values;
5. a lower-floor theorem falsifying adaptive Branch A; or
6. a return to the parked Branch-B or Branch-C theorem packages.

Paper 26 does not prove confinement.  It sharply localizes the surviving
Branch-A obstruction: the program now needs new actual-law scalar data, not
new finite labels for already-defined slots.

## 14. Residual-Source Work Package: Unwind The Actual Law

This section executes the next repair inside Paper 26 rather than starting a
new paper.  The target is not another finite label or another atom definition.
The target is the primitive same-law residual log-density table.

### Definition 14.1: Actual Residual Density Chain

Use Paper 23 Definition 15.1.  For each adaptive row \((N,j)\), let

```math
\Gamma_{N,j}^{SEL2}
```

be the actual pushed-forward scalar law on the finite compact record space
\(\Omega_{N,j}\), and let \(\lambda_{N,j}\) be the finite reference
Haar/readout measure on the same coordinates.  On the essential support,
write

```math
d\Gamma_{N,j}^{SEL2}
=
p_{N,j}(\omega)\,d\lambda_{N,j}(\omega).
```

Let \(K_p^{CE,N,j}\) be the central one-plaquette factor already selected by
the exact-entry `CE` gate.  The exact residual density and residual
Hamiltonian are

```math
{\mathcal R}_{N,j}(\omega)
:=
Z_{N,j}
{p_{N,j}(\omega)\over
\prod_{p\in P_{N,j}}K_p^{CE,N,j}(\omega_p)},
\qquad
H_{RPF}^{N,j}(\omega):=\log {\mathcal R}_{N,j}(\omega).
```

Equivalently, on the essential support,

```math
H_{RPF}^{N,j}(\omega)
=
\log Z_{N,j}
+\log p_{N,j}(\omega)
-\sum_{p\in P_{N,j}}\log K_p^{CE,N,j}(\omega_p).
```

The constant \(\log Z_{N,j}\) is irrelevant for atom oscillations and
Dobrushin rows, but it is part of the normalized conditional density whenever
absolute conditional probabilities are requested.

### Lemma 14.2: This Is A Same-Law Identity

Definition 14.1 is an identity inside the adaptive pushed-forward scalar law.
It introduces no off-law heat-kernel subprocess and no continuum
Yang-Mills measure.

Proof.

All terms are functions of the finite record coordinates on
\(\Omega_{N,j}\).  The reference measure \(\lambda_{N,j}\) is the declared
record-coordinate reference used to write the density of
\(\Gamma_{N,j}^{SEL2}\); it is not a second physical law.  The `CE` factor is
the exact central-entry factor already divided out before the RPF residual is
formed. `square`

### Definition 14.3: Primitive Residual Source Package

For a cofinal template schedule \({\mathfrak T}(N,j)\), define

```math
\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE}({\mathfrak T})
```

to be the assertion that the following finite data are printed or rigorously
bounded cofinally on the actual adaptive `SEL2` law:

1. the finite state set and essential-support mask for the records retained
   by \({\mathfrak T}(N,j)\);
2. the exact density values \(p_{N,j}(\omega)\), or intervals sharp enough for
   the required atom and row oscillations, on every template state used by
   the worksheet;
3. the exact `CE` factors \(K_p^{CE,N,j}(\omega_p)\) on the same states;
4. the conditional outside-label weights needed to normalize
   \(p_{\mathfrak T}^{N,j}(\omega\mid\zeta)\);
5. if the template omits active records, a residual tail certificate bounding
   the omitted contribution to \(H_{RPF}^{N,j}\), its atoms, and the worksheet
   rows.

This is stronger than formal atom existence and weaker than proving
confinement: it is exactly the missing actual finite scalar table.

## 15. Primitive Source Ledger

### Proposition 15.1: Source Status Ledger

Relative to Papers 20--25, the primitive residual source package has the
following status.

| primitive | current status | reason |
|---|---|---|
| finite record space \(\Omega_{N,j}\) and template labels | closed as finite bookkeeping | Papers 21--23 print finite carriers and canonical labels |
| pushed-forward law \(\Gamma_{N,j}^{SEL2}\) | declared, not value-populated | the law is named, but its finite density table is not printed cofinally |
| density values \(p_{N,j}(\omega)\) | finite but unvalued | definability of a finite density is not a numerical table |
| `CE` factors \(K_p^{CE,N,j}\) | algebraically licensed | exact-entry division is closed, but this does not populate the residual density table |
| normalization \(Z_{N,j}\) | finite, oscillation-irrelevant, probability-relevant | constants drop from atoms but matter for absolute conditional weights |
| residual Hamiltonian \(H_{RPF}^{N,j}\) | formally defined, not populated | it needs \(p_{N,j}\) and the `CE` factors on the same states |
| atoms \(\Phi_A^{N,j}\) | formally closed, not value-populated | Paper 23 prints Möbius inversion; Paper 26 Section 12 proves value gap |
| Peter-Weyl tails and bridge amplitudes | not populated by this ledger | they need extra projection/bridge identities or direct tables |

Proof.

Each row is a direct import from Paper 23 Definition 15.1, Paper 23
Definition 15.2, Paper 25 Corollary 16.9, and Sections 9--12 of this paper.
The only delicate point is the `CE` row: exact `CE` is an algebraic
same-record division, not a conditional probability or residual atom table.
This is Lemma 8.1 in the present paper. `square`

### Corollary 15.2: The Minimal New Object

The smallest upstream object that would unlock the atom route is not another
atom label table.  It is the cofinal value table

```math
\left\{
\log p_{N,j}(\omega)
-\sum_{p}\log K_p^{CE,N,j}(\omega_p)
\right\}_{\omega\in{\mathfrak T}(N,j)}
```

with enough outside-label normalization data and enough omitted-record tail
control for the chosen template.

## 16. Same-Law Residual Identity And Atom Population

### Theorem 16.1: Residual Source Populates Atoms

If

```math
\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE}({\mathfrak T})
```

holds, then

```math
\mathrm{P26\text{-}ACTATOM\text{-}POP}({\mathfrak T})
```

holds, with atom-value and atom-oscillation intervals obtained by finite
Möbius arithmetic from \(H_{RPF}^{N,j}\).

Proof.

By Definition 14.1 the residual Hamiltonian values on the template are finite
same-law scalar values.  By Paper 23 Definition 15.2 and Lemma 15.3, each
atom is a finite alternating sum of those values against a fixed base
configuration.  Finite interval arithmetic propagates the residual-value
bounds to atom-value and oscillation bounds.  The omitted-record tail
certificate in Definition 14.3 supplies the error term when the template is
not full. `square`

### Corollary 16.2: Residual Source Populates The Local Worksheet

Assume
\(\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE}({\mathfrak T})\).
Then the local conditional part of

```math
{\mathcal W}_{26}^{N,j}({\mathfrak T},L)
```

is populated: conditional weights, one-site and two-site kernels,
conditional influence entries, and screened shell sums become finite scalar
computations.

Proof.

Theorem 16.1 gives the atom-value population source.  Lemma 12.4 then
computes the conditional weights and influence rows by finite normalization,
marginalization, and finite oscillation suprema. `square`

### Corollary 16.3: What Still Does Not Follow Automatically

The residual source package does not automatically supply:

1. a Peter-Weyl tail profile for the residual transfer operator;
2. projected edge-matrix norm bounds;
3. true-bridge amplitude damping;
4. the lower-floor theorem \(\overline\Lambda_{13}^{RPF}\ge M_*\).

Each requires a further same-law projection, bridge, or lower-floor theorem.

Proof.

This is Lemma 12.5 applied after the stronger residual-value source.  Values
on a finite template populate local conditionals, but spectral tails and
bridge damping are additional transforms unless the template is explicitly
enriched with the corresponding finite projection and bridge data. `square`

## 17. Run The Paper-26 Worksheet Under The Residual Source

### Theorem 17.1: Conditional Branch-A Rows Become Decidable

If
\(\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE}({\mathfrak T})\)
holds with a cofinal omitted-record tail small enough for the selected row,
then the direct Dobrushin and screened-shell options
\({\mathsf T}_1\) and \({\mathsf T}_2\) of Paper 25 become decidable by the
Paper-26 worksheet.

Proof.

Corollary 16.2 populates \(J_{uv}^{N,j}\), \(\Delta_{uv}^{N,j}\), and the
shell sums \(S_r^{N,j}\).  Paper 25 Theorems 3.1 and 4.1 give the exact
closing inequalities for direct Dobrushin and screened shell rows.  Therefore
the worksheet either verifies the corresponding strict inequalities or fails
them with explicit row values. `square`

### Theorem 17.2: Full Branch-A Decidability Requires The Extra Rows

A residual source package plus one of the following extra same-law packages
decides the corresponding remaining Paper-25 option:

1. a Peter-Weyl step projection and path-expansion table decides
   \({\mathsf T}_3\);
2. a Peter-Weyl tail profile plus projected finite-table values decides
   \({\mathsf T}_4\);
3. a bridge-amplitude/damping table plus the common tail profile decides
   \({\mathsf T}_5\).

Proof.

This is Paper 25 Corollary 16.9 written in Paper-26 worksheet notation.  The
residual source supplies the local conditional rows; the named extra packages
populate exactly the spectral, tail, and bridge rows not determined by local
atom values alone. `square`

### Theorem 17.3: Residual-Source Gap Verdict

The current Papers 20--25 prove

```math
\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE\text{-}GAP}.
```

That is, they do not prove
\(\mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE}({\mathfrak T})\) for
any cofinal template schedule sufficient to populate the Paper-26 worksheet.

Proof.

The finite record carriers and atom formulas are closed.  Proposition 15.1
shows that the actual density values \(p_{N,j}(\omega)\), the cofinal
residual Hamiltonian table, outside-label conditional normalizers, and
omitted-record tail certificate are not printed by the current corpus.  Since
Definition 14.3 requires exactly those primitive values, the residual source
package is not proved. `square`

## 18. Completion After The Residual-Source Pass

### Theorem 18.1: Paper-26 Completion After Residual Sourcing

Paper 26 completes the finite-template, atom-value, and residual-source
extraction campaign:

1. it defines the finite worksheet for the five Paper-25 Branch-A gates;
2. it proves populated worksheet decidability;
3. it imports the Paper-23 formal RPF atom identity;
4. it separates formal atom existence from atom-value population;
5. it unwinds the exact residual density identity
   \(H_{RPF}^{N,j}=\log Z+\log p-\sum_p\log K_p^{CE}\);
6. it proves that a primitive residual source would populate atoms and the
   local conditional worksheet;
7. it proves the three current-corpus gaps
   \[
   \mathrm{P26\text{-}ACTLAW\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE\text{-}GAP}.
   \]

Proof.

Items 1--4 are Sections 3--13.  Items 5--6 are Sections 14--17.  Item 7 is
Theorems 9.2, 12.9, and 17.3. `square`

### Corollary 18.2: Export After The Residual-Source Pass

The next continuation should target one of these, in order of leverage:

1. a cofinal primitive residual density table
   \[
   \log p_{N,j}(\omega)-\sum_p\log K_p^{CE,N,j}(\omega_p)
   \]
   with outside-label normalization and omitted-record tail control;
2. a direct cofinal conditional worksheet table, bypassing atom values;
3. a same-law Peter-Weyl projection/tail theorem for the residual transfer
   operation;
4. an actual true-bridge amplitude/damping theorem;
5. a lower-floor theorem falsifying adaptive Branch A;
6. a return to Branch B or Branch C.

The highest-leverage positive route is item 1 because it feeds the atom
table, the conditional rows, and the screened-shell worksheet without
introducing any off-law object.

## 19. `SEL2` Radon-Nikodym Ratio Bypass

The residual-source pass asks for the full finite density table.  That is
stronger than the local row estimates need.  Dobrushin and screened-shell
rows are driven by mixed conditional variation.  Mixed variation is controlled
by four-point log-ratios, and those ratios cancel constants, normalizers, and
endpoint-additive terms.

### Definition 19.1: Full `SEL2` RN Factor Source

For a cofinal template schedule \({\mathfrak T}(N,j)\), define

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}FACTOR}({\mathfrak T})
```

to be the assertion that the actual density \(p_{N,j}\) of
\(\Gamma_{N,j}^{SEL2}\) admits a finite same-law factorization on the template:

```math
\log p_{N,j}(\omega)
=
C_{N,j}
+\sum_{\beta\in{\mathcal B}_{N,j}}
F_\beta^{N,j}(\omega_\beta),
```

where:

1. every factor \(F_\beta^{N,j}\) is a declared finite scalar record under
   the same pushed-forward `SEL2` law;
2. the factor list \({\mathcal B}_{N,j}\) is finite and cofinally specified;
3. every value of every factor touching \({\mathfrak T}(N,j)\) is printed or
   rigorously bounded;
4. omitted factors have a cofinal tail bound in every mixed ratio needed by
   the worksheet.

This is a density-source theorem, not a new physical measure.

### Definition 19.2: `SEL2` RN Mixed-Ratio Source

Fix a rooted live pair \((x,y)\) in a template and an outside label \(\zeta\).
For endpoint values \(u,u'\) at \(x\) and \(v,v'\) at \(y\), define the
same-law four-point density ratio

```math
Q_{p}^{N,j}(u,u';v,v'\mid\zeta)
:=
\log p_{N,j}(u,v,\zeta)
+\log p_{N,j}(u',v',\zeta)
-\log p_{N,j}(u,v',\zeta)
-\log p_{N,j}(u',v,\zeta).
```

Define the corresponding exact-entry residual ratio

```math
Q_{RPF}^{N,j}(u,u';v,v'\mid\zeta)
:=
Q_p^{N,j}(u,u';v,v'\mid\zeta)
-
\sum_{p\in P_{N,j}}
Q_{\log K_p^{CE,N,j}}(u,u';v,v'\mid\zeta),
```

where \(Q_{\log K_p^{CE,N,j}}\) is the same four-point difference applied to
\(\log K_p^{CE,N,j}\).  The assertion

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO}({\mathfrak T},\Delta)
```

means that, cofinally in \((N,j)\), all live template ratios
\(Q_{RPF}^{N,j}\) are printed or bounded and satisfy

```math
\sup_{e,\zeta,u,u',v,v'}
\left|Q_{RPF}^{N,j}(u,u';v,v'\mid\zeta)\right|
\le \Delta,
```

with a certified omitted-record error if \({\mathfrak T}\) is not full.

### Lemma 19.3: Full RN Factorization Implies RN Ratio Values

If
\(\mathrm{P26\text{-}SEL2\text{-}RN\text{-}FACTOR}({\mathfrak T})\) holds,
then the ratio values in
\(\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO}({\mathfrak T},\Delta)\)
are finite same-law arithmetic for some computable \(\Delta\).

Proof.

Substitute the finite factorization of \(\log p_{N,j}\) into the four-point
difference.  The constant \(C_{N,j}\) cancels.  Every factor depending only on
\(x\), only on \(y\), or only on the outside label \(\zeta\) cancels.  Only
factors whose support meets both endpoint sides survive.  The exact `CE`
four-point terms are algebraically licensed by the exact-entry audit.  The
omitted-factor tail in Definition 19.1 supplies the error. `square`

### Lemma 19.4: Ratio Source Is Weaker Than Full Density Source

The ratio source can hold even when the full density table is not printed.

Proof.

The ratio source only asks for mixed four-point differences.  It is blind to
normalizing constants, endpoint-additive terms, outside-only terms, and
one-site selector weights.  The full density table contains all of those.
Therefore the ratio assertion is strictly weaker as a data request. `square`

## 20. Ratio Control Of Conditional Rows

### Lemma 20.1: Four-Point Ratios Control Two-Site Log-Odds

For every finite row and outside label \(\zeta\), the conditional two-site
law satisfies

```math
\log
{p_{\mathfrak T}^{N,j}(u,v\mid\zeta)
 p_{\mathfrak T}^{N,j}(u',v'\mid\zeta)
\over
 p_{\mathfrak T}^{N,j}(u,v'\mid\zeta)
 p_{\mathfrak T}^{N,j}(u',v\mid\zeta)}
=
Q_{RPF}^{N,j}(u,u';v,v'\mid\zeta)
```

after all endpoint-additive and outside-only terms are cancelled.

Proof.

Write the conditional log-density as a sum of the residual Hamiltonian,
endpoint-additive terms, outside-only terms, and a normalizing constant.  The
four-point alternating difference annihilates every term depending on only
one endpoint, only the outside label, or no endpoint.  The surviving term is
exactly the residual four-point ratio of Definition 19.2. `square`

### Lemma 20.2: Ratio Bounds Give Influence Bounds

If
\(\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO}({\mathfrak T},\Delta)\)
holds, then every live two-site conditional influence entry in the template
is bounded by an explicit finite function of \(\Delta\).  A conservative
bound is

```math
J_{xy}^{N,j}\le \tanh(\Delta/4).
```

Equivalently, using the looser bound already compatible with Paper 23's
log-ratio gates,

```math
J_{xy}^{N,j}\le \sinh(\Delta/2).
```

Proof.

For finite two-site conditionals, a uniform bound on the mixed log-odds ratio
controls the projective diameter of the conditional kernel.  The Birkhoff
contraction estimate gives the \(\tanh(\Delta/4)\) form.  The
\(\sinh(\Delta/2)\) form is the looser Paper-23-compatible estimate used in
the marginal crossing route.  Both are finite scalar consequences of the same
ratio bound. `square`

### Corollary 20.3: RN Ratio Decides Direct And Screened Rows

If the ratio source supplies cofinal bounds
\(\Delta_{xy}^{N,j}\) for all live row pairs and the weighted sums

```math
\sup_x\sum_{y\ne x}e^{a d_{RPF}(x,y)}\tanh(\Delta_{xy}^{N,j}/4)
```

or the corresponding screened shells are finite and below the Paper-25
thresholds, then \({\mathsf T}_1\) or \({\mathsf T}_2\) holds.  If the same
computed sums exceed every admissible strict threshold and the lower-floor
package is supplied, the corresponding route is falsified.

Proof.

Lemma 20.2 gives the influence entries.  Paper 25 Theorems 3.1 and 4.1 give
the exact Dobrushin and screened-shell closure inequalities.  The lower-floor
condition is the Paper-25 requirement for falsifying Branch A rather than only
one route. `square`

### Corollary 20.4: Ratio Bypass Does Not Settle Spectral Or Bridge Rows

The RN-ratio source does not by itself prove Peter-Weyl tail decay, projected
edge-matrix contraction, true-bridge damping, or the lower-floor theorem.

Proof.

The ratio source controls finite mixed conditional variation.  Spectral tails
and bridge amplitudes are different transforms of the residual object.  They
require the extra same-law rows listed in Paper 25 Corollary 16.9. `square`

## 21. Three Outcomes Of The RN Audit

### Proposition 21.1: Exhaustive RN Outcomes

For the actual adaptive `SEL2` law, a future source theorem must land in one
of three mutually exclusive practical outcomes:

1. **full density outcome:** `P26-SEL2-RN-FACTOR` holds, hence the primitive
   residual table and atom table are populated;
2. **ratio-only outcome:** `P26-SEL2-RN-RATIO` holds while full density values
   remain unprinted; direct Dobrushin and screened-shell rows become
   decidable, but spectral/bridge rows remain separate;
3. **RN gap outcome:** neither full density values nor mixed ratios are
   supplied by the current construction.

Proof.

The full density outcome implies the ratio outcome by Lemma 19.3 and also
implies residual-source population by Definition 14.3.  If the ratio outcome
holds without the full density table, Lemma 19.4 describes exactly the
ratio-only case.  If neither source is supplied, the RN obstruction remains.
These cases exhaust the logical possibilities relevant to the Paper-26
worksheet. `square`

### Theorem 21.2: Current-Corpus RN-Ratio Verdict

The current Papers 20--25 prove

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}GAP}.
```

That is, they do not print or bound the cofinal four-point ratios
\(Q_{RPF}^{N,j}\) on a live adaptive template with enough precision to decide
the Paper-25 Dobrushin or screened-shell routes.

Proof.

Paper 23 defines the actual density and its literal atoms by finite
same-law algebra, but it does not print the density values \(p_{N,j}\) or the
mixed four-point density ratios.  Paper 25 proves that the direct Dobrushin
and screened-shell routes remain undecided by the current corpus.  Sections
14--18 of the present paper prove that the primitive residual density table is
not populated.  Since the ratio source is a weaker but still numerical
same-law source, and no previous paper prints the required four-point
ratio table or an equivalent factorization, the current corpus does not prove
`P26-SEL2-RN-RATIO`. `square`

## 22. Completion After The RN-Ratio Bypass

### Theorem 22.1: Paper-26 Completion After RN Ratios

Paper 26 completes the finite-template, atom-value, residual-source, and
RN-ratio extraction campaign:

1. the finite worksheet is decisive if populated;
2. formal atoms exist by same-law Möbius inversion;
3. full residual density values would populate atoms and local conditionals;
4. mixed RN ratios would bypass the full density table for Dobrushin and
   screened-shell rows;
5. the current corpus supplies none of the required cofinal value tables:
   \[
   \mathrm{P26\text{-}ACTLAW\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE\text{-}GAP},\quad
   \mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}GAP}.
   \]

Proof.

Items 1--3 are Sections 3--18.  Item 4 is Sections 19--20.  Item 5 is
Theorems 9.2, 12.9, 17.3, and 21.2. `square`

### Corollary 22.2: Export After The RN-Ratio Bypass

The highest-leverage next target is now sharpened to:

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO}({\mathfrak T},\Delta)
```

on a cofinal live adaptive template.  This is weaker than printing the full
actual density table and strong enough to decide the direct Dobrushin and
screened-shell routes.  If that cannot be supplied, the next alternatives are
the full residual density table, a same-law Peter-Weyl tail/projection
theorem, a true-bridge damping theorem, a lower-floor falsification theorem,
or a return to Branch B/C.

## 23. Minimal-Edge RN-Ratio Attempt

We now execute the endpoint target from Corollary 22.2 on the cheapest live
template.  The goal is to see whether the RN-ratio source is a genuinely new
shortcut or just a different presentation of the already isolated mixed
`CleanRPF` amplitude.

### Definition 23.1: Minimal RN-Ratio Template

Let

```math
{\mathfrak T}_{0}^{edge}(x,y;\zeta)
```

be the minimal rooted live edge template of Section 6 and Paper 23 Section
40.  The free endpoint records are \(u,u'\) at \(x\) and \(v,v'\) at \(y\);
the outside Markov blanket is fixed to \(\zeta\).  Define

```math
Q_{RPF,0}^{N,j}(u,u';v,v'\mid\zeta)
```

to be the four-point residual RN ratio of Definition 19.2 restricted to this
minimal template.

For a crossing clean atom
\(A\in{\mathcal U}_{cross,0}^{N,j}(x,y)\), write

```math
G_A(u,v;\zeta):=\Phi_A^{N,j}(\omega_A^{u,v,\zeta})
```

and define its mixed four-point difference

```math
\delta_A^{\square}(u,u';v,v'\mid\zeta)
:=
G_A(u,v;\zeta)+G_A(u',v';\zeta)
-G_A(u,v';\zeta)-G_A(u',v;\zeta).
```

### Lemma 23.2: Minimal RN-Ratio Ledger

On \({\mathfrak T}_{0}^{edge}\), every term entering the four-point residual
RN ratio belongs to exactly one of the following classes:

| term class | four-point status | source status |
|---|---|---|
| global normalizer \(C_{N,j}\), residual \(Z_{N,j}\) | cancels | no debit |
| outside-only selector or blanket factor | cancels | no debit |
| endpoint-only selector factor | cancels | no mixed debit |
| endpoint-additive atom | cancels | Paper 23 Lemma 45.3 |
| endpoint-blind atom | cancels | Paper 23 Lemma 49.2 |
| exact `CE` one-plaquette factor | subtracted in \(Q_{RPF}\) | algebraically licensed, no double charge |
| non-`CleanRPF` residual class | removed or assigned before this slot | Paper 23 no-double-charge audit |
| `CleanRPF` true mixed atom | survives | value not printed by current corpus |
| omitted active mixed atom | survives as tail | requires a tail certificate |

Proof.

The four-point alternating difference annihilates constants, outside-only
terms, one-endpoint terms, and endpoint-additive terms.  The residual ratio
subtracts the exact `CE` factor by definition, so `CE` is not charged again.
Paper 23's classifier removes non-`CleanRPF` rows before the live RPF source.
The only terms depending genuinely on both endpoint variables are the
crossing `CleanRPF` atoms, plus any omitted crossing atoms if the template is
not full. `square`

### Proposition 23.3: Minimal RN Ratio Equals The Mixed Clean Table

For every finite row and outside label,

```math
Q_{RPF,0}^{N,j}(u,u';v,v'\mid\zeta)
=
\sum_{A\in{\mathcal U}_{cross,0}^{N,j}(x,y)}
\delta_A^{\square}(u,u';v,v'\mid\zeta)
+E_{tail}^{N,j}(u,u';v,v'\mid\zeta),
```

where \(E_{tail}^{N,j}=0\) on a full minimal carrier and otherwise is the
omitted active mixed residual tail.

Proof.

Expand \(H_{RPF}^{N,j}\) into literal atoms using Paper 23 Lemma 15.3 and
then apply the four-point alternating difference.  Lemma 23.2 cancels every
non-crossing, endpoint-additive, endpoint-blind, assigned, or exact-entry
term.  The surviving finite sum is precisely the mixed difference of the
crossing `CleanRPF` atoms, with an explicit tail if the chosen template omits
active crossing atoms. `square`

### Definition 23.4: Minimal RN Mixed Amplitude

Define the minimal RN mixed amplitude

```math
D_{RN,0}^{N,j}(x,y)
:=
\operatorname*{ess\,sup}_{\zeta,u,u',v,v'}
\left|
\sum_{A\in{\mathcal U}_{cross,0}^{N,j}(x,y)}
\delta_A^{\square}(u,u';v,v'\mid\zeta)
+E_{tail}^{N,j}
\right|.
```

The cofinal source

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}T0}(\Delta_{xy})
```

asserts that \(D_{RN,0}^{N,j}(x,y)\le\Delta_{xy}\) cofinally for every live
edge in the selected template ladder.

### Corollary 23.5: The Ratio Attempt Is The Mixed-Amplitude Attempt

On the minimal live template,

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}T0}(\Delta_{xy})
```

is equivalent to a cofinal bound on the same mixed four-point amplitudes that
Paper 23 names as the minimal mixed/true-bridge table.

Proof.

Proposition 23.3 identifies the RN ratio with the finite sum of the mixed
crossing clean atom differences.  Paper 23 Lemmas 45.3, 49.2, and 49.3 state
that endpoint-additive and endpoint-blind rows carry zero mixed debit and
that the positive mixed rows are exactly the true-bridge rows. `square`

## 24. Row Test From The Minimal RN Attempt

### Definition 24.1: RN-Ratio Dobrushin Test

For \(a>0\), define the RN-ratio row estimate

```math
D_{RN\to DOB}^{N,j}(a)
:=
\sup_x\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
\tanh\!\left({D_{RN,0}^{N,j}(x,y)\over4}\right).
```

The conservative Paper-23-compatible variant replaces
\(\tanh(D/4)\) by \(\sinh(D/2)\).

### Theorem 24.2: RN-Ratio Row Pass Criterion

If, cofinally, for some \(a>0\),

```math
D_{RN\to DOB}^{N,j}(a)\le q<1,
```

then the direct actual-law Dobrushin route \({\mathsf T}_1\) holds and
adaptive Branch A closes.

Proof.

Definition 24.1 and Lemma 20.2 bound the actual conditional influence row.
Paper 25 Theorem 3.1 then closes adaptive Branch A from the direct actual-law
Dobrushin row. `square`

### Definition 24.3: RN-Ratio Screened Shell Test

For \(r\ge1\), define

```math
S_{RN}^{N,j}(r)
:=
\sup_x\sum_{y:d_{RPF}(x,y)=r}
\tanh\!\left({D_{RN,0}^{N,j}(x,y)\over4}\right).
```

### Theorem 24.4: RN-Ratio Screened Pass Criterion

If the cofinal shell estimate

```math
S_{RN}^{N,j}(r)\le A C_{sh}e^{-(\mu-h_{sh})r}
```

holds with the Paper-25 screened strict margin, then the screened-shell route
\({\mathsf T}_2\) holds and adaptive Branch A closes.

Proof.

The shell estimate bounds the actual screened conditional influence by Lemma
20.2.  Paper 25 Theorem 4.3 applies the optimized screened margin. `square`

### Corollary 24.5: What Must Be Numerically Small

The RN attempt passes only if the true mixed clean amplitudes satisfy a
cofinal weighted smallness condition.  The needed data are not support labels
but values:

```math
\left\{
\delta_A^{\square}(u,u';v,v'\mid\zeta):
A\in{\mathcal U}_{cross,0}^{N,j}(x,y)
\right\}.
```

## 25. Current-Corpus Verdict For The Minimal Attempt

### Theorem 25.1: Minimal RN-Ratio Attempt Verdict

The current Papers 20--25 prove

```math
\mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}ATTEMPT\text{-}GAP}.
```

More precisely, the minimal RN-ratio attempt reduces exactly to the true
mixed `CleanRPF`/bridge amplitude table, and the current corpus does not
bound that table in the closing range.

Proof.

Lemma 23.2 and Proposition 23.3 prove the exact reduction.  Paper 23 Lemmas
45.3, 49.2, and 49.3 close the structural zero classes and identify the
surviving mixed rows with true bridges.  Paper 25 Lemma 14.3 records that
finite bridge labels do not bound the amplitudes:
residual-tail completions can preserve the closed non-RPF ledgers and the
same finite labels while assigning \(O(1)\) mixed four-point amplitude to a
surviving bridge row.  Therefore the present corpus supplies neither
\(D_{RN,0}^{N,j}(x,y)\) nor the weighted/screened smallness conditions of
Theorems 24.2 and 24.4. `square`

### Corollary 25.2: What The Attempt Settles

The RN-ratio bypass is valuable but not independent.  It proves:

1. all endpoint-additive, endpoint-blind, outside-only, and exact-entry terms
   carry no RN mixed debit;
2. the only surviving minimal-edge RN ratio is the actual mixed
   `CleanRPF`/true-bridge amplitude;
3. the next positive theorem must bound that amplitude, not merely classify
   its support;
4. if such a bound is small in the weighted or screened row sense, Branch A
   closes through Paper 25.

## 26. Completion After The Minimal RN Attempt

### Theorem 26.1: Paper-26 Completion After The Minimal RN Attempt

Paper 26 completes the finite-template, atom-value, residual-source,
RN-ratio, and minimal-edge RN-attempt campaign:

1. the finite worksheet is decisive if populated;
2. formal atoms exist by same-law Möbius inversion;
3. full residual density values would populate atoms and local conditionals;
4. mixed RN ratios would bypass the full density table for Dobrushin and
   screened-shell rows;
5. on the minimal live edge, the mixed RN ratio equals the true mixed
   `CleanRPF`/bridge amplitude table;
6. the current corpus supplies none of the required cofinal value tables:
   \[
   \mathrm{P26\text{-}ACTLAW\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE\text{-}GAP},\quad
   \mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}GAP},\quad
   \mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}ATTEMPT\text{-}GAP}.
   \]

Proof.

Items 1--4 are Theorem 22.1.  Item 5 is Corollary 23.5.  Item 6 is Theorem
25.1 together with Theorems 9.2, 12.9, 17.3, and 21.2. `square`

### Corollary 26.2: Export After The Minimal RN Attempt

The highest-leverage next target is no longer an abstract RN-ratio theorem.
It is the value theorem

```math
\mathrm{P26\text{-}RN\text{-}MIXAMP}(D)
```

asserting a cofinal weighted or screened bound on the true mixed
`CleanRPF`/bridge amplitudes
\(\delta_A^{\square}\).  If it passes in the row tests of Section 24, adaptive
Branch A closes.  If it fails and a same-law lower floor
\(\overline\Lambda_{13}^{RPF}\ge M_*\) is supplied, adaptive Branch A is
falsified.  Without one of those two value theorems, Paper 26 parks Branch A
at missing actual-law mixed-amplitude data.

## 27. RN-MIXAMP Value Campaign

The minimal RN attempt leaves one value theorem.  This section attacks it
directly.  The target is no longer support classification, endpoint
cancellation, or a new quotient.  The target is the actual numerical size of
the surviving mixed `CleanRPF`/true-bridge amplitudes on the same adaptive
`SEL2` pushed-forward law.

### Definition 27.1: RN-MIXAMP Value Source

For a cofinal live template schedule, define

```math
\mathrm{P26\text{-}RN\text{-}MIXAMP}(D,a)
```

to be the assertion that, cofinally in \((N,j)\),

```math
\sup_x\sum_{y\ne x}
e^{a d_{RPF}(x,y)}
\tanh\!\left({D_{RN,0}^{N,j}(x,y)\over4}\right)
\le D
```

for the actual minimal RN mixed amplitudes of Definition 23.4.  The
screened-shell variant

```math
\mathrm{P26\text{-}RN\text{-}MIXAMP\text{-}SCR}(A,\mu,h_{sh},C_{sh})
```

asserts

```math
S_{RN}^{N,j}(r)
\le
A C_{sh}e^{-(\mu-h_{sh})r}
```

cofinally, where \(S_{RN}^{N,j}(r)\) is Definition 24.3.

### Definition 27.2: Closing And Falsifying Thresholds

The value campaign has two possible hard exits:

1. **positive exit:** there exist \(a>0\) and \(D<1\) such that
   \[
   \mathrm{P26\text{-}RN\text{-}MIXAMP}(D,a)
   \]
   holds, or the screened variant holds with the Paper-25 strict screened
   margin;
2. **negative exit:** the same actual-law table proves the lower floor
   \[
   \overline\Lambda_{13}^{RPF}\ge M_*.
   \]

The first exit closes adaptive Branch A.  The second falsifies adaptive
Branch A as a route through the Paper-20/Paper-22 loss gate.  Anything less is
not a closure.

### Lemma 27.3: Positive Exit Closes Branch A

If the positive exit of Definition 27.2 holds, adaptive Branch A closes.

Proof.

For the weighted case, Definition 27.1 is exactly the row estimate
of Definition 24.1 with \(D<1\).  Theorem 24.2 closes the direct actual-law
Dobrushin route.  For the screened case, Definition 27.1's screened variant
is the row estimate of Definition 24.3 with the Paper-25 strict screened
margin.  Theorem 24.4 closes the screened-shell route. `square`

### Lemma 27.4: Negative Exit Falsifies Branch A

If the actual-law value table proves
\(\overline\Lambda_{13}^{RPF}\ge M_*\) and all positive Paper-25 gates fail
on the same worksheet, then adaptive Branch A is falsified.

Proof.

Paper 25 makes failure of sufficient gates insufficient by itself.  The
same-record lower floor reaching \(M_*\) is the extra condition needed to
turn route failure into Branch-A falsification.  This is the lower-floor
clause already imported in Theorem 5.1 and Definition 10.2 of the present
paper. `square`

## 28. Live Mixed-Amplitude Table

### Definition 28.1: Literal Mixed-Amplitude Row

For every rooted live edge \(e=(x,y)\), define the literal row

| field | value |
|---|---|
| edge | \(e=(x,y)\) |
| outside label | \(\zeta\) |
| atom support | \(A\in{\mathcal U}_{cross,0}^{N,j}(x,y)\) |
| class | surviving `CleanRPF` |
| true-bridge flag | \(\beta_A(x,y)=1_{\{\delta_\square(A;x,y)>0\}}\) |
| mixed value | \(\delta_A^\square(u,u';v,v'\mid\zeta)\) |
| amplitude | \(\delta_\square(A;x,y)=\operatorname*{ess\,sup}|\delta_A^\square|\) |
| row contribution | \(\tanh(\delta_\square(A;x,y)/4)\), or the safe \(\sinh(\delta_\square(A;x,y)/2)\) |
| hull data | \(Y(A),\ell_{RPF}(A),\operatorname{diam}_{RPF}(A)\) |

The row is finite for every fixed \((N,j)\).  It is populated only when the
actual values of \(\delta_A^\square\) or rigorous intervals for them are
printed.

### Lemma 28.2: Table Equivalence With Paper-23 Sources

The literal mixed-amplitude table is the same value object as Paper 23's
minimal mixed census and true-bridge amplitude table:

```math
\mathrm{P26\text{-}RN\text{-}MIXAMP}
\quad\Longleftrightarrow\quad
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}MIXCENSUS}
\quad\Longleftrightarrow\quad
\mathrm{P23\text{-}RPF\text{-}MIN\text{-}BRIDGE}
```

up to the explicit choice of weighted/screened row norm.

Proof.

Paper 23 Lemma 49.3 identifies true bridges with active mixed rows, and
Paper 23 Definition 49.4 defines `MIN-BRIDGE(D)` by the same
\(\delta_\square\) amplitudes.  Proposition 23.3 of the present paper
identifies the RN ratio with the same mixed four-point table.  Therefore the
objects differ only in the norm used to summarize the same row values.
`square`

### Corollary 28.3: Labels Are Exhausted

The remaining problem is not which rows exist.  It is the size of the values
\(\delta_\square(A;x,y)\).

Proof.

Paper 23 and Sections 23--25 of this paper already classify endpoint-blind,
endpoint-additive, exact-entry, and non-`CleanRPF` rows.  The literal table
contains only the surviving true mixed rows. `square`

## 29. Final Structural-Zero Sweep

### Proposition 29.1: All Zero Classes Are Already Removed

On the minimal live template, the following rows carry zero RN-MIXAMP debit:

1. outside-only rows;
2. endpoint-blind rows;
3. endpoint-additive rows;
4. exact `CE` rows already divided out;
5. local/removable non-`CleanRPF` residual rows;
6. RP/Cov and surface/decorative ledgers already assigned outside this slot.

Proof.

Outside-only and endpoint-only rows cancel in the four-point difference.
Endpoint-additive rows vanish by Paper 23 Lemma 45.3.  Endpoint-blind rows
vanish by Paper 23 Lemma 49.2.  Exact `CE` rows are subtracted in
Definition 19.2.  Non-`CleanRPF` rows and already assigned ledgers are removed
by the no-double-charge audit imported in Paper 23 Sections 18--19 and used
again in Lemma 23.2 of this paper. `square`

### Corollary 29.2: No Further Structural Zero Theorem Is Available

Any further positive proof must bound the actual values of surviving
\(\delta_\square\) rows or prove signed cancellation among them.  It cannot
come from another endpoint-additive or support-label argument.

Proof.

Proposition 29.1 exhausts the zero classes licensed by the current corpus.
The surviving class is defined by \(\delta_\square>0\), so support
classification cannot make it zero. `square`

## 30. Actual-Law Smallness Attempt

### Definition 30.1: Same-Law Smallness Source

`P26-RN-MIXAMP-SMALL(D,a)` is the value theorem

```math
\mathrm{P26\text{-}RN\text{-}MIXAMP}(D,a)
\quad\text{with}\quad D<1.
```

The screened version is
`P26-RN-MIXAMP-SCR(A,mu,h_sh,C_sh)` with the Paper-25 strict screened margin.

### Lemma 30.2: What Would Prove Smallness

Smallness can be proved by any one of the following same-law value sources:

1. a direct bound on every \(\delta_\square(A;x,y)\) and a summable row count;
2. a signed cancellation theorem bounding the sum
   \(\sum_A\delta_A^\square\) before absolute values are taken;
3. a conditional spectral theorem implying the \(\tanh(D/4)\) row bound;
4. a bridge-damping theorem that implies the same \(\delta_\square\) row
   bound.

Each source must be evaluated under \(\Gamma_{N,j}^{SEL2}\).

Proof.

These are exactly the possible ways to bound Definition 27.1: bound each
summand and count, bound the signed sum, bound the conditional kernel
directly, or bound the equivalent bridge-amplitude object. `square`

### Theorem 30.3: Current Corpus Does Not Prove RN-MIXAMP Smallness

The current Papers 20--25 do not prove
`P26-RN-MIXAMP-SMALL(D,a)` or the screened smallness variant.

Proof.

Paper 25 Theorem 15.1 and Corollary 16.10 prove that the current corpus does
not decide the direct Dobrushin or screened-shell source.  Paper 23
Proposition 49.6 proves that true-bridge classification is finite but does
not supply an amplitude bound small enough for closure.  Paper 25 Lemma 14.3
states the exact obstruction: finite bridge labels do not bound
\(\delta_\square\), because residual-tail completions can preserve the closed
non-RPF ledgers and assign \(O(1)\) mixed four-point amplitude to a surviving
bridge row. `square`

## 31. Lower-Floor Falsification Attempt

### Definition 31.1: RN-MIXAMP Lower-Floor Source

`P26-RN-MIXAMP-FLOOR` is the assertion that the actual-law mixed-amplitude
table, together with any already assigned RP/Cov and surface ledgers, proves

```math
\overline\Lambda_{13}^{RPF}\ge M_*.
```

### Lemma 31.2: What Would Prove The Floor

A lower floor requires a same-law inequality showing that every admissible
completion of the actual adaptive branch carries RPF predebit at least
\(M_*\).  It is not enough to show that one sufficient positive gate fails.

Proof.

The Paper-23 and Paper-25 lower-floor clauses distinguish route failure from
Branch-A falsification.  A large observed row, by itself, may only defeat one
proof route.  A floor must lower-bound the actual RPF predebit entering the
Paper-20/Paper-22 denominator gate. `square`

### Theorem 31.3: Current Corpus Does Not Prove The Lower Floor

The current Papers 20--25 do not prove `P26-RN-MIXAMP-FLOOR`.

Proof.

Paper 25 Theorem 7.3 proves that the current corpus neither proves the
direct Dobrushin route nor the stronger lower floor
\(\overline\Lambda_{13}^{RPF}\ge M_*\).  Paper 23 records repeatedly that
without a same-record lower floor, failure of a source route is not
falsification.  The RN-MIXAMP table has now been identified with the same
true-bridge amplitude table, but its values are not populated; hence it
cannot prove the lower floor. `square`

## 32. RN-MIXAMP Value Verdict

### Theorem 32.1: RN-MIXAMP Current-Corpus Verdict

The current Papers 20--25 prove

```math
\mathrm{P26\text{-}RN\text{-}MIXAMP\text{-}VALUE\text{-}GAP}.
```

That is, they neither prove RN-MIXAMP smallness in the closing range nor prove
the lower floor needed to falsify adaptive Branch A.

Proof.

The table is finite and structurally reduced by Sections 28--29.  Positive
smallness is not proved by Theorem 30.3.  The lower floor is not proved by
Theorem 31.3.  Therefore the current corpus does not settle the actual
mixed-amplitude values. `square`

### Corollary 32.2: RN-MIXAMP Trichotomy

The next actual-law theorem must prove exactly one of:

1. `P26-RN-MIXAMP-SMALL`, closing Branch A through Dobrushin/screening;
2. `P26-RN-MIXAMP-FLOOR`, falsifying adaptive Branch A after route failure;
3. a new signed/spectral/bridge theorem that evaluates the same
   \(\delta_\square\) table by a different norm.

No further finite-label theorem can settle the branch.

## 33. Final Paper-26 Completion After RN-MIXAMP

### Theorem 33.1: Paper-26 Final Completion

Paper 26 completes the finite-template, atom-value, residual-source,
RN-ratio, minimal-edge RN-attempt, and RN-MIXAMP value campaign:

1. the finite worksheet is decisive if populated;
2. formal atoms exist by same-law Möbius inversion;
3. full residual density values would populate atoms and local conditionals;
4. mixed RN ratios would bypass the full density table for Dobrushin and
   screened-shell rows;
5. on the minimal live edge, the mixed RN ratio equals the true mixed
   `CleanRPF`/bridge amplitude table;
6. all structural zero classes have been exhausted;
7. RN-MIXAMP smallness and the RN-MIXAMP lower floor are both unproved by the
   current corpus;
8. the current corpus proves the six gaps
   \[
   \mathrm{P26\text{-}ACTLAW\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}ACTATOM\text{-}DATA\text{-}GAP},\quad
   \mathrm{P26\text{-}RPF\text{-}RESID\text{-}SOURCE\text{-}GAP},\quad
   \mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}GAP},\quad
   \mathrm{P26\text{-}SEL2\text{-}RN\text{-}RATIO\text{-}ATTEMPT\text{-}GAP},\quad
   \mathrm{P26\text{-}RN\text{-}MIXAMP\text{-}VALUE\text{-}GAP}.
   \]

Proof.

Items 1--5 are Theorem 26.1.  Item 6 is Proposition 29.1 and Corollary 29.2.
Item 7 is Theorems 30.3 and 31.3.  Item 8 is Theorem 32.1 together with the
gap theorems already listed in Theorem 26.1. `square`

### Corollary 33.2: Final Export After Paper 26

Paper 26 has reduced adaptive Branch A to actual-law mixed-amplitude values.
The next continuation should not add more finite labels.  It must do one of:

1. prove `P26-RN-MIXAMP-SMALL` by direct values, signed cancellation,
   conditional spectral contraction, or bridge damping;
2. prove `P26-RN-MIXAMP-FLOOR`, giving
   \(\overline\Lambda_{13}^{RPF}\ge M_*\) after route failure;
3. leave adaptive Branch A and return to Branch B/C.

This is the sharp endpoint of Paper 26.
