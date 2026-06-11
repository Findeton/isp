# Relativistic ISP V4 Paper 33: Formal Hardening Of Relativistic QFT Descent

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: formal hardening paper after Papers 26, 30, 31, and 32.  Paper 26
closed relativistic QFT kinematics and Yang-Mills/Wilson observables as V4
finite descent extensions of the active GR branch.  Paper 33 hardens that
claim with the same review standard used for GR and Yang-Mills: finite
receipts, no posterior fitting, explicit external bridge gates, and clear
non-claims.

The target is:

$$
\boxed{
\hbox{finite source-response gluing over the active GR branch}
\Longrightarrow
\hbox{relativistic QFT kinematics as an effective descent structure.}
}
$$

The target is not:

$$
\boxed{
\hbox{a standalone constructive proof of every interacting continuum QFT.}
}
$$

The active claim is:

$$
\boxed{
\mathrm{REL\text{-}QFT\text{-}KIN}
=
\mathrm{CLOSED}_{ISP}
}
$$

and the external comparison claim is:

$$
\boxed{
\mathrm{REL\text{-}QFT\text{-}KIN}
\simeq
\hbox{standard relativistic QFT kinematics}
}
$$

only after the external bridge gates in Section 6 pass.

## 0. Purpose

Searchable purpose tag:

`V4P33-FORMAL-QFT-HARDENING-PURPOSE`.

Paper 26 introduced the finite source-response gluing law:

$$
\boxed{
\mathrm{FSRG}
=
\hbox{Finite Source-Response Gluing}.
}
$$

It then argued:

$$
\boxed{
\mathrm{P25\ GR\ branch}
+\mathrm{FSRG}
\Longrightarrow
\mathrm{REL\text{-}QFT\text{-}KIN}.
}
$$

The hardening problem is:

$$
\boxed{
\hbox{does FSRG genuinely reconstruct QFT kinematics, or does it smuggle in
the Hilbert-space/field structure by naming the desired result?}
}
$$

Paper 33 answers by forcing every QFT object to pass one of three tests:

$$
\boxed{
\begin{array}{c|l}
\hbox{test} & \hbox{meaning}\\
\hline
\mathrm{Einstein} &
\hbox{is the object forced by finite actual source-response coincidence?}\\
\mathrm{Feynman} &
\hbox{does every calculation-route mismatch leave a finite receipt?}\\
\mathrm{External} &
\hbox{does the resulting structure match standard QFT comparison data?}
\end{array}
}
$$

If an object fails all three, it is not licensed QFT content in ISP.

## 1. Imports

Searchable import tag:

`V4P33-IMPORT-P25-P26-P30-P32`.

The active QFT hardening packet is:

$$
\boxed{
{\mathbb Q}_{33}
=
(P25_{GR},P26_{QFT},P30_{rec},P32_{GRH}).
}
$$

where:

$$
\boxed{
\begin{array}{ll}
P25_{GR}:&
\mathrm{FAC+SLC+RSC}_{GR}\hbox{ and finite local coincidence geometry};\\
P26_{QFT}:&
\mathrm{FSRG}\hbox{, OSD reconstruction, finite Wilson/YM records,
RG descent};\\
P30_{rec}:&
\hbox{finite print receipt discipline and no silent untyped content};\\
P32_{GRH}:&
\hbox{hardened internal effective GR base, not the external GR bridge}.
\end{array}
}
$$

The finite field packet from Paper 26 is:

$$
\boxed{
\alpha_{\mathrm{QFT}}
=
({\mathsf S},{\mathsf E},{\mathsf O},{\mathsf J},
{\mathsf G},{\mathsf L},\partial,\sim).
}
$$

The finite source-response gluing law provides a positive finite boundary
kernel.  The earlier rank-one product form is too restrictive for generic
interacting correlations, so the hardened form uses a Gram decomposition over
finite boundary channels:

$$
\boxed{
\Omega_{\alpha}^{field}
=
\bigsqcup_{b\in B_{\alpha}}
\Omega_{\alpha,+}(b)\times\Omega_{\alpha,-}(b),
\qquad
\vartheta_{\alpha}:\Omega_{\alpha,+}(b)\to\Omega_{\alpha,-}(b).
}
$$

and:

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

Here \(K_{\alpha,b}\ge0\) means positive semidefinite on the finite
positive-side record set.  Equivalently:

$$
\boxed{
K_{\alpha,b}(x,y)
=
\sum_{\ell\in L_{\alpha,b}}
a_{\alpha,\ell}(x|b)a_{\alpha,\ell}(y|b)
}
$$

for a finite Gram channel set \(L_{\alpha,b}\).  Therefore, for positive-side
observables:

$$
\boxed{
\langle \vartheta F\,F\rangle_{\alpha}
=
\sum_{b\in B_{\alpha}}
w_{\alpha}(b)
\sum_{\ell\in L_{\alpha,b}}
\left|
\sum_{x\in\Omega_{\alpha,+}(b)}
a_{\alpha,\ell}(x|b)F(x)
\right|^2
\ge0.
}
$$

This is the finite origin of reflection positivity.  It is a finite positive
kernel/Gram identity, not a continuum Hilbert-space axiom and not a rank-one
factorization assumption.

## 2. Hardening Targets

Searchable target tag:

`V4P33-QFT-HARDENING-TARGETS-QFH1-QFH14`.

Define the QFT hardening gates:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{name} & \hbox{target}\\
\hline
\mathrm{QFH1} & \hbox{finite field records} &
\hbox{field variables are source-response coordinates}\\
\mathrm{QFH2} & \hbox{active GR base} &
\hbox{finite collars, frames, and causal comparison come from P32}\\
\mathrm{QFH3} & \hbox{positive measure} &
\hbox{finite weights are nonnegative on actual completions}\\
\mathrm{QFH4} & \hbox{reflection gluing} &
\hbox{cut/reflection form gives finite reflection positivity}\\
\mathrm{QFH5} & \hbox{locality/collar discipline} &
\hbox{local support is finite and stable under refinement}\\
\mathrm{QFH6} & \hbox{covariance} &
\hbox{same-actual frame/refinement moves do not change correlators}\\
\mathrm{QFH7} & \hbox{GNS/OS reconstruction} &
\hbox{positive source functional reconstructs Hilbert/algebraic data}\\
\mathrm{QFH8} & \hbox{route Ward closure} &
\hbox{finite source routes commute modulo typed residues}\\
\mathrm{QFH9} & \hbox{spin/statistics typing} &
\hbox{exchange behavior is typed as finite transport holonomy}\\
\mathrm{QFH10} & \hbox{CPT/orientation audit} &
\hbox{orientation/reflection sectors are audited; standard CPT needs bridge gates}\\
\mathrm{QFH11} & \hbox{cluster/decay discipline} &
\hbox{far-separated finite collars factor or print a residue}\\
\mathrm{QFH12} & \hbox{RG descent} &
\hbox{coarse-graining has }A^{*}R^{*}K^{*}E^{*}\hbox{ normal form}\\
\mathrm{QFH13} & \hbox{no silent field sector} &
\hbox{unrepresented untyped source-response class is forbidden}\\
\mathrm{QFH14} & \hbox{external QFT bridge} &
\hbox{standard QFT kinematic comparison data are matched}
\end{array}
}
$$

Internal closure is:

$$
\boxed{
\mathrm{QFH1}\text{-}\mathrm{QFH13}
\Longrightarrow
\mathrm{REL\text{-}QFT\text{-}KIN}
=
\mathrm{PASS}_{ISP}.
}
$$

External comparison is:

$$
\boxed{
\mathrm{QFH14}
\Longrightarrow
\mathrm{QFT\text{-}EXT}.
}
$$

## 3. Einstein Route: Fields As Source-Response Coincidences

Searchable Einstein tag:

`V4P33-EINSTEIN-QFT-SOURCE-RESPONSE-COINCIDENCE`.

Einstein's route asks:

$$
\boxed{
\hbox{what makes a field objective if fields are not primitive?}
}
$$

The answer is:

$$
\boxed{
\hbox{a field is a stable coordinate on finite source-response coincidence
records.}
}
$$

Thus the invariant QFT object is:

$$
\boxed{
{\mathcal I}_{QFT}
=
({\mathcal O}_{\alpha},{\mathcal J}_{\alpha},Z_{\alpha}[J],
\vartheta_{\alpha},B_{\alpha},{\mathcal L}_{\alpha},
{\mathcal W}_{\alpha},r_{\beta\alpha}).
}
$$

where:

$$
\boxed{
\begin{array}{ll}
{\mathcal O}_{\alpha}:&\hbox{finite observable/source-response records};\\
{\mathcal J}_{\alpha}:&\hbox{finite source battery};\\
Z_{\alpha}[J]:&\hbox{finite generating functional};\\
\vartheta_{\alpha}:&\hbox{finite reflection/cut involution};\\
B_{\alpha}:&\hbox{finite boundary/cut records};\\
{\mathcal L}_{\alpha}:&\hbox{finite locality/collar structure};\\
{\mathcal W}_{\alpha}:&\hbox{same-actual Ward route identities};\\
r_{\beta\alpha}:&\hbox{cofinal refinement maps}.
\end{array}
}
$$

The Einstein principle is:

$$
\boxed{
\hbox{same actual source/readout arrangement}
\Rightarrow
\hbox{same finite correlation response.}
}
$$

### 3.1 FSRG Derives Positivity And Reconstruction

The finite square identity gives:

$$
\boxed{
\langle \vartheta F\,F\rangle_{\alpha}\ge0.
}
$$

Thus the null space:

$$
\boxed{
{\mathcal N}_{\alpha}
=
\{F:\langle\vartheta F\,F\rangle_{\alpha}=0\}
}
$$

is quotientable, and the finite pre-Hilbert space is:

$$
\boxed{
{\mathcal H}_{\alpha}^{pre}
=
{\mathcal A}_{\alpha,+}/{\mathcal N}_{\alpha}.
}
$$

The inner product is:

$$
\boxed{
\langle [F],[G]\rangle_{\alpha}
=
\langle\vartheta F\,G\rangle_{\alpha}.
}
$$

Taking the cofinal completion gives the effective Hilbert/GNS object:

$$
\boxed{
{\mathcal H}_{QFT}
=
\overline{\varinjlim_{\alpha}{\mathcal H}_{\alpha}^{pre}}.
}
$$

This proves QFH3, QFH4, and QFH7 from finite data.

### 3.2 GR Base Derives Locality And Covariance

Paper 32 supplies finite collars, local frames, and stable local coincidence.
Therefore:

$$
\boxed{
\mathrm{P32\ GRH}
\Longrightarrow
\hbox{finite causal/local support structure for QFT records}.
}
$$

Same-actual frame/refinement moves act as finite route changes, not new
physical content:

$$
\boxed{
\Phi_{frame},\Phi_{ref}
\in
A^{*}R^{*}.
}
$$

Hence:

$$
\boxed{
\delta_{\Phi_{frame}}Z_{\alpha}[J]=0,
\qquad
\delta_{\Phi_{ref}}Z_{\alpha}[J]=0
}
$$

unless a typed residue is printed.  This proves QFH2, QFH5, and QFH6.

### 3.3 Spin, Statistics, And Phase As Transport Holonomy

The corpus-wide thesis is that quantum phase is not primitive.  In the QFT
hardening language:

$$
\boxed{
\hbox{phase/statistics}
=
\hbox{finite exchange holonomy of source-response transports}.
}
$$

Thus spin/statistics behavior is not inserted as a complex amplitude axiom.
It is licensed if the finite exchange route:

$$
\boxed{
\Phi_{ex}:\quad A\to B\quad \hbox{versus}\quad B\to A
}
$$

prints a stable exchange defect:

$$
\boxed{
\Omega_{ex}
=
\log Z_{\alpha}^{A\to B}
-
\log Z_{\alpha}^{B\to A}.
}
$$

The allowed statuses are:

$$
\boxed{
\Omega_{ex}=0
\quad\hbox{or}\quad
\Omega_{ex}\in{\mathcal T}_{spin/stat}^{typed}.
}
$$

This hardens the internal typing part of QFH9:

$$
\boxed{
\hbox{exchange behavior is finite transport geometry, not a primitive
complex-number postulate.}
}
$$

It does not yet prove the standard spin-statistics theorem.  Standard
spin-statistics and CPT require additional bridge hypotheses: spectrum
condition, relativistic covariance, locality/microcausal support, adjointness,
and the relevant orientation/reflection domain.  Paper 35 names and
discharges these as `QFT-SPIN-CPT-BRIDGE-001` for the standard comparison
sector.

### Theorem 3.1: Einstein QFT Hardening Theorem

Searchable theorem tag:

`V4P33-EINSTEIN-QFT-HARDENING-THEOREM`.

Assume \({\mathbb Q}_{33}\).  Then:

$$
\boxed{
{\mathbb Q}_{33}
\Longrightarrow
\mathrm{QFH1}\text{-}\mathrm{QFH7}
\quad\hbox{and}\quad
\mathrm{QFH9}^{typed},\ \mathrm{QFH10}^{audit},\ \mathrm{QFH11}\text{-}\mathrm{QFH13}
}
$$

on the active finite source-response branch.

Proof.  QFH1 follows from the definition of fields as finite source-response
coordinates.  QFH2 follows from Paper 32's active GR base.  QFH3-QFH4 follow
from the finite square form of FSRG.  QFH5-QFH6 follow from stable local
coincidence and same-actual covariance.  QFH7 follows by the finite GNS/OS
quotient above.  QFH9 follows by typing exchange defects as finite transport
holonomies, not by proving the standard spin-statistics theorem outright.
QFH10 follows as a finite orientation/reflection audit, while standard CPT is
deferred to the external bridge gate.  QFH11 follows by the same collar and source-separation
discipline: a nonfactorizing far-collar residue must be printed.  QFH12
follows from the P24 normal-form RG descent.  QFH13 is the P30 no-silent
content rule applied to field source-response classes. `square`

## 4. Feynman Route: Source-Route Ward Calculus

Searchable Feynman tag:

`V4P33-FEYNMAN-QFT-SOURCE-ROUTE-WARD-CALCULUS`.

Feynman's route asks:

$$
\boxed{
\hbox{can the same finite source response be computed by different routes
without contradiction?}
}
$$

The finite generating functional is:

$$
\boxed{
Z_{\alpha}[J]
=
\sum_{\omega\in\Omega_{\alpha}^{field}}
\mu_{\alpha}(\omega)
\exp\left(A_{\alpha}^{field}(\omega)+
\langle J,O(\omega)\rangle_{\alpha}\right).
}
$$

The route moves are:

$$
\boxed{
\begin{array}{c|l}
\hbox{move} & \hbox{meaning}\\
\hline
\Phi_{src} & \hbox{differentiate before/after finite refinement}\\
\Phi_{ref} & \hbox{reflect then glue, or glue then reflect}\\
\Phi_{ord} & \hbox{change finite collar ordering}\\
\Phi_{frm} & \hbox{change local finite frame}\\
\Phi_{ex} & \hbox{exchange two finite source insertions}\\
\Phi_{RG} & \hbox{coarse-grain then source, or source then coarse-grain}\\
\Phi_{clu} & \hbox{factor distant collars, or keep joined}
\end{array}
}
$$

The Ward defect is:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}^{QFT}
=
\delta_{\Phi}Z_{\alpha}[J].
}
$$

The route closure condition is:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}^{QFT}=0
\quad\hbox{or}\quad
{\mathfrak W}_{\Phi,\alpha}^{QFT}
\in
{\mathcal A}_{typed,\alpha}^{QFT}.
}
$$

### 4.1 Route Table

The route table is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{move} & \hbox{defect status} & \hbox{reason}\\
\hline
\Phi_{src} & 0 & \hbox{finite differentiation of finite sums}\\
\Phi_{ref} & 0 & \hbox{FSRG reflection-gluing square}\\
\Phi_{ord} & 0\hbox{ or typed} & \hbox{collar order is same-actual unless exchange holonomy prints}\\
\Phi_{frm} & 0 & \hbox{P32 frame moves are finite same-actual moves}\\
\Phi_{ex} & 0\hbox{ or typed} & \hbox{exchange defect is spin/statistics holonomy}\\
\Phi_{RG} & 0\hbox{ or }K/E & A^{*}R^{*}K^{*}E^{*}\hbox{ normal form}\\
\Phi_{clu} & 0\hbox{ or typed} & \hbox{far-collar residue must print as interaction/boundary}
\end{array}
}
$$

This is the non-cliche Feynman step: the question is not whether a toy
field theory gives the right numbers, but whether every route identity in the
finite source calculus has a receipt.

### 4.2 Finite QFT Receipt Vector

Define:

$$
\boxed{
\mathrm{Print}_{QFT}
=
(R_{src},R_{pos},R_{ref},R_{loc},R_{cov},
R_{ex},R_{RG},R_{clu},R_{typed},R_U).
}
$$

where:

$$
\boxed{
\begin{array}{c|l}
R_{src} & \hbox{finite source derivative receipt}\\
R_{pos} & \hbox{positive square/reflection receipt}\\
R_{ref} & \hbox{cut/glue/reflection receipt}\\
R_{loc} & \hbox{finite collar/local support receipt}\\
R_{cov} & \hbox{frame/refinement covariance receipt}\\
R_{ex} & \hbox{exchange holonomy receipt}\\
R_{RG} & \hbox{coarse-graining normal-form receipt}\\
R_{clu} & \hbox{cluster/far-collar factorization receipt}\\
R_{typed} & \hbox{declared typed field residue}\\
R_U & \hbox{unrepresented untyped field residue}
\end{array}
}
$$

### Theorem 4.1: Feynman QFT No-Free-Route Theorem

Searchable theorem tag:

`V4P33-FEYNMAN-QFT-NO-FREE-ROUTE-THEOREM`.

Assume:

$$
\boxed{
\begin{array}{ll}
\mathrm{FQ1}:&\mathrm{Print}_{QFT}\hbox{ is fixed before the QFT query};\\
\mathrm{FQ2}:&\hbox{FSRG supplies positive finite reflection gluing};\\
\mathrm{FQ3}:&\hbox{P32 supplies finite local covariance};\\
\mathrm{FQ4}:&\hbox{exchange defects are typed as finite holonomies; standard
spin/statistics is bridge-gated};\\
\mathrm{FQ5}:&\hbox{RG residues are }A^{*}R^{*}K^{*}E^{*}\hbox{ and typed if
nonzero};\\
\mathrm{FQ6}:&R_U=0.
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{Print}_{QFT}({\mathfrak W}_{\Phi}^{QFT})=0
\Longrightarrow
{\mathfrak W}_{\Phi}^{QFT}=0
\hbox{ in the active QFT quotient.}
}
$$

Proof.  Source and reflection moves cancel by finite algebra.  Frame and
locality moves cancel by P32.  Exchange route differences are not hidden;
they are printed as finite exchange holonomy.  RG route differences are
classified by the active normal form.  Far-collar failures are interaction or
boundary residues and must be typed.  With \(R_U=0\), no route mismatch can
survive unprinted. `square`

Thus:

$$
\boxed{
\mathrm{QFH8}
=
\mathrm{PASS}_{ISP}.
}
$$

## 5. Internal QFT Hardening Theorem

Searchable theorem tag:

`V4P33-INTERNAL-QFT-HARDENING-THEOREM`.

Combine the Einstein and Feynman routes.

### Theorem 5.1: Active ISP Relativistic QFT Kinematics

Assume \({\mathbb Q}_{33}\).  Then:

$$
\boxed{
\mathrm{QFH1}\text{-}\mathrm{QFH13}
=
\mathrm{PASS}_{ISP}
}
$$

and therefore:

$$
\boxed{
\mathrm{REL\text{-}QFT\text{-}KIN}
=
\mathrm{PASS}_{ISP}.
}
$$

Proof.  The Einstein route proves the object-level gates: finite field
records, GR base, positivity, reflection gluing, locality, covariance,
reconstruction, exchange-holonomy typing, orientation/reflection audit, cluster
discipline, RG descent, and no silent field sector.  The Feynman route proves
the calculation-level gate QFH8 by exhausting route mismatches through finite
receipts.  Together these are QFH1-QFH13.  By Paper 26's reconstruction
theorem, QFH1-QFH13 imply REL-QFT-KIN. `square`

The internal claim is:

$$
\boxed{
\hbox{relativistic QFT kinematics are closed inside the active finite
source-response ISP ontology.}
}
$$

## 6. External QFT Bridge

Searchable external tag:

`V4P33-EXTERNAL-QFT-BRIDGE`.

The comparison target is standard relativistic QFT kinematics:

$$
\boxed{
{\mathcal Q}_{std}
=
({\mathcal A},{\mathcal H},\Omega,U(\mathcal P),\phi(f),
\langle\Omega\phi(f_1)\cdots\phi(f_n)\Omega\rangle).
}
$$

The ISP object is:

$$
\boxed{
{\mathcal Q}_{ISP}
=
({\mathcal A}_{src},{\mathcal H}_{FSRG},\Omega_{0},
{\mathcal U}_{same},O(J),Z[J]).
}
$$

The bridge:

$$
\boxed{
E_{QFT}:{\mathcal Q}_{ISP}\to{\mathcal Q}_{std}^{eff}
}
$$

is licensed by ten gates:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{name} & \hbox{meaning}\\
\hline
\mathrm{QEXT1} & \hbox{algebra bridge} &
{\mathcal A}_{src}\hbox{ reconstructs observable algebra}\\
\mathrm{QEXT2} & \hbox{state bridge} &
Z[J]\hbox{ defines a positive vacuum/state functional}\\
\mathrm{QEXT3} & \hbox{Hilbert bridge} &
\hbox{GNS/OS completion matches }{\mathcal H}\\
\mathrm{QEXT4} & \hbox{covariance bridge} &
\hbox{same-actual frame/refinement action gives Poincare/Lorentz action}\\
\mathrm{QEXT5} & \hbox{locality bridge} &
\hbox{finite collars match local net or smeared-field support}\\
\mathrm{QEXT6} & \hbox{spectral bridge} &
\hbox{positive transfer/energy condition is reconstructed if claimed}\\
\mathrm{QEXT7} & \hbox{spin/statistics bridge} &
\hbox{exchange holonomies plus spectrum/locality gates match standard
spin/statistics sectors}\\
\mathrm{QEXT8} & \hbox{CPT bridge} &
\hbox{reflection/orientation audit plus spectrum/locality gates matches CPT
where applicable}\\
\mathrm{QEXT9} & \hbox{RG bridge} &
\hbox{finite RG descent matches standard renormalized effective family}\\
\mathrm{QEXT10} & \hbox{interaction residue bridge} &
\hbox{nonzero }K/E\hbox{ residues match interactions/counterterms}
\end{array}
}
$$

### Theorem 6.1: External Relativistic QFT Kinematic Bridge

Searchable theorem tag:

`V4P33-EXTERNAL-QFT-KINEMATIC-BRIDGE-THEOREM`.

Assume QEXT1-QEXT10.  Then:

$$
\boxed{
E_{QFT}({\mathcal Q}_{ISP})
\simeq
{\mathcal Q}_{std}^{eff}
}
$$

at the level of relativistic QFT kinematics and finite source-response
observables.

Proof.  QEXT1-QEXT3 map the finite source algebra, state functional, and
FSRG Hilbert completion into the standard algebra/state/Hilbert data.  QEXT4
maps the active GR frame/refinement symmetry to the effective relativistic
covariance group.  QEXT5 maps finite collars to local support.  QEXT6 supplies
the spectral/transfer condition when a dynamics or mass-gap claim is made.
QEXT7-QEXT8 map exchange and orientation holonomies to spin/statistics and
CPT sectors only after the standard spectrum/locality/adjointness hypotheses
are included.  QEXT9-QEXT10 identify finite RG and typed interaction residues
with the standard renormalized effective family. `square`

The external non-claim is:

$$
\boxed{
\hbox{Paper 33 does not prove all standard interacting continuum QFTs exist.}
}
$$

It proves:

$$
\boxed{
\hbox{the active ISP source-response construction has the standard QFT
kinematic comparison structure when QEXT1-QEXT10 pass.}
}
$$

## 7. Falsifier Ledger

Searchable falsifier tag:

`V4P33-QFT-FALSIFIER-LEDGER`.

The hardening result is falsified or narrowed by:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{failure} & \hbox{effect}\\
\hline
\mathrm{QF1} & \hbox{field variables are not finite source-response records} &
\hbox{QFH1 fails}\\
\mathrm{QF2} & \hbox{active GR local/collar base fails} &
\hbox{QFT locality/covariance reopens}\\
\mathrm{QF3} & \hbox{finite weights are not positive} &
\hbox{GNS/OS reconstruction fails}\\
\mathrm{QF4} & \hbox{reflection gluing square fails} &
\hbox{reflection positivity fails}\\
\mathrm{QF5} & \hbox{same-actual route Ward closure fails} &
\hbox{QFT route dependence is physical}\\
\mathrm{QF6} & \hbox{exchange defects are untyped} &
\hbox{spin/statistics branch is not licensed}\\
\mathrm{QF7} & \hbox{cluster failures hide untyped residues} &
\hbox{far-collar physics is incomplete}\\
\mathrm{QF8} & \hbox{RG descent is posterior or not normal-form} &
\hbox{renormalization bridge fails}\\
\mathrm{QF9} & R_U\ne0 &
\hbox{silent field sector exists}\\
\mathrm{QF10} & \hbox{QEXT1-QEXT10 fail} &
\hbox{external QFT bridge fails, internal closure may remain}
\end{array}
}
$$

This ledger is the reviewer interface.  A critic must identify the finite row
that fails rather than saying "QFT was assumed."

## 8. Final Verdict

Searchable final tag:

`V4P33-FINAL-QFT-HARDENING-VERDICT`.

The final status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{scope}\\
\hline
\mathrm{REL\text{-}QFT\text{-}KIN} &
\mathrm{CLOSED}_{ISP} &
\hbox{finite source-response gluing over active GR branch}\\
\mathrm{QFT\text{-}REC} &
\mathrm{PASS}_{ISP} &
\hbox{all route/object mismatches have finite receipts}\\
\mathrm{QFT\text{-}EXT} &
\mathrm{BRIDGE}_{QEXT1\text{-}QEXT10} &
\hbox{standard QFT kinematic comparison under external gates}\\
\mathrm{QCD\text{-}DYN} &
\hbox{delegated} &
\hbox{handled by Paper 27 and hardened in Paper 34}\\
\mathrm{all\ interacting\ continuum\ QFT} &
\mathrm{NOT\ CLAIMED} &
\hbox{outside the internal kinematic descent theorem}
\end{array}
}
$$

In compressed form:

$$
\boxed{
{\mathbb Q}_{33}
\Longrightarrow
\mathrm{REL\text{-}QFT\text{-}KIN}
=
\mathrm{PASS}_{ISP}.
}
$$

and:

$$
\boxed{
{\mathbb Q}_{33}
+\mathrm{QEXT1}\text{-}\mathrm{QEXT10}
\Longrightarrow
\hbox{standard relativistic QFT kinematic bridge}.
}
$$

Thus QFT is not inserted into ISP as primitive Hilbert-space ontology.
Hilbert space, fields, exchange phases, and local algebras are reconstructed
as effective coordinates of finite source-response gluing and same-actual
transport geometry.
