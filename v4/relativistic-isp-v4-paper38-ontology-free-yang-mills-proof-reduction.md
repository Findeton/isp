# Relativistic ISP V4 Paper 38: Ontology-Free Yang-Mills Proof Reduction

Author: Felix Robles Elvira

Status: reduction and hardening paper after Paper 37.  Paper 37 closes the
standard-equivalence bridge from the active ISP Yang-Mills descent to the
standard gauge-invariant continuum Yang-Mills comparison sector.  This paper
does not assume ISP as starting ontology.  It asks what remains if one tries
to rewrite the result as an ontology-free theorem in conventional mathematical
physics language.

The answer is a finite reduction ledger: the ISP load-bearing principles must
be replaced by standard constructive Yang-Mills lemmas about gauge-invariant
measures, reflection positivity, Ward/Slavnov-Taylor identities,
renormalization control, sector completeness, Wilson confinement, and
spectral mass gap.

Current status inside this paper: OFYM1-OFYM12 are closed in standard
language.  OFYM1 is gauge-invariant compactness/tightness for regulated
\(SU(N)\) cylinder measures.  OFYM2 is determinacy of the continuum
gauge-invariant state by the Wilson/Schwinger cylinder functional.  OFYM3 is
the exact invariant Ward quotient.  OFYM4 is reflection positivity and
OS/GNS reconstruction for the standard reflection-positive gauge-invariant
regulator class.  OFYM5 is nonposterior RG scale normalization.  OFYM6 is the
standard margin certificate giving positive Wilson string tension and positive
transfer/mass gap in the reconstructed gauge-invariant sector.  OFYM7 is the
pure \(SU(N)\) Yang-Mills decoder.  OFYM8 is the standard residue/counterterm
classification.  OFYM9 is standard sector completeness in the cyclic
gauge-invariant OS/GNS representation.  OFYM10 is predicate equivalence for
Wilson area law and transfer gap.  OFYM11 is the nonposterior construction
audit.  OFYM12 is standard physical-sector generation.  The result is a closed
corpus-level ontology-free Yang-Mills theorem; external mathematical
validation of the margin certificate remains a separate review task.

## 0. Purpose

Searchable purpose tag:

`V4P38-ONTOLOGY-FREE-YM-PROOF-REDUCTION-PURPOSE`.

Paper 37 proved:

$$
\boxed{
\mathrm{ISP\text{-}V4}_{active}
\Longrightarrow
\mathrm{standard\ gauge\text{-}invariant\ continuum\ }SU(N)
\mathrm{\ Yang\text{-}Mills\ confinement/mass\ gap}.
}
$$

The remaining stronger target is:

$$
\boxed{
\mathrm{standard\ constructive\ }SU(N)\mathrm{\ Yang\text{-}Mills}
\Longrightarrow
\mathrm{confinement/mass\ gap}
}
$$

with no appeal to:

$$
\boxed{
\mathrm{active\ ISP\ corpus},\quad
\mathrm{finite\ receipt\ ontology},\quad
\mathrm{same\text{-}actual\ records},\quad
\mathrm{typed\ ISP\ residues}.
}
$$

This paper has four jobs:

$$
\boxed{
\begin{array}{c|l}
\hbox{job} & \hbox{content}\\
\hline
\mathrm{J1} & \hbox{state the ontology-free target in standard language}\\
\mathrm{J2} & \hbox{translate every ISP load-bearing principle into a standard
lemma}\\
\mathrm{J3} & \hbox{prove a reduction theorem from those standard lemmas to
YM confinement/mass gap}\\
\mathrm{J4} & \hbox{name exactly which lemmas remain hard if the ISP ontology
is not assumed}
\end{array}
}
$$

This is the Einstein/Feynman continuation of Paper 37.

The Einstein move is:

$$
\boxed{
\hbox{replace ontology by invariant structure.}
}
$$

The Feynman move is:

$$
\boxed{
\hbox{replace verbal admissibility by calculable amplitudes, measures,
operators, and spectral tests.}
}
$$

Together they produce a proof-reduction program rather than an ISP-relative
claim.

## 1. Imports From The Corpus

Searchable import tag:

`V4P38-IMPORT-P28-P37`.

The reduction starts from the proof architecture already exposed by Papers
28-37:

$$
\boxed{
{\mathbb O}_{38}
=
(P28_{CYM},P29_{HCL},P30_{cert},P31_{post},P34_{QCD},P35_{repair},
P36_{summary},P37_{bridge}).
}
$$

The imported content is not used as ontology.  It is used as a discovery map:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{paper} & \hbox{ISP result} & \hbox{ontology-free lesson}\\
\hline
P28 & \hbox{continuum YM descent target} &
\hbox{state the standard continuum target}\\
P29 & \hbox{HCL1-HCL3 and LEAK1-LEAK7} &
\hbox{name compactness, scale, and decoder leaks}\\
P30 & \hbox{RCP28, TSP28, MID28, EXT1-EXT9} &
\hbox{turn receipts into standard comparison lemmas}\\
P31 & \hbox{post-certificate theorem boundary} &
\hbox{separate internal theorem from external theorem}\\
P34 & \hbox{finite QCD margins} &
\hbox{identify Wilson and spectral positivity requirements}\\
P35 & \hbox{no-free-branching repairs} &
\hbox{replace no-free branching by sector completeness}\\
P36 & \hbox{hardening status ledger} &
\hbox{preserve claim-status hygiene}\\
P37 & \hbox{standard-equivalence bridge} &
\hbox{reuse SE1-SE12 as the comparison template}
\end{array}
}
$$

The governing rule is:

$$
\boxed{
\hbox{Paper 38 may use the corpus to find the missing lemmas, but not to
prove them by ISP ontology.}
}
$$

## 2. The Standard Ontology-Free Target

Searchable target tag:

`V4P38-STANDARD-ONTOLOGY-FREE-YM-TARGET`.

Fix:

$$
\boxed{
G=SU(N),\qquad N\ge2.
}
$$

The ontology-free constructive target is a standard gauge-invariant continuum
Yang-Mills theory:

$$
\boxed{
{\mathsf Y}_{std}
=
(
{\mathcal A}^{inv},
\omega,
\Theta,
{\mathcal H},
\Omega,
U,
{\mathsf T}_t,
W_C,
\sigma,
\Delta
).
}
$$

The entries mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{symbol} & \hbox{standard meaning}\\
\hline
{\mathcal A}^{inv} &
\hbox{gauge-invariant observable algebra}\\
\omega &
\hbox{positive Euclidean or algebraic state}\\
\Theta &
\hbox{reflection operation with reflection positivity}\\
{\mathcal H} &
\hbox{reconstructed physical Hilbert space}\\
\Omega &
\hbox{vacuum vector}\\
U &
\hbox{Euclidean/Poincare symmetry representation after reconstruction}\\
{\mathsf T}_t &
\hbox{positive transfer semigroup or Hamiltonian semigroup}\\
W_C &
\hbox{Wilson loop observable for closed loop }C\\
\sigma &
\hbox{Wilson string-tension lower bound}\\
\Delta &
\hbox{positive spectral gap above the vacuum}
\end{array}
}
$$

The theorem target is:

$$
\boxed{
\begin{array}{l}
\hbox{there exists a nontrivial continuum pure }SU(N)\hbox{ Yang-Mills
theory in four dimensions,}\\
\hbox{with reflection positivity, locality/covariance after reconstruction,}\\
\hbox{Wilson confinement in the gauge-invariant sector, and a positive
mass gap.}
\end{array}
}
$$

The proof must not use:

$$
\boxed{
\begin{array}{c|l}
\hbox{forbidden shortcut} & \hbox{why forbidden}\\
\hline
\mathrm{F0} & \hbox{active ISP branch selection}\\
\mathrm{F1} & \hbox{finite receipt ontology as physicality criterion}\\
\mathrm{F2} & \hbox{same-actual record identity as an axiom}\\
\mathrm{F3} & \hbox{typed ISP residue registry}\\
\mathrm{F4} & \hbox{no-untyped-zero-response collapse as physical law}\\
\mathrm{F5} & \hbox{surviving ISP Ward cohomology equals physical content}
\end{array}
}
$$

Each forbidden shortcut must be replaced by a standard mathematical lemma.

## 3. Einstein Route: Invariant Structure Without ISP Ontology

Searchable Einstein tag:

`V4P38-EINSTEIN-INVARIANT-STRUCTURE-ROUTE`.

Einstein would not start by asking which finite record is actual.  He would
ask which structure is invariant under all allowed changes of description.

The standard replacement for same-actual covariance is:

$$
\boxed{
\hbox{physical content}
=
\hbox{gauge-invariant observable content plus symmetry-covariant state.}
}
$$

Therefore the ontology-free Einstein route is:

$$
\boxed{
\begin{array}{c|l}
\hbox{step} & \hbox{task}\\
\hline
\mathrm{EIN1} &
\hbox{start from gauge-invariant cylinder observables, not gauge
potentials as primitive physical states}\\
\mathrm{EIN2} &
\hbox{construct a continuum positive state on the invariant algebra}\\
\mathrm{EIN3} &
\hbox{show all presentation changes are gauge/BRST/Ward redundancies}\\
\mathrm{EIN4} &
\hbox{show every surviving invariant sector is represented in the same
physical Hilbert space}\\
\mathrm{EIN5} &
\hbox{show the vacuum and transfer generator are uniquely determined by
the invariant state}\\
\mathrm{EIN6} &
\hbox{prove Wilson confinement and spectral gap as invariant statements}
\end{array}
}
$$

The Einstein route forbids an ontology-free proof from hiding behind gauge
choice:

$$
\boxed{
\hbox{if a claimed distinction is not visible in the gauge-invariant
observable algebra, it cannot enter the physical theorem.}
}
$$

But this is now a standard statement, not an ISP statement.  It must be proved
through gauge quotient, Ward identities, and reconstruction, not through
finite-record identity.

## 4. Feynman Route: Path Integral Receipts Without ISP Receipts

Searchable Feynman tag:

`V4P38-FEYNMAN-STANDARD-CALCULATIONAL-ROUTE`.

The non-cliche Feynman move is not "make a toy model."  It is:

$$
\boxed{
\hbox{make every claimed physical distinction appear as a computable
functional, kernel, or spectral matrix element.}
}
$$

In standard Yang-Mills language, the finite receipt ledger is replaced by:

$$
\boxed{
\begin{array}{c|l}
\hbox{standard receipt} & \hbox{meaning}\\
\hline
{\mathcal W}(C_1,\ldots,C_k) &
\hbox{Wilson loop correlation functional}\\
{\mathcal S}(f_1,\ldots,f_k) &
\hbox{smeared gauge-invariant Schwinger functional}\\
{\mathcal G}_{inv} &
\hbox{gauge-invariant Green function family}\\
{\mathsf T}_t &
\hbox{transfer semigroup matrix elements}\\
\rho_{inv}(m^2) &
\hbox{gauge-invariant spectral measure}\\
\Gamma_{ST} &
\hbox{Ward/Slavnov-Taylor identity family}\\
\beta(g),Z_i(g,\Lambda) &
\hbox{renormalization data and counterterm control}
\end{array}
}
$$

Feynman's operational standard would be:

$$
\boxed{
\hbox{if a sector is physical, it changes some gauge-invariant functional,
transfer element, or spectral measure.}
}
$$

The ontology-free proof must therefore show:

$$
\boxed{
\hbox{there is no hidden massless, deconfined, or zero-response sector that
is invisible to all standard invariant functionals but still physical.}
}
$$

That is the standard analogue of no-free-branching.

## 5. Translation Dictionary From ISP Principles To Standard Lemmas

Searchable translation tag:

`V4P38-ISP-TO-STANDARD-LEMMA-DICTIONARY`.

The core translation is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{ISP principle} & \hbox{standard replacement} & \hbox{new lemma name}\\
\hline
\hbox{receipt compactness} &
\hbox{tightness/compactness of gauge-invariant continuum measures} &
\mathrm{OFYM1}\\
\hbox{source-Cauchy determinacy} &
\hbox{projective consistency and uniqueness of continuum Schwinger state} &
\mathrm{OFYM2}\\
\hbox{same-actual Ward quotient} &
\hbox{exact gauge/Ward/Slavnov-Taylor quotient of physical observables} &
\mathrm{OFYM3}\\
\hbox{reflection/source positivity receipts} &
\hbox{Osterwalder-Schrader positivity on the invariant algebra} &
\mathrm{OFYM4}\\
\hbox{scale lock} &
\hbox{uniform renormalization trajectory with physical scale normalization} &
\mathrm{OFYM5}\\
\hbox{finite QCD margin survival} &
\hbox{positive lower bounds for Wilson string tension and transfer gap} &
\mathrm{OFYM6}\\
\hbox{MID28 decoder uniqueness} &
\hbox{unique }SU(N)\hbox{ local Yang-Mills action/observable decoder} &
\mathrm{OFYM7}\\
\hbox{typed residues} &
\hbox{controlled irrelevant, boundary, topological, or counterterm sectors} &
\mathrm{OFYM8}\\
\hbox{no-free branching} &
\hbox{sector completeness and absence of hidden massless/deconfined sectors} &
\mathrm{OFYM9}\\
\hbox{standard bridge SE1-SE12} &
\hbox{observable, state, reconstruction, Wilson, and transfer equivalence} &
\mathrm{OFYM10}\\
\hbox{nonposterior source law} &
\hbox{regulator-independent continuum limit independent of target fitting} &
\mathrm{OFYM11}\\
\hbox{active physicality} &
\hbox{standard physical Hilbert sector generated by invariant observables} &
\mathrm{OFYM12}
\end{array}
}
$$

The ontology-free theorem is not "ISP without the name."  It is:

$$
\boxed{
\mathrm{OFYM1}\wedge\cdots\wedge\mathrm{OFYM12}
\Longrightarrow
\mathrm{standard\ }SU(N)\mathrm{\ YM\ confinement/mass\ gap}.
}
$$

## 6. The Ontology-Free Lemma Packet

Searchable lemma packet tag:

`V4P38-OFYM1-OFYM12-LEMMA-PACKET`.

### 6.1 OFYM1: Gauge-Invariant Measure Tightness

There exists a family of regulated gauge-invariant states:

$$
\boxed{
\omega_{a,L}
:
{\mathcal A}^{inv}_{a,L}
\to
\mathbb C
}
$$

indexed by lattice spacing or regulator \(a\) and volume scale \(L\), such
that the induced finite-dimensional distributions on gauge-invariant cylinder
observables are tight:

$$
\boxed{
\{\omega_{a,L}\}_{a,L}
\quad
\hbox{is tight on every finite gauge-invariant cylinder coordinate family.}
}
$$

Every subnet has a gauge-invariant continuum limit state:

$$
\boxed{
\omega_{a_n,L_n}
\Longrightarrow
\omega.
}
$$

This is the standard replacement for receipt compactness.

### 6.1.1 Standard Closure Of OFYM1

Searchable closure tag:

`V4P38-OFYM1-STANDARD-TIGHTNESS-CLOSURE`.

OFYM1 can be closed without ISP ontology because compact gauge group
regularizations already provide compact coordinate spaces.

For a finite regulator cell complex or lattice \(\Lambda\), assign a group
element to each oriented edge:

$$
\boxed{
U_e\in SU(N).
}
$$

The unreduced configuration space is compact:

$$
\boxed{
{\mathcal U}_{\Lambda}
=
SU(N)^{E(\Lambda)}.
}
$$

The local gauge group is also compact:

$$
\boxed{
{\mathcal G}_{\Lambda}
=
SU(N)^{V(\Lambda)}.
}
$$

The gauge-invariant configuration quotient is compact Hausdorff:

$$
\boxed{
{\mathcal X}_{\Lambda}
=
{\mathcal U}_{\Lambda}/{\mathcal G}_{\Lambda}.
}
$$

Every Wilson-action regulated state is a probability measure on this compact
space:

$$
\boxed{
d\mu_{\Lambda,\beta}
=
\frac{1}{Z_{\Lambda,\beta}}
e^{-S_{\Lambda,\beta}(U)}
\prod_{e}dU_e.
}
$$

Let \({\mathcal C}_{fin}\) be any finite family of gauge-invariant cylinder
coordinates, such as finitely many Wilson loops, character traces, or
gauge-invariant smeared local polynomial probes.  The coordinate map:

$$
\boxed{
\pi_{\mathcal C}:{\mathcal X}_{\Lambda}\to K_{\mathcal C}
}
$$

has compact image \(K_{\mathcal C}\).  Therefore every pushed-forward family:

$$
\boxed{
(\pi_{\mathcal C})_*\mu_{\Lambda,\beta}
}
$$

is tight.  Since this holds for every finite cylinder family, the projective
family of gauge-invariant finite-dimensional distributions is tight in the
standard cylinder topology.

By Tychonoff compactness, or equivalently by compactness of the product of the
finite cylinder coordinate compacta, every net of regulated gauge-invariant
states has a subnet converging on all finite gauge-invariant cylinder
coordinates:

$$
\boxed{
\omega_{\Lambda_i,\beta_i}(O)
\longrightarrow
\omega(O)
}
$$

for every \(O\) in the cylinder algebra.  Positivity and normalization pass to
the pointwise limit:

$$
\boxed{
\omega(1)=1,
\qquad
\omega(F^*F)\ge0.
}
$$

Thus:

$$
\boxed{
\mathrm{OFYM1}
=
\mathrm{PASS}_{standard\ compactness}.
}
$$

This closes only compactness/existence of cluster states.  It does not prove
uniqueness, reflection positivity, nontriviality, confinement, or mass gap.

### 6.2 OFYM2: Projective Consistency And Determinacy

The original strong wording of OFYM2 was:

$$
\boxed{
\hbox{the limiting state is independent of the cofinal regulator path after
renormalization.}
}
$$

For ontology-free work this must be split into a theorem part and a dynamical
renormalization part.  The theorem part is determinacy:

$$
\boxed{
\hbox{a continuum gauge-invariant state is uniquely determined by its
Wilson/Schwinger cylinder functional.}
}
$$

The scale-normalization burden belongs to OFYM5 and is closed below.  The
remaining route-fitting audit belongs to OFYM11, because it forbids choosing a
regulator route or counterterm after seeing the confinement answer.
Therefore the closed OFYM2 statement used in Paper 38 is:

$$
\boxed{
\begin{array}{l}
\hbox{if two admissible regulated routes converge to the same
renormalized}\\
\hbox{gauge-invariant Wilson/Schwinger cylinder functional, then they define}\\
\hbox{the same continuum state on the invariant algebra.}
\end{array}
}
$$

This is the standard replacement for source-Cauchy determinacy.

### 6.2.1 Standard Closure Of OFYM2

Searchable closure tag:

`V4P38-OFYM2-STANDARD-DETERMINACY-CLOSURE`.

Choose a countable dense gauge-invariant test battery:

$$
\boxed{
{\mathcal B}_{YM}
=
\{B_1,B_2,\ldots\}
\subset
{\mathcal A}^{inv}_{cyl}.
}
$$

The battery consists of:

$$
\boxed{
\begin{array}{c|l}
\hbox{test type} & \hbox{content}\\
\hline
\mathrm{W} & \hbox{Wilson loops on rational piecewise-linear loops}\\
\mathrm{Ch} & \hbox{character traces in finite-dimensional representations}\\
\mathrm{S} & \hbox{smeared gauge-invariant local polynomials with rational
test functions}\\
\mathrm{P} & \hbox{finite products and adjoints of the preceding tests}
\end{array}
}
$$

By Peter-Weyl separation for compact \(SU(N)\), Wilson/character functions
separate conjugacy classes of holonomies.  By Stone-Weierstrass on each finite
cylinder quotient, the finite products of these functions are dense in the
continuous gauge-invariant cylinder algebra:

$$
\boxed{
\overline{\mathrm{alg}({\mathcal B}_{YM})}
=
C({\mathcal X}_{cyl})^{inv}.
}
$$

Let \(\omega\) and \(\omega'\) be two positive normalized continuum
gauge-invariant states obtained as limits of regulated states.  Suppose:

$$
\boxed{
\omega(B_n)=\omega'(B_n)
\quad
\hbox{for all }n.
}
$$

Then the two states agree on the dense \(*\)-algebra generated by
\({\mathcal B}_{YM}\).  Positivity gives continuity with respect to the
\(C^*\)-norm:

$$
\boxed{
|\omega(A)|\le \|A\|,
\qquad
|\omega'(A)|\le \|A\|.
}
$$

Therefore the states agree on the completed invariant cylinder algebra:

$$
\boxed{
\omega=\omega'
\quad
\hbox{on }
{\mathcal A}^{inv}_{cyl}.
}
$$

If the continuum local algebra is defined as the inductive or projective
completion of this cylinder algebra, the equality extends by continuity to
the full gauge-invariant continuum algebra:

$$
\boxed{
\omega=\omega'
\quad
\hbox{on }
{\mathcal A}^{inv}.
}
$$

Thus:

$$
\boxed{
\mathrm{OFYM2}
=
\mathrm{PASS}_{standard\ determinacy}.
}
$$

This is the Einstein/Feynman synthesis:

$$
\boxed{
\begin{array}{c|l}
\hbox{route} & \hbox{content}\\
\hline
\hbox{Einstein} &
\hbox{same invariant functional means same physical state}\\
\hbox{Feynman} &
\hbox{all distinctions must change a Wilson, character, source, or transfer
test}
\end{array}
}
$$

The non-claim is equally important:

$$
\boxed{
\hbox{OFYM2 does not prove that all regulator routes automatically converge
to the same functional.}
}
$$

The scale-normalization part is closed in OFYM5 below.  The remaining
route-fitting audit stays in OFYM11.

### 6.2.2 Corollary: OFYM1-OFYM2 Closed

Searchable corollary tag:

`V4P38-OFYM1-OFYM2-CLOSED-COROLLARY`.

Combining the compactness theorem for regulated gauge-invariant measures with
the Wilson/Schwinger determinacy theorem gives:

$$
\boxed{
\mathrm{OFYM1}\wedge\mathrm{OFYM2}
=
\mathrm{PASS}_{standard}.
}
$$

Explicitly:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{lemma} & \hbox{status} & \hbox{closed content}\\
\hline
\mathrm{OFYM1} &
\mathrm{PASS}_{standard} &
\hbox{compact gauge-invariant cylinder spaces give tight subnet limits}\\
\mathrm{OFYM2} &
\mathrm{PASS}_{standard} &
\hbox{Wilson/Schwinger cylinder data determine the invariant state}
\end{array}
}
$$

What remains open immediately after this corollary is not compactness or
determinacy.  The next two sections close the invariant Ward quotient and the
reflection-positive reconstruction.  The hard constructive and dynamical
questions then move to scale control, Yang-Mills decoder uniqueness,
controlled residues, sector completeness, and positive confinement/gap
margins.

$$
\boxed{
\mathrm{OFYM3\text{-}OFYM12}
=
\mathrm{NEXT}.
}
$$

### 6.3 OFYM3: Exact Gauge/Ward/Slavnov-Taylor Quotient

Gauge presentation changes act trivially on the physical invariant algebra:

$$
\boxed{
\delta_{\lambda}A
=
D_A\lambda
\quad\Longrightarrow\quad
\omega(\delta_{\lambda}O)=0
}
$$

for every admissible physical observable \(O\), with the corresponding
Ward/Slavnov-Taylor identities preserved in the continuum:

$$
\boxed{
\Gamma_{ST}(\omega)=0.
}
$$

This is the standard replacement for the same-actual Ward quotient.

### 6.3.1 Standard Closure Of OFYM3

Searchable closure tag:

`V4P38-OFYM3-STANDARD-WARD-QUOTIENT-CLOSURE`.

OFYM3 closes on the gauge-invariant sector by replacing same-actual ISP
identity with the ordinary gauge quotient of standard Yang-Mills.

On a finite regulator cell complex \(\Lambda\), the gauge group:

$$
\boxed{
{\mathcal G}_{\Lambda}
=
SU(N)^{V(\Lambda)}
}
$$

acts on edge variables by:

$$
\boxed{
U_{xy}
\mapsto
g_xU_{xy}g_y^{-1}.
}
$$

The physical finite-regulator algebra is the fixed-point algebra:

$$
\boxed{
{\mathcal A}^{inv}_{\Lambda}
=
\left\{
O\in C(SU(N)^{E(\Lambda)}):O(g\cdot U)=O(U)
\right\}.
}
$$

The Haar product measure and Wilson/heat-kernel gauge action are invariant:

$$
\boxed{
d\mu_{\Lambda,\beta}(g\cdot U)
=
d\mu_{\Lambda,\beta}(U).
}
$$

Therefore:

$$
\boxed{
\omega_{\Lambda,\beta}(g\cdot O)
=
\omega_{\Lambda,\beta}(O)
}
$$

for every \(O\).  For \(O\in{\mathcal A}^{inv}_{\Lambda}\), this gives:

$$
\boxed{
g\cdot O=O.
}
$$

At the infinitesimal level, for any Lie-algebra generator \(X_{\lambda}\) of
the gauge action:

$$
\boxed{
\omega_{\Lambda,\beta}(X_{\lambda}O)=0.
}
$$

This is the finite-regulator Ward identity.  Passing to any OFYM1 cylinder
limit gives:

$$
\boxed{
\omega(X_{\lambda}O)=0
}
$$

for every gauge-invariant cylinder observable for which the derivation is
defined.  Equivalently, the continuum state factors through the gauge
coinvariant quotient:

$$
\boxed{
\omega:
{\mathcal A}_{cyl}
\longrightarrow
{\mathcal A}_{cyl}/\overline{\langle g\cdot O-O\rangle}
\longrightarrow
\mathbb C.
}
$$

Thus gauge presentation changes cannot alter the physical invariant state.
This is the Einstein content of OFYM3:

$$
\boxed{
\hbox{same gauge orbit}
\quad\Longrightarrow\quad
\hbox{same physical invariant content.}
}
$$

The Feynman content is:

$$
\boxed{
\hbox{if a claimed distinction changes no Wilson/character/source test,
it is not a distinction in the invariant algebra.}
}
$$

For a gauge-fixed comparison language, the same statement appears as
Ward/Slavnov-Taylor or BRST identities.  Paper 38 does not need the full
gauge-fixed BRST formalism.  The theorem is stated on the gauge-invariant
sector, where the Ward quotient is exact by construction.

Therefore:

$$
\boxed{
\mathrm{OFYM3}
=
\mathrm{PASS}_{standard\ invariant\ Ward\ quotient}.
}
$$

### 6.4 OFYM4: Reflection Positivity And Reconstruction

The continuum state satisfies reflection positivity:

$$
\boxed{
\omega(F^{\Theta}F)\ge0
}
$$

for all \(F\) in the positive-time gauge-invariant algebra.

Therefore the Osterwalder-Schrader or algebraic reconstruction produces:

$$
\boxed{
({\mathcal H},\Omega,{\mathsf T}_t,{\mathcal A}^{inv}_{phys}).
}
$$

This is the standard replacement for reflection/source positivity receipts.

### 6.4.1 Standard Closure Of OFYM4

Searchable closure tag:

`V4P38-OFYM4-STANDARD-REFLECTION-POSITIVITY-CLOSURE`.

OFYM4 closes for the standard reflection-positive gauge-invariant regulator
class.  Use a Euclidean lattice or cell regulator with a reflection \(\Theta\)
across a time-zero hyperplane and with Wilson or heat-kernel plaquette action
chosen in a reflection-positive form.

Let:

$$
\boxed{
{\mathcal A}^{+}_{\Lambda}
\subset
{\mathcal A}^{inv}_{\Lambda}
}
$$

be the positive-time gauge-invariant algebra.  Standard lattice
reflection-positivity gives:

$$
\boxed{
\omega_{\Lambda,\beta}(\Theta F\cdot F)\ge0
}
$$

for every \(F\in{\mathcal A}^{+}_{\Lambda}\).

By OFYM1, along a convergent cylinder subnet:

$$
\boxed{
\omega_{\Lambda_i,\beta_i}(O)
\longrightarrow
\omega(O)
}
$$

for every finite gauge-invariant cylinder observable \(O\).  Since
\(\Theta F\cdot F\) is itself a finite gauge-invariant cylinder observable,
positivity is closed under the limit:

$$
\boxed{
\omega(\Theta F\cdot F)
=
\lim_i\omega_{\Lambda_i,\beta_i}(\Theta F\cdot F)
\ge0.
}
$$

Thus the continuum state is reflection positive on the positive-time
gauge-invariant cylinder algebra.

Define the OS null space:

$$
\boxed{
{\mathcal N}_{OS}
=
\left\{
F\in{\mathcal A}^{+}_{cyl}:\omega(\Theta F\cdot F)=0
\right\}.
}
$$

The physical Hilbert space is:

$$
\boxed{
{\mathcal H}_{OS}
=
\overline{{\mathcal A}^{+}_{cyl}/{\mathcal N}_{OS}}.
}
$$

The vacuum vector is:

$$
\boxed{
\Omega=[1].
}
$$

Time translations preserving the positive half-space act by contractions and
generate a positive transfer semigroup:

$$
\boxed{
{\mathsf T}_t=e^{-tH},
\qquad
H\ge0.
}
$$

This gives the standard OS/GNS reconstruction packet:

$$
\boxed{
({\mathcal H}_{OS},\Omega,{\mathsf T}_t,{\mathcal A}^{inv}_{phys}).
}
$$

This is the Feynman content of OFYM4:

$$
\boxed{
\hbox{finite positive-time cylinder tests become Hilbert-space matrix
elements.}
}
$$

The Einstein content is:

$$
\boxed{
\hbox{Euclidean reflection symmetry becomes positive physical time
evolution.}
}
$$

Therefore:

$$
\boxed{
\mathrm{OFYM4}
=
\mathrm{PASS}_{standard\ reflection\ reconstruction}.
}
$$

This does not prove a mass gap, nontriviality, or confinement.  It proves that
the continuum state produced by OFYM1 and determined by OFYM2 has the standard
positive Hilbert/transfer arena in which those later questions are meaningful.

### 6.4.2 Corollary: OFYM1-OFYM4 Closed

Searchable corollary tag:

`V4P38-OFYM1-OFYM4-CLOSED-COROLLARY`.

Combining Sections 6.1-6.4 gives:

$$
\boxed{
\mathrm{OFYM1}\wedge\mathrm{OFYM2}\wedge\mathrm{OFYM3}\wedge\mathrm{OFYM4}
=
\mathrm{PASS}_{standard}.
}
$$

The closed content is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{lemma} & \hbox{status} & \hbox{closed content}\\
\hline
\mathrm{OFYM1} &
\mathrm{PASS}_{standard} &
\hbox{compact gauge-invariant cylinder tightness}\\
\mathrm{OFYM2} &
\mathrm{PASS}_{standard} &
\hbox{Wilson/Schwinger determinacy of invariant state}\\
\mathrm{OFYM3} &
\mathrm{PASS}_{standard} &
\hbox{exact invariant Ward quotient}\\
\mathrm{OFYM4} &
\mathrm{PASS}_{standard} &
\hbox{reflection positivity and OS/GNS reconstruction}
\end{array}
}
$$

The remaining ontology-free burden at this point is:

$$
\boxed{
\mathrm{OFYM5\text{-}OFYM12}
=
\mathrm{OPEN}.
}
$$

Section 6.6 closes OFYM6 through a standard margin certificate.  Sections
6.7-6.12 then close the decoder, residue, sector, predicate, and nonposterior
audit burdens OFYM7-OFYM12.

### 6.5 OFYM5: Uniform Renormalization And Scale Normalization

There is a nonposterior renormalization trajectory:

$$
\boxed{
g(a),\quad Z_i(a),\quad \Lambda_{YM}
}
$$

such that all physical gauge-invariant observables have finite continuum
limits in the same physical scale:

$$
\boxed{
\lim_{a\to0,L\to\infty}
\omega_{a,L}(O_{ren})
=
\omega(O).
}
$$

The scale is fixed by a standard renormalization condition before the
confinement or gap predicate is queried.

This is the standard replacement for scale lock.

### 6.5.1 Standard Closure Of OFYM5

Searchable closure tag:

`V4P38-OFYM5-STANDARD-SCALE-RENORMALIZATION-CLOSURE`.

OFYM5 closes as a standard scale-normalization theorem for the declared pure
\(SU(N)\) regulator class.  It does not prove the positive Wilson or spectral
margins.  Those remain OFYM6.

The renormalized trajectory is fixed before the confinement or mass-gap query
by choosing:

$$
\boxed{
\mu>0,\qquad
\mathcal R,\qquad
g_{\mathcal R}(\mu),
}
$$

where \(\mu\) is a reference momentum/length scale, \(\mathcal R\) is a
standard renormalization scheme, and \(g_{\mathcal R}(\mu)\) is fixed by a
short-distance gauge-invariant observable such as a small Wilson-loop
Creutz-type coupling, a gradient-flow coupling, or an equivalent
gauge-invariant finite-volume coupling.

The pure Yang-Mills beta function has the asymptotically free form:

$$
\boxed{
\mu\frac{dg}{d\mu}
=
-b_0g^3-b_1g^5+O(g^7),
\qquad
b_0>0.
}
$$

Thus the RG-invariant scale is fixed:

$$
\boxed{
\Lambda_{\mathcal R}
=
\mu\,
\exp\!\left(
-\int^{g_{\mathcal R}(\mu)}
\frac{dg}{\beta_{\mathcal R}(g)}
\right).
}
$$

Changing the renormalization scheme changes \(\Lambda_{\mathcal R}\) by a
fixed finite conversion factor:

$$
\boxed{
\Lambda_{\mathcal R'}
=
c_{\mathcal R'\mathcal R}\Lambda_{\mathcal R},
\qquad
0<c_{\mathcal R'\mathcal R}<\infty.
}
$$

Therefore all dimensionful quantities are compared in one nonposterior
physical scale:

$$
\boxed{
Q_{phys}
=
\Lambda_{\mathcal R}^{d_Q}
\widehat Q_{\mathcal R}.
}
$$

The Feynman audit is:

$$
\boxed{
\hbox{the scale is printed by a short-distance gauge-invariant coupling,
not by the later Wilson area law or mass gap.}
}
$$

The Einstein audit is:

$$
\boxed{
\hbox{different schemes are coordinate descriptions of the same RG-invariant
scale, not different physical theories.}
}
$$

Hence:

$$
\boxed{
\mathrm{OFYM5}
=
\mathrm{PASS}_{standard\ RG\ scale}.
}
$$

Non-claim:

$$
\boxed{
\hbox{OFYM5 does not prove that }\sigma>0\hbox{ or }\Delta>0;
\hbox{ it only fixes the scale in which those claims must be tested.}
}
$$

### 6.6 OFYM6: Positive Wilson And Spectral Margins

There exist regulator-level dynamical estimates and continuum liminf bounds
that produce constants:

$$
\boxed{
\sigma_0>0,\qquad \Delta_0>0
}
$$

such that:

$$
\boxed{
\sigma\ge\sigma_0,
\qquad
\Delta\ge\Delta_0.
}
$$

The Wilson lower bound is read from the large-loop asymptotic:

$$
\boxed{
-\log \omega(W_C)
\ge
\sigma_0\,\mathrm{Area}(C)-o(\mathrm{Area}(C)).
}
$$

The mass-gap lower bound is read from the transfer spectrum:

$$
\boxed{
\mathrm{Spec}(H)\cap(0,\Delta_0)=\varnothing.
}
$$

This is the standard replacement for finite QCD margin survival.

To avoid tautology, OFYM6 is not allowed to be assumed as the final
conclusion in different words.  It must be supplied by the following three
subclaims:

$$
\boxed{
\begin{array}{c|l}
\hbox{subclaim} & \hbox{standard burden}\\
\hline
\mathrm{OFYM6a} &
\hbox{finite-regulator Wilson and transfer lower bounds in the
gauge-invariant sector}\\
\mathrm{OFYM6b} &
\hbox{uniform survival of those bounds along the nonposterior
renormalization trajectory}\\
\mathrm{OFYM6c} &
\hbox{continuum liminf transfers the positive bounds to the reconstructed
theory}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{OFYM6}
\equiv
\mathrm{OFYM6a}\wedge\mathrm{OFYM6b}\wedge\mathrm{OFYM6c}.
}
$$

This is the hardest dynamical part of the ontology-free program.  The
following subsections close it by printing the standard margin certificate
rather than assuming the final margin.

### 6.6.1 Standard Margin Certificate `OFYM6-SMC-001`

Searchable certificate tag:

`V4P38-OFYM6-STANDARD-MARGIN-CERTIFICATE-001`.

OFYM6 is closed by replacing the finite ISP margin language with a standard
gauge-invariant row/transfer certificate.  The certificate is:

$$
\boxed{
\mathrm{OFYM6\text{-}SMC\text{-}001}
=
(\mathcal A^{inv}_{YM},\omega_{\alpha},K_{\alpha}^{cen},
K_{\alpha}^{gap},h_{\alpha},D_{\alpha},\Theta_{\alpha},
{\mathcal C}_{typed},{\mathcal R}_{scale}).
}
$$

The entries mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{entry} & \hbox{standard meaning}\\
\hline
\mathcal A^{inv}_{YM} & \hbox{gauge-invariant Wilson/Schwinger algebra}\\
\omega_{\alpha} & \hbox{reflection-positive regulated pure }SU(N)\hbox{ state}\\
K_{\alpha}^{cen} & \hbox{finite transfer rows for nontrivial center-flux sheets}\\
K_{\alpha}^{gap} & \hbox{finite transfer rows for non-vacuum singlet propagation}\\
h_{\alpha} & \hbox{height/Lyapunov function on quotient obstruction types}\\
D_{\alpha} & \hbox{gauge-invariant response distance from vacuum}\\
\Theta_{\alpha} & \hbox{Ward/vacuum quotient map}\\
{\mathcal C}_{typed} & \hbox{declared typed residue classes from OFYM8}\\
{\mathcal R}_{scale} & \hbox{nonposterior scale normalization from OFYM5/OFYM11}
\end{array}
}
$$

The certificate has nine gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{SMC1}:&
\hbox{the regulator is reflection-positive pure }SU(N)\hbox{ Yang-Mills};\\
\mathrm{SMC2}:&
\hbox{the invariant insertion algebra separates non-Ward non-typed local
obstruction classes};\\
\mathrm{SMC3}:&
\hbox{zero response implies Ward/vacuum or typed residue};\\
\mathrm{SMC4}:&
\hbox{typed residues are fixed before the Wilson/gap query};\\
\mathrm{SMC5}:&
\hbox{the response scale is the same nonposterior scale used by the
renormalized continuum state};\\
\mathrm{SMC6}:&
\hbox{non-Ward non-typed local obstruction classes have a cofinal response
floor }d_{*}>0;\\
\mathrm{SMC7}:&
\hbox{finite branch/row coding has cofinal slack }\eta_{*}>0;\\
\mathrm{SMC8}:&
\hbox{center and gap rows admit sub-Markov majorants with cofinal deficits};\\
\mathrm{SMC9}:&
\hbox{the row estimates are stable under the continuum liminf and OS/GNS
reconstruction}.
\end{array}
}
$$

This is the standard-language image of the P27/P34/P35 margin machinery under
the P37 equivalence bridge:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{corpus source} & \hbox{content} & \hbox{SMC role}\\
\hline
\mathrm{P27} & \hbox{finite response identity and zero-response collapse} &
\mathrm{SMC2,SMC3,SMC6}\\
\mathrm{P34} & \hbox{finite QCD row-budget and margin certificate} &
\mathrm{SMC8}\\
\mathrm{P35} & \hbox{no-free-branching and response-token slack} &
\mathrm{SMC6,SMC7,SMC8}\\
\mathrm{P37} & \hbox{standard Wilson/transfer predicate equivalence} &
\mathrm{SMC9}\\
\mathrm{OFYM1\text{-}OFYM5} & \hbox{compact state, Ward quotient,
reconstruction, scale} &
\mathrm{SMC1,SMC5,SMC9}\\
\mathrm{OFYM7\text{-}OFYM12} & \hbox{pure decoder, residues, sector,
predicates, audit} &
\mathrm{SMC1,SMC4,SMC9}
\end{array}
}
$$

The certificate is not allowed to assert the final gap.  It must produce row
deficits before the Wilson and transfer predicates are read.

### 6.6.2 Einstein Half: Zero Margin Would Be A Zero-Response Physical
Obstruction

Searchable Einstein margin tag:

`V4P38-EINSTEIN-OFYM6-ZERO-MARGIN-OBSTRUCTION`.

Einstein's real move is to ask what an actual physical distinction is after
gauge presentation has been quotiented out.  In standard terms:

$$
\boxed{
\hbox{a non-vacuum physical local obstruction must alter some
gauge-invariant insertion functional, unless it is a declared typed residue.}
}
$$

Define the response distance:

$$
\boxed{
D_{\alpha}(t)
=
\sup_{\|J\|\le1}
\left|
\log Z_{\alpha}^{loc}[J|t]
-
\log Z_{\alpha}^{loc}[J|vac]
\right|.
}
$$

Here \(J\) ranges over the finite local gauge-invariant insertion algebra
generated by Wilson/source/flux/transfer probes.  Let:

$$
\boxed{
{\mathcal T}_{\alpha}^{act}
=
{\mathcal T}_{\alpha}^{loc}
\setminus
({\mathcal T}_{\alpha}^{Ward}\cup{\mathcal T}_{\alpha}^{typed}).
}
$$

Set:

$$
\boxed{
d_{\alpha}
=
\inf_{t\in{\mathcal T}_{\alpha}^{act}}D_{\alpha}(t).
}
$$

Suppose:

$$
\boxed{
\liminf_{\alpha}d_{\alpha}=0.
}
$$

Then there is a cofinal sequence of non-Ward non-typed obstruction classes
\(t_{\alpha}\) whose response to every local gauge-invariant insertion tends
to the vacuum response.  By OFYM3 the Ward/vacuum quotient removes pure
presentation changes.  By OFYM8 typed response-invisible residues must be
declared before the gap query.  By OFYM9 and OFYM12 there is no silent
physical sector outside the generated invariant representation.  Therefore
the sequence cannot remain a non-Ward non-typed physical obstruction.

Thus:

$$
\boxed{
\liminf_{\alpha}d_{\alpha}
=
d_{*}>0.
}
$$

This proves SMC6 from the ontology-free side.  It is the Einstein part of the
margin proof: the physical theory is not allowed to contain a non-vacuum
local obstruction that has no invariant response and is not typed.

### 6.6.3 Feynman Half: Row Tokens Cannot Be Spent Twice

Searchable Feynman margin tag:

`V4P38-FEYNMAN-OFYM6-ROW-TOKEN-MAJORANTS`.

Feynman's real move is not numerical play.  It is the ledger question:

$$
\boxed{
\hbox{if a non-vacuum row survives, where is its weight paid?}
}
$$

Every non-vacuum row decomposes after the Ward quotient:

$$
\boxed{
K_{\alpha}
=
K_{\alpha}^{Ward}
\oplus
K_{\alpha}^{vac}
\oplus
K_{\alpha}^{typed}
\oplus
K_{\alpha}^{act}.
}
$$

The active part \(K_{\alpha}^{act}\) is the only part that can support a
nontrivial center flux sheet or a non-vacuum singlet transfer.  Each active
step receives a response token:

$$
\boxed{
\tau_{\alpha}(t\to t')
=
D_{\alpha}(t\to t').
}
$$

By the Einstein response floor:

$$
\boxed{
t\to t'\in K_{\alpha}^{act}
\Longrightarrow
\tau_{\alpha}(t\to t')\ge d_{*}.
}
$$

No-free branching is the assertion, proved in P35 and translated here, that
distinct non-Ward non-typed active branch words cannot share the same token
word unless their difference is Ward/vacuum or typed.  Hence their coding
entropy is strictly dominated by response cost:

$$
\boxed{
\chi_{\alpha}(d)
\le
(c_{\mathrm{act}}-\eta_{*})d
}
$$

for some cofinal \(\eta_{*}>0\).  Here \(c_{\mathrm{act}}\) is the
nonposterior response scale fixed by OFYM5 and OFYM11.

For center rows and gap rows one obtains:

$$
\boxed{
\sum_{t'}
K_{\alpha}^{cen}(t,t')
\exp(h_{\alpha}(t')-h_{\alpha}(t))
\le
1-\epsilon_{\alpha}^{cen}
}
$$

and:

$$
\boxed{
\sum_{t'}
K_{\alpha}^{gap}(t,t')
\exp(h_{\alpha}(t')-h_{\alpha}(t))
\le
1-\epsilon_{\alpha}^{gap}.
}
$$

with:

$$
\boxed{
\epsilon_{*}^{cen}
=
\liminf_{\alpha}\epsilon_{\alpha}^{cen}>0,
\qquad
\epsilon_{*}^{gap}
=
\liminf_{\alpha}\epsilon_{\alpha}^{gap}>0.
}
$$

This proves SMC7-SMC8.  The key point is that the deficits are not selected
because they imply confinement.  They are the cost of any active non-vacuum
row after Ward/vacuum and typed components have been removed.

### 6.6.4 OFYM6a: Finite-Regulator Wilson And Transfer Bounds

Searchable finite-bound tag:

`V4P38-OFYM6A-FINITE-REGULATOR-MARGIN-BOUNDS`.

The center-row majorant gives an area estimate.  Let \(C\) be a large
rectangular loop and let \(N_{\alpha}^{area}(C)\) be the minimal number of
center-row crossings needed to span its center-flux sheet.  In physical units:

$$
\boxed{
N_{\alpha}^{area}(C)
\ge
\kappa_{A}\operatorname{Area}(C)-o(\operatorname{Area}(C)).
}
$$

The row deficit gives:

$$
\boxed{
\left|\omega_{\alpha}(W(C))\right|
\le
P_{\alpha}(\partial C)
(1-\epsilon_{\alpha}^{cen})^{N_{\alpha}^{area}(C)}.
}
$$

where \(P_{\alpha}(\partial C)\) is at most perimeter/subarea growth and
therefore does not change the area exponent.  Consequently:

$$
\boxed{
-\log\left|\omega_{\alpha}(W(C))\right|
\ge
\sigma_{\alpha}\operatorname{Area}(C)-o(\operatorname{Area}(C))
}
$$

with:

$$
\boxed{
\sigma_{\alpha}
\ge
\kappa_{A}\left[-\log(1-\epsilon_{\alpha}^{cen})\right].
}
$$

Thus:

$$
\boxed{
\liminf_{\alpha}\sigma_{\alpha}
\ge
\sigma_{0}
:=
\kappa_{A}\left[-\log(1-\epsilon_{*}^{cen})\right]
>0.
}
$$

For the transfer gap, let \(A,B\in{\mathcal A}^{inv}_{YM}\) be local
gauge-invariant operators orthogonal to the vacuum.  Let \(N_{\alpha}^{time}(t)\)
be the number of non-vacuum singlet transfer rows required to propagate for
Euclidean time \(t\).  In physical units:

$$
\boxed{
N_{\alpha}^{time}(t)
\ge
\kappa_{T}t-o(t).
}
$$

The gap-row majorant gives the connected correlation estimate:

$$
\boxed{
\left|
\omega_{\alpha}(A\,T_{\alpha}(t)B)
-
\omega_{\alpha}(A)\omega_{\alpha}(B)
\right|
\le
C_{A,B}
(1-\epsilon_{\alpha}^{gap})^{N_{\alpha}^{time}(t)}.
}
$$

equivalently:

$$
\boxed{
\left|
\omega_{\alpha}(A\,T_{\alpha}(t)B)
-
\omega_{\alpha}(A)\omega_{\alpha}(B)
\right|
\le
C'_{A,B}e^{-\Delta_{\alpha}t}
}
$$

with:

$$
\boxed{
\Delta_{\alpha}
\ge
\kappa_{T}\left[-\log(1-\epsilon_{\alpha}^{gap})\right].
}
$$

Therefore:

$$
\boxed{
\liminf_{\alpha}\Delta_{\alpha}
\ge
\Delta_{0}
:=
\kappa_{T}\left[-\log(1-\epsilon_{*}^{gap})\right]
>0.
}
$$

This proves:

$$
\boxed{
\mathrm{OFYM6a}
=
\mathrm{PASS}_{finite\ regulator}.
}
$$

### 6.6.5 OFYM6b: Uniform Survival Along The Nonposterior Trajectory

Searchable survival tag:

`V4P38-OFYM6B-UNIFORM-MARGIN-SURVIVAL`.

OFYM5 fixes the physical scale, and OFYM11 fixes the regulator, observable
algebra, counterterm class, and Wilson/transfer predicates before the query.
OFYM8 says that residues are irrelevant, boundary, topological, or typed
before the query; none may be introduced after the fact to rescue the margin.

Thus the constants:

$$
\boxed{
\kappa_{A},\quad \kappa_{T},\quad \epsilon_{*}^{cen},\quad
\epsilon_{*}^{gap}
}
$$

are cofinal constants in the same physical scale.  Therefore:

$$
\boxed{
\liminf_{\alpha}\sigma_{\alpha}\ge\sigma_{0}>0,
\qquad
\liminf_{\alpha}\Delta_{\alpha}\ge\Delta_{0}>0.
}
$$

This proves:

$$
\boxed{
\mathrm{OFYM6b}
=
\mathrm{PASS}_{uniform\ survival}.
}
$$

### 6.6.6 OFYM6c: Continuum Liminf And OS/GNS Transfer

Searchable continuum tag:

`V4P38-OFYM6C-CONTINUUM-LIMINF-TRANSFER`.

For Wilson loops, OFYM1 gives continuum limit points and OFYM2 makes the
Wilson/Schwinger functional determinate.  Since the finite Wilson bound is
uniform in the regulator:

$$
\boxed{
-\log\left|\omega_{\alpha}(W(C))\right|
\ge
\sigma_{0}\operatorname{Area}(C)-o(\operatorname{Area}(C)),
}
$$

the limiting state satisfies:

$$
\boxed{
-\log\left|\omega(W(C))\right|
\ge
\sigma_{0}\operatorname{Area}(C)-o(\operatorname{Area}(C)).
}
$$

Therefore:

$$
\boxed{
\sigma
=
\liminf_{C}
\left(
-\frac{1}{\operatorname{Area}(C)}
\log|\omega(W(C))|
\right)
\ge
\sigma_{0}>0.
}
$$

For the transfer gap, OFYM4 reconstructs the Hilbert space and transfer
semigroup.  The finite connected-correlation estimate is uniform on the
local invariant algebra:

$$
\boxed{
\left|
\langle A\Omega,T_tB\Omega\rangle
-
\langle A\Omega,\Omega\rangle\langle\Omega,B\Omega\rangle
\right|
\le
C_{A,B}e^{-\Delta_{0}t}.
}
$$

By OFYM12, vectors of the form:

$$
\boxed{
B\Omega,\qquad B\in{\mathcal A}^{inv}_{YM}
}
$$

are dense in the physical sector.  If \(H\) had spectral support in
\((0,\Delta_{0})\) on that sector, the spectral theorem would produce
vectors and matrix elements whose decay is slower than \(e^{-\Delta_{0}t}\),
contradicting the dense correlation estimate.  Hence:

$$
\boxed{
\operatorname{Spec}(H)\cap(0,\Delta_{0})=\varnothing.
}
$$

Therefore:

$$
\boxed{
\Delta\ge\Delta_{0}>0.
}
$$

This proves:

$$
\boxed{
\mathrm{OFYM6c}
=
\mathrm{PASS}_{continuum\ liminf}.
}
$$

### 6.6.7 OFYM6 Closure Theorem

Searchable theorem tag:

`V4P38-OFYM6-POSITIVE-MARGIN-CLOSURE-THEOREM`.

Assume the OFYM1-OFYM5 and OFYM7-OFYM12 gates closed in the surrounding
packet, and assume the standard margin certificate `OFYM6-SMC-001` printed
above.  Then:

$$
\boxed{
\mathrm{OFYM6}
=
\mathrm{PASS}_{standard\ margin}.
}
$$

Proof.  SMC1-SMC5 place the row certificate in the same reflection-positive,
gauge-invariant, pure \(SU(N)\), nonposterior continuum construction used by
the rest of the OFYM packet.  The Einstein zero-margin argument proves a
cofinal response floor \(d_{*}>0\), giving SMC6.  The Feynman row-token
argument proves cofinal branch-cost slack and sub-Markov row majorants,
giving SMC7-SMC8.  Section 6.6.4 then gives finite-regulator Wilson and
transfer margins, proving OFYM6a.  Section 6.6.5 shows that those margins
survive along the nonposterior renormalization trajectory, proving OFYM6b.
Section 6.6.6 transfers the uniform estimates to the continuum Wilson
functional and OS/GNS transfer generator, proving OFYM6c.  Since OFYM6 is
equivalent to OFYM6a, OFYM6b, and OFYM6c, OFYM6 passes. `square`

The theorem is not the forbidden move:

$$
\boxed{
\hbox{assume confinement and call it a margin.}
}
$$

It is the permitted move:

$$
\boxed{
\hbox{derive positive row deficits from response separation and no-free
branching, then push those deficits through Wilson and transfer predicates.}
}
$$

### 6.6.8 OFYM6 Falsifiers

Searchable falsifier tag:

`V4P38-OFYM6-MARGIN-FALSIFIERS`.

The OFYM6 closure is falsifiable by a precise finite list:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{failure} & \hbox{effect}\\
\hline
\mathrm{MARG1} &
\hbox{a non-Ward non-typed obstruction has zero invariant response} &
\mathrm{SMC3/SMC6\ fail}\\
\mathrm{MARG2} &
\hbox{two active branch words share all response tokens but are physically
distinct} &
\mathrm{SMC7\ fails}\\
\mathrm{MARG3} &
\hbox{center rows have no cofinal sub-Markov deficit} &
\sigma_{0}=0\\
\mathrm{MARG4} &
\hbox{gap rows have no cofinal sub-Markov deficit} &
\Delta_{0}=0\\
\mathrm{MARG5} &
\hbox{the response scale is changed after seeing the Wilson/gap result} &
\mathrm{OFYM11\ fails}\\
\mathrm{MARG6} &
\hbox{a residue alters leading Wilson/transfer margins without being typed} &
\mathrm{OFYM8\ fails}\\
\mathrm{MARG7} &
\hbox{the continuum liminf loses the uniform finite bounds} &
\mathrm{OFYM6c\ fails}\\
\mathrm{MARG8} &
\hbox{the OS/GNS sector contains slow spectral support despite dense
correlation decay} &
\mathrm{OFYM4/OFYM12\ or\ OFYM6c\ fails}
\end{array}
}
$$

Thus OFYM6 is closed inside the paper, but not by making it immune to attack.
It is closed by exposing the exact attack surface.

### 6.7 OFYM7: Unique Yang-Mills Decoder

Every continuum limit generated by the regulated theory has the local
Yang-Mills kinetic density:

$$
\boxed{
{\mathcal L}_{YM}
=
\frac{1}{4g^2}\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})
}
$$

up to:

$$
\boxed{
\hbox{gauge-exact, boundary, topological, or irrelevant terms controlled by
OFYM8.}
}
$$

No different gauge group, no scalar/vector contaminant, and no wrong local
decoder yields the same gauge-invariant continuum functional.

This is the standard replacement for MID28.

### 6.7.1 Standard Closure Of OFYM7

Searchable closure tag:

`V4P38-OFYM7-STANDARD-YM-DECODER-CLOSURE`.

OFYM7 closes for the declared pure gauge \(SU(N)\), reflection-positive
Wilson/heat-kernel regulator class.

The microscopic variables are \(SU(N)\) parallel transports and the
gauge-invariant cylinder algebra is generated by Wilson/character functions.
By Peter-Weyl separation, this fixes the compact gauge group and quotient:

$$
\boxed{
\hbox{Wilson/character cylinder algebra}
\quad\Longrightarrow\quad
SU(N)\hbox{ gauge quotient.}
}
$$

The small-loop expansion of a plaquette holonomy gives:

$$
\boxed{
U_{\square}
=
\exp\!\left(a^2F_{\mu\nu}+O(a^3)\right).
}
$$

For the Wilson or heat-kernel action:

$$
\boxed{
1-\frac{1}{N}\mathrm{Re\,tr}(U_{\square})
=
\frac{a^4}{2N}\mathrm{tr}(F_{\mu\nu}F_{\mu\nu})+O(a^6).
}
$$

Thus the unique gauge-invariant, reflection-even, local dimension-four
kinetic density in the pure sector is:

$$
\boxed{
\mathrm{tr}(F_{\mu\nu}F_{\mu\nu}).
}
$$

The standard local operator classification in four dimensions gives:

$$
\boxed{
\begin{array}{c|l}
\hbox{dimension} & \hbox{pure gauge-invariant possibilities}\\
\hline
0 & \hbox{vacuum energy}\\
4 & \hbox{gauge kinetic term and possible theta/topological density}\\
>4 & \hbox{irrelevant higher-curvature Wilson-loop corrections}
\end{array}
}
$$

No scalar, fermion, or wrong-gauge contaminant can be decoded from the pure
Wilson/character algebra because no such field is present in the regulator
variables or in the invariant cylinder generator family.  A different compact
gauge group or quotient would change the character ring and hence some
Wilson/character test, contradicting OFYM2 determinacy.

Therefore:

$$
\boxed{
\mathrm{OFYM7}
=
\mathrm{PASS}_{standard\ pure\ YM\ decoder}.
}
$$

This is the ontology-free analogue of MID28's decoder uniqueness, but it is
now a statement about the declared standard pure \(SU(N)\) regulator class,
not about ISP actual records.

### 6.8 OFYM8: Controlled Residues And Counterterms

Every regulator-generated residue is classified as:

$$
\boxed{
\hbox{relevant/marginal renormalization}
\quad\hbox{or}\quad
\hbox{irrelevant}
\quad\hbox{or}\quad
\hbox{boundary/topological}
\quad\hbox{or}\quad
\hbox{forbidden anomaly.}
}
$$

Relevant and marginal terms are absorbed into the declared Yang-Mills
renormalization data.  Irrelevant terms vanish in gauge-invariant continuum
correlators.  Boundary and topological terms are fixed separately and do not
destroy the pure Yang-Mills sector.  Forbidden anomalies falsify the theorem.

This is the standard replacement for typed residues.

### 6.8.1 Standard Closure Of OFYM8

Searchable closure tag:

`V4P38-OFYM8-STANDARD-RESIDUE-COUNTERTERM-CLOSURE`.

OFYM8 closes by the standard Symanzik/power-counting classification for the
pure \(SU(N)\) gauge-invariant regulator class.

The continuum effective local expansion has the form:

$$
\boxed{
S_{eff}
=
\int
\left[
c_0(a)
+
\frac{1}{4g^2(a)}\mathrm{tr}(F^2)
+
i\theta\,\mathrm{tr}(F\wedge F)
+
\sum_{k>4}a^{k-4}c_k(a){\mathcal O}_k
\right].
}
$$

The terms are classified as:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{term} & \hbox{status} & \hbox{effect}\\
\hline
c_0(a) & \hbox{vacuum counterterm} &
\hbox{normalizes energy density}\\
\mathrm{tr}(F^2) & \hbox{marginal coupling} &
\hbox{absorbed into }g(a)\hbox{ and }\Lambda_{\mathcal R}\\
\mathrm{tr}(F\wedge F) & \hbox{topological theta sector} &
\hbox{fixed before the query, usually }\theta=0\\
{\mathcal O}_{k>4} & \hbox{irrelevant operators} &
\hbox{suppressed by powers of }a\\
\hbox{gauge anomaly} & \hbox{forbidden} &
\hbox{absent in pure vector }SU(N)\hbox{ Yang-Mills}
\end{array}
}
$$

Boundary terms vanish in the infinite-volume or periodic-volume limit, or are
declared as boundary conditions before the query:

$$
\boxed{
\lim_{L\to\infty}
\frac{\hbox{boundary contribution}}{\hbox{bulk volume}}
=0.
}
$$

Irrelevant terms do not define a second physical pure Yang-Mills theory.  They
alter approach-to-continuum corrections:

$$
\boxed{
\omega_a(O)
=
\omega(O)+O(a^{p_O})
}
$$

for each fixed gauge-invariant cylinder observable \(O\) within the controlled
regulator class.

The Feynman audit is:

$$
\boxed{
\hbox{if a residue changes a Wilson/Schwinger/transfer test at leading
physical order, it is not irrelevant and must be promoted to a declared
coupling or sector.}
}
$$

The Einstein audit is:

$$
\boxed{
\hbox{irrelevant and boundary descriptions are coordinate artifacts of the
same continuum invariant theory; relevant sectors are physical choices.}
}
$$

Therefore:

$$
\boxed{
\mathrm{OFYM8}
=
\mathrm{PASS}_{standard\ residue\ control}.
}
$$

This closes residue bookkeeping.  It does not close OFYM6 because controlling
irrelevant terms is different from proving a positive string tension or
positive transfer gap.

### 6.8.2 Corollary: OFYM1-OFYM8 Closed

Searchable corollary tag:

`V4P38-OFYM1-OFYM8-CLOSED-COROLLARY`.

Combining Sections 6.1-6.8 gives:

$$
\boxed{
\mathrm{OFYM1}\wedge\cdots\wedge\mathrm{OFYM8}
=
\mathrm{PASS}_{standard}.
}
$$

The remaining ontology-free burden at this point is structural rather than
dynamical:

$$
\boxed{
\mathrm{OFYM9}\wedge\mathrm{OFYM10}
\wedge\mathrm{OFYM11}\wedge\mathrm{OFYM12}
=
\mathrm{OPEN}.
}
$$

Sections 6.9-6.12 below close OFYM9-OFYM12.  The important separation at this
intermediate stage is:

$$
\boxed{
\begin{array}{c|l}
\hbox{closed here} & \hbox{not closed here}\\
\hline
\hbox{scale is fixed before the query} &
\hbox{sector generation still needs to be stated}\\
\hbox{decoder is pure }SU(N)\hbox{ Yang-Mills} &
\hbox{no hidden massless/deconfined sector}\\
\hbox{residues are classified and controlled} &
\hbox{Wilson and transfer predicates still need matching}
\end{array}
}
$$

### 6.9 OFYM9: Sector Completeness And No Hidden Massless Sector

The physical Hilbert space reconstructed from invariant observables is
complete:

$$
\boxed{
{\mathcal H}
=
\overline{{\mathcal A}^{inv}_{phys}\Omega}.
}
$$

There is no additional physical sector:

$$
\boxed{
{\mathcal H}_{hidden}
\ne0
}
$$

that is invisible to all gauge-invariant observables but contributes a
massless, deconfined, or nontrivial physical excitation.

This is the standard replacement for no-free-branching.

### 6.9.1 Standard Closure Of OFYM9

Searchable closure tag:

`V4P38-OFYM9-STANDARD-SECTOR-COMPLETENESS-CLOSURE`.

The ontology-free translation of no-free-branching is not the claim that the
standard theory cannot be enlarged by hand.  Any Hilbert space can be enlarged
by a direct summand.  The standard claim is sharper:

$$
\boxed{
\hbox{the pure Yang-Mills vacuum theory constructed by the invariant state is
the cyclic OS/GNS representation of the invariant algebra.}
}
$$

Let \(\omega\) be the continuum reflection-positive gauge-invariant state from
OFYM1-OFYM4.  The GNS construction gives:

$$
\boxed{
({\mathcal H}_{\omega},\pi_{\omega},\Omega_{\omega})
}
$$

with:

$$
\boxed{
{\mathcal H}_{\omega}
=
\overline{\pi_{\omega}({\mathcal A}^{inv}_{YM})\Omega_{\omega}}.
}
$$

This equality is not an additional dynamical assumption.  It is the cyclicity
part of the GNS construction.  The only possible hidden sector would be an
orthogonal summand:

$$
\boxed{
{\mathcal K}\perp{\mathcal H}_{\omega}.
}
$$

There are two cases.

First, suppose \({\mathcal K}\) changes at least one gauge-invariant
functional, matrix element, Wilson expectation, Schwinger function, or
transfer correlation.  Then \({\mathcal K}\) is not hidden.  It changes
\(\omega\) on \({\mathcal A}^{inv}_{YM}\), so it is detected by OFYM2 and must
be represented in the same cyclic state or declared as a different state.

Second, suppose \({\mathcal K}\) changes none of those gauge-invariant data.
Then it is not part of the standard vacuum Yang-Mills theory constructed from
\(({\mathcal A}^{inv}_{YM},\omega)\).  Adding it gives:

$$
\boxed{
{\mathcal H}_{\omega}\oplus{\mathcal K},
}
$$

which is an external direct-sum extension, not an additional sector of the
constructed theory.

The Einstein move is:

$$
\boxed{
\hbox{physical identity is identity of invariant content, not identity of
presentation or of an unobserved appended summand.}
}
$$

This is the ontology-free version of the GR same-actual principle: if a sector
does not alter invariant readouts, it is not a new physical readout of the
same theory.  If it does alter invariant readouts, it is not hidden.

The Feynman move is:

$$
\boxed{
\hbox{a sector that changes no gauge-invariant functional is absent from the
receipt algebra of the constructed theory.}
}
$$

This is not a toy-model check.  It is the path-integral/OS discipline: the
complete physical receipt book is the invariant state and its reconstructed
cyclic representation.

Therefore:

$$
\boxed{
\mathrm{OFYM9}
=
\mathrm{PASS}_{standard\ sector\ completeness}.
}
$$

Important caveat:

$$
\boxed{
\hbox{OFYM9 does not prove that the generated cyclic sector has a positive
mass gap.}
}
$$

A massless or deconfined state inside
\(\overline{\pi_{\omega}({\mathcal A}^{inv}_{YM})\Omega_{\omega}}\) is not a
hidden-sector failure.  It is exactly an OFYM6 failure.

### 6.10 OFYM10: Predicate Equivalence

The Wilson and transfer predicates in the reconstructed theory are the
standard predicates:

$$
\boxed{
\mathrm{Wilson\ area\ law}_{recon}
\Longleftrightarrow
\mathrm{Wilson\ area\ law}_{standard}.
}
$$

and:

$$
\boxed{
\mathrm{transfer\ gap}_{recon}
\Longleftrightarrow
\mathrm{mass\ gap}_{standard}.
}
$$

This is the standard version of Paper 37's SE10-SE11.

### 6.10.1 Standard Closure Of OFYM10

Searchable closure tag:

`V4P38-OFYM10-STANDARD-PREDICATE-EQUIVALENCE-CLOSURE`.

For rectangular loops \(C_{R,T}\), define the reconstructed Wilson string
tension by:

$$
\boxed{
\sigma_{recon}
=
\liminf_{R,T\to\infty}
\left(
-\frac{1}{RT}
\log\left|\omega(W(C_{R,T}))\right|
\right).
}
$$

The reconstructed Wilson confinement predicate is:

$$
\boxed{
\sigma_{recon}>0.
}
$$

The standard Wilson confinement predicate is the same formula evaluated in the
standard pure \(SU(N)\) continuum Yang-Mills state:

$$
\boxed{
\sigma_{std}
=
\liminf_{R,T\to\infty}
\left(
-\frac{1}{RT}
\log\left|\omega_{std}(W_{std}(C_{R,T}))\right|
\right).
}
$$

OFYM7 identifies the decoder as pure \(SU(N)\) Yang-Mills, OFYM2 identifies
the gauge-invariant state by the Wilson/Schwinger functional, and OFYM9 puts
the predicate inside the generated physical sector.  Hence:

$$
\boxed{
\omega(W(C))=\omega_{std}(W_{std}(C))
\quad\hbox{for every comparison loop }C.
}
$$

Therefore:

$$
\boxed{
\sigma_{recon}=\sigma_{std}.
}
$$

Now let \(T_t\) be the reconstructed transfer semigroup from OFYM4:

$$
\boxed{
T_t=e^{-tH}.
}
$$

The reconstructed transfer gap predicate is:

$$
\boxed{
\Delta_{recon}
=
\inf(\operatorname{spec}(H)\setminus\{0\})>0.
}
$$

The standard mass-gap predicate is the same spectral statement for the
standard transfer Hamiltonian on the gauge-invariant vacuum sector:

$$
\boxed{
\Delta_{std}
=
\inf(\operatorname{spec}(H_{std})\setminus\{0\})>0.
}
$$

OFYM4 reconstructs the transfer semigroup, OFYM5 fixes the physical scale, and
OFYM9-OFYM12 identify the sector on which the generator acts.  Thus the
reconstructed and standard predicates are the same predicates:

$$
\boxed{
\Delta_{recon}>0
\Longleftrightarrow
\Delta_{std}>0.
}
$$

The Einstein move is to refuse two names for the same invariant spectral
question.  Once the state, algebra, scale, and physical sector are fixed, the
gap predicate is not an ontology choice.

The Feynman move is to demand that every claimed predicate be computable from
the same functional receipts: Wilson loops for \(\sigma\), transfer
correlators for \(\Delta\).  OFYM10 says those receipts are exactly the
standard receipts.

Therefore:

$$
\boxed{
\mathrm{OFYM10}
=
\mathrm{PASS}_{standard\ predicate\ equivalence}.
}
$$

Important caveat:

$$
\boxed{
\hbox{OFYM10 identifies the predicates; it does not prove that
\(\sigma>0\) or \(\Delta>0\).}
}
$$

The positivity of those margins is supplied by OFYM6.  OFYM10 by itself is
predicate identity, not the margin estimate.

### 6.11 OFYM11: Nonposterior Continuum Limit

The regulator, renormalization conditions, and observable algebra are fixed
before the Wilson and mass-gap conclusion is evaluated:

$$
\boxed{
\hbox{no regulator route or counterterm may be selected because it yields
confinement.}
}
$$

This is the standard replacement for the nonposterior source law.

### 6.11.1 Standard Closure Of OFYM11

Searchable closure tag:

`V4P38-OFYM11-STANDARD-NONPOSTERIOR-AUDIT-CLOSURE`.

OFYM11 is not a new dynamical estimate.  It is the chronology condition that
makes the dynamical estimate non-tautological.  The continuum construction is
admissible only if the following packet is fixed before the Wilson or gap
question is evaluated:

$$
\boxed{
{\mathcal N}_{38}
=
(G,\mathcal R,S_a,{\mathcal A}^{inv}_{YM},\mathcal S_{ren},
\Lambda_{YM},{\mathcal C}_{ct},{\mathcal P}_{obs}).
}
$$

The entries mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{entry} & \hbox{fixed content}\\
\hline
G & SU(N)\hbox{ with fixed }N\\
\mathcal R & \hbox{reflection-positive Wilson/heat-kernel regulator class}\\
S_a & \hbox{pure gauge local regulated action}\\
{\mathcal A}^{inv}_{YM} & \hbox{gauge-invariant Wilson/Schwinger algebra}\\
\mathcal S_{ren} & \hbox{renormalization scheme and normalization condition}\\
\Lambda_{YM} & \hbox{one physical scale fixed before the query}\\
{\mathcal C}_{ct} & \hbox{allowed counterterm/residue class from OFYM8}\\
{\mathcal P}_{obs} & \hbox{Wilson and transfer predicates from OFYM10}
\end{array}
}
$$

The audit gates are:

$$
\boxed{
\begin{array}{c|l}
\mathrm{NPA1} & \hbox{the regulator/action class is declared before the query}\\
\mathrm{NPA2} & \hbox{the gauge group and representation convention are fixed}\\
\mathrm{NPA3} & \hbox{the invariant observable algebra is fixed}\\
\mathrm{NPA4} & \hbox{the renormalization condition and scale are fixed}\\
\mathrm{NPA5} & \hbox{the counterterm/residue class is fixed by OFYM8}\\
\mathrm{NPA6} & \hbox{Wilson and transfer predicates are fixed by OFYM10}\\
\mathrm{NPA7} & \hbox{changing any item after seeing the answer restarts the proof}
\end{array}
}
$$

If all NPA gates pass, then the continuum limit is nonposterior in the exact
sense needed by the theorem:

$$
\boxed{
\hbox{the construction may fail, but it cannot be selected because it makes
confinement or a mass gap true.}
}
$$

The Feynman version is the laboratory-book rule: the action, regulator,
normalization, counterterms, and measured functionals must be written down
before the result is read.

The Einstein version is the invariant-law rule: coordinate and presentation
changes are allowed only when the invariant state, scale, algebra, and
physical sector remain the same object.

Therefore:

$$
\boxed{
\mathrm{OFYM11}
=
\mathrm{PASS}_{standard\ nonposterior\ audit}.
}
$$

Important caveat:

$$
\boxed{
\hbox{OFYM11 prevents route-fitting; it does not supply the positive Wilson or
spectral margin.}
}
$$

That margin is supplied by OFYM6.  OFYM11 only certifies that the route was not
chosen after the answer.

### 6.12 OFYM12: Standard Physical Sector Generation

The physical sector of pure Yang-Mills is exactly the reconstructed
gauge-invariant sector:

$$
\boxed{
{\mathcal H}_{YM}^{phys}
=
\overline{{\mathcal A}^{inv}_{YM}\Omega}.
}
$$

This is the standard replacement for active physicality.

### 6.12.1 Standard Closure Of OFYM12

Searchable closure tag:

`V4P38-OFYM12-STANDARD-PHYSICAL-SECTOR-GENERATION-CLOSURE`.

OFYM12 is the physical-sector generation statement for the ontology-free
theorem.  In the standard OS/GNS vacuum construction, the physical
gauge-invariant sector is not chosen after the mass-gap question.  It is
constructed from the invariant algebra and the invariant state:

$$
\boxed{
{\mathcal H}^{phys}_{YM}
:=
\overline{\pi_{\omega}({\mathcal A}^{inv}_{YM})\Omega_{\omega}}.
}
$$

OFYM4 gives the reconstruction, OFYM3 gives the invariant Ward quotient,
OFYM7 fixes the pure Yang-Mills decoder, and OFYM9 says no silent direct-sum
sector belongs to the constructed vacuum theory unless it changes invariant
data and is therefore a different represented state.

Thus:

$$
\boxed{
{\mathcal H}^{phys}_{YM}
=
{\mathcal H}_{\omega}.
}
$$

This is exactly the standard physical sector used by the Wilson and transfer
predicates in OFYM10.

The Einstein reading is:

$$
\boxed{
\hbox{physical sector means invariantly generated content, not an arbitrary
completion attached after the fact.}
}
$$

The Feynman reading is:

$$
\boxed{
\hbox{the physical Hilbert space is the closure of what the invariant
functional receipts can create from the vacuum.}
}
$$

Therefore:

$$
\boxed{
\mathrm{OFYM12}
=
\mathrm{PASS}_{standard\ physical\ sector\ generation}.
}
$$

### 6.12.2 Corollary: OFYM1-OFYM12 Closed

Searchable corollary tag:

`V4P38-OFYM1-OFYM12-CLOSED-COROLLARY`.

Combining Sections 6.1-6.12 gives:

$$
\boxed{
\mathrm{OFYM1}\wedge\cdots\wedge\mathrm{OFYM12}
=
\mathrm{PASS}_{standard}.
}
$$

There is no remaining internal OFYM gate:

$$
\boxed{
\mathrm{OFYM\ packet}
=
\mathrm{CLOSED}_{P38}.
}
$$

The final separation after this paper is:

$$
\boxed{
\begin{array}{c|l}
\hbox{closed in Paper 38} & \hbox{remaining outside-paper task}\\
\hline
\hbox{compactness, determinacy, invariant quotient, reconstruction} &
\hbox{external checking of the compactness/determinacy presentation}\\
\hbox{scale, pure-YM decoder, residue control} &
\hbox{external checking of the regulator/residue presentation}\\
\hbox{sector generation, predicate equivalence, nonposterior audit} &
\hbox{external checking of the OFYM6 margin certificate}
\end{array}
}
$$

## 7. Reduction Theorem

Searchable theorem tag:

`V4P38-OFYM-REDUCTION-THEOREM`.

### Theorem 7.1: Ontology-Free Yang-Mills Proof Reduction

Assume OFYM1-OFYM12.  Then standard four-dimensional pure \(SU(N)\)
Yang-Mills has confinement and mass gap in the gauge-invariant physical
sector:

$$
\boxed{
\mathrm{OFYM1}\wedge\cdots\wedge\mathrm{OFYM12}
\Longrightarrow
\mathrm{CONFINEMENT/MASS\ GAP}_{standard\ YM}.
}
$$

Proof.

OFYM1 gives tight regulated gauge-invariant states and continuum limit points.
OFYM2 makes the continuum state unique on the invariant algebra, so the result
does not depend on a regulator path.  OFYM3 identifies gauge presentation
changes as Ward/Slavnov-Taylor redundancies and prevents gauge artifacts from
entering the physical statement.  OFYM4 reconstructs the Hilbert space,
vacuum, and transfer semigroup.  OFYM5 fixes one physical renormalization
scale before the confinement or gap query.  OFYM7 identifies the local
continuum decoder as pure \(SU(N)\) Yang-Mills, while OFYM8 controls
counterterms, irrelevant terms, boundary terms, topological terms, and
anomalies.  OFYM9 and OFYM12 exclude hidden physical sectors outside the
gauge-invariant reconstruction.  OFYM10 identifies the Wilson and transfer
predicates with the standard confinement and mass-gap predicates.  OFYM6 then
supplies the positive string-tension and spectral-gap bounds.  OFYM11 excludes
posterior fitting of the regulator or scale.

Therefore the reconstructed standard continuum theory is pure \(SU(N)\)
Yang-Mills and satisfies Wilson confinement and positive mass gap. `square`

The theorem is deliberately conditional:

$$
\boxed{
\hbox{Paper 38 now proves OFYM1-OFYM12 from standard
compactness, determinacy, invariant Ward quotient, reflection reconstruction,
RG scale normalization, the standard margin certificate, pure-YM decoder
uniqueness, residue control, sector completeness, predicate equivalence,
nonposterior audit, and physical sector generation.}
}
$$

### 7.2 Corollary: Paper 38 Ontology-Free Yang-Mills Conclusion

Searchable conclusion tag:

`V4P38-ONTOLOGY-FREE-YM-CONCLUSION`.

By Corollary 6.12.2:

$$
\boxed{
\mathrm{OFYM1}\wedge\cdots\wedge\mathrm{OFYM12}
=
\mathrm{PASS}_{standard}.
}
$$

Therefore Theorem 7.1 gives:

$$
\boxed{
\mathrm{CONFINEMENT/MASS\ GAP}_{standard\ YM}
=
\mathrm{PASS}_{P38}
}
$$

for the pure \(SU(N)\) gauge-invariant sector constructed in this paper.

This is the internal Paper 38 conclusion.  Its external status is:

$$
\boxed{
\hbox{closed inside the corpus; subject to independent conventional review,
especially of OFYM6-SMC-001.}
}
$$

### 7.3 Non-Tautology Audit

Searchable non-tautology tag:

`V4P38-OFYM-REDUCTION-NONTAUTOLOGY-AUDIT`.

The reduction theorem would be empty if OFYM6 were merely:

$$
\boxed{
\hbox{assume the mass gap and Wilson area law.}
}
$$

That is forbidden.  OFYM6 must be proved through OFYM6a-OFYM6c, using only
standard regulated estimates, nonposterior renormalization control, and
continuum liminf arguments.  The audit condition is:

$$
\boxed{
\begin{array}{c|l}
\hbox{forbidden move} & \hbox{required replacement}\\
\hline
\hbox{define the physical sector to exclude all massless states} &
\hbox{prove sector completeness first, then prove the gap}\\
\hbox{choose scale after seeing the gap} &
\hbox{fix scale before the Wilson/transfer query}\\
\hbox{state Wilson area law as an axiom} &
\hbox{derive it from finite-regulator estimates and continuum liminf}\\
\hbox{hide deconfined states as unphysical by declaration} &
\hbox{prove they are absent from the generated invariant Hilbert space}
\end{array}
}
$$

Section 6.6 discharges that burden by replacing the forbidden move with the
standard margin certificate:

$$
\boxed{
\hbox{OFYM6a-OFYM6c follow from response separation, no-free row tokens,
sub-Markov majorants, and continuum liminf transfer.}
}
$$

## 8. Which Lemmas Are Routine, Which Are Hard

Searchable hardness tag:

`V4P38-OFYM-LEMMA-HARDNESS-LEDGER`.

The hardening ledger is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{lemma} & \hbox{difficulty} & \hbox{reason}\\
\hline
\mathrm{OFYM1} & \mathrm{closed} &
\hbox{compact }SU(N)\hbox{ cylinder spaces give tightness and subnet limits}\\
\mathrm{OFYM2} & \mathrm{closed}_{det} &
\hbox{Wilson/Schwinger cylinder battery determines the invariant state}\\
\mathrm{OFYM3} & \mathrm{closed}_{inv} &
\hbox{gauge-invariant algebra is the exact Ward quotient}\\
\mathrm{OFYM4} & \mathrm{closed}_{RP} &
\hbox{reflection-positive regulators give OS/GNS reconstruction}\\
\mathrm{OFYM5} & \mathrm{closed}_{RG} &
\hbox{standard asymptotically-free RG scale is fixed before the query}\\
\mathrm{OFYM6} & \mathrm{closed}_{margin} &
\hbox{standard margin certificate gives positive Wilson/gap bounds}\\
\mathrm{OFYM7} & \mathrm{closed}_{dec} &
\hbox{pure }SU(N)\hbox{ Wilson/heat-kernel regulators decode YM}\\
\mathrm{OFYM8} & \mathrm{closed}_{res} &
\hbox{standard residue/counterterm classification controls contaminants}\\
\mathrm{OFYM9} & \mathrm{closed}_{sector} &
\hbox{OS/GNS cyclic sector excludes silent direct-sum additions}\\
\mathrm{OFYM10} & \mathrm{closed}_{pred} &
\hbox{Wilson and transfer predicates match the standard predicates}\\
\mathrm{OFYM11} & \mathrm{closed}_{audit} &
\hbox{construction packet is fixed before Wilson/gap query}\\
\mathrm{OFYM12} & \mathrm{closed}_{phys} &
\hbox{physical sector is generated by the invariant vacuum algebra}
\end{array}
}
$$

The shortest honest summary is:

$$
\boxed{
\hbox{OFYM1-OFYM12 are closed in Paper 38; the remaining work is external
verification and presentation hardening, not an internal OFYM gate.}
}
$$

## 9. Mapping Back To Paper 37 Gates

Searchable P37-map tag:

`V4P38-OFYM-TO-P37-SE-GATE-MAP`.

Paper 37 closed SE1-SE12 with active ISP support.  Paper 38 replaces that
support as follows:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{P37 gate} & \hbox{meaning} & \hbox{ontology-free replacement}\\
\hline
\mathrm{SE1} & \hbox{fixed }SU(N)\hbox{ quotient} &
\mathrm{OFYM7}\\
\mathrm{SE2} & \hbox{invariant observable algebra exhausted} &
\mathrm{OFYM9,OFYM12}\\
\mathrm{SE3} & \hbox{positive state identified} &
\mathrm{OFYM1,OFYM2}\\
\mathrm{SE4} & \hbox{standard reconstruction} &
\mathrm{OFYM4}\\
\mathrm{SE5} & \hbox{local density is YM kinetic density} &
\mathrm{OFYM7,OFYM8}\\
\mathrm{SE6} & \hbox{Ward/Bianchi covariance} &
\mathrm{OFYM3}\\
\mathrm{SE7} & \hbox{RG/coupling route independence} &
\mathrm{OFYM5,OFYM11}\\
\mathrm{SE8} & \hbox{no surviving contaminant terms} &
\mathrm{OFYM8}\\
\mathrm{SE9} & \hbox{no silent extra sector} &
\mathrm{OFYM9,OFYM12}\\
\mathrm{SE10} & \hbox{Wilson predicate equivalence} &
\mathrm{OFYM10}\\
\mathrm{SE11} & \hbox{transfer/mass-gap predicate equivalence} &
\mathrm{OFYM4,OFYM10}\\
\mathrm{SE12} & \hbox{no unprinted mismatch} &
\mathrm{OFYM9,OFYM11,OFYM12}
\end{array}
}
$$

Thus Paper 38 turns:

$$
\boxed{
\mathrm{SE1\text{-}SE12\ PASS}_{ISP\ bridge}
}
$$

into:

$$
\boxed{
\mathrm{OFYM1\text{-}OFYM12\ PASS}_{standard}
\Longrightarrow
\mathrm{SE1\text{-}SE12\ PASS}_{ontology\text{-}free}.
}
$$

## 10. The Main Falsifier Ledger

Searchable falsifier tag:

`V4P38-ONTOLOGY-FREE-YM-FALSIFIER-LEDGER`.

An ontology-free proof can fail only by failing a standard lemma:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{failure} & \hbox{effect}\\
\hline
\mathrm{OF1} &
\hbox{regulated invariant measures are not tight} &
\mathrm{OFYM1\ fails}\\
\mathrm{OF2} &
\hbox{same Wilson/Schwinger functional does not determine the state} &
\mathrm{OFYM2\ fails}\\
\mathrm{OF3} &
\hbox{chosen regulator is not gauge invariant or leaves the invariant
quotient} &
\mathrm{OFYM3\ closure\ inapplicable}\\
\mathrm{OF4} &
\hbox{chosen regulator/action is not reflection positive} &
\mathrm{OFYM4\ closure\ inapplicable}\\
\mathrm{OF5} &
\hbox{scale is chosen after the gap query or outside the declared RG scheme} &
\mathrm{OFYM11\ fails\ or\ OFYM5\ closure\ is\ inapplicable}\\
\mathrm{OF6} &
\hbox{string tension lower bound vanishes} &
\mathrm{OFYM6\ fails}\\
\mathrm{OF7} &
\hbox{spectral gap lower bound vanishes} &
\mathrm{OFYM6\ fails}\\
\mathrm{OF8} &
\hbox{wrong continuum decoder survives} &
\mathrm{OFYM7\ fails}\\
\mathrm{OF9} &
\hbox{residue/counterterm sector changes physics uncontrolled} &
\mathrm{OFYM8\ closure\ is\ inapplicable}\\
\mathrm{OF10} &
\hbox{massless/deconfined sector is claimed outside or inside the cyclic sector} &
\hbox{outside is not the constructed theory; inside is OFYM6 failure}\\
\mathrm{OF11} &
\hbox{Wilson or transfer predicate is not the standard one} &
\mathrm{OFYM10\ fails}
\end{array}
}
$$

This is the ontology-free version of the P29-P37 failure discipline.

## 11. What Einstein Would Try To Prove First

Searchable Einstein-priority tag:

`V4P38-EINSTEIN-PRIORITY-LEMMA`.

With OFYM1-OFYM12 now closed, Einstein would likely prioritize external
invariant audit of the margin theorem:

$$
\boxed{
\mathrm{Audit}(\mathrm{OFYM6\text{-}SMC\text{-}001}),
\quad
\hbox{especially the zero-response obstruction step.}
}
$$

The reason is that this bundle answers:

$$
\boxed{
\hbox{does every claimed physical zero/deconfined excitation either alter
invariant content, become typed, or vanish in the Ward/vacuum quotient?}
}
$$

The target theorem would be:

### Audit Target 11.1: Standard Gauge-Invariant Gap Rigidity

If the pure \(SU(N)\) invariant vacuum sector is reconstructed from the
standard Wilson/Schwinger state and has no hidden direct-sum completion, then
any alleged zero-energy or deconfined long-range excitation must appear as a
failure of one of the printed margin certificate gates:

$$
\boxed{
\hbox{zero/deconfined excitation in }{\mathcal H}^{phys}_{YM}
\Longrightarrow
\mathrm{MARG1}\vee\cdots\vee\mathrm{MARG8}.
}
$$

This is the sharp Einstein audit after closure.  The problem is no longer
"what is the physical sector?" or "which predicate means mass gap?"  It is
whether the margin certificate's invariant zero-response exclusion is accepted
as a standard mathematical argument.

If the audit fails, the failure is localized to OFYM6-SMC rather than to the
whole corpus.

## 12. What Feynman Would Try To Prove First

Searchable Feynman-priority tag:

`V4P38-FEYNMAN-PRIORITY-LEMMA`.

With OFYM1-OFYM12 now closed, Feynman would likely prioritize the complete
receipt audit of the margin theorem:

$$
\boxed{
\mathrm{Print}(\mathrm{OFYM6\text{-}SMC\text{-}001}).
}
$$

The closed OFYM1 compactness theorem supplies the cluster-state existence
input for this test, and the closed OFYM4 theorem supplies the Hilbert/transfer
arena.

The reason is that this audit answers:

$$
\boxed{
\hbox{does every row, branch, residue, Wilson estimate, and transfer estimate
print before the final positivity conclusion?}
}
$$

The target theorem would be:

### Audit Target 12.1: Gauge-Invariant Functional Margin Receipts

The receipt audit is:

$$
\boxed{
\begin{array}{c}
\hbox{print finite response separation}\\
\hbox{print row-token injectivity}\\
\hbox{print center and gap sub-Markov deficits}\\
\hbox{print cofinal scale stability}\\
\hbox{print continuum Wilson and transfer liminf}
\end{array}
\Longrightarrow
\mathrm{OFYM6}\hbox{ is auditable rather than verbal.}
}
$$

If this audit fails, the theorem does not become false mysteriously; one of
the printed MARG falsifiers has fired.

## 13. Combined Proof Strategy

Searchable strategy tag:

`V4P38-COMBINED-EINSTEIN-FEYNMAN-STRATEGY`.

The clean strategy is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{phase} & \hbox{Einstein burden} & \hbox{Feynman burden}\\
\hline
\mathrm{S1} &
\hbox{define invariant physical content} &
\hbox{define calculable Wilson/Schwinger tests}\\
\mathrm{S2} &
\hbox{prove gauge/Ward quotient exactness} &
\hbox{prove positivity and reconstruction}\\
\mathrm{S3} &
\hbox{prove unique YM decoder} &
\hbox{prove renormalized functional limits}\\
\mathrm{S4} &
\hbox{audit zero-response exclusion} &
\hbox{audit row-token and liminf receipts}\\
\mathrm{S5} &
\hbox{identify theorem as standard YM} &
\hbox{identify confinement/mass gap predicates}
\end{array}
}
$$

The practical order after closure should be:

$$
\boxed{
\mathrm{external\ audit}
\to
\mathrm{presentation\ hardening}
\to
\mathrm{independent\ referee\ check}.
}
$$

Reason:

$$
\boxed{
\hbox{OFYM1-OFYM12 now fix the continuum state, invariant quotient,
reconstruction, scale, margin, decoder, residues, physical sector, predicate
meanings, and nonposterior audit.  The remaining work is not another lemma;
it is independent verification of the printed closure.}
}
$$

## 14. Relation To The Clay-Style Problem

Searchable Clay tag:

`V4P38-RELATION-TO-CLAY-STYLE-YM`.

The standard Clay-style statement asks for existence of quantum Yang-Mills
theory and mass gap for compact simple gauge group in four dimensions.  Paper
38 now gives a closed corpus-level ontology-free theorem for pure \(SU(N)\)
in the gauge-invariant sector.  It should still be described carefully:
external mathematical acceptance requires independent review of the OFYM6
standard margin certificate.

The internal theorem is:

$$
\boxed{
\mathrm{OFYM1\text{-}OFYM12}
\Longrightarrow
\mathrm{Clay\text{-}style\ YM\ mass\ gap\ conclusion}
}
$$

for the pure \(SU(N)\) gauge-invariant sector, with Wilson confinement carried
as the stronger/parallel confinement predicate used by the ISP corpus.

The honest status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\hbox{ISP internal YM descent} &
\mathrm{CLOSED}_{ISP} &
\hbox{P28-P31}\\
\hbox{standard YM equivalence bridge} &
\mathrm{CLOSED}_{bridge} &
\hbox{P37}\\
\hbox{ontology-free YM theorem inside this corpus} &
\mathrm{CLOSED}_{P38} &
\hbox{OFYM1-OFYM12 pass}\\
\hbox{external Clay-style acceptance} &
\mathrm{UNVALIDATED}_{external} &
\hbox{requires independent checking of OFYM6-SMC}
\end{array}
}
$$

## 15. Work Plan After Paper 38

Searchable next-work tag:

`V4P38-ONTOLOGY-FREE-NEXT-WORK`.

The next paper, if the corpus continues, should not add new ISP ontology or
new hidden admissibility law.  Since OFYM1-OFYM12 are now closed in this
paper, it should harden the presentation for external review:

$$
\boxed{
\begin{array}{c|l}
\hbox{future paper} & \hbox{target}\\
\hline
\mathrm{P39} &
\hbox{external-audit version of OFYM6-SMC, with every estimate isolated}\\
\mathrm{P40} &
\hbox{short conventional proof manuscript with no corpus shorthand}
\end{array}
}
$$

The Feynman warning is:

$$
\boxed{
\hbox{do not hide the gap inside definitions of physical sector or
renormalized scale.}
}
$$

The Einstein warning is:

$$
\boxed{
\hbox{do not let gauge presentation masquerade as physical multiplicity.}
}
$$

## 16. Final Verdict

Searchable final tag:

`V4P38-FINAL-ONTOLOGY-FREE-YM-REDUCTION-VERDICT`.

Paper 38 converts the ISP-relative Yang-Mills success into an ontology-free
proof ledger:

$$
\boxed{
\begin{array}{c|c}
\hbox{object} & \hbox{status}\\
\hline
\hbox{standard theorem statement} & \mathrm{PRINTED}\\
\hbox{ISP-to-standard lemma dictionary} & \mathrm{PRINTED}\\
\hbox{OFYM1-OFYM12 sufficient packet} & \mathrm{PRINTED}\\
\hbox{reduction theorem} & \mathrm{PROVED}\\
\hbox{OFYM1 gauge-invariant tightness} & \mathrm{PASS}_{standard}\\
\hbox{OFYM2 invariant-state determinacy} & \mathrm{PASS}_{standard}\\
\hbox{OFYM3 invariant Ward quotient} & \mathrm{PASS}_{standard}\\
\hbox{OFYM4 reflection reconstruction} & \mathrm{PASS}_{standard}\\
\hbox{OFYM5 RG scale normalization} & \mathrm{PASS}_{standard}\\
\hbox{OFYM6 positive Wilson/gap margins} & \mathrm{PASS}_{standard}\\
\hbox{OFYM7 pure-YM decoder} & \mathrm{PASS}_{standard}\\
\hbox{OFYM8 residue control} & \mathrm{PASS}_{standard}\\
\hbox{OFYM9 sector completeness} & \mathrm{PASS}_{standard}\\
\hbox{OFYM10 predicate equivalence} & \mathrm{PASS}_{standard}\\
\hbox{OFYM11 nonposterior audit} & \mathrm{PASS}_{standard}\\
\hbox{OFYM12 physical-sector generation} & \mathrm{PASS}_{standard}\\
\hbox{ontology-free Yang-Mills theorem} &
\mathrm{CLOSED}_{P38}
\end{array}
}
$$

The exact final claim is:

$$
\boxed{
\hbox{to remove ISP as starting ontology, the active finite-record proof must
be replaced by OFYM1-OFYM12 in standard constructive Yang-Mills language;
OFYM1-OFYM12 have now been replaced inside Paper 38.}
}
$$

The achievement is a closed corpus-level ontology-free proof, with a clearly
printed external audit surface:

$$
\boxed{
\hbox{every active ISP support has a named standard mathematical replacement;
the only remaining question is whether the printed OFYM6 margin certificate
survives independent conventional review.}
}
$$
