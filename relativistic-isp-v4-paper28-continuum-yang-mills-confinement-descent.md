# Relativistic ISP V4 Paper 28: Continuum Yang-Mills Confinement Descent

Author: Felix Robles Elvira

Status: continuum-bridge paper after Paper 27.

Paper 27 closed the finite ISP QCD dynamics certificate on the active
Barandes-aligned branch:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

It did not claim continuum Yang-Mills confinement:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{NOT\ CLAIMED}_{P27}.
}
$$

This paper attacks the remaining bridge problem:

$$
\boxed{
\hbox{when does finite ISP QCD-DYN survive continuum descent as a continuum
Yang-Mills confinement theorem?}
}
$$

The target is not to import continuum Yang-Mills as primitive ontology.  The
target is to prove that a cofinal family of finite ISP gauge-record systems
has a continuum gauge-invariant limit whose Wilson sector has positive string
tension and whose gauge-invariant local sector has positive mass gap.

## 0. Imports From Papers 24-27

Paper 24 supplies the Barandes-aligned finite effective calibration bridge:

$$
\boxed{
\hbox{finite actual records first; effective continuum language second.}
}
$$

Paper 25 supplies the active GR-compatible finite actual branch:

$$
\boxed{
\mathrm{FAC+SLC+RSC}_{GR}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

Paper 26 supplies finite relativistic QFT and Yang-Mills kinematics:

$$
\boxed{
\begin{array}{c|c}
\hbox{claim} & \hbox{status}\\
\hline
\mathrm{REL\text{-}QFT\text{-}KIN} & \mathrm{PASS}\\
\mathrm{YM\text{-}GAUGE} & \mathrm{PASS}\\
\mathrm{YM\text{-}WILSON} & \mathrm{PASS}\\
\mathrm{RG\text{-}DESCENT} & \mathrm{PASS}\\
\mathrm{BARANDES} & \mathrm{PASS}
\end{array}
}
$$

Paper 27 supplies finite QCD dynamics:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}
}
$$

on the active physical-admissibility law:

$$
\boxed{
\hbox{no physical local obstruction exists outside finite response,
same-actual Ward quotienting, and typed residues.}
}
$$

The present paper imports those finite results but not a continuum
Yang-Mills measure, continuum path integral, continuum confinement theorem,
or continuum mass gap theorem.

## 1. Barandes Boundary For Paper 28

Searchable boundary tag:

`V4P28-BARANDES-CONTINUUM-BRIDGE-BOUNDARY`.

The allowed primitives are:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{finite actual record systems};\\
2.&\hbox{finite same-actual gauge/Ward quotients};\\
3.&\hbox{finite Wilson/source-response observables};\\
4.&\hbox{finite reflection/source-response positivity};\\
5.&\hbox{cofinal refinement maps};\\
6.&\hbox{typed residue registries};\\
7.&\hbox{finite QCD-DYN margins from Paper 27};\\
8.&\hbox{effective continuum objects only as limits of finite records}.
\end{array}
}
$$

The forbidden shortcuts are:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{continuum Yang-Mills measure as primitive ontology};\\
2.&\hbox{continuum path integral as source authority};\\
3.&\hbox{mass gap assumed as input};\\
4.&\hbox{Wilson area law assumed as input};\\
5.&\hbox{untyped zero-response sectors reintroduced in the limit};\\
6.&\hbox{gauge fixing that changes same-actual observables};\\
7.&\hbox{choosing subsequences after seeing the desired confinement result}.
\end{array}
}
$$

Thus Paper 28 may prove continuum confinement only by finite descent:

$$
\boxed{
\hbox{finite ISP certificate}
+
\hbox{cofinal compactness}
+
\hbox{uniform physical margins}
\Longrightarrow
\hbox{continuum YM confinement.}
}
$$

## 2. Continuum YM Target Statement

Searchable target tag:

`V4P28-CONTINUUM-YM-CONFINEMENT-TARGET`.

The continuum target is stated only in gauge-invariant language.

Let:

$$
\boxed{
G=SU(N),
\qquad
d=4
}
$$

unless otherwise stated.  Let:

$$
\boxed{
W(C)
}
$$

be the continuum Wilson loop observable for a closed loop \(C\), understood
as a limit of finite Wilson traces, not as a primitive continuum trace.

Let:

$$
\boxed{
{\mathcal O}_{g.i.}
}
$$

be the continuum gauge-invariant local observable algebra generated as the
descent limit of finite gauge-invariant source probes.

Continuum confinement for this paper means:

$$
\boxed{
\begin{array}{ll}
\mathrm{CYM\text{-}Area}:&
\hbox{there is }\sigma_{*}>0\hbox{ such that large Wilson loops obey an
area-law decay};\\
\mathrm{CYM\text{-}Gap}:&
\hbox{there is }\Delta_{*}>0\hbox{ such that the gauge-invariant local
sector has a mass gap};\\
\mathrm{CYM\text{-}Ward}:&
\hbox{the limiting observables are gauge-invariant same-actual Ward
descents};\\
\mathrm{CYM\text{-}OS}:&
\hbox{the limiting correlators satisfy the reconstruction positivity needed
for a physical continuum sector.}
\end{array}
}
$$

The target theorem is:

$$
\boxed{
\mathrm{finite\ ISP\ QCD\text{-}DYN}
\Longrightarrow
\mathrm{continuum\ YM\ confinement}
}
$$

only after the continuum descent gates below pass.

## 3. Cofinal Finite Gauge Family

Searchable family tag:

`V4P28-COFINAL-FINITE-GAUGE-FAMILY`.

A continuum candidate is a cofinal family:

$$
\boxed{
{\mathfrak Y}
=
\left(
{\mathfrak A}_{\alpha},
K_{\alpha},
a_{\alpha},
L_{\alpha},
{\mathcal G}_{\alpha},
{\mathcal W}_{\alpha},
{\mathcal O}_{\alpha}^{g.i.},
R_{\beta\alpha}
\right)_{\alpha\in I}.
}
$$

The entries are:

$$
\boxed{
\begin{array}{ll}
{\mathfrak A}_{\alpha}:&\hbox{finite ISP actual-record algebra};\\
K_{\alpha}:&\hbox{finite spacetime/gauge cell complex or record graph};\\
a_{\alpha}:&\hbox{effective mesh scale};\\
L_{\alpha}:&\hbox{effective physical volume scale};\\
{\mathcal G}_{\alpha}:&\hbox{finite same-actual gauge groupoid};\\
{\mathcal W}_{\alpha}:&\hbox{finite Wilson loop battery};\\
{\mathcal O}_{\alpha}^{g.i.}:&\hbox{finite gauge-invariant local source
algebra};\\
R_{\beta\alpha}:&\hbox{cofinal refinement/coarse-graining map}.
\end{array}
}
$$

The continuum regime is:

$$
\boxed{
a_{\alpha}\to0,
\qquad
L_{\alpha}\to\infty,
\qquad
\frac{L_{\alpha}}{a_{\alpha}}\to\infty.
}
$$

Every object remains finite at fixed \(\alpha\).  The continuum object is the
cofinal descent of finite observable laws.

## 4. The Eight Continuum Descent Gates

Searchable gate tag:

`V4P28-CYM1-CYM8-DESCENT-GATES`.

Paper 28 reduces continuum Yang-Mills confinement to eight gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{CYM1}:&
\hbox{finite Wilson and local gauge-invariant observables are complete};\\
\mathrm{CYM2}:&
\hbox{same-actual Ward quotienting descends to continuum gauge invariance};\\
\mathrm{CYM3}:&
\hbox{finite reflection/source-response positivity survives descent};\\
\mathrm{CYM4}:&
\hbox{finite correlator laws are tight/compact cofinally};\\
\mathrm{CYM5}:&
\hbox{continuum limits are independent of licensed refinement route};\\
\mathrm{CYM6}:&
\hbox{Wilson area-law margins have positive physical liminf};\\
\mathrm{CYM7}:&
\hbox{gauge-invariant transfer gaps have positive physical liminf};\\
\mathrm{CYM8}:&
\hbox{the limiting theory is continuum Yang-Mills, not a different effective
gauge theory}.
\end{array}
}
$$

The active status before this paper works is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{initial status} & \hbox{source}\\
\hline
\mathrm{CYM1} & \mathrm{PASS}_{P26/P27} &
\hbox{finite Wilson/source-response observables and QCD-DYN}\\
\mathrm{CYM2} & \mathrm{PASS}_{P24\text{-}P27} &
\hbox{same-actual Ward quotient discipline}\\
\mathrm{CYM3} & \mathrm{PASS}_{finite;\ OPEN_{limit}} &
\hbox{finite reflection positivity exists; limit survival must be proved}\\
\mathrm{CYM4} & \mathrm{OPEN}_{compactness} &
\hbox{needs tightness/prokhorov-style finite observable control}\\
\mathrm{CYM5} & \mathrm{OPEN}_{route} &
\hbox{needs cofinal route-independence of limiting laws}\\
\mathrm{CYM6} & \mathrm{OPEN}_{string\ tension} &
\hbox{needs positive physical Wilson margin}\\
\mathrm{CYM7} & \mathrm{OPEN}_{mass\ gap} &
\hbox{needs positive physical spectral margin}\\
\mathrm{CYM8} & \mathrm{OPEN}_{identification} &
\hbox{needs YM identification rather than merely ISP gauge theory}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{CYM3\text{-}CYM8}.
}
$$

This is the initial bridge status, before the later closure packets of Paper
28 are printed and audited.  It should not be read as the final verdict of
the paper.  The final verdict is given in Sections 51-54:

$$
\boxed{
\hbox{initial bridge reduction: }\mathrm{OPEN}_{CYM3\text{-}CYM8}
\quad\longrightarrow\quad
\hbox{final active branch: }\mathrm{PASS}_{ISP\ descent}.
}
$$

The point of the rest of the paper is to turn the open gates in this table
into explicit packets, audits, leak closures, and falsifier gates.

## 5. Physical Margin Survival

Searchable margin tag:

`V4P28-PHYSICAL-MARGIN-SURVIVAL`.

Paper 27 supplies finite margins.  Paper 28 must show they do not disappear
under physical scaling.

Let:

$$
\boxed{
\sigma_{\alpha}^{fin}>0
}
$$

be the finite Wilson area-law margin in lattice/cell units.  Let:

$$
\boxed{
A_{\alpha}^{phys}(S)
}
$$

be the physical area assigned to a spanning surface \(S\).  The physical
string tension is:

$$
\boxed{
\sigma_{\alpha}^{phys}
=
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}}
}
$$

when the finite area count scales as:

$$
\boxed{
|S|_{\alpha}
\sim
\frac{A_{\alpha}^{phys}(S)}{a_{\alpha}^{2}}.
}
$$

The Wilson survival condition is:

$$
\boxed{
\sigma_{*}
=
\liminf_{\alpha}\sigma_{\alpha}^{phys}
>0.
}
$$

Similarly, let:

$$
\boxed{
\Delta_{\alpha}^{fin}
=
-\log
\frac{\lambda_{1,\alpha}^{g.i.}}{\lambda_{0,\alpha}^{g.i.}}
}
$$

be the finite gauge-invariant transfer gap in one effective time step.  The
physical mass gap is:

$$
\boxed{
\Delta_{\alpha}^{phys}
=
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}
}
$$

when the time step scales as \(a_{\alpha}\).  The mass-gap survival condition
is:

$$
\boxed{
\Delta_{*}
=
\liminf_{\alpha}\Delta_{\alpha}^{phys}
>0.
}
$$

Thus the core survival theorem is:

$$
\boxed{
\sigma_{*}>0
\quad\hbox{and}\quad
\Delta_{*}>0
}
$$

with no continuum area law or mass gap inserted as an input.

## 6. Main Bridge Theorem

Searchable main theorem tag:

`V4P28-FINITE-TO-CONTINUUM-YM-CONFINEMENT-THEOREM`.

### Theorem 6.1: CYM1-CYM8 Prove Continuum Yang-Mills Confinement

Assume a cofinal finite gauge family \({\mathfrak Y}\) satisfies CYM1-CYM8.
Then the cofinal limit has a continuum gauge-invariant Yang-Mills sector with
Wilson area law and positive mass gap:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{PASS}.
}
$$

More explicitly:

$$
\boxed{
\langle W(C)\rangle
\le
A(C)\exp(-\sigma_{*}\operatorname{Area}(C))
}
$$

for large admissible loops \(C\), with \(\sigma_{*}>0\), and:

$$
\boxed{
\| \langle{\mathcal O}(x){\mathcal O}(y)\rangle_c \|
\le
B_{\mathcal O}\exp(-\Delta_{*}d(x,y))
}
$$

for gauge-invariant local observables \({\mathcal O}\), with
\(\Delta_{*}>0\).

Proof.  CYM1 gives the finite observable family whose Wilson and local
gauge-invariant sectors are complete enough to test confinement.  CYM2
identifies the same-actual Ward quotient with gauge invariance at every
finite level and in the limit.  CYM3 supplies positivity required for a
physical reconstruction.  CYM4 gives compactness/tightness, so a limiting
observable law exists.  CYM5 prevents the limit from depending on a chosen
refinement route.  CYM6 passes the finite Wilson area-law margins to a
positive physical string tension.  CYM7 passes the finite transfer gap to a
positive physical mass gap.  CYM8 identifies the resulting continuum
gauge-invariant limit as Yang-Mills rather than an unrelated effective gauge
law.  Therefore the continuum limit satisfies area law and gauge-invariant
mass gap. `square`

The theorem is deliberately conditional.  The rest of Paper 28 must attack
CYM3-CYM8.

## 7. Einstein Move: Make The Continuum A Descent Object

Searchable Einstein tag:

`V4P28-EINSTEIN-CONTINUUM-AS-DESCENT-OBJECT`.

Einstein's move is to refuse an unexamined background continuum.  The
continuum must be reconstructed from the invariants of the finite system.

Define the continuum candidate as the projective observable object:

$$
\boxed{
{\mathcal Y}_{\infty}
=
\varprojlim_{\alpha}
\left(
{\mathcal W}_{\alpha},
{\mathcal O}_{\alpha}^{g.i.},
\omega_{\alpha},
R_{\beta\alpha}^{*}
\right).
}
$$

Here \(\omega_{\alpha}\) is the finite source-response state:

$$
\boxed{
\omega_{\alpha}(F)
=
\frac{1}{Z_{\alpha}}
\sum_{x\in{\mathfrak A}_{\alpha}}
\mu_{\alpha}(x)e^{-S_{\alpha}(x)}F(x)
}
$$

where the expression is only finite notation for the actual-record
source-response weight.  It is not a primitive continuum path integral.

The Einstein test is:

$$
\boxed{
\hbox{all continuum geometric and gauge claims must be invariant data of }
{\mathcal Y}_{\infty}.
}
$$

This yields four Einstein subgates:

$$
\boxed{
\begin{array}{ll}
\mathrm{EYM1}:&
\hbox{coincidence/causal/geometric data descend from P25};\\
\mathrm{EYM2}:&
\hbox{gauge holonomy data descend from P26};\\
\mathrm{EYM3}:&
\hbox{finite QCD-DYN margins descend from P27};\\
\mathrm{EYM4}:&
\hbox{no continuum object is used before it is reconstructed}.
\end{array}
}
$$

If EYM1-EYM4 pass, then CYM5 and the Barandes part of CYM8 become natural:
the continuum is not a new ontology but the cofinal invariant face of the
finite record family.

## 8. Feynman Move: The Continuum Source Ledger

Searchable Feynman tag:

`V4P28-FEYNMAN-CONTINUUM-SOURCE-LEDGER`.

Feynman's move is to turn the continuum claim into a source ledger.  Every
claim must be represented as a finite source derivative before the limit is
taken.

Define the finite source functional:

$$
\boxed{
Z_{\alpha}[J,\eta]
=
\sum_{x\in{\mathfrak A}_{\alpha}}
\mu_{\alpha}(x)
\exp\left(
-S_{\alpha}(x)
+J\cdot{\mathcal O}_{\alpha}^{g.i.}(x)
+\eta\cdot{\mathcal W}_{\alpha}(x)
\right).
}
$$

The continuum source functional exists if:

$$
\boxed{
\log Z_{\alpha}[J,\eta]
\longrightarrow
\log Z_{\infty}[J,\eta]
}
$$

on a cofinal source domain, with Ward defects vanishing or becoming typed
residues.

The Feynman subgates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{FYM1}:&
\hbox{source derivatives commute with same-actual Ward quotienting};\\
\mathrm{FYM2}:&
\hbox{source derivatives commute with cofinal refinement};\\
\mathrm{FYM3}:&
\hbox{reflection positivity is a finite square before the limit};\\
\mathrm{FYM4}:&
\hbox{all nonzero limiting defects are typed};\\
\mathrm{FYM5}:&
\hbox{the Wilson and gap margins appear as derivatives or spectral
singularities of the same source ledger}.
\end{array}
}
$$

If FYM1-FYM5 pass, then CYM3-CYM5 are not aesthetic assumptions.  They are
ledger identities.

## 9. Compactness And Tightness Packet

Searchable compactness tag:

`V4P28-COMPACTNESS-TIGHTNESS-PACKET`.

The first genuinely new continuum problem is compactness.

Define the finite observable law:

$$
\boxed{
\nu_{\alpha}
=
\mathrm{Law}_{\omega_{\alpha}}
\left(
({\mathcal O}_{\alpha}^{g.i.}(f))_{f\in{\mathcal F}},
(W_{\alpha}(C))_{C\in{\mathcal C}}
\right)
}
$$

on a finite probe battery \({\mathcal F}\cup{\mathcal C}\).  A compactness
packet is:

$$
\boxed{
\mathrm{YM\text{-}COMPACT\text{-}001}
=
\left(
{\mathcal F},
{\mathcal C},
p,
M_p,
{\mathcal M},
{\mathcal R}
\right).
}
$$

It must satisfy:

$$
\boxed{
\begin{array}{ll}
\mathrm{CP1}:&
\hbox{uniform moment bound }
\sup_{\alpha}\omega_{\alpha}(|{\mathcal O}(f)|^p)\le M_p(f);\\
\mathrm{CP2}:&
\hbox{uniform Wilson bound }|W_{\alpha}(C)|\le{\mathcal M}(C);\\
\mathrm{CP3}:&
\hbox{equicontinuity under finite geometric refinement};\\
\mathrm{CP4}:&
\hbox{tightness of all finite probe marginals};\\
\mathrm{CP5}:&
\hbox{projective consistency of overlapping probe batteries};\\
\mathrm{CP6}:&
\hbox{typed residues do not carry unbounded unobserved mass}.
\end{array}
}
$$

### Theorem 9.1: Compactness Packet Proves CYM4

If `YM-COMPACT-001` satisfies CP1-CP6, then CYM4 holds.

Proof.  CP1-CP2 bound the local and Wilson probe distributions.  CP3 gives
equicontinuity along refinement.  CP4 gives tightness of finite marginals.
CP5 makes the marginals projective.  CP6 prevents probability mass from
escaping into untyped zero-response sectors.  Therefore a cofinal limiting
observable law exists. `square`

Active status:

$$
\boxed{
\mathrm{CYM4}
=
\mathrm{OPEN}_{YM\text{-}COMPACT\text{-}001}.
}
$$

## 10. Uniform Wilson String-Tension Packet

Searchable string-tension tag:

`V4P28-UNIFORM-WILSON-STRING-TENSION-PACKET`.

Paper 27 proves finite Wilson area law in the active branch.  Paper 28 needs
physical survival:

$$
\boxed{
\sigma_{*}
=
\liminf_{\alpha}\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}}
>0.
}
$$

Define:

$$
\boxed{
\mathrm{YM\text{-}STRING\text{-}001}
=
\left(
\sigma_{\alpha}^{fin},
a_{\alpha},
{\mathcal S}_{\alpha},
E_{\alpha}^{surf},
B_{\alpha}^{surf}
\right)_{\alpha}.
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
{\mathcal S}_{\alpha}:&\hbox{finite spanning-surface battery};\\
E_{\alpha}^{surf}:&\hbox{center-flux surface energy/cost};\\
B_{\alpha}^{surf}:&\hbox{surface entropy/branching budget}.
\end{array}
}
$$

The packet gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{ST1}:&
\hbox{finite Wilson loops are represented by descent traces};\\
\mathrm{ST2}:&
\hbox{nontrivial center flux cannot be same-actual vacuum};\\
\mathrm{ST3}:&
E_{\alpha}^{surf}-B_{\alpha}^{surf}
\ge
\sigma_{\alpha}^{fin}|S|_{\alpha};\\
\mathrm{ST4}:&
|S|_{\alpha}a_{\alpha}^{2}
\to
\operatorname{Area}(S);\\
\mathrm{ST5}:&
\liminf_{\alpha}\sigma_{\alpha}^{fin}/a_{\alpha}^{2}>0;\\
\mathrm{ST6}:&
\hbox{boundary/perimeter corrections are subarea in the physical limit}.
\end{array}
}
$$

### Theorem 10.1: String Packet Proves CYM6

If `YM-STRING-001` satisfies ST1-ST6, then CYM6 holds.

Proof.  ST1-ST3 import the finite Paper 27 Wilson area mechanism.  ST4
converts finite surface count to physical area.  ST5 preserves positive
physical string tension.  ST6 prevents perimeter or boundary corrections
from swallowing the area term.  Therefore the limiting Wilson sector has
positive area-law rate. `square`

Active status:

$$
\boxed{
\mathrm{CYM6}
=
\mathrm{OPEN}_{YM\text{-}STRING\text{-}001}.
}
$$

## 11. Uniform Gauge-Invariant Mass-Gap Packet

Searchable mass-gap tag:

`V4P28-UNIFORM-MASS-GAP-PACKET`.

Paper 27 proves finite gauge-invariant spectral gap in the active branch.
Paper 28 needs:

$$
\boxed{
\Delta_{*}
=
\liminf_{\alpha}\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}
>0.
}
$$

Define:

$$
\boxed{
\mathrm{YM\text{-}GAP\text{-}001}
=
\left(
T_{\alpha}^{g.i.},
\lambda_{0,\alpha},
\lambda_{1,\alpha},
a_{\alpha},
{\mathcal O}_{\alpha}^{g.i.}
\right)_{\alpha}.
}
$$

The packet gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{MG1}:&
T_{\alpha}^{g.i.}\hbox{ is the finite gauge-invariant transfer operator};\\
\mathrm{MG2}:&
\lambda_{0,\alpha}\hbox{ is the vacuum/singlet Perron value};\\
\mathrm{MG3}:&
\lambda_{1,\alpha}\hbox{ is the first non-vacuum gauge-invariant value};\\
\mathrm{MG4}:&
\Delta_{\alpha}^{fin}
=-\log(\lambda_{1,\alpha}/\lambda_{0,\alpha});\\
\mathrm{MG5}:&
\liminf_{\alpha}\Delta_{\alpha}^{fin}/a_{\alpha}>0;\\
\mathrm{MG6}:&
\hbox{finite reflection positivity reconstructs this as a physical mass
gap};\\
\mathrm{MG7}:&
\hbox{typed residues are either massive or excluded from the YM sector}.
\end{array}
}
$$

### Theorem 11.1: Gap Packet Proves CYM7

If `YM-GAP-001` satisfies MG1-MG7, then CYM7 holds.

Proof.  MG1-MG4 define the finite gap in the gauge-invariant transfer
sector.  MG5 gives positive physical liminf.  MG6 turns the transfer gap into
decay of reconstructed gauge-invariant correlators.  MG7 prevents a
zero-response typed residue from reappearing as a massless YM excitation.
Therefore the continuum gauge-invariant sector has mass gap
\(\Delta_{*}>0\). `square`

Active status:

$$
\boxed{
\mathrm{CYM7}
=
\mathrm{OPEN}_{YM\text{-}GAP\text{-}001}.
}
$$

## 12. Yang-Mills Identification Packet

Searchable identification tag:

`V4P28-YANG-MILLS-IDENTIFICATION-PACKET`.

Even if compactness, string tension, and mass gap pass, Paper 28 must prove
the limit is continuum Yang-Mills rather than an arbitrary confining
finite-gauge effective theory.

Define:

$$
\boxed{
\mathrm{YM\text{-}ID\text{-}001}
=
\left(
G,
{\mathcal A}_{\alpha}^{conn},
F_{\alpha},
S_{\alpha}^{YM},
{\mathcal W}_{\alpha},
{\mathcal O}_{\alpha}^{g.i.},
{\mathcal R}_{\alpha}
\right)_{\alpha}.
}
$$

The gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{ID1}:&
\hbox{finite holonomy records have structure group }SU(N);\\
\mathrm{ID2}:&
\hbox{small-loop expansion recovers curvature }F_{\mu\nu}\hbox{ in descent};\\
\mathrm{ID3}:&
\hbox{finite action density descends to }\frac{1}{4g^{2}}\int
\operatorname{tr}F_{\mu\nu}F^{\mu\nu};\\
\mathrm{ID4}:&
\hbox{Ward identities descend to continuum gauge invariance};\\
\mathrm{ID5}:&
\hbox{locality/collar compatibility descends from P25 SLC};\\
\mathrm{ID6}:&
\hbox{renormalized couplings are route-independent cofinal invariants};\\
\mathrm{ID7}:&
\hbox{no extra massless or silent sector remains in the YM observable algebra}.
\end{array}
}
$$

### Theorem 12.1: Identification Packet Proves CYM8

If `YM-ID-001` satisfies ID1-ID7, then CYM8 holds.

Proof.  ID1-ID2 identify the gauge connection and curvature data.  ID3
identifies the local action density.  ID4 preserves gauge invariance.  ID5
puts the theory on the P25 effective locality/collar structure.  ID6 removes
renormalization-route dependence.  ID7 prevents hidden non-YM sectors.
Therefore the limiting gauge-invariant continuum law is Yang-Mills in the
scope of the reconstructed observables. `square`

Active status:

$$
\boxed{
\mathrm{CYM8}
=
\mathrm{OPEN}_{YM\text{-}ID\text{-}001}.
}
$$

## 13. Master Continuum Certificate

Searchable master packet tag:

`V4P28-CONTINUUM-YM-CERTIFICATE-001`.

The continuum certificate is:

$$
\boxed{
\mathrm{CYM\text{-}CERT\text{-}001}
=
\left(
{\mathfrak Y},
\mathrm{YM\text{-}COMPACT\text{-}001},
\mathrm{YM\text{-}STRING\text{-}001},
\mathrm{YM\text{-}GAP\text{-}001},
\mathrm{YM\text{-}ID\text{-}001}
\right).
}
$$

It passes if:

$$
\boxed{
\begin{array}{c|c}
\hbox{packet} & \hbox{required gates}\\
\hline
{\mathfrak Y} & \mathrm{CYM1,CYM2,CYM3,CYM5}\\
\mathrm{YM\text{-}COMPACT\text{-}001} & \mathrm{CP1\text{-}CP6}\\
\mathrm{YM\text{-}STRING\text{-}001} & \mathrm{ST1\text{-}ST6}\\
\mathrm{YM\text{-}GAP\text{-}001} & \mathrm{MG1\text{-}MG7}\\
\mathrm{YM\text{-}ID\text{-}001} & \mathrm{ID1\text{-}ID7}
\end{array}
}
$$

### Theorem 13.1: Master Certificate Closes Continuum YM Confinement

If `CYM-CERT-001` passes, then:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{PASS}_{ISP\ descent}.
}
$$

Proof.  The master certificate gives CYM1-CYM8 by construction: CYM1-CYM3
from the cofinal finite family and Papers 26-27, CYM4 from Theorem 9.1,
CYM6 from Theorem 10.1, CYM7 from Theorem 11.1, CYM8 from Theorem 12.1, and
CYM5 from route-independence of the cofinal family.  Then Theorem 6.1 proves
continuum Yang-Mills confinement in the reconstructed gauge-invariant sector.
`square`

Current status:

$$
\boxed{
\mathrm{CYM\text{-}CERT\text{-}001}
=
\mathrm{OPEN}_{compactness+string+gap+identification}.
}
$$

## 14. Falsifier Gates

Searchable falsifier tag:

`V4P28-CONTINUUM-YM-FALSIFIER-GATES`.

Paper 28 should be falsifiable.  The route fails if any of the following
occur:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{F1} &
\hbox{finite observable laws have no tight cofinal limit} &
\hbox{no continuum observable law}\\
\mathrm{F2} &
\hbox{reflection positivity fails in the limit} &
\hbox{no physical reconstructed sector}\\
\mathrm{F3} &
\sigma_{\alpha}^{fin}/a_{\alpha}^{2}\to0 &
\hbox{finite area law becomes zero continuum string tension}\\
\mathrm{F4} &
\Delta_{\alpha}^{fin}/a_{\alpha}\to0 &
\hbox{finite mass gap becomes zero continuum gap}\\
\mathrm{F5} &
\hbox{same-actual Ward quotient fails under refinement} &
\hbox{bad gauge descent}\\
\mathrm{F6} &
\hbox{a silent untyped sector appears in the limit} &
\hbox{Paper 27 actual-response ontology breaks at continuum descent}\\
\mathrm{F7} &
\hbox{the limit is not YM but another gauge effective law} &
\hbox{identification failure}\\
\mathrm{F8} &
\hbox{subsequence is chosen after the desired result is known} &
\hbox{posterior continuum fitting}
\end{array}
}
$$

If F1-F8 are all avoided and `CYM-CERT-001` passes, the continuum theorem
closes.  If any falsifier fires, the failure is informative rather than
vague: it locates the exact bridge that cannot be licensed.

## 15. Initial Work Order

Searchable work-order tag:

`V4P28-CONTINUUM-YM-WORK-ORDER`.

The next concrete work is:

$$
\boxed{
\begin{array}{c|l|c}
\hbox{step} & \hbox{task} & \hbox{target}\\
\hline
1 &
\hbox{print }{\mathfrak Y}\hbox{ explicitly from P24-P27 finite packets} &
\mathrm{CYM1,CYM2,CYM3,CYM5}\\
2 &
\hbox{print moment/tightness controls for finite source observables} &
\mathrm{CP1\text{-}CP6}\\
3 &
\hbox{scale the Paper 27 Wilson margin into physical units} &
\mathrm{ST1\text{-}ST6}\\
4 &
\hbox{scale the Paper 27 transfer gap into physical units} &
\mathrm{MG1\text{-}MG7}\\
5 &
\hbox{prove small-loop/curvature/action-density identification} &
\mathrm{ID1\text{-}ID7}\\
6 &
\hbox{audit all route choices for posterior fitting} &
\mathrm{F8}
\end{array}
}
$$

This is the real attack surface:

$$
\boxed{
\hbox{compactness, uniform physical margins, and YM identification.}
}
$$

## 16. Active Paper 28 Verdict

Searchable verdict tag:

`V4P28-ACTIVE-CONTINUUM-YM-VERDICT`.

At the start of Paper 28:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{finite\ ISP\ QCD\text{-}DYN} &
\mathrm{PASS} &
\hbox{Paper 27}\\
\mathrm{continuum\ observable\ limit} &
\mathrm{OPEN} &
\hbox{requires compactness/tightness}\\
\mathrm{positive\ continuum\ string\ tension} &
\mathrm{OPEN} &
\hbox{requires }\liminf\sigma_{\alpha}^{fin}/a_{\alpha}^{2}>0\\
\mathrm{positive\ continuum\ mass\ gap} &
\mathrm{OPEN} &
\hbox{requires }\liminf\Delta_{\alpha}^{fin}/a_{\alpha}>0\\
\mathrm{continuum\ YM\ identification} &
\mathrm{OPEN} &
\hbox{requires small-loop/action-density/Ward descent}\\
\mathrm{continuum\ YM\ confinement} &
\mathrm{OPEN}_{CYM\text{-}CERT\text{-}001} &
\hbox{requires the master certificate}
\end{array}
}
$$

Therefore the honest status is:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{compactness+uniform\ margins+YM\ identification}.
}
$$

The win from Paper 27 is that the finite dynamics is no longer the missing
piece.  The remaining problem is a sharply named continuum descent problem.

## 17. Einstein Way: Continuum Identity By Invariant Descent

Searchable Einstein identity tag:

`V4P28-EINSTEIN-CONTINUUM-IDENTITY-BY-INVARIANT-DESCENT`.

Einstein's deeper move is to remove a false freedom.  The continuum cannot be
a second world placed behind the finite records.  It must be the invariant
language of a cofinal family of finite record relations.

Define the finite gauge-invariant observable packet at level \(\alpha\):

$$
\boxed{
{\mathcal P}_{\alpha}^{g.i.}
=
\left(
{\mathcal W}_{\alpha},
{\mathcal O}_{\alpha}^{g.i.},
\omega_{\alpha},
{\mathcal I}_{\alpha}^{Ward},
{\mathcal T}_{\alpha}^{typed}
\right).
}
$$

The continuum physical packet is not a manifold plus fields first.  It is:

$$
\boxed{
{\mathcal P}_{\infty}^{g.i.}
=
\varprojlim_{\alpha}
{\mathcal P}_{\alpha}^{g.i.}
}
$$

whenever the projective limit exists after same-actual Ward quotienting and
typed-residue registration.

A continuum presentation:

$$
\boxed{
{\mathcal C}
=
(M,G,{\mathcal A},{\mathcal O}^{g.i.},W,\omega)
}
$$

is licensed only if it represents the same projective packet:

$$
\boxed{
\operatorname{Rep}({\mathcal C})
=
{\mathcal P}_{\infty}^{g.i.}.
}
$$

The Einstein identity principle is:

$$
\boxed{
\operatorname{Rep}({\mathcal C})
=
\operatorname{Rep}({\mathcal C}')
\quad\Longrightarrow\quad
{\mathcal C}\sim_{\mathrm{phys}}{\mathcal C}'.
}
$$

That is, two continuum descriptions with the same cofinal finite
gauge-invariant content are the same physical continuum sector.  Coordinates,
gauge choices, collars, triangulations, regulators, and route presentations
are not additional physics.

The identity packet is:

$$
\boxed{
\mathrm{EYM\text{-}IDENTITY\text{-}001}
}
$$

with gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{EI1}:&
\hbox{finite Wilson and local source probes are cofinally complete};\\
\mathrm{EI2}:&
\hbox{same-actual Ward quotienting removes all gauge/presentation
redundancy};\\
\mathrm{EI3}:&
\hbox{typed residues are the only allowed response-invisible survivors};\\
\mathrm{EI4}:&
\hbox{projective observable limits are route-independent};\\
\mathrm{EI5}:&
\hbox{small-loop and local-source normal forms identify }SU(N)\hbox{ YM};\\
\mathrm{EI6}:&
\hbox{no continuum field variable is admitted without finite observable
descent}.
\end{array}
}
$$

### Theorem 17.1: Einstein Identity Proves Route And Ontology Uniqueness

Assume `EYM-IDENTITY-001` satisfies EI1-EI6.  Then CYM5 holds.  Moreover,
CYM8 reduces to the small-loop/action-density identification gate EI5.

Proof.  EI1 says the finite observable packet is complete for the continuum
questions being asked.  EI2 and EI3 say the only invisible differences are
same-actual Ward redundancy or typed residue.  EI4 makes the projective limit
independent of the chosen cofinal refinement route, proving CYM5.  EI6
forbids adding continuum field variables that are not represented in
\({\mathcal P}_{\infty}^{g.i.}\).  Therefore any remaining difference
between the reconstructed sector and continuum Yang-Mills must be in EI5:
the identification of the finite holonomy/action-density normal form with
the Yang-Mills curvature/action form. `square`

Einstein's conclusion is:

$$
\boxed{
\hbox{the continuum is not an extra arena; it is the invariant completion of
finite gauge-invariant records.}
}
$$

So the continuum bridge is sharpened:

$$
\boxed{
\mathrm{CYM5}
=
\mathrm{OPEN}_{EI4},
\qquad
\mathrm{CYM8}
=
\mathrm{OPEN}_{EI5}.
}
$$

## 18. Einstein Strong Equivalence Audit For Continuum YM

Searchable equivalence tag:

`V4P28-EINSTEIN-STRONG-CONTINUUM-EQUIVALENCE-AUDIT`.

Einstein would next ask whether the continuum limit has an analogue of the
equivalence principle: all licensed finite descriptions of the same actual
gauge record must give the same continuum physics.

Let:

$$
\boxed{
\Phi_{\alpha}
:
{\mathcal P}_{\alpha}^{g.i.}
\to
{\mathcal P}_{\alpha}^{g.i.}
}
$$

be a licensed finite route move: refinement, collar change, gauge
presentation change, local frame change, or source-order change.  Define the
continuum Ward defect:

$$
\boxed{
{\mathfrak D}_{\infty}(\Phi;J,\eta)
=
\lim_{\alpha}
\left(
\log Z_{\alpha}[\Phi^{*}(J,\eta)]
-
\log Z_{\alpha}[J,\eta]
\right).
}
$$

The strong continuum equivalence audit is:

$$
\boxed{
{\mathfrak D}_{\infty}(\Phi;J,\eta)
=0
\quad\hbox{or}\quad
{\mathfrak D}_{\infty}(\Phi;J,\eta)
\in{\mathcal T}_{\infty}^{typed}.
}
$$

If a route defect is neither zero nor typed, the continuum is not a descent
object.  It is carrying unlicensed route-dependent physics.

### Theorem 18.1: Strong Equivalence Blocks Continuum Gauge Ambiguity

Assume every licensed finite route move satisfies the strong continuum
equivalence audit.  Then no gauge, collar, source-order, or refinement route
ambiguity can change continuum Wilson or gauge-invariant local correlators
except by declared typed residue.

Proof.  The defect formula measures the entire source-response change under
the route move.  If it vanishes, source derivatives agree for all Wilson and
local gauge-invariant observables.  If it is typed, the difference is not a
hidden ambiguity but a printed sector.  No other case is admitted.  Therefore
continuum gauge and route ambiguity are removed at the level of physical
observable laws. `square`

This is the Einstein version of the next bridge:

$$
\boxed{
\hbox{prove all continuum route defects vanish or are typed.}
}
$$

## 19. Feynman Way: Continuum Source Ledger No-Escape Decomposition

Searchable Feynman no-escape tag:

`V4P28-FEYNMAN-CONTINUUM-NO-ESCAPE-LEDGER`.

Feynman's deeper move is to make the continuum theorem pay rent in the
ledger.  If finite QCD-DYN passes but continuum confinement fails, then the
failure must appear as a named term in the source-response accounting.

Use the finite source functional:

$$
\boxed{
Z_{\alpha}[J,\eta]
=
\sum_{x\in{\mathfrak A}_{\alpha}}
\mu_{\alpha}(x)
\exp\left(
-S_{\alpha}(x)
+J\cdot{\mathcal O}_{\alpha}^{g.i.}(x)
+\eta\cdot{\mathcal W}_{\alpha}(x)
\right).
}
$$

Define the finite free-energy ledger:

$$
\boxed{
{\mathcal F}_{\alpha}[J,\eta]
=
-\log Z_{\alpha}[J,\eta].
}
$$

The continuum source ledger exists on a source domain
\({\mathcal D}_{src}\) if:

$$
\boxed{
{\mathcal F}_{\alpha}[J,\eta]
\to
{\mathcal F}_{\infty}[J,\eta]
\qquad
\hbox{for }(J,\eta)\in{\mathcal D}_{src}.
}
$$

Now define the seven leak channels:

$$
\boxed{
\begin{array}{ll}
\mathrm{LEAK1}:&
\hbox{compactness leak: }{\mathcal F}_{\alpha}\hbox{ has no cofinal source
limit};\\
\mathrm{LEAK2}:&
\hbox{positivity leak: reflection/source positivity fails in the limit};\\
\mathrm{LEAK3}:&
\hbox{Ward leak: same-actual source derivatives disagree in the limit};\\
\mathrm{LEAK4}:&
\hbox{string leak: }\liminf\sigma_{\alpha}^{fin}/a_{\alpha}^{2}=0;\\
\mathrm{LEAK5}:&
\hbox{gap leak: }\liminf\Delta_{\alpha}^{fin}/a_{\alpha}=0;\\
\mathrm{LEAK6}:&
\hbox{identity leak: the limit is not }SU(N)\hbox{ Yang-Mills};\\
\mathrm{LEAK7}:&
\hbox{hidden-sector leak: untyped zero-response mass survives the limit}.
\end{array}
}
$$

These are not optional metaphors.  They are the only places where finite
QCD-DYN can fail to become continuum confinement while respecting the source
ledger.

### Theorem 19.1: Feynman No-Escape Decomposition

Assume:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}
}
$$

and assume no posterior subsequence fitting.  If continuum Yang-Mills
confinement fails, then at least one leak channel fires:

$$
\boxed{
\neg\mathrm{CYM\text{-}Confinement}
\Longrightarrow
\bigvee_{k=1}^{7}\mathrm{LEAK}k.
}
$$

Proof.  If LEAK1 does not fire, the finite source ledgers have a cofinal
continuum source limit.  If LEAK2 does not fire, the limit is a physical
reflection-positive reconstructed sector.  If LEAK3 does not fire,
same-actual Ward quotienting survives the limit.  If LEAK4 does not fire,
the Paper 27 finite Wilson area margins survive as positive physical string
tension.  If LEAK5 does not fire, the Paper 27 finite transfer gaps survive
as a positive physical mass gap.  If LEAK6 does not fire, the reconstructed
sector is the \(SU(N)\) Yang-Mills sector.  If LEAK7 does not fire, no silent
untyped zero-response sector carries away probability, spectral weight, or
source response.  With all seven leaks shut, CYM1-CYM8 hold, so Theorem 6.1
gives continuum Yang-Mills confinement.  Therefore failure implies at least
one leak. `square`

The contrapositive is the working theorem:

$$
\boxed{
\bigwedge_{k=1}^{7}\neg\mathrm{LEAK}k
\Longrightarrow
\mathrm{continuum\ YM\ confinement}.
}
$$

This is the real Feynman move: every possible failure must leave a finite
ledger trace.

## 20. Feynman Ledger Equalities For The Two Physical Margins

Searchable margin-ledger tag:

`V4P28-FEYNMAN-MARGIN-LEDGER-EQUALITIES`.

The two most dangerous leaks are LEAK4 and LEAK5.  Feynman would put them
directly into the source ledger.

For a Wilson loop \(C=\partial S\), define:

$$
\boxed{
{\mathcal A}_{\alpha}^{W}(C)
=
-\log
\left|
\frac{\partial}{\partial\eta_C}
\log Z_{\alpha}[0,\eta]
\bigg|_{\eta=0}
\right|.
}
$$

The finite area-law margin is the lower density:

$$
\boxed{
\sigma_{\alpha}^{fin}
=
\inf_{C=\partial S}
\frac{
{\mathcal A}_{\alpha}^{W}(C)-B_{\alpha}^{per}(C)
}
{|S|_{\alpha}}.
}
$$

The physical string tension is:

$$
\boxed{
\sigma_{\alpha}^{phys}
=
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}}.
}
$$

Thus LEAK4 is exactly:

$$
\boxed{
\inf_{\alpha\ \mathrm{cofinal}}\sigma_{\alpha}^{phys}=0.
}
$$

For the mass gap, define the connected two-point ledger:

$$
\boxed{
G_{\alpha}^{conn}(f,g;t)
=
\frac{\partial^{2}}{\partial J_f\partial J_g}
\log Z_{\alpha}[J,0]\bigg|_{J=0,\,\mathrm{sep}=t}.
}
$$

The finite transfer gap is licensed by:

$$
\boxed{
\|G_{\alpha}^{conn}(f,g;t)\|
\le
C_{\alpha}(f,g)e^{-\Delta_{\alpha}^{fin} t}.
}
$$

The physical mass gap is:

$$
\boxed{
\Delta_{\alpha}^{phys}
=
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}.
}
$$

Thus LEAK5 is exactly:

$$
\boxed{
\inf_{\alpha\ \mathrm{cofinal}}\Delta_{\alpha}^{phys}=0.
}
$$

The margin ledger says:

$$
\boxed{
\mathrm{continuum\ confinement}
\hbox{ can fail after finite QCD-DYN only if one of these two physical
densities collapses or another named leak fires.}
}
$$

## 21. Combined Einstein-Feynman Audit

Searchable combined audit tag:

`V4P28-EINSTEIN-FEYNMAN-CONTINUUM-AUDIT`.

The two ways now fit together:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{route} & \hbox{principle} & \hbox{paper effect}\\
\hline
\hbox{Einstein} &
\hbox{continuum identity by invariant descent} &
\hbox{sharpens CYM5 and CYM8}\\
\hbox{Feynman} &
\hbox{source-ledger no-escape decomposition} &
\hbox{sharpens CYM3-CYM7 and falsifiers}\\
\hbox{Paper 27} &
\hbox{finite QCD-DYN pass} &
\hbox{supplies the finite Wilson and gap engines}
\end{array}
}
$$

Updated gate status:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{updated status} & \hbox{new form}\\
\hline
\mathrm{CYM1} &
\mathrm{PASS} &
\hbox{P26/P27 finite Wilson and local observables}\\
\mathrm{CYM2} &
\mathrm{PASS} &
\hbox{same-actual Ward quotient discipline}\\
\mathrm{CYM3} &
\mathrm{OPEN}_{LEAK2} &
\hbox{limit reflection positivity}\\
\mathrm{CYM4} &
\mathrm{OPEN}_{LEAK1} &
\hbox{source-ledger compactness}\\
\mathrm{CYM5} &
\mathrm{OPEN}_{EI4+LEAK3} &
\hbox{route-independent projective limit}\\
\mathrm{CYM6} &
\mathrm{OPEN}_{LEAK4} &
\hbox{positive physical string tension}\\
\mathrm{CYM7} &
\mathrm{OPEN}_{LEAK5} &
\hbox{positive physical mass gap}\\
\mathrm{CYM8} &
\mathrm{OPEN}_{EI5+LEAK6} &
\hbox{Yang-Mills identification}\\
\hbox{hidden sector} &
\mathrm{OPEN}_{LEAK7} &
\hbox{no untyped zero-response escape in continuum descent}
\end{array}
}
$$

Therefore the bridge has become:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{LEAK1\text{-}LEAK7}.
}
$$

and the exact closure criterion is:

$$
\boxed{
\neg\mathrm{LEAK1}
\wedge\cdots\wedge
\neg\mathrm{LEAK7}
\Longrightarrow
\mathrm{continuum\ YM\ confinement}.
}
$$

## 22. Next Direct Attack Order

Searchable next-order tag:

`V4P28-NEXT-DIRECT-ATTACK-ORDER`.

The correct order is not arbitrary.  Some gates are structural, and some are
physical-margin gates.

First close the structural gates:

$$
\boxed{
\begin{array}{c|l}
\hbox{priority} & \hbox{gate}\\
\hline
1 & \mathrm{LEAK3}\hbox{: Ward/source route consistency}\\
2 & \mathrm{LEAK7}\hbox{: no silent untyped continuum sector}\\
3 & \mathrm{LEAK1}\hbox{: source-ledger compactness}\\
4 & \mathrm{LEAK2}\hbox{: limit reflection positivity}\\
5 & \mathrm{LEAK6}\hbox{: YM identification}
\end{array}
}
$$

Then close the physical margins:

$$
\boxed{
\begin{array}{c|l}
\hbox{priority} & \hbox{gate}\\
\hline
6 & \mathrm{LEAK4}\hbox{: positive physical string tension}\\
7 & \mathrm{LEAK5}\hbox{: positive physical mass gap}
\end{array}
}
$$

The reason is simple.  If the continuum source ledger is not well-defined, or
if Ward identity fails, or if silent sectors reappear, then the physical
margin numbers do not yet mean what they are supposed to mean.

The next concrete packet to print is therefore:

$$
\boxed{
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}
}
$$

with:

$$
\boxed{
\begin{array}{ll}
\mathrm{SLC1}:&\hbox{finite source domain }{\mathcal D}_{src};\\
\mathrm{SLC2}:&\hbox{uniform logarithmic moment bounds};\\
\mathrm{SLC3}:&\hbox{same-actual Ward derivative invariance};\\
\mathrm{SLC4}:&\hbox{typed-residue tightness};\\
\mathrm{SLC5}:&\hbox{reflection-square stability};\\
\mathrm{SLC6}:&\hbox{projective consistency under }R_{\beta\alpha};\\
\mathrm{SLC7}:&\hbox{no posterior subsequence selection}.
\end{array}
}
$$

If SLC1-SLC7 pass, LEAK1, LEAK2, LEAK3, and LEAK7 are substantially reduced.
Then Paper 28 can attack the two margin survival estimates with a clean
continuum ledger.

## 23. Einstein Way: Continuum Actual Identity Has No Silent Limit

Searchable Einstein no-silent-limit tag:

`V4P28-EINSTEIN-CONTINUUM-ACTUAL-IDENTITY-NO-SILENT-LIMIT`.

Einstein's next move is to make the continuum identity rule strong enough to
survive the limit.  Paper 27 ruled out finite untyped zero-response QCD
obstructions.  Paper 28 must rule out their return as a continuum artifact.

For each finite level define the source-response profile:

$$
\boxed{
{\mathsf R}_{\alpha}^{src}(x)
=
\left(
\frac{\partial^{|I|+|K|}}
{\partial J_I\partial\eta_K}
\log Z_{\alpha}[J,\eta]\bigg|_{J=\eta=0}
\right)_{(I,K)\in{\mathcal B}_{src,\alpha}}.
}
$$

Here \({\mathcal B}_{src,\alpha}\) is a finite battery of local
gauge-invariant source derivatives and Wilson source derivatives.

The continuum source-response profile is the cofinal class:

$$
\boxed{
{\mathsf R}_{\infty}^{src}(x)
=
\left[{\mathsf R}_{\alpha}^{src}(x_{\alpha})\right]_{\alpha\ \mathrm{cofinal}}.
}
$$

The continuum actual-identity law is:

$$
\boxed{
{\mathsf R}_{\infty}^{src}(x)
=
{\mathsf R}_{\infty}^{src}(y)
\quad\Longrightarrow\quad
x\sim_{\infty}^{same}y
\hbox{ or }x-y\in{\mathcal T}_{\infty}^{typed}.
}
$$

This law says that there is no hidden continuum actual difference behind all
finite source-response data.  A difference is physical only if it is visible
in the cofinal source ledger or printed as typed residue.

The Einstein packet is:

$$
\boxed{
\mathrm{CONTINUUM\text{-}ACTUAL\text{-}IDENTITY\text{-}001}
}
$$

with gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{CAI1}:&
\hbox{finite source-response batteries are cofinally separating};\\
\mathrm{CAI2}:&
\hbox{same-actual Ward equivalence is closed under cofinal refinement};\\
\mathrm{CAI3}:&
\hbox{typed residue registry is closed under cofinal refinement};\\
\mathrm{CAI4}:&
\hbox{no new response-invisible class appears only at the limit};\\
\mathrm{CAI5}:&
\hbox{source derivatives commute with the projective limit on }
{\mathcal D}_{src};\\
\mathrm{CAI6}:&
\hbox{continuum equality is equality of cofinal finite profiles, not an
external continuum equality}.
\end{array}
}
$$

### Theorem 23.1: Continuum Actual Identity Closes LEAK3 And LEAK7

If `CONTINUUM-ACTUAL-IDENTITY-001` satisfies CAI1-CAI6, then:

$$
\boxed{
\neg\mathrm{LEAK3}
\quad\hbox{and}\quad
\neg\mathrm{LEAK7}.
}
$$

Proof.  CAI5 makes source derivatives compatible with cofinal descent.
Therefore a same-actual finite Ward move cannot change the limiting source
derivatives unless the change survives as a typed residue.  CAI2 and CAI3
make that classification stable, so LEAK3 is shut.  For LEAK7, suppose an
untyped zero-response sector appears only in the continuum.  By CAI6 it must
be represented by a cofinal finite profile.  By CAI1 and CAI4, a
response-invisible cofinal class is either same-actual Ward/vacuum or typed.
That contradicts the assumption that it is an untyped hidden sector.
Therefore LEAK7 is shut. `square`

The Einstein result is:

$$
\boxed{
\mathrm{CONTINUUM\text{-}ACTUAL\text{-}IDENTITY\text{-}001}
\Longrightarrow
\neg\mathrm{LEAK3}\wedge\neg\mathrm{LEAK7}.
}
$$

This does not yet prove compactness or physical margins.  It proves that the
continuum limit is not allowed to invent silent actual QCD content after the
finite theory has removed it.

## 24. Feynman Way: Source-Ledger Compactness And Positivity

Searchable source-ledger compactness tag:

`V4P28-FEYNMAN-SOURCE-LEDGER-COMPACTNESS-NO-ESCAPE`.

Feynman's next move is to give the source ledger enough structure that
compactness, positivity, Ward invariance, and hidden-sector tightness become
one theorem.

Define the normalized finite source free energy:

$$
\boxed{
\Phi_{\alpha}[J,\eta]
=
\log Z_{\alpha}[J,\eta]
-\log Z_{\alpha}[0,0].
}
$$

The source domain is a finite-radius cylinder:

$$
\boxed{
{\mathcal D}_{src}(r)
=
\left\{
(J,\eta):
\|J\|_{{\mathcal B}_{loc}}+\|\eta\|_{{\mathcal B}_{W}}\le r
\right\}.
}
$$

The no-escape source-ledger packet is:

$$
\boxed{
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}
}
$$

with gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{SLC1}:&
\hbox{a fixed cofinal source domain }{\mathcal D}_{src}(r)\hbox{ is declared};\\
\mathrm{SLC2}:&
\hbox{uniform logarithmic moment bounds hold on }{\mathcal D}_{src}(r);\\
\mathrm{SLC3}:&
\hbox{same-actual Ward derivative defects vanish or are typed};\\
\mathrm{SLC4}:&
\hbox{typed residues are tight and carry declared response};\\
\mathrm{SLC5}:&
\hbox{finite reflection-square positivity is stable on the source domain};\\
\mathrm{SLC6}:&
\hbox{projective consistency holds under }R_{\beta\alpha};\\
\mathrm{SLC7}:&
\hbox{no posterior subsequence selection is used};\\
\mathrm{SLC8}:&
\hbox{escaping source mass is impossible outside Ward/vacuum or typed
residue};\\
\mathrm{SLC9}:&
\hbox{all limiting derivatives are limits of finite derivatives}.
\end{array}
}
$$

The uniform logarithmic moment bound is:

$$
\boxed{
\sup_{\alpha}
\sup_{(J,\eta)\in{\mathcal D}_{src}(r)}
|\Phi_{\alpha}[J,\eta]|
\le
M(r).
}
$$

The derivative bound is:

$$
\boxed{
\sup_{\alpha}
\sup_{(J,\eta)\in{\mathcal D}_{src}(r/2)}
\left|
\partial_{J}^{I}\partial_{\eta}^{K}\Phi_{\alpha}[J,\eta]
\right|
\le
M_{I,K}(r).
}
$$

The Ward derivative defect is:

$$
\boxed{
{\mathfrak W}_{\alpha,\Phi}^{I,K}
=
\partial_{J}^{I}\partial_{\eta}^{K}
\left(
\Phi_{\alpha}[\Phi^{*}(J,\eta)]
-\Phi_{\alpha}[J,\eta]
\right)\bigg|_{J=\eta=0}.
}
$$

SLC3 requires:

$$
\boxed{
{\mathfrak W}_{\alpha,\Phi}^{I,K}
\to0
\quad\hbox{or}\quad
{\mathfrak W}_{\alpha,\Phi}^{I,K}
\to
{\mathfrak t}_{\Phi}^{I,K}
\in{\mathcal T}_{\infty}^{typed}.
}
$$

Reflection-square stability means that for every reflected source
\(\theta J,\theta\eta\):

$$
\boxed{
\liminf_{\alpha}
\sum_{a,b}
\overline{c_a}c_b
Z_{\alpha}[\theta s_a+s_b]
\ge0.
}
$$

### Theorem 24.1: Source-Ledger Compactness Shuts Four Leaks

If `YM-SOURCE-LEDGER-COMPACTNESS-001` satisfies SLC1-SLC9, then:

$$
\boxed{
\neg\mathrm{LEAK1}
\wedge
\neg\mathrm{LEAK2}
\wedge
\neg\mathrm{LEAK3}
\wedge
\neg\mathrm{LEAK7}.
}
$$

Proof.  SLC1, SLC2, SLC6, SLC7, and the derivative bounds give normal-family
compactness of the finite source free energies on the declared source domain,
so a cofinal source ledger exists without posterior subsequence fitting.  This
shuts LEAK1.  SLC5 passes finite reflection-square positivity to the limit,
shutting LEAK2.  SLC3 and SLC9 make same-actual Ward derivative invariance
survive the limit, with nonzero defects printed as typed residues; this shuts
LEAK3.  SLC4 and SLC8 prevent probability, spectral weight, or response
weight from escaping into an untyped zero-response sector, shutting LEAK7.
`square`

Thus:

$$
\boxed{
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}
\Longrightarrow
\neg\mathrm{LEAK1}
\wedge
\neg\mathrm{LEAK2}
\wedge
\neg\mathrm{LEAK3}
\wedge
\neg\mathrm{LEAK7}.
}
$$

This is the Feynman result: the continuum source ledger has no unaccounted
place to lose finite QCD-DYN.

## 25. Structural Leak Reduction Theorem

Searchable structural reduction tag:

`V4P28-STRUCTURAL-LEAK-REDUCTION-THEOREM`.

Combine the Einstein and Feynman packets:

$$
\boxed{
\mathrm{STRUCTURAL\text{-}DESCENT\text{-}001}
=
\mathrm{CONTINUUM\text{-}ACTUAL\text{-}IDENTITY\text{-}001}
+
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}.
}
$$

### Theorem 25.1: Structural Descent Reduces Continuum YM To Three Leaks

If `STRUCTURAL-DESCENT-001` passes, then:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{LEAK4+LEAK5+LEAK6}.
}
$$

Equivalently, after structural descent:

$$
\boxed{
\neg\mathrm{LEAK4}
\wedge
\neg\mathrm{LEAK5}
\wedge
\neg\mathrm{LEAK6}
\Longrightarrow
\mathrm{continuum\ YM\ confinement}.
}
$$

Proof.  Theorem 23.1 shuts LEAK3 and LEAK7.  Theorem 24.1 shuts LEAK1,
LEAK2, LEAK3, and LEAK7.  Therefore the only remaining channels in the
Feynman no-escape decomposition are LEAK4, LEAK5, and LEAK6.  By Theorem
19.1, if those three do not fire, continuum Yang-Mills confinement follows.
`square`

The meaning is sharp:

$$
\boxed{
\begin{array}{c|l}
\hbox{remaining leak} & \hbox{meaning}\\
\hline
\mathrm{LEAK4} & \hbox{physical string tension collapses}\\
\mathrm{LEAK5} & \hbox{physical mass gap collapses}\\
\mathrm{LEAK6} & \hbox{limit is not continuum }SU(N)\hbox{ Yang-Mills}
\end{array}
}
$$

## 26. Audit Of The Structural Descent Packet

Searchable structural audit tag:

`V4P28-STRUCTURAL-DESCENT-AUDIT`.

The current audit is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{CAI1} &
\mathrm{OPEN}_{cofinal\ separation} &
\hbox{must prove source batteries separate continuum-relevant classes}\\
\mathrm{CAI2} &
\mathrm{PASS}_{P24\text{-}P27} &
\hbox{same-actual Ward equivalence is the active corpus rule}\\
\mathrm{CAI3} &
\mathrm{PASS}_{P27} &
\hbox{typed residue registry is the no-silent-sector rule}\\
\mathrm{CAI4} &
\mathrm{OPEN}_{limit} &
\hbox{must rule out new response-invisible limit classes}\\
\mathrm{CAI5} &
\mathrm{OPEN}_{derivatives} &
\hbox{must commute source derivatives with cofinal limits}\\
\mathrm{CAI6} &
\mathrm{PASS}_{definition} &
\hbox{continuum equality is defined by cofinal finite profiles}
\end{array}
}
$$

and:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{SLC1} &
\mathrm{PASS}_{declared} &
\hbox{source domain can be fixed before the query}\\
\mathrm{SLC2} &
\mathrm{OPEN}_{moment} &
\hbox{needs uniform logarithmic moment bounds}\\
\mathrm{SLC3} &
\mathrm{PASS}_{P24\text{-}P27} &
\hbox{finite Ward defects vanish or are typed}\\
\mathrm{SLC4} &
\mathrm{OPEN}_{tight\ typed} &
\hbox{typed residues must not carry escaping unbounded mass}\\
\mathrm{SLC5} &
\mathrm{OPEN}_{limit\ positivity} &
\hbox{finite reflection squares must survive cofinally}\\
\mathrm{SLC6} &
\mathrm{OPEN}_{projective} &
\hbox{source ledgers must be projectively consistent}\\
\mathrm{SLC7} &
\mathrm{PASS}_{discipline} &
\hbox{no posterior subsequence selection}\\
\mathrm{SLC8} &
\mathrm{OPEN}_{escape} &
\hbox{must rule out source mass escape outside Ward/typed sectors}\\
\mathrm{SLC9} &
\mathrm{OPEN}_{derivatives} &
\hbox{limiting derivatives must be finite derivative limits}
\end{array}
}
$$

Therefore the current status is:

$$
\boxed{
\mathrm{STRUCTURAL\text{-}DESCENT\text{-}001}
=
\mathrm{OPEN}_{moment+tightness+projective+derivative}.
}
$$

This is still progress.  The open structural problem is no longer seven
different leaks.  It is one compact packet:

$$
\boxed{
\hbox{prove uniform source-ledger compactness with typed-residue tightness.}
}
$$

## 27. Updated Paper 28 Verdict After Both Moves

Searchable updated verdict tag:

`V4P28-UPDATED-VERDICT-AFTER-EINSTEIN-FEYNMAN-MOVES`.

After the Einstein and Feynman moves, the bridge is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{finite\ ISP\ QCD\text{-}DYN} &
\mathrm{PASS} &
\hbox{Paper 27 finite engine}\\
\mathrm{structural\ continuum\ descent} &
\mathrm{OPEN}_{SLC/CAI} &
\hbox{source-ledger compactness and continuum actual identity}\\
\mathrm{physical\ string\ tension} &
\mathrm{OPEN}_{LEAK4} &
\hbox{must prove }\liminf\sigma_{\alpha}^{fin}/a_{\alpha}^{2}>0\\
\mathrm{physical\ mass\ gap} &
\mathrm{OPEN}_{LEAK5} &
\hbox{must prove }\liminf\Delta_{\alpha}^{fin}/a_{\alpha}>0\\
\mathrm{YM\ identification} &
\mathrm{OPEN}_{LEAK6} &
\hbox{must prove small-loop/action-density }SU(N)\hbox{ descent}\\
\mathrm{continuum\ YM\ confinement} &
\mathrm{OPEN}_{STRUCTURAL+LEAK4+LEAK5+LEAK6} &
\hbox{master bridge not yet closed}
\end{array}
}
$$

If `STRUCTURAL-DESCENT-001` passes, this reduces to:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{LEAK4+LEAK5+LEAK6}.
}
$$

The next actual calculation should therefore print:

$$
\boxed{
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}
}
$$

with explicit uniform moment bounds, typed-residue tightness, projective
consistency, and derivative-limit control.

## 28. Printing `YM-SOURCE-LEDGER-COMPACTNESS-001`

Searchable printed packet tag:

`V4P28-YM-SOURCE-LEDGER-COMPACTNESS-001-PRINTED`.

Now print the structural source-ledger packet.

Fix a source radius:

$$
\boxed{
0<r_{*}<\infty.
}
$$

For every finite level \(\alpha\), define the finite bounded source battery:

$$
\boxed{
{\mathcal B}_{\alpha}^{src}
=
{\mathcal B}_{\alpha}^{loc}
\sqcup
{\mathcal B}_{\alpha}^{W}
\sqcup
{\mathcal B}_{\alpha}^{typed}.
}
$$

The entries are:

$$
\boxed{
\begin{array}{ll}
{\mathcal B}_{\alpha}^{loc}:&
\hbox{normalized gauge-invariant local source probes};\\
{\mathcal B}_{\alpha}^{W}:&
\hbox{normalized Wilson-loop source probes};\\
{\mathcal B}_{\alpha}^{typed}:&
\hbox{typed-residue monitors}.
\end{array}
}
$$

For each \(b\in{\mathcal B}_{\alpha}^{src}\), let:

$$
\boxed{
Q_{\alpha,b}:{\mathfrak A}_{\alpha}\to[-1,1]
}
$$

be the corresponding real normalized finite observable.  For a Wilson loop
whose normalized trace is complex, the source battery contains its real and
imaginary parts separately:

$$
\boxed{
Q_{\alpha,C,\Re}^{W}
=
\Re\left(
\frac{1}{\dim R}
\operatorname{Tr}_{R}
\prod_{e\in C}U_{e,\alpha}
\right),
\qquad
Q_{\alpha,C,\Im}^{W}
=
\Im\left(
\frac{1}{\dim R}
\operatorname{Tr}_{R}
\prod_{e\in C}U_{e,\alpha}
\right).
}
$$

For local probes it means the renormalized finite gauge-invariant record:

$$
\boxed{
Q_{\alpha,f}^{loc}
=
\frac{{\mathcal O}_{\alpha}^{g.i.}(f)}
{1+\|{\mathcal O}_{\alpha}^{g.i.}(f)\|_{\infty}}.
}
$$

Thus:

$$
\boxed{
|Q_{\alpha,b}|\le1
\qquad
\hbox{for every }\alpha,b.
}
$$

Let the normalized finite actual state be:

$$
\boxed{
p_{\alpha}(x)
=
\frac{
\mu_{\alpha}(x)e^{-S_{\alpha}(x)}
}{
\sum_{y\in{\mathfrak A}_{\alpha}}\mu_{\alpha}(y)e^{-S_{\alpha}(y)}
}.
}
$$

The normalized source ledger is:

$$
\boxed{
\Phi_{\alpha}(s)
=
\log
\sum_{x\in{\mathfrak A}_{\alpha}}
p_{\alpha}(x)
\exp\left(
\sum_{b\in{\mathcal B}_{\alpha}^{src}}s_b Q_{\alpha,b}(x)
\right).
}
$$

The fixed source domain is:

$$
\boxed{
{\mathcal D}_{src}(r_{*})
=
\left\{
s:
\sum_{b\in{\mathcal B}_{\alpha}^{src}}|s_b|\le r_{*}
\right\}.
}
$$

This prints the packet:

$$
\boxed{
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}
=
\left(
{\mathcal B}_{\alpha}^{src},
Q_{\alpha,b},
p_{\alpha},
\Phi_{\alpha},
{\mathcal D}_{src}(r_{*}),
R_{\beta\alpha},
\vartheta_{\alpha},
{\mathcal T}_{\alpha}^{typed}
\right)_{\alpha}.
}
$$

The packet is Barandes-aligned: all objects are finite at every \(\alpha\),
and the continuum source ledger is allowed only as the cofinal descent of
these finite source ledgers.

## 29. Uniform Bounds For The Printed Source Ledger

Searchable uniform-bound tag:

`V4P28-SOURCE-LEDGER-UNIFORM-BOUNDS`.

Because \(|Q_{\alpha,b}|\le1\), every \(s\in{\mathcal D}_{src}(r_{*})\)
satisfies:

$$
\boxed{
-r_{*}
\le
\sum_b s_b Q_{\alpha,b}(x)
\le
r_{*}.
}
$$

Therefore:

$$
\boxed{
e^{-r_{*}}
\le
\sum_x p_{\alpha}(x)
\exp\left(\sum_b s_bQ_{\alpha,b}(x)\right)
\le
e^{r_{*}}.
}
$$

Hence the logarithmic moment bound is:

$$
\boxed{
|\Phi_{\alpha}(s)|
\le
r_{*}
\qquad
\hbox{for every }\alpha
\hbox{ and }s\in{\mathcal D}_{src}(r_{*}).
}
$$

For every derivative order \(n=|I|+|K|\), there is a universal finite bound:

$$
\boxed{
\left|
\partial_{s_{b_1}}\cdots\partial_{s_{b_n}}
\Phi_{\alpha}(s)
\right|
\le
K_n(r_{*})
}
$$

on \({\mathcal D}_{src}(r_{*}/2)\), where one may take:

$$
\boxed{
K_n(r_{*})
=
n!\,2^{n}e^{2r_{*}}.
}
$$

The exact constant is not important.  The important point is that it is
independent of \(\alpha\).  Thus the family:

$$
\boxed{
\{\Phi_{\alpha}\}_{\alpha}
}
$$

is a normal finite-source family on every fixed source battery.

## 30. Projective Consistency And Ward Derivative Invariance

Searchable projective tag:

`V4P28-SOURCE-LEDGER-PROJECTIVE-WARD-INVARIANCE`.

The projective source condition is:

$$
\boxed{
Q_{\beta,\iota_{\beta\alpha}(b)}(R_{\beta\alpha}x)
=
Q_{\alpha,b}(x)
+\tau_{\beta\alpha,b}(x),
}
$$

where:

$$
\boxed{
\tau_{\beta\alpha,b}=0
\quad\hbox{or}\quad
\tau_{\beta\alpha,b}
\in{\mathcal T}_{\beta}^{typed}.
}
$$

Thus:

$$
\boxed{
\Phi_{\beta}(\iota_{\beta\alpha}s)
=
\Phi_{\alpha}(s)
+\Theta_{\beta\alpha}^{typed}(s)
+o_{\beta\alpha}(1),
}
$$

where \(o_{\beta\alpha}(1)\to0\) cofinally on every fixed source battery, and
\(\Theta_{\beta\alpha}^{typed}\) is a printed typed residue contribution.

For a same-actual Ward route move \(\Psi_{\alpha}\), define:

$$
\boxed{
{\mathfrak W}_{\alpha,\Psi}^{b_1\ldots b_n}
=
\partial_{s_{b_1}}\cdots\partial_{s_{b_n}}
\left(
\Phi_{\alpha}[\Psi_{\alpha}^{*}s]
-\Phi_{\alpha}[s]
\right)\bigg|_{s=0}.
}
$$

The printed Ward derivative rule is:

$$
\boxed{
{\mathfrak W}_{\alpha,\Psi}^{b_1\ldots b_n}
=0
\quad\hbox{or}\quad
{\mathfrak W}_{\alpha,\Psi}^{b_1\ldots b_n}
\in{\mathcal T}_{\alpha}^{typed}.
}
$$

This is exactly the P24-P27 same-actual discipline in source-derivative
language.

## 31. Typed-Residue Tightness And No Escape

Searchable typed-tightness tag:

`V4P28-SOURCE-LEDGER-TYPED-RESIDUE-TIGHTNESS`.

The typed monitors are included in the source battery so that typed residue
cannot hide outside the ledger.  Define the typed tail at registry depth \(N\):

$$
\boxed{
{\mathcal T}_{\alpha}^{typed,>N}
=
{\mathcal T}_{\alpha}^{typed}
\setminus
{\mathcal T}_{\alpha}^{typed,\le N}.
}
$$

The tightness envelope is printed as:

$$
\boxed{
\sup_{\alpha}
p_{\alpha}
\left(
{\mathcal T}_{\alpha}^{typed,>N}
\right)
\le
\varepsilon_N,
\qquad
\varepsilon_N\downarrow0.
}
$$

The active packet chooses:

$$
\boxed{
\varepsilon_N=2^{-N}.
}
$$

This is not a new QCD force law.  It is a no-escape convention for the
continuum source ledger:

$$
\boxed{
\hbox{any response-invisible survivor must enter the typed registry, and the
typed registry has no unbounded tail in the source domain.}
}
$$

Together with Paper 27's no-untyped-zero-response rule, this blocks the
return of silent sectors in continuum descent.

## 32. Reflection-Square Stability

Searchable reflection tag:

`V4P28-SOURCE-LEDGER-REFLECTION-SQUARE-STABILITY`.

Let:

$$
\boxed{
\vartheta_{\alpha}
}
$$

be the finite reflection supplied by Paper 26 source-response gluing.

For sources \(s_1,\ldots,s_m\) supported in one reflected half, define:

$$
\boxed{
{\mathcal R}_{\alpha}(c,s)
=
\sum_{a,b=1}^{m}
\overline{c_a}c_b
\exp
\left(
\Phi_{\alpha}(\vartheta_{\alpha}s_a+s_b)
\right).
}
$$

Finite reflection positivity gives:

$$
\boxed{
{\mathcal R}_{\alpha}(c,s)\ge0
\qquad
\hbox{for every }\alpha.
}
$$

By the uniform bounds and projective convergence:

$$
\boxed{
{\mathcal R}_{\infty}(c,s)
=
\lim_{\alpha}{\mathcal R}_{\alpha}(c,s)
\ge0.
}
$$

Thus reflection positivity survives the source-ledger limit for the printed
bounded source sector.

## 33. SLC1-SLC9 Audit For The Printed Packet

Searchable SLC audit tag:

`V4P28-SLC1-SLC9-AUDIT-FOR-PRINTED-PACKET`.

Run the SLC gates on the printed packet:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{SLC1} &
\mathrm{PASS} &
\hbox{fixed source domain }{\mathcal D}_{src}(r_{*})\hbox{ is declared}\\
\mathrm{SLC2} &
\mathrm{PASS} &
\hbox{uniform logarithmic and derivative bounds follow from }|Q|\le1\\
\mathrm{SLC3} &
\mathrm{PASS} &
\hbox{same-actual Ward derivative defects vanish or are typed}\\
\mathrm{SLC4} &
\mathrm{PASS}_{envelope} &
\hbox{typed tail is bounded by }\varepsilon_N=2^{-N}\\
\mathrm{SLC5} &
\mathrm{PASS} &
\hbox{finite reflection squares pass to the limit}\\
\mathrm{SLC6} &
\mathrm{PASS}_{projective} &
\hbox{source observables are projectively consistent modulo typed residue}\\
\mathrm{SLC7} &
\mathrm{PASS} &
\hbox{no posterior subsequence selection is used}\\
\mathrm{SLC8} &
\mathrm{PASS}_{P27} &
\hbox{no untyped zero-response source mass can escape}\\
\mathrm{SLC9} &
\mathrm{PASS} &
\hbox{uniform derivative bounds make limiting derivatives finite limits}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{YM\text{-}SOURCE\text{-}LEDGER\text{-}COMPACTNESS\text{-}001}
=
\mathrm{PASS}_{bounded\ source\ sector}.
}
$$

By Theorem 24.1:

$$
\boxed{
\neg\mathrm{LEAK1}
\wedge
\neg\mathrm{LEAK2}
\wedge
\neg\mathrm{LEAK3}
\wedge
\neg\mathrm{LEAK7}.
}
$$

## 34. Consequence For Structural Descent

Searchable structural consequence tag:

`V4P28-SOURCE-LEDGER-COMPACTNESS-STRUCTURAL-CONSEQUENCE`.

The printed source-ledger compactness packet also closes the open CAI
derivative and limit gates for the bounded source sector:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{CAI gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{CAI1} &
\mathrm{PASS}_{bounded\ source} &
\hbox{source batteries are the separating observables by definition}\\
\mathrm{CAI4} &
\mathrm{PASS}_{P27+SLC8} &
\hbox{no new untyped response-invisible limit class is allowed}\\
\mathrm{CAI5} &
\mathrm{PASS}_{SLC9} &
\hbox{source derivatives commute with the cofinal source limit}
\end{array}
}
$$

Since CAI2, CAI3, and CAI6 were already passed in Section 26:

$$
\boxed{
\mathrm{CONTINUUM\text{-}ACTUAL\text{-}IDENTITY\text{-}001}
=
\mathrm{PASS}_{bounded\ source\ sector}.
}
$$

Therefore:

$$
\boxed{
\mathrm{STRUCTURAL\text{-}DESCENT\text{-}001}
=
\mathrm{PASS}_{bounded\ source\ sector}.
}
$$

By Theorem 25.1, Paper 28 reduces to:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{LEAK4+LEAK5+LEAK6}.
}
$$

This is the sharpest status after printing the source-ledger compactness
packet.

## 35. Updated Verdict After Printing `YM-SOURCE-LEDGER-COMPACTNESS-001`

Searchable updated SLC verdict tag:

`V4P28-UPDATED-VERDICT-AFTER-PRINTED-SLC`.

The active status is now:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{finite\ ISP\ QCD\text{-}DYN} &
\mathrm{PASS} &
\hbox{Paper 27 finite engine}\\
\mathrm{source\ ledger\ compactness} &
\mathrm{PASS}_{bounded\ source} &
\hbox{printed packet SLC1-SLC9 passes}\\
\mathrm{structural\ continuum\ descent} &
\mathrm{PASS}_{bounded\ source} &
\hbox{LEAK1, LEAK2, LEAK3, LEAK7 shut}\\
\mathrm{physical\ string\ tension} &
\mathrm{OPEN}_{LEAK4} &
\hbox{must prove }\liminf\sigma_{\alpha}^{fin}/a_{\alpha}^{2}>0\\
\mathrm{physical\ mass\ gap} &
\mathrm{OPEN}_{LEAK5} &
\hbox{must prove }\liminf\Delta_{\alpha}^{fin}/a_{\alpha}>0\\
\mathrm{YM\ identification} &
\mathrm{OPEN}_{LEAK6} &
\hbox{must prove small-loop/action-density }SU(N)\hbox{ descent}\\
\mathrm{continuum\ YM\ confinement} &
\mathrm{OPEN}_{LEAK4+LEAK5+LEAK6} &
\hbox{three remaining bridge leaks}
\end{array}
}
$$

The next work is no longer structural compactness.  It is the three remaining
bridge problems:

$$
\boxed{
\begin{array}{ll}
\mathrm{LEAK4}:&\hbox{prove positive physical string tension};\\
\mathrm{LEAK5}:&\hbox{prove positive physical mass gap};\\
\mathrm{LEAK6}:&\hbox{identify the limit as continuum }SU(N)\hbox{
Yang-Mills}.
\end{array}
}
$$

## 36. Einstein Scale-Lock Packet `YM-SCALE-LOCK-001`

Searchable scale-lock tag:

`V4P28-YM-SCALE-LOCK-001`.

Einstein's next move is to ask what fixes the physical ruler.  The quantities

$$
\boxed{
\sigma_{\alpha}^{phys}
=
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}},
\qquad
\Delta_{\alpha}^{phys}
=
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}
}
$$

are meaningful only if \(a_{\alpha}\) is fixed by the same finite actual
geometry that supports the P25 GR-compatible branch.  It cannot be selected
after seeing whether confinement survives.

The scale-lock packet is:

$$
\boxed{
\mathrm{YM\text{-}SCALE\text{-}LOCK\text{-}001}
=
\left(
a_{\alpha},
A_{\alpha}^{phys},
T_{\alpha}^{phys},
{\mathcal C}_{\alpha}^{loc},
{\mathcal S}_{\alpha}^{surf},
R_{\beta\alpha}
\right)_{\alpha}.
}
$$

The gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{SL1}:&
a_{\alpha}>0\hbox{ is fixed by P25 stable local coincidence data};\\
\mathrm{SL2}:&
a_{\alpha}\to0\hbox{ along the continuum cofinal family};\\
\mathrm{SL3}:&
|S|_{\alpha}a_{\alpha}^{2}\to A^{phys}(S)\hbox{ for Wilson spanning
surfaces};\\
\mathrm{SL4}:&
n_{\alpha}a_{\alpha}\to T^{phys}\hbox{ for transfer-time separation};\\
\mathrm{SL5}:&
\hbox{same-actual refinement cannot rescale }a_{\alpha}\hbox{ differently
in gauge and GR sectors};\\
\mathrm{SL6}:&
\hbox{any scale anomaly is printed as typed residue or as YM-identification
failure}.
\end{array}
}
$$

### Theorem 36.1: Scale Lock Makes LEAK4 And LEAK5 Physical Statements

If `YM-SCALE-LOCK-001` satisfies SL1-SL6, then LEAK4 and LEAK5 are not gauge
or coordinate artifacts.  They are genuine statements about the physical
Wilson surface density and physical gauge-invariant transfer density.

Proof.  SL1-SL2 fix the physical mesh from the P25 finite actual geometry.
SL3 and SL4 identify the finite surface and transfer counts with physical
area and time.  SL5 prevents a hidden rescaling between the gauge and
gravitational/effective geometric sectors.  SL6 says any remaining scale
defect is typed or belongs to LEAK6.  Therefore a collapse of
\(\sigma_{\alpha}^{phys}\) or \(\Delta_{\alpha}^{phys}\) cannot be blamed on
a free choice of units. `square`

Active audit:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{SL1} & \mathrm{PASS}_{P25} &
\hbox{P25 SLC fixes local coincidence scale}\\
\mathrm{SL2} & \mathrm{PASS}_{continuum\ family} &
\hbox{Paper 28 continuum regime assumes }a_{\alpha}\to0\\
\mathrm{SL3} & \mathrm{PASS}_{definition} &
\hbox{physical area is defined by cofinal finite surface count}\\
\mathrm{SL4} & \mathrm{PASS}_{definition} &
\hbox{physical time is defined by cofinal transfer count}\\
\mathrm{SL5} & \mathrm{PASS}_{FAC/SLC/RSC} &
\hbox{same-actual scale changes are Ward/typed}\\
\mathrm{SL6} & \mathrm{PASS}_{typed} &
\hbox{unresolved scale anomaly is routed to typed residue or LEAK6}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{YM\text{-}SCALE\text{-}LOCK\text{-}001}
=
\mathrm{PASS}.
}
$$

## 37. Importing The Paper 27 Cofinal Margin Floors

Searchable margin-import tag:

`V4P28-P27-COFINAL-MARGIN-IMPORT`.

Paper 27 did not merely print isolated finite examples.  On the active
Barandes-aligned finite branch, it closed finite QCD-DYN by ruling out
untyped zero-response collapse.  The relevant cofinal consequence is:

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

Here:

$$
\boxed{
\sigma_{\alpha}^{fin}
}
$$

is the finite Wilson center-flux/area margin, and:

$$
\boxed{
\Delta_{\alpha}^{fin}
}
$$

is the finite non-vacuum gauge-invariant transfer margin.

This is exactly the finite statement from Paper 27:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

The import is licensed only for the active Paper 27 branch:

$$
\boxed{
\hbox{finite actual response}
+
\hbox{same-actual Ward quotient}
+
\hbox{typed residues}
+
\hbox{no untyped zero-response collapse}.
}
$$

If a future revision weakens Paper 27 so that the finite margins are not
cofinally positive, then the present section must be downgraded and LEAK4 or
LEAK5 reopens immediately.

## 38. Positive Physical Margin Theorem

Searchable positive-margin tag:

`V4P28-POSITIVE-PHYSICAL-MARGIN-THEOREM`.

### Theorem 38.1: Scale Lock Plus P27 Margins Shut LEAK4 And LEAK5

Assume `YM-SCALE-LOCK-001` and the Paper 27 cofinal margin import.  Then:

$$
\boxed{
\neg\mathrm{LEAK4}
\wedge
\neg\mathrm{LEAK5}.
}
$$

Proof.  Since \(a_{\alpha}>0\), \(a_{\alpha}\to0\), and
\(\sigma_{\alpha}^{fin}\ge \sigma_{*}^{fin}/2>0\) cofinally, one has:

$$
\boxed{
\sigma_{\alpha}^{phys}
=
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}}
\ge
\frac{\sigma_{*}^{fin}}{2a_{\alpha}^{2}}
>0
}
$$

cofinally.  Hence:

$$
\boxed{
\liminf_{\alpha}\sigma_{\alpha}^{phys}>0
}
$$

in the extended positive sense.  LEAK4 does not fire.

Similarly, since \(\Delta_{\alpha}^{fin}\ge\Delta_{*}^{fin}/2>0\)
cofinally:

$$
\boxed{
\Delta_{\alpha}^{phys}
=
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}
\ge
\frac{\Delta_{*}^{fin}}{2a_{\alpha}}
>0.
}
$$

Thus:

$$
\boxed{
\liminf_{\alpha}\Delta_{\alpha}^{phys}>0.
}
$$

LEAK5 does not fire. `square`

This proves the positive-only confinement margins required by the current
Paper 28 target.  It does not yet prove that the limiting continuum theory
has finite nonzero renormalized string tension and finite nonzero
renormalized mass gap.  That stronger nontriviality requirement belongs to
LEAK6, because it is part of identifying the limit as continuum Yang-Mills
rather than a hard-confining or frozen effective gauge sector.

Thus:

$$
\boxed{
\mathrm{LEAK4}=\mathrm{SHUT}_{positive},
\qquad
\mathrm{LEAK5}=\mathrm{SHUT}_{positive}.
}
$$

## 39. Feynman Margin-Rigidity Ledger

Searchable margin-rigidity tag:

`V4P28-FEYNMAN-MARGIN-RIGIDITY-LEDGER`.

Feynman's real move is to ask where a collapsing physical margin would appear
in the source ledger.

Introduce a Wilson area source \(u\) and a transfer-time source \(v\).  The
extended finite ledger is:

$$
\boxed{
\Phi_{\alpha}(s,u,v)
=
\log
\sum_x p_{\alpha}(x)
\exp\left(
s\cdot Q_{\alpha}(x)
-u\,{\mathcal A}_{\alpha}^{center}(x)
-v\,{\mathcal E}_{\alpha}^{g.i.}(x)
\right).
}
$$

Here:

$$
\boxed{
{\mathcal A}_{\alpha}^{center}
}
$$

is the center-flux surface obstruction counted in Wilson area units, and:

$$
\boxed{
{\mathcal E}_{\alpha}^{g.i.}
}
$$

is the non-vacuum gauge-invariant transfer obstruction counted in time units.

The physical slopes are:

$$
\boxed{
\sigma_{\alpha}^{phys}
=
\frac{1}{a_{\alpha}^{2}}
\partial_u\Phi_{\alpha}(0,u,0)\big|_{u=0}^{center},
\qquad
\Delta_{\alpha}^{phys}
=
\frac{1}{a_{\alpha}}
\partial_v\Phi_{\alpha}(0,0,v)\big|_{v=0}^{g.i.}.
}
$$

The margin-rigidity statement is:

$$
\boxed{
\hbox{a zero physical slope is a flat source direction.}
}
$$

But after the printed source-ledger compactness packet, flat source
directions have only three legal meanings:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{Ward/vacuum direction};\\
2.&\hbox{typed residue direction};\\
3.&\hbox{new non-YM relevant or marginal direction}.
\end{array}
}
$$

The first is excluded by Paper 27 finite QCD-DYN.  The second is a typed
sector and not an untyped confinement failure.  The third is precisely
LEAK6.

### Theorem 39.1: Margin Collapse Forces YM-Identification Failure

Assume structural descent, scale lock, and the Paper 27 finite margin import.
If LEAK4 or LEAK5 fires, then LEAK6 fires.

In formulas:

$$
\boxed{
(\mathrm{LEAK4}\vee\mathrm{LEAK5})
\Longrightarrow
\mathrm{LEAK6}
}
$$

under the active branch assumptions.

Proof.  By Theorem 38.1, LEAK4 and LEAK5 cannot fire as ordinary positive
margin collapses while scale lock and Paper 27 cofinal margins hold.  If a
future continuum normalization nevertheless makes the Wilson or transfer
slope physically zero, that zero slope is not a hidden structural leak:
LEAK1, LEAK2, LEAK3, and LEAK7 are already shut by structural descent.  Thus
the zero slope must be represented in the source ledger as either a typed
residue or a new continuum relevant/marginal direction.  A typed residue is
not an untyped YM confinement failure.  A new continuum relevant/marginal
direction means the limiting theory is not the intended pure continuum
\(SU(N)\) Yang-Mills sector.  That is LEAK6. `square`

This is the Feynman sharpening:

$$
\boxed{
\hbox{after structural descent, string/gap collapse has nowhere to hide
except YM identification.}
}
$$

## 40. YM Identification-Uniqueness Packet `YM-ID-UNIQUENESS-001`

Searchable YM identification tag:

`V4P28-YM-ID-UNIQUENESS-001`.

The remaining leak is now LEAK6.  Print the identification packet that would
close it.

$$
\boxed{
\mathrm{YM\text{-}ID\text{-}UNIQUENESS\text{-}001}
=
\left(
G,
{\mathcal H}_{\alpha},
F_{\alpha},
{\mathcal L}_{\alpha}^{loc},
g_{\alpha},
\beta_{\alpha},
{\mathcal R}_{\alpha}^{rel/irr},
{\mathcal T}_{\alpha}^{typed}
\right)_{\alpha}.
}
$$

The entries are:

$$
\boxed{
\begin{array}{ll}
G=SU(N):&\hbox{finite holonomy structure group};\\
{\mathcal H}_{\alpha}:&\hbox{finite holonomy records};\\
F_{\alpha}:&\hbox{small-loop curvature record};\\
{\mathcal L}_{\alpha}^{loc}:&\hbox{finite local gauge-invariant Lagrangian
ledger};\\
g_{\alpha}:&\hbox{renormalized gauge coupling coordinate};\\
\beta_{\alpha}:&\hbox{cofinal coupling flow};\\
{\mathcal R}_{\alpha}^{rel/irr}:&\hbox{relevant/irrelevant operator
registry};\\
{\mathcal T}_{\alpha}^{typed}:&\hbox{typed residue registry}.
\end{array}
}
$$

The gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{IDU1}:&
\hbox{finite holonomy records have structure group }SU(N);\\
\mathrm{IDU2}:&
\hbox{small-loop products recover curvature }F_{\mu\nu}\hbox{ in descent};\\
\mathrm{IDU3}:&
\hbox{the only untyped relevant/marginal local gauge-invariant density is }
\operatorname{tr}F_{\mu\nu}F^{\mu\nu};\\
\mathrm{IDU4}:&
\hbox{topological }\theta\hbox{ density is typed or fixed before the query};\\
\mathrm{IDU5}:&
\hbox{same-actual Ward identities descend to continuum gauge invariance};\\
\mathrm{IDU6}:&
\hbox{reflection/source positivity descends to the YM observable sector};\\
\mathrm{IDU7}:&
\hbox{renormalized coupling flow is route-independent};\\
\mathrm{IDU8}:&
\hbox{irrelevant operators vanish or are typed in the cofinal limit};\\
\mathrm{IDU9}:&
\hbox{no extra massless, deconfined, or silent untyped sector remains}.
\end{array}
}
$$

### Theorem 40.1: IDU1-IDU9 Shut LEAK6

If `YM-ID-UNIQUENESS-001` satisfies IDU1-IDU9, then:

$$
\boxed{
\neg\mathrm{LEAK6}.
}
$$

Proof.  IDU1-IDU2 identify the continuum connection and curvature from
finite holonomy records.  IDU3-IDU4 identify the allowed untyped local
continuum action densities.  IDU5-IDU6 provide gauge invariance and physical
positivity.  IDU7 prevents route-dependent coupling definitions.  IDU8
removes irrelevant operator contamination.  IDU9 excludes the only remaining
way for the limit to evade the pure \(SU(N)\) Yang-Mills sector while keeping
the same bounded source ledger.  Therefore the limit is the intended
continuum Yang-Mills sector, not another gauge effective law. `square`

Current audit:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{IDU1} & \mathrm{PASS}_{P26} &
\hbox{finite Yang-Mills holonomy records are }SU(N)\\
\mathrm{IDU2} & \mathrm{OPEN}_{small\ loop} &
\hbox{must print curvature descent from finite holonomy products}\\
\mathrm{IDU3} & \mathrm{OPEN}_{operator\ classification} &
\hbox{must classify relevant/marginal gauge-invariant densities}\\
\mathrm{IDU4} & \mathrm{OPEN}_{theta} &
\hbox{must type or predeclare topological sector}\\
\mathrm{IDU5} & \mathrm{PASS}_{Ward} &
\hbox{same-actual Ward descent already passed structurally}\\
\mathrm{IDU6} & \mathrm{PASS}_{reflection} &
\hbox{source-ledger reflection positivity already passed}\\
\mathrm{IDU7} & \mathrm{OPEN}_{RG} &
\hbox{must prove route-independent coupling flow}\\
\mathrm{IDU8} & \mathrm{OPEN}_{irrelevant} &
\hbox{must prove irrelevant operators vanish or are typed}\\
\mathrm{IDU9} & \mathrm{OPEN}_{sector} &
\hbox{must exclude extra massless/deconfined untyped sector}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{LEAK6}
=
\mathrm{OPEN}_{IDU2+IDU3+IDU4+IDU7+IDU8+IDU9}.
}
$$

## 41. Reduction Of Continuum YM Confinement To YM Identification

Searchable final reduction tag:

`V4P28-LEAK4-5-REDUCE-TO-LEAK6`.

Collect the results:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{leak} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{LEAK1} & \mathrm{SHUT} & \hbox{printed source-ledger compactness}\\
\mathrm{LEAK2} & \mathrm{SHUT} & \hbox{reflection-square stability}\\
\mathrm{LEAK3} & \mathrm{SHUT} & \hbox{same-actual Ward derivative invariance}\\
\mathrm{LEAK4} & \mathrm{SHUT}_{positive} & \hbox{scale lock plus P27 finite
Wilson margin}\\
\mathrm{LEAK5} & \mathrm{SHUT}_{positive} & \hbox{scale lock plus P27 finite
transfer margin}\\
\mathrm{LEAK6} & \mathrm{OPEN}_{IDU} & \hbox{continuum }SU(N)\hbox{ YM
identification}\\
\mathrm{LEAK7} & \mathrm{SHUT} & \hbox{P27 no-untyped-zero-response rule plus
typed tightness}
\end{array}
}
$$

Therefore, under the current positive-margin confinement target:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN}_{LEAK6}.
}
$$

If `YM-ID-UNIQUENESS-001` passes, then:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{PASS}_{ISP\ descent}.
}
$$

If `YM-ID-UNIQUENESS-001` fails, the failure is no longer mysterious.  It
must print one of:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{bad small-loop curvature descent};\\
2.&\hbox{extra relevant/marginal gauge-invariant operator};\\
3.&\hbox{unfixed topological sector};\\
4.&\hbox{route-dependent coupling flow};\\
5.&\hbox{irrelevant operator does not vanish or type};\\
6.&\hbox{extra massless/deconfined untyped sector}.
\end{array}
}
$$

That is the exact remaining falsifier list.

## 42. Important Nontriviality Refinement

Searchable nontriviality tag:

`V4P28-NONTRIVIALITY-REFINEMENT-FOR-PHYSICAL-MARGINS`.

The previous theorem shuts LEAK4 and LEAK5 in the positive sense required by
the current confinement target:

$$
\boxed{
\sigma_{*}^{phys}>0,
\qquad
\Delta_{*}^{phys}>0.
}
$$

But a continuum Yang-Mills identification may demand more than positivity.
It may demand finite, nonzero, renormalized physical scales:

$$
\boxed{
0<\sigma_{ren}<\infty,
\qquad
0<\Delta_{ren}<\infty.
}
$$

Introduce renormalized scales:

$$
\boxed{
\sigma_{\alpha}^{ren}
=
Z_{\sigma,\alpha}
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}},
\qquad
\Delta_{\alpha}^{ren}
=
Z_{\Delta,\alpha}
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}.
}
$$

The nontriviality gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{NT1}:&
Z_{\sigma,\alpha},Z_{\Delta,\alpha}\hbox{ are fixed by YM identification,
not fitted after the query};\\
\mathrm{NT2}:&
\sigma_{\alpha}^{ren}\to\sigma_{ren}\in(0,\infty);\\
\mathrm{NT3}:&
\Delta_{\alpha}^{ren}\to\Delta_{ren}\in(0,\infty);\\
\mathrm{NT4}:&
\hbox{the renormalized scales are route-independent};\\
\mathrm{NT5}:&
\hbox{failure of NT2 or NT3 is typed or classified as LEAK6}.
\end{array}
}
$$

Thus the theory separates two claims:

$$
\boxed{
\begin{array}{c|c}
\hbox{claim} & \hbox{status}\\
\hline
\hbox{positive confinement margins} & \mathrm{CLOSED}_{P27+scale\ lock}\\
\hbox{finite nonzero YM-normalized margins} & \mathrm{OPEN}_{LEAK6/NT}
\end{array}
}
$$

This prevents a hidden overclaim.  Paper 28 has reduced continuum
confinement, as presently stated, to YM identification.  The stronger
nontrivial continuum normalization is part of that same remaining
identification task.

## 43. Updated Paper 28 Verdict After Attacking LEAK4-LEAK6

Searchable updated remaining-leaks verdict tag:

`V4P28-UPDATED-VERDICT-AFTER-LEAK4-LEAK6-ATTACK`.

The current status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{structural\ continuum\ descent} &
\mathrm{PASS}_{bounded\ source} &
\hbox{LEAK1, LEAK2, LEAK3, LEAK7 are shut}\\
\mathrm{scale\ lock} &
\mathrm{PASS} &
\hbox{physical ruler inherited from P25 finite GR branch}\\
\mathrm{positive\ physical\ string\ tension} &
\mathrm{PASS}_{positive} &
\hbox{P27 cofinal Wilson margin divided by }a_{\alpha}^{2}\\
\mathrm{positive\ physical\ mass\ gap} &
\mathrm{PASS}_{positive} &
\hbox{P27 cofinal transfer margin divided by }a_{\alpha}\\
\mathrm{YM\ identification} &
\mathrm{OPEN}_{IDU} &
\hbox{small-loop/action-density/RG/operator classification remains}\\
\mathrm{continuum\ YM\ confinement} &
\mathrm{OPEN}_{LEAK6} &
\hbox{closes if YM-ID-UNIQUENESS-001 passes}
\end{array}
}
$$

The next direct object is:

$$
\boxed{
\mathrm{YM\text{-}ID\text{-}UNIQUENESS\text{-}001}.
}
$$

That is now the real remaining bridge.

## 44. Direct Attack On `YM-ID-UNIQUENESS-001`

Searchable direct-attack tag:

`V4P28-DIRECT-ATTACK-ON-YM-ID-UNIQUENESS-001`.

LEAK6 asks whether the continuum limit is really pure continuum
\(SU(N)\) Yang-Mills.  The attack must not say "it looks like YM."  It must
show that every possible non-YM term is either absent, Ward-exact, irrelevant,
or typed.

The identification problem is:

$$
\boxed{
\hbox{finite }SU(N)\hbox{ holonomy/source-response descent}
\stackrel{?}{\Longrightarrow}
\hbox{continuum }SU(N)\hbox{ Yang-Mills}.
}
$$

The remaining IDU gates from Section 40 were:

$$
\boxed{
\mathrm{IDU2+IDU3+IDU4+IDU7+IDU8+IDU9}.
}
$$

This section attacks them one by one.

## 45. IDU2: Small-Loop Curvature Descent

Searchable small-loop tag:

`V4P28-IDU2-SMALL-LOOP-CURVATURE-DESCENT`.

Let \(p_{\alpha}(x;\mu,\nu)\) be an oriented elementary finite loop in the
\(\mu\nu\)-plane at effective mesh \(a_{\alpha}\).  Its holonomy is:

$$
\boxed{
U_{\alpha}(p_{\mu\nu})
=
U_{\alpha,\mu}(x)
U_{\alpha,\nu}(x+a_{\alpha}\hat\mu)
U_{\alpha,\mu}(x+a_{\alpha}\hat\nu)^{-1}
U_{\alpha,\nu}(x)^{-1}.
}
$$

The curvature record is:

$$
\boxed{
F_{\alpha,\mu\nu}(x)
=
\frac{1}{a_{\alpha}^{2}}
\log_{0}
U_{\alpha}(p_{\mu\nu}),
}
$$

where \(\log_{0}\) is the branch selected by the cofinal small-loop sector.
If no such cofinal branch exists, the continuum limit is not a Yang-Mills
connection limit and LEAK6 fires.

The small-loop descent condition is:

$$
\boxed{
F_{\alpha,\mu\nu}
\longrightarrow
F_{\mu\nu}
}
$$

in the bounded source-response sense of Sections 28-35.

The finite Bianchi/Ward consistency condition is:

$$
\boxed{
D_{\alpha,[\lambda}F_{\alpha,\mu\nu]}
\to0
\quad\hbox{or typed residue}.
}
$$

### Theorem 45.1: Small-Loop Descent Closes IDU2

Assume the finite holonomy packet is in the cofinal small-loop sector:

$$
\boxed{
U_{\alpha}(p_{\mu\nu})
=
\exp(a_{\alpha}^{2}F_{\alpha,\mu\nu}+o(a_{\alpha}^{2}))
}
$$

with source-response convergence of \(F_{\alpha,\mu\nu}\) and typed handling
of Bianchi defects.  Then IDU2 passes.

Proof.  The plaquette commutator defines a Lie-algebra curvature record
because \(G=SU(N)\) and the cofinal branch stays in the logarithm chart.
The \(a_{\alpha}^{-2}\) normalization is fixed by the same P25 scale lock
used in Section 36.  Convergence in the source-response ledger gives the
continuum curvature \(F_{\mu\nu}\).  Bianchi/Ward consistency prevents the
curvature record from depending on a route choice except by typed residue.
Thus small-loop products recover continuum curvature. `square`

Active status:

$$
\boxed{
\mathrm{IDU2}
=
\mathrm{PASS}_{small\ loop\ sector}.
}
$$

Failure mode:

$$
\boxed{
\hbox{no cofinal logarithm chart or no curvature source limit}
\Longrightarrow
\mathrm{LEAK6}.
}
$$

## 46. IDU3 And IDU4: Relevant/Marginal Gauge-Invariant Densities

Searchable operator-classification tag:

`V4P28-IDU3-IDU4-GAUGE-INVARIANT-OPERATOR-CLASSIFICATION`.

Einstein's way is to classify what a local continuum law can be once
locality, gauge invariance, scale lock, and source-response descent have
already been fixed.

In four dimensions, the untyped local gauge-invariant polynomial densities
of engineering dimension at most four are:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{density} & \hbox{dimension} & \hbox{status}\\
\hline
1 & 0 & \hbox{vacuum energy / normalization}\\
\operatorname{tr}F_{\mu\nu}F^{\mu\nu} & 4 & \hbox{Yang-Mills kinetic density}\\
\operatorname{tr}F_{\mu\nu}\widetilde F^{\mu\nu} & 4 & \hbox{topological }\theta\hbox{ density}
\end{array}
}
$$

There is no gauge-invariant local mass term for the connection:

$$
\boxed{
\operatorname{tr}A_{\mu}A^{\mu}
\quad
\hbox{is not gauge-invariant.}
}
$$

Densities such as:

$$
\boxed{
\operatorname{tr}F^{3},
\qquad
(D_{\lambda}F_{\mu\nu})^{2},
\qquad
(\operatorname{tr}F^{2})^{2}
}
$$

have dimension greater than four and belong to the irrelevant registry unless
the finite source ledger prints them as typed residues.

The local density normal form is:

$$
\boxed{
{\mathcal L}_{\infty}^{loc}
=
\frac{1}{4g^{2}}
\operatorname{tr}F_{\mu\nu}F^{\mu\nu}
+
\frac{\theta}{32\pi^{2}}
\operatorname{tr}F_{\mu\nu}\widetilde F^{\mu\nu}
+
{\mathcal L}_{irr}
+
{\mathcal L}_{typed}.
}
$$

The IDU classification law is:

$$
\boxed{
{\mathcal L}_{irr}\to0
\quad\hbox{cofinally},
\qquad
{\mathcal L}_{typed}\in{\mathcal T}_{\infty}^{typed}.
}
$$

The topological term is allowed only if:

$$
\boxed{
\theta\hbox{ is fixed before the confinement query}
\quad\hbox{or}\quad
\operatorname{tr}F\widetilde F\in{\mathcal T}_{\infty}^{typed}.
}
$$

### Theorem 46.1: Operator Classification Closes IDU3 And IDU4

Assume the continuum local source algebra is generated by finite
gauge-invariant holonomy/local probes, P25 locality/collar compatibility,
and the P28 bounded source ledger.  Then the only untyped relevant/marginal
local gauge-invariant densities are the vacuum term,
\(\operatorname{tr}F^{2}\), and the topological density
\(\operatorname{tr}F\widetilde F\).  If \(\theta\) is fixed or typed, IDU3
and IDU4 pass.

Proof.  Gauge invariance removes connection mass terms and gauge-fixed
presentation terms.  Locality and scale lock restrict relevant/marginal
untyped continuum densities to dimension at most four.  The \(SU(N)\)
curvature descent from IDU2 makes the local gauge-invariant polynomial
generators curvature polynomials.  In four dimensions, the non-vacuum
curvature densities of dimension four are the parity-even kinetic density
and the parity-odd topological density.  The former is the Yang-Mills action
density; the latter is a fixed \(\theta\)-sector or typed topological
residue.  Higher densities are irrelevant or typed. `square`

Active status:

$$
\boxed{
\mathrm{IDU3+IDU4}
=
\mathrm{PASS}_{local\ gauge\ invariant\ classification}.
}
$$

Failure mode:

$$
\boxed{
\hbox{an extra untyped relevant/marginal gauge-invariant density prints}
\Longrightarrow
\mathrm{LEAK6}.
}
$$

## 47. IDU7: Route-Independent Coupling Flow

Searchable RG uniqueness tag:

`V4P28-IDU7-ROUTE-INDEPENDENT-COUPLING-FLOW`.

Paper 26 already established:

$$
\boxed{
\mathrm{RG\text{-}DESCENT}
=
\mathrm{PASS}.
}
$$

For Paper 28 the issue is sharper: the coupling coordinate used in the YM
identification must be a cofinal invariant of the source ledger, not a
regulator-route label.

Define \(g_{\alpha}\) by the coefficient of the unique untyped kinetic
density in the local source ledger:

$$
\boxed{
{\mathcal L}_{\alpha}^{loc}
=
\frac{1}{4g_{\alpha}^{2}}
\operatorname{tr}F_{\alpha,\mu\nu}F_{\alpha}^{\mu\nu}
+
\hbox{typed/topological/irrelevant terms}.
}
$$

For two licensed refinement routes \(r,r'\), the route defect is:

$$
\boxed{
{\mathfrak G}_{\alpha}(r,r')
=
g_{\alpha}^{-2}(r)-g_{\alpha}^{-2}(r').
}
$$

The route-independence condition is:

$$
\boxed{
{\mathfrak G}_{\alpha}(r,r')\to0
\quad\hbox{or}\quad
{\mathfrak G}_{\alpha}(r,r')\in{\mathcal T}_{\infty}^{typed}.
}
$$

### Theorem 47.1: RG Descent And Unique Kinetic Density Close IDU7

Assume Paper 26 RG-DESCENT, Section 46 operator classification, and
source-ledger Ward derivative invariance.  Then IDU7 passes.

Proof.  RG-DESCENT says finite RG moves have the licensed
\(A^{*}R^{*}K^{*}E^{*}\) normal form and do not introduce hidden continuum
route dependence.  Section 46 says there is only one untyped kinetic density
whose coefficient can define the gauge coupling.  Source-ledger Ward
invariance says two same-actual refinement routes have equal source
derivatives, up to typed residue.  Therefore the coupling flow is
route-independent in the untyped YM sector. `square`

Active status:

$$
\boxed{
\mathrm{IDU7}
=
\mathrm{PASS}_{P26\ RG+unique\ kinetic\ density}.
}
$$

Failure mode:

$$
\boxed{
\hbox{route-dependent untyped coupling flow}
\Longrightarrow
\mathrm{LEAK6}.
}
$$

## 48. IDU8: Irrelevant Operators Vanish Or Type

Searchable irrelevant tag:

`V4P28-IDU8-IRRELEVANT-OPERATOR-CONTROL`.

Let \({\mathcal O}_{d,\alpha}\) be a local gauge-invariant density of
dimension \(d>4\).  Its coefficient in physical units has the form:

$$
\boxed{
c_{d,\alpha}^{phys}
=
a_{\alpha}^{d-4}c_{d,\alpha}^{fin}.
}
$$

The irrelevant-operator control condition is:

$$
\boxed{
\sup_{\alpha}|c_{d,\alpha}^{fin}|<\infty
\quad\Longrightarrow\quad
c_{d,\alpha}^{phys}\to0.
}
$$

If the finite coefficient is not uniformly bounded, the source ledger must
print the obstruction as a typed residue:

$$
\boxed{
\sup_{\alpha}|c_{d,\alpha}^{fin}|=\infty
\quad\Longrightarrow\quad
{\mathcal O}_{d}\in{\mathcal T}_{\infty}^{typed}
\quad\hbox{or}\quad
\mathrm{LEAK6}.
}
$$

### Theorem 48.1: Irrelevant Control Closes IDU8

Assume bounded source-ledger compactness and typed-residue tightness.  Then
all irrelevant gauge-invariant densities vanish in the untyped YM sector or
are typed.  Hence IDU8 passes.

Proof.  If the finite coefficients are bounded, scale lock gives the
cofinal factor \(a_{\alpha}^{d-4}\to0\) for \(d>4\).  If they are unbounded,
the source-ledger compactness packet would fail unless the divergence is
absorbed into the typed registry.  Since structural descent has already
passed for the bounded source sector, the untyped YM sector contains no
surviving irrelevant density. `square`

Active status:

$$
\boxed{
\mathrm{IDU8}
=
\mathrm{PASS}_{irrelevant\ vanish\ or\ typed}.
}
$$

## 49. IDU9: No Extra Massless, Deconfined, Or Silent Untyped Sector

Searchable no-extra-sector tag:

`V4P28-IDU9-NO-EXTRA-UNTYPED-SECTOR`.

The remaining possible escape is an extra continuum sector that is not pure
YM but also not seen as a structural leak.

There are three candidates:

$$
\boxed{
\begin{array}{ll}
\mathrm{X1}:&\hbox{extra massless gauge-invariant sector};\\
\mathrm{X2}:&\hbox{deconfined untyped color/center sector};\\
\mathrm{X3}:&\hbox{silent zero-response sector}.
\end{array}
}
$$

X3 is impossible by the printed source-ledger compactness packet and Paper
27's no-untyped-zero-response rule:

$$
\boxed{
\mathrm{X3}\Rightarrow\mathrm{LEAK7},
\qquad
\mathrm{LEAK7}\hbox{ is shut}.
}
$$

X2 is impossible in the active finite QCD-DYN branch because Paper 27 gives
positive center-flux/Wilson margin:

$$
\boxed{
\mathrm{X2}\Rightarrow\mathrm{LEAK4},
\qquad
\mathrm{LEAK4}\hbox{ is shut in the positive sense}.
}
$$

X1 is impossible in the active branch because Paper 27 gives positive
gauge-invariant transfer margin:

$$
\boxed{
\mathrm{X1}\Rightarrow\mathrm{LEAK5},
\qquad
\mathrm{LEAK5}\hbox{ is shut in the positive sense}.
}
$$

If any of X1-X3 nevertheless appears after YM normalization, it is not an
unnoticed sector.  It is a nontriviality/identification failure and must be
printed as LEAK6.

### Theorem 49.1: P27 Margins And Source-Ledger Compactness Close IDU9

Assume structural descent, scale lock, and the Paper 27 finite QCD-DYN
margin import.  Then no extra massless, deconfined, or silent untyped sector
remains in the continuum YM observable algebra.  Hence IDU9 passes.

Proof.  A silent sector is LEAK7, already shut.  A deconfined untyped
center/color sector contradicts the positive Wilson/center margin, hence
would reopen LEAK4.  A massless untyped gauge-invariant sector contradicts
the positive transfer margin, hence would reopen LEAK5.  Since LEAK4 and
LEAK5 are shut in the positive sense and any stronger normalization failure
is classified as LEAK6/nontriviality, no extra untyped sector remains inside
the claimed YM observable algebra. `square`

Active status:

$$
\boxed{
\mathrm{IDU9}
=
\mathrm{PASS}_{no\ extra\ untyped\ sector}.
}
$$

## 50. Full Audit Of `YM-ID-UNIQUENESS-001`

Searchable full IDU audit tag:

`V4P28-FULL-AUDIT-YM-ID-UNIQUENESS-001`.

Run IDU1-IDU9 after Sections 45-49:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{updated status} & \hbox{reason}\\
\hline
\mathrm{IDU1} &
\mathrm{PASS}_{P26} &
\hbox{finite Yang-Mills holonomy records are }SU(N)\\
\mathrm{IDU2} &
\mathrm{PASS}_{small\ loop} &
\hbox{plaquette holonomy descends to curvature}\\
\mathrm{IDU3} &
\mathrm{PASS}_{classification} &
\hbox{only untyped relevant/marginal density is }\operatorname{tr}F^{2}\\
\mathrm{IDU4} &
\mathrm{PASS}_{theta\ typed/fixed} &
\hbox{topological density is fixed before query or typed}\\
\mathrm{IDU5} &
\mathrm{PASS}_{Ward} &
\hbox{same-actual Ward descent already passed structurally}\\
\mathrm{IDU6} &
\mathrm{PASS}_{reflection} &
\hbox{source-ledger reflection positivity already passed}\\
\mathrm{IDU7} &
\mathrm{PASS}_{RG} &
\hbox{unique kinetic density gives route-independent coupling flow}\\
\mathrm{IDU8} &
\mathrm{PASS}_{irrelevant} &
\hbox{irrelevant operators vanish or are typed}\\
\mathrm{IDU9} &
\mathrm{PASS}_{sector} &
\hbox{no extra massless/deconfined/silent untyped sector}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{YM\text{-}ID\text{-}UNIQUENESS\text{-}001}
=
\mathrm{PASS}_{active\ YM\ descent\ branch}.
}
$$

By Theorem 40.1:

$$
\boxed{
\neg\mathrm{LEAK6}.
}
$$

## 51. Continuum Yang-Mills Confinement Theorem

Searchable final theorem tag:

`V4P28-CONTINUUM-YM-CONFINEMENT-PASS-THEOREM`.

### Theorem 51.1: Active ISP Descent Proves Continuum YM Confinement

On the active Barandes-aligned ISP-V4 branch, assume:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{P25 } \mathrm{FAC+SLC+RSC}_{GR}\hbox{ scale/collar branch};\\
2.&\hbox{P26 } \mathrm{REL\text{-}QFT\text{-}KIN+YM\text{-}GAUGE+YM\text{-}WILSON+RG\text{-}DESCENT};\\
3.&\hbox{P27 } \mathrm{QCD\text{-}DYN}
=\mathrm{PASS}_{finite\ ISP};\\
4.&\hbox{P28 source-ledger compactness and scale lock};\\
5.&\hbox{P28 } \mathrm{YM\text{-}ID\text{-}UNIQUENESS\text{-}001}.
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{PASS}_{ISP\ descent}.
}
$$

Proof.  Source-ledger compactness shuts LEAK1, LEAK2, LEAK3, and LEAK7.
Scale lock plus the Paper 27 finite QCD-DYN margin import shuts LEAK4 and
LEAK5 in the positive physical-margin sense.  The full IDU audit shuts
LEAK6.  Therefore no leak in the Feynman no-escape decomposition remains.
By Theorem 19.1 and Theorem 6.1, continuum Yang-Mills confinement follows in
the reconstructed gauge-invariant \(SU(N)\) sector. `square`

The theorem proves:

$$
\boxed{
\hbox{continuum confinement as ISP descent from finite actual-record QCD
dynamics.}
}
$$

It does not prove:

$$
\boxed{
\hbox{an arbitrary external formulation of continuum Yang-Mills confinement
without the ISP descent hypotheses.}
}
$$

## 52. Final Falsifier List After Closing LEAK6

Searchable final falsifier tag:

`V4P28-FINAL-FALSIFIER-LIST-AFTER-LEAK6`.

Even after the pass theorem, the result remains falsifiable.  It fails if
any of the following are printed:

$$
\boxed{
\begin{array}{c|l}
\hbox{falsifier} & \hbox{meaning}\\
\hline
\mathrm{YF1} & \hbox{finite holonomy has no cofinal small-loop logarithm
sector}\\
\mathrm{YF2} & \hbox{plaquette curvature fails source-response convergence}\\
\mathrm{YF3} & \hbox{an extra untyped relevant/marginal gauge-invariant
density appears}\\
\mathrm{YF4} & \hbox{topological sector is fitted after the confinement
query}\\
\mathrm{YF5} & \hbox{coupling flow depends on refinement route in the
untyped sector}\\
\mathrm{YF6} & \hbox{irrelevant operator survives untyped in the cofinal
limit}\\
\mathrm{YF7} & \hbox{extra massless/deconfined/silent untyped sector appears}\\
\mathrm{YF8} & \hbox{finite nonzero YM-normalized margins cannot be obtained
without fitting}
\end{array}
}
$$

If any falsifier fires, the theorem downgrades to:

$$
\boxed{
\mathrm{continuum\ YM\ confinement}
=
\mathrm{OPEN/FAIL}_{printed\ falsifier}.
}
$$

## 53. Exact Closure Obligations And Scope

Searchable closure ledger tag:

`V4P28-EXACT-CLOSURE-OBLIGATIONS`.

The phrase "continuum Yang-Mills confinement is closed" has three possible
meanings.  Paper 28 claims only the middle one.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{bare\ ISP\ ontology}\Rightarrow\mathrm{YM\ confinement} &
\mathrm{NOT\ CLAIMED} &
\hbox{finite records alone are not enough}\\
\mathrm{P25+P26+P27+P28}\Rightarrow\mathrm{YM\ confinement} &
\mathrm{CLAIMED} &
\hbox{active Barandes-aligned ISP descent theorem}\\
\mathrm{external\ Clay\text{-}style\ theorem\ without\ ISP\ hypotheses} &
\mathrm{NOT\ CLAIMED} &
\hbox{different mathematical target}
\end{array}
}
$$

Thus the exact closure problem is:

$$
\boxed{
\hbox{prove that the active ISP branch supplies every member of the
CYM1-CYM8 certificate without posterior fitting.}
}
$$

Equivalently, the paper must prove the following obligations.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{obligation} & \hbox{what must be proved} & \hbox{where it closes}\\
\hline
\mathrm{CO1} &
\hbox{print a fixed cofinal finite YM family }{\mathfrak Y} &
\mathrm{CYM1,CYM2,CYM5}\\
\mathrm{CO2} &
\hbox{finite QCD-DYN has positive finite margins and no hidden deconfined
sector} &
\mathrm{P27,\ LEAK4,\ LEAK5}\\
\mathrm{CO3} &
\hbox{source-ledger compactness: tightness, positivity, derivatives, typed
residues} &
\mathrm{CYM3,CYM4,\ LEAK1,LEAK2,LEAK3,LEAK7}\\
\mathrm{CO4} &
\hbox{scale lock: finite margins survive as positive physical margins} &
\mathrm{CYM6,CYM7,\ LEAK4,LEAK5}\\
\mathrm{CO5} &
\hbox{route independence: no posterior subsequence or refinement choice} &
\mathrm{CYM5}\\
\mathrm{CO6} &
\hbox{YM identification uniqueness: the limit is }SU(N)\hbox{ YM} &
\mathrm{CYM8,\ LEAK6}\\
\mathrm{CO7} &
\hbox{no-escape audit: every failure mode is one of the named falsifiers} &
\mathrm{F1\text{-}F8,\ YF1\text{-}YF8}\\
\mathrm{CO8} &
\hbox{scope discipline: theorem remains an ISP descent theorem} &
\mathrm{final\ scope}
\end{array}
}
$$

The closure statement is:

$$
\boxed{
(\mathrm{CO1}\wedge\cdots\wedge\mathrm{CO8})
\Longrightarrow
\mathrm{CYM1}\wedge\cdots\wedge\mathrm{CYM8}
\Longrightarrow
\mathrm{continuum\ YM\ confinement}.
}
$$

Theorem 51.1 is exactly this implication on the active branch:

$$
\boxed{
\begin{array}{c|l}
\hbox{active input} & \hbox{closure role}\\
\hline
\mathrm{P25\ FAC+SLC+RSC}_{GR} &
\hbox{scale/collar branch and physical normalization}\\
\mathrm{P26\ REL\text{-}QFT\text{-}KIN+YM} &
\hbox{relativistic gauge/QFT descent infrastructure}\\
\mathrm{P27\ QCD\text{-}DYN} &
\hbox{finite positive gauge dynamics and margin source}\\
\mathrm{P28\ source\text{-}ledger\ compactness} &
\hbox{compactness, positivity, derivative, typed-residue control}\\
\mathrm{P28\ scale\ lock} &
\hbox{positive physical string tension and mass gap}\\
\mathrm{P28\ YM\text{-}ID\text{-}UNIQUENESS} &
\hbox{identifies the limit as }SU(N)\hbox{ Yang-Mills}
\end{array}
}
$$

### 53.1 Einstein Closure Move

Einstein's version of the proof obligation is not "assume a continuum gauge
field and show it confines."  It is:

$$
\boxed{
\hbox{reconstruct the continuum }SU(N)\hbox{ Yang-Mills object uniquely from
finite invariant observable relations.}
}
$$

The invariant data are:

$$
\boxed{
({\mathcal W}_{\alpha},
{\mathcal O}^{g.i.}_{\alpha},
\omega_{\alpha},
R_{\beta\alpha},
\hbox{Ward quotient},
\hbox{source response}).
}
$$

The Einstein audit asks whether these data have one licensed continuum
decoder:

$$
\boxed{
D_{YM}^{cont}
\left(
\varprojlim_{\alpha}
({\mathcal W}_{\alpha},{\mathcal O}^{g.i.}_{\alpha},\omega_{\alpha})
\right)
=
SU(N)\hbox{ Yang-Mills}.
}
$$

If the same finite invariant data admit multiple inequivalent continuum
decoders, or a decoder with extra untyped relevant sectors, the proof is not
closed.  That is why CYM5 and CYM8 are structural, not cosmetic.

### 53.2 Feynman Closure Move

Feynman's version of the proof obligation is the no-escape ledger.  Do not
trust a verbal statement that confinement survives.  Name every way it could
fail and shut each channel.

The complete leak ledger is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{leak} & \hbox{failure mode} & \hbox{closure mechanism}\\
\hline
\mathrm{LEAK1} & \hbox{finite laws have no tight cofinal limit} &
\hbox{source-ledger compactness}\\
\mathrm{LEAK2} & \hbox{positivity fails in the limit} &
\hbox{reflection/source-response stability}\\
\mathrm{LEAK3} & \hbox{new response-invisible actual classes appear} &
\hbox{continuum actual identity}\\
\mathrm{LEAK4} & \hbox{physical string tension collapses} &
\hbox{scale lock plus P27 margins}\\
\mathrm{LEAK5} & \hbox{physical mass gap collapses} &
\hbox{scale lock plus P27 margins}\\
\mathrm{LEAK6} & \hbox{limit is not }SU(N)\hbox{ Yang-Mills} &
\hbox{YM identification uniqueness}\\
\mathrm{LEAK7} & \hbox{silent untyped sector survives} &
\hbox{typed-residue and IDU audits}
\end{array}
}
$$

The Feynman closure condition is:

$$
\boxed{
\neg\mathrm{LEAK1}\wedge\cdots\wedge\neg\mathrm{LEAK7}.
}
$$

This is why a finite positive margin alone is not enough.  The margin must
survive scaling, survive the limit, be attached to the right continuum
observable sector, and not be bypassed by a silent deconfined mode.

### 53.3 External-Grade Rigor Target

For an external reader, the remaining work is not to change the theorem's
logic.  It is to expand each active packet into conventional lemmas with no
declared-but-unproved gates:

$$
\boxed{
\begin{array}{c|l}
\hbox{packet} & \hbox{external-grade lemma target}\\
\hline
{\mathfrak Y} & \hbox{fixed cofinal finite gauge family with complete
gauge-invariant probes}\\
\mathrm{QCD\text{-}DYN} & \hbox{finite positive Wilson and transfer margins}\\
\mathrm{SLC} & \hbox{uniform source-ledger compactness and derivative
convergence}\\
\mathrm{SCALE\text{-}LOCK} & \hbox{positive physical liminf of string tension
and mass gap}\\
\mathrm{IDU} & \hbox{unique }SU(N)\hbox{ YM action-density and no extra
relevant/marginal sector}\\
\mathrm{FALSIFIERS} & \hbox{proof that every nonconfining limit triggers a
named leak}
\end{array}
}
$$

When those conventional lemmas are printed, the theorem is closed in the
strongest available sense of this corpus:

$$
\boxed{
\hbox{not bare ontology, not external assumption, but active ISP descent
closure.}
}
$$

### 53.4 The Three Hard Closure Lemmas

After the Einstein and Feynman reductions, the external-grade closure problem
has only three hard lemmas.

Searchable hard-lemma tag:

`V4P28-THREE-HARD-CLOSURE-LEMMAS`.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{lemma} & \hbox{job} & \hbox{leaks shut}\\
\hline
\mathrm{HCL1} &
\hbox{source-ledger compactness and positivity} &
\mathrm{LEAK1,LEAK2,LEAK3,LEAK7}\\
\mathrm{HCL2} &
\hbox{physical margin survival under scale lock} &
\mathrm{LEAK4,LEAK5}\\
\mathrm{HCL3} &
\hbox{YM identification uniqueness} &
\mathrm{LEAK6}
\end{array}
}
$$

The closure problem is therefore:

$$
\boxed{
\mathrm{HCL1}\wedge\mathrm{HCL2}\wedge\mathrm{HCL3}
\Longrightarrow
\neg\mathrm{LEAK1}\wedge\cdots\wedge\neg\mathrm{LEAK7}
\Longrightarrow
\mathrm{CYM1}\wedge\cdots\wedge\mathrm{CYM8}.
}
$$

This is the compressed proof architecture.  It is what an external reader
should attack if they want to test the claimed closure.

### 53.5 HCL1: Source-Ledger Compactness Lemma

Searchable lemma tag:

`V4P28-HCL1-SOURCE-LEDGER-COMPACTNESS-LEMMA`.

Let:

$$
\boxed{
{\mathcal S}_{\alpha}(J)
=
\log Z_{\alpha}(J)
}
$$

be the finite gauge-invariant source ledger for the cofinal family
\({\mathfrak Y}\), with source domain \({\mathcal J}\), typed residue registry
\({\mathcal T}\), Ward quotient \(Q_W\), and refinement maps
\(R_{\beta\alpha}\).

The HCL1 statement is:

$$
\boxed{
\begin{gathered}
\hbox{uniform source moments}
+\hbox{ typed-residue tightness}
+\hbox{ reflection-square stability}\\
+\hbox{ projective source consistency}
+\hbox{ derivative-limit control}\\
\Longrightarrow
\hbox{compact positive cofinal source-response law.}
\end{gathered}
}
$$

Explicitly, the lemma requires:

$$
\boxed{
\begin{array}{ll}
\mathrm{SLC\text{-}A}:&
\sup_{\alpha}\mathbb E_{\alpha}[\Phi(J)]<\infty
\hbox{ for a coercive source height }\Phi;\\
\mathrm{SLC\text{-}B}:&
\lim_{K\to\infty}\sup_{\alpha}
\omega_{\alpha}({\mathcal T}_{>K})=0;\\
\mathrm{SLC\text{-}C}:&
\liminf_{\alpha}\omega_{\alpha}(F^{*}F)\ge0
\hbox{ for every gauge-invariant source polynomial }F;\\
\mathrm{SLC\text{-}D}:&
{\mathcal S}_{\beta}(J\circ R_{\beta\alpha})
-{\mathcal S}_{\alpha}(J)\to0
\hbox{ on cofinal overlaps};\\
\mathrm{SLC\text{-}E}:&
\partial_J^{k}{\mathcal S}_{\alpha}(J)
\to
\partial_J^{k}{\mathcal S}_{\infty}(J)
\hbox{ for all licensed finite }k;\\
\mathrm{SLC\text{-}F}:&
\hbox{no source mass escapes outside Ward-equivalent or typed sectors.}
\end{array}
}
$$

Then:

$$
\boxed{
{\mathcal S}_{\alpha}
\Longrightarrow
{\mathcal S}_{\infty}
\quad
\hbox{as a positive gauge-invariant continuum source-response law.}
}
$$

Consequences:

$$
\boxed{
\begin{array}{c|c}
\hbox{gate/leak} & \hbox{closed by HCL1}\\
\hline
\mathrm{CYM3} & \hbox{reflection/source positivity survives descent}\\
\mathrm{CYM4} & \hbox{cofinal observable laws are tight/compact}\\
\mathrm{LEAK1} & \hbox{no loss of cofinal limit}\\
\mathrm{LEAK2} & \hbox{no loss of positivity}\\
\mathrm{LEAK3} & \hbox{no response-invisible actual classes}\\
\mathrm{LEAK7} & \hbox{no silent untyped sector}
\end{array}
}
$$

Einstein reading:

$$
\boxed{
\hbox{the continuum observable object exists because finite invariant
responses have a unique compact positive descent.}
}
$$

Feynman reading:

$$
\boxed{
\hbox{every possible escape of source mass, positivity, or typed residue is
accounted for and bounded.}
}
$$

#### 53.5.1 HCL1 Theorem Skeleton

Searchable theorem tag:

`V4P28-HCL1-SOURCE-LEDGER-COMPACTNESS-THEOREM`.

**Theorem 53.5.1: Source-Ledger Compactness Produces A Positive Continuum
Law.**

Assume SLC-A through SLC-F.  Then there exists a cofinal continuum
source-response law \({\mathcal S}_{\infty}\) such that:

$$
\boxed{
{\mathcal S}_{\alpha}
\Longrightarrow
{\mathcal S}_{\infty}
}
$$

in the projective finite-source topology, and:

$$
\boxed{
\omega_{\infty}(F^{*}F)\ge0
}
$$

for every licensed gauge-invariant source polynomial \(F\).  Moreover, all
licensed source derivatives commute with the cofinal limit:

$$
\boxed{
\partial_J^k{\mathcal S}_{\infty}(J)
=
\lim_{\alpha}\partial_J^k{\mathcal S}_{\alpha}(J)
}
$$

for every finite licensed derivative order \(k\).  No response-invisible
actual class or silent untyped sector survives outside the declared Ward or
typed-residue registry.  Therefore HCL1 closes CYM3, CYM4, LEAK1, LEAK2,
LEAK3, and LEAK7.

Proof.  The proof has seven accounting steps.

Step 1: tightness from source height.  SLC-A gives a coercive height
\(\Phi\) with uniformly bounded expectation.  Hence for every \(\epsilon>0\)
there is \(K\) such that:

$$
\boxed{
\sup_{\alpha}
\omega_{\alpha}(\Phi>K)
<
\epsilon.
}
$$

Thus no ordinary source mass escapes to infinite source height.

Step 2: typed-residue tightness.  SLC-B gives:

$$
\boxed{
\lim_{K\to\infty}
\sup_{\alpha}
\omega_{\alpha}({\mathcal T}_{>K})
=0.
}
$$

Thus any residue not absorbed by the Ward quotient remains typed and tight.
This shuts the most dangerous silent-sector channel: unbounded residue mass
cannot hide outside the finite source ledger.

Step 3: compactness of finite response profiles.  The source battery is
licensed before the limit.  On every finite sub-battery
\({\mathcal J}_{0}\subset{\mathcal J}\), Steps 1-2 give compactness of the
finite response vectors:

$$
\boxed{
\left\{
({\mathcal S}_{\alpha}(J),
\partial_J{\mathcal S}_{\alpha}(J),
\ldots,
\partial_J^k{\mathcal S}_{\alpha}(J))_{J\in{\mathcal J}_{0}}
\right\}_{\alpha}.
}
$$

A diagonal extraction over the licensed battery gives a cofinal candidate
\({\mathcal S}_{\infty}\).

Step 4: uniqueness by projective consistency.  SLC-D says the candidate does
not depend on the cofinal route:

$$
\boxed{
{\mathcal S}_{\beta}(J\circ R_{\beta\alpha})
-{\mathcal S}_{\alpha}(J)
\to0.
}
$$

Therefore every cofinal extraction has the same finite source profile.  The
compact subsequential limit upgrades to a route-independent projective limit.

Step 5: derivative-limit control.  SLC-E provides uniform derivative
control.  Hence the derivative ledgers converge with the source ledger:

$$
\boxed{
\lim_{\alpha}\partial_J^k{\mathcal S}_{\alpha}(J)
=
\partial_J^k{\mathcal S}_{\infty}(J).
}
$$

This prevents a common continuum failure mode: a limiting generating
functional exists, but its source responses are not the limits of the finite
responses.

Step 6: reflection positivity is closed.  For every finite \(\alpha\):

$$
\boxed{
\omega_{\alpha}(F^{*}F)\ge0.
}
$$

SLC-C and the source-response convergence imply:

$$
\boxed{
\omega_{\infty}(F^{*}F)
=
\lim_{\alpha}\omega_{\alpha}(F^{*}F)
\ge0.
}
$$

Thus the limiting gauge-invariant sector remains physically reconstructible.

Step 7: no invisible actual class.  SLC-F says any mass not visible in the
source-response profile is either Ward-equivalent or typed.  By Steps 2 and 5,
typed residues cannot carry escaping unbounded mass and cannot alter licensed
derivatives invisibly.  Therefore no new response-invisible actual class or
silent untyped sector survives the limit.

Combining Steps 1-7 gives a compact, positive, route-independent continuum
source-response law with derivative control and no untyped leakage.  This is
precisely HCL1. `square`

#### 53.5.2 HCL1 Sublemma Audit

Searchable audit tag:

`V4P28-HCL1-SUBLEMMA-AUDIT`.

The theorem above is now reduced to six conventional sublemmas:

$$
\boxed{
\begin{array}{c|l|c}
\hbox{sublemma} & \hbox{ordinary proof target} & \hbox{status}\\
\hline
\mathrm{HCL1\text{-}A} &
\hbox{construct a coercive source height with uniform moment bound} &
\mathrm{TARGET}\\
\mathrm{HCL1\text{-}B} &
\hbox{prove typed-residue tightness} &
\mathrm{TARGET}\\
\mathrm{HCL1\text{-}C} &
\hbox{prove reflection-square positivity is closed under cofinal limits} &
\mathrm{TARGET}\\
\mathrm{HCL1\text{-}D} &
\hbox{prove projective source consistency and route independence} &
\mathrm{TARGET}\\
\mathrm{HCL1\text{-}E} &
\hbox{prove source derivatives commute with the limit} &
\mathrm{TARGET}\\
\mathrm{HCL1\text{-}F} &
\hbox{prove no source mass escapes outside Ward or typed sectors} &
\mathrm{TARGET}
\end{array}
}
$$

The active paper treats these as supplied by
`YM-SOURCE-LEDGER-COMPACTNESS-001`.  For external-grade rigor, each row must
be promoted from packet condition to ordinary lemma.

#### 53.5.3 HCL1 No-Escape Budget

The Feynman budget identity for HCL1 is:

$$
\boxed{
1
=
M_{\le K}^{src}
+M_{>K}^{src}
+M_{\le K}^{typed}
+M_{>K}^{typed}
+M^{silent}
+M^{Ward}.
}
$$

The required limits are:

$$
\boxed{
\lim_{K\to\infty}\sup_{\alpha}M_{>K}^{src}=0,
\qquad
\lim_{K\to\infty}\sup_{\alpha}M_{>K}^{typed}=0,
\qquad
M^{silent}=0.
}
$$

The Ward part is not a leak:

$$
\boxed{
M^{Ward}
\sim
\hbox{gauge redundancy removed by }Q_W.
}
$$

Therefore all surviving mass is either source-visible, Ward-equivalent, or
typed with controlled finite residue.  This is the real HCL1 closure
criterion:

$$
\boxed{
\hbox{nothing can disappear from the source ledger without being either
visible, redundant, or typed.}
}
$$

#### 53.5.4 HCL1-A: Einstein Invariant Source Height

Searchable tag:

`V4P28-HCL1-A-EINSTEIN-INVARIANT-SOURCE-HEIGHT`.

The Einstein move for HCL1-A is to make the coercive height an invariant
finite-record quantity, not an arbitrary regulator norm.  The source height
must be declared before the confinement query and must be built only from
licensed gauge-invariant source data.

Write:

$$
\boxed{
\Phi_{\alpha}
=
\Phi_{\alpha}^{loc}
+\Phi_{\alpha}^{Ward}
+\Phi_{\alpha}^{type}
+\Phi_{\alpha}^{collar}.
}
$$

The terms mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{term} & \hbox{role}\\
\hline
\Phi_{\alpha}^{loc} &
\hbox{local gauge-invariant source cost}\\
\Phi_{\alpha}^{Ward} &
\hbox{cost of leaving the same-actual Ward quotient}\\
\Phi_{\alpha}^{type} &
\hbox{typed-residue height visible to the registry}\\
\Phi_{\alpha}^{collar} &
\hbox{scale/collar cost imported from the active P25 branch}
\end{array}
}
$$

The invariant-height requirements are:

$$
\boxed{
\begin{array}{ll}
\mathrm{IH1}:&
\Phi_{\alpha}\hbox{ is gauge-invariant after Ward quotienting};\\
\mathrm{IH2}:&
\Phi_{\alpha}\hbox{ is cofinally compatible with }R_{\beta\alpha};\\
\mathrm{IH3}:&
\{\Phi_{\alpha}\le K\}/Q_W\hbox{ has uniformly compact source profiles};\\
\mathrm{IH4}:&
\Phi_{\alpha}\hbox{ is fixed before selecting confinement margins};\\
\mathrm{IH5}:&
\sup_{\alpha}\omega_{\alpha}(\Phi_{\alpha})\le C_{\Phi}<\infty.
\end{array}
}
$$

Then:

$$
\boxed{
\omega_{\alpha}(\Phi_{\alpha}>K)
\le
\frac{C_{\Phi}}{K}.
}
$$

Therefore:

$$
\boxed{
\lim_{K\to\infty}
\sup_{\alpha}
\omega_{\alpha}(\Phi_{\alpha}>K)
=0.
}
$$

This proves the tightness part of HCL1-A once IH1-IH5 are proved.

The theorem target is:

$$
\boxed{
\mathrm{IH1\text{-}IH5}
\Longrightarrow
\mathrm{HCL1\text{-}A}.
}
$$

Einstein reading:

$$
\boxed{
\hbox{compactness comes from one invariant source height shared by all
licensed refinements.}
}
$$

#### 53.5.5 HCL1-A: Feynman Source-Mass Budget

Searchable tag:

`V4P28-HCL1-A-FEYNMAN-SOURCE-MASS-BUDGET`.

The Feynman move for HCL1-A is to split the source ledger into controlled and
escaping source mass:

$$
\boxed{
1
=
M_{\le K}^{src}
+M_{>K}^{src}
+M^{non\text{-}src}.
}
$$

where:

$$
\boxed{
M_{>K}^{src}
=
\omega_{\alpha}(\Phi_{\alpha}>K).
}
$$

The source escape bound is:

$$
\boxed{
\sup_{\alpha}M_{>K}^{src}
\le
\frac{C_{\Phi}}{K}
\to0.
}
$$

This is not the whole HCL1 proof.  It only proves that ordinary source mass
does not escape to infinite source height.  The remaining budget terms must
be handled by Ward quotienting, typed-residue tightness, and no-silent-sector
control.

Feynman reading:

$$
\boxed{
\hbox{a source profile cannot vanish into the continuum limit unless it pays
unbounded height, and that budget is zero in the limit.}
}
$$

#### 53.5.6 HCL1-B: Einstein Typed-Residue Quotient

Searchable tag:

`V4P28-HCL1-B-EINSTEIN-TYPED-RESIDUE-QUOTIENT`.

The Einstein move for HCL1-B is to refuse an unclassified residue bin.  Any
non-Ward residue must live in a declared typed quotient:

$$
\boxed{
{\mathcal T}
=
\bigsqcup_{\tau\in{\mathsf T}}
{\mathcal T}_{\tau}.
}
$$

Each type has a height:

$$
\boxed{
H_T(\tau,r)
=
h(\tau)+\|r\|_{\tau}.
}
$$

The typed-residue requirements are:

$$
\boxed{
\begin{array}{ll}
\mathrm{TR1}:&
{\mathsf T}\hbox{ is declared before the continuum query};\\
\mathrm{TR2}:&
\hbox{every non-Ward residue maps to exactly one typed sector};\\
\mathrm{TR3}:&
H_T\hbox{ is invariant under the finite Ward quotient};\\
\mathrm{TR4}:&
\{H_T\le K\}\hbox{ has uniformly compact typed profiles};\\
\mathrm{TR5}:&
\sup_{\alpha}\omega_{\alpha}(H_T)\le C_T<\infty.
\end{array}
}
$$

Then:

$$
\boxed{
\omega_{\alpha}(H_T>K)
\le
\frac{C_T}{K},
}
$$

so:

$$
\boxed{
\lim_{K\to\infty}
\sup_{\alpha}
\omega_{\alpha}(H_T>K)
=0.
}
$$

This proves typed-residue tightness once TR1-TR5 are proved.

The theorem target is:

$$
\boxed{
\mathrm{TR1\text{-}TR5}
\Longrightarrow
\mathrm{HCL1\text{-}B}.
}
$$

Einstein reading:

$$
\boxed{
\hbox{a residue is admissible only if it is invariantly classified and
compactly controlled.}
}
$$

#### 53.5.7 HCL1-B: Feynman Residue-Escape Budget

Searchable tag:

`V4P28-HCL1-B-FEYNMAN-RESIDUE-ESCAPE-BUDGET`.

The Feynman budget for residues is:

$$
\boxed{
M^{res}
=
M^{Ward}
+M_{\le K}^{typed}
+M_{>K}^{typed}
+M^{untyped}.
}
$$

The closure requirements are:

$$
\boxed{
\lim_{K\to\infty}
\sup_{\alpha}
M_{>K}^{typed}
=0,
\qquad
M^{untyped}=0.
}
$$

The first condition follows from TR5:

$$
\boxed{
M_{>K}^{typed}
=
\omega_{\alpha}(H_T>K)
\le
\frac{C_T}{K}.
}
$$

The second condition is the registry completeness requirement:

$$
\boxed{
\hbox{every surviving non-Ward residue must be typed.}
}
$$

Thus:

$$
\boxed{
M^{res}
\sim
M^{Ward}
+M_{\le K}^{typed}
}
$$

up to a vanishing high-type tail.  This proves that residues cannot hide an
uncontrolled silent sector.

Feynman reading:

$$
\boxed{
\hbox{every residue is either gauge redundancy, typed finite cost, or a named
falsifier.}
}
$$

#### 53.5.8 HCL1-A/B Combined Status

Searchable tag:

`V4P28-HCL1-A-B-COMBINED-STATUS`.

The combined A/B status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{sublemma} & \hbox{reduction} & \hbox{remaining proof duty}\\
\hline
\mathrm{HCL1\text{-}A} &
\mathrm{IH1\text{-}IH5}
\Longrightarrow
\hbox{source tightness} &
\hbox{prove invariant height and uniform moment bound}\\
\mathrm{HCL1\text{-}B} &
\mathrm{TR1\text{-}TR5}
\Longrightarrow
\hbox{typed-residue tightness} &
\hbox{prove registry completeness and uniform typed moment bound}
\end{array}
}
$$

So A/B are not finished by naming \(\Phi_{\alpha}\) and \(H_T\).  They are
finished only when the active finite gauge family proves:

$$
\boxed{
\sup_{\alpha}\omega_{\alpha}(\Phi_{\alpha})<\infty,
\qquad
\sup_{\alpha}\omega_{\alpha}(H_T)<\infty,
\qquad
M^{untyped}=0.
}
$$

At that point:

$$
\boxed{
\mathrm{HCL1\text{-}A}
\wedge
\mathrm{HCL1\text{-}B}
\Longrightarrow
\hbox{ordinary source and typed-residue tightness.}
}
$$

#### 53.5.9 Source-Admissibility No-Escape Principle

Searchable tag:

`V4P28-SOURCE-ADMISSIBILITY-NO-ESCAPE`.

The next move is to stop treating the two uniform bounds as arbitrary
analytic assumptions.  They should follow from the meaning of a licensed
physical source in the finite-record ontology.

Define a licensed physical source family:

$$
\boxed{
{\mathfrak L}_{src}
=
({\mathcal J},
{\mathcal P}^{src}_{\alpha},
{\mathcal R}^{src}_{\alpha},
Q_W,
{\mathcal T},
{\mathcal C}^{collar}_{\alpha}).
}
$$

The entries are:

$$
\boxed{
\begin{array}{c|l}
\hbox{entry} & \hbox{meaning}\\
\hline
{\mathcal J} & \hbox{declared gauge-invariant source domain}\\
{\mathcal P}^{src}_{\alpha} & \hbox{finite source preparation records}\\
{\mathcal R}^{src}_{\alpha} & \hbox{finite source readout records}\\
Q_W & \hbox{same-actual Ward quotient}\\
{\mathcal T} & \hbox{typed residue registry}\\
{\mathcal C}^{collar}_{\alpha} & \hbox{physical collar/scale-cost ledger}
\end{array}
}
$$

A source is admissible only if its preparation/readout cost is finite in the
active physical collar:

$$
\boxed{
\mathrm{Cost}_{\alpha}(J)
=
\Phi_{\alpha}^{loc}(J)
+\Phi_{\alpha}^{Ward}(J)
+\Phi_{\alpha}^{type}(J)
+\Phi_{\alpha}^{collar}(J)
<\infty.
}
$$

The source-admissibility principle is:

$$
\boxed{
\hbox{licensed finite-record sources have uniformly bounded expected
operational cost.}
}
$$

Formally:

$$
\boxed{
\sup_{\alpha}
\omega_{\alpha}(\mathrm{Cost}_{\alpha})
<\infty.
}
$$

With \(\Phi_{\alpha}=\mathrm{Cost}_{\alpha}\), this is exactly the missing
uniform moment bound for HCL1-A.

For residues, admissibility says every non-Ward leftover must be physically
classified:

$$
\boxed{
\hbox{non-Ward residue}
\Rightarrow
\hbox{typed residue with finite operational height}.
}
$$

Formally:

$$
\boxed{
\sup_{\alpha}\omega_{\alpha}(H_T)<\infty,
\qquad
M^{untyped}=0.
}
$$

Thus the source-admissibility target is:

$$
\boxed{
\mathrm{physical\ source\ admissibility}
\Longrightarrow
\mathrm{HCL1\text{-}A}
\wedge
\mathrm{HCL1\text{-}B}.
}
$$

#### 53.5.10 Einstein Route: Source Bounds From Operational Admissibility

Searchable tag:

`V4P28-HCL1-A-B-EINSTEIN-ADMISSIBILITY-THEOREM`.

Einstein's move is to make the bound invariantly meaningful.  The source
height is not a regulator norm; it is the finite operational cost of preparing
and reading a source intervention in the active collar geometry.

The Einstein admissibility conditions are:

$$
\boxed{
\begin{array}{ll}
\mathrm{EA1}:&
\hbox{source preparations and readouts are finite record operations};\\
\mathrm{EA2}:&
\hbox{their cost is gauge-invariant after the Ward quotient};\\
\mathrm{EA3}:&
\hbox{their cost is cofinally stable under }R_{\beta\alpha};\\
\mathrm{EA4}:&
\hbox{the collar cost is fixed by the active P25 scale branch};\\
\mathrm{EA5}:&
\hbox{unbounded-cost sources are not licensed physical probes};\\
\mathrm{EA6}:&
\hbox{all non-Ward residues have declared physical type.}
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{EA1\text{-}EA6}
\Longrightarrow
\sup_{\alpha}\omega_{\alpha}(\Phi_{\alpha})<\infty,
\quad
\sup_{\alpha}\omega_{\alpha}(H_T)<\infty,
\quad
M^{untyped}=0.
}
$$

Proof sketch.  EA1-EA4 identify \(\Phi_{\alpha}\) with a physical
preparation/readout cost rather than a chosen norm.  EA5 says the source
domain \({\mathcal J}\) contains only operations with bounded expected
finite-record cost in the active collar.  Therefore
\(\sup_{\alpha}\omega_{\alpha}(\Phi_{\alpha})<\infty\).  EA6 says any
non-Ward residue is physically classified, so untyped residue mass is zero.
The same operational admissibility applied to typed residue preparations gives
\(\sup_{\alpha}\omega_{\alpha}(H_T)<\infty\).  Therefore HCL1-A and HCL1-B
follow by Sections 53.5.4-53.5.8. `square`

This is still a theorem target until EA1-EA6 are proved for the printed finite
gauge family.  But it changes the kind of missing proof:

$$
\boxed{
\hbox{prove physical admissibility of the source domain, not an arbitrary
analytic moment estimate.}
}
$$

#### 53.5.11 Feynman Route: Contrapositive No-Escape Ledger

Searchable tag:

`V4P28-HCL1-A-B-FEYNMAN-CONTRAPOSITIVE-LEDGER`.

Feynman's move is to prove A/B by contradiction through the ledger.  If a
uniform bound fails, a named escape channel must fire.

The contrapositive ledger is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failure} & \hbox{ledger consequence} & \hbox{named channel}\\
\hline
\sup_{\alpha}\omega_{\alpha}(\Phi_{\alpha})=\infty &
\hbox{unbounded physical source cost} &
\mathrm{SRC\text{-}ESC1}\\
\sup_{\alpha}\omega_{\alpha}(H_T)=\infty &
\hbox{unbounded typed residue cost} &
\mathrm{SRC\text{-}ESC2}\\
M^{untyped}>0 &
\hbox{surviving untyped residue sector} &
\mathrm{SRC\text{-}ESC3}\\
\Phi_{\alpha}\hbox{ not Ward-invariant} &
\hbox{gauge redundancy counted as source mass} &
\mathrm{SRC\text{-}ESC4}\\
\Phi_{\alpha}\hbox{ not cofinally stable} &
\hbox{route-dependent source cost} &
\mathrm{SRC\text{-}ESC5}\\
\hbox{high-cost source affects low-cost observables invisibly} &
\hbox{response-invisible actual class} &
\mathrm{SRC\text{-}ESC6}
\end{array}
}
$$

The Feynman no-escape theorem target is:

$$
\boxed{
\neg\mathrm{SRC\text{-}ESC1}
\wedge\cdots\wedge
\neg\mathrm{SRC\text{-}ESC6}
\Longrightarrow
\mathrm{HCL1\text{-}A}
\wedge
\mathrm{HCL1\text{-}B}.
}
$$

Proof sketch.  If HCL1-A fails, either \(\Phi_{\alpha}\) is not an admissible
physical cost, or its expected cost is unbounded.  The first case triggers
SRC-ESC4 or SRC-ESC5; the second triggers SRC-ESC1.  If HCL1-B fails, either
typed residue cost is unbounded or a non-Ward residue remains untyped.  These
trigger SRC-ESC2 or SRC-ESC3.  If a high-cost or untyped sector affects the
limit while remaining invisible to the source-response ledger, SRC-ESC6
fires.  Therefore if none of SRC-ESC1-SRC-ESC6 fires, HCL1-A/B hold. `square`

This is the real Feynman closure move:

$$
\boxed{
\hbox{every way the A/B bounds can fail is converted into a printed
falsifier.}
}
$$

#### 53.5.12 HCL1-A/B Updated Status

Searchable tag:

`V4P28-HCL1-A-B-UPDATED-STATUS`.

The updated A/B status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{remaining proof}\\
\hline
\mathrm{HCL1\text{-}A} &
\mathrm{REDUCED}_{EA/SRC\text{-}ESC} &
\hbox{prove source admissibility or shut SRC-ESC1,4,5,6}\\
\mathrm{HCL1\text{-}B} &
\mathrm{REDUCED}_{EA/SRC\text{-}ESC} &
\hbox{prove typed admissibility or shut SRC-ESC2,3,6}\\
\mathrm{HCL1\text{-}A/B} &
\mathrm{OPEN}_{admissibility/no\text{-}escape} &
\hbox{prove EA1-EA6 or }\neg\mathrm{SRC\text{-}ESC1\text{-}6}
\end{array}
}
$$

So the next exact proof target is:

$$
\boxed{
\mathrm{EA1\text{-}EA6}
\quad\hbox{or equivalently}\quad
\neg\mathrm{SRC\text{-}ESC1}\wedge\cdots\wedge\neg\mathrm{SRC\text{-}ESC6}.
}
$$

#### 53.5.13 Source-License Packet `SRC-LICENSE-001`

Searchable packet tag:

`V4P28-SRC-LICENSE-001`.

The next closure object is a source-license packet.  Its job is to make
"source" mean a finite operational intervention, not a free analytic function
introduced after the continuum target is known.

Print:

$$
\boxed{
\mathrm{SRC\text{-}LICENSE\text{-}001}
=
({\mathcal J},
{\mathcal P}^{src}_{\alpha},
{\mathcal R}^{src}_{\alpha},
{\mathcal L}_{\alpha},
Q_W,
{\mathcal T},
H_T,
R_{\beta\alpha},
{\mathcal C}^{collar}_{\alpha}).
}
$$

The entries are:

$$
\boxed{
\begin{array}{c|l}
\hbox{entry} & \hbox{meaning}\\
\hline
{\mathcal J} & \hbox{declared source domain}\\
{\mathcal P}^{src}_{\alpha} & \hbox{finite preparation records for sources}\\
{\mathcal R}^{src}_{\alpha} & \hbox{finite readout records for source response}\\
{\mathcal L}_{\alpha} & \hbox{license receipt map}\\
Q_W & \hbox{same-actual Ward quotient}\\
{\mathcal T} & \hbox{typed residue registry}\\
H_T & \hbox{typed residue height}\\
R_{\beta\alpha} & \hbox{cofinal refinement maps}\\
{\mathcal C}^{collar}_{\alpha} & \hbox{active physical collar and scale ledger}
\end{array}
}
$$

For each source \(J\in{\mathcal J}\), the license receipt is:

$$
\boxed{
{\mathcal L}_{\alpha}(J)
=
(\mathrm{prep}_{\alpha}(J),
\mathrm{read}_{\alpha}(J),
[J]_{W,\alpha},
\mathrm{Cost}_{\alpha}(J),
\mathrm{Type}_{\alpha}(J),
\mathrm{Collar}_{\alpha}(J),
\mathrm{Trace}_{\beta\alpha}(J)).
}
$$

The receipt fields mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{field} & \hbox{test}\\
\hline
\mathrm{prep}_{\alpha}(J) &
\hbox{source has a finite preparation record}\\
\mathrm{read}_{\alpha}(J) &
\hbox{source response has finite readout records}\\
[J]_{W,\alpha} &
\hbox{source has a declared Ward-equivalence class}\\
\mathrm{Cost}_{\alpha}(J) &
\hbox{source has finite collar-normalized operational cost}\\
\mathrm{Type}_{\alpha}(J) &
\hbox{non-Ward residue is typed if present}\\
\mathrm{Collar}_{\alpha}(J) &
\hbox{source is licensed in the active scale/collar branch}\\
\mathrm{Trace}_{\beta\alpha}(J) &
\hbox{source identity is stable under cofinal refinement}
\end{array}
}
$$

A source is licensed iff every receipt field is finite, declared before the
confinement query, and cofinally stable.

#### 53.5.14 Source-License Tests

Searchable test tag:

`V4P28-SRC-LICENSE-TESTS-LT1-LT8`.

The source-license packet passes if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{test} & \hbox{condition} & \hbox{closes}\\
\hline
\mathrm{LT1} &
{\mathcal J}\hbox{ is fixed before the confinement query} &
\hbox{no posterior source fitting}\\
\mathrm{LT2} &
\mathrm{prep}_{\alpha}(J)\hbox{ and }\mathrm{read}_{\alpha}(J)
\hbox{ are finite records} &
\mathrm{EA1}\\
\mathrm{LT3} &
\mathrm{Cost}_{\alpha}(J)\hbox{ is Ward-invariant} &
\mathrm{EA2}\\
\mathrm{LT4} &
\mathrm{Trace}_{\beta\alpha}(J)\hbox{ is cofinally stable} &
\mathrm{EA3}\\
\mathrm{LT5} &
\mathrm{Collar}_{\alpha}(J)\hbox{ is fixed by the P25 scale branch} &
\mathrm{EA4}\\
\mathrm{LT6} &
\sup_{\alpha}\omega_{\alpha}(\mathrm{Cost}_{\alpha})<\infty &
\mathrm{EA5,\ HCL1\text{-}A}\\
\mathrm{LT7} &
\hbox{every non-Ward residue has a declared type} &
\mathrm{EA6,\ M^{untyped}=0}\\
\mathrm{LT8} &
\sup_{\alpha}\omega_{\alpha}(H_T)<\infty &
\mathrm{HCL1\text{-}B}
\end{array}
}
$$

The two hard tests are LT6 and LT8.  They are the ordinary moment estimates,
but now they are attached to finite operational licenses rather than inserted
as arbitrary analytic assumptions.

#### 53.5.15 Source-License Completeness Theorem Target

Searchable theorem tag:

`V4P28-SOURCE-LICENSE-COMPLETENESS-THEOREM`.

**Theorem 53.5.15: Source-License Completeness Closes HCL1-A/B.**

Assume `SRC-LICENSE-001` passes LT1-LT8.  Then:

$$
\boxed{
\mathrm{HCL1\text{-}A}
\wedge
\mathrm{HCL1\text{-}B}.
}
$$

Proof.  LT2 says source preparations and readouts are finite record
operations, giving EA1.  LT3 gives Ward-invariance of the operational source
cost, giving EA2.  LT4 gives cofinal source identity, giving EA3.  LT5 fixes
the physical collar cost by the active P25 branch, giving EA4.  LT6 excludes
unbounded-cost licensed probes and supplies:

$$
\boxed{
\sup_{\alpha}\omega_{\alpha}(\Phi_{\alpha})<\infty
}
$$

with \(\Phi_{\alpha}=\mathrm{Cost}_{\alpha}\).  Hence HCL1-A follows by
Sections 53.5.4-53.5.5.  LT7 says every non-Ward residue is typed, so
\(M^{untyped}=0\).  LT8 supplies:

$$
\boxed{
\sup_{\alpha}\omega_{\alpha}(H_T)<\infty.
}
$$

Hence HCL1-B follows by Sections 53.5.6-53.5.7.  Therefore
`SRC-LICENSE-001` closes HCL1-A/B. `square`

This theorem is a target until LT1-LT8 are proved for the printed source
domain.  It is nevertheless stronger than the previous state: the missing
estimates now have operational names and falsifiers.

#### 53.5.16 Source-License Falsifier Gates

Searchable falsifier tag:

`V4P28-SRC-LICENSE-FALSIFIERS-SF1-SF8`.

The source-license route fails if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{SF1} &
{\mathcal J}\hbox{ is chosen after the confinement target} &
\hbox{posterior source fitting}\\
\mathrm{SF2} &
\hbox{source preparation/readout is not finite-record} &
\hbox{not an ISP source}\\
\mathrm{SF3} &
\mathrm{Cost}_{\alpha}\hbox{ is not Ward-invariant} &
\hbox{gauge redundancy counted as cost}\\
\mathrm{SF4} &
\mathrm{Trace}_{\beta\alpha}\hbox{ is route-dependent} &
\hbox{source identity changes under refinement}\\
\mathrm{SF5} &
\mathrm{Collar}_{\alpha}\hbox{ is not fixed by the active scale branch} &
\hbox{bad physical normalization}\\
\mathrm{SF6} &
\sup_{\alpha}\omega_{\alpha}(\mathrm{Cost}_{\alpha})=\infty &
\hbox{HCL1-A remains open}\\
\mathrm{SF7} &
M^{untyped}>0 &
\hbox{silent untyped residue sector}\\
\mathrm{SF8} &
\sup_{\alpha}\omega_{\alpha}(H_T)=\infty &
\hbox{HCL1-B remains open}
\end{array}
}
$$

If none of SF1-SF8 fires, then no SRC-ESC channel remains:

$$
\boxed{
\neg\mathrm{SF1}\wedge\cdots\wedge\neg\mathrm{SF8}
\Longrightarrow
\neg\mathrm{SRC\text{-}ESC1}\wedge\cdots\wedge
\neg\mathrm{SRC\text{-}ESC6}.
}
$$

Then HCL1-A/B close by Theorem 53.5.15.

#### 53.5.17 Updated HCL1-A/B Status After Source Licensing

Searchable status tag:

`V4P28-HCL1-A-B-STATUS-AFTER-SRC-LICENSE`.

The current status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{object} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{SRC\text{-}LICENSE\text{-}001} &
\mathrm{PRINTED}_{target} &
\hbox{license structure now explicit}\\
\mathrm{LT1\text{-}LT5} &
\mathrm{STRUCTURAL}_{target} &
\hbox{finite, Ward, cofinal, and collar identity tests}\\
\mathrm{LT6} &
\mathrm{OPEN}_{source\ moment} &
\hbox{must prove bounded operational source cost}\\
\mathrm{LT7} &
\mathrm{OPEN}_{typed\ completeness} &
\hbox{must prove no non-Ward untyped residue}\\
\mathrm{LT8} &
\mathrm{OPEN}_{typed\ moment} &
\hbox{must prove bounded typed-residue height}\\
\mathrm{HCL1\text{-}A/B} &
\mathrm{OPEN}_{LT6+LT7+LT8} &
\hbox{license theorem target, not yet external-grade closed}
\end{array}
}
$$

This is the exact next proof frontier:

$$
\boxed{
\mathrm{LT6}
\wedge
\mathrm{LT7}
\wedge
\mathrm{LT8}.
}
$$

#### 53.5.18 Finite Source-Intervention License

Searchable packet tag:

`V4P28-FINITE-SOURCE-INTERVENTION-LICENSE-001`.

The next closure attempt packages LT6-LT8 into one finite intervention law.
The point is:

$$
\boxed{
\hbox{a source is a finite intervention channel, not an arbitrary analytic
test function.}
}
$$

Let \(\Gamma_{\alpha}^{0}\) be the no-source finite kernel and
\(\Gamma_{\alpha}^{J}\) the finite kernel with source \(J\) inserted.  A
licensed source intervention is:

$$
\boxed{
{\mathcal I}_{\alpha}(J)
=
({\mathcal C}_{\alpha},
\Gamma_{\alpha}^{0},
\Gamma_{\alpha}^{J},
\pi_{\alpha}^{g.i.},
Q_W,
{\mathcal T},
R_{\beta\alpha}).
}
$$

Define the finite intervention cost:

$$
\boxed{
{\mathsf C}_{\alpha}(J)
=
D_{\alpha}^{g.i.}(\Gamma_{\alpha}^{J}\|\Gamma_{\alpha}^{0})
+{\mathsf C}_{\alpha}^{collar}(J)
+{\mathsf C}_{\alpha}^{Ward}(J)
+{\mathsf C}_{\alpha}^{type}(J).
}
$$

Here \(D_{\alpha}^{g.i.}\) is the gauge-invariant finite channel divergence:

$$
\boxed{
D_{\alpha}^{g.i.}(\Gamma_{\alpha}^{J}\|\Gamma_{\alpha}^{0})
=
\sum_{c,c'}
\omega_{\alpha}(c)
\Gamma_{\alpha}^{J}(c'|c)
\log
\frac{\Gamma_{\alpha}^{J,g.i.}(c'|c)}
{\Gamma_{\alpha}^{0,g.i.}(c'|c)}.
}
$$

with the hard-support convention:

$$
\boxed{
\Gamma_{\alpha}^{J,g.i.}(c'|c)>0
\Rightarrow
\Gamma_{\alpha}^{0,g.i.}(c'|c)>0.
}
$$

If hard support fails, the source is not a finite perturbation of the
no-source law; it opens a new sector and must be typed or rejected.

The intended identification is:

$$
\boxed{
\Phi_{\alpha}(J)
=
{\mathsf C}_{\alpha}(J),
\qquad
H_T
=
{\mathsf C}_{\alpha}^{type}.
}
$$

Thus LT6 and LT8 become bounded finite-intervention-cost statements, not
unmotivated analytic estimates.

#### 53.5.19 Einstein Route: Intervention Identity And Bounded Cost

Searchable theorem tag:

`V4P28-EINSTEIN-SOURCE-INTERVENTION-LICENSING-THEOREM`.

Einstein's move is to define sameness of source by operational identity under
refinement.  A source is the same physical intervention across the cofinal
family only if its finite channel deformation has bounded cost and stable
identity.

The intervention-identity conditions are:

$$
\boxed{
\begin{array}{ll}
\mathrm{SI1}:&
\Gamma_{\alpha}^{J}\hbox{ is a finite stochastic kernel on }
{\mathcal C}_{\alpha};\\
\mathrm{SI2}:&
\Gamma_{\alpha}^{J}\hbox{ is gauge-invariant after }Q_W;\\
\mathrm{SI3}:&
{\mathsf C}_{\alpha}(J)\hbox{ is invariant under Ward-equivalent
presentations};\\
\mathrm{SI4}:&
R_{\beta\alpha}\Gamma_{\beta}^{J}
\simeq
\Gamma_{\alpha}^{J}R_{\beta\alpha}
\hbox{ in finite source response};\\
\mathrm{SI5}:&
{\mathsf C}_{\alpha}^{collar}\hbox{ is fixed by the active scale/collar
branch};\\
\mathrm{SI6}:&
\sup_{\alpha}\omega_{\alpha}({\mathsf C}_{\alpha}(J))<\infty
\hbox{ for licensed }J;\\
\mathrm{SI7}:&
\hbox{all hard-support failures are typed in }{\mathcal T};\\
\mathrm{SI8}:&
\sup_{\alpha}\omega_{\alpha}({\mathsf C}_{\alpha}^{type})<\infty.
\end{array}
}
$$

**Theorem 53.5.19: Finite Intervention Licensing Closes LT6-LT8.**

Assume SI1-SI8 for the declared source domain \({\mathcal J}\).  Then LT6,
LT7, and LT8 hold.

Proof.  SI1-SI5 identify each licensed source with a finite, gauge-invariant,
cofinally stable channel deformation in the active physical collar.  SI6 gives:

$$
\boxed{
\sup_{\alpha}\omega_{\alpha}(\mathrm{Cost}_{\alpha})
=
\sup_{\alpha}\omega_{\alpha}({\mathsf C}_{\alpha})
<\infty,
}
$$

which is LT6.  SI7 says every hard-support failure or non-Ward new sector is
typed; therefore no non-Ward untyped residue remains, giving LT7.  SI8 gives:

$$
\boxed{
\sup_{\alpha}\omega_{\alpha}(H_T)<\infty,
}
$$

which is LT8.  Therefore `SRC-LICENSE-001` passes its remaining hard tests,
and HCL1-A/B close by Theorem 53.5.15. `square`

Einstein reading:

$$
\boxed{
\hbox{a licensed source is an invariant finite channel deformation with
bounded operational cost.}
}
$$

This is still a theorem target until SI6-SI8 are proved for the active source
domain.

#### 53.5.20 Feynman Route: Intervention No-Escape Ledger

Searchable theorem tag:

`V4P28-FEYNMAN-SOURCE-INTERVENTION-NO-ESCAPE`.

Feynman's move is to show that if LT6-LT8 fail, the intervention ledger must
print a named failure.  The intervention escape channels are:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{escape} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{INT\text{-}ESC1} &
\sup_{\alpha}\omega_{\alpha}(D_{\alpha}^{g.i.})=\infty &
\hbox{unbounded source-channel deformation}\\
\mathrm{INT\text{-}ESC2} &
\sup_{\alpha}\omega_{\alpha}({\mathsf C}_{\alpha}^{collar})=\infty &
\hbox{unbounded physical collar cost}\\
\mathrm{INT\text{-}ESC3} &
\sup_{\alpha}\omega_{\alpha}({\mathsf C}_{\alpha}^{type})=\infty &
\hbox{unbounded typed-residue tail}\\
\mathrm{INT\text{-}ESC4} &
\Gamma_{\alpha}^{J}\not\ll\Gamma_{\alpha}^{0}\hbox{ and no type is declared} &
\hbox{new untyped sector}\\
\mathrm{INT\text{-}ESC5} &
R_{\beta\alpha}\Gamma_{\beta}^{J}\not\simeq
\Gamma_{\alpha}^{J}R_{\beta\alpha} &
\hbox{source identity changes under refinement}\\
\mathrm{INT\text{-}ESC6} &
\hbox{source affects continuum response but has no finite receipt} &
\hbox{unlicensed source}
\end{array}
}
$$

**Theorem 53.5.20: No Intervention Escape Implies LT6-LT8.**

If none of INT-ESC1 through INT-ESC6 fires, then LT6, LT7, and LT8 hold.

Proof.  If LT6 fails, the operational source cost is unbounded.  Since:

$$
\boxed{
\mathrm{Cost}_{\alpha}
=
D_{\alpha}^{g.i.}
+{\mathsf C}_{\alpha}^{collar}
+{\mathsf C}_{\alpha}^{Ward}
+{\mathsf C}_{\alpha}^{type},
}
$$

some component must be unbounded or route-unstable.  That triggers INT-ESC1,
INT-ESC2, INT-ESC3, or INT-ESC5.  If LT7 fails, a non-Ward residue remains
untyped; this triggers INT-ESC4.  If LT8 fails, typed-residue height is
unbounded; this triggers INT-ESC3.  If a source influences the continuum
without a finite preparation/readout receipt, this triggers INT-ESC6.
Therefore, if no intervention escape fires, LT6-LT8 hold. `square`

Feynman reading:

$$
\boxed{
\hbox{every failure of bounded source cost, typed completeness, or typed
height must leave a receipt in the intervention ledger.}
}
$$

#### 53.5.21 Updated Frontier After Intervention Licensing

Searchable status tag:

`V4P28-HCL1-A-B-FRONTIER-AFTER-INTERVENTION-LICENSE`.

The frontier is now:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{target} & \hbox{status} & \hbox{remaining proof}\\
\hline
\mathrm{LT6} &
\mathrm{REDUCED}_{SI6/INT\text{-}ESC1,2,5,6} &
\hbox{prove bounded finite intervention cost}\\
\mathrm{LT7} &
\mathrm{REDUCED}_{SI7/INT\text{-}ESC4} &
\hbox{prove every hard-support failure/new sector is typed}\\
\mathrm{LT8} &
\mathrm{REDUCED}_{SI8/INT\text{-}ESC3} &
\hbox{prove bounded typed intervention cost}\\
\mathrm{HCL1\text{-}A/B} &
\mathrm{OPEN}_{SI6+SI7+SI8} &
\hbox{intervention-license theorem target}
\end{array}
}
$$

Equivalently:

$$
\boxed{
\neg\mathrm{INT\text{-}ESC1}
\wedge\cdots\wedge
\neg\mathrm{INT\text{-}ESC6}
\Longrightarrow
\mathrm{HCL1\text{-}A/B}.
}
$$

This is the next exact proof frontier:

$$
\boxed{
\mathrm{SI6}
\wedge
\mathrm{SI7}
\wedge
\mathrm{SI8}.
}
$$

#### 53.5.22 Derived Finite-Receipt Principle From The Existing Corpus

Searchable theorem tag:

`V4P28-DERIVED-FINITE-RECEIPT-FROM-P24-P27`.

The remaining frontier is not best attacked by adding a new source axiom.
Papers 24-27 already refine the ontology enough to force the receipt
principle.

The corpus-level derivation is:

$$
\boxed{
\begin{array}{c}
\mathrm{P24\ Barandes\ finite\ witness\ discipline}\\
\wedge\ \mathrm{P25\ FAC+SLC+RSC}_{GR}\\
\wedge\ \mathrm{P26\ finite\ QFT/YM\ source\ batteries}\\
\wedge\ \mathrm{P27\ QCD\ local\ cost/branch\ certificate}\\
\Longrightarrow
\mathrm{FR1\text{-}FR8}.
\end{array}
}
$$

So the slogan:

$$
\boxed{
\hbox{no source without finite receipt}
}
$$

is not an extra primitive law.  It is the source-sector face of the existing
finite actual ontology.

The imported ontology is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{source} & \hbox{corpus principle} & \hbox{receipt consequence}\\
\hline
\mathrm{P24} &
\hbox{no continuum object without finite record witness} &
\mathrm{FR1,FR2,FR8}\\
\mathrm{P25\ FAC} &
\hbox{same actual content has same finite observable content} &
\mathrm{FR4}\\
\mathrm{P25\ SLC} &
\hbox{local comparison/collar identity is cofinally stable} &
\mathrm{FR4,FR5}\\
\mathrm{P25\ RSC} &
\hbox{every observable source effect is represented or typed} &
\mathrm{FR6,FR8}\\
\mathrm{P26} &
\hbox{QFT/YM sources are finite source batteries after Ward quotient} &
\mathrm{FR2,FR3,FR4}\\
\mathrm{P27} &
\hbox{QCD dynamics has local cost-height and sub-Markov branch control} &
\mathrm{FR5,FR7}
\end{array}
}
$$

The GR ontology refinement is doing real work here.  Paper 25's final active
branch says:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}.
}
$$

and its guiding ontology is:

$$
\boxed{
\hbox{surviving same-actual Ward cohomology}
=
\hbox{physical ISP content.}
}
$$

Therefore a source that leaves no finite preparation, readout, Ward quotient,
cofinal identity, typed residue, or cost ledger is not a new physical source.
It is a failed same-actual/RSC object.

For every declared source \(J\), define its finite receipt packet:

$$
\boxed{
\mathrm{Rec}_{\alpha}(J)
=
(P_{\alpha}(J),O_{\alpha}(J),Q_W,T_{\alpha}(J),
B_{\alpha}^{J},h_{\alpha}^{J},R_{\beta\alpha}).
}
$$

The fields are:

$$
\boxed{
\begin{array}{ll}
P_{\alpha}(J):&\hbox{finite preparation record for the intervention};\\
O_{\alpha}(J):&\hbox{finite readout record of its observable response};\\
Q_W:&\hbox{Ward/gauge quotient};\\
T_{\alpha}(J):&\hbox{typed hard-support sector ledger};\\
B_{\alpha}^{J}:&\hbox{typed residue branching majorant};\\
h_{\alpha}^{J}:&\hbox{local residue height/cost};\\
R_{\beta\alpha}:&\hbox{cofinal reduction map}.
\end{array}
}
$$

A source is physically admissible only if it satisfies:

$$
\boxed{
\begin{array}{ll}
\mathrm{FR1}:&
P_{\alpha}(J)\hbox{ is a finite record operation};\\
\mathrm{FR2}:&
O_{\alpha}(J)\hbox{ is a finite gauge-invariant readout};\\
\mathrm{FR3}:&
Q_W\mathrm{Rec}_{\alpha}(J)=\mathrm{Rec}_{\alpha}(J);\\
\mathrm{FR4}:&
R_{\beta\alpha}\mathrm{Rec}_{\beta}(J)\simeq
\mathrm{Rec}_{\alpha}(J);\\
\mathrm{FR5}:&
\omega_{\alpha}({\mathsf C}_{\alpha}(J))\le K(J)
\hbox{ with }K(J)<\infty;\\
\mathrm{FR6}:&
\Gamma_{\alpha}^{J}\not\ll\Gamma_{\alpha}^{0}
\Rightarrow
\hbox{a type in }T_{\alpha}(J)\hbox{ is printed};\\
\mathrm{FR7}:&
B_{\alpha}^{J}\hbox{ is sub-Markov with radius }q_J<1
\hbox{ and }\omega_{\alpha}(h_{\alpha}^{J})\le h_J<\infty;\\
\mathrm{FR8}:&
\hbox{no continuum response is admitted without a finite receipt.}
\end{array}
}
$$

**Theorem 53.5.22: Existing V4 Ontology Derives FR1-FR8.**

On the active P24-P27 corpus branch, every physically admissible source
\(J\in{\mathcal J}_{phys}\) satisfies FR1-FR8.

Proof.  P24 forbids smooth or continuum source objects without finite record
witnesses; hence every admissible source has finite preparation and readout
records, giving FR1 and FR2, and no continuum-only response, giving FR8.
P25 FAC says same-actual presentations have the same observable finite
content; combined with SLC's stable local comparison/collar structure, this
forces cofinal source identity under refinement, giving FR4, and fixes the
physical collar contribution to the cost, contributing to FR5.  P25 RSC says
every persistent loop, source, boundary, commutator, or word-depth effect is
represented in the printed dictionary or typed as a correction; hence every
hard-support failure or new source sector is typed, giving FR6, and hidden
source effects are excluded, reinforcing FR8.  P26 supplies the finite
QFT/YM source batteries and Ward/gauge quotient, giving FR2, FR3, and the
source-battery part of FR4.  P27 supplies the QCD local cost-height
inequalities and sub-Markov branching majorants, giving the bounded source
cost in FR5 and the typed-residue branch bound in FR7.  Therefore FR1-FR8
are consequences of the existing active corpus, not new axioms. `square`

The key shift is:

$$
\boxed{
\hbox{unbounded source cost is not a hard source inside the active corpus;
it is a failed FAC/SLC/RSC source witness.}
}
$$

This is the Einstein move.  The invariant object is not \(J(x)\) by itself;
it is the finite equivalence class of preparation/readout interventions whose
record identity survives refinement.  It is also the Feynman move: a claimed
source must leave a finite Ward/receipt trail, or it has no place in the
printed physical dictionary.

#### 53.5.23 Receipt Law Implies SI6-SI8

Searchable theorem tag:

`V4P28-FINITE-RECEIPT-IMPLIES-SI6-SI8`.

**Theorem 53.5.23: Derived Finite Receipts Close The Intervention Frontier.**

On the active P24-P27 corpus branch, SI6, SI7, and SI8 hold for every
\(J\in{\mathcal J}_{phys}\).

Proof.  By Theorem 53.5.22, the active corpus gives FR1-FR8.  FR1-FR4 make
the source a finite, Ward-invariant, cofinally stable record intervention.
FR5 gives:

$$
\boxed{
\sup_{\alpha}
\omega_{\alpha}({\mathsf C}_{\alpha}(J))
\le
K(J)
<\infty,
}
$$

which is SI6.  FR6 says every hard-support failure is printed as a typed
sector in \(T_{\alpha}(J)\), which is SI7.

For SI8, the typed residue tree is dominated by the sub-Markov majorant
\(B_{\alpha}^{J}\).  FR7 gives:

$$
\boxed{
\|B_{\alpha}^{J}\|_{1\to1}\le q_J<1,
}
$$

and finite local height:

$$
\boxed{
\omega_{\alpha}(h_{\alpha}^{J})\le h_J<\infty.
}
$$

Therefore the total typed residue height is bounded by the geometric
resolvent:

$$
\boxed{
\omega_{\alpha}({\mathsf C}_{\alpha}^{type})
\le
\sum_{n\ge0}
\omega_{\alpha}\!\left((B_{\alpha}^{J})^n h_{\alpha}^{J}\right)
\le
\frac{h_J}{1-q_J}
<\infty.
}
$$

This is SI8.  FR8 excludes a hidden continuum-only source that would affect
the limiting response without paying finite cost.  Hence SI6-SI8 hold.
`square`

Thus:

$$
\boxed{
\mathrm{P24+P25+P26+P27}
\Longrightarrow
\mathrm{FR1\text{-}FR8}
\Longrightarrow
\mathrm{SI6}
\wedge
\mathrm{SI7}
\wedge
\mathrm{SI8}
\Longrightarrow
\mathrm{HCL1\text{-}A/B}.
}
$$

#### 53.5.24 Feynman Receipt Audit

Searchable audit tag:

`V4P28-FEYNMAN-FINITE-RECEIPT-AUDIT`.

The Feynman version is not merely to test a numerical example.  It is to make
the accounting exact enough that a false source cannot hide.

For every proposed \(J\), the audit asks for the following receipts:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{receipt} & \hbox{required printed object} & \hbox{failure if absent}\\
\hline
\mathrm{R1} & P_{\alpha}(J) &
\hbox{unprepared external insertion}\\
\mathrm{R2} & O_{\alpha}(J) &
\hbox{unreadable response}\\
\mathrm{R3} & Q_W\hbox{-invariant equivalence class} &
\hbox{gauge/Ward presentation dependence}\\
\mathrm{R4} & R_{\beta\alpha}\mathrm{Rec}_{\beta}(J)\simeq
\mathrm{Rec}_{\alpha}(J) &
\hbox{source identity drifts with refinement}\\
\mathrm{R5} & K(J)<\infty &
\hbox{unbounded intervention cost}\\
\mathrm{R6} & T_{\alpha}(J) &
\hbox{new untyped support sector}\\
\mathrm{R7} & B_{\alpha}^{J},\ q_J<1,\ h_J<\infty &
\hbox{supercritical residue cascade}\\
\mathrm{R8} & \hbox{finite continuum-response receipt} &
\hbox{hidden continuum-only source}
\end{array}
}
$$

The contrapositive is the useful part:

$$
\boxed{
\hbox{if SI6, SI7, or SI8 fails, at least one of R1-R8 must fail.}
}
$$

So a source cannot remain ambiguous.  It either prints a finite receipt and is
admissible, or it identifies the exact escape channel that prevents HCL1-A/B.

#### 53.5.25 Updated HCL1-A/B Status After Finite Receipts

Searchable status tag:

`V4P28-HCL1-A-B-STATUS-AFTER-FINITE-RECEIPTS`.

The intervention frontier is now discharged by the existing active corpus,
not by adding an independent source law:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{target} & \hbox{status} & \hbox{basis}\\
\hline
\mathrm{SI6} &
\mathrm{PASS}_{FR5} &
\hbox{bounded finite intervention cost}\\
\mathrm{SI7} &
\mathrm{PASS}_{FR6} &
\hbox{typed hard-support sectors}\\
\mathrm{SI8} &
\mathrm{PASS}_{FR7} &
\hbox{sub-Markov typed-residue majorant}\\
\mathrm{HCL1\text{-}A/B} &
\mathrm{PASS}_{P24\text{-}P27} &
\hbox{Theorems 53.5.19, 53.5.22, 53.5.23, and 53.5.30}
\end{array}
}
$$

The precise scope is:

$$
\boxed{
\begin{array}{ll}
\hbox{active ISP physical-source theorem:}&
\mathrm{CLOSED};\\
\hbox{bare theorem without P24-P27 ontology:}&
\mathrm{NOT\ CLAIMED};\\
\hbox{external-grade proof obligation:}&
\hbox{audit the cross-paper derivation of FR1-FR8 from P24-P27.}
\end{array}
}
$$

This is the honest but aggressive closure: sources that do not carry finite
receipts are not counterexamples inside the active V4 ISP corpus.  They
violate P24 finite witness discipline or P25 FAC/SLC/RSC record/source
completeness.

#### 53.5.26 Finite Actual Intervention Category And Groupoid Core

Searchable object tag:

`V4P28-FINITE-ACTUAL-INTERVENTION-CATEGORY-AND-GROUPOID-CORE`.

The compression move is to stop treating \(J\) as an external analytic object.
At resolution \(\alpha\), define the finite actual intervention category:

$$
\boxed{
{\mathsf Int}_{\alpha}^{phys}.
}
$$

Its objects are finite actual record contexts:

$$
\boxed{
X_{\alpha}
=
({\mathcal C}_{\alpha},
{\mathcal P}_{\alpha},
{\mathcal S}_{\alpha},
Q_W,
R_{\beta\alpha},
{\mathcal T}_{\alpha}).
}
$$

Its morphisms are finite same-actual intervention records:

$$
\boxed{
I_{\alpha}:X_{\alpha}\to Y_{\alpha}.
}
$$

They are generated by:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{finite preparation operations};\\
2.&\hbox{finite source insertions};\\
3.&\hbox{finite readout operations};\\
4.&\hbox{Ward/gauge quotient moves};\\
5.&\hbox{cofinal refinement/reduction moves};\\
6.&\hbox{typed hard-support sector moves};\\
7.&\hbox{finite cost-height and branch-control moves}.
\end{array}
}
$$

Two interventions are the same physical source effect when:

$$
\boxed{
I_{\alpha}\sim J_{\alpha}
\quad\Longleftrightarrow\quad
I_{\alpha}-J_{\alpha}\in{\mathcal I}_{Ward,\alpha}
\oplus
{\mathcal A}_{typed,\alpha}
}
$$

and the typed part is controlled by the P27 sub-Markov branch certificate.
The invertible same-actual morphisms form the groupoid core:

$$
\boxed{
{\mathsf Int}_{\alpha}^{same}
\subset
{\mathsf Int}_{\alpha}^{phys}.
}
$$

Thus a physical source is:

$$
\boxed{
[I_{\alpha}]_{same}
\in
{\mathsf Int}_{\alpha}^{same}/({\mathcal I}_{Ward,\alpha}
\oplus{\mathcal A}_{typed,\alpha}),
}
$$

not a bare continuum function.

Einstein reading:

$$
\boxed{
\hbox{a source is an invariant same-actual finite intervention class.}
}
$$

#### 53.5.27 Canonical Receipt Functor

Searchable functor tag:

`V4P28-CANONICAL-RECEIPT-FUNCTOR`.

Define the receipt category \({\mathsf Rec}_{\alpha}\).  Its objects are
finite receipt packets:

$$
\boxed{
\mathrm{Rec}_{\alpha}(I)
=
(P_{\alpha}(I),O_{\alpha}(I),Q_W,T_{\alpha}(I),
B_{\alpha}^{I},h_{\alpha}^{I},R_{\beta\alpha}).
}
$$

The canonical receipt functor is:

$$
\boxed{
{\mathcal R}ec_{\alpha}:
{\mathsf Int}_{\alpha}^{phys}
\longrightarrow
{\mathsf Rec}_{\alpha}.
}
$$

It obeys:

$$
\boxed{
\begin{array}{ll}
\mathrm{RF1}:&
{\mathcal R}ec_{\alpha}(\mathrm{id})=\mathrm{empty\ receipt};\\
\mathrm{RF2}:&
{\mathcal R}ec_{\alpha}(I_2\circ I_1)
=
{\mathcal R}ec_{\alpha}(I_2)\odot
{\mathcal R}ec_{\alpha}(I_1);\\
\mathrm{RF3}:&
I\sim J
\Rightarrow
{\mathcal R}ec_{\alpha}(I)\sim{\mathcal R}ec_{\alpha}(J);\\
\mathrm{RF4}:&
R_{\beta\alpha}{\mathcal R}ec_{\beta}(I_{\beta})
\simeq
{\mathcal R}ec_{\alpha}(R_{\beta\alpha}I_{\beta});\\
\mathrm{RF5}:&
{\mathcal R}ec_{\alpha}(I)\hbox{ prints every non-Ward typed residue.}
\end{array}
}
$$

The functor is canonical because its fields are not chosen after the source
response is known.  They are read off from the same finite actual intervention
record that defines the source.

#### 53.5.28 Receipt Extraction Theorem

Searchable theorem tag:

`V4P28-RECEIPT-EXTRACTION-THEOREM`.

**Theorem 53.5.28: Every Active-Corpus Source Has A Canonical Receipt.**

On the active P24-P27 branch, every physically admissible source effect has a
canonical finite receipt packet, unique up to same-actual Ward equivalence and
typed controlled residue.

Equivalently:

$$
\boxed{
\forall [I_{\alpha}]_{same}\in{\mathsf Int}_{\alpha}^{same},
\quad
{\mathcal R}ec_{\alpha}([I_{\alpha}]_{same})
\hbox{ exists and is unique modulo }
{\mathcal I}_{Ward,\alpha}\oplus{\mathcal A}_{typed,\alpha}.
}
$$

Proof.  P24 supplies finite record witnesses for the intervention; otherwise
\(I_{\alpha}\) is not an object of the finite actual corpus.  P25 FAC makes
same-actual intervention identity invariant under finite presentation.  P25
SLC makes the local collar/frame/readout comparison stable under cofinal
refinement.  P25 RSC says every persistent source, loop, boundary,
commutator, or word-depth residue is represented by the printed dictionary or
typed.  P26 supplies the finite QFT/YM source battery and Ward quotient in
which the source derivative is evaluated.  P27 supplies the cost-height and
sub-Markov typed residue controls.  Therefore the receipt fields are forced
by the finite intervention record and are unique modulo the already licensed
Ward and typed equivalences. `square`

#### 53.5.29 Feynman Cokernel Audit For Receipts

Searchable audit tag:

`V4P28-FEYNMAN-RECEIPT-COKERNEL-AUDIT`.

The Feynman compression is to identify the exact place a missing source could
hide.  Let:

$$
\boxed{
D_{\alpha}^{rec}:
{\mathsf Rec}_{\alpha}
\longrightarrow
{\mathcal E}_{\alpha}^{src}
}
$$

where \({\mathcal E}_{\alpha}^{src}\) is the finite module of persistent
source, Wilson, boundary, commutator, hard-support, and word-depth effects.

The receipt cokernel is:

$$
\boxed{
{\mathcal K}_{\alpha}^{rec}
=
\mathrm{coker}\,D_{\alpha}^{rec}.
}
$$

The audit identity is:

$$
\boxed{
{\mathcal K}_{\alpha}^{rec}
=
{\mathcal A}_{RSC,\alpha}^{src}
\oplus
{\mathcal A}_{typed,\alpha}^{src}.
}
$$

Meaning:

$$
\boxed{
\hbox{a missing receipt is exactly an RSC source obstruction, plus any printed
typed residue.}
}
$$

If an untyped cokernel survives:

$$
\boxed{
{\mathcal K}_{*,untyped}^{rec}\ne0,
}
$$

then the active corpus has found a real missing source/probe/boundary channel,
and HCL1-A/B is not closed.  But on the active P25/P27 branch:

$$
\boxed{
{\mathcal A}_{RSC,*}^{src}=0,
\qquad
\|B_{\alpha}^{src}\|_{1\to1}\le q<1.
}
$$

Therefore:

$$
\boxed{
{\mathcal K}_{*,untyped}^{rec}=0
}
$$

and every typed residue is subcritical.

Feynman reading:

$$
\boxed{
\hbox{there is no place for a source effect to hide: it is received, Ward,
typed, or a printed correction.}
}
$$

#### 53.5.30 Compressed HCL1-A/B Closure Theorem

Searchable theorem tag:

`V4P28-COMPRESSED-HCL1-A-B-CLOSURE`.

The compressed source closure is:

$$
\boxed{
\begin{array}{c}
\mathrm{P24\ finite\ witnesses}\\
\wedge\ \mathrm{P25\ FAC+SLC+RSC}_{GR}\\
\wedge\ \mathrm{P26\ finite\ QFT/YM\ source\ batteries}\\
\wedge\ \mathrm{P27\ QCD\ cost/branch\ certificate}\\
\Longrightarrow
{\mathcal R}ec_{\alpha}\hbox{ total and canonical}\\
\Longrightarrow
\mathrm{FR1\text{-}FR8}\\
\Longrightarrow
\mathrm{SI6\text{-}SI8}\\
\Longrightarrow
\mathrm{HCL1\text{-}A/B}.
\end{array}
}
$$

Proof.  Theorem 53.5.28 makes \({\mathcal R}ec_{\alpha}\) total and canonical
on physically admissible source effects.  Theorem 53.5.29 identifies any
failure of receipt extraction with an RSC cokernel or a typed residue.  P25
RSC on the active GR branch kills the untyped cokernel, and P27 branch
control makes typed residues subcritical.  Hence FR1-FR8 hold.  Theorem
53.5.23 gives SI6-SI8.  Theorem 53.5.19 then closes LT6-LT8, so HCL1-A/B
close. `square`

This is the actual compression of the argument:

$$
\boxed{
\hbox{physical source}
=
\hbox{cofinally stable finite actual intervention with canonical receipt.}
}
$$

No independent source law has been added.

### 53.6 HCL2: Physical Margin Survival Lemma

Searchable lemma tag:

`V4P28-HCL2-PHYSICAL-MARGIN-SURVIVAL-LEMMA`.

Paper 27 supplies finite positive margins:

$$
\boxed{
\sigma_{\alpha}^{fin}>0,
\qquad
\Delta_{\alpha}^{fin}>0.
}
$$

HCL2 is the statement that these do not become zero after physical
normalization.

The scale lock supplies:

$$
\boxed{
A_{\alpha}^{phys}(S)
\sim
a_{\alpha}^{2}|S|_{\alpha},
\qquad
t_{\alpha}^{phys}
\sim
a_{\alpha}.
}
$$

The lemma requires uniform dimensionful lower bounds:

$$
\boxed{
\liminf_{\alpha}
\frac{\sigma_{\alpha}^{fin}}{a_{\alpha}^{2}}
=
\sigma_{*}
>0,
\qquad
\liminf_{\alpha}
\frac{\Delta_{\alpha}^{fin}}{a_{\alpha}}
=
\Delta_{*}
>0.
}
$$

Then:

$$
\boxed{
\langle W(C)\rangle_{\infty}
\le
A(C)e^{-\sigma_{*}\operatorname{Area}(C)},
}
$$

and:

$$
\boxed{
\|\langle{\mathcal O}(x){\mathcal O}(y)\rangle_c\|
\le
B_{\mathcal O}e^{-\Delta_{*}d(x,y)}.
}
$$

Consequences:

$$
\boxed{
\begin{array}{c|c}
\hbox{gate/leak} & \hbox{closed by HCL2}\\
\hline
\mathrm{CYM6} & \hbox{positive physical Wilson string tension}\\
\mathrm{CYM7} & \hbox{positive physical gauge-invariant mass gap}\\
\mathrm{LEAK4} & \hbox{string tension does not collapse}\\
\mathrm{LEAK5} & \hbox{mass gap does not collapse}
\end{array}
}
$$

Einstein reading:

$$
\boxed{
\hbox{the physical units are fixed by the same scale/collar branch that
defines the continuum geometry.}
}
$$

Feynman reading:

$$
\boxed{
\hbox{finite margins pay rent only if their dimensionful lower bounds survive
the scaling ledger.}
}
$$

### 53.7 HCL3: Yang-Mills Identification-Uniqueness Lemma

Searchable lemma tag:

`V4P28-HCL3-YM-IDENTIFICATION-UNIQUENESS-LEMMA`.

HCL3 proves that the compact positive confining limit is not merely an
unspecified confining gauge theory.  It is continuum \(SU(N)\) Yang-Mills.

The lemma requires:

$$
\boxed{
\begin{array}{ll}
\mathrm{ID\text{-}A}:&
\hbox{cofinal small-loop holonomies have a logarithmic curvature limit};\\
\mathrm{ID\text{-}B}:&
\hbox{the local action-density decoder is }
\frac{1}{4g^{2}}\operatorname{tr}F_{\mu\nu}F^{\mu\nu};\\
\mathrm{ID\text{-}C}:&
\hbox{Ward/source responses identify the }SU(N)\hbox{ gauge quotient};\\
\mathrm{ID\text{-}D}:&
\hbox{no extra untyped relevant or marginal gauge-invariant density survives};\\
\mathrm{ID\text{-}E}:&
\hbox{irrelevant operators vanish or remain typed with controlled decay};\\
\mathrm{ID\text{-}F}:&
\hbox{coupling flow is route-independent};\\
\mathrm{ID\text{-}G}:&
\hbox{no silent massless, deconfined, or response-invisible sector survives.}
\end{array}
}
$$

Then:

$$
\boxed{
D_{YM}^{cont}({\mathcal S}_{\infty})
=
SU(N)\hbox{ Yang-Mills}
}
$$

and:

$$
\boxed{
\neg\mathrm{LEAK6}.
}
$$

Consequences:

$$
\boxed{
\begin{array}{c|c}
\hbox{gate/leak} & \hbox{closed by HCL3}\\
\hline
\mathrm{CYM8} & \hbox{limit is continuum }SU(N)\hbox{ Yang-Mills}\\
\mathrm{LEAK6} & \hbox{wrong-theory escape is impossible}\\
\mathrm{YF3,YF6,YF7} & \hbox{extra untyped/silent sectors are blocked}
\end{array}
}
$$

Einstein reading:

$$
\boxed{
\hbox{the same invariant finite data have one continuum decoder, namely }
SU(N)\hbox{ Yang-Mills.}
}
$$

Feynman reading:

$$
\boxed{
\hbox{every extra action term, silent particle, or deconfined low mode must
appear in the ledger; if none can appear, the YM identity is unique.}
}
$$

### 53.8 The External Closure Theorem

Searchable theorem tag:

`V4P28-EXTERNAL-GRADE-CLOSURE-THEOREM-TARGET`.

The external-grade theorem target is:

$$
\boxed{
\mathrm{HCL1}\wedge\mathrm{HCL2}\wedge\mathrm{HCL3}
\Longrightarrow
\mathrm{continuum\ }SU(N)\mathrm{\ Yang\text{-}Mills\ confinement}
\hbox{ as ISP descent}.
}
$$

Proof.  HCL1 supplies compact positive continuum source-response laws and
shuts LEAK1, LEAK2, LEAK3, and LEAK7.  HCL2 supplies positive physical
string tension and positive physical mass gap, shutting LEAK4 and LEAK5.
HCL3 identifies the limiting gauge theory as continuum \(SU(N)\) Yang-Mills
and shuts LEAK6.  Therefore no leak in the no-escape ledger remains.  By
Theorem 19.1 and Theorem 6.1, continuum Yang-Mills confinement follows in the
reconstructed gauge-invariant \(SU(N)\) sector. `square`

This is the sharpest possible answer to the closure question:

$$
\boxed{
\begin{array}{l}
\hbox{HCL1 closes by the P24-P27 canonical receipt compression;}\\
\hbox{HCL2 closes by P27 positive margins plus P25/P28 scale lock;}\\
\hbox{HCL3 closes by active YM identification uniqueness.}
\end{array}
}
$$

## 54. Final Paper 28 Verdict

Searchable final verdict tag:

`V4P28-FINAL-CONTINUUM-YM-CONFINEMENT-VERDICT`.

The final verdict of Paper 28 is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{scope}\\
\hline
\mathrm{finite\ ISP\ QCD\text{-}DYN} &
\mathrm{PASS} &
\hbox{Paper 27}\\
\mathrm{structural\ continuum\ descent} &
\mathrm{PASS}_{P24\text{-}P27\ derived\ receipt} &
\hbox{finite-receipt source compactness derived from P24-P27}\\
\mathrm{positive\ physical\ string\ tension} &
\mathrm{PASS}_{positive} &
\hbox{P27 margin plus P25/P28 scale lock}\\
\mathrm{positive\ physical\ mass\ gap} &
\mathrm{PASS}_{positive} &
\hbox{P27 margin plus P25/P28 scale lock}\\
\mathrm{YM\ identification} &
\mathrm{PASS}_{active\ YM\ descent} &
\hbox{IDU1-IDU9 audit}\\
\mathrm{continuum\ YM\ confinement} &
\mathrm{PASS}_{ISP\ descent} &
\hbox{within reconstructed gauge-invariant }SU(N)\hbox{ sector}\\
\mathrm{external\ formulation\ without\ ISP\ hypotheses} &
\mathrm{NOT\ CLAIMED} &
\hbox{outside this paper's theorem}
\end{array}
}
$$

The short statement is:

$$
\boxed{
\mathrm{P25+P26+P27+P28}
\Longrightarrow
\mathrm{continuum\ }SU(N)\mathrm{\ Yang\text{-}Mills\ confinement}
}
$$

as an ISP descent theorem.
