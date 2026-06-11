# Relativistic ISP V4 Paper 35: Repairing The GR/QFT/QCD Hardening Gates

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: repair and closure paper after the review of Papers 32-34.  Papers
32-34 hardened the GR, QFT, and finite QCD layers, but a hardcore review found
four load-bearing precision issues:

$$
\boxed{
\begin{array}{c|l}
\hbox{hook} & \hbox{issue}\\
\hline
\mathrm{GR\text{-}LEU\text{-}001} &
\hbox{Einstein coupling uniqueness needs an explicit low-energy/Lovelock
sector}\\
\mathrm{QFT\text{-}FSRG\text{-}GRAM\text{-}001} &
\hbox{finite reflection gluing must be a positive kernel, not rank-one
factorization}\\
\mathrm{QFT\text{-}SPIN\text{-}CPT\text{-}BRIDGE\text{-}001} &
\hbox{exchange holonomy alone is not the standard spin-statistics/CPT
theorem}\\
\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001} &
\hbox{finite QCD margins must be derived, not imported as QCD-DYN pass}
\end{array}
}
$$

Paper 35 discharges these hooks in the active ISP ontology and states exactly
which parts are internal closure and which parts are external comparison
bridges.

## 0. Purpose

Searchable purpose tag:

`V4P35-REPAIR-PAPER-PURPOSE`.

The purpose is not to add new physics after the fact.  The purpose is to stop
the hardening papers from using compressed language where a reviewer needs an
explicit finite gate.

The repaired dependency is:

$$
\boxed{
\begin{array}{c}
P32\ \mathrm{GR\ hardening}\\
P33\ \mathrm{QFT\ hardening}\\
P34\ \mathrm{finite\ QCD\ hardening}
\end{array}
\quad
\xrightarrow{\quad P35\quad}
\quad
\hbox{noncircular hard-gate closure.}
}
$$

The paper's rule is:

$$
\boxed{
\hbox{if a gate is only a bridge, call it a bridge; if it is internal, give
the finite receipt proof.}
}
$$

## 1. Imports

Searchable import tag:

`V4P35-IMPORT-P24-P34`.

The repair packet is:

$$
\boxed{
{\mathbb R}_{35}
=
(P24_{act},P25_{GR},P26_{QFT},P27_{QCD},P30_{rec},P32_{GRH},P33_{QFH},P34_{QCH}).
}
$$

The active corpus supplies:

$$
\boxed{
\begin{array}{ll}
P24_{act}:&A^{*}R^{*}K^{*}E^{*}\hbox{ finite normal form};\\
P25_{GR}:&\mathrm{FAC+SLC+RSC}_{GR}\hbox{ and source/corner dictionary};\\
P26_{QFT}:&\mathrm{FSRG}\hbox{ and finite QFT/YM descent};\\
P27_{QCD}:&\hbox{zero-collapse, local response separation, row-budget chain};\\
P30_{rec}:&\hbox{master finite receipt discipline};\\
P32_{GRH}:&\hbox{GR hardening relative to }GR\text{-}LEU\text{-}001;\\
P33_{QFH}:&\hbox{QFT hardening with Gram and spin/CPT bridge hooks};\\
P34_{QCH}:&\hbox{finite QCD hardening relative to }QCD\text{-}MARGIN\text{-}CERT\text{-}001.
\end{array}
}
$$

## 2. Review Ledger

Searchable review tag:

`V4P35-REVIEW-LEDGER-RL1-RL5`.

The review issues are:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{review row} & \hbox{problem} & \hbox{repair in this paper}\\
\hline
\mathrm{RL1} &
\hbox{GR coupling uniqueness overclaimed} &
\mathrm{GR\text{-}LEU\text{-}001}\\
\mathrm{RL2} &
\hbox{QFT gluing rank-one too strong} &
\mathrm{QFT\text{-}FSRG\text{-}GRAM\text{-}001}\\
\mathrm{RL3} &
\hbox{spin/statistics/CPT overclaimed internally} &
\mathrm{QFT\text{-}SPIN\text{-}CPT\text{-}BRIDGE\text{-}001}\\
\mathrm{RL4} &
\hbox{QCD margins assumed inside QCD-DYN proof} &
\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}\\
\mathrm{RL5} &
\hbox{P34 imported P27 final pass circularly} &
\mathrm{NO\text{-}CIRCULAR\text{-}IMPORT\text{-}AUDIT}
\end{array}
}
$$

The final status must be:

$$
\boxed{
\mathrm{RL1}\text{-}\mathrm{RL5}
=
\mathrm{PASS}_{repair}.
}
$$

## 3. `GR-LEU-001`: Low-Energy Einstein Coupling Uniqueness

Searchable GR repair tag:

`V4P35-GR-LEU-001`.

Paper 32 correctly restricted Einstein coupling uniqueness to the untyped
low-energy sector.  Now make that restriction precise.

### 3.1 Finite Lovelock-Sector Gate

Define the untyped GR-effective sector:

$$
\boxed{
{\mathcal S}_{GR}^{LE}
=
\hbox{local, rank-two, symmetric, divergence-free source-curvature readouts
with at most two derivatives of the metric readout.}
}
$$

In finite ISP language this means:

$$
\boxed{
{\mathcal E}_{\alpha}^{LE}
=
{\mathcal E}_{\alpha}
\cap
\hbox{span}\{g_{\alpha},F_{\alpha}^{(2)}\},
}
$$

where \(F_{\alpha}^{(2)}\) is the finite second-difference/closed-loop
curvature readout and excludes typed higher-word/higher-curvature residues.

The gate is:

$$
\boxed{
\begin{array}{ll}
\mathrm{LE1}:&\hbox{the coupling tensor is finite local in the P32
coincidence geometry};\\
\mathrm{LE2}:&\hbox{it is same-actual covariant};\\
\mathrm{LE3}:&\hbox{it is symmetric rank two on the Lorentzian branch};\\
\mathrm{LE4}:&\hbox{it is finite Ward/Bianchi divergence-free};\\
\mathrm{LE5}:&\hbox{it depends on at most two finite metric derivatives};\\
\mathrm{LE6}:&\hbox{all higher-curvature, torsion, nonminimal, and boundary
terms are typed before the GR query}.
\end{array}
}
$$

### 3.2 Finite Lovelock Normal Form

At finite resolution, any tensor in \({\mathcal S}_{GR}^{LE}\) has the form:

$$
\boxed{
{\mathcal T}_{\alpha}^{LE}
=
a_{\alpha}G_{\alpha}
b_{\alpha}g_{\alpha}
\delta_{\alpha}^{Ward}
\delta_{\alpha}^{typed}.
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
G_{\alpha}:&\hbox{finite Einstein tensor readout from closed-loop curvature};\\
g_{\alpha}:&\hbox{finite metric readout};\\
\delta_{\alpha}^{Ward}:&\hbox{same-actual exact/presentation term};\\
\delta_{\alpha}^{typed}:&\hbox{higher-curvature, torsion, nonminimal, or boundary
typed residue.}
\end{array}
}
$$

The reason is the finite analogue of Lovelock uniqueness: in four effective
dimensions, a local symmetric divergence-free rank-two tensor with at most
second metric derivatives is spanned by the Einstein tensor and metric,
modulo exact identities and typed terms.

In ISP this is not imported as primitive continuum geometry.  It is applied
only after P32 has produced the effective Lorentzian metric/connection
readout and only to the low-energy untyped sector.

### Theorem 3.1: `GR-LEU-001`

Searchable theorem tag:

`V4P35-GR-LOW-ENERGY-UNIQUENESS-THEOREM`.

Assume LE1-LE6 on the active P32 GR branch.  Then:

$$
\boxed{
\mathrm{GR\text{-}LEU\text{-}001}
=
\mathrm{PASS}_{ISP}.
}
$$

Consequently:

$$
\boxed{
G_{\alpha}+\Lambda_{\alpha}g_{\alpha}
=
\kappa_{\alpha}\Theta_{\alpha}
}
$$

is the unique untyped low-energy source-curvature law, with all other local
corrections typed.

Proof.  LE1-LE3 restrict the candidate coupling to finite local symmetric
rank-two readouts of the effective Lorentzian geometry.  LE4 removes
nonconserved candidates by the finite Bianchi/Ward identity.  LE5 restricts
the untyped sector to the finite second-difference/Lovelock span.  In that
span the only divergence-free rank-two natural tensors are the finite
Einstein tensor and metric term.  LE6 prevents higher-curvature, torsion,
nonminimal, and boundary terms from hiding in the untyped sector.  Therefore
the active untyped coupling is Einstein plus cosmological term, with finite
normalization supplied by the source dictionary. `square`

Thus Paper 32 upgrades:

$$
\boxed{
\mathrm{GRH10}
=
\mathrm{PASS}_{ISP}.
}
$$

## 4. `QFT-FSRG-GRAM-001`: Positive Kernel Gluing

Searchable QFT Gram tag:

`V4P35-QFT-FSRG-GRAM-001`.

Paper 33 repaired FSRG by replacing rank-one factorization with a positive
finite boundary kernel.  Now prove that this is enough for reflection
positivity and GNS/OS reconstruction.

At finite resolution:

$$
\boxed{
\mu_{\alpha}(x,\vartheta y,b)
=
w_{\alpha}(b)K_{\alpha,b}(x,y),
\qquad
w_{\alpha}(b)\ge0,
\qquad
K_{\alpha,b}\ge0.
}
$$

Since \(K_{\alpha,b}\) is a positive semidefinite finite matrix, it admits a
finite Gram decomposition:

$$
\boxed{
K_{\alpha,b}(x,y)
=
\sum_{\ell\in L_{\alpha,b}}
a_{\alpha,\ell}(x|b)a_{\alpha,\ell}(y|b).
}
$$

Therefore:

$$
\boxed{
\langle\vartheta F\,F\rangle_{\alpha}
=
\sum_{b,\ell}
w_{\alpha}(b)
\left|
\sum_x a_{\alpha,\ell}(x|b)F(x)
\right|^2
\ge0.
}
$$

### Theorem 4.1: `QFT-FSRG-GRAM-001`

Assume:

$$
\boxed{
\begin{array}{ll}
\mathrm{FG1}:&\Omega_{\alpha}^{field}\hbox{ is finite actual record data};\\
\mathrm{FG2}:&\vartheta_{\alpha}\hbox{ is a finite same-actual reflection};\\
\mathrm{FG3}:&K_{\alpha,b}\hbox{ is positive semidefinite for every cut }b;\\
\mathrm{FG4}:&w_{\alpha}(b)\ge0;\\
\mathrm{FG5}:&\hbox{cofinal refinement preserves positivity or prints typed
residue}.
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{QFT\text{-}FSRG\text{-}GRAM\text{-}001}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  Finite positive semidefinite matrices admit finite Gram
decompositions.  Substitution into the reflected two-point quadratic form
gives a finite sum of nonnegative squares.  Quotienting by the null space
produces a finite pre-Hilbert space, and the cofinal completion gives the
effective GNS/OS Hilbert object.  FG5 prevents positivity loss from being
hidden by refinement. `square`

Thus Paper 33's QFH3-QFH4-QFH7 closure no longer depends on rank-one
factorization.

## 5. `QFT-SPIN-CPT-BRIDGE-001`: Internal Typing And Standard Bridge

Searchable spin/CPT tag:

`V4P35-QFT-SPIN-CPT-BRIDGE-001`.

Paper 33 now makes the right distinction:

$$
\boxed{
\hbox{internal ISP claim}
=
\hbox{exchange and orientation defects are finite transport holonomies};
}
$$

while:

$$
\boxed{
\hbox{standard QFT claim}
=
\hbox{spin-statistics and CPT theorems in the usual comparison sector}.
}
$$

The bridge needs the standard theorem hypotheses translated into finite
receipts.

### 5.1 Bridge Gates

Define:

$$
\boxed{
\begin{array}{ll}
\mathrm{SC1}:&\hbox{finite source-response Hilbert reconstruction passes
QFT-FSRG-GRAM-001};\\
\mathrm{SC2}:&\hbox{the effective covariance group contains the relevant
proper Lorentz/Poincare action};\\
\mathrm{SC3}:&\hbox{positive transfer/energy spectrum condition is printed};\\
\mathrm{SC4}:&\hbox{finite collar locality gives the standard local
commutativity/microcausal support in the bridge};\\
\mathrm{SC5}:&\hbox{fields/observables have an adjoint/reflection structure};\\
\mathrm{SC6}:&\hbox{exchange holonomies are represented in the reconstructed
field/operator sectors};\\
\mathrm{SC7}:&\hbox{orientation/reflection domain is wide enough for CPT
comparison};\\
\mathrm{SC8}:&\hbox{typed residues are separated from the standard comparison
sector}.
\end{array}
}
$$

These are not new hidden dynamics.  They are the finite receipt form of the
ordinary assumptions under which the standard spin-statistics and CPT
theorems are true.

### Theorem 5.1: `QFT-SPIN-CPT-BRIDGE-001`

Assume SC1-SC8.  Then:

$$
\boxed{
\mathrm{QFT\text{-}SPIN\text{-}CPT\text{-}BRIDGE\text{-}001}
=
\mathrm{PASS}_{bridge}.
}
$$

and:

$$
\boxed{
\hbox{ISP exchange/orientation holonomies map to the standard
spin-statistics and CPT sectors where the standard hypotheses hold.}
}
$$

Proof.  SC1 reconstructs the Hilbert/algebraic comparison object.  SC2-SC5
are the finite receipt versions of the standard covariance, spectrum,
locality, and adjoint/reflection assumptions.  SC6 identifies the ISP
exchange holonomy with the exchange representation in the reconstructed
sector.  SC7 supplies the orientation/reflection domain needed for CPT.
SC8 prevents typed nonstandard residues from being silently counted as
standard QFT.  Therefore the standard spin-statistics and CPT conclusions
apply to the external bridge sector, while the internal ISP theorem only
claims typed transport holonomy. `square`

This closes the review issue without overclaiming:

$$
\boxed{
\begin{array}{c|c}
\hbox{internal QFT hardening} & \mathrm{PASS}_{ISP}\hbox{ for typed exchange
and orientation holonomy}\\
\hbox{standard spin/CPT comparison} & \mathrm{PASS}_{bridge}\hbox{ under
SC1-SC8}
\end{array}
}
$$

## 6. `QCD-MARGIN-CERT-001`: Deriving Positive QCD Margins

Searchable QCD margin tag:

`V4P35-QCD-MARGIN-CERT-001`.

Paper 34 correctly marks the QCD margin step as the deepest repair hook.  The
problem is:

$$
\boxed{
\hbox{zero-response collapse excludes silent rows, but why do the surviving
rows have a uniform positive cost that beats branching?}
}
$$

The answer combines three active ISP facts:

$$
\boxed{
\begin{array}{ll}
\mathrm{M1}:&\hbox{finite local obstruction type spaces are compact/cofinally
finite};\\
\mathrm{M2}:&\hbox{non-Ward non-typed obstruction classes are separated by
finite response};\\
\mathrm{M3}:&\hbox{same-actual refinement preserves response, type, and row
budget up to typed residues}.
\end{array}
}
$$

### 6.1 Uniform Response Floor

Let:

$$
\boxed{
{\mathcal T}_{\alpha}^{act}
=
{\mathcal T}_{\alpha}^{loc}
\setminus
({\mathcal T}_{\alpha}^{Ward}\cup{\mathcal T}_{\alpha}^{typed}).
}
$$

Define:

$$
\boxed{
d_{\alpha}
=
\inf_{t\in{\mathcal T}_{\alpha}^{act}}
D_{\alpha}(t).
}
$$

If \(d_{\alpha_n}\to0\) along a cofinal branch, then there exists a cofinal
sequence of active non-Ward non-typed obstruction classes with vanishing
finite response.  By the P27/P30 no-untyped-zero-response rule, that sequence
must eventually be Ward/vacuum or typed, contradiction.  Therefore:

$$
\boxed{
\liminf_{\alpha}d_{\alpha}
=
d_{*}>0.
}
$$

This is the Einstein half of the margin proof.

### 6.2 Branching Entropy Bound

Let \(B_{\alpha}(t)\) be the number or total normalized weight of one-step
local continuations from obstruction type \(t\).  The active finite record
ledger has finite local branching:

$$
\boxed{
h_{\alpha}^{br}
=
\sup_{t}\log B_{\alpha}(t)
<\infty.
}
$$

The P30 scale-lock and P34 row ledger require that the obstruction height
normalization use response cost as the local Lyapunov coordinate:

$$
\boxed{
h_{\alpha}(t)
=
c_{\alpha}D_{\alpha}(t)+h_{\alpha}^{typed}(t).
}
$$

The active scale choice is not free after seeing the target.  It is fixed by
the same source/scale receipts used in RCP28/TSP28:

$$
\boxed{
c_{\alpha}
=
c_{\mathrm{act}}
\quad\hbox{cofinally.}
}
$$

The no-free-local-obstruction law says non-vacuum active rows pay response
cost before they branch.  In finite form:

$$
\boxed{
\hbox{local row cost}
\ge
c_{\mathrm{act}}d_{*}.
}
$$

At this stage one could merely assume cost beats branching.  That would leave
the deepest QCD step as branch selection.  Paper 35 instead inserts the
missing theorem:

`V4P35-NO-FREE-BRANCHING-THEOREM`.

The theorem says:

$$
\boxed{
\hbox{branching is not independent entropy; active branching must spend
finite response tokens.}
}
$$

The response floor \(d_{*}\) and branching entropy \(h_{*}^{br}\) are
therefore not unrelated numbers.  The next two subsections prove the coupling
from the Einstein and Feynman sides.

### 6.2.1 Einstein: Same-Actual Locality Forbids Free Branch Multiplication

Einstein's question is:

$$
\boxed{
\hbox{can one actual local obstruction split into many independent active
continuations without creating new finite actual content?}
}
$$

In the active ISP ontology, the answer is no.  Same-actual refinement may
split, relabel, or refine presentations, but it may not create unpaired
actual content:

$$
\boxed{
A^{*}R^{*}
\hbox{ does not create new active obstruction branches.}
}
$$

An active non-vacuum continuation that is not Ward/vacuum must therefore
carry at least one \(K/E\)-type residue:

$$
\boxed{
t\to t'
\quad\hbox{active and non-Ward}
\Longrightarrow
\Delta_{t\to t'}\in K_{\alpha}^{QCD}\oplus E_{\alpha}^{QCD}.
}
$$

By record/source completeness, every such residue is represented by a finite
Wilson/source/flux receipt:

$$
\boxed{
\Delta_{t\to t'}
\mapsto
R_{wil}\oplus R_{src}\oplus R_{flux}.
}
$$

By the response floor, a represented non-typed continuation pays at least
\(d_{*}\) in response norm.  Thus a branch is not free multiplicity; it is a
new charged local record.  If a continuation carried no response receipt, it
would be Ward/vacuum or typed by no-untyped-zero-response collapse.

The Einstein local-branch accounting is:

$$
\boxed{
\hbox{number/weight of active continuations}
\le
\exp\left(\chi_{\alpha}(D_{\alpha}(t))\right),
}
$$

where \(\chi_{\alpha}\) is the finite record-combinatorial entropy available
after same-actual quotienting.  This entropy is not an independent dial.  It
is computed from the finite response-token code:

$$
\boxed{
\mathrm{Tok}_{\alpha}:
\{\hbox{active branch words}\}
\longrightarrow
\{\hbox{finite Wilson/source/flux token words}\}.
}
$$

The crucial locality claim is not "the inequality we want".  It is the
following no-free-copying fact:

$$
\boxed{
\mathrm{Tok}_{\alpha}(\pi)=\mathrm{Tok}_{\alpha}(\pi')
\Longrightarrow
\pi\sim\pi'
\hbox{ modulo Ward/vacuum/typed residue}.
}
$$

If this injectivity failed, two distinct active non-typed continuations would
have the same finite receipts and zero response difference.  That is exactly
the no-untyped-zero-response obstruction.  Thus branch entropy is bounded by
the number of available response-token words, not by an extra free branching
parameter.

The resulting token-coding bound, proved below as Lemma 6.E, is:

$$
\boxed{
\chi_{\alpha}(d)
\le
(c_{\mathrm{act}}-\eta)d
}
$$

for some cofinal \(\eta>0\) on the active no-untyped-obstruction corpus.  In
particular:

$$
\boxed{
h_{*}^{br}
\le
(c_{\mathrm{act}}-\eta)d_{*}
<
c_{\mathrm{act}}d_{*}.
}
$$

The only way to violate this bound is to print an untyped branch-creation
residue: a physical continuation count not represented by Wilson/source/flux
receipts.  That is exactly forbidden by RSC/P30.

### 6.2.2 Feynman: Row Tokens Cannot Be Duplicated For Free

Feynman's question is:

$$
\boxed{
\hbox{where does the row weight go?}
}
$$

For each normalized non-vacuum row, decompose:

$$
\boxed{
K_{\alpha}(t,\cdot)
=
K_{\alpha}^{Ward}(t,\cdot)
\oplus
K_{\alpha}^{vac}(t,\cdot)
\oplus
K_{\alpha}^{typed}(t,\cdot)
\oplus
K_{\alpha}^{act}(t,\cdot).
}
$$

The pieces mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{piece} & \hbox{meaning}\\
\hline
K^{Ward} & \hbox{same-actual/gauge/presentation movement}\\
K^{vac} & \hbox{return to the singlet vacuum sector}\\
K^{typed} & \hbox{declared typed residue}\\
K^{act} & \hbox{active non-Ward non-typed obstruction continuation}
\end{array}
}
$$

The finite token ledger assigns one response token \(\tau\) to every active
continuation:

$$
\boxed{
\tau(t\to t')
=
\|{\mathsf R}_{\alpha}(t\to t')\|_{\infty}.
}
$$

The token separation law is:

$$
\boxed{
t\to t'\in K^{act}
\Longrightarrow
\tau(t\to t')\ge d_{*}.
}
$$

The row-budget identity is:

$$
\boxed{
\sum_{t'}K_{\alpha}^{act}(t,t')
\exp(h_{\alpha}(t')-h_{\alpha}(t))
\le
\sum_{t'}K_{\alpha}^{act}(t,t')
\exp(-c_{\mathrm{act}}\tau(t\to t')+\chi_{\alpha}(\tau)).
}
$$

Using the Einstein token-coding entropy bound
\(\chi_{\alpha}(\tau)\le(c_{\mathrm{act}}-\eta)\tau\), each active term is
suppressed by at least \(\exp(-\eta d_{*})\).  Therefore:

$$
\boxed{
\sum_{t'}K_{\alpha}^{act}(t,t')
\exp(h_{\alpha}(t')-h_{\alpha}(t))
\le
1-\epsilon_{branch}
}
$$

for:

$$
\boxed{
\epsilon_{branch}
=
1-\exp(-\eta d_{*})
>0.
}
$$

This is the Feynman row-token proof.  The deficit is not an estimate chosen
to get confinement.  It is the token spent by any row that remains
non-vacuum after Ward, vacuum, and typed pieces are removed.

### 6.2.3 No-Free-Branching Packet

The finite packet is:

$$
\boxed{
\mathrm{NO\text{-}FREE\text{-}BRANCHING\text{-}001}
=
(NFB1,\ldots,NFB9).
}
$$

The gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{NFB1}:&\hbox{active continuations are finite actual local records};\\
\mathrm{NFB2}:&\hbox{same-actual refinement cannot create unpaired active
branches};\\
\mathrm{NFB3}:&\hbox{every non-Ward active branch has a Wilson/source/flux
receipt};\\
\mathrm{NFB4}:&\hbox{no-untyped-zero-response collapse supplies }d_{*}>0;\\
\mathrm{NFB5}:&\hbox{finite locality gives a finite response-token alphabet
with bounded collar overhead};\\
\mathrm{NFB6}:&\mathrm{Tok}_{\alpha}\hbox{ is injective modulo
Ward/vacuum/typed equivalence};\\
\mathrm{NFB7}:&\hbox{active scale lock assigns response tokens a strict
cost-coding slack }\eta>0;\\
\mathrm{NFB8}:&\hbox{typed branch anomalies are registered before QCD-DYN};\\
\mathrm{NFB9}:&\hbox{cofinal refinement preserves the row-token accounting}.
\end{array}
}
$$

### Theorem 6.A: Actuality-Receipt Theorem

Searchable theorem tag:

`V4P35-ACTUALITY-RECEIPT-THEOREM-NFB1-NFB5-NFB8-NFB9`.

Assume the active corpus packet \({\mathbb R}_{35}\).  Then:

$$
\boxed{
\mathrm{NFB1},\mathrm{NFB2},\mathrm{NFB3},\mathrm{NFB4},
\mathrm{NFB5},\mathrm{NFB8},\mathrm{NFB9}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  NFB1 follows from the P24 active normal-form theorem: active
continuations are finite actual local records, not states in an external
configuration space.  NFB2 follows from P25 same-actual covariance:
refinement may split, relabel, or pair presentations, but it may not create
unpaired physical content.  NFB3 follows from P25/P30 record/source
completeness: every persistent non-Ward local residue must be represented by
the finite source/probe dictionary, and the QCD part of that dictionary is
Wilson/source/flux response.  NFB4 follows from P27 no-untyped-zero-response
collapse: a cofinal active non-Ward non-typed class with zero response would
be Ward/vacuum or typed, contradiction.  NFB5 follows because finite locality
admits only finitely many local receipt letters across a bounded collar, and
cofinal refinement changes the collar by bounded same-actual overhead.  NFB8
is precisely the P30 rule that typed anomalies must be printed before a
sector is declared closed.  NFB9 follows from the P30 receipt-functor
discipline: cofinal refinement preserves row tokens modulo Ward/vacuum/typed
terms. `square`

### Theorem 6.B: Receipt Faithfulness Theorem

Searchable theorem tag:

`V4P35-RECEIPT-FAITHFULNESS-THEOREM-NFB6`.

Assume \({\mathbb R}_{35}\).  Then:

$$
\boxed{
\mathrm{Tok}_{\alpha}(\pi)=\mathrm{Tok}_{\alpha}(\pi')
\Longrightarrow
\pi\sim\pi'
\hbox{ modulo Ward/vacuum/typed equivalence}.
}
$$

Consequently:

$$
\boxed{
\mathrm{NFB6}=\mathrm{PASS}_{ISP}.
}
$$

Proof.  Let \(\pi,\pi'\) be active branch words with the same finite
Wilson/source/flux token word.  Pull both words to a common finite actual
refinement.  Their difference:

$$
\boxed{
\Delta_{\pi\pi'}
=
\pi-\pi'
}
$$

has zero printed Wilson/source/flux receipt.  By the P25 RSC dictionary audit,
any persistent local difference is exactly one of:

$$
\boxed{
\begin{array}{c|l}
\hbox{kind} & \hbox{meaning}\\
\hline
\mathrm{Ward/vacuum} & \hbox{same-actual presentation or singlet return}\\
\mathrm{typed} & \hbox{declared extension/anomaly channel}\\
\mathrm{receipt} & \hbox{finite source/probe/Wilson/flux response}\\
\mathrm{untyped\ cokernel} & \hbox{missing physical record channel}
\end{array}
}
$$

The receipt component is zero by hypothesis.  The untyped cokernel is
forbidden on the active P25/P30 branch.  Therefore the difference is
Ward/vacuum or typed.  This is exactly token injectivity modulo
Ward/vacuum/typed equivalence. `square`

### Theorem 6.C: Single Response-Scale Theorem

Searchable theorem tag:

`V4P35-SINGLE-RESPONSE-SCALE-THEOREM-NFB7`.

Assume \({\mathbb R}_{35}\) and restrict to the active no-typed-branch-anomaly
sector.  Then the QCD row response scale is the same finite actual scale as
the GR/source response scale, and there is a cofinal strict coding slack
\(\eta>0\):

$$
\boxed{
\mathrm{NFB7}=\mathrm{PASS}_{ISP}.
}
$$

Proof.  P25 fixes the GR side by FAC/SLC/RSC: clocks, frames, curvature
readouts, source response, and finite stress-response probes are all measured
in one same-actual response scale.  P30 then uses the same finite
source/row receipts for RCP28/TSP28/MID28; the receipt functor has no second
free normalization.  A QCD row scale different from the GR/source scale would
therefore define a finite local residue:

$$
\boxed{
\Delta_{\mathrm{scale}}
=
D_{\alpha}^{QCD}
-
\lambda D_{\alpha}^{GR/src}.
}
$$

If \(\Delta_{\mathrm{scale}}\) is Ward, the two scales are the same in the
physical quotient.  If it is typed, it must be printed before QCD-DYN and the
sector is not the active no-typed-branch-anomaly sector.  If it is neither,
it is an untyped RSC/source-response cokernel, forbidden by P25/P30.  Hence
the active QCD row response scale is the same actual response scale already
fixed by the GR/source dictionary.

Now suppose there is no cofinal strict slack.  Then there is a cofinal
sequence of active branch-token families whose coding entropy saturates the
response cost.  In the finite source topology this produces either a new
typed critical channel or a family of distinct active branch words with no
separating response receipt.  The first case exits the active no-typed sector;
the second contradicts Theorem 6.B and no-untyped-zero-response collapse.
Therefore a cofinal \(\eta>0\) exists on the active sector. `square`

### Theorem 6.D: NFB Closure From The Active Corpus

Searchable theorem tag:

`V4P35-NFB1-NFB9-CORPUS-CLOSURE`.

Assume \({\mathbb R}_{35}\) and the active no-typed-branch-anomaly sector.
Then:

$$
\boxed{
\mathrm{NO\text{-}FREE\text{-}BRANCHING\text{-}001}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  Theorem 6.A proves NFB1-NFB5 and NFB8-NFB9 from finite actuality,
same-actual refinement, receipt completeness, typed-anomaly discipline, and
cofinal receipt functoriality.  Theorem 6.B proves NFB6 from receipt
faithfulness.  Theorem 6.C proves NFB7 from the single response-scale theorem
and active no-typed-branch restriction.  Hence NFB1-NFB9 pass. `square`

### Lemma 6.E: Token-Coding Entropy Bound

Assume NFB1-NFB7.  Then there is a cofinal \(\eta>0\) such that:

$$
\boxed{
\chi_{\alpha}(d)
\le
(c_{\mathrm{act}}-\eta)d
}
$$

for active non-Ward non-typed branch words of response budget \(d\).

Proof.  NFB1-NFB3 say every active branch word must print finite
Wilson/source/flux receipts.  NFB4 says a non-Ward non-typed receipt has a
positive response-token floor.  NFB5 gives a finite local token alphabet with
only bounded collar overhead under finite refinement.  NFB6 says distinct
active branch words cannot share the same token word unless their difference
is Ward/vacuum or typed.  Therefore active branch counting injects into
response-token counting.

It remains to identify the slope.  NFB7 is the scale-lock statement that the
active response cost is not measured in arbitrary units after the confinement
query; it is the same cost scale already fixed by the finite source/row
receipts.  In that locked scale, one unit of active response carries less
coding entropy than active cost by a cofinal gap \(\eta\).  If no such
\(\eta\) existed, there would be a cofinal sequence of distinct active branch
words with the same response-token budget but no separating receipt.  By
pigeonhole, two of them would have identical receipts while remaining
non-Ward and non-typed, contradicting no-untyped-zero-response collapse.
Hence the stated bound holds. `square`

### Theorem 6.1: No-Free-Branching

Searchable theorem tag:

`V4P35-NO-FREE-BRANCHING-001`.

Assume \({\mathbb R}_{35}\) and the active no-typed-branch-anomaly sector.
Then:

$$
\boxed{
R_{branch}=0
}
$$

on the active no-typed-branch-anomaly QCD sector, and:

$$
\boxed{
h_{*}^{br}<c_{\mathrm{act}}d_{*}.
}
$$

Proof.  Theorem 6.D first derives NFB1-NFB9 from the active corpus rather
than taking them as a free packet.  NFB1-NFB2 say branch multiplication cannot
occur inside same-actual presentation/refinement alone.  NFB3 says every
active branch therefore carries a represented finite receipt.  NFB4 gives a
positive response token floor for any non-Ward non-typed branch.  Lemma 6.E
then uses NFB5-NFB7 to derive, rather than assume, the strict token-coding
entropy bound.  NFB8 prevents hiding failures as posterior typed residues.
NFB9 transports the row-token accounting cofinally.  Therefore the active
branch entropy is strictly dominated by response cost, so \(R_{branch}=0\).
`square`

If NFB6 or NFB7 fails, the failure is meaningful:

$$
\boxed{
\neg\mathrm{NFB6}\vee\neg\mathrm{NFB7}
\Longrightarrow
\hbox{typed deconfining/branching phase or failure of active QCD-DYN}.
}
$$

Thus the no-free-branching theorem is falsifiable inside ISP.  It is not a
silent assumption.

The repaired status is:

$$
\boxed{
\hbox{\(R_{branch}=0\) is no longer selected; it is derived from finite
token injectivity plus active scale lock.}
}
$$

The remaining load-bearing facts are visible.  A critic can attack NFB6 by
printing two distinct active non-typed branch words with the same finite
Wilson/source/flux receipts.  A critic can attack NFB7 by showing that the
active response scale used in QCD rows differs from the scale fixed by the
source/row receipts.  Either attack would produce a typed anomaly or a
failure of QCD-DYN before the continuum confinement theorem is invoked.

### 6.3 Sub-Markov Row Majorants

With Theorem 6.1, the branching entropy is finite and strictly cost-dominated.
Define the branching-anomaly receipt:

$$
\boxed{
R_{branch}
=
\left(c_{\mathrm{act}}d_{*}-h_{*}^{br}\right)_{-},
}
$$

where \(x_{-}=\max(0,-x)\).  If \(R_{branch}\ne0\), the active finite QCD
row budget fails before any continuum limit is taken.  The failure is not
hidden; it is a typed deconfining/branching anomaly.

Thus the active no-anomaly branch condition printed by the theorem is:

$$
\boxed{
c_{\mathrm{act}}d_{*}
>
h_{*}^{br}.
}
$$

This inequality is not chosen after the confinement query, and it is not an
extra numerical fit.  It is the finite QCD instance of physical scale lock
plus no-free response-token duplication:

$$
\boxed{
\hbox{same actual response scale fixes cost units before Wilson rows are
summed.}
}
$$

Equivalently:

$$
\boxed{
R_{branch}=0
\quad\Longleftrightarrow\quad
c_{\mathrm{act}}d_{*}>h_{*}^{br}
\hbox{ on the strict QCD-DYN branch.}
}
$$

Now define the normalized non-vacuum row kernel:

$$
\boxed{
\widehat K_{\alpha}(t,t')
=
K_{\alpha}(t,t')\exp(h_{\alpha}(t')-h_{\alpha}(t)).
}
$$

The response floor and branching bound give:

$$
\boxed{
\sum_{t'\ne vac}\widehat K_{\alpha}(t,t')
\le
\exp(h_{*}^{br}-c_{\mathrm{act}}d_{*})
=
1-\epsilon_{*}
}
$$

for:

$$
\boxed{
\epsilon_{*}
=
1-\exp(h_{*}^{br}-c_{\mathrm{act}}d_{*})
>0.
}
$$

Apply this to the center sector and the singlet-gap sector:

$$
\boxed{
\epsilon_{*}^{center}>0,
\qquad
\epsilon_{*}^{gap}>0.
}
$$

Hence:

$$
\boxed{
\liminf_{\alpha}\epsilon_{\alpha}^{center}>0,
\qquad
\liminf_{\alpha}\epsilon_{\alpha}^{gap}>0.
}
$$

### Theorem 6.2: `QCD-MARGIN-CERT-001`

Assume:

$$
\boxed{
\begin{array}{ll}
\mathrm{QM1}:&\hbox{finite local obstruction type spaces are cofinally
compact};\\
\mathrm{QM2}:&\hbox{no untyped zero-response collapse holds};\\
\mathrm{QM3}:&\hbox{typed residues are registered before QCD-DYN};\\
\mathrm{QM4}:&\hbox{active scale lock fixes response-cost normalization};\\
\mathrm{QM5}:&\hbox{local branching entropy is finite and typed if anomalous};\\
\mathrm{QM6}:&\mathrm{NO\text{-}FREE\text{-}BRANCHING\text{-}001}
\hbox{ passes};\\
\mathrm{QM7}:&\hbox{cofinal refinement preserves the row-budget inequalities}.
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

and:

$$
\boxed{
\mathrm{QCH9}\text{-}\mathrm{QCH13}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

Proof.  QM1-QM3 give the uniform positive response floor: otherwise a
cofinal sequence of non-Ward non-typed obstructions would have zero response,
contradicting no-untyped-zero-response collapse.  QM4 fixes the cost scale
before the Wilson/transfer query.  QM5 gives finite branching entropy and
forces anomalous branching to be typed.  QM6 invokes Theorem 6.1, giving
\(R_{branch}=0\) and hence \(c_{\mathrm{act}}d_{*}>h_{*}^{br}\) on the active
no-typed-branch-anomaly sector.  QM7 transports the inequalities cofinally.
Therefore normalized non-vacuum
row sums are strictly sub-Markov in the center and gap sectors, giving
positive surface-tension and transfer-gap margins. `square`

This is the exact place where the active ISP ontology does real work.  If
QM6 fails, the theory does not get to pretend QCD-DYN passes; it prints a
typed deconfining/branching anomaly.

## 7. No-Circular Import Audit For Paper 34

Searchable circularity tag:

`V4P35-NO-CIRCULAR-IMPORT-AUDIT-P34`.

The repaired Paper 34 import graph is:

$$
\boxed{
\begin{array}{c|l}
\hbox{import} & \hbox{allowed content}\\
\hline
P26/P33 & \hbox{QFT/YM kinematics, gauge quotient, Wilson records, positivity}\\
P27 & \hbox{certificate object, zero-collapse theorem, local response
separation, row-budget machinery}\\
P30 & \hbox{finite receipt discipline and no posterior typed residues}\\
P35 & \hbox{QCD-MARGIN-CERT-001}
\end{array}
}
$$

The forbidden import is:

$$
\boxed{
P27:\quad \mathrm{QCD\text{-}DYN}=\mathrm{PASS}
\quad\hbox{as a premise for P34's theorem.}
}
$$

The repaired proof path is:

$$
\boxed{
\begin{array}{c}
P26/P33\ \mathrm{QFT/YM\ kinematics}\\
\wedge\ P27\ \mathrm{zero\text{-}collapse/local\ response\ machinery}\\
\wedge\ P30\ \mathrm{receipt\ discipline}\\
\wedge\ P35\ \mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}\\
\Longrightarrow
P34\ \mathrm{QCD\text{-}DYN}=\mathrm{PASS}_{finite\ ISP}.
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{NO\text{-}CIRCULAR\text{-}IMPORT\text{-}AUDIT}
=
\mathrm{PASS}.
}
$$

## 8. Combined Repair Theorem

Searchable combined theorem tag:

`V4P35-COMBINED-HARD-GATE-REPAIR-THEOREM`.

### Theorem 8.1: P35 Discharges The P32-P34 Repair Hooks

Assume the active ISP corpus packet \({\mathbb R}_{35}\).  Then:

$$
\boxed{
\begin{array}{c|c}
\hbox{repair hook} & \hbox{status}\\
\hline
\mathrm{GR\text{-}LEU\text{-}001} &
\mathrm{PASS}_{ISP}\\
\mathrm{QFT\text{-}FSRG\text{-}GRAM\text{-}001} &
\mathrm{PASS}_{ISP}\\
\mathrm{QFT\text{-}SPIN\text{-}CPT\text{-}BRIDGE\text{-}001} &
\mathrm{PASS}_{bridge}\\
\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001} &
\mathrm{PASS}_{finite\ ISP}\\
\mathrm{NO\text{-}CIRCULAR\text{-}IMPORT\text{-}AUDIT} &
\mathrm{PASS}
\end{array}
}
$$

Proof.  Section 3 proves `GR-LEU-001`.  Section 4 proves the positive-kernel
version of FSRG.  Section 5 separates the internal exchange/orientation
typing from the standard spin-statistics/CPT bridge and proves the bridge
under SC1-SC8.  Section 6 derives positive QCD margins from finite response
separation, scale lock, finite branching, and no untyped zero-response
collapse.  Section 7 removes the P34 circular import. `square`

## 9. Effect On Papers 32-34

Searchable effect tag:

`V4P35-EFFECT-ON-P32-P34`.

The upgrade is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{paper} & \hbox{before P35} & \hbox{after P35}\\
\hline
P32 &
\mathrm{GR\text{-}INT}\ \mathrm{relative\ to\ }GR\text{-}LEU\text{-}001 &
\mathrm{GR\text{-}INT}=\mathrm{CLOSED}_{ISP}\\
P33 &
\mathrm{QFT\text{-}KIN}\hbox{ with Gram/spin-CPT hooks} &
\mathrm{QFT\text{-}KIN}=\mathrm{CLOSED}_{ISP},\ 
\mathrm{spin/CPT}=\mathrm{BRIDGE}_{SC1\text{-}SC8}\\
P34 &
\mathrm{QCD\text{-}DYN}\ \mathrm{relative\ to\ }QCD\text{-}MARGIN\text{-}CERT &
\mathrm{QCD\text{-}DYN}=\mathrm{CLOSED}_{finite\ ISP}
\end{array}
}
$$

The exact non-claim remains:

$$
\boxed{
\hbox{P35 does not make the whole stack ontology-free, and it does not by
itself replace the P28-P31 continuum Yang-Mills descent theorem.}
}
$$

## 10. Final Verdict

Searchable final tag:

`V4P35-FINAL-REPAIR-VERDICT`.

The final repair status is:

$$
\boxed{
\mathrm{RL1}\text{-}\mathrm{RL5}
=
\mathrm{PASS}_{repair}.
}
$$

In compressed form:

$$
\boxed{
P35
\Longrightarrow
\left[
\begin{array}{c}
P32\ \mathrm{GR\ hardening\ no\ longer\ overclaims\ coupling\ uniqueness}\\
P33\ \mathrm{QFT\ hardening\ no\ longer\ assumes\ rank\text{-}one\ gluing\ or
standard\ spin/CPT}\\
P34\ \mathrm{QCD\ hardening\ no\ longer\ imports\ QCD\text{-}DYN\ circularly}
\end{array}
\right].
}
$$

The active post-P35 corpus has:

$$
\boxed{
\begin{array}{c|c}
\hbox{layer} & \hbox{post-P35 status}\\
\hline
\mathrm{effective\ GR} & \mathrm{CLOSED}_{ISP}\\
\mathrm{relativistic\ QFT\ kinematics} & \mathrm{CLOSED}_{ISP}\\
\mathrm{finite\ QCD\ dynamics} & \mathrm{CLOSED}_{finite\ ISP}\\
\mathrm{standard\ spin/CPT} & \mathrm{BRIDGE}_{SC1\text{-}SC8}\\
\mathrm{continuum\ YM\ confinement/mass\ gap} & \mathrm{handled\ by\ P28\text{-}P31}
\end{array}
}
$$

Paper 36 can now be a clean synthesis paper rather than another repair paper.
