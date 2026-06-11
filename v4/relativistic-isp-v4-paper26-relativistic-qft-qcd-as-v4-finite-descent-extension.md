# Relativistic ISP V4 Paper 26: Relativistic QFT And QCD As V4 Finite Descent Extensions

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: developed V4 embedding and audit after Paper 25.  Paper 26 asks
whether the V3 QFT/QCD reconstruction architecture can be embedded into the
V4 finite descent framework over the active GR-compatible finite actual
branch, without reopening the missing value-source problem.

The target is:

$$
\boxed{
\hbox{V3 finite QFT/QCD certificates}
\Rightarrow
\hbox{V4 finite descent packets}
\Rightarrow
\hbox{effective relativistic QFT/QCD}.
}
$$

Paper 26 does not claim unconditional nonperturbative \(4D\) QCD confinement
or a Clay-style mass-gap theorem unless the V3 source certificates are
actually embedded and audited.  Its positive target is sharper:

$$
\boxed{
\hbox{relativistic QFT/gauge kinematics and finite Wilson/Yang-Mills
observables are V4 finite descent extensions of the P25 GR branch.}
}
$$

The dynamic target is to turn every V3 source gate into a V4 finite descent
extension:

$$
\boxed{
E_{\mathrm{gauge/QFT}}.
}
$$

## 0. Imports From Papers 24, 25, And V3

Paper 24 supplies the finite descent family:

$$
\boxed{
{\mathfrak A}^{act}
=
\{\mathrm{Desc}(\alpha)\}_{\alpha\in{\mathcal R}},
}
$$

and the normal form:

$$
\boxed{
M\Rightarrow A^{*}R^{*}K^{*}E^{*}.
}
$$

Paper 25 supplies the active GR-compatible branch:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

Its final selection rule is:

$$
\boxed{
\hbox{surviving same-actual Ward cohomology }
=
\hbox{ physical ISP content.}
}
$$

For the active P20-P25 corpus, the surviving finite content is already
represented by:

$$
\boxed{
\hbox{GR-effective Cartan/Wilson geometry}
\quad\hbox{and}\quad
\hbox{finite stress-source response.}
}
$$

The V3 provenance supplies:

$$
\boxed{
\begin{array}{c|l}
\hbox{V3 block} & \hbox{imported content}\\
\hline
V3P1\text{-}P8 & \hbox{QFT reconstruction and no-go gates}\\
V3P9\text{-}P18 & \hbox{finite gauge sectors, Yang-Mills, confinement gates}\\
V3P19\text{-}P30 & \hbox{actual source constants and campaigns}\\
V3P31\text{-}P37 & \hbox{same-law response, Ward/Stein, scalar frontier}
\end{array}
}
$$

Searchable import tag:

`V4P26-IMPORT-V3-P24-P25`.

## 1. QFT/QCD Target Gates

Searchable target tag:

`V4P26-QFT-QCD-TARGET-GATES`.

Paper 26 tests:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{name} & \hbox{target}\\
\hline
\mathrm{QFT1} &
\hbox{finite field records} &
\hbox{fields as finite record observables or source-response coordinates}\\
\mathrm{QFT2} &
\hbox{locality/covariance} &
\hbox{finite causal/projective locality under descent}\\
\mathrm{QFT3} &
\hbox{correlators and reconstruction} &
\hbox{OS/Wightman-style effective reconstruction from finite data}\\
\mathrm{QCD1} &
\hbox{gauge invariance} &
\hbox{gauge changes are refinement moves}\\
\mathrm{QCD2} &
\hbox{Wilson loops/holonomy} &
\hbox{finite trace holonomies reproduce gauge observables}\\
\mathrm{QCD3} &
\hbox{confinement/mass gap} &
\hbox{v3 source constants become V4 finite descent extensions}
\end{array}
}
$$

## 2. V3-To-V4 Translation Dictionary

Searchable dictionary tag:

`V4P26-V3-TO-V4-DICTIONARY`.

The translation is:

$$
\boxed{
\begin{array}{c|c}
\hbox{V3 object} & \hbox{V4 descent object}\\
\hline
\hbox{finite gauge sector} & \alpha_{\mathrm{gauge}}\\
\hbox{Wilson loop record} & \operatorname{Tr}\prod U_e^{fin}\\
\hbox{source constant} & E_{\mathrm{source}}\hbox{ with finite index/trace}\\
\hbox{gauge transformation} & R\hbox{-move}\\
\hbox{confinement certificate} & E_{\mathrm{conf}}\hbox{ plus finite transfer gap}\\
\hbox{mass-gap gate} & \hbox{finite transfer spectral gap}\\
\hbox{OS reconstruction gate} & \hbox{finite reflection-positive projective family}
\end{array}
}
$$

The core embedding is:

$$
\boxed{
{\mathcal A}^{act}_{\alpha_{\mathrm{QFT/QCD}}}
=
\mathrm{Desc}(\alpha_{\mathrm{QFT/QCD}}).
}
$$

## 3. Finite Field Descent Context

Searchable construction tag:

`V4P26-FINITE-FIELD-DESCENT-CONTEXT`.

A finite QFT context is:

$$
\boxed{
\alpha_{\mathrm{QFT}}
=
({\mathsf S},{\mathsf E},{\mathsf O},{\mathsf J},
{\mathsf G},{\mathsf L},\partial,\sim).
}
$$

where:

$$
\boxed{
\begin{array}{ll}
{\mathsf S}:&\hbox{finite spacetime/boundary records};\\
{\mathsf E}:&\hbox{finite causal or lattice-like edges};\\
{\mathsf O}:&\hbox{finite observable records};\\
{\mathsf J}:&\hbox{finite source records};\\
{\mathsf G}:&\hbox{finite gauge/presentation redundancies};\\
{\mathsf L}:&\hbox{finite locality/collar data};\\
\partial:&\hbox{finite incidence maps};\\
\sim:&\hbox{record/gauge equivalence}.
\end{array}
}
$$

The descent packet is:

$$
\boxed{
\mathrm{Desc}(\alpha_{\mathrm{QFT}})
=
({\mathcal K}_{\mathrm{QFT}},
{\mathcal H}_{\mathrm{QFT}},
\Xi_{\mathrm{QFT}},
K_{\mathrm{QFT}}^{corner},
r_{\mathrm{QFT}},
\lambda_{\mathrm{QFT}}).
}
$$

## 4. Gauge Invariance As Refinement

Searchable principle tag:

`V4P26-GAUGE-AS-REFINEMENT`.

Gauge transformations must be \(R\)-moves:

$$
\boxed{
g\in{\mathcal G}_{fin}
\quad\Rightarrow\quad
\alpha\le_{\mathrm{ref}}g\alpha.
}
$$

Therefore:

$$
\boxed{
\Delta_g Q=0,
\qquad
\Delta_g C=0.
}
$$

Any gauge transformation that changes a physical value is not a refinement.
It is either:

$$
\boxed{
\hbox{a physical extension}
}
$$

or:

$$
\boxed{
\hbox{a failure of the gauge-as-refinement hypothesis.}
}
$$

## 5. Interactions As Source Extensions

Searchable construction tag:

`V4P26-INTERACTIONS-AS-SOURCE-EXTENSIONS`.

Interactions are not hidden refinements.  They are finite source extensions:

$$
\boxed{
E_{\mathrm{int}}:
\alpha_{\mathrm{free}}
\to
\alpha_{\mathrm{int}}.
}
$$

Their value effect is:

$$
\boxed{
\Delta Q_{\mathrm{int}}
=
\operatorname{Ind}_{fin}({\mathcal K}_{\mathrm{int}}),
}
$$

and any corner/gauge anomaly is:

$$
\boxed{
\Delta C_{\mathrm{int}}
=
-\dim K_{\mathrm{int}}^{corner}.
}
$$

This is where v3 source constants must land.

## 6. Wilson Loops And Finite Holonomy

Searchable construction tag:

`V4P26-FINITE-WILSON-LOOP-HOLONOMY`.

A finite Wilson loop is:

$$
\boxed{
W_{\alpha}(\gamma)
=
\operatorname{Tr}
\prod_{e\in\gamma}
U_{\alpha}(e),
}
$$

where \(U_{\alpha}(e)\) is a finite transport operator sourced by the descent
packet.

Gauge invariance requires:

$$
\boxed{
W_{\alpha}(g\gamma)=W_{\alpha}(\gamma)
}
$$

for \(R\)-move gauge transformations.

Curvature/holonomy residue is:

$$
\boxed{
H_{\alpha}(\gamma)
=
\lambda\sum_{\triangle\subset\gamma}
\left(
C_{\alpha}(ij)+C_{\alpha}(jk)-C_{\alpha}(ik)
\right).
}
$$

The v3 Wilson-loop functionals are recovered as effective finite trace
observables.

## 7. OS/Wightman Reconstruction Gate

Searchable reconstruction tag:

`V4P26-OS-WIGHTMAN-RECONSTRUCTION-GATE`.

The finite descent family must provide:

$$
\boxed{
\begin{array}{ll}
\mathrm{OS1}:&\hbox{reflection positivity or finite positive analogue};\\
\mathrm{OS2}:&\hbox{Euclidean covariance/projective covariance};\\
\mathrm{OS3}:&\hbox{clustering or finite mixing gap};\\
\mathrm{OS4}:&\hbox{continuum/effective limit of correlators};\\
\mathrm{OS5}:&\hbox{field/operator reconstruction or operational substitute}.
\end{array}
}
$$

If these pass, the finite record law has a QFT effective face.

If they fail, Paper 26 must say whether the failure is:

$$
\boxed{
\hbox{missing source extension}
\quad\hbox{or}\quad
\hbox{failure of QFT reconstruction from finite descent.}
}
$$

## 8. QCD Confinement Gate

Searchable confinement tag:

`V4P26-QCD-CONFINEMENT-GATE`.

The v3 confinement architecture is translated into:

$$
\boxed{
E_{\mathrm{conf}}
=
({\mathcal K}_{\mathrm{conf}},
\Xi_{\mathrm{conf}},
K_{\mathrm{conf}}^{corner},
\hbox{source constants}).
}
$$

The finite confinement target is an area-law or transfer-gap statement:

$$
\boxed{
\mathbb E[W(C)]
\le
A_0\exp(-\sigma\,\mathrm{Area}(C))
}
$$

or a finite descent equivalent.

The V4 source requirement is:

$$
\boxed{
\sigma
\hbox{ and all reserve/source constants are finite index/trace/cohomology
data or licensed calibrated values.}
}
$$

## 9. Mass Gap Gate

Searchable mass-gap tag:

`V4P26-MASS-GAP-GATE`.

The finite transfer operator is:

$$
\boxed{
T_{\alpha}^{QFT}
}
$$

and the mass-gap target is:

$$
\boxed{
\lambda_0-\lambda_1\ge m_{gap}>0
}
$$

or the corresponding decay of finite connected correlators.

The source audit asks whether:

$$
\boxed{
m_{gap}
\hbox{ is produced by finite descent data}
}
$$

rather than inserted as an external constant.

## 10. Paper 26 Verdict Preview

Searchable preview tag:

`V4P26-VERDICT-PREVIEW`.

The developed audit below will end with:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{QFT1} & \mathrm{PASS} & \hbox{finite field records}\\
\mathrm{QFT2} & \mathrm{PASS}_{P25} & \hbox{locality/covariance}\\
\mathrm{QFT3} & \mathrm{PASS} & \hbox{correlators/reconstruction by FSRG}\\
\mathrm{QCD1} & \mathrm{PASS} & \hbox{gauge invariance}\\
\mathrm{QCD2} & \mathrm{PASS} & \hbox{Wilson loops/holonomy}\\
\mathrm{QCD3} & \mathrm{OPEN}_{cert} & \hbox{confinement/mass gap}
\end{array}
}
$$

Possible final classifications:

$$
\boxed{
\begin{array}{c|l}
\hbox{claim} & \hbox{allowed meaning}\\
\hline
\mathrm{QFT\text{-}KIN} &
\hbox{finite descent embeds QFT kinematics and correlator reconstruction}\\
\mathrm{QCD\text{-}GATE} &
\hbox{finite descent embeds gauge/Wilson-loop/confinement gates}\\
\mathrm{QCD\text{-}DYN} &
\hbox{finite source constants close confinement/mass-gap dynamics}\\
\mathrm{QCD\text{-}OPEN} &
\hbox{some v3 source constant remains outside finite descent}
\end{array}
}
$$

## 11. Initial Work Items Executed Below

The following sections execute the initial work items:

$$
\boxed{
\begin{array}{c|l}
\hbox{item} & \hbox{where executed}\\
\hline
1 & \hbox{V3-to-V4 dictionary and field/gauge packets, Sections 12-17}\\
2 & \hbox{Wilson loop as V4 descent trace, Sections 17-20}\\
3 & \hbox{gauge transformations as }R\hbox{-moves, Sections 18-19}\\
4 & \hbox{V3 source constants as }E\hbox{-extensions, Section 26}\\
5 & \hbox{OS/reconstruction gate, Section 16}\\
6 & \hbox{confinement/mass-gap certificate audit, Sections 23-25}
\end{array}
}
$$

The first concrete target is executed below as:

$$
\boxed{
\hbox{one finite gauge-loop packet whose Wilson loop is a V4 descent trace and
whose gauge transformations are exact refinements.}
}
$$

## 12. Paper 25 Import: The GR-Compatible Base Branch

Searchable import tag:

`V4P26-P25-GR-COMPATIBLE-BASE-BRANCH`.

Paper 26 is not allowed to place QFT on an unexamined continuum spacetime.
The base branch is the finite actual branch certified in Paper 25:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}.
}
$$

This supplies:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{same-actual covariance};\\
2.&\hbox{stable local clock/ruler/frame comparisons};\\
3.&\hbox{torsion-free GR-effective Cartan geometry};\\
4.&\hbox{complete Cartan/Wilson/corner probe algebra};\\
5.&\hbox{complete finite stress-source response dictionary};\\
6.&\hbox{same-actual Ward cohomology selection rule}.
\end{array}
}
$$

Therefore the allowed QFT/QCD extension is:

$$
\boxed{
\alpha_{GR}
\xrightarrow{E_{field}}
\alpha_{QFT}
\xrightarrow{E_{gauge}}
\alpha_{YM/QCD}
}
$$

where \(E_{field}\) and \(E_{gauge}\) are finite actual source extensions, not
hidden continuum ontology.

The important consequence of Paper 25 is:

$$
\boxed{
\hbox{if a QFT/QCD residue survives, it must appear as a finite Ward
cohomology class.}
}
$$

Thus Paper 26 will not decide QFT/QCD by aesthetic analogy.  It asks which
field/gauge Ward cohomology classes survive after same-actual quotient.

## 13. Finite Relativistic Field Packet

Searchable construction tag:

`V4P26-FINITE-RELATIVISTIC-FIELD-PACKET`.

A finite field packet over the P25 branch is:

$$
\boxed{
{\mathcal F}_{\alpha}
=
({\mathcal R}_{\alpha}^{GR},
{\mathcal V}_{\alpha},
{\mathcal O}_{\alpha}^{field},
{\mathcal J}_{\alpha},
{\mathcal D}_{\alpha},
{\mathcal W}_{\alpha},
\Theta_{\alpha},
Z_{\alpha}[J]).
}
$$

The entries are:

$$
\boxed{
\begin{array}{ll}
{\mathcal R}_{\alpha}^{GR}:&\hbox{finite GR-effective actual records from P25};\\
{\mathcal V}_{\alpha}:&\hbox{finite field-value/source-response fibers};\\
{\mathcal O}_{\alpha}^{field}:&\hbox{finite field observables};\\
{\mathcal J}_{\alpha}:&\hbox{finite source records};\\
{\mathcal D}_{\alpha}:&\hbox{finite kinetic/Dirac/wave comparison operator};\\
{\mathcal W}_{\alpha}:&\hbox{finite Wick/response/cumulant dictionary};\\
\Theta_{\alpha}:&\hbox{finite reflection, time-order, or causal order data};\\
Z_{\alpha}[J]:&\hbox{finite source generating functional}.
\end{array}
}
$$

The field packet is a V4 descent extension iff:

$$
\boxed{
{\mathcal F}_{\alpha}
\in
\mathrm{Desc}(\alpha_{QFT})
}
$$

and every presentation/gauge/relabeling change of the same field record is an
\(A^{*}R^{*}\)-move.

The finite source functional is:

$$
\boxed{
Z_{\alpha}[J]
=
\sum_{\omega\in\Omega_{\alpha}^{field}}
\mu_{\alpha}(\omega)
\exp\left(
A_{\alpha}^{field}(\omega)
+\langle J,O(\omega)\rangle_{\alpha}
\right).
}
$$

All sets are finite.  The continuum field is not primitive.  It is the
effective reconstruction of this finite projective source-response family.

## 14. Einstein Audit For Relativistic QFT Kinematics

Searchable audit tag:

`V4P26-EINSTEIN-QFT-KINEMATIC-AUDIT`.

Einstein's question is:

$$
\boxed{
\hbox{what must finite actual records satisfy for relativistic field
observables to be meaningful on the GR branch?}
}
$$

The answer is a finite field equivalence principle:

$$
\boxed{
X\sim_{\alpha}^{same}
\Rightarrow
\langle O_1\cdots O_n\rangle_X
=
\langle O_1\cdots O_n\rangle_Y
}
$$

for every licensed finite field battery.

The QFT kinematic gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{FQ1}:&\hbox{field observables descend to same-actual quotient};\\
\mathrm{FQ2}:&\hbox{source insertions are finite actual records or typed
extensions};\\
\mathrm{FQ3}:&\hbox{locality is defined by the P25 finite causal/collar
structure};\\
\mathrm{FQ4}:&\hbox{covariance is inherited from FAC and SLC};\\
\mathrm{FQ5}:&\hbox{stress-response couples through the P25 RSC dictionary};\\
\mathrm{FQ6}:&\hbox{cofinal refinement changes correlators only by }R\hbox{-moves
or typed }E\hbox{-extensions}.
\end{array}
}
$$

The obstruction table is:

$$
\boxed{
\begin{array}{c|l}
\hbox{failed gate} & \hbox{meaning}\\
\hline
\mathrm{FQ1} & \hbox{field is presentation data, not actual observable}\\
\mathrm{FQ2} & \hbox{unlicensed field source}\\
\mathrm{FQ3} & \hbox{no relativistic locality/collar interpretation}\\
\mathrm{FQ4} & \hbox{breaks P25 GR covariance branch}\\
\mathrm{FQ5} & \hbox{missing stress/source coupling}\\
\mathrm{FQ6} & \hbox{no cofinal field reconstruction}
\end{array}
}
$$

On the active P25 base branch, FAC/SLC/RSC give FQ1, FQ3, FQ4, and FQ5.  FQ2
and FQ6 hold precisely when field insertions are declared as finite source
extensions and their projective tails converge or are typed.

Therefore:

$$
\boxed{
\mathrm{P25\ GR\ branch}
+\mathrm{finite\ field\ source\ extension}
\Longrightarrow
\mathrm{QFT\text{-}KIN\text{-}PASS}.
}
$$

## 15. Feynman Audit For Field Correlators

Searchable audit tag:

`V4P26-FEYNMAN-FIELD-CORRELATOR-WARD-AUDIT`.

Feynman's question is:

$$
\boxed{
\hbox{do all finite ways of computing the same field correlator agree?}
}
$$

Let \(\Phi\) be a same-actual move of the finite field packet:

$$
\boxed{
\Phi
\in
\{\hbox{field relabeling, source displacement inside same record,
local frame change, refinement, Wick rebracketing, time-order route}\}.
}
$$

The field Ward defect is:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}^{field}
=
\delta_{\Phi}Z_{\alpha}[J].
}
$$

The finite field packet is QFT-admissible iff:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}
\in
\mathrm{im}\,D_{\alpha}^{field}
\oplus
{\mathcal A}_{typed,\alpha}^{field}
}
$$

for every same-actual field move.

The non-cliche Feynman content is:

$$
\boxed{
\hbox{the field theory is the quotient of finite source-response calculus by
same-actual Ward identities.}
}
$$

If all typed field anomalies vanish cofinally:

$$
\boxed{
{\mathcal A}_{typed,\alpha_n}^{field}\to0,
}
$$

then the finite projective family has a QFT effective face.  If not, the
surviving field Ward cohomology is the ISP correction to ordinary QFT.

## 16. OS/Wightman Reconstruction As A V4 Gate

Searchable theorem tag:

`V4P26-FINITE-OS-WIGHTMAN-DESCENT-THEOREM`.

The V3 reconstruction results are imported into V4 only in finite descent
form.  A finite OS/Wightman packet is:

$$
\boxed{
{\mathcal O}{\mathcal S}_{\alpha}
=
({\mathcal A}_{+,\alpha},
\vartheta_{\alpha},
S_{\alpha}^{(n)},
\mu_{\alpha},
{\mathcal R}_{\alpha\to\beta}).
}
$$

where:

$$
\boxed{
\begin{array}{ll}
{\mathcal A}_{+,\alpha}:&\hbox{positive-time finite observable algebra};\\
\vartheta_{\alpha}:&\hbox{finite reflection};\\
S_{\alpha}^{(n)}:&\hbox{finite Schwinger/correlation functions};\\
\mu_{\alpha}:&\hbox{finite positive source law};\\
{\mathcal R}_{\alpha\to\beta}:&\hbox{projective refinement maps}.
\end{array}
}
$$

The gate conditions are:

$$
\boxed{
\begin{array}{ll}
\mathrm{OSD1}:&\hbox{finite positivity};\\
\mathrm{OSD2}:&\hbox{finite reflection positivity};\\
\mathrm{OSD3}:&\hbox{finite Euclidean/projective covariance};\\
\mathrm{OSD4}:&\hbox{locality/collar compatibility with P25 SLC};\\
\mathrm{OSD5}:&\hbox{cofinal correlator convergence or typed floor};\\
\mathrm{OSD6}:&\hbox{same-actual Ward defects vanish or are typed}.
\end{array}
}
$$

The theorem is:

$$
\boxed{
\mathrm{OSD1}\text{-}\mathrm{OSD6}
\Longrightarrow
\mathrm{QFT\text{-}RECON\text{-}PASS}.
}
$$

Proof.  OSD1 and OSD2 give the finite positive reconstruction form.  OSD3 and
OSD4 attach it to the P25 GR-compatible finite coincidence structure.  OSD5
supplies the cofinal effective correlators.  OSD6 identifies calculation-route
ambiguities as Ward identities or typed anomalies.  Thus the reconstruction
is a finite descent theorem, not a primitive continuum assumption. `square`

For the active V4 corpus, the status is:

$$
\boxed{
\mathrm{QFT\text{-}RECON}
=
\mathrm{PASS}_{FSRG}
}
$$

because Sections 30-33 derive the finite OS/reflection-positive projective
packet from finite source-response gluing rather than importing it as a
continuum axiom.

## 17. Finite Gauge/Yang-Mills Descent Packet

Searchable construction tag:

`V4P26-FINITE-GAUGE-YANG-MILLS-DESCENT-PACKET`.

A finite gauge packet over the P25 branch is:

$$
\boxed{
{\mathcal G}_{\alpha}^{YM}
=
(V_{\alpha},E_{\alpha},G_{\alpha},
U_{\alpha},P_{\alpha},W_{\alpha},
{\mathcal J}_{\alpha}^{gauge},
Z_{\alpha}^{gauge}[J]).
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
V_{\alpha},E_{\alpha}:&\hbox{finite vertices and edges from the descent context};\\
G_{\alpha}:&\hbox{finite compact/gauge-group approximation or finite
representation battery};\\
U_{\alpha}(e):&\hbox{finite parallel transport on edges};\\
P_{\alpha}(p):&\hbox{finite plaquette/curvature word};\\
W_{\alpha}(\gamma):&\hbox{finite Wilson loop trace};\\
{\mathcal J}_{\alpha}^{gauge}:&\hbox{finite gauge/source records};\\
Z_{\alpha}^{gauge}[J]:&\hbox{finite gauge-invariant source functional}.
\end{array}
}
$$

Gauge transformation at vertices is:

$$
\boxed{
U_e
\mapsto
h_{s(e)}U_eh_{t(e)}^{-1}.
}
$$

In V4 this is an \(R\)-move:

$$
\boxed{
h\in{\mathcal G}_{\alpha}
\Rightarrow
\alpha\le_{\mathrm{ref}}h\alpha.
}
$$

Therefore:

$$
\boxed{
\Delta_h Q=0,
\qquad
\Delta_h C=0,
\qquad
W_{\alpha}(h\gamma)=W_{\alpha}(\gamma).
}
$$

The finite Yang-Mills action is not primitive ontology.  It is the effective
source score of the finite gauge packet:

$$
\boxed{
A_{\alpha}^{YM}(U)
=
\sum_{p\in P_{\alpha}}
a_p\,\chi_p(P_{\alpha}(p))
+A_{\alpha}^{ct}(U)
}
$$

where the coefficients and counterterms must be finite descent data, licensed
calibrated constants, or typed source extensions.

## 18. Einstein Gauge Audit

Searchable audit tag:

`V4P26-EINSTEIN-GAUGE-AS-REFINEMENT-AUDIT`.

Einstein's gauge question is:

$$
\boxed{
\hbox{is gauge a change of finite presentation, or does it change actual
content?}
}
$$

For the V4 gauge packet, the audit is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{test} & \hbox{failure}\\
\hline
\mathrm{GA1} &
h\hbox{ preserves Wilson traces} &
\hbox{gauge not refinement}\\
\mathrm{GA2} &
h\hbox{ preserves source functional }Z[J] &
\hbox{gauge anomaly}\\
\mathrm{GA3} &
h\hbox{ acts inside }A^{*}R^{*} &
\hbox{gauge changes actual content}\\
\mathrm{GA4} &
\hbox{gauge fixing has Faddeev-Popov/quotient finite record} &
\hbox{hidden continuum gauge fixing}\\
\mathrm{GA5} &
\hbox{refinements commute with gauge quotient} &
\hbox{projective gauge anomaly}
\end{array}
}
$$

For finite Wilson traces:

$$
\boxed{
\operatorname{Tr}
\prod_{e\in\gamma}
h_{s(e)}U_eh_{t(e)}^{-1}
=
\operatorname{Tr}
\prod_{e\in\gamma}U_e.
}
$$

Thus GA1 passes by finite trace cyclicity.  GA2-GA5 pass when the gauge source
functional is built from class functions, quotient records, and projective
gauge-compatible refinements.

Therefore:

$$
\boxed{
\mathrm{finite\ gauge\ packet}
\Longrightarrow
\mathrm{QCD1\ PASS}
}
$$

provided gauge transformations are declared as same-actual \(R\)-moves.

## 19. Feynman Gauge/Wilson Ward Audit

Searchable audit tag:

`V4P26-FEYNMAN-GAUGE-WILSON-WARD-AUDIT`.

Feynman's gauge question is:

$$
\boxed{
\hbox{do all gauge-related calculations of the same Wilson observable agree?}
}
$$

Define the finite Wilson generating functional:

$$
\boxed{
Z_{\alpha}^{W}[J]
=
\sum_{U\in{\mathcal U}_{\alpha}}
\mu_{\alpha}(U)
\exp\left(
A_{\alpha}^{YM}(U)
+\sum_{\gamma}J_{\gamma}W_{\alpha}(\gamma;U)
\right).
}
$$

For a gauge move \(h\), the Ward defect is:

$$
\boxed{
{\mathfrak W}_{h,\alpha}^{gauge}
=
\delta_h Z_{\alpha}^{W}[J].
}
$$

If the measure, score, and Wilson batteries are class functions:

$$
\boxed{
\mu_{\alpha}(hU)=\mu_{\alpha}(U),
\quad
A_{\alpha}^{YM}(hU)=A_{\alpha}^{YM}(U),
\quad
W_{\alpha}(\gamma;hU)=W_{\alpha}(\gamma;U),
}
$$

then:

$$
\boxed{
{\mathfrak W}_{h,\alpha}^{gauge}=0.
}
$$

If a defect survives:

$$
\boxed{
{\mathfrak W}_{h,*}^{gauge}\ne0
\Longrightarrow
\hbox{finite gauge anomaly or missing quotient/source record.}
}
$$

Thus:

$$
\boxed{
\mathrm{QCD1}
=
\mathrm{PASS}_{Ward}
}
$$

on every finite gauge packet satisfying class-function and quotient-record
conditions.

## 20. Wilson Loop And Yang-Mills Observables

Searchable result tag:

`V4P26-WILSON-YANG-MILLS-OBSERVABLES-PASS`.

The finite Wilson loop:

$$
\boxed{
W_{\alpha}(\gamma)
=
\operatorname{Tr}\prod_{e\in\gamma}U_{\alpha}(e)
}
$$

is a V4 descent observable because:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{it is finite at every }\alpha;\\
2.&\hbox{it is invariant under gauge }R\hbox{-moves};\\
3.&\hbox{it is represented in the P25 Cartan/Wilson probe dictionary};\\
4.&\hbox{its commutator/ordering residues are Wilson-word residues};\\
5.&\hbox{its cofinal behavior is controlled by projective refinement or typed}.
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{QCD2}
=
\mathrm{PASS}.
}
$$

This does not yet prove an area law.  It proves that the Wilson loop
observable itself is a legitimate V4 finite descent trace.

The finite Yang-Mills observable algebra is:

$$
\boxed{
{\mathfrak W}_{\alpha}^{YM}
=
\langle
W_{\alpha}(\gamma),
\chi_R(P_{\alpha}(p)),
J\hbox{-derivatives},
\hbox{source/stress insertions}
\rangle
/
{\mathcal I}_{Ward}.
}
$$

This is the gauge-field analogue of Paper 25's completed Wilson algebra.  It
is finite at every \(\alpha\), and its same-actual Ward ideal is the place
where gauge anomalies, missing source channels, or confinement certificates
must appear.

## 21. Matter, Fermions, And Spinor Packets

Searchable construction tag:

`V4P26-FINITE-MATTER-FERMION-PACKET`.

A finite matter packet is:

$$
\boxed{
{\mathcal M}_{\alpha}
=
({\mathcal S}_{\alpha}^{spin},
{\mathcal D}_{\alpha}^{Dirac},
\psi_{\alpha},\bar\psi_{\alpha},
U_{\alpha},
J_{\alpha}^{m},
Z_{\alpha}^{m}[\eta,\bar\eta,J]).
}
$$

The Dirac comparison operator is finite:

$$
\boxed{
{\mathcal D}_{\alpha}^{Dirac}
:
{\mathcal S}_{\alpha}^{spin}
\to
{\mathcal S}_{\alpha}^{spin}.
}
$$

Its covariance condition is:

$$
\boxed{
{\mathcal D}_{\alpha}^{Dirac}(h\psi)
=
h{\mathcal D}_{\alpha}^{Dirac}\psi
}
$$

up to same-actual \(R\)-moves and typed anomalies.

Matter is not a hidden continuum field.  It is a finite source extension:

$$
\boxed{
E_{matter}:
\alpha_{GR/YM}
\to
\alpha_{GR/YM/matter}.
}
$$

The source/stress response lies in the P25 RSC dictionary:

$$
\boxed{
T_{\mu\nu}^{matter}
\in
{\mathcal S}_{stress,\alpha}.
}
$$

Therefore matter coupling is V4-admissible iff:

$$
\boxed{
\delta_{\Phi}Z_{\alpha}^{m}
\in
\mathrm{im}\,D_{\alpha}^{matter}
\oplus
{\mathcal A}_{typed,\alpha}^{matter}
}
$$

for gauge, Lorentz, spin-frame, and same-actual refinement moves.

## 22. Renormalization As Descent Normal Form

Searchable theorem tag:

`V4P26-RENORMALIZATION-AS-DESCENT-NORMAL-FORM`.

In V4, renormalization is not a hidden continuum process.  A finite RG move is
a corpus transformation:

$$
\boxed{
\alpha_a\to\alpha_b.
}
$$

By Paper 24 normal form:

$$
\boxed{
\alpha_a\to\alpha_b
\Rightarrow
A^{*}R^{*}K^{*}E^{*}.
}
$$

Interpretation:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{normal-form part} & \hbox{RG meaning} & \hbox{physical effect}\\
\hline
A & \hbox{analysis/bookkeeping} & \Delta=0\\
R & \hbox{field redefinition, exact counterterm, quotient refinement} & \Delta=0\\
K & \hbox{corner/anomaly residue} & \hbox{typed curvature/boundary term}\\
E & \hbox{new relevant/marginal source content} & \hbox{physical coupling/source}
\end{array}
}
$$

Thus a counterterm is legitimate in V4 only if it is:

$$
\boxed{
\hbox{an }R\hbox{-move}
\quad\hbox{or}\quad
\hbox{a printed }K/E\hbox{ source extension.}
}
$$

The theorem is:

$$
\boxed{
\hbox{finite RG compatibility}
\Longleftrightarrow
\hbox{RG move has }A^{*}R^{*}K^{*}E^{*}\hbox{ normal form.}
}
$$

If a renormalization step cannot be classified, it triggers the P24 normal
form falsifier and becomes a new primitive, not an accepted QFT derivation.

## 23. QCD Confinement And Mass-Gap Certificate Gate

Searchable gate tag:

`V4P26-QCD-CONFINEMENT-MASS-GAP-CERTIFICATE-GATE`.

The nonperturbative QCD target is stronger than finite gauge compatibility.
It requires a certificate packet:

$$
\boxed{
{\mathcal C}_{\alpha}^{QCD}
=
({\mathcal G}_{\alpha}^{YM},
T_{\alpha}^{gauge},
W_{\alpha},
\sigma_{\alpha},
m_{\alpha},
{\mathcal B}_{\alpha}^{cert},
{\mathcal R}_{\alpha\to\beta}).
}
$$

where:

$$
\boxed{
\begin{array}{ll}
T_{\alpha}^{gauge}:&\hbox{finite transfer operator};\\
\sigma_{\alpha}:&\hbox{finite string-tension/area-rate candidate};\\
m_{\alpha}:&\hbox{finite mass-gap candidate};\\
{\mathcal B}_{\alpha}^{cert}:&\hbox{finite certificate battery};\\
{\mathcal R}_{\alpha\to\beta}:&\hbox{projective refinement}.
\end{array}
}
$$

The certificate gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{QC1}:&\hbox{finite gauge packet passes QCD1-QCD2};\\
\mathrm{QC2}:&\hbox{reflection positivity / OS positivity on the certificate
battery};\\
\mathrm{QC3}:&\hbox{finite transfer gap }m_{\alpha}\ge m_0>0\hbox{ cofinally};\\
\mathrm{QC4}:&\hbox{Wilson-loop area law or equivalent confinement witness};\\
\mathrm{QC5}:&\hbox{all constants are finite index/trace/cohomology/source
data};\\
\mathrm{QC6}:&\hbox{projective refinement preserves the certificate or gives
summable typed error};\\
\mathrm{QC7}:&\hbox{no external continuum Yang-Mills measure, mass gap, or
area law is imported.}
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{QC1}\text{-}\mathrm{QC7}
\Longrightarrow
\mathrm{QCD\text{-}DYN\text{-}PASS}.
}
$$

The current V4 status is:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{OPEN}_{cert}
}
$$

unless the V3 source/certificate campaigns are imported as a closed finite
certificate packet satisfying QC1-QC7.

This is not a retreat.  It is the exact Barandes-aligned statement:

$$
\boxed{
\hbox{finite gauge/Yang-Mills observables embed now; confinement/mass gap
requires a finite certificate.}
}
$$

## 24. Einstein Audit Of The QCD Certificate

Searchable audit tag:

`V4P26-EINSTEIN-QCD-CERTIFICATE-AUDIT`.

Einstein's question is:

$$
\boxed{
\hbox{does the finite actual law force confinement/mass-gap structure from
gauge-invariant coincidence data?}
}
$$

The certificate must be invariant under:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{gauge presentation};\\
2.&\hbox{finite refinement};\\
3.&\hbox{loop reparametrization};\\
4.&\hbox{local frame/collar changes};\\
5.&\hbox{source-battery enlargement by exact pairs}.
\end{array}
}
$$

The Einstein certificate obstruction is:

$$
\boxed{
{\mathcal A}_{QCD}^{Ein}
=
\hbox{certificate value changes under a same-actual }A^{*}R^{*}\hbox{ move}.
}
$$

Thus:

$$
\boxed{
{\mathcal A}_{QCD}^{Ein}=0
\Longleftrightarrow
\hbox{confinement/mass-gap certificate is actual, not gauge/presentation
data.}
}
$$

If the obstruction is nonzero, the certificate is not a physical QCD result.
It is a gauge or refinement artifact.

## 25. Feynman Audit Of The QCD Certificate

Searchable audit tag:

`V4P26-FEYNMAN-QCD-CERTIFICATE-WARD-AUDIT`.

Feynman's question is:

$$
\boxed{
\hbox{does the finite sum over gauge alternatives produce a stable
confinement/mass-gap residue?}
}
$$

Define:

$$
\boxed{
Z_{\alpha}^{QCD}[J]
=
\sum_{U,\psi,\bar\psi}
\mu_{\alpha}(U,\psi,\bar\psi)
\exp(A_{\alpha}^{QCD}+J\cdot W+\bar\eta\psi+\bar\psi\eta).
}
$$

The QCD certificate Ward defect is:

$$
\boxed{
{\mathfrak W}_{QCD,\alpha}
=
\delta_{\Phi_{cert}}Z_{\alpha}^{QCD}.
}
$$

The certificate passes iff:

$$
\boxed{
{\mathfrak W}_{QCD,\alpha_n}\to0
}
$$

and the certificate residue survives:

$$
\boxed{
\sigma_{\alpha_n}\to\sigma>0
\quad\hbox{or}\quad
m_{\alpha_n}\to m>0.
}
$$

If:

$$
\boxed{
{\mathfrak W}_{QCD,*}\ne0
}
$$

then the surviving defect is not discarded.  It must be typed as:

$$
\boxed{
\begin{array}{c|l}
\hbox{defect} & \hbox{meaning}\\
\hline
{\mathcal A}_{gauge} & \hbox{gauge anomaly}\\
{\mathcal A}_{RP} & \hbox{reflection positivity failure}\\
{\mathcal A}_{tail} & \hbox{uncontrolled cofinal tail}\\
{\mathcal A}_{source} & \hbox{missing actual source constant}\\
{\mathcal A}_{area} & \hbox{area-law witness not sourced}\\
{\mathcal A}_{gap} & \hbox{mass-gap witness not sourced}
\end{array}
}
$$

This is the real Feynman criterion: the certificate is accepted only when the
finite alternative calculus itself leaves a positive, route-independent
residue.

## 26. V3 Source Campaigns As V4 Descent Extensions

Searchable import tag:

`V4P26-V3-SOURCE-CAMPAIGNS-AS-V4-EXTENSIONS`.

The V3 source campaigns are not imported as conclusions.  They are imported
as candidate \(E\)-extensions:

$$
\boxed{
V3P19\text{-}P30
\longmapsto
E_{source}^{cand}.
}
$$

The V4 classification is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{V3 object} & \hbox{V4 status} & \hbox{meaning}\\
\hline
\hbox{finite source constant} & E_{source} & \hbox{physical source extension}\\
\hbox{certificate inequality} & {\mathcal B}^{cert} & \hbox{finite audit battery}\\
\hbox{failed route} & {\mathcal A}_{typed} & \hbox{typed obstruction}\\
\hbox{closed finite dual certificate} & E_{cert} & \hbox{admissible V4 certificate input}\\
\hbox{missing scalar table} & \mathrm{OPEN}_{value} & \hbox{not a QCD proof}
\end{array}
}
$$

Therefore:

$$
\boxed{
\hbox{V3 source campaigns are V4-admissible provenance, but not automatically
QCD-DYN closure.}
}
$$

The positive import is:

$$
\boxed{
\hbox{no V3 source campaign reopens the P24/P25 value-source problem if it is
classified as }A,R,K,\hbox{ or }E.
}
$$

The negative discipline is:

$$
\boxed{
\hbox{a V3 route that did not close remains open in V4 unless its missing
finite certificate is supplied.}
}
$$

## 27. Developed Gate Audit

Searchable audit tag:

`V4P26-DEVELOPED-QFT-QCD-GATE-AUDIT`.

Run the target gates from Section 1.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{QFT1} &
\mathrm{PASS} &
\hbox{field records are finite source-response extensions}\\
\mathrm{QFT2} &
\mathrm{PASS}_{P25} &
\hbox{locality/covariance inherit FAC+SLC+RSC}_{GR}\\
\mathrm{QFT3} &
\mathrm{PASS} &
\hbox{FSRG derives OSD1-OSD6 and Ward route closure}\\
\mathrm{QCD1} &
\mathrm{PASS} &
\hbox{gauge transformations are }R\hbox{-moves}\\
\mathrm{QCD2} &
\mathrm{PASS} &
\hbox{Wilson loops are finite descent traces}\\
\mathrm{QCD3} &
\mathrm{OPEN}_{cert} &
\hbox{confinement/mass gap require QC1-QC7 certificate}
\end{array}
}
$$

This is the central result of Paper 26.

It says:

$$
\boxed{
\mathrm{V4\ ISP}
\hbox{ is compatible with relativistic QFT and finite nonabelian gauge/QCD
kinematics on the P25 GR branch.}
}
$$

It does not say:

$$
\boxed{
\hbox{V4 has unconditionally proved }4D\hbox{ QCD confinement or mass gap.}
}
$$

## 28. Final Theorem: V4 QFT/QCD Descent Compatibility

Searchable theorem tag:

`V4P26-QFT-QCD-DESCENT-COMPATIBILITY-THEOREM`.

Assume:

$$
\boxed{
\begin{array}{ll}
1.&{\mathfrak A}^{act}_{P24}\models\mathrm{FAC+SLC+RSC}_{GR};\\
2.&{\mathcal F}_{\alpha}\hbox{ is a finite field descent packet};\\
3.&{\mathcal G}_{\alpha}^{YM}\hbox{ is a finite gauge/Yang-Mills descent
packet};\\
4.&\hbox{gauge transformations are }R\hbox{-moves};\\
5.&\hbox{Wilson and source functionals are finite same-actual Ward quotients};\\
6.&\hbox{FSRG holds, hence OSD1-OSD6 and QFT Ward route closure hold};\\
7.&\hbox{QC1-QC7 hold if confinement/mass-gap dynamics is claimed}.
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{V4}
\Longrightarrow
\mathrm{effective\ relativistic\ QFT/YM}
}
$$

and, if QC1-QC7 also hold:

$$
\boxed{
\mathrm{V4}
\Longrightarrow
\mathrm{QCD\text{-}DYN\text{-}PASS}.
}
$$

Proof.  Paper 25 supplies the GR-effective finite base.  Sections 13-16
construct finite field records, source functionals, and reconstruction gates.
Sections 17-20 construct finite gauge packets and Wilson observables as
same-actual descent traces.  Section 22 shows RG/counterterm flow has
\(A^{*}R^{*}K^{*}E^{*}\) normal form.  Sections 23-25 isolate the additional
confinement/mass-gap certificate burden.  Therefore QFT/YM compatibility
closes at the finite descent level, while QCD confinement/mass-gap closes
only when the certificate gates close. `square`

## 29. Final Status Of Paper 26

Searchable final tag:

`V4P26-FINAL-QFT-QCD-STATUS`.

The final status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{REL\text{-}QFT\text{-}KIN} &
\mathrm{PASS} &
\hbox{finite source-response gluing gives OSD reconstruction}\\
\mathrm{YM\text{-}GAUGE} &
\mathrm{PASS} &
\hbox{gauge is finite refinement}\\
\mathrm{YM\text{-}WILSON} &
\mathrm{PASS} &
\hbox{Wilson loops are finite descent traces}\\
\mathrm{RG\text{-}DESCENT} &
\mathrm{PASS} &
\hbox{renormalization classified by }A^{*}R^{*}K^{*}E^{*}\\
\mathrm{QCD\text{-}DYN} &
\mathrm{OPEN}_{cert} &
\hbox{requires finite confinement/mass-gap certificate}\\
\mathrm{BARANDES} &
\mathrm{PASS} &
\hbox{no primitive continuum field/path integral imported}
\end{array}
}
$$

Thus Paper 26 closes the following:

$$
\boxed{
\hbox{V4 ISP is compatible with relativistic QFT/Yang-Mills as finite descent
extensions of the P25 GR branch.}
}
$$

It leaves open:

$$
\boxed{
\hbox{unconditional }4D\hbox{ QCD confinement and mass gap, unless a finite
QC1-QC7 certificate is supplied.}
}
$$

After the REL-QFT-KIN closure audit below, the remaining task is not another
compatibility paper.  It is a certificate paper:

$$
\boxed{
\hbox{print or import a finite }QC1\text{-}QC7\hbox{ QCD certificate packet.}
}
$$

## 30. Finite Source-Response Gluing Law

Searchable law tag:

`V4P26-FINITE-SOURCE-RESPONSE-GLUING-LAW`.

Section 29 identified the last \(\mathrm{REL\text{-}QFT\text{-}KIN}\)
burden as the finite OS/Wightman descent gates.  The next move is to replace
those gates by a finite actual-record law.

The law is not continuum reflection positivity.  It is finite
source-response gluing:

$$
\boxed{
\mathrm{FSRG}
=
\hbox{Finite Source-Response Gluing}.
}
$$

At each finite resolution \(\alpha\), an actual field packet admits:

$$
\boxed{
\Omega_{\alpha}^{field}
=
\bigsqcup_{b\in B_{\alpha}}
\Omega_{\alpha,+}(b)
\times
\Omega_{\alpha,-}(b),
}
$$

where \(b\) is a finite cut/boundary record and \(+\), \(-\) are the two
finite halves of the record slab.  There is a finite reflection:

$$
\boxed{
\vartheta_{\alpha}:
\Omega_{\alpha,+}(b)
\to
\Omega_{\alpha,-}(b).
}
$$

The gluing law says the same actual doubled slab has positive square form:

$$
\boxed{
\mu_{\alpha}(x,\vartheta y,b)
=
w_{\alpha}(b)\,
a_{\alpha}(x|b)\,
a_{\alpha}(y|b)
}
$$

with:

$$
\boxed{
w_{\alpha}(b)\ge0,
\qquad
a_{\alpha}(x|b)\ge0.
}
$$

For a finite observable \(F\) supported on the \(+\)-half:

$$
\boxed{
\langle \vartheta F\,F\rangle_{\alpha}
=
\sum_{b\in B_{\alpha}}
w_{\alpha}(b)
\left|
\sum_{x\in\Omega_{\alpha,+}(b)}
a_{\alpha}(x|b)F(x)
\right|^2
\ge0.
}
$$

This is the finite record reason for reflection positivity.

The FSRG gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{FSRG1}:&\Omega_{\alpha}^{field}\hbox{ is finite actual record data};\\
\mathrm{FSRG2}:&\vartheta_{\alpha}\hbox{ is a finite same-actual reflection
of a cut slab};\\
\mathrm{FSRG3}:&\mu_{\alpha}\hbox{ glues through positive boundary weights};\\
\mathrm{FSRG4}:&\hbox{source insertions on the positive side reflect to the
negative side};\\
\mathrm{FSRG5}:&\hbox{P25 local collars supply the finite locality structure};\\
\mathrm{FSRG6}:&\hbox{cofinal refinements preserve the gluing form or print a
typed residue}.
\end{array}
}
$$

This is Barandes-aligned because every object is finite: finite slabs, finite
cuts, finite source records, finite reflection maps, finite positive weights,
and finite projective refinements.

## 31. Einstein Way: QFT From Finite Coincidence And Gluing

Searchable theorem tag:

`V4P26-EINSTEIN-FINITE-QFT-KINEMATIC-CLOSURE`.

Einstein's question is:

$$
\boxed{
\hbox{what must finite actual records satisfy so that a field is an objective
source-response structure?}
}
$$

The answer is:

$$
\boxed{
\hbox{same actual source/readout arrangement}
\Rightarrow
\hbox{same finite correlation response.}
}
$$

This is the field analogue of FAC.  A field is not primitive \(\phi(x)\).  A
field is the stable coordinate system on finite source-response records.

### 31.1 Einstein Derivation Of OSD1-OSD6

Assume the P25 base branch:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}.
}
$$

Assume a finite field packet satisfies FSRG1-FSRG6.  Then:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{OSD gate} & \hbox{source} & \hbox{reason}\\
\hline
\mathrm{OSD1} & \mathrm{FSRG1,FSRG3} &
\hbox{finite positive weights}\\
\mathrm{OSD2} & \mathrm{FSRG2,FSRG3} &
\hbox{reflection pairing is a positive square}\\
\mathrm{OSD3} & \mathrm{P25\ FAC+SLC} &
\hbox{covariance under same-actual frame/refinement moves}\\
\mathrm{OSD4} & \mathrm{P25\ SLC+FSRG5} &
\hbox{locality/collar structure is finite and stable}\\
\mathrm{OSD5} & \mathrm{FSRG6+P24\ normal\ form} &
\hbox{cofinal refinements are }A^{*}R^{*}\hbox{ or typed }K/E\\
\mathrm{OSD6} & \mathrm{P25\ Ward\ rule+FSRG4} &
\hbox{same-actual route moves are Ward identities}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{P25\ GR\ branch}
+
\mathrm{FSRG}
\Longrightarrow
\mathrm{OSD1}\text{-}\mathrm{OSD6}.
}
$$

### 31.2 Einstein QFT Kinematic Theorem

The theorem is:

$$
\boxed{
\mathrm{P25\ GR\ branch}
+
\mathrm{finite\ source\text{-}response\ gluing}
\Longrightarrow
\mathrm{REL\text{-}QFT\text{-}KIN}.
}
$$

Proof.  P25 supplies finite actual covariance, stable local coincidence, and
record/source completeness on the GR branch.  FSRG supplies finite
source-response cuts and positive reflected gluing.  The OSD table above
derives positivity, reflection positivity, covariance, locality, cofinal
stability, and Ward route-independence without importing continuum QFT as
primitive ontology.  Thus the field algebra is reconstructed as the effective
finite source-response algebra. `square`

Einstein's result is not:

$$
\boxed{
\hbox{fields are fundamental continuum objects.}
}
$$

It is:

$$
\boxed{
\hbox{fields are stable coordinates on finite actual source-response
coincidences.}
}
$$

## 32. Feynman Way: Complete Source-Route Ward Calculus

Searchable theorem tag:

`V4P26-FEYNMAN-SOURCE-ROUTE-WARD-CLOSURE`.

Feynman's question is:

$$
\boxed{
\hbox{do all finite calculation routes for the same source response agree?}
}
$$

Start with the finite generating functional:

$$
\boxed{
Z_{\alpha}[J]
=
\sum_{\omega\in\Omega_{\alpha}^{field}}
\mu_{\alpha}(\omega)
\exp\left(
A_{\alpha}^{field}(\omega)
+\langle J,O(\omega)\rangle_{\alpha}
\right).
}
$$

The source routes are:

$$
\boxed{
\begin{array}{c|l}
\hbox{route} & \hbox{move}\\
\hline
\Phi_{src} & \hbox{differentiate before/after same-actual refinement}\\
\Phi_{ref} & \hbox{reflect then multiply, or multiply then reflect}\\
\Phi_{ord} & \hbox{finite time/collar ordering route}\\
\Phi_{frm} & \hbox{local frame route inherited from P25 SLC}\\
\Phi_{Wick} & \hbox{response expansion/rebracketing route}\\
\Phi_{proj} & \hbox{project to coarser/finer finite source battery}
\end{array}
}
$$

For every such route define:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}^{QFT}
=
\delta_{\Phi}Z_{\alpha}[J].
}
$$

The finite route calculus closes iff:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}
=0
\quad
\hbox{or}
\quad
{\mathfrak W}_{\Phi,\alpha}
\in
{\mathcal A}_{typed,\alpha}^{field}.
}
$$

### 32.1 Ward Cancellation Under FSRG

Under FSRG, each source-route defect is either an exact reindexing of a finite
sum, a positive reflection-square identity, or an \(A^{*}R^{*}\) refinement.

Thus:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{route} & \hbox{defect} & \hbox{reason}\\
\hline
\Phi_{src} & 0 & \hbox{finite differentiation of a finite sum}\\
\Phi_{ref} & 0 & \hbox{reflection gluing square}\\
\Phi_{ord} & 0 & \hbox{finite collar order is same-actual}\\
\Phi_{frm} & 0 & \hbox{P25 frame moves are }R\hbox{-moves}\\
\Phi_{Wick} & 0 & \hbox{finite response expansion is rebracketing}\\
\Phi_{proj} & 0 & \hbox{P24 refinement is }A^{*}R^{*}
\end{array}
}
$$

If a route defect persists, P24 normal form forces it to be \(K\) or \(E\):

$$
\boxed{
{\mathfrak W}_{\Phi,*}^{QFT}\ne0
\Longrightarrow
{\mathfrak W}_{\Phi,*}^{QFT}
\in
K^{field}\oplus E^{field}.
}
$$

That means a typed QFT correction:

$$
\boxed{
\begin{array}{c|l}
\hbox{surviving class} & \hbox{meaning}\\
\hline
K^{field} & \hbox{boundary/corner/anomaly field residue}\\
E^{field} & \hbox{new source or interaction content}
\end{array}
}
$$

For the active finite source-response gluing packet, no untyped \(K^{field}\)
or \(E^{field}\) residue is printed.  Therefore:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha_n}^{QFT}\to0
}
$$

for all source routes \(\Phi\).

### 32.2 Feynman QFT Kinematic Theorem

The theorem is:

$$
\boxed{
\mathrm{FSRG}
\Longrightarrow
\mathrm{same\text{-}actual\ source\ route\ Ward\ closure}.
}
$$

Therefore:

$$
\boxed{
\mathrm{FSRG}
\Longrightarrow
\mathrm{REL\text{-}QFT\text{-}KIN}.
}
$$

Proof.  \(Z_{\alpha}[J]\) is a finite sum over actual field completions.  Each
allowed route move is either a reindexing of that finite sum, a reflection
gluing identity, a P24 exact refinement, or a P25 same-actual frame/collar
move.  The first three give exact finite cancellation; the fourth is an
\(R\)-move on the GR-compatible branch.  Any nonzero residue must be a printed
\(K/E\) extension.  Since no such untyped field extension appears in the
active source-response packet, the source-route Ward cohomology vanishes
cofinally. `square`

This is the real Feynman result: QFT kinematics is the quotient of finite
source-response calculations by same-actual Ward identities.

## 33. REL-QFT-KIN Closure Verdict

Searchable verdict tag:

`V4P26-REL-QFT-KIN-CLOSURE-VERDICT`.

The remaining conditional QFT gate is now evaluated.

Einstein side:

$$
\boxed{
\mathrm{P25\ GR\ branch}
+
\mathrm{FSRG}
\Longrightarrow
\mathrm{OSD1}\text{-}\mathrm{OSD6}.
}
$$

Feynman side:

$$
\boxed{
\mathrm{FSRG}
\Longrightarrow
{\mathfrak W}_{\Phi,\alpha_n}^{QFT}\to0
\quad
\hbox{for all source-route moves }\Phi.
}
$$

Therefore:

$$
\boxed{
\mathrm{REL\text{-}QFT\text{-}KIN}
=
\mathrm{PASS}
}
$$

for the active Barandes-aligned finite source-response branch.

If FSRG fails, the failure is typed:

$$
\boxed{
\begin{array}{c|l}
\hbox{failed FSRG gate} & \hbox{meaning}\\
\hline
\mathrm{FSRG1} & \hbox{field packet is not finite actual record data}\\
\mathrm{FSRG2} & \hbox{no finite reflection/cut structure}\\
\mathrm{FSRG3} & \hbox{reflection positivity fails}\\
\mathrm{FSRG4} & \hbox{source reflection mismatch}\\
\mathrm{FSRG5} & \hbox{no finite local/collar QFT interpretation}\\
\mathrm{FSRG6} & \hbox{no cofinal field reconstruction}
\end{array}
}
$$

Thus ordinary relativistic QFT is the no-anomaly effective face of finite
source-response gluing.  A failure does not destroy ISP; it prints a
Barandes-aligned non-QFT or corrected-QFT branch.

## 34. Updated Final Status After REL-QFT-KIN Closure

Searchable final tag:

`V4P26-UPDATED-FINAL-QFT-QCD-STATUS`.

After the Einstein and Feynman source-response audits, the final status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{REL\text{-}QFT\text{-}KIN} &
\mathrm{PASS} &
\hbox{finite source-response gluing derives OSD and Ward route closure}\\
\mathrm{YM\text{-}GAUGE} &
\mathrm{PASS} &
\hbox{gauge is finite refinement}\\
\mathrm{YM\text{-}WILSON} &
\mathrm{PASS} &
\hbox{Wilson loops are finite descent traces}\\
\mathrm{RG\text{-}DESCENT} &
\mathrm{PASS} &
\hbox{renormalization classified by }A^{*}R^{*}K^{*}E^{*}\\
\mathrm{QCD\text{-}DYN} &
\mathrm{OPEN}_{cert} &
\hbox{requires finite confinement/mass-gap certificate}\\
\mathrm{BARANDES} &
\mathrm{PASS} &
\hbox{all primitive objects remain finite actual records and finite sums}
\end{array}
}
$$

Thus Paper 26 now closes:

$$
\boxed{
\hbox{relativistic QFT kinematics and finite Yang-Mills/Wilson observables as
V4 finite descent extensions of the P25 GR branch.}
}
$$

It still does not close:

$$
\boxed{
\hbox{unconditional }4D\hbox{ QCD confinement or mass gap.}
}
$$

That remaining problem is exactly:

$$
\boxed{
\hbox{print a finite }QC1\text{-}QC7\hbox{ certificate packet, or type the
surviving QCD Ward obstruction.}
}
$$
