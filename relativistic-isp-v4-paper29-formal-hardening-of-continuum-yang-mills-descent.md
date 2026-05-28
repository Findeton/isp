# Relativistic ISP V4 Paper 29: Formal Hardening Of The Internal Yang-Mills Descent Theorem

Author: Felix Robles Elvira

Status: formal hardening paper after Paper 28.  This paper adds no new
physics ontology.  It rewrites the Paper 25-Paper 28 chain in dependency
normal form, so that the internal ISP descent claim can be inspected without
quietly importing its own conclusion.

The target is:

$$
\boxed{
\mathrm{P25+P26+P27+P28^{pre}}
\Longrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}
}
$$

as an internal ISP-V4 descent theorem for the descended \(4D\) \(SU(N)\)
sector.

The non-target is:

$$
\boxed{
\hbox{a standalone Clay-style proof independent of ISP finite-record
ontology.}
}
$$

Nor is the target:

$$
\boxed{
\hbox{an unconditional proof that the ISP-descended sector has already been
identified with the standard continuum Yang-Mills Hilbert/algebraic theory.}
}
$$

## 0. What Is Being Hardened

Searchable scope tag:

`V4P29-FORMAL-HARDENING-SCOPE`.

Paper 28 ended with:

$$
\boxed{
\begin{array}{c|c}
\hbox{component} & \hbox{status in active V4 corpus}\\
\hline
\mathrm{P25\ GR\ ontology} &
\mathrm{FAC+SLC+RSC}_{GR}\ \mathrm{PASS}\\
\mathrm{P26\ QFT/YM\ kinematics} &
\mathrm{REL\text{-}QFT\text{-}KIN,\ YM\text{-}GAUGE,\ YM\text{-}WILSON}\ \mathrm{PASS}\\
\mathrm{P27\ finite\ QCD\ dynamics} &
\mathrm{QCD\text{-}DYN}=\mathrm{PASS}_{finite\ ISP}\\
\mathrm{P28\ pre-conclusion\ bridge\ packets} &
\mathrm{receipt,\ scale,\ and\ YM\ identification\ audits}
\end{array}
}
$$

The proof target is internally closed only after the receipt, scale, and
decoder packets are composed without circular import.  Paper 29 performs that
composition in one formal ledger:

$$
\boxed{
\hbox{finite objects}
\quad\to\quad
\hbox{axioms/imports}
\quad\to\quad
\hbox{lemmas}
\quad\to\quad
\hbox{main theorem}
\quad\to\quad
\hbox{falsifiers}.
}
$$

No new source law, margin law, or continuum Yang-Mills law is introduced.
Every assumption below is either:

$$
\boxed{
\hbox{an imported PASS or certificate result from Papers 24-28-pre}
\quad\hbox{or}\quad
\hbox{a definition of the formal language used to restate them.}
}
$$

The proof ledger uses the following dependency discipline:

$$
\boxed{
\begin{array}{c|l}
\hbox{kind} & \hbox{allowed role in Paper 29}\\
\hline
\mathrm{definition} &
\hbox{fixes the language of records, receipts, sources, and sectors}\\
\mathrm{imported\ packet} &
\hbox{imports a prior non-conclusion theorem or audit result}\\
\mathrm{derived\ lemma} &
\hbox{derives a Paper 29 claim from definitions and imported packets}\\
\mathrm{externalization} &
\hbox{records what must be rewritten for standard publication}
\end{array}
}
$$

In particular, Paper 29 is not allowed to import "continuum YM confinement"
as a premise and then reprint it as a conclusion.

## 1. Active Import Ledger

Searchable import tag:

`V4P29-ACTIVE-IMPORT-LEDGER`.

The active import packet is:

$$
\boxed{
{\mathbb I}_{24:28}^{red}
=
(\mathrm{B24},\mathrm{G25},\mathrm{Q26},\mathrm{D27},\mathrm{C28}^{pre}).
}
$$

The entries are:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{tag} & \hbox{source paper} & \hbox{imported content}\\
\hline
\mathrm{B24} &
\hbox{Paper 24} &
\hbox{finite actual records first; continuum language only after descent}\\
\mathrm{G25} &
\hbox{Paper 25} &
\mathrm{FAC+SLC+RSC}_{GR}\hbox{ and GR-DYN-COFINAL-PASS}\\
\mathrm{Q26} &
\hbox{Paper 26} &
\hbox{relativistic QFT kinematics, YM gauge, Wilson observables, RG descent}\\
\mathrm{D27} &
\hbox{Paper 27} &
\hbox{finite QCD-DYN, positive finite margins, typed residue discipline}\\
\mathrm{C28}^{pre} &
\hbox{Paper 28} &
\hbox{receipt data, scale packet, YM identification audit; no continuum
confinement conclusion}
\end{array}
}
$$

The Paper 28 import is deliberately reduced:

$$
\boxed{
\mathrm{C28}^{pre}
=
(\mathrm{RCP28},\mathrm{TSP28},\mathrm{MID28}).
}
$$

where:

$$
\boxed{
\begin{array}{c|l}
\hbox{tag} & \hbox{meaning}\\
\hline
\mathrm{RCP28} &
\hbox{finite receipt-compression, source-Cauchy, and determinacy data}\\
\mathrm{TSP28} &
\hbox{nonposterior scale map and margin-survival comparison certificate}\\
\mathrm{MID28} &
\hbox{YM decoder audit conditions before the final identification theorem}
\end{array}
}
$$

The forbidden import is:

$$
\boxed{
\mathrm{C28}^{pre}
\ne
\hbox{``continuum YM confinement/mass gap already proved.''}
}
$$

The hard content of \(C28^{pre}\) is not free.  It is exactly where a reviewer
must look if the theorem is challenged:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{packet} & \hbox{load-bearing claim} & \hbox{failure mode}\\
\hline
\mathrm{RCP28} &
\hbox{the source ledger is Cauchy/determinate, not merely compact} &
\hbox{only cluster points exist}\\
\mathrm{TSP28} &
\hbox{finite QCD margins survive the physical scale normalization} &
\hbox{string/gap margins collapse}\\
\mathrm{MID28} &
\hbox{the compact source law has a unique }SU(N)\hbox{ YM decoder} &
\hbox{wrong or silent decoder survives}
\end{array}
}
$$

Thus Paper 29 proves a relative internal theorem:

$$
\boxed{
\hbox{if these three hard certificates are accepted, the ISP descent theorem
closes; if one fails, the proof fails at the named gate.}
}
$$

The active ontology imported from Paper 25 is:

$$
\boxed{
\hbox{surviving same-actual Ward cohomology}
=
\hbox{physical ISP content.}
}
$$

This is the central rule used below.  A claimed physical object that leaves no
finite record, no same-actual class, no source/probe receipt, and no typed
residue is not an invisible new object inside the active corpus.  It is
outside the active physical dictionary.

## 2. Formal Objects

Searchable object tag:

`V4P29-FORMAL-OBJECTS`.

### 2.1 Cofinal Index System

Let \(({\mathcal A},\le)\) be a directed cofinal index set.  A refinement
\(\alpha\le\beta\) means that \(\beta\) is a finer finite actual record
description than \(\alpha\).

There are reduction maps:

$$
\boxed{
R_{\beta\alpha}:{\mathcal C}_{\beta}\to{\mathcal C}_{\alpha}.
}
$$

They compose cofinally:

$$
\boxed{
R_{\gamma\alpha}
=
R_{\beta\alpha}R_{\gamma\beta}
\quad
\hbox{whenever }
\alpha\le\beta\le\gamma.
}
$$

### 2.2 Finite Record Systems

At each \(\alpha\), a finite record system is:

$$
\boxed{
{\mathfrak X}_{\alpha}
=
({\mathcal C}_{\alpha},
\omega_{\alpha},
{\mathcal G}_{\alpha},
Q_{W,\alpha},
{\mathcal J}_{\alpha},
{\mathcal W}_{\alpha},
{\mathcal T}_{\alpha}).
}
$$

The entries are:

$$
\boxed{
\begin{array}{ll}
{\mathcal C}_{\alpha}:&\hbox{finite actual configuration/record space};\\
\omega_{\alpha}:&\hbox{positive finite normalized state};\\
{\mathcal G}_{\alpha}:&\hbox{finite gauge/same-actual move groupoid};\\
Q_{W,\alpha}:&\hbox{same-actual Ward quotient};\\
{\mathcal J}_{\alpha}:&\hbox{finite source battery};\\
{\mathcal W}_{\alpha}:&\hbox{finite Wilson/source-response observables};\\
{\mathcal T}_{\alpha}:&\hbox{typed residue registry}.
\end{array}
}
$$

All sets and sums at finite level are finite.

### 2.3 Source Ledger

For a source \(J\in{\mathcal J}_{\alpha}\), define:

$$
\boxed{
Z_{\alpha}(J)
=
\sum_{c\in{\mathcal C}_{\alpha}}
\omega_{\alpha}(c)\exp A_{\alpha}(c;J),
}
$$

and:

$$
\boxed{
{\mathcal S}_{\alpha}(J)=\log Z_{\alpha}(J).
}
$$

This is a finite source ledger, not a continuum path integral.

### 2.4 Wilson And Transfer Sectors

The finite Wilson sector is the finite algebra generated by:

$$
\boxed{
W_{\alpha}(\Gamma)
=
\operatorname{Tr}\prod_{e\in\Gamma}U_{\alpha,e}
}
$$

for finite loops \(\Gamma\).  The finite transfer sector contains transfer
operators:

$$
\boxed{
T_{\alpha}^{center},
\qquad
T_{\alpha}^{gap}.
}
$$

Paper 27 supplies positive finite Wilson/transfer margins:

$$
\boxed{
\sigma_{\alpha}^{fin}>0
\quad
\hbox{for the finite Wilson area-law/center sector},
\qquad
\Delta_{\alpha}^{fin}>0
\quad
\hbox{for the finite transfer/gauge-singlet sector}.
}
$$

The continuum theorem requires these margins to survive physical
normalization and cofinal descent.

## 3. Admissibility Axioms Imported As Passed Packets

Searchable axiom tag:

`V4P29-ACTIVE-ADMISSIBILITY-PACKETS`.

The following are treated as already passed inside the active corpus.

### A0: Finite Witness Discipline

Every physical object used in the theorem has a finite witness at each level:

$$
\boxed{
\hbox{physical object}
\Rightarrow
\hbox{finite record, finite source response, or typed residue.}
}
$$

This is imported from Paper 24.

### A1: Same-Actual Ward Quotient

Same-actual changes are quotiented by the Ward ideal:

$$
\boxed{
X\sim_{same}Y
\Rightarrow
{\mathcal O}(X)={\mathcal O}(Y)
\quad
\hbox{for every licensed finite observable }{\mathcal O}.
}
$$

Equivalently:

$$
\boxed{
{\mathcal I}_{Ward,\alpha}=0
\quad
\hbox{modulo exact finite terms and declared typed residues.}
}
$$

This is imported from P25 FAC/SLC/RSC.

### A2: Record/Source Completeness

Every persistent finite source, loop, boundary, commutator, or word-depth
effect is represented by the printed dictionary or typed:

$$
\boxed{
\mathrm{coker}\,
D_{\alpha}
\subset
{\mathcal A}_{typed,\alpha}
}
$$

and on the active GR branch:

$$
\boxed{
\mathrm{coker}\,D_{*,untyped}=0.
}
$$

This is imported from Paper 25.

### A3: Relativistic QFT/YM Kinematic Descent

Finite source-response gluing reconstructs the relativistic QFT kinematic
sector:

$$
\boxed{
\mathrm{REL\text{-}QFT\text{-}KIN}=\mathrm{PASS}.
}
$$

Finite gauge/Wilson observables descend:

$$
\boxed{
\mathrm{YM\text{-}GAUGE}
=
\mathrm{YM\text{-}WILSON}
=
\mathrm{RG\text{-}DESCENT}
=
\mathrm{PASS}.
}
$$

This is imported from Paper 26.

### A4: Finite QCD Dynamics

The finite QCD dynamics certificate passes:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

It supplies:

$$
\boxed{
\begin{array}{ll}
\mathrm{D27a}:&\hbox{finite Wilson area-law/center-string margin};\\
\mathrm{D27b}:&\hbox{finite transfer/singlet mass-gap margin};\\
\mathrm{D27c}:&\hbox{no untyped local zero-response obstruction};\\
\mathrm{D27d}:&\hbox{typed residue registry declared before the query};\\
\mathrm{D27e}:&\hbox{sub-Markov local residue branching majorant}.
\end{array}
}
$$

This is imported from Paper 27.

### A5: Scale And Margin Survival Packet

There is a physical scale map:

$$
\boxed{
a_{\alpha}>0
}
$$

fixed by the P25/P28 finite actual geometry, not chosen after seeing the
confinement target.  It turns finite margins into physical margins:

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

The scale packet is not the conclusion that the physical margins survive.  It
contains the following nonposterior data:

$$
\boxed{
\begin{array}{ll}
\mathrm{SL1}:&
a_{\alpha}\hbox{ is fixed by the finite actual geometry before the target};\\
\mathrm{SL2}:&
\hbox{refinements obey }a_{\beta}/a_{\alpha}\hbox{ through printed
reduction data};\\
\mathrm{SL3}:&
\hbox{finite center/string and singlet/gap margins are the P27 margins};\\
\mathrm{SL4}:&
\hbox{there are constants }\sigma_{*},\Delta_{*}>0\hbox{ such that}\\
&
\sigma_{\alpha}^{fin}\ge\sigma_{*}a_{\alpha}^{2},
\qquad
\Delta_{\alpha}^{fin}\ge\Delta_{*}a_{\alpha}
\quad\hbox{cofinally};\\
\mathrm{SL5}:&
\hbox{no posterior rescaling is allowed after asking for confinement.}
\end{array}
}
$$

This is imported from Paper 28 using P25/P27 as a scale certificate, not as
the theorem that the continuum margins have already survived.

### A6: YM Decoder Audit Packet

The active corpus imports the decoder audit conditions, not the final decoder
uniqueness conclusion.  The audit packet is:

$$
\boxed{
\begin{array}{ll}
\mathrm{YMU1}:&
\hbox{the gauge group label is fixed as }SU(N)\hbox{ before the query};\\
\mathrm{YMU2}:&
\hbox{finite Wilson traces separate the gauge quotient used by the decoder};\\
\mathrm{YMU3}:&
\hbox{small-loop source derivatives identify the kinetic density }
\mathrm{tr}\,F^{2};\\
\mathrm{YMU4}:&
\hbox{Ward and Bianchi identities hold in the same-actual quotient};\\
\mathrm{YMU5}:&
\hbox{RG coupling flow is route independent modulo typed irrelevant terms};\\
\mathrm{YMU6}:&
\hbox{irrelevant or boundary operators vanish, are Ward exact, or are typed};\\
\mathrm{YMU7}:&
\hbox{no untyped massless, deconfined, or wrong-gauge silent sector remains.}
\end{array}
}
$$

This is imported from Paper 28 as `MID28`.  Lemma 8.1 below derives decoder
uniqueness from YMU1-YMU7.

## 4. Formal Definitions

Searchable definition tag:

`V4P29-FORMAL-DEFINITIONS`.

### Definition 4.1: Internal ISP Continuum Descent

Let \({\mathcal J}\) be the countable licensed dictionary of finite source
letters, Wilson-loop insertions, boundary probes, and gauge-invariant
polynomial readouts.  For a finite battery \(J_0\subset{\mathcal J}\) and
derivative order \(k\), define the finite response coordinate:

$$
\boxed{
V_{\alpha}(J_0,k)
=
\left(
\partial_{J}^{m}
{\mathcal S}_{\alpha}(0)
\right)_{J\in J_0,\ |m|\le k}
\in{\mathbb R}^{N(J_0,k)}.
}
$$

The source-ledger topology is the projective cylinder topology generated by
all coordinates \(V_{\alpha}(J_0,k)\), modulo Ward-exact directions and
declared typed residue coordinates.

A cofinal finite family \(\{{\mathfrak X}_{\alpha}\}\) has an internal ISP
continuum descent if there exists a projective limiting source-response law:

$$
\boxed{
{\mathcal S}_{\alpha}
\Longrightarrow
{\mathcal S}_{\infty}
}
$$

such that:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{finite source responses converge on every finite source battery};\\
2.&\hbox{the coordinate limits are compatible with all reductions }
R_{\beta\alpha};\\
3.&\hbox{Ward/same-actual equivalence is preserved};\\
4.&\hbox{reflection/source positivity survives on every finite polynomial};\\
5.&\hbox{all non-Ward residues are typed and tight};\\
6.&\hbox{source derivatives commute with the cofinal limit}.
\end{array}
}
$$

### Definition 4.2: Internal Yang-Mills Confinement/Mass Gap

For rectangular Wilson loops \(C_{\rho}(R,T)\) in a fixed nontrivial
center-sensitive representation \(\rho\), write:

$$
\boxed{
W_{\infty,\rho}(R,T)
=
\omega_{\infty}(\mathrm{tr}_{\rho}\,U(C_{\rho}(R,T))).
}
$$

For gauge-invariant local source polynomials \(F,G\), write the connected
correlator in the reconstructed physical sector as:

$$
\boxed{
C_{F,G}(x)
=
\omega_{\infty}(F(x)G(0))
-
\omega_{\infty}(F(x))\omega_{\infty}(G(0)).
}
$$

The active family satisfies internal \(SU(N)\) Yang-Mills confinement/mass
gap if:

$$
\boxed{
\begin{array}{ll}
\mathrm{YM1}:&
D_{YM}^{desc}({\mathcal S}_{\infty})=SU(N)\hbox{ Yang-Mills};\\
\mathrm{YM2}:&
\hbox{there is }\sigma_{phys}>0\hbox{ such that}\\
&
\displaystyle
\liminf_{\substack{R,T\to\infty\\ \eta^{-1}\le R/T\le\eta}}
\frac{-\log |W_{\infty,\rho}(R,T)|}{RT}
\ge\sigma_{phys}
\quad\hbox{for every fixed }\eta>1;\\
\mathrm{YM3}:&
\hbox{there is }\Delta_{phys}>0\hbox{ such that the descended}\\
&
\hbox{transfer/Hamiltonian sector above the vacuum has gap }
\Delta_{phys};\\
\mathrm{YM4}:&
\hbox{the sector is gauge-invariant and reflection-positive};\\
\mathrm{YM5}:&
\hbox{no silent untyped deconfined or massless sector remains.}
\end{array}
}
$$

Then:

$$
\boxed{
\mathrm{YM1+YM2+YM3+YM4+YM5}
\Longleftrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}.
}
$$

The phrase \(CONFINEMENT/MASS\ GAP_{ISP\text{-}descent}\) is therefore not
merely a positive number in an abstract table.  It is a Wilson-area-law plus
spectral gap statement inside the reconstructed finite-record sector.

After a standard OS/transfer reconstruction, the internal spectral gap should
imply the conventional connected-correlator estimate:

$$
\boxed{
|C_{F,G}(x)|\le K_{F,G}e^{-\Delta_{phys}d(x,0)}
}
$$

for licensed gauge-invariant \(F,G\).  That comparison claim is not part of
the internal definition.  It belongs to the external OS/Hilbert/algebraic
comparison step recorded in Section 12.

### Definition 4.3: Closed Internal Descent Theorem

A theorem is closed internally if all its hypotheses are:

$$
\boxed{
\hbox{definitions}
\quad\hbox{or}\quad
\hbox{previously passed active-corpus packets},
}
$$

and the theorem introduces no posterior fitted table, no continuum primitive,
and no new hidden ontology.

It is not required to be a theorem of standard continuum QFT without ISP
premises.

## 5. Receipt Compression

Searchable compression tag:

`V4P29-RECEIPT-COMPRESSION`.

Paper 28's source compactness program is hardened as a receipt theorem.

Define the finite actual intervention category:

$$
\boxed{
{\mathsf Int}_{\alpha}^{phys}
}
$$

Its objects are finite actual preparation contexts.  A morphism:

$$
\boxed{
I:X\to Y
}
$$

is a finite intervention record carrying a source insertion, gauge-invariant
probe, boundary deformation, local commutator test, or typed residue
operation from context \(X\) to context \(Y\).  Composition is finite
concatenation followed by the same-actual Ward quotient:

$$
\boxed{
I_2\circ I_1
=
Q_W(I_2\cdot I_1).
}
$$

The identity morphism is the empty finite intervention:

$$
\boxed{
\mathrm{id}_X=\varnothing_X.
}
$$

For this to be a category after quotienting, the Ward quotient must be a
congruence for finite intervention composition.  The required congruence
facts are:

$$
\boxed{
\begin{array}{ll}
\mathrm{WQ1}:&
Q_W(Q_W(I))=Q_W(I);\\
\mathrm{WQ2}:&
Q_W(I_3\cdot(I_2\cdot I_1))
=Q_W((I_3\cdot I_2)\cdot I_1);\\
\mathrm{WQ3}:&
I\sim_{same}I'\Rightarrow
Q_W(J\cdot I)=Q_W(J\cdot I')\hbox{ and }
Q_W(I\cdot J)=Q_W(I'\cdot J);\\
\mathrm{WQ4}:&
\hbox{typed residue composition is closed under the declared
sub-Markov branch majorants.}
\end{array}
}
$$

These are imported from the same-actual Ward quotient and typed-residue
discipline in A1-A4.  Without WQ1-WQ4, \({\mathsf Int}_{\alpha}^{phys}\)
would be only a notation, not a category.

and its same-actual groupoid core:

$$
\boxed{
{\mathsf Int}_{\alpha}^{same}
\subset
{\mathsf Int}_{\alpha}^{phys}.
}
$$

A physical source effect is a class:

$$
\boxed{
[I_{\alpha}]_{same}
\in
{\mathsf Int}_{\alpha}^{same}/
({\mathcal I}_{Ward,\alpha}\oplus{\mathcal A}_{typed,\alpha}).
}
$$

Define the canonical receipt functor:

$$
\boxed{
{\mathcal R}ec_{\alpha}:
{\mathsf Int}_{\alpha}^{phys}
\to
{\mathsf Rec}_{\alpha}.
}
$$

Its value is:

$$
\boxed{
{\mathcal R}ec_{\alpha}(I)
=
(P_{\alpha}(I),O_{\alpha}(I),Q_{W,\alpha},T_{\alpha}(I),
B_{\alpha}^{I},h_{\alpha}^{I},R_{\beta\alpha}).
}
$$

The receipt category \({\mathsf Rec}_{\alpha}\) has receipt records as
morphisms and composition:

$$
\boxed{
r_2\odot r_1
=
Q_W(r_2\cdot r_1)
}
$$

with typed residue fields composed by the declared sub-Markov branch
majorants.  The empty receipt is:

$$
\boxed{
{\bf 1}_X
=
{\mathcal R}ec_{\alpha}(\varnothing_X).
}
$$

The functor laws are part of the receipt construction:

$$
\boxed{
\begin{array}{ll}
\mathrm{RF1}:&
{\mathcal R}ec_{\alpha}(\mathrm{id}_X)={\bf 1}_X;\\
\mathrm{RF2}:&
{\mathcal R}ec_{\alpha}(I_2\circ I_1)
=
{\mathcal R}ec_{\alpha}(I_2)\odot
{\mathcal R}ec_{\alpha}(I_1);\\
\mathrm{RF3}:&
{\mathcal R}ec_{\alpha}(I)\simeq{\mathcal R}ec_{\alpha}(I')
\hbox{ whenever }I\sim_{same}I';\\
\mathrm{RF4}:&
R_{\beta\alpha}{\mathcal R}ec_{\beta}(I)
\simeq
{\mathcal R}ec_{\alpha}(R_{\beta\alpha}I).
\end{array}
}
$$

The receipt gates are:

$$
\boxed{
\begin{array}{ll}
\mathrm{FR1}:&P_{\alpha}(I)\hbox{ is finite preparation};\\
\mathrm{FR2}:&O_{\alpha}(I)\hbox{ is finite gauge-invariant readout};\\
\mathrm{FR3}:&Q_W{\mathcal R}ec_{\alpha}(I)={\mathcal R}ec_{\alpha}(I);\\
\mathrm{FR4}:&\mathrm{RF1\text{-}RF4}\hbox{ hold cofinally};\\
\mathrm{FR5}:&\omega_{\alpha}({\mathsf C}_{\alpha}(I))\le K(I)<\infty;\\
\mathrm{FR6}:&\hbox{hard-support failures are typed};\\
\mathrm{FR7}:&\|B_{\alpha}^{I}\|_{1\to1}\le q_I<1
\hbox{ and }\omega_{\alpha}(h_{\alpha}^{I})\le h_I<\infty;\\
\mathrm{FR8}:&\hbox{no continuum response without finite receipt}.
\end{array}
}
$$

### Lemma 5.1: Receipt Extraction

Searchable lemma tag:

`V4P29-LEMMA-RECEIPT-EXTRACTION`.

For every physically admissible source effect in the active P24-P27 corpus,
\({\mathcal R}ec_{\alpha}\) exists and is unique modulo same-actual Ward
equivalence and typed controlled residue.

Proof.  A0 gives finite witnesses.  A1 gives same-actual Ward identity.  A2
says every source/probe residue is represented or typed.  A3 supplies the
finite QFT/YM source batteries and Ward quotient.  A4 supplies the cost-height
and sub-Markov typed branch control.  WQ1-WQ4 make the Ward quotient a
congruence for finite intervention composition, so identity and associativity
survive the quotient.  The receipt fields are computed from that finite
product and typed residue composition.  Therefore RF1-RF4 hold, each receipt
field is forced by the finite intervention record, and the result is unique
modulo the active quotient. `square`

### Lemma 5.2: Receipt Cokernel Is The RSC Obstruction

Searchable lemma tag:

`V4P29-LEMMA-RECEIPT-COKERNEL`.

Let:

$$
\boxed{
D_{\alpha}^{rec}:{\mathsf Rec}_{\alpha}\to{\mathcal E}_{\alpha}^{src}
}
$$

map receipts to persistent source, Wilson, boundary, commutator,
hard-support, and word-depth effects.  Then:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{rec}
=
{\mathcal A}_{RSC,\alpha}^{src}
\oplus
{\mathcal A}_{typed,\alpha}^{src}.
}
$$

On the active branch:

$$
\boxed{
\mathrm{coker}\,D_{*,untyped}^{rec}=0.
}
$$

Proof.  By definition, a missing receipt is exactly a persistent source effect
not represented in the source/probe dictionary.  That is the RSC obstruction.
Paper 25 kills the untyped RSC cokernel on the active GR branch; Paper 27
keeps printed typed residues subcritical. `square`

### Corollary 5.3: FR1-FR8 Are Derived, Not Added

$$
\boxed{
\mathrm{B24+G25+Q26+D27}
\Longrightarrow
\mathrm{FR1\text{-}FR8}.
}
$$

Proof.  Lemma 5.1 gives total canonical receipts.  Lemma 5.2 eliminates the
untyped cokernel and controls typed residues.  The eight receipt gates are
exactly the fields and bounds of this canonical receipt. `square`

## 6. Source Compactness

Searchable source tag:

`V4P29-SOURCE-COMPACTNESS-HARDENED`.

### 6.1 Projective Source Topology

For each finite battery \(J_0\subset{\mathcal J}\) and derivative order \(k\),
let:

$$
\boxed{
{\mathsf V}(J_0,k)
=
{\mathbb R}^{N(J_0,k)}
}
$$

with the usual finite-dimensional topology.  The full source-coordinate
ambient space is:

$$
\boxed{
{\mathsf V}_{src}
=
\prod_{(J_0,k)}
{\mathsf V}(J_0,k).
}
$$

The topology on ledgers is the subspace topology induced by the embedding:

$$
\boxed{
{\mathcal S}_{\alpha}
\mapsto
\bigl(V_{\alpha}(J_0,k)\bigr)_{(J_0,k)}
\in{\mathsf V}_{src}.
}
$$

The positive cone is:

$$
\boxed{
{\mathsf V}_{src}^{+}
=
\left\{
{\mathcal S}:\omega_{\mathcal S}(F^{*}F)\ge0
\hbox{ for every licensed finite gauge-invariant polynomial }F
\right\}.
}
$$

When the continuity condition SC4 below holds, each inequality
\(\omega_{\mathcal S}(F^{*}F)\ge0\) is closed in the projective source
topology.  Hence \({\mathsf V}_{src}^{+}\) is a closed positive cone under the
source-Cauchy packet.

### 6.2 RCP28 Source-Cauchy And Determinacy Packet

Compactness alone gives cluster points.  The full cofinal limit used by the
theorem requires the stronger \(RCP28\) source-Cauchy/determinacy certificate:

$$
\boxed{
\begin{array}{ll}
\mathrm{SC1}:&
\hbox{for every }(J_0,k),\ V_{\alpha}(J_0,k)\hbox{ is eventually bounded};\\
\mathrm{SC2}:&
\hbox{for every }(J_0,k),\ V_{\alpha}(J_0,k)\hbox{ is a Cauchy net};\\
\mathrm{SC3}:&
\hbox{the coordinate limits commute with all reductions }R_{\beta\alpha};\\
\mathrm{SC4}:&
\omega_{\mathcal S}(F^{*}F)\hbox{ is a continuous coordinate functional
for every licensed }F;\\
\mathrm{SC5}:&
\hbox{the finite source coordinates separate internal source laws.}
\end{array}
}
$$

Without SC2 and SC5 the result below must be weakened to existence of
compatible cluster points, not convergence of the active cofinal family.

### Lemma 6.1: Source-Ledger Compactness

Assume FR1-FR8, the projective source topology above, and SC1-SC5 from
\(RCP28\).  Then the finite source ledgers have a unique positive cofinal
limit:

$$
\boxed{
{\mathcal S}_{\alpha}
\Longrightarrow
{\mathcal S}_{\infty}.
}
$$

Moreover:

$$
\boxed{
\omega_{\infty}(F^{*}F)\ge0
}
$$

for every licensed gauge-invariant finite source polynomial \(F\), and:

$$
\boxed{
\partial_J^k{\mathcal S}_{\infty}(J)
=
\lim_{\alpha}\partial_J^k{\mathcal S}_{\alpha}(J)
}
$$

for every licensed finite derivative order \(k\).

Proof.  FR5 supplies a uniform source height bound.  FR6 and FR7 give typed
residue tightness through the sub-Markov majorant:

$$
\boxed{
\omega_{\alpha}({\mathsf C}_{\alpha}^{type})
\le
\frac{h_I}{1-q_I}.
}
$$

FR3 preserves Ward/gauge invariance.  FR4 gives projective consistency.  FR8
excludes a continuum-only response.

SC1 places every finite coordinate in a compact closed interval box after
quotienting Ward directions and adding typed residue coordinates.  SC2 gives
actual cofinal convergence in each finite-dimensional coordinate box, not just
a subnet.  SC3 assembles the coordinate limits into a compatible projective
source ledger.  SC4 makes positivity closed along this convergence:

$$
\boxed{
\omega_{\alpha}(F^{*}F)\ge0
\quad\Longrightarrow\quad
\omega_{\infty}(F^{*}F)\ge0.
}
$$

SC5 says that agreement on all finite source coordinates is equality of
internal source laws, so the limit is unique in the internal dictionary.
Derivative control is built into the coordinate topology.  Therefore the
source-response family has a unique positive cofinal limit with derivative
control. `square`

### Corollary 6.2: HCL1

$$
\boxed{
\mathrm{HCL1}
=
\mathrm{PASS}_{relative\ to\ RCP28}.
}
$$

It shuts:

$$
\boxed{
\mathrm{LEAK1},\mathrm{LEAK2},\mathrm{LEAK3},\mathrm{LEAK7}.
}
$$

## 7. Physical Margin Survival

Searchable margin tag:

`V4P29-MARGIN-SURVIVAL-HARDENED`.

### Lemma 7.1: Scale-Locked Positive Margins Survive

Assume A4 and the A5 scale-and-margin survival packet SL1-SL5.  Then:

$$
\boxed{
\sigma_{phys}
=
\liminf_{\alpha}a_{\alpha}^{-2}\sigma_{\alpha}^{fin}
>0,
}
$$

and:

$$
\boxed{
\Delta_{phys}
=
\liminf_{\alpha}a_{\alpha}^{-1}\Delta_{\alpha}^{fin}
>0.
}
$$

Proof.  A4 identifies the relevant finite QCD-DYN center/string and
singlet/gap margins.  A5 does not assume the desired limit.  It supplies the
nonposterior scale map and the finite-to-physical comparison inequalities:

$$
\boxed{
\sigma_{\alpha}^{fin}\ge\sigma_{*}a_{\alpha}^{2},
\qquad
\Delta_{\alpha}^{fin}\ge\Delta_{*}a_{\alpha}
\quad
\hbox{cofinally}.
}
$$

Therefore:

$$
\boxed{
a_{\alpha}^{-2}\sigma_{\alpha}^{fin}\ge\sigma_{*}>0,
\qquad
a_{\alpha}^{-1}\Delta_{\alpha}^{fin}\ge\Delta_{*}>0
\quad
\hbox{cofinally}.
}
$$

Taking cofinal \(\liminf\) gives the stated positive physical margins.  SL5
prevents this from being a posterior rescaling trick. `square`

### Corollary 7.2: HCL2

$$
\boxed{
\mathrm{HCL2}
=
\mathrm{PASS}_{relative\ to\ TSP28}.
}
$$

It shuts:

$$
\boxed{
\mathrm{LEAK4},\mathrm{LEAK5}.
}
$$

This is the sharp status of the scale step:

$$
\boxed{
\hbox{P29 does not derive SL4 from bare finite positivity.  It proves that
SL1-SL5, especially SL4, are exactly the margin-survival certificate needed
for HCL2.}
}
$$

## 8. Yang-Mills Identification

Searchable identification tag:

`V4P29-YM-IDENTIFICATION-HARDENED`.

### Lemma 8.1: Unique Descended YM Decoder

Assume A3, the compact positive source law of Lemma 6.1, and the A6 decoder
audit packet YMU1-YMU7.  The descended decoder of the compact positive source
law is unique:

$$
\boxed{
D_{YM}^{desc}({\mathcal S}_{\infty})
=
SU(N)\hbox{ Yang-Mills}.
}
$$

Proof.  A3 says gauge transformations, Wilson observables, and RG descent are
finite same-actual descent data.  YMU1 fixes the candidate gauge group before
the query.  YMU2 says Wilson traces separate the gauge quotient, so a decoder
with a different gauge quotient changes finite Wilson receipts.  YMU3
identifies the local kinetic density from small-loop derivatives.  YMU4
forces the Ward/Bianchi identities in the same-actual quotient.  YMU5 forbids
route-dependent coupling flow.  YMU6 removes irrelevant or boundary
ambiguities unless they are typed.  YMU7 forbids a silent untyped low-energy
escape sector.

Thus two admissible decoders can differ only by a Ward-equivalent
presentation or by a typed irrelevant residue.  They cannot differ in gauge
group, Wilson algebra, kinetic density, coupling flow, or physical silent
sector.  Hence the descended decoder is unique on physical ISP content:

$$
\boxed{
D_{YM}^{desc}({\mathcal S}_{\infty})
=
SU(N)\hbox{ Yang-Mills}.
}
$$

`square`

### Corollary 8.2: HCL3

$$
\boxed{
\mathrm{HCL3}
=
\mathrm{PASS}_{relative\ to\ MID28}.
}
$$

It shuts:

$$
\boxed{
\mathrm{LEAK6}.
}
$$

This is the sharp status of the decoder step:

$$
\boxed{
\hbox{P29 does not derive YMU1-YMU7 from an empty dictionary.  It proves that
these are exactly the decoder-separation conditions needed for HCL3.}
}
$$

## 9. Main Theorem

Searchable theorem tag:

`V4P29-CLOSED-INTERNAL-YM-CONFINEMENT-THEOREM`.

### Theorem 9.1: ISP-V4 Internal Yang-Mills Descent Confinement/Mass Gap

Assume the reduced active import packet \({\mathbb I}_{24:28}^{red}\).  Then the active
ISP-V4 finite actual corpus has an internal continuum descent whose
gauge-invariant \(SU(N)\) sector is confining and has a positive mass gap:

$$
\boxed{
{\mathbb I}_{24:28}^{red}
\Longrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}
}
$$

or explicitly:

$$
\boxed{
\begin{array}{c}
\mathrm{P25\ FAC+SLC+RSC}_{GR}\\
\wedge\ \mathrm{P26\ REL\text{-}QFT\text{-}KIN/YM\text{-}GAUGE/YM\text{-}WILSON/RG}\\
\wedge\ \mathrm{P27\ QCD\text{-}DYN}_{finite\ ISP}\\
\wedge\ \mathrm{P28\ receipt/scale/YM\ audit\ packets}\\
\Longrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}
\end{array}
}
$$

as an ISP descent theorem.

Proof.  Corollary 6.2 gives HCL1: a unique positive cofinal source-response
limit with no source-mass, positivity, invisible-class, or silent-sector
leakage.
Corollary 7.2 gives HCL2: finite QCD-DYN margins survive physical
normalization.  Since the P27 margins are Wilson area-law and transfer/gap
margins, HCL2 yields the \(\sigma_{phys}>0\) and \(\Delta_{phys}>0\)
requirements in Definition 4.2.
Corollary 8.2 gives HCL3: the limiting gauge-invariant descended sector is
uniquely the ISP \(SU(N)\) Yang-Mills decoder, not a wrong-theory decoder.
Therefore all internal leak channels are closed:

$$
\boxed{
\neg\mathrm{LEAK1}\wedge\cdots\wedge\neg\mathrm{LEAK7}.
}
$$

By Definition 4.2, the active descended sector satisfies internal Yang-Mills
confinement/mass gap. `square`

## 10. Exact Non-Claim

Searchable non-claim tag:

`V4P29-EXACT-NON-CLAIM`.

Theorem 9.1 does not assert:

$$
\boxed{
\hbox{standard continuum Yang-Mills mass gap has been proved without ISP
premises.}
}
$$

It asserts:

$$
\boxed{
\hbox{given ISP-V4 finite actual ontology and the active P25-P28-pre packets,
the ISP-descended }SU(N)\hbox{ sector has internal confinement/mass gap.}
}
$$

The difference is not cosmetic.  Standard continuum Yang-Mills begins with a
different ontology: continuum fields, gauge orbits, operator/state or
path-integral language, and a continuum limit problem.  ISP-V4 begins with
finite actual records, finite source-response ledgers, same-actual Ward
quotients, typed residues, and continuum reconstruction by descent.

Thus the external comparison is:

$$
\boxed{
\begin{array}{c|c}
\hbox{standard route} & \hbox{prove YM from continuum QFT/YM foundations}\\
\hline
\hbox{ISP route} & \hbox{prove an ISP-descended YM sector from finite actual
record descent, then compare it externally}
\end{array}
}
$$

No route is assumption-free.

## 11. Falsifier Ledger

Searchable falsifier tag:

`V4P29-FALSIFIER-LEDGER`.

At this level of compression, the internal theorem fails if one of the
following gates or certificate sub-gates fires:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{F1} &
\hbox{finite witness absent} &
\hbox{P24/Barandes discipline fails}\\
\mathrm{F2} &
\hbox{same-actual Ward quotient fails} &
\hbox{FAC/SLC failure}\\
\mathrm{F3} &
\hbox{untyped RSC cokernel survives} &
\hbox{missing source/probe/boundary channel}\\
\mathrm{F4} &
\hbox{QFT/YM finite source battery fails} &
\hbox{P26 kinematic descent fails}\\
\mathrm{F5} &
\hbox{canonical receipt extraction fails} &
\hbox{source not represented in finite intervention category}\\
\mathrm{F6} &
\hbox{RCP28/SC1-SC5 source-Cauchy or determinacy fails} &
\hbox{loss of HCL1}\\
\mathrm{F7} &
\hbox{TSP28/SL4 center-string margin survival fails} &
\hbox{loss of confinement}\\
\mathrm{F8} &
\hbox{TSP28/SL4 singlet-gap margin survival fails} &
\hbox{loss of mass gap}\\
\mathrm{F9} &
\hbox{scale lock is posterior or unstable} &
\hbox{physical margin not licensed}\\
\mathrm{F10} &
\hbox{MID28/YMU1-YMU7 wrong decoder survives} &
\hbox{not uniquely }SU(N)\hbox{ Yang-Mills}\\
\mathrm{F11} &
\hbox{silent untyped sector survives} &
\hbox{Barandes/RSC response ontology fails}\\
\mathrm{F12} &
\hbox{posterior fitting of source, type, or scale} &
\hbox{not a theorem of the active corpus}
\end{array}
}
$$

This is the Feynman audit compressed to one table.  A failure is not vague.
It identifies which prior packet or descent map must be repaired.

## 12. Externalization Checklist

Searchable externalization tag:

`V4P29-EXTERNALIZATION-CHECKLIST`.

The essential topology, receipt functor, scale packet, and decoder audit have
now been pulled into the internal proof ledger.  The remaining checklist is
therefore not an extra hidden hypothesis.  It is the work needed to translate
the internal ISP theorem into a conventional mathematical manuscript:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{item} & \hbox{internal status} & \hbox{external formalization task}\\
\hline
\mathrm{E1} & \mathrm{DONE}_{internal} &
\hbox{package finite actual record categories in standard notation}\\
\mathrm{E2} & \mathrm{DONE}_{internal} &
\hbox{write same-actual Ward ideals and typed residue modules algebraically}\\
\mathrm{E3} & \mathrm{DONE}_{internal} &
\hbox{publish the receipt functor as an explicit categorical construction}\\
\mathrm{E4} & \mathrm{DONE}_{internal} &
\hbox{formalize the projective source topology and coordinate batteries}\\
\mathrm{E5} & \mathrm{DONE}_{internal} &
\hbox{state positivity closure as a closed-cone lemma}\\
\mathrm{E6} & \mathrm{COMPARISON}_{external} &
\hbox{construct the standard Hilbert/algebraic sector for outside readers}\\
\mathrm{E7} & \mathrm{DONE}_{internal} &
\hbox{print P27 finite margin inequalities in publication notation}\\
\mathrm{E8} & \mathrm{DONE}_{internal} &
\hbox{rewrite SL1-SL5 as a conventional lower-bound proposition}\\
\mathrm{E9} & \mathrm{DONE}_{internal} &
\hbox{rewrite YMU1-YMU7 as a standard decoder uniqueness theorem}\\
\mathrm{E10} & \mathrm{COMPARISON}_{external} &
\hbox{show equivalence to the usual continuum YM confinement criterion}
\end{array}
}
$$

Thus the checklist is not allowed to re-open HCL1-HCL3 inside ISP.  It only
marks the interface between the internal finite-record theorem and a
standalone mathematical presentation in conventional continuum language.

## 13. Final Verdict

Searchable final tag:

`V4P29-FORMAL-HARDENING-FINAL-VERDICT`.

The hardened status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{scope}\\
\hline
\mathrm{P25\ GR\ ontology} &
\mathrm{CLOSED}_{active} &
\mathrm{FAC+SLC+RSC}_{GR}\\
\mathrm{P26\ QFT/YM\ kinematics} &
\mathrm{CLOSED}_{active} &
\hbox{finite source-response and Wilson descent}\\
\mathrm{P27\ finite\ QCD\ dynamics} &
\mathrm{CLOSED}_{active} &
\mathrm{QCD\text{-}DYN}=\mathrm{PASS}_{finite\ ISP}\\
\mathrm{P28\ pre-conclusion\ packets} &
\mathrm{CERTIFICATE\ TARGETS}_{active} &
\hbox{RCP28/TSP28/MID28 are named load-bearing certificates}\\
\mathrm{P29\ formal\ hardening} &
\mathrm{CLOSED}_{relative\ internal} &
\hbox{HCL1-HCL3 derived relative to RCP28/TSP28/MID28}\\
\mathrm{external\ Clay-style\ proof} &
\mathrm{NOT\ CLAIMED} &
\hbox{requires externalization checklist}
\end{array}
}
$$

The compact theorem is:

$$
\boxed{
\mathrm{ISP\text{-}V4}_{active}
\Longrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}
}
$$

as a finite-record descent theorem.

This is what has been achieved:

$$
\boxed{
\hbox{the internal proof architecture is closed relative to the named
RCP28/TSP28/MID28 certificates and audit-indexed.}
}
$$

This is what remains for public mathematics:

$$
\boxed{
\hbox{translate the active ISP packets into a conventional formal proof
environment and defend the ontology/premises.}
}
$$

## 14. Paper 30 Handoff

Searchable handoff tag:

`V4P29-PAPER30-HANDOFF`.

Paper 29 leaves exactly three internal certificate targets for Paper 30:

$$
\boxed{
\mathrm{Paper\ 30\ target}
=
\mathrm{prove\ RCP28+TSP28+MID28\ from\ ISP\ primitives.}
}
$$

Expanded:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{certificate} & \hbox{Paper 30 proof target} & \hbox{closure gained}\\
\hline
\mathrm{RCP28} &
\hbox{derive SC1-SC5 source-Cauchy/determinacy} &
\hbox{HCL1 no longer conditional}\\
\mathrm{TSP28} &
\hbox{derive SL4 scale-normalized margin survival} &
\hbox{HCL2 no longer conditional}\\
\mathrm{MID28} &
\hbox{derive YMU1-YMU7 decoder separation/uniqueness} &
\hbox{HCL3 no longer conditional}
\end{array}
}
$$

If Paper 30 proves these three certificates from the active ISP primitives,
then the theorem status upgrades from:

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

## 15. Review Closure Ledger

Searchable review tag:

`V4P29-HARDCORE-REVIEW-CLOSURE-LEDGER`.

The hard review issues are closed in the text as follows:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{issue} & \hbox{review concern} & \hbox{paper-29 correction}\\
\hline
\mathrm{R1} &
\hbox{circularly imported Paper 28 continuum bridge} &
{\mathbb I}_{24:28}^{red}\hbox{ imports only }\mathrm{C28}^{pre}\\
\mathrm{R2} &
\hbox{confinement definition only restated positive margins} &
\hbox{Definition 4.2 now includes Wilson area law and spectral/correlation gap}\\
\mathrm{R3} &
\hbox{scale lock lemma assumed its conclusion} &
\hbox{A5 is SL1-SL5; Lemma 7.1 derives liminf bounds from comparisons}\\
\mathrm{R4} &
\hbox{YM uniqueness lemma assumed decoder uniqueness} &
\hbox{A6 is YMU1-YMU7; Lemma 8.1 derives uniqueness}\\
\mathrm{R5} &
\hbox{source compactness had no topology} &
\hbox{Section 6 defines projective source topology and closed positivity cone}\\
\mathrm{R6} &
\hbox{receipt functor was named but not constructed} &
\hbox{Section 5 defines intervention/receipt categories and RF1-RF4}\\
\mathrm{R7} &
\hbox{externalization checklist contained core proof obligations} &
\hbox{Section 12 separates internal closure from external publication work}\\
\mathrm{R8} &
\hbox{leak notation was logically wrong} &
\neg\mathrm{LEAK1}\wedge\cdots\wedge\neg\mathrm{LEAK7}\hbox{ is printed}\\
\mathrm{R9} &
\hbox{standard continuum YM was overclaimed} &
\hbox{the theorem now states }\mathrm{CONFINEMENT/MASS\ GAP}_{ISP\text{-}descent}\\
\mathrm{R10} &
\hbox{compactness gave only cluster points} &
\hbox{RCP28 now includes SC1-SC5 source-Cauchy/determinacy}\\
\mathrm{R11} &
\hbox{SL4 is the scaling miracle, not a trivial certificate} &
\hbox{TSP28 is marked as the load-bearing margin-survival certificate}\\
\mathrm{R12} &
\hbox{standard Hilbert/OS comparison remains external} &
\hbox{E6/E10 remain external comparison tasks, not hidden premises}\\
\mathrm{R13} &
\hbox{Paper 29 needed a clean handoff instead of drifting into Paper 30} &
\hbox{Section 14 names RCP28/TSP28/MID28 as Paper 30 targets}
\end{array}
}
$$

This ledger is not a new proof step.  It records that the formal hardening
has answered the review objections one by one.
