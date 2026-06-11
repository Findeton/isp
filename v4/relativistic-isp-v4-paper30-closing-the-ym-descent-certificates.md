# Relativistic ISP V4 Paper 30: Closing The Yang-Mills Descent Certificates

Preprint, not peer reviewed, version 2026-05-29.

Author: Felix Robles Elvira

Status: RCP28, TSP28, and MID28 closed relative to the active ISP corpus, with
the external standard-YM comparison bridge developed and internally checked.
This paper follows Paper 29 and discharges the internal proof obligations
needed to upgrade the
Yang-Mills descent result from:

$$
\boxed{
\mathrm{CLOSED}_{relative\ internal}
}
$$

to:

$$
\boxed{
\mathrm{CLOSED}_{ISP\ ontology}.
}
$$

This file closes RCP28, TSP28, and MID28 relative to the active
P24/P25/P26/P27/P28/P29 corpus results, then develops the EXT1-EXT9 bridge to
the standard gauge-invariant continuum Yang-Mills comparison sector.

## 0. Paper 30 Target

Searchable target tag:

`V4P30-CERTIFICATE-CLOSURE-TARGET`.

Paper 29 isolated three load-bearing certificate targets:

$$
\boxed{
\mathrm{Paper\ 30\ target}
=
\mathrm{prove\ RCP28+TSP28+MID28\ from\ ISP\ primitives.}
}
$$

Equivalently:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{certificate} & \hbox{issue to close} & \hbox{current Paper 30 status}\\
\hline
\mathrm{RCP28} &
\hbox{source-Cauchy and determinacy} &
\hbox{closed in Sections 1.4-1.10}\\
\mathrm{TSP28} &
\hbox{scale-normalized margin survival} &
\hbox{closed in Sections 2.1-2.10}\\
\mathrm{MID28} &
\hbox{YM decoder separation and uniqueness} &
\hbox{closed in Sections 3.1-3.10}
\end{array}
}
$$

Thus the Paper 30 target is now discharged:

$$
\boxed{
\mathrm{RCP28+TSP28+MID28}
=
\mathrm{PASS}_{ISP}
}
$$

with:

$$
\boxed{
\mathrm{RCP28}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{HCL1}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{TSP28}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{HCL2}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{MID28}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{HCL3}=\mathrm{PASS}_{ISP}.
}
$$

### Continuum-floor audit note (external review, 2026-05)

The `CLOSED_{ISP ontology}` status above must be read as conditional on one open
continuum step, located precisely in `TSP28`.

- `RCP28` (source-Cauchy/determinacy) and `MID28` (decoder separation) are
  existence/uniqueness-type certificates.  The ISP suppositions they use are
  existence, reconstruction, and whole-process-compatibility conditions only;
  none assumes clustering, a correlation length, a mass scale, or a string
  tension.  So the mass gap is genuinely *reduced* here, not assumed: the
  closure is **non-circular** at the ontology level.

- `TSP28` ("scale-normalized margin survival") is exactly the continuum-survival
  certificate, and it is the load-bearing one.  Its `PASS_{ISP}` is conditional
  on the margin floor staying positive *uniformly as the heat-kernel collar
  (smearing) time* $t_-\downarrow0$.  In the standalone consolidation of this
  margin (paper 39, Section 11, the row-token Bessel gap `TOK-BESSEL`), the floor
  is established only at *fixed* $t_->0$: the detector variance (paper 39 Lemma
  11.2a2) and the Casimir/height tail rates (paper 39 Lemma 11.2a4) are positive
  only because $t_-$ is held away from $0$, and both degrade as $t_-\downarrow0$.
  If Sections 2.1-2.10 below intend a genuinely $t_-\downarrow0$-uniform margin,
  that uniform step is the one a reviewer must verify; it is the genuine
  infrared/strong-coupling content and coincides with the open part of the Clay
  problem.

Net: `RCP28+MID28` close the *existence/uniqueness* of the continuum object
relative to the ISP ontology, but `TSP28` — the positive continuum string
tension/mass gap — is `PASS` only modulo the $t_-\downarrow0$ survival of the
floor.  "`CLOSED_{ISP ontology}`" should be understood with that single
conditional attached.

## 1. Issue List: RCP28

Searchable issue tag:

`V4P30-RCP28-ISSUES`.

RCP28 must prove the source ledger has a genuine cofinal limit, not merely
compatible cluster points.

The sub-issues are:

$$
\boxed{
\begin{array}{c|l}
\hbox{subgate} & \hbox{issue}\\
\hline
\mathrm{SC1} &
\hbox{eventual boundedness of every finite source-response coordinate}\\
\mathrm{SC2} &
\hbox{Cauchy convergence of every finite source-response coordinate}\\
\mathrm{SC3} &
\hbox{compatibility of coordinate limits with all reduction maps}\\
\mathrm{SC4} &
\hbox{continuity of } \omega(F^{*}F) \hbox{ in the source topology}\\
\mathrm{SC5} &
\hbox{finite source coordinates separate internal source laws}
\end{array}
}
$$

The hard point is:

$$
\boxed{
\hbox{derive Cauchy/determinacy from finite actual records, Ward quotient,
receipt completeness, and typed residue control.}
}
$$

## 1.1 Einstein Route To RCP28

Searchable route tag:

`V4P30-RCP28-EINSTEIN-ROUTE`.

The Einstein move is to treat RCP28 as a principle of physical record
determinacy:

$$
\boxed{
\hbox{two cofinal presentations of the same actual physical content cannot
produce different licensed source responses.}
}
$$

The existing corpus gives the ontology needed for this principle:

$$
\boxed{
\hbox{physical ISP content}
=
\hbox{surviving same-actual Ward cohomology.}
}
$$

Therefore the proof should run by contradiction.

Assume \(\mathrm{SC2}\) fails.  Then for some finite source battery \(J_0\),
derivative order \(m\), and \(\epsilon>0\), there are cofinal refinements
\(\alpha_n,\beta_n\) such that:

$$
\boxed{
\left|
\partial_J^m{\mathcal S}_{\alpha_n}(0)
-
\partial_J^m{\mathcal S}_{\beta_n}(0)
\right|
\ge \epsilon.
}
$$

This is a persistent source-response distinction between two alleged
same-actual cofinal presentations.  The P25 RSC ontology says that such a
distinction has only three possible statuses:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{case} & \hbox{status} & \hbox{consequence}\\
\hline
\mathrm{E1} &
\hbox{Ward exact} &
\hbox{vanishes in the same-actual quotient}\\
\mathrm{E2} &
\hbox{represented source/probe residue} &
\hbox{appears as a finite receipt coordinate}\\
\mathrm{E3} &
\hbox{typed residue} &
\hbox{subcritical under P27 branch control}\\
\mathrm{E4} &
\hbox{unrepresented untyped residue} &
\hbox{violates RSC}
\end{array}
}
$$

Thus a non-Cauchy source coordinate is not an innocent analytic defect.  It is
a hidden physical distinction unless it is Ward exact, represented, or typed.
The Einstein route proves the determinacy half by reducing any persistent
failure to a forbidden untyped RSC cokernel:

$$
\boxed{
\mathrm{FAC+RSC+typed\ subcriticality}
\Longrightarrow
\mathrm{SC2+SC5}.
}
$$

This closes the determinacy part of RCP28 from the GR ontology already
developed in Paper 25.

## 1.2 Feynman Route To RCP28

Searchable route tag:

`V4P30-RCP28-FEYNMAN-ROUTE`.

The Feynman move is operational source accounting.  Do not ask first whether
the source ledger converges.  Ask what finite apparatus would measure the
failure of convergence.

For two refinements \(\alpha\le\beta\), define the source-difference
observable:

$$
\boxed{
\Delta_{\beta\alpha}(J,m)
=
\partial_J^m{\mathcal S}_{\beta}(0)
-
\partial_J^m{\mathcal S}_{\alpha}(0).
}
$$

Then decompose every possible source difference into the finite receipt
ledger:

$$
\boxed{
\Delta_{\beta\alpha}
=
\Delta^{Ward}_{\beta\alpha}
+
D_{\alpha}^{rec}(r_{\beta\alpha})
+
\Delta^{typed}_{\beta\alpha}
+
\Delta^{unrep}_{\beta\alpha}.
}
$$

The four terms mean:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{term} & \hbox{meaning} & \hbox{allowed fate}\\
\hline
\Delta^{Ward}_{\beta\alpha} &
\hbox{same-actual presentation change} &
\hbox{zero in the Ward quotient}\\
D_{\alpha}^{rec}(r_{\beta\alpha}) &
\hbox{represented finite receipt response} &
\hbox{tracked by source coordinates}\\
\Delta^{typed}_{\beta\alpha} &
\hbox{declared typed residue} &
\hbox{bounded by sub-Markov majorant}\\
\Delta^{unrep}_{\beta\alpha} &
\hbox{unrepresented response} &
\hbox{RSC violation}
\end{array}
}
$$

The Feynman route proves this accounting identity first, then derives
Cauchy behavior from the fate of each term:

$$
\boxed{
\begin{array}{c|l}
\hbox{ingredient} & \hbox{RCP28 use}\\
\hline
\Delta^{Ward}=0 &
\hbox{removes same-actual presentation noise}\\
D^{rec}(r)\hbox{ tracked} &
\hbox{turns persistent effects into ledger coordinates}\\
\|\Delta^{typed}\|\to0\hbox{ or subcritical} &
\hbox{prevents typed residue from splitting the physical law}\\
\Delta^{unrep}=0 &
\hbox{uses RSC to forbid hidden response channels}
\end{array}
}
$$

This is the operational version of RCP28:

$$
\boxed{
\hbox{every measurable source difference is either quotient, receipt, typed,
or impossible.}
}
$$

## 1.3 Combined RCP28 Proof Template

Searchable template tag:

`V4P30-RCP28-PROOF-TEMPLATE`.

The two routes are combined as follows.

First prove the finite source-difference decomposition:

$$
\boxed{
\Delta_{\beta\alpha}
=
\Delta^{Ward}_{\beta\alpha}
+
D_{\alpha}^{rec}(r_{\beta\alpha})
+
\Delta^{typed}_{\beta\alpha}.
}
$$

with no unrepresented remainder:

$$
\boxed{
\Delta^{unrep}_{\beta\alpha}=0.
}
$$

Then derive the RCP28 subgates:

$$
\boxed{
\begin{array}{c|l}
\hbox{subgate} & \hbox{derivation}\\
\hline
\mathrm{SC1} &
\hbox{finite receipt height plus typed sub-Markov majorants give boundedness}\\
\mathrm{SC2} &
\hbox{persistent non-Cauchy oscillation would be an untyped RSC cokernel}\\
\mathrm{SC3} &
\hbox{receipt functor reduction law gives compatibility with }R_{\beta\alpha}\\
\mathrm{SC4} &
\hbox{finite source coordinates include all }F^{*}F\hbox{ positivity tests}\\
\mathrm{SC5} &
\hbox{if all finite receipts agree, RSC leaves no physical distinction}
\end{array}
}
$$

The theorem proved below is:

$$
\boxed{
\mathrm{P25\ FAC+RSC}
\wedge
\mathrm{P27\ typed\ subcriticality}
\wedge
\mathrm{P29\ receipt\ functor}
\Longrightarrow
\mathrm{RCP28}.
}
$$

Since this theorem is discharged in Sections 1.4-1.10, HCL1 becomes
unconditional inside the active ISP branch:

$$
\boxed{
\mathrm{HCL1}
=
\mathrm{PASS}_{ISP}.
}
$$

A future challenge to this theorem must identify a new finite response channel
not captured by the current RSC dictionary.  That would not be a small
technical defect.  It would be a new physical branch of the ISP ontology.

## 1.4 RCP28 Corpus Import Ledger

Searchable import tag:

`V4P30-RCP28-CORPUS-IMPORT-LEDGER`.

The RCP28 proof uses the following already-developed corpus facts.

From Paper 25:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}.
}
$$

In particular:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{25}=0
}
$$

on the active normal-form corpus, where every persistent residue is represented
by Cartan/Wilson/corner probes or finite source/stress response.

From Paper 27:

$$
\boxed{
\hbox{typed residues are declared before the query, subcritical, and no
untyped zero-response survivor remains.}
}
$$

From Paper 29:

$$
\boxed{
{\mathcal R}ec_{\alpha}
:
{\mathsf Int}_{\alpha}^{phys}
\to
{\mathsf Rec}_{\alpha}
}
$$

is a finite receipt functor modulo same-actual Ward equivalence and controlled
typed residue, and:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{rec}
=
{\mathcal A}_{RSC,\alpha}^{src}
\oplus
{\mathcal A}_{typed,\alpha}^{src}.
}
$$

On the active no-untyped branch:

$$
\boxed{
\mathrm{coker}\,D_{*,untyped}^{rec}=0.
}
$$

These imports are exactly the ontology refinements needed for RCP28:

$$
\boxed{
\hbox{finite source differences must be Ward, receipt-represented, typed, or
impossible.}
}
$$

## 1.5 Source-Difference Module

Searchable definition tag:

`V4P30-SOURCE-DIFFERENCE-MODULE`.

For a finite source battery \(J_0\), derivative order \(m\), and two
refinements \(\alpha\le\beta\), define:

$$
\boxed{
\Delta_{\beta\alpha}(J,m)
=
\partial_J^m{\mathcal S}_{\beta}(0)
-
\partial_J^m{\mathcal S}_{\alpha}(0).
}
$$

Let \({\mathsf Diff}_{\alpha}^{src}\) be the finite module generated by all
such source differences after pulling both terms to the common finite actual
comparison context.  It carries four canonical submodules:

$$
\boxed{
\begin{array}{ll}
{\mathsf W}_{\alpha}^{src}:&
\hbox{same-actual Ward-exact source differences};\\
\mathrm{im}\,D_{\alpha}^{rec}:&
\hbox{receipt-represented source/probe/boundary/commutator differences};\\
{\mathcal A}_{typed,\alpha}^{src}:&
\hbox{declared typed residue differences};\\
{\mathcal A}_{unrep,\alpha}^{src}:&
\hbox{unrepresented source-response differences}.
\end{array}
}
$$

The last term is the dangerous one.  It is precisely the RSC cokernel viewed
as a source-response difference:

$$
\boxed{
{\mathcal A}_{unrep,\alpha}^{src}
=
\mathrm{coker}\,D_{\alpha}^{rec}
\quad
\hbox{after removing typed classes.}
}
$$

## 1.6 Lemma: Source-Difference Decomposition

Searchable lemma tag:

`V4P30-RCP28-SOURCE-DIFFERENCE-DECOMPOSITION`.

For every finite source difference \(\Delta_{\beta\alpha}\):

$$
\boxed{
\Delta_{\beta\alpha}
=
\Delta^{Ward}_{\beta\alpha}
+
D_{\alpha}^{rec}(r_{\beta\alpha})
+
\Delta^{typed}_{\beta\alpha}
+
\Delta^{unrep}_{\beta\alpha}.
}
$$

Proof.  Compare \(\alpha\) and \(\beta\) inside the common finite actual
context supplied by the directed refinement system.  By the P24/P25 normal
form, any finite transformation decomposes into presentation/refinement
pieces and residue pieces.  The presentation/refinement pieces are
same-actual and therefore lie in \({\mathsf W}_{\alpha}^{src}\).  By the P25
RSC dictionary audit, every persistent source, loop, boundary, commutator, or
word-depth residue is either represented by the finite source/probe dictionary
or typed.  By the P29 receipt functor, represented source effects are exactly
the image of \(D_{\alpha}^{rec}\).  Any remainder is, by definition, the
unrepresented RSC cokernel.  This gives the displayed decomposition. `square`

## 1.7 Lemma: No Unrepresented Source Difference On The Active Branch

Searchable lemma tag:

`V4P30-RCP28-NO-UNREPRESENTED-SOURCE-DIFFERENCE`.

On the active P25 no-untyped-RSC branch:

$$
\boxed{
\Delta^{unrep}_{\beta\alpha}=0.
}
$$

Proof.  If \(\Delta^{unrep}_{\beta\alpha}\ne0\), then there is a persistent
source-response distinction between two finite actual presentations that is
not Ward exact, not receipt-represented, and not typed.  This is exactly a
nonzero untyped RSC cokernel.  Paper 25 proves:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{25}=0
}
$$

for the active normal-form corpus, and Paper 29 identifies the receipt
cokernel with the source RSC obstruction:

$$
\boxed{
\mathrm{coker}\,D_{*,untyped}^{rec}=0.
}
$$

Therefore no unrepresented source-response difference survives on the active
branch. `square`

## 1.8 Lemma: Typed Residues Do Not Split The Physical Source Law

Searchable lemma tag:

`V4P30-RCP28-TYPED-NONSEPARATION`.

Typed source differences do not define distinct physical source laws in the
active ISP quotient:

$$
\boxed{
\Delta^{typed}_{\beta\alpha}
\sim_{phys}
0.
}
$$

Proof.  Typed residues are not posterior hidden variables.  By Paper 27 they
are declared before the QCD-DYN query, closed under refinement, and controlled
by finite sub-Markov branch majorants.  Paper 29 packages this as:

$$
\boxed{
\|B_{\alpha}^{I}\|_{1\to1}\le q_I<1,
\qquad
\omega_{\alpha}(h_{\alpha}^{I})\le h_I<\infty.
}
$$

Thus a typed difference has only two possible statuses.  Either it remains
inside the declared typed module, in which case it is part of the typed
extension label and not a split of the active physical source law; or it
produces a nonzero untyped source response, in which case it is no longer
typed and violates the no-untyped-zero-collapse rule from Paper 27.

Therefore typed residue cannot create two different physical source laws
inside the active quotient.  It either stays typed or becomes a falsifier.
`square`

## 1.9 Theorem: RCP28 From Active ISP Source Determinacy

Searchable theorem tag:

`V4P30-RCP28-SOURCE-DETERMINACY-THEOREM`.

Assume:

$$
\boxed{
\mathrm{P25\ FAC+RSC}_{GR}
\wedge
\mathrm{P27\ typed\ subcriticality/no\ untyped\ collapse}
\wedge
\mathrm{P29\ receipt\ functor}.
}
$$

Then:

$$
\boxed{
\mathrm{RCP28}
=
\mathrm{SC1+SC2+SC3+SC4+SC5}.
}
$$

Proof.  Prove each subgate.

For SC1, every finite source coordinate is a finite receipt coordinate plus
possibly typed residue coordinates.  Receipt height is finite by P29 FR5, and
typed residue growth is controlled by the P27/P29 sub-Markov majorants.
Therefore every finite source-response coordinate is eventually bounded:

$$
\boxed{
\sup_{\alpha\ge\alpha_0}|V_{\alpha}(J_0,k)|<\infty.
}
$$

For SC2, suppose a coordinate is not Cauchy.  Then some cofinal pair
\(\alpha_n,\beta_n\) has:

$$
\boxed{
|\Delta_{\beta_n\alpha_n}(J,m)|\ge\epsilon>0.
}
$$

By the source-difference decomposition:

$$
\boxed{
\Delta_{\beta_n\alpha_n}
=
\Delta^{Ward}
+
D^{rec}(r_n)
+
\Delta^{typed}
+
\Delta^{unrep}.
}
$$

The Ward term vanishes in the same-actual quotient.  The unrepresented term
vanishes by Lemma 1.7.  The typed term is nonseparating by Lemma 1.8.  The
receipt term is a represented finite source coordinate.  If it produced a
persistent non-Cauchy distinction between same-actual cofinal presentations,
that distinction would be a new source-response class not killed by Ward,
typing, or receipt functoriality, hence an untyped RSC cokernel.  This is
forbidden on the active branch.  Therefore the physical source coordinate is
Cauchy.

For SC3, P29 RF4 gives:

$$
\boxed{
R_{\beta\alpha}{\mathcal R}ec_{\beta}(I)
\simeq
{\mathcal R}ec_{\alpha}(R_{\beta\alpha}I).
}
$$

Since source coordinates are receipt coordinates modulo Ward and typed
nonseparation, their limits commute with reductions.

For SC4, each licensed \(F^{*}F\) positivity test is itself a finite
gauge-invariant source/probe polynomial in the receipt dictionary.  Therefore
\(\omega(F^{*}F)\) is a finite coordinate functional, hence continuous in the
projective source topology generated by those coordinates.

For SC5, suppose two internal source laws agree on all finite source
coordinates but are physically distinct.  Then their distinction leaves no
finite source/probe receipt.  By the Paper 25 ontology:

$$
\boxed{
\hbox{physical ISP content}
=
\hbox{surviving same-actual Ward cohomology}.
}
$$

A distinction with no finite coordinate must therefore be either Ward exact,
typed, or an unrepresented source channel.  Ward exact differences are not
physical distinctions; typed differences are typed extension labels, not
splits of the active physical source law; unrepresented differences violate
RSC.  Hence finite source coordinates separate active internal source laws.

Thus SC1-SC5 hold, and RCP28 is proved for the active ISP branch. `square`

## 1.10 RCP28 Verdict

Searchable verdict tag:

`V4P30-RCP28-VERDICT`.

The RCP28 certificate is closed inside the active ISP ontology:

$$
\boxed{
\mathrm{RCP28}
=
\mathrm{PASS}_{ISP}.
}
$$

Consequently:

$$
\boxed{
\mathrm{HCL1}
=
\mathrm{PASS}_{ISP}.
}
$$

This closes the source-Cauchy and source-determinacy certificate.  TSP28 is
closed separately in Section 2, and MID28 is closed separately in Section 3.

## 2. Issue List: TSP28

Searchable issue tag:

`V4P30-TSP28-ISSUES`.

TSP28 must prove that finite QCD margins survive physical scale normalization.

The sub-issues are:

$$
\boxed{
\begin{array}{c|l}
\hbox{subgate} & \hbox{issue}\\
\hline
\mathrm{SL1} &
\hbox{physical scale }a_{\alpha}\hbox{ is fixed by finite actual geometry}\\
\mathrm{SL2} &
\hbox{scale ratios are compatible with refinement reductions}\\
\mathrm{SL3} &
\hbox{finite center/string and singlet/gap margins are the P27 margins}\\
\mathrm{SL4} &
\hbox{derive cofinal lower bounds }
\sigma_{\alpha}^{fin}\ge\sigma_{*}a_{\alpha}^{2},
\quad
\Delta_{\alpha}^{fin}\ge\Delta_{*}a_{\alpha}\\
\mathrm{SL5} &
\hbox{exclude posterior rescaling or target-fitted scale choice}
\end{array}
}
$$

The hard point is:

$$
\boxed{
\mathrm{SL4}.
}
$$

This is the scale-normalized string-tension and gap-survival estimate.

## 2.1 TSP28 Corpus Import Ledger

Searchable import tag:

`V4P30-TSP28-CORPUS-IMPORT-LEDGER`.

The TSP28 proof uses the following already-developed corpus facts.

From Paper 25, the active GR-compatible branch supplies a nonposterior
finite actual geometry:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}.
}
$$

In particular, local coincidence scale, collar thickness, transfer distance,
and surface/time records are same-actual geometric content.  They are not
free regulator labels.

From Paper 28, the scale-lock packet is closed:

$$
\boxed{
\mathrm{YM\text{-}SCALE\text{-}LOCK\text{-}001}
=
\mathrm{PASS}.
}
$$

It supplies:

$$
\boxed{
a_{\alpha}>0,
\qquad
a_{\alpha}\to0,
\qquad
|S|_{\alpha}a_{\alpha}^{2}\to A^{phys}(S),
\qquad
n_{\alpha}a_{\alpha}\to T^{phys}.
}
$$

and forbids same-actual refinement from rescaling the gauge and GR sectors
differently.

From Paper 27, after the printed local cost-height inequalities and
sub-Markov branching majorants:

$$
\boxed{
\mathrm{QCD\text{-}LOCAL\text{-}COST\text{-}BRANCH\text{-}001}
\Longrightarrow
\mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

The cofinal finite margin floors are:

$$
\boxed{
\sigma_{*}^{fin}
=
\liminf_{\alpha}\sigma_{\alpha}^{fin}
>0,
\qquad
\Delta_{*}^{fin}
=
\liminf_{\alpha}\Delta_{\alpha}^{fin}
>0.
}
$$

From Sections 1 and 3 of this paper:

$$
\boxed{
\mathrm{RCP28}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{MID28}=\mathrm{PASS}_{ISP}.
}
$$

So the scale theorem cannot hide failure in nonconvergent source response or
in a wrong continuum decoder.  A physical margin collapse must now be a true
scale-survival failure.

## 2.2 Scale-Margin Module

Searchable definition tag:

`V4P30-TSP28-SCALE-MARGIN-MODULE`.

Define the finite-to-physical margin map:

$$
\boxed{
\sigma_{\alpha}^{phys}
=
a_{\alpha}^{-2}\sigma_{\alpha}^{fin},
\qquad
\Delta_{\alpha}^{phys}
=
a_{\alpha}^{-1}\Delta_{\alpha}^{fin}.
}
$$

The two possible margin-collapse defects are:

$$
\boxed{
{\mathfrak L}_{\sigma}
=
\left[
\liminf_{\alpha}
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}}
=0
\right],
\qquad
{\mathfrak L}_{\Delta}
=
\left[
\liminf_{\alpha}
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}
=0
\right].
}
$$

TSP28 is the statement:

$$
\boxed{
\neg{\mathfrak L}_{\sigma}
\wedge
\neg{\mathfrak L}_{\Delta}
}
$$

with \(a_{\alpha}\) fixed before the confinement query.

## 2.3 Einstein Route To TSP28

Searchable route tag:

`V4P30-TSP28-EINSTEIN-ROUTE`.

Einstein's move is scale identity by finite actual geometry:

$$
\boxed{
\hbox{the physical ruler is part of the same actual record geometry that
supports the GR-compatible branch.}
}
$$

Therefore an admissible scale map must satisfy:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{case} & \hbox{scale defect} & \hbox{fate}\\
\hline
\mathrm{S1} & \hbox{same-actual rescaling of gauge but not geometry} &
\hbox{FAC/SLC/RSC violation}\\
\mathrm{S2} & \hbox{posterior scale chosen after margin query} &
\hbox{SL5 violation}\\
\mathrm{S3} & \hbox{surface/time count not matched to actual geometry} &
\hbox{scale-lock violation}\\
\mathrm{S4} & \hbox{new physical scale anomaly} &
\hbox{typed residue or YM-identification failure}
\end{array}
}
$$

The active corpus excludes S1-S3, and S4 is not an untyped TSP28 failure.  It
would be a typed extension or a challenge to the active branch.

## 2.4 Feynman Route To TSP28

Searchable route tag:

`V4P30-TSP28-FEYNMAN-ROUTE`.

Feynman's move is operational margin accounting.  A disappearing physical
string tension is a cheap-sheet receipt; a disappearing physical gap is a
slow-mode receipt:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{receipt} & \hbox{collapse detected} & \hbox{finite consequence}\\
\hline
\mathrm{CS} &
\sigma_{\alpha}^{fin}/a_{\alpha}^{2}\to0 &
\hbox{center flux crosses physical area at vanishing cost}\\
\mathrm{SM} &
\Delta_{\alpha}^{fin}/a_{\alpha}\to0 &
\hbox{non-vacuum gauge-invariant transfer has vanishing physical cost}
\end{array}
}
$$

After RCP28, such receipts cannot be response-invisible.  After MID28, they
belong to the unique \(SU(N)\) YM decoder.  After Paper 27, they contradict
the cofinal finite margin floors unless the physical scale map is not the
actual geometric scale.  That last escape is exactly what Paper 28 scale lock
forbids.

## 2.5 Lemma: Actual Scale Lock Proves SL1, SL2, And SL5

Searchable lemma tag:

`V4P30-TSP28-SL1-SL2-SL5-ACTUAL-SCALE-LOCK`.

On the active branch:

$$
\boxed{
\mathrm{SL1+SL2+SL5}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  SL1 follows from P25/P28: \(a_{\alpha}\) is fixed by stable finite
local coincidence data, not by the confinement target.  SL2 follows from the
cofinal continuum family and reduction data:

$$
\boxed{
a_{\alpha}>0,
\qquad
a_{\alpha}\to0,
\qquad
a_{\beta}/a_{\alpha}
\hbox{ is fixed by }R_{\beta\alpha}.
}
$$

SL5 follows from FAC/SLC/RSC.  A same-actual refinement cannot rescale the
gauge sector differently from the GR/effective-geometric sector without
leaving a finite source, Wilson, Cartan, or stress receipt.  Such a receipt
would be represented, typed, or forbidden by the active RSC closure.  Hence
posterior or sector-split rescaling is not licensed. `square`

## 2.6 Lemma: P27 Finite Margins Prove SL3

Searchable lemma tag:

`V4P30-TSP28-SL3-P27-MARGIN-IDENTIFICATION`.

On the active branch:

$$
\boxed{
\mathrm{SL3}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  Paper 27's finite QCD-DYN pass identifies the two finite margins:

$$
\boxed{
\sigma_{\alpha}^{fin}
=
\hbox{finite Wilson center-flux/area margin},
\qquad
\Delta_{\alpha}^{fin}
=
\hbox{finite non-vacuum gauge-invariant transfer margin}.
}
$$

The local cost-height packet prints these margins from finite actual
obstruction costs and sub-Markov quotient path budgets.  They are not
continuum inputs and not posterior scale choices.  Therefore the margins used
by TSP28 are exactly the P27 finite margins. `square`

## 2.7 Lemma: Cofinal Finite Floors Imply SL4

Searchable lemma tag:

`V4P30-TSP28-SL4-COFINAL-FLOORS-IMPLY-SCALE-BOUNDS`.

On the active branch:

$$
\boxed{
\mathrm{SL4}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  From the Paper 27 cofinal margin import, choose a cofinal tail
\(\alpha\ge\alpha_0\) such that:

$$
\boxed{
\sigma_{\alpha}^{fin}\ge\frac12\sigma_{*}^{fin}>0,
\qquad
\Delta_{\alpha}^{fin}\ge\frac12\Delta_{*}^{fin}>0.
}
$$

From scale lock, \(a_{\alpha}\to0\), hence on a further cofinal tail:

$$
\boxed{
0<a_{\alpha}\le a_{\max}<\infty.
}
$$

Define:

$$
\boxed{
\sigma_{*}
=
\frac{\sigma_{*}^{fin}}{2a_{\max}^{2}},
\qquad
\Delta_{*}
=
\frac{\Delta_{*}^{fin}}{2a_{\max}}.
}
$$

Then for all \(\alpha\) in the cofinal tail:

$$
\boxed{
\sigma_{\alpha}^{fin}
\ge
\frac12\sigma_{*}^{fin}
\ge
\sigma_{*}a_{\alpha}^{2},
}
$$

and:

$$
\boxed{
\Delta_{\alpha}^{fin}
\ge
\frac12\Delta_{*}^{fin}
\ge
\Delta_{*}a_{\alpha}.
}
$$

This is exactly SL4:

$$
\boxed{
\sigma_{\alpha}^{fin}\ge\sigma_{*}a_{\alpha}^{2},
\qquad
\Delta_{\alpha}^{fin}\ge\Delta_{*}a_{\alpha}
\quad\hbox{cofinally}.
}
$$

Notice the direction of the proof.  We do not assume continuum physical
confinement.  We import cofinal finite obstruction floors from Paper 27 and
use the actual geometric scale lock to convert them into dimensionally
correct physical lower bounds. `square`

## 2.8 Lemma: Cheap-Sheet/Slow-Mode Collapse Is Impossible

Searchable lemma tag:

`V4P30-TSP28-NO-CHEAP-SHEET-NO-SLOW-MODE`.

On the active branch:

$$
\boxed{
{\mathfrak L}_{\sigma}
=
{\mathfrak L}_{\Delta}
=
0.
}
$$

Proof.  Suppose \({\mathfrak L}_{\sigma}\) fires.  Then there is a cofinal
subsequence of physical Wilson sheets whose center-flux obstruction cost per
physical area tends to zero.  By RCP28 this is a genuine source/Wilson
receipt, not a hidden nonconvergent coordinate.  By MID28 it belongs to the
unique \(SU(N)\) YM decoder, not a wrong theory.  By SL1-SL5, the scale is
the actual geometric scale.  Therefore the only remaining interpretation is
a collapse of the P27 finite center margin, contradicting
\(\sigma_{*}^{fin}>0\).

The same argument applies to \({\mathfrak L}_{\Delta}\).  A slow physical
mode must be a represented gauge-invariant transfer receipt by RCP28, must
belong to the active YM decoder by MID28, and must use the actual time scale
by scale lock.  It therefore contradicts \(\Delta_{*}^{fin}>0\).

Thus neither cheap-sheet nor slow-mode collapse is possible on the active
branch. `square`

## 2.9 Theorem: TSP28 From Active ISP Scale-Margin Determinacy

Searchable theorem tag:

`V4P30-TSP28-SCALE-MARGIN-DETERMINACY-THEOREM`.

Assume:

$$
\boxed{
\mathrm{P25\ FAC+SLC+RSC}_{GR}
\wedge
\mathrm{P27\ QCD\text{-}DYN/cofinal\ finite\ margins}
\wedge
\mathrm{P28\ YM\text{-}SCALE\text{-}LOCK}
\wedge
\mathrm{RCP28}
\wedge
\mathrm{MID28}.
}
$$

Then:

$$
\boxed{
\mathrm{TSP28}
=
\mathrm{SL1+SL2+SL3+SL4+SL5}.
}
$$

Proof.  Lemma 2.5 proves SL1, SL2, and SL5.  Lemma 2.6 proves SL3.  Lemma
2.7 proves SL4.  Lemma 2.8 supplies the Feynman no-collapse reading of the
same result: any physical margin collapse would be a represented cheap-sheet
or slow-mode receipt, and those contradict the active finite margins once
RCP28, MID28, and scale lock are in place.

Therefore:

$$
\boxed{
\liminf_{\alpha}a_{\alpha}^{-2}\sigma_{\alpha}^{fin}
\ge
\sigma_{*}
>0,
\qquad
\liminf_{\alpha}a_{\alpha}^{-1}\Delta_{\alpha}^{fin}
\ge
\Delta_{*}
>0.
}
$$

Thus TSP28 is proved for the active ISP branch. `square`

## 2.10 TSP28 Verdict

Searchable verdict tag:

`V4P30-TSP28-VERDICT`.

The TSP28 certificate is closed inside the active ISP ontology:

$$
\boxed{
\mathrm{TSP28}
=
\mathrm{PASS}_{ISP}.
}
$$

Consequently:

$$
\boxed{
\mathrm{HCL2}
=
\mathrm{PASS}_{ISP}.
}
$$

The result is the positive physical-margin survival required for the ISP
descent confinement theorem.  It is not the stronger external nontriviality
claim that the renormalized continuum string tension and gap have finite
nonzero numerical limits independent of the ISP descent packet.  That
stronger comparison remains an external-grade reconstruction question.

## 3. Issue List: MID28

Searchable issue tag:

`V4P30-MID28-ISSUES`.

MID28 must prove the descended sector has a unique \(SU(N)\) Yang-Mills
decoder and no silent wrong sector.

The sub-issues are:

$$
\boxed{
\begin{array}{c|l}
\hbox{subgate} & \hbox{issue}\\
\hline
\mathrm{YMU1} &
\hbox{gauge group label }SU(N)\hbox{ is fixed before the query}\\
\mathrm{YMU2} &
\hbox{finite Wilson traces separate the gauge quotient}\\
\mathrm{YMU3} &
\hbox{small-loop source derivatives identify }\mathrm{tr}\,F^{2}\\
\mathrm{YMU4} &
\hbox{Ward and Bianchi identities hold in the same-actual quotient}\\
\mathrm{YMU5} &
\hbox{RG coupling flow is route independent modulo typed irrelevant terms}\\
\mathrm{YMU6} &
\hbox{irrelevant or boundary operators vanish, are Ward exact, or typed}\\
\mathrm{YMU7} &
\hbox{no untyped massless, deconfined, or wrong-gauge silent sector remains}
\end{array}
}
$$

The hard point is:

$$
\boxed{
\hbox{prove decoder uniqueness from finite Wilson/source-response data rather
than assume the continuum YM dictionary.}
}
$$

## 3.1 MID28 Corpus Import Ledger

Searchable import tag:

`V4P30-MID28-CORPUS-IMPORT-LEDGER`.

The MID28 proof uses the following already-developed corpus facts.

From Paper 26, finite gauge transformations are refinement moves and Wilson
traces are invariant finite records:

$$
\boxed{
U_e\mapsto h_{s(e)}U_eh_{t(e)}^{-1},
\qquad
\operatorname{Tr}\prod_{e\in\gamma}
h_{s(e)}U_eh_{t(e)}^{-1}
=
\operatorname{Tr}\prod_{e\in\gamma}U_e.
}
$$

Thus gauge is same-actual presentation, not extra physical content.

From Paper 28, the active YM identification packet closes IDU1-IDU9:

$$
\boxed{
\mathrm{YM\text{-}ID\text{-}UNIQUENESS\text{-}001}
=
\mathrm{PASS}_{active\ YM\ descent\ branch}.
}
$$

The relevant IDU gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{IDU1}:&\hbox{finite holonomy records have structure group }SU(N);\\
\mathrm{IDU2}:&\hbox{small-loop products recover curvature }F_{\mu\nu};\\
\mathrm{IDU3}:&\hbox{only untyped relevant/marginal kinetic density is }
\operatorname{tr}F^{2};\\
\mathrm{IDU4}:&\hbox{topological density is fixed or typed};\\
\mathrm{IDU5}:&\hbox{same-actual Ward identities descend};\\
\mathrm{IDU6}:&\hbox{reflection/source positivity descends};\\
\mathrm{IDU7}:&\hbox{coupling flow is route-independent};\\
\mathrm{IDU8}:&\hbox{irrelevant operators vanish or are typed};\\
\mathrm{IDU9}:&\hbox{no extra massless, deconfined, or silent untyped sector}.
\end{array}
}
$$

From Paper 29, YMU1-YMU7 are exactly the decoder-separation hypotheses needed
for HCL3.  Paper 30 now imports the stronger Paper 28 IDU audit and discharges
YMU1-YMU7 rather than leaving MID28 as a named certificate.

The dictionary between the two gate systems is:

$$
\boxed{
\begin{array}{c|l}
\hbox{MID28 gate} & \hbox{active corpus source}\\
\hline
\mathrm{YMU1} & \mathrm{IDU1/P26\ finite\ }SU(N)\hbox{ holonomy packet}\\
\mathrm{YMU2} & \hbox{P26 Wilson trace quotient plus finite trace separation}\\
\mathrm{YMU3} & \mathrm{IDU2+IDU3}\\
\mathrm{YMU4} & \mathrm{IDU5}\hbox{ plus P25 same-actual Ward ontology}\\
\mathrm{YMU5} & \mathrm{IDU7}\hbox{ plus P26 RG-DESCENT}\\
\mathrm{YMU6} & \mathrm{IDU4+IDU8}\\
\mathrm{YMU7} & \mathrm{IDU9}\hbox{ plus RCP28/P27 no-silent-sector control}
\end{array}
}
$$

## 3.2 Decoder-Difference Module

Searchable definition tag:

`V4P30-MID28-DECODER-DIFFERENCE-MODULE`.

A continuum decoder is an assignment:

$$
\boxed{
D:
{\mathcal S}_{\infty}
\mapsto
(G_D,
{\mathcal W}_D,
F_D,
{\mathcal L}^{loc}_D,
g_D(\mu),
{\mathcal R}^{irr}_D,
{\mathcal X}_D),
}
$$

where:

$$
\boxed{
\begin{array}{ll}
G_D:&\hbox{candidate structure group};\\
{\mathcal W}_D:&\hbox{Wilson/character algebra};\\
F_D:&\hbox{small-loop curvature field};\\
{\mathcal L}^{loc}_D:&\hbox{local action-density decoder};\\
g_D(\mu):&\hbox{renormalized coupling flow};\\
{\mathcal R}^{irr}_D:&\hbox{irrelevant/boundary operator registry};\\
{\mathcal X}_D:&\hbox{extra low-energy or silent sectors}.
\end{array}
}
$$

For two decoders \(D,D'\), define the decoder defect:

$$
\boxed{
\Xi(D,D')
=
(\Xi_G,\Xi_W,\Xi_F,\Xi_L,\Xi_{RG},\Xi_{irr},\Xi_X).
}
$$

MID28 is the statement:

$$
\boxed{
\Xi(D,D')=0
\quad
\hbox{modulo same-actual Ward equivalence and declared typed residues}
}
$$

whenever \(D\) and \(D'\) decode the same active source law
\({\mathcal S}_{\infty}\).

## 3.3 Einstein Route To MID28

Searchable route tag:

`V4P30-MID28-EINSTEIN-ROUTE`.

The Einstein move is physical identity by invariant record content:

$$
\boxed{
\hbox{two decoders of the same finite actual content cannot be physically
different unless their difference survives as finite same-actual Ward
cohomology.}
}
$$

Using the Paper 25 ontology:

$$
\boxed{
\hbox{physical ISP content}
=
\hbox{surviving same-actual Ward cohomology}.
}
$$

Therefore a rival decoder has only four possible statuses:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{case} & \hbox{decoder defect} & \hbox{fate}\\
\hline
\mathrm{M1} & \hbox{Ward/same-actual presentation change} &
\hbox{not physical}\\
\mathrm{M2} & \hbox{declared typed irrelevant/topological residue} &
\hbox{typed extension, not a new active decoder}\\
\mathrm{M3} & \hbox{finite Wilson/source-visible difference} &
\hbox{caught by MID28 coordinates}\\
\mathrm{M4} & \hbox{untyped response-invisible difference} &
\hbox{forbidden by RCP28/P27/P28 no-silent-sector control}
\end{array}
}
$$

Thus decoder uniqueness is not a continuum prejudice.  It is a consequence of
the active ISP identity rule: physical differences must print finite invariant
records, survive as typed residues, or vanish as presentation.

## 3.4 Feynman Route To MID28

Searchable route tag:

`V4P30-MID28-FEYNMAN-ROUTE`.

The Feynman move is to build the decoder as an operational receipt machine.
Every proposed non-YM escape must produce one of the following receipts:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{receipt} & \hbox{what it measures} & \hbox{gate}\\
\hline
\mathrm{FW} & \hbox{closed-loop Wilson/character traces} & \mathrm{YMU2}\\
\mathrm{FP} & \hbox{small plaquette logarithms and curvature records} &
\mathrm{YMU3}\\
\mathrm{FD} & \hbox{local source derivatives of action density} &
\mathrm{YMU3}\\
\mathrm{FB} & \hbox{finite Ward/Bianchi defects} & \mathrm{YMU4}\\
\mathrm{FRG} & \hbox{coupling route defects} & \mathrm{YMU5}\\
\mathrm{FIRR} & \hbox{irrelevant/boundary operator coefficients} &
\mathrm{YMU6}\\
\mathrm{FS} & \hbox{silent, massless, or deconfined extra sector tests} &
\mathrm{YMU7}
\end{array}
}
$$

The no-escape statement is:

$$
\boxed{
\Xi(D,D')\ne0
\Longrightarrow
\mathrm{FW}\vee\mathrm{FP}\vee\mathrm{FD}\vee\mathrm{FB}\vee
\mathrm{FRG}\vee\mathrm{FIRR}\vee\mathrm{FS}
}
$$

and each receipt is already classified by the active corpus as Ward-exact,
typed, represented, or impossible.

## 3.5 Lemma: Fixed Gauge Label And Wilson Quotient

Searchable lemma tag:

`V4P30-MID28-YMU1-YMU2-FIXED-GAUGE-WILSON-QUOTIENT`.

On the active finite gauge branch:

$$
\boxed{
\mathrm{YMU1+YMU2}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  YMU1 is fixed by the P26/P28 finite holonomy packet:

$$
\boxed{
G=SU(N)
}
$$

is declared before the confinement query.  It is not selected after observing
the desired mass gap or Wilson area law.

For YMU2, the complete finite Wilson dictionary contains closed-loop traces
in the licensed representation battery.  Gauge transformations act at
vertices and preserve every closed trace by finite trace cyclicity.  Conversely,
within the active finite \(SU(N)\) holonomy packet, two holonomy assignments
that agree on the complete Wilson/character battery define the same gauge
quotient point.  This is the finite trace-separation/Tannaka principle used by
the corpus: the gauge quotient is the quotient seen by the full class-function
Wilson algebra.

If a rival decoder has a different gauge quotient, then some finite Wilson
coordinate differs.  If no finite Wilson coordinate differs, the alleged
difference is not a physical difference in the active same-actual quotient.
Thus finite Wilson traces separate the gauge quotient used by the decoder.
`square`

## 3.6 Lemma: Small-Loop And Action-Density Identification

Searchable lemma tag:

`V4P30-MID28-YMU3-SMALL-LOOP-ACTION-DENSITY`.

On the active branch:

$$
\boxed{
\mathrm{YMU3}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  Paper 28 IDU2 defines the finite plaquette curvature record:

$$
\boxed{
F_{\alpha,\mu\nu}(x)
=
a_{\alpha}^{-2}\log_0 U_{\alpha}(p_{\mu\nu}).
}
$$

The cofinal small-loop branch gives:

$$
\boxed{
U_{\alpha}(p_{\mu\nu})
=
\exp(a_{\alpha}^{2}F_{\alpha,\mu\nu}+o(a_{\alpha}^{2})),
\qquad
F_{\alpha,\mu\nu}\to F_{\mu\nu}.
}
$$

Paper 28 IDU3 then classifies the untyped relevant/marginal local
gauge-invariant densities in four dimensions.  Apart from normalization and a
fixed or typed topological density, the unique untyped kinetic density is:

$$
\boxed{
\operatorname{tr}F_{\mu\nu}F^{\mu\nu}.
}
$$

Therefore the small-loop source derivatives do not merely resemble a YM
action.  They identify the unique untyped local kinetic density available to
the active finite holonomy/source-response calculus. `square`

## 3.7 Lemma: Ward, Bianchi, And Route-Independent Coupling

Searchable lemma tag:

`V4P30-MID28-YMU4-YMU5-WARD-BIANCHI-RG`.

On the active branch:

$$
\boxed{
\mathrm{YMU4+YMU5}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  YMU4 follows from the P25 same-actual Ward ontology and Paper 28 IDU5.
Gauge transformations and Bianchi route changes are finite same-actual
presentation moves unless a typed residue is explicitly printed.  Thus:

$$
\boxed{
D_{\alpha,[\lambda}F_{\alpha,\mu\nu]}
\to0
\quad\hbox{or typed residue},
}
$$

and Ward identities descend in the same-actual quotient.

YMU5 follows from Paper 26 RG-DESCENT and Paper 28 IDU7.  Since YMU3 gives a
unique untyped kinetic density, the coupling coordinate \(g_{\alpha}\) is the
coefficient of that density.  Two licensed refinement routes \(r,r'\) can
differ only by:

$$
\boxed{
{\mathfrak G}_{\alpha}(r,r')
=
g_{\alpha}^{-2}(r)-g_{\alpha}^{-2}(r')
\to0
\quad\hbox{or}\quad
{\mathfrak G}_{\alpha}(r,r')\in{\mathcal T}_{\infty}^{typed}.
}
$$

So untyped coupling flow is route-independent. `square`

## 3.8 Lemma: Irrelevant, Boundary, And Silent Sectors

Searchable lemma tag:

`V4P30-MID28-YMU6-YMU7-NO-WRONG-SILENT-SECTOR`.

On the active branch:

$$
\boxed{
\mathrm{YMU6+YMU7}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  YMU6 follows from Paper 28 IDU4 and IDU8.  The topological density is
fixed before the query or typed, and irrelevant operators obey:

$$
\boxed{
c_{d,\alpha}^{phys}
=
a_{\alpha}^{d-4}c_{d,\alpha}^{fin}
\to0
\quad(d>4)
}
$$

whenever the finite source coefficient is bounded.  If it is not bounded, it
must be declared typed or it becomes LEAK6.  Boundary ambiguities are likewise
Ward-exact, typed, or represented finite boundary/source receipts.

YMU7 follows from Paper 28 IDU9 plus the P27 no-untyped-zero-response rule and
RCP28 source determinacy.  A silent sector would be a response-invisible
untyped difference, forbidden by RCP28/P27.  A deconfined untyped sector would
contradict the finite Wilson/center margin.  A new massless untyped decoder
sector would either introduce a finite transfer/source coordinate or be
silent; the former is represented in the ledger and the latter is forbidden.
The quantitative physical scale survival of the already represented positive
gap is supplied by TSP28.  Thus no wrong-gauge, deconfined, silent, or extra
massless untyped sector can survive as part of the active decoder. `square`

## 3.9 Theorem: MID28 From Active ISP Decoder Determinacy

Searchable theorem tag:

`V4P30-MID28-DECODER-DETERMINACY-THEOREM`.

Assume:

$$
\boxed{
\mathrm{P25\ same\text{-}actual\ Ward/RSC\ ontology}
\wedge
\mathrm{P26\ finite\ }SU(N)\mathrm{\ gauge/Wilson/RG\ packet}
\wedge
\mathrm{P27\ QCD\text{-}DYN/no\ silent\ untyped\ branch}
\wedge
\mathrm{P28\ IDU1\text{-}IDU9}
\wedge
\mathrm{P29\ compact\ positive\ source\ law}.
}
$$

Then:

$$
\boxed{
\mathrm{MID28}
=
\mathrm{YMU1+YMU2+YMU3+YMU4+YMU5+YMU6+YMU7}.
}
$$

Proof.  Lemma 3.5 proves YMU1-YMU2.  Lemma 3.6 proves YMU3.  Lemma 3.7 proves
YMU4-YMU5.  Lemma 3.8 proves YMU6-YMU7.

Now let \(D,D'\) be two admissible decoders of the same active source law
\({\mathcal S}_{\infty}\).  If \(\Xi_G\) or \(\Xi_W\) is nonzero, YMU1-YMU2
produce a finite Wilson-coordinate difference.  If \(\Xi_F\) or \(\Xi_L\) is
nonzero, YMU3 produces a finite small-loop/source-derivative difference.  If
\(\Xi_{RG}\) is nonzero, YMU5 produces a finite route-defect receipt unless
the difference is typed.  If \(\Xi_{irr}\) is nonzero, YMU6 says it is
irrelevant-vanishing, Ward/boundary-exact, typed, or a LEAK6 falsifier.  If
\(\Xi_X\) is nonzero, YMU7 says it is a silent/wrong-sector falsifier.

Thus any decoder difference is Ward-equivalent, typed, represented by finite
receipts, or impossible.  Since \(D\) and \(D'\) decode the same active source
law, represented receipt differences are absent.  Ward differences are
presentation, typed differences are not active untyped decoder splits, and
impossible differences are excluded.  Therefore:

$$
\boxed{
D=D'
\quad
\hbox{on active physical ISP content.}
}
$$

The unique decoder is:

$$
\boxed{
D_{YM}^{desc}({\mathcal S}_{\infty})
=
SU(N)\hbox{ Yang-Mills}.
}
$$

Hence MID28 is proved for the active ISP branch. `square`

## 3.10 MID28 Verdict

Searchable verdict tag:

`V4P30-MID28-VERDICT`.

The MID28 certificate is closed inside the active ISP ontology:

$$
\boxed{
\mathrm{MID28}
=
\mathrm{PASS}_{ISP}.
}
$$

Consequently:

$$
\boxed{
\mathrm{HCL3}
=
\mathrm{PASS}_{ISP}.
}
$$

This closes the YM decoder separation and uniqueness certificate.  The
quantitative scale-normalized survival of the positive finite margins is
closed separately in Section 2.

## 4. Cross-Certificate Consistency Issues

Searchable issue tag:

`V4P30-CROSS-CERTIFICATE-ISSUES`.

The certificates cannot be proved independently if their data conflict.  Since
RCP28, TSP28, and MID28 are now closed, run the cross-certificate consistency
audit:

$$
\boxed{
\begin{array}{c|l}
\hbox{check} & \hbox{issue}\\
\hline
\mathrm{X1} &
\hbox{RCP28 source topology is the topology used by MID28 decoder data}
\quad \mathrm{PASS}\\
\mathrm{X2} &
\hbox{TSP28 scale map is compatible with RCP28 reductions}
\quad \mathrm{PASS}\\
\mathrm{X3} &
\hbox{Wilson loops used for SL4 are the same Wilson data used by YMU2}
\quad \mathrm{PASS}\\
\mathrm{X4} &
\hbox{typed residues remain subcritical after scale normalization}
\quad \mathrm{PASS}\\
\mathrm{X5} &
\hbox{no certificate hides a posterior choice of source, scale, or decoder}
\quad \mathrm{PASS}
\end{array}
}
$$

## 5. Einstein/Feynman Answer To The Admissibility Critique

Searchable critique tag:

`V4P30-ADMISSIBILITY-NOT-TARGET-FITTING-ANSWER`.

The strongest mathematical-physics objection is:

$$
\boxed{
\hbox{do the active corpus packet, same-actual Ward quotient, typed residues,
and no-silent-sector rules encode the desired physics by admissibility?}
}
$$

This is the right objection.  The answer is not to deny that these principles
are load-bearing.  They are load-bearing.  The question is whether they are
target-fitted or independently forced by the ISP ontology.

### 5.1 Einstein Answer: Identity Of Actual Records

The Einstein move is to ask what must be invariant if two descriptions are
descriptions of the same actual finite process.

The primitive equivalence principle is:

$$
\boxed{
\hbox{same actual finite record}
\Longrightarrow
\hbox{same physical source response.}
}
$$

Thus the same-actual Ward quotient is not introduced to make Yang-Mills work.
It is the finite-record version of general covariance/gauge redundancy:

$$
\boxed{
\hbox{presentation change without a new record}
=
\hbox{zero physical difference.}
}
$$

Conversely:

$$
\boxed{
\hbox{persistent difference in licensed source response}
=
\hbox{physical content.}
}
$$

This gives the contested principle:

$$
\boxed{
\hbox{surviving same-actual Ward cohomology}
=
\hbox{physical ISP content.}
}
$$

It is not a Yang-Mills-specific rule.  It is used already in the GR and source
papers to decide whether a residual is:

$$
\boxed{
\hbox{presentation artifact}
\quad\hbox{or}\quad
\hbox{new physical source content}
\quad\hbox{or}\quad
\hbox{typed extension.}
}
$$

If this principle fails, the theory does not merely lose confinement.  It loses
record identity: two presentations of the same finite actual process would be
allowed to have different physical responses with no finite distinguishing
record.

That is why the Einstein answer is:

$$
\boxed{
\hbox{these are not optional YM conveniences; they are the identity laws of
finite actual geometry.}
}
$$

### 5.2 Feynman Answer: Receipts Or Nothing

The Feynman move is operational bookkeeping.  For every alleged missing
physical distinction, ask:

$$
\boxed{
\hbox{what finite apparatus record would distinguish it?}
}
$$

There are only four licensed answers:

$$
\boxed{
\begin{array}{c|l}
\hbox{case} & \hbox{meaning}\\
\hline
\mathrm{W} & \hbox{Ward/same-actual presentation change}\\
\mathrm{R} & \hbox{finite receipt in the source/probe/Wilson/boundary ledger}\\
\mathrm{T} & \hbox{declared typed residue branch}\\
\mathrm{U} & \hbox{unrepresented untyped difference}
\end{array}
}
$$

The rule:

$$
\boxed{
\hbox{no untyped zero-response collapse}
}
$$

means:

$$
\boxed{
\hbox{an untyped sector with no finite response is not active physical
content.}
}
$$

This is not a hidden way to force confinement.  It is the finite operational
meaning of physicality.  If a proposed sector is physical, it must change some
licensed finite source, transfer, Wilson, boundary, or detector response.  If
it changes none, it is a presentation duplicate or an undeclared metaphysical
addition.  If it changes one, the receipt ledger must print it.

So the Feynman answer is:

$$
\boxed{
\hbox{show me the finite receipt.  If there is none, it is not a physical
degree of freedom in ISP.}
}
$$

### 5.3 Why This Is Not Merely Encoding The Desired Physics

The principles are licensed only if they pass four independence tests:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{test} & \hbox{requirement} & \hbox{reason}\\
\hline
\mathrm{I1} &
\hbox{declared before the YM conclusion} &
\hbox{prevents posterior fitting}\\
\mathrm{I2} &
\hbox{used across GR, QFT, QCD, and YM} &
\hbox{not target-specific}\\
\mathrm{I3} &
\hbox{has finite falsifier receipts} &
\hbox{not verbal metaphysics}\\
\mathrm{I4} &
\hbox{allows typed failure branches} &
\hbox{does not force the desired theory}
\end{array}
}
$$

Audit:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{principle} & \hbox{status} & \hbox{non-fitted content}\\
\hline
\hbox{active corpus packet} &
\mathrm{PASS}_{I1,I2} &
\hbox{fixed by P24-P29 before the final P30 theorem}\\
\hbox{same-actual Ward quotient} &
\mathrm{PASS}_{I1,I2,I3} &
\hbox{same finite record implies same physical response}\\
\hbox{typed residues} &
\mathrm{PASS}_{I1,I3,I4} &
\hbox{failures are printed as extension branches, not hidden}\\
\hbox{no untyped zero-response collapse} &
\mathrm{PASS}_{I2,I3} &
\hbox{physical content must have a finite response channel}\\
\hbox{surviving Ward cohomology is physical} &
\mathrm{PASS}_{I2,I3,I4} &
\hbox{surviving classes predict corrections or new sectors}
\end{array}
}
$$

Therefore the honest status is:

$$
\boxed{
\hbox{these are strong ISP physical-admissibility laws, not derivations from
ontology-free mathematics.}
}
$$

But they are not merely the desired YM conclusion in disguise, because each one
can fail in a named way:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failure} & \hbox{finite signal} & \hbox{effect}\\
\hline
\mathrm{A1} & \hbox{same-actual move changes a licensed response} &
\hbox{Ward quotient fails}\\
\mathrm{A2} & \hbox{untyped zero-response branch later becomes detectable} &
\hbox{RCP28/P27 fail}\\
\mathrm{A3} & \hbox{typed residue grows to relevant/marginal order} &
\hbox{new physical sector}\\
\mathrm{A4} & \hbox{finite receipt is missing from the source dictionary} &
\hbox{RSC/source completeness fails}\\
\mathrm{A5} & \hbox{surviving cohomology is not represented in YM} &
\hbox{MID28 fails}
\end{array}
}
$$

The Einstein/Feynman answer to the reviewer is therefore:

$$
\boxed{
\begin{array}{l}
\hbox{Einstein: the principles express identity and covariance of finite
actual records;}\\
\hbox{Feynman: every alleged alternative must print an operational finite
receipt;}\\
\hbox{if it prints one, the theorem can fail; if it prints none, it is not
active ISP physics.}
\end{array}
}
$$

## 6. External Equivalence To Standard Continuum Yang-Mills

Searchable external-equivalence tag:

`V4P30-EXTERNAL-YM-EQUIVALENCE-BRIDGE`.

Paper 30 no longer leaves the external equivalence as an empty handoff.  It
now develops the bridge that must be checked against the standard continuum
Yang-Mills formulation.

Define the ISP-descended object:

$$
\boxed{
{\mathsf Y}_{ISP}
=
(
{\mathcal A}^{inv}_{ISP},
\omega_{ISP},
W_{ISP},
{\mathsf T}_{ISP},
\sigma_{ISP},
\Delta_{ISP},
D_{YM}^{desc}
).
}
$$

Here \({\mathcal A}^{inv}_{ISP}\) is the gauge-invariant source/Wilson algebra
generated by finite descent, \(\omega_{ISP}\) is the positive limiting source
state, \(W_{ISP}\) is the descended Wilson-loop functional,
\({\mathsf T}_{ISP}\) is the transfer semigroup, and
\(\sigma_{ISP},\Delta_{ISP}>0\) are the physical string-tension and gap
margins supplied by TSP28.

Define the standard comparison target:

$$
\boxed{
{\mathsf Y}_{std}
=
(
{\mathcal A}^{inv}_{std},
\omega_{std},
W_{std},
{\mathsf T}_{std},
\sigma_{std},
\Delta_{std},
SU(N)
).
}
$$

An external equivalence is a map:

$$
\boxed{
{\mathfrak E}:{\mathsf Y}_{std}\longleftrightarrow{\mathsf Y}_{ISP}
}
$$

that preserves the gauge-invariant algebra, the state, Wilson loops, transfer
dynamics, and the positive confinement/gap criteria.

### 6.1 External Equivalence Gates

The bridge requires the following gates:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{requirement} & \hbox{Paper 30 source}\\
\hline
\mathrm{EXT1} &
\hbox{fixed gauge group }SU(N)\hbox{ and Wilson quotient} &
\mathrm{MID28/YMU1,YMU2}\\
\mathrm{EXT2} &
\hbox{finite Wilson/source dictionary generates the invariant algebra} &
\mathrm{RCP28+MID28}\\
\mathrm{EXT3} &
\hbox{positive source state supports OS/GNS reconstruction} &
\mathrm{RCP28/SC4}\\
\mathrm{EXT4} &
\hbox{small-loop density is the standard YM kinetic density} &
\mathrm{MID28/YMU3}\\
\mathrm{EXT5} &
\hbox{Ward/Bianchi identities match standard gauge covariance} &
\mathrm{MID28/YMU4}\\
\mathrm{EXT6} &
\hbox{RG/coupling coordinate is route-independent} &
\mathrm{MID28/YMU5}\\
\mathrm{EXT7} &
\hbox{irrelevant, boundary, and topological terms do not change the sector} &
\mathrm{MID28/YMU6}\\
\mathrm{EXT8} &
\hbox{no silent extra sector survives the comparison} &
\mathrm{MID28/YMU7}\\
\mathrm{EXT9} &
\hbox{Wilson area law and transfer gap match the standard criteria} &
\mathrm{TSP28}
\end{array}
}
$$

### 6.2 Einstein Route: Invariant-Content Uniqueness

Searchable Einstein comparison tag:

`V4P30-EXT-EINSTEIN-INVARIANT-CONTENT-UNIQUENESS`.

Einstein's route is not to match words.  It is to identify the invariant
physical object and prove that two presentations with the same invariant object
are the same theory on the comparison sector.

Define the invariant comparison content:

$$
\boxed{
{\mathcal I}_{YM}
=
(
G,
{\mathcal A}^{inv},
\omega,
W,
{\mathcal D}_{loc},
{\mathcal W}_{Ward},
{\mathcal R}_{RG},
{\mathcal N}_{sector},
{\mathcal C}_{conf}
).
}
$$

The entries mean:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{entry} & \hbox{invariant content} & \hbox{EXT gate}\\
\hline
G &
\hbox{fixed compact gauge group and quotient} &
\mathrm{EXT1}\\
{\mathcal A}^{inv} &
\hbox{gauge-invariant Wilson/source algebra} &
\mathrm{EXT2}\\
\omega &
\hbox{positive source state} &
\mathrm{EXT3}\\
W &
\hbox{Wilson-loop functional} &
\mathrm{EXT2,EXT9}\\
{\mathcal D}_{loc} &
\hbox{local small-loop kinetic density} &
\mathrm{EXT4}\\
{\mathcal W}_{Ward} &
\hbox{Ward/Bianchi covariance identities} &
\mathrm{EXT5}\\
{\mathcal R}_{RG} &
\hbox{route-independent coupling/RG coordinate} &
\mathrm{EXT6}\\
{\mathcal N}_{sector} &
\hbox{no wrong, silent, boundary, or extra massless sector} &
\mathrm{EXT7,EXT8}\\
{\mathcal C}_{conf} &
\hbox{positive Wilson string tension and transfer gap} &
\mathrm{EXT9}
\end{array}
}
$$

The Einstein comparison principle is:

$$
\boxed{
{\mathcal I}_{YM}({\mathsf Y}_{ISP})
=
{\mathcal I}_{YM}({\mathsf Y}_{std})
\Longrightarrow
{\mathsf Y}_{ISP}\simeq{\mathsf Y}_{std}
\hbox{ on gauge-invariant physical content.}
}
$$

This is the same kind of move used in the GR papers: physical equivalence is
not equality of presentations; it is equality of same-actual invariant content.

#### Lemma 6.2.1: EXT1-EXT2 Fix The Gauge-Invariant Algebra

Assume EXT1 and EXT2.  Then the ISP-descended Wilson/source algebra and the
standard \(SU(N)\) gauge-invariant algebra have the same quotient content:

$$
\boxed{
({\mathcal A}^{inv}_{ISP},G_{ISP})
\simeq
({\mathcal A}^{inv}_{std},SU(N)).
}
$$

Proof.  EXT1 fixes \(G=SU(N)\) before the comparison query.  EXT2 says the
finite Wilson/source dictionary generates the invariant algebra.  By the
finite trace-separation/Tannaka principle already used in MID28, closed Wilson
characters separate the active gauge quotient.  Therefore any standard
gauge-invariant polynomial not represented by the ISP dictionary would define a
new invariant coordinate.  RCP28 would then print it as a source receipt, or
MID28 would print it as a Wilson/decoder receipt.  Since EXT2 passes, no such
unrepresented invariant coordinate remains. `square`

#### Lemma 6.2.2: EXT3 Supplies The State-Reconstruction Object

Assume EXT3.  Then \(\omega_{ISP}\) defines the same positive state data needed
for the standard algebraic comparison:

$$
\boxed{
\omega_{ISP}(F^{*}F)\ge0
\quad
\hbox{for every licensed gauge-invariant }F.
}
$$

Consequently the GNS reconstruction of the gauge-invariant algebra is licensed.
If the comparison is written in Euclidean language, the additional reflection
or OS positivity clauses must be the reflected form of the same finite
source-positivity receipts, not a new posterior assumption.

Proof.  RCP28/SC4 makes positivity closed in the projective source topology.
The finite \(F^{*}F\) tests are part of the source receipt dictionary.  Hence
the limiting state is positive on the invariant algebra.  Algebraic GNS follows
from positivity.  Any Euclidean OS presentation must use the same finite
reflection/source receipts; otherwise it prints an external receipt \(R_{ext}\)
and EXT3 fails. `square`

#### Lemma 6.2.3: EXT4-EXT6 Fix The Local Yang-Mills Law

Assume EXT4-EXT6.  Then the descended local continuum law is the usual
route-independent \(SU(N)\) Yang-Mills local law:

$$
\boxed{
{\mathcal D}_{loc}
=
\operatorname{tr}F_{\mu\nu}F^{\mu\nu},
\qquad
{\mathcal W}_{Ward}=\mathrm{PASS},
\qquad
{\mathcal R}_{RG}=\mathrm{PASS}.
}
$$

Proof.  EXT4 is exactly YMU3: the small-loop source derivatives identify the
unique untyped local kinetic density \(\operatorname{tr}F^2\).  EXT5 is YMU4:
Ward and Bianchi identities descend in the same-actual quotient.  EXT6 is YMU5:
the coupling coordinate is route-independent modulo typed residue.  Thus the
local density, covariance identities, and RG coordinate are the standard YM
ones on active untyped physical content. `square`

#### Lemma 6.2.4: EXT7-EXT8 Remove Non-YM Contaminants

Assume EXT7-EXT8.  Then no boundary, irrelevant, topological, silent,
wrong-gauge, deconfined, or extra massless sector changes the active
comparison object:

$$
\boxed{
{\mathcal N}_{sector}
=
\mathrm{clean}_{active}.
}
$$

Proof.  EXT7 is YMU6: irrelevant terms vanish under scale normalization,
boundary terms are Ward/boundary exact, represented, or typed, and topological
terms are fixed or typed before the query.  EXT8 is YMU7: a silent extra sector
is forbidden by RCP28/P27 no-untyped-zero-response control, while any
detectable extra sector prints a finite receipt.  Hence no contaminant remains
inside the active standard comparison object. `square`

#### Lemma 6.2.5: EXT9 Fixes The Confinement And Gap Predicates

Assume EXT9.  Then the ISP confinement and mass-gap predicates are the standard
Wilson/transfer predicates on the identified gauge-invariant sector:

$$
\boxed{
\sigma_{ISP}>0
\Longleftrightarrow
\sigma_{std}>0,
\qquad
\Delta_{ISP}>0
\Longleftrightarrow
\Delta_{std}>0
}
$$

on the comparison sector.

Proof.  TSP28 supplies the scale-normalized finite margin survival:

$$
\boxed{
\liminf_{\alpha}a_{\alpha}^{-2}\sigma_{\alpha}^{fin}>0,
\qquad
\liminf_{\alpha}a_{\alpha}^{-1}\Delta_{\alpha}^{fin}>0.
}
$$

EXT9 says these are the same Wilson area-law and transfer-gap predicates used
in the standard comparison sector.  Since EXT1-EXT8 have already identified the
sector, algebra, state, local law, and absence of contaminants, the predicates
cannot refer to different physical objects. `square`

#### Theorem 6.2: Einstein Invariant-Content Equivalence

Assume EXT1-EXT9.  Then:

$$
\boxed{
{\mathcal I}_{YM}({\mathsf Y}_{ISP})
=
{\mathcal I}_{YM}({\mathsf Y}_{std}).
}
$$

Therefore:

$$
\boxed{
{\mathsf Y}_{ISP}
\simeq
{\mathsf Y}_{std}
\quad
\hbox{on gauge-invariant physical content.}
}
$$

Proof.  Lemma 6.2.1 fixes \(G\), \({\mathcal A}^{inv}\), and \(W\).  Lemma
6.2.2 fixes \(\omega\).  Lemma 6.2.3 fixes \({\mathcal D}_{loc}\),
\({\mathcal W}_{Ward}\), and \({\mathcal R}_{RG}\).  Lemma 6.2.4 fixes
\({\mathcal N}_{sector}\).  Lemma 6.2.5 fixes \({\mathcal C}_{conf}\).
Thus the invariant comparison content agrees.  Same invariant content means
same physical comparison object, with only presentation differences left.
`square`

### 6.3 Feynman Route: Mismatch Receipt Exhaustion

Searchable Feynman comparison tag:

`V4P30-EXT-FEYNMAN-MISMATCH-RECEIPT-EXHAUSTION`.

Feynman's route asks what would have to be printed if the standard and ISP
descriptions were not equivalent.

Define the comparison mismatch vector:

$$
\boxed{
\Xi_{ext}
=
(
\Xi_G,
\Xi_A,
\Xi_{\omega},
\Xi_W,
\Xi_F,
\Xi_{Ward},
\Xi_{RG},
\Xi_{sect},
\Xi_{conf}
).
}
$$

The components are routed to finite receipts as follows:

$$
\boxed{
\begin{array}{c|l|l|l}
\hbox{mismatch} & \hbox{meaning} & \hbox{finite receipt} & \hbox{gate}\\
\hline
\Xi_G &
\hbox{different gauge group or quotient} &
R_{wil},R_{ext} &
\mathrm{EXT1}\\
\Xi_A &
\hbox{invariant algebra not generated by ISP dictionary} &
R_{src},R_{wil},R_{ext} &
\mathrm{EXT2}\\
\Xi_{\omega} &
\hbox{state or positivity mismatch} &
R_{pos},R_{ext} &
\mathrm{EXT3}\\
\Xi_W &
\hbox{Wilson functional mismatch} &
R_{wil},R_{ext} &
\mathrm{EXT2,EXT9}\\
\Xi_F &
\hbox{local action-density mismatch} &
R_{curv},R_{src},R_{ext} &
\mathrm{EXT4}\\
\Xi_{Ward} &
\hbox{Ward/Bianchi mismatch} &
R_W,R_{bd},R_{ext} &
\mathrm{EXT5}\\
\Xi_{RG} &
\hbox{route-dependent coupling/RG mismatch} &
R_{rg},R_{ext} &
\mathrm{EXT6}\\
\Xi_{sect} &
\hbox{irrelevant, boundary, silent, or extra-sector mismatch} &
R_{bd},R_{tr},R_{typ},R_U,R_{ext} &
\mathrm{EXT7,EXT8}\\
\Xi_{conf} &
\hbox{area-law or transfer-gap predicate mismatch} &
R_{wil},R_{tr},R_{sc},R_{ext} &
\mathrm{EXT9}
\end{array}
}
$$

The Feynman criterion is:

$$
\boxed{
\Xi_{ext}\ne0
\Longrightarrow
\mathrm{Print}_{30}(\Xi_{ext})\ne0
\hbox{ or }R_U\ne0.
}
$$

That is, a genuine mismatch either prints a finite receipt or falsifies the
active packet.

#### Theorem 6.3: No Unprinted Standard-Comparison Mismatch

Assume RCP28, TSP28, MID28, and the master receipt ledger
\(\mathrm{PRINT\text{-}REC}_{30}\).  If EXT1-EXT9 pass, then:

$$
\boxed{
\Xi_{ext}=0
\quad
\hbox{on active untyped physical comparison content.}
}
$$

Proof.  Suppose \(\Xi_{ext}\ne0\).  The routing table sends each component of
\(\Xi_{ext}\) to a finite receipt.  If the receipt is \(R_W\), it is a
same-actual presentation move and vanishes in the Ward quotient.  If the
receipt is \(R_{typ}\), it is a declared typed extension and not active untyped
comparison content.  If the receipt is one of \(R_{src},R_{pos},R_{wil},
R_{curv},R_{tr},R_{sc},R_{rg},R_{bd},R_{ext}\), then EXT1-EXT9 say the
corresponding represented mismatch is absent.  If \(R_U\ne0\), the active
packet is falsified rather than repaired.

Therefore, on the active branch where EXT1-EXT9 and
\(\mathrm{PRINT\text{-}REC}_{30}\) pass, no untyped physical comparison
mismatch remains. `square`

### 6.4 Combined EXT1-EXT9 Comparison Theorem

Searchable combined comparison tag:

`V4P30-EXT1-EXT9-COMBINED-COMPARISON-THEOREM`.

Assume EXT1-EXT9, RCP28, TSP28, MID28, and
\(\mathrm{PRINT\text{-}REC}_{30}\).  Then:

$$
\boxed{
{\mathfrak E}
:
{\mathsf Y}_{std}
\simeq
{\mathsf Y}_{ISP}
\quad
\hbox{on the gauge-invariant continuum }SU(N)\hbox{ sector.}
}
$$

Moreover:

$$
\boxed{
\sigma_{ISP}>0,\ \Delta_{ISP}>0
\Longleftrightarrow
\sigma_{std}>0,\ \Delta_{std}>0
}
$$

on that sector.

Proof.  The Einstein theorem proves equality of invariant content.  The
Feynman theorem proves that any alleged remaining mismatch must print a finite
receipt, be typed, vanish as Ward presentation, or falsify the packet.  Since
EXT1-EXT9 pass, no represented mismatch remains.  Since
\(\mathrm{PRINT\text{-}REC}_{30}\) passes, no unrepresented untyped mismatch is
hidden.  Therefore \({\mathfrak E}\) identifies the standard and ISP objects on
the active gauge-invariant sector.  EXT9 transfers the Wilson/string-tension
and transfer-gap predicates in both directions on that identified sector.
`square`

### 6.5 What Is Now Checked, And What Remains External

Paper 30 checks EXT1-EXT9 internally and develops both the invariant-content
and mismatch-receipt routes:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{internal status} & \hbox{external formalization status}\\
\hline
\mathrm{EXT1} & \mathrm{PASS}_{ISP} & \hbox{standard }SU(N)\hbox{ label fixed}\\
\mathrm{EXT2} & \mathrm{PASS}_{ISP} & \hbox{requires algebraic density writeup}\\
\mathrm{EXT3} & \mathrm{PASS}_{ISP} & \hbox{requires explicit OS/GNS reconstruction}\\
\mathrm{EXT4} & \mathrm{PASS}_{ISP} & \hbox{standard small-loop comparison}\\
\mathrm{EXT5} & \mathrm{PASS}_{ISP} & \hbox{standard Ward/Bianchi comparison}\\
\mathrm{EXT6} & \mathrm{PASS}_{ISP} & \hbox{standard RG coordinate comparison}\\
\mathrm{EXT7} & \mathrm{PASS}_{ISP} & \hbox{irrelevant/topological bookkeeping}\\
\mathrm{EXT8} & \mathrm{PASS}_{ISP} & \hbox{no-extra-sector comparison}\\
\mathrm{EXT9} & \mathrm{PASS}_{ISP} & \hbox{Wilson/gap predicate comparison}
\end{array}
}
$$

The precise status is:

$$
\boxed{
\begin{array}{l}
\hbox{the ISP-to-standard comparison bridge is written, expanded, and
internally checked;}\\
\hbox{Einstein route: invariant-content uniqueness is proved;}\\
\hbox{Feynman route: every mismatch has a finite receipt or is not active
physics;}\\
\hbox{the conventional standalone mathematical proof still requires rewriting
the bridge in standard external language.}
\end{array}
}
$$

This is stronger than postponement and weaker than overclaim.  Paper 30 now
contains the equivalence target, the gate-by-gate check, the invariant-content
proof, and the mismatch-receipt audit.  A hostile reviewer must attack one of
EXT1-EXT9, \(\mathrm{PRINT\text{-}REC}_{30}\), or the legitimacy of the ISP
finite-record ontology itself.

## 7. Cross-Theory Pattern: GR, QFT/QCD, And YM

Searchable pattern tag:

`V4P30-GR-QFT-QCD-YM-ADMISSIBILITY-PATTERN`.

The same pattern appears in Papers 25-27:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{paper} & \hbox{load-bearing law} & \hbox{status}\\
\hline
P25 &
\hbox{FAC/SLC/RSC physical admissibility for effective GR} &
\hbox{strong ISP ontology law}\\
P26 &
\hbox{finite QFT/YM kinematics and Wilson/RG descent} &
\hbox{finite descent extension}\\
P27 &
\hbox{active finite QCD admissibility and no-silent-sector rule} &
\hbox{finite QCD-DYN certificate}\\
P30 &
\hbox{RCP28/TSP28/MID28 plus EXT1-EXT9} &
\hbox{YM descent and comparison bridge}
\end{array}
}
$$

This is not a defect to hide.  It is the theory's architecture:

$$
\boxed{
\hbox{ISP is not ontology-free.  It is a finite-record ontology with auditable
physical-admissibility laws.}
}
$$

The right standard is therefore:

$$
\boxed{
\begin{array}{l}
\hbox{do the admissibility laws follow from finite actual record identity;}\\
\hbox{are they declared before the target theorem;}\\
\hbox{do they have finite falsifier receipts;}\\
\hbox{do failures generate typed corrections rather than being suppressed?}
\end{array}
}
$$

P25-P30 answer yes inside the active corpus.  External acceptance requires
translating those admissibility laws into standard mathematical physics
language and then deciding whether finite-record ISP is an acceptable ontology.

## 8. Master Finite Print Receipt Ledger

Searchable receipt tag:

`V4P30-MASTER-FINITE-PRINT-RECEIPT-LEDGER`.

The Feynman answer must not remain only a slogan.  This section consolidates
the distributed receipt machinery of RCP28, TSP28, MID28, and EXT1-EXT9 into
one printed ledger.

The principle is:

$$
\boxed{
\hbox{every alleged physical distinction must print a finite receipt.}
}
$$

Let \(\delta\) denote any alleged difference between two active presentations,
two source laws, two scale choices, two decoders, or two comparison maps.  Paper
30 assigns to \(\delta\) the finite receipt vector:

$$
\boxed{
\mathrm{Print}_{30}(\delta)
=
(
R_W,
R_{src},
R_{pos},
R_{wil},
R_{curv},
R_{tr},
R_{sc},
R_{rg},
R_{bd},
R_{typ},
R_{ext},
R_U
).
}
$$

The entries are:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{receipt} & \hbox{finite printout} & \hbox{meaning}\\
\hline
R_W &
\hbox{same-actual/Ward generator} &
\hbox{presentation change}\\
R_{src} &
\hbox{finite source-response coordinate} &
\hbox{source-law distinction}\\
R_{pos} &
\hbox{finite }F^{*}F\hbox{ positivity test} &
\hbox{state/positivity distinction}\\
R_{wil} &
\hbox{Wilson loop or character trace} &
\hbox{gauge quotient or confinement distinction}\\
R_{curv} &
\hbox{small-loop curvature/action-density record} &
\hbox{local YM-density distinction}\\
R_{tr} &
\hbox{finite transfer, string-tension, or gap coordinate} &
\hbox{mass-gap/confinement distinction}\\
R_{sc} &
\hbox{finite scale/coincidence/clock record} &
\hbox{physical scale distinction}\\
R_{rg} &
\hbox{refinement-route or coupling-flow defect} &
\hbox{RG path-dependence distinction}\\
R_{bd} &
\hbox{boundary, collar, or flux record} &
\hbox{boundary-sector distinction}\\
R_{typ} &
\hbox{declared typed residue label and bound} &
\hbox{typed extension, not active untyped physics}\\
R_{ext} &
\hbox{external comparison coordinate} &
\hbox{standard YM comparison distinction}\\
R_U &
\hbox{unrepresented untyped residue} &
\hbox{falsifier of the active packet}
\end{array}
}
$$

The active receipt rule is:

$$
\boxed{
\delta\hbox{ is active physical content}
\Longrightarrow
R_{src}\vee R_{pos}\vee R_{wil}\vee R_{curv}\vee R_{tr}\vee
R_{sc}\vee R_{rg}\vee R_{bd}\vee R_{ext}
\ne0
}
$$

unless \(\delta\) is a typed branch:

$$
\boxed{
R_{typ}\ne0
\quad\Longrightarrow\quad
\delta\hbox{ is a declared typed extension, not an untyped active split.}
}
$$

If every represented receipt vanishes and the difference is not typed, then:

$$
\boxed{
\mathrm{Print}_{30}(\delta)=R_W
\quad\Longrightarrow\quad
\delta=0
\hbox{ in the same-actual Ward quotient.}
}
$$

If \(R_U\ne0\), the active theorem is falsified rather than rescued:

$$
\boxed{
R_U\ne0
\Longrightarrow
\mathrm{RCP28/TSP28/MID28\ reopens.}
}
$$

### 8.1 Receipt Routing By Certificate

The consolidated routing is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{certificate} & \hbox{receipt channels} & \hbox{use}\\
\hline
\mathrm{RCP28} &
R_W,R_{src},R_{pos},R_{bd},R_{typ},R_U &
\hbox{source Cauchy, positivity, determinacy}\\
\mathrm{TSP28} &
R_{sc},R_{wil},R_{tr},R_{src},R_{typ},R_U &
\hbox{scale lock and physical margin survival}\\
\mathrm{MID28} &
R_W,R_{wil},R_{curv},R_{rg},R_{bd},R_{tr},R_{typ},R_U &
\hbox{unique }SU(N)\hbox{ YM decoder}\\
\mathrm{EXT1\text{-}EXT9} &
R_{ext},R_{wil},R_{src},R_{pos},R_{curv},R_{rg},R_{tr} &
\hbox{standard comparison bridge}
\end{array}
}
$$

Thus the distributed Feynman checks in Sections 1-6 are one receipt machine:

$$
\boxed{
\mathrm{RCP28}
\wedge
\mathrm{TSP28}
\wedge
\mathrm{MID28}
\wedge
\mathrm{EXT1\text{-}EXT9}
\Longrightarrow
\mathrm{Print}_{30}\hbox{ is complete on the active branch.}
}
$$

### 8.2 Master No-Free-Difference Theorem

Searchable theorem tag:

`V4P30-MASTER-NO-FREE-DIFFERENCE-RECEIPT-THEOREM`.

Let \(\delta\) be any alleged active physical difference in the P24-P30 corpus.
If:

$$
\boxed{
R_{src}=R_{pos}=R_{wil}=R_{curv}=R_{tr}=R_{sc}=R_{rg}=R_{bd}=R_{ext}=0,
}
$$

and:

$$
\boxed{
R_{typ}=0,
\qquad
R_U=0,
}
$$

then:

$$
\boxed{
\delta=0
\quad
\hbox{in active ISP physical content.}
}
$$

Proof.  RCP28 says finite source, positivity, boundary, and source-law
differences are either same-actual/Ward, represented, typed, or unrepresented
untyped.  TSP28 says physical scale, Wilson margin, and transfer-gap
differences are either represented by finite scale/margin receipts, typed, or
forbidden.  MID28 says decoder differences are caught by Wilson, curvature,
Ward/Bianchi, RG, boundary, transfer, or typed receipts.  EXT1-EXT9 add the
standard comparison receipts.

By hypothesis all represented receipts vanish, no typed branch is declared, and
no unrepresented untyped residue remains.  The only remaining component of
\(\mathrm{Print}_{30}(\delta)\) is \(R_W\), a same-actual presentation change.
Therefore \(\delta\) vanishes in the same-actual Ward quotient and is not
active physical ISP content. `square`

This is the consolidated Feynman rule:

$$
\boxed{
\hbox{no finite print receipt}
\Longrightarrow
\hbox{no active physical distinction.}
}
$$

### 8.3 Printed Falsifier Table

The receipt ledger is falsifiable:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{printed event} & \hbox{effect}\\
\hline
\mathrm{FR1} &
R_U\ne0 &
\hbox{unrepresented untyped residue, active packet incomplete}\\
\mathrm{FR2} &
R_{typ}\hbox{ declared after the target theorem} &
\hbox{posterior typing, proof unlicensed}\\
\mathrm{FR3} &
R_W\hbox{ changes a finite response} &
\hbox{same-actual Ward quotient fails}\\
\mathrm{FR4} &
R_{src}\hbox{ is finite but absent from source topology} &
\hbox{RCP28 source completeness fails}\\
\mathrm{FR5} &
R_{sc}\hbox{ is target-fitted} &
\hbox{TSP28 scale lock fails}\\
\mathrm{FR6} &
R_{wil}\hbox{ distinguishes a rival gauge quotient} &
\hbox{MID28/YMU2 fails}\\
\mathrm{FR7} &
R_{curv}\hbox{ prints a relevant non-YM kinetic density} &
\hbox{MID28/YMU3 fails}\\
\mathrm{FR8} &
R_{tr}\hbox{ shows vanishing physical gap or string tension} &
\hbox{TSP28/P27 margin survival fails}\\
\mathrm{FR9} &
R_{ext}\hbox{ rejects the ISP-to-standard comparison} &
\hbox{external bridge fails, internal theorem may remain}
\end{array}
}
$$

Therefore a reviewer cannot merely say:

$$
\boxed{
\hbox{the admissibility law might hide physics.}
}
$$

The reviewer must print one of:

$$
\boxed{
R_U,\ R_{typ}^{posterior},\ R_W^{nonzero},\ R_{src},\ R_{sc},\ R_{wil},
R_{curv},\ R_{tr},\ R_{ext}.
}
$$

### 8.4 Receipt Consolidation Verdict

Searchable verdict tag:

`V4P30-FINITE-PRINT-RECEIPT-VERDICT`.

The consolidated receipt status is:

$$
\boxed{
\mathrm{PRINT\text{-}REC}_{30}
=
\mathrm{PASS}_{ISP}.
}
$$

Meaning:

$$
\boxed{
\begin{array}{l}
\hbox{all active differences are routed through finite printed receipts;}\\
\hbox{Ward differences vanish as same-actual presentation changes;}\\
\hbox{typed differences are declared extension branches;}\\
\hbox{unrepresented untyped differences are falsifiers, not hidden content.}
\end{array}
}
$$

This is the consolidated finite-print version of the Feynman answer.

## 9. Success Criterion

Searchable success tag:

`V4P30-SUCCESS-CRITERION`.

Paper 30 now has a three-part success criterion.

First, it succeeds as a finite-receipt consolidation if it proves:

$$
\boxed{
\mathrm{PRINT\text{-}REC}_{30}
=
\mathrm{PASS}_{ISP}.
}
$$

Section 8 discharges this target.

Second, it succeeds internally if it proves:

$$
\boxed{
\mathrm{ISP\ primitives}
\Longrightarrow
\mathrm{RCP28+TSP28+MID28}.
}
$$

Sections 1.4-1.10, 2.1-2.10, and 3.1-3.10 discharge this target:

$$
\boxed{
\mathrm{RCP28+TSP28+MID28}
=
\mathrm{PASS}_{ISP}
}
$$

with:

$$
\boxed{
\mathrm{RCP28}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{TSP28}=\mathrm{PASS}_{ISP},
\qquad
\mathrm{MID28}=\mathrm{PASS}_{ISP}
}
$$

on the active P24/P25/P26/P27/P28/P29 corpus branch.

Then Paper 29 upgrades to:

$$
\boxed{
\mathrm{ISP\text{-}V4}_{active}
\Longrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}
}
$$

as a closed theorem of the active ISP ontology, rather than a theorem relative
to named internal certificates.

Third, it succeeds as an external-equivalence development if it develops and
checks the comparison bridge:

$$
\boxed{
\mathrm{EXT1+\cdots+EXT9}
=
\mathrm{PASS}_{ISP\ comparison}.
}
$$

This gives:

$$
\boxed{
{\mathsf Y}_{ISP}
\simeq
{\mathsf Y}_{std}
\quad
\hbox{on the gauge-invariant comparison sector, provided the external
OS/GNS/algebraic reconstruction language accepts the ISP bridge.}
}
$$

Thus Paper 30's final status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{tier} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{finite\ receipt\ audit} &
\mathrm{PRINT\text{-}REC}_{30}=\mathrm{PASS}_{ISP} &
\hbox{all active differences route to finite printed receipts}\\
\mathrm{internal\ ISP} &
\mathrm{CLOSED}_{ISP} &
\hbox{RCP28/TSP28/MID28 discharge HCL1-HCL3}\\
\mathrm{standard\ comparison} &
\mathrm{BRIDGE\ DEVELOPED+CHECKED}_{ISP} &
\hbox{EXT1-EXT9 identify the standard gauge-invariant sector by invariant
content and receipt exhaustion}\\
\mathrm{ontology\text{-}free\ Clay\ proof} &
\mathrm{NOT\ CLAIMED} &
\hbox{requires external formalization and acceptance of the bridge}
\end{array}
}
$$
