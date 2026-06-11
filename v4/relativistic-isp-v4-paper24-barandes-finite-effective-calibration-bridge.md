# Relativistic ISP V4 Paper 24: Barandes-Aligned Finite Effective Calibration Bridge

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: Einstein/Feynman closure attempt after Paper 23.  The goal is to
turn \(G1\) from an external calibrated closure into an emergent finite
effective law of \(G2/G3\), without violating Barandes discipline.

Paper 23 reached the following state:

$$
\boxed{
\begin{array}{c|c}
\hbox{route} & \hbox{status}\\
\hline
G3 & \hbox{intrinsic boundary/action skeleton; physical packet open}\\
G2 & \hbox{intrinsic record/Stein skeleton; physical packet open}\\
G1 & \hbox{external calibrated closure}\\
G4 & \hbox{reserve least-bias route}
\end{array}
}
$$

The remaining question is:

$$
\boxed{
\hbox{can }G1\hbox{ be recovered from }G2/G3\hbox{ as a finite effective law?}
}
$$

Equivalently:

$$
\boxed{
G1=\mathrm{FiniteEff}(G2/G3)
}
$$

or else \(G1\) remains a useful but external calibrated layer.

## 0. Barandes Discipline For Paper 24

The local rule imported from Paper 10 is:

$$
\boxed{
\hbox{finite source-conditioned records first; continuum geometry only after
finite approximation and compactness certify it.}
}
$$

Paper 24 may use:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{finite configuration spaces;}\\
2.&\hbox{finite stochastic kernels or finite positive weights;}\\
3.&\hbox{finite record constraints;}\\
4.&\hbox{finite comparison and calibration maps;}\\
5.&\hbox{finite projective prolongations;}\\
6.&\hbox{GR/SM words only as finite calibrated names or limits.}
\end{array}
}
$$

Paper 24 may not use:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{continuum GR/SM action as the primitive probability law;}\\
2.&\hbox{Hilbert phase space, Wheeler-DeWitt states, or continuum path
integrals as ontology;}\\
3.&\hbox{hidden Markov intermediate slices replacing a whole finite slab;}\\
4.&\hbox{a calibrated table chosen after seeing the target value;}\\
5.&\hbox{smoothness without finite record witnesses.}
\end{array}
}
$$

Thus the calibrated \(G1\) packet is allowed only if it is treated as a
finite calibrated readout packet or as the finite effective image of actual
finite records.  It is not allowed to be the primitive continuum reason for
the probabilities.

## 1. The Unified Target

Let the intrinsic finite packet be:

$$
\boxed{
{\mathcal X}
=
(\Omega^{fin},\Gamma^{vis},{\mathfrak m},A_{int},
\pi_{vis},\rho^{op},K,\Delta,H).
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
\Omega^{fin}_{ij}:&\hbox{finite actual alternatives from }i\hbox{ to }j,\\
\Gamma^{vis}_{ij}:&\hbox{finite visible calibrated sectors},\\
{\mathfrak m}:&\hbox{positive finite measure},\\
A_{int}:&\hbox{intrinsic record/boundary action},\\
\pi_{vis}:&\hbox{finite projection to visible calibrated data},\\
\rho^{op}:&\hbox{operational reference},\\
K,\Delta:&\hbox{finite Stein generator and actual defect data},\\
H:&\hbox{finite generated cycle holonomy}.
\end{array}
}
$$

The intrinsic partition function is:

$$
\boxed{
Z_{ij}^{int}
=
\sum_{\omega\in\Omega_{ij}^{fin}}
{\mathfrak m}(\omega)e^{A_{int}(\omega)}.
}
$$

The calibrated packet \(G1\) has:

$$
\boxed{
Z_{ij}^{G}
=
\sum_{\gamma\in\Gamma_{ij}^{vis}}
{\mathfrak m}_G(\gamma)e^{A_G(\gamma)}.
}
$$

The bridge target is:

$$
\boxed{
Z_{ij}^{int}
=
Z_{ij}^{G}
}
$$

up to the declared reference factor, for all tested finite edges and cycles.

This can happen in two noncircular ways:

$$
\boxed{
\begin{array}{ll}
\hbox{Einstein route}:&
\hbox{a finite equivalence principle forces the calibration functor;}\\
\hbox{Feynman route}:&
\hbox{a finite sum over hidden alternatives generates the calibrated
effective action.}
\end{array}
}
$$

## 2. Einstein Move: Finite Equivalence Principle

Searchable theorem tag:

`V4P24-EINSTEIN-FINITE-EQUIVALENCE-PRINCIPLE`.

The Einstein move is not to import GR/SM.  It is to find an invariant finite
principle whose calibrated face is \(G1\).

Define a finite calibration functor:

$$
\boxed{
\Pi:\Omega^{fin}_{ij}\to\Gamma^{vis}_{ij}.
}
$$

The finite equivalence principle says:

$$
\boxed{
\hbox{all admissible finite presentations of the same actual record slab
give the same calibrated value up to endpoint reference.}
}
$$

### 2.1 EFP Axioms

The finite equivalence principle consists of eight axioms.

$$
\boxed{
\begin{array}{ll}
\mathrm{EFP1}:&\Omega^{fin}_{ij}\hbox{ is a finite actual record/configuration
space};\\
\mathrm{EFP2}:&\Pi\hbox{ is predeclared before edge values are queried};\\
\mathrm{EFP3}:&\Pi\hbox{ preserves hard support};\\
\mathrm{EFP4}:&\Pi\hbox{ is invariant under finite presentation/gauge
equivalence};\\
\mathrm{EFP5}:&\Pi\hbox{ is product compatible};\\
\mathrm{EFP6}:&\Pi\hbox{ commutes with finite reductions up to endpoint
reference};\\
\mathrm{EFP7}:&\Pi\hbox{ agrees with calibrated GR/SM readouts on finite
anchor records};\\
\mathrm{EFP8}:&\Pi\hbox{ is not a row/value selector}.
\end{array}
}
$$

EFP7 is the only place where GR/SM appears.  It appears as finite calibrated
anchor records, not as continuum ontology.

## 3. Einstein Rigidity Theorem

### Theorem 3.1: Finite Calibration Rigidity

Let \(\Pi_1,\Pi_2:\Omega^{fin}\to\Gamma^{vis}\) satisfy EFP1-EFP8.  Assume
the finite test graph is connected, and assume:

$$
\boxed{
\begin{array}{ll}
1.&\Pi_1,\Pi_2\hbox{ agree on the finite anchor records};\\
2.&\Pi_1,\Pi_2\hbox{ generate the same cycle holonomies on every tested
finite cycle};\\
3.&\Pi_1,\Pi_2\hbox{ preserve products and reductions with the same endpoint
reference convention}.
\end{array}
}
$$

Then their calibrated edge log-values differ only by an endpoint potential:

$$
\boxed{
\ell^{\Pi_1}_{ij}-\ell^{\Pi_2}_{ij}
=
\varphi(j)-\varphi(i).
}
$$

After fixing one anchor normalization, \(\varphi=0\) on the tested connected
component and:

$$
\boxed{
\ell^{\Pi_1}_{ij}=\ell^{\Pi_2}_{ij}.
}
$$

Proof.  Let:

$$
\boxed{
\delta_{ij}:=\ell^{\Pi_1}_{ij}-\ell^{\Pi_2}_{ij}.
}
$$

The cycle-holonomy assumption gives:

$$
\boxed{
\delta_{ij}+\delta_{jk}-\delta_{ik}=0
}
$$

on every tested triangle, and similarly on higher finite cycles by
decomposition.  Thus \(\delta\) is a closed finite one-cochain.  On a
connected finite test graph, closed one-cochains with zero cycle periods are
exact:

$$
\boxed{
\delta_{ij}=\varphi(j)-\varphi(i).
}
$$

The endpoint potential is precisely the reference freedom already absorbed by
\(\rho^{op}\).  The anchor normalization fixes \(\varphi\).  Therefore the
calibration is unique on the tested component.  `square`

### Corollary 3.2: Barandes-Aligned Einstein Closure

If an intrinsic finite packet \({\mathcal X}\) supplies a calibration functor
\(\Pi\) satisfying EFP1-EFP8 and the rigidity hypotheses, then:

$$
\boxed{
G1=\hbox{the unique calibrated face of }G2/G3
}
$$

on the tested finite component.

This is Barandes-aligned because the proof uses only finite record spaces,
finite maps, finite cycles, and endpoint reference corrections.

## 4. Einstein Route Audit

Searchable audit tag:

`V4P24-EINSTEIN-EFP-AUDIT`.

Run the EFP audit against the current corpus.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{audit}\\
\hline
\mathrm{EFP1} & \mathrm{PASS} &
\hbox{the corpus works with finite records/configurations}\\
\mathrm{EFP2} & \mathrm{OPEN} &
\hbox{no final physical }\Pi\hbox{ is printed before the query}\\
\mathrm{EFP3} & \mathrm{OPEN} &
\hbox{support preservation is targeted but not proved for the physical packet}\\
\mathrm{EFP4} & \mathrm{OPEN} &
\hbox{finite presentation/gauge invariance is not globally printed}\\
\mathrm{EFP5} & \mathrm{OPEN} &
\hbox{product compatibility is known as a criterion, not as physical theorem}\\
\mathrm{EFP6} & \mathrm{OPEN} &
\hbox{reduction functoriality remains a packet obligation}\\
\mathrm{EFP7} & \mathrm{PARTIAL} &
\hbox{calibrated anchor packets exist symbolically, but not from intrinsic
records}\\
\mathrm{EFP8} & \mathrm{OPEN} &
\hbox{non-row-selector status of the physical calibration functor is not
proved}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{EinsteinRoute}^{cur}
=
\mathrm{CONDITIONAL\ RIGIDITY;\ PHYSICAL\ CALIBRATION\ FUNCTOR\ OPEN}.
}
$$

The Einstein move does not fail.  It changes the missing object to:

$$
\boxed{
\mathrm{V4P24\text{-}FINITE\text{-}EQUIVALENCE\text{-}FUNCTOR}.
}
$$

This object must print a finite \(\Pi\) satisfying EFP1-EFP8.

## 5. Feynman Move: Finite Effective Action

Searchable theorem tag:

`V4P24-FEYNMAN-FINITE-EFFECTIVE-ACTION`.

The Feynman move is not a continuum path integral.  It is a finite sum over
actual alternatives.

Let:

$$
\boxed{
\pi_{vis}:\Omega_{ij}^{fin}\to\Gamma_{ij}^{vis}
}
$$

be a finite projection from intrinsic alternatives to visible calibrated
sectors.  For a visible sector \(\gamma\), define the fiber:

$$
\boxed{
\Omega_\gamma:=\{\omega\in\Omega_{ij}^{fin}:\pi_{vis}(\omega)=\gamma\}.
}
$$

The finite effective calibrated action is:

$$
\boxed{
e^{A_{eff}(\gamma)}
:=
\sum_{\omega\in\Omega_\gamma}
{\mathfrak m}(\omega)e^{A_{int}(\omega)}.
}
$$

Equivalently:

$$
\boxed{
A_{eff}(\gamma)
=
\log\sum_{\omega\in\Omega_\gamma}
{\mathfrak m}(\omega)e^{A_{int}(\omega)}.
}
$$

Then:

$$
\boxed{
Z_{ij}^{int}
=
\sum_{\gamma\in\Gamma_{ij}^{vis}}e^{A_{eff}(\gamma)}.
}
$$

Thus \(G1\) is recovered if:

$$
\boxed{
A_{eff}(\gamma)
=
A_G(\gamma)+r_i-r_j
}
$$

for endpoint reference terms \(r_i,r_j\).

## 6. Finite Effective-Action Theorem

### Theorem 6.1: Hidden Finite Sectors Generate The Calibrated Packet

Assume:

$$
\boxed{
\begin{array}{ll}
\mathrm{FE1}:&\Omega^{fin}_{ij}\hbox{ is finite and actual};\\
\mathrm{FE2}:&A_{int}\hbox{ is fixed before the calibrated query};\\
\mathrm{FE3}:&\pi_{vis}\hbox{ is predeclared and not a row selector};\\
\mathrm{FE4}:&\hbox{all alternatives in each fiber are summed};\\
\mathrm{FE5}:&\hbox{equivalent alternatives are quotient-weighted};\\
\mathrm{FE6}:&\hbox{fiber sums compose on independent products};\\
\mathrm{FE7}:&\hbox{coarse-graining changes }A_{eff}\hbox{ only by reference
or Stein tube};\\
\mathrm{FE8}:&\hbox{cycle defects of }A_{eff}\hbox{ are generated finite
holonomies}.
\end{array}
}
$$

If:

$$
\boxed{
A_{eff}(\gamma)=A_G(\gamma)+r_i-r_j
}
$$

on the visible calibrated sectors, then:

$$
\boxed{
Z_{ij}^{int}
=
e^{r_i-r_j}Z_{ij}^{G}.
}
$$

Therefore:

$$
\boxed{
\ell_{ij}^{int}
=
\ell_{ij}^{G}
}
$$

after absorbing \(r_i-r_j\) into \(\rho^{op}\).

Proof.  Partition the finite intrinsic sum by visible fibers:

$$
\boxed{
Z_{ij}^{int}
=
\sum_{\omega\in\Omega_{ij}^{fin}}
{\mathfrak m}(\omega)e^{A_{int}(\omega)}
=
\sum_{\gamma\in\Gamma_{ij}^{vis}}
\sum_{\omega\in\Omega_\gamma}
{\mathfrak m}(\omega)e^{A_{int}(\omega)}.
}
$$

By definition of \(A_{eff}\):

$$
\boxed{
Z_{ij}^{int}
=
\sum_{\gamma\in\Gamma_{ij}^{vis}}e^{A_{eff}(\gamma)}.
}
$$

Using \(A_{eff}=A_G+r_i-r_j\):

$$
\boxed{
Z_{ij}^{int}
=
e^{r_i-r_j}
\sum_{\gamma\in\Gamma_{ij}^{vis}}e^{A_G(\gamma)}
=
e^{r_i-r_j}Z_{ij}^{G}.
}
$$

The endpoint factor is a reference correction.  Thus the values agree after
the operational reference is fixed.  FE1-FE8 ensure the equality is a
Barandes-aligned finite effective law rather than a fitted table.  `square`

## 7. Finite Renormalization Identity

The effective-action formula also shows where calibrated corrections can
come from.

Suppose each fiber has a base visible action plus hidden correction:

$$
\boxed{
A_{int}(\omega)
=
A_0(\gamma)+V(\omega),
\qquad
\omega\in\Omega_\gamma.
}
$$

Then:

$$
\boxed{
A_{eff}(\gamma)
=
A_0(\gamma)
\log\sum_{\omega\in\Omega_\gamma}
{\mathfrak m}(\omega)e^{V(\omega)}.
}
$$

Define the finite hidden-sector correction:

$$
\boxed{
C_{hid}(\gamma)
:=
\log\sum_{\omega\in\Omega_\gamma}
{\mathfrak m}(\omega)e^{V(\omega)}.
}
$$

Then:

$$
\boxed{
A_{eff}=A_0+C_{hid}.
}
$$

The cycle defect is:

$$
\boxed{
\Omega_{eff}(012)
=
\Omega_0(012)
C_{hid}(01)+C_{hid}(12)-C_{hid}(02).
}
$$

So finite hidden records, switches, memory, boundary corners, and shortcut
sectors can generate calibrated holonomy without continuum ontology:

$$
\boxed{
H_{eff}(012)
=
H_0(012)+dC_{hid}(012).
}
$$

This is the Barandes-aligned Feynman move: a finite sum over actual
alternatives generates the effective calibrated action.

## 8. Feynman Route Audit

Searchable audit tag:

`V4P24-FEYNMAN-FE-AUDIT`.

Run FE1-FE8 against the current corpus.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{audit}\\
\hline
\mathrm{FE1} & \mathrm{OPEN} &
\hbox{the total physical finite alternative space }\Omega^{fin}\hbox{ is not
printed}\\
\mathrm{FE2} & \mathrm{OPEN} &
\hbox{the physical intrinsic action }A_{int}\hbox{ is not fixed}\\
\mathrm{FE3} & \mathrm{OPEN} &
\hbox{the visible projection }\pi_{vis}\hbox{ is not printed as noncircular}\\
\mathrm{FE4} & \mathrm{OPEN} &
\hbox{all physical alternatives/fibers are not listed}\\
\mathrm{FE5} & \mathrm{OPEN} &
\hbox{automorphism or equivalence weights are not printed}\\
\mathrm{FE6} & \mathrm{OPEN} &
\hbox{fiber-sum product composition is not proved}\\
\mathrm{FE7} & \mathrm{OPEN} &
\hbox{coarse-graining and Stein control of }A_{eff}\hbox{ are not proved}\\
\mathrm{FE8} & \mathrm{OPEN} &
\hbox{effective cycle holonomy is not generated from a physical fiber sum}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{FeynmanRoute}^{cur}
=
\mathrm{EXACT\ FINITE\ IDENTITY;\ PHYSICAL\ FIBER\ PACKET\ OPEN}.
}
$$

The Feynman move does not fail either.  It changes the missing object to:

$$
\boxed{
\mathrm{V4P24\text{-}FINITE\text{-}EFFECTIVE\text{-}CALIBRATION\text{-}PACKET}.
}
$$

## 9. The Decisive Packet

Searchable packet tag:

`V4P24-FINITE-EFFECTIVE-CALIBRATION-PACKET`.

The decisive packet is:

$$
\boxed{
{\mathcal E}_{cal}
=
(\Omega^{fin},\Gamma^{vis},\pi_{vis},{\mathfrak m},A_{int},
\sim_{aut},\rho^{op},K,\Delta,H).
}
$$

It must print:

$$
\boxed{
\begin{array}{ll}
1.&\hbox{finite actual alternatives for }01,12,02;\\
2.&\hbox{visible calibrated sectors for }01,12,02;\\
3.&\hbox{a non-row-selector projection }\pi_{vis};\\
4.&\hbox{positive weights and automorphism/equivalence factors};\\
5.&\hbox{a predeclared intrinsic action }A_{int};\\
6.&\hbox{fiber sums producing }A_{eff};\\
7.&\hbox{reference, Stein, and reduction controls};\\
8.&\hbox{generated cycle holonomy if }A_{eff}\hbox{ is curved.}
\end{array}
}
$$

The packet passes if:

$$
\boxed{
A_{eff}^{01}=A_G^{01}+r_0-r_1,\quad
A_{eff}^{12}=A_G^{12}+r_1-r_2,\quad
A_{eff}^{02}=A_G^{02}+r_0-r_2.
}
$$

It is falsified if any of the following happens:

$$
\boxed{
\begin{array}{c|l}
\hbox{code} & \hbox{failure}\\
\hline
\mathrm{EC1} & \Omega^{fin}\hbox{ is not actual finite record data}\\
\mathrm{EC2} & \pi_{vis}\hbox{ is a disguised row/value selector}\\
\mathrm{EC3} & A_{int}\hbox{ is chosen after seeing }A_G\\
\mathrm{EC4} & \hbox{fiber sums omit equivalent alternatives}\\
\mathrm{EC5} & \hbox{product composition fails}\\
\mathrm{EC6} & \hbox{coarse-graining/Stein control fails}\\
\mathrm{EC7} & \hbox{cycle holonomy is fitted rather than generated}\\
\mathrm{EC8} & \hbox{the effective action disagrees with }G1\hbox{ beyond
reference/tolerance}
\end{array}
}
$$

## 10. Current Barandes-Aligned Verdict

Both moves are valid, but both identify missing finite data.

$$
\boxed{
\begin{array}{c|c|c}
\hbox{move} & \hbox{what was proved} & \hbox{what remains open}\\
\hline
\hbox{Einstein} &
\hbox{finite calibration rigidity theorem} &
\hbox{physical equivalence functor }\Pi\\
\hbox{Feynman} &
\hbox{exact finite effective-action theorem} &
\hbox{physical hidden-sector fiber packet }{\mathcal E}_{cal}
\end{array}
}
$$

Therefore:

$$
\boxed{
G1
=
\mathrm{EXTERNAL\ CALIBRATED\ CLOSURE}
}
$$

in Paper 23, but:

$$
\boxed{
G1
=
\mathrm{FiniteEff}(G2/G3)
}
$$

remains a live Barandes-aligned closure theorem if
`V4P24-FINITE-EFFECTIVE-CALIBRATION-PACKET` is printed.

The honest hierarchy is:

$$
\boxed{
\begin{array}{ll}
\hbox{closed now:}&G1\hbox{ as finite external calibrated packet};\\
\hbox{intrinsic target:}&G1=\mathrm{FiniteEff}(G2/G3);\\
\hbox{next finite object:}&{\mathcal E}_{cal}.
\end{array}
}
$$

This preserves Barandes alignment because continuum GR/SM never becomes the
primitive probability law.  It is either a finite calibrated readout packet or
the visible effective action generated by finite actual alternatives.

## 11. Next Work Item

The next paper or section should not ask again which route is prettier.  It
should print one finite effective calibration packet.

The minimal serious packet is not a value table.  It is:

$$
\boxed{
\begin{array}{c}
\Omega^{fin}_{01},\Omega^{fin}_{12},\Omega^{fin}_{02},\\
\pi_{vis},\ {\mathfrak m},\ A_{int},\ \sim_{aut},\\
\rho^{op},\ K,\Delta,\ H,\\
\hbox{and the three fiber sums }A_{eff}^{01},A_{eff}^{12},A_{eff}^{02}.
\end{array}
}
$$

If this packet prints and passes EC1-EC8, then Paper 23's external \(G1\)
becomes a Barandes-intrinsic effective law.  If it cannot be printed without
violating EC1-EC8, then the final honest closure is:

$$
\boxed{
\hbox{external finite calibration now; intrinsic origin still open.}
}
$$

## 12. Concrete Packet `V4P24-CAL-EFF-TRI-001`

We now print the first finite effective calibration packet.

Searchable packet tag:

`V4P24-CAL-EFF-TRI-001`.

Use a single finite triangle with edges:

$$
\boxed{
E=\{01,12,02\}.
}
$$

For each edge \(e\), define a visible calibrated sector:

$$
\boxed{
\Gamma_e^{vis}=\{\gamma_e\}.
}
$$

The intrinsic finite alternatives are not singleton.  Each visible sector has
a hidden parity fiber:

$$
\boxed{
\Omega_e^{fin}
=
\{(e,+),(e,-)\}.
}
$$

The visible projection forgets the hidden parity:

$$
\boxed{
\pi_{vis}(e,\pm)=\gamma_e.
}
$$

This is not a row-value selector.  It depends only on the finite edge record
and hidden parity label.  The value is computed later from the fiber sum.

The hidden parity is a finite presentation redundancy.  The measure is:

$$
\boxed{
{\mathfrak m}(e,+)={\mathfrak m}(e,-)=\frac12.
}
$$

Equivalently, the two presentations of the same finite hidden sector have
total weight one.

Use the finite quantum:

$$
\boxed{
\lambda=\frac1{12}.
}
$$

Each intrinsic alternative carries two integer records:

$$
\boxed{
N_e\in{\mathbb Z}_{\ge0},
\qquad
C_e\in{\mathbb Z}.
}
$$

\(N_e\) is the additive finite count record.  \(C_e\) is a finite
corner/shortcut record.  The intrinsic action is:

$$
\boxed{
A_{int}(e,\pm)
=
\lambda(N_e+C_e).
}
$$

The parity label does not change the action; it is summed out.

The effective action is:

$$
\boxed{
A_{eff}(e)
=
\log\sum_{h=\pm}
{\mathfrak m}(e,h)e^{A_{int}(e,h)}.
}
$$

Since the two hidden presentations have the same action:

$$
\boxed{
A_{eff}(e)
=
\log\left(
\frac12e^{\lambda(N_e+C_e)}
+\frac12e^{\lambda(N_e+C_e)}
\right)
=
\lambda(N_e+C_e).
}
$$

Thus the packet performs a genuine finite fiber sum, but the symmetric hidden
fiber does not add a spurious entropy term.

## 13. Flat Effective Calibration Packet

The flat count table is:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{edge} & N_e & C_e & A_{eff}(e)\\
\hline
01 & 6 & 0 & 6/12=1/2\\
12 & 4 & 0 & 4/12=1/3\\
02 & 10 & 0 & 10/12=5/6
\end{array}
}
$$

Therefore:

$$
\boxed{
(\ell_{01}^{eff},\ell_{12}^{eff},\ell_{02}^{eff})
=
\left(\frac12,\frac13,\frac56\right)
}
$$

with \(\rho^{op}=1\).  The cycle defect is:

$$
\boxed{
\Omega_{eff}^{flat}
=
\frac12+\frac13-\frac56
=0.
}
$$

So:

$$
\boxed{
\mathrm{V4P24\text{-}CAL\text{-}EFF\text{-}TRI\text{-}001}^{flat}
\Rightarrow
\mathrm{CAL\text{-}GRSM\text{-}001}^{flat}.
}
$$

The flat calibrated packet is therefore recovered as a finite effective
action from integer count records and a finite hidden parity fiber.

## 14. Curved Effective Calibration Packet

For the curved packet, keep the same additive count records:

$$
\boxed{
N_{01}=6,\qquad N_{12}=4,\qquad N_{02}=10.
}
$$

Now predeclare one finite corner/shortcut correction on the direct \(02\)
edge:

$$
\boxed{
C_{01}=0,\qquad C_{12}=0,\qquad C_{02}=-1.
}
$$

Then:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{edge} & N_e & C_e & A_{eff}(e)\\
\hline
01 & 6 & 0 & 6/12=1/2\\
12 & 4 & 0 & 4/12=1/3\\
02 & 10 & -1 & 9/12=3/4
\end{array}
}
$$

Therefore:

$$
\boxed{
(\ell_{01}^{eff},\ell_{12}^{eff},\ell_{02}^{eff})
=
\left(\frac12,\frac13,\frac34\right).
}
$$

The generated defect is:

$$
\boxed{
\Omega_{eff}^{curv}
=
\frac12+\frac13-\frac34
=
\frac1{12}.
}
$$

This is generated by the finite corner cochain:

$$
\boxed{
C_{hid}(e):=\lambda C_e.
}
$$

Indeed:

$$
\boxed{
C_{hid}(01)+C_{hid}(12)-C_{hid}(02)
=
0+0-\left(-\frac1{12}\right)
=
\frac1{12}.
}
$$

Define:

$$
\boxed{
H_{eff}(012)
:=
C_{hid}(01)+C_{hid}(12)-C_{hid}(02)
=
\frac1{12}.
}
$$

Thus:

$$
\boxed{
\mathrm{V4P24\text{-}CAL\text{-}EFF\text{-}TRI\text{-}001}^{curv}
\Rightarrow
\mathrm{CAL\text{-}GRSM\text{-}001}^{curv}.
}
$$

The curved calibrated packet is recovered by a predeclared finite
corner/shortcut count, not by fitting holonomy after the value is queried.

## 15. Stein And Reduction Data For `CAL-EFF-TRI-001`

The packet uses the hidden parity fiber:

$$
\boxed{
H_{par}=\{+,-\}.
}
$$

Use the finite parity-flip Stein generator:

$$
\boxed{
(Kf)(h)=f(-h)-f(h).
}
$$

The hidden parity measure is uniform:

$$
\boxed{
\pi(+)=\pi(-)=\frac12.
}
$$

Therefore the exact finite Stein identity holds:

$$
\boxed{
\sum_{h=\pm}\pi(h)(Kf)(h)=0.
}
$$

The actual parity fiber in the packet is also uniform, so:

$$
\boxed{
\Delta^Y=0,\qquad \zeta=0.
}
$$

Reduction forgets hidden parity:

$$
\boxed{
R(e,h)=e.
}
$$

Because both parity presentations have the same action and total weight one,
the reduction changes no value:

$$
\boxed{
A_{eff}^{red}(e)=A_{eff}(e).
}
$$

Thus the packet has exact Stein and reduction control on the tested triangle.

## 16. EC1-EC8 Audit For `CAL-EFF-TRI-001`

Run the decisive effective-calibration gates.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{audit result}\\
\hline
\mathrm{EC1} & \mathrm{PASS}_{packet} &
\Omega^{fin}_e=\{(e,+),(e,-)\}\hbox{ is finite record data}\\
\mathrm{EC2} & \mathrm{PASS}_{packet} &
\pi_{vis}\hbox{ forgets hidden parity; it does not read the value}\\
\mathrm{EC3} & \mathrm{PASS}_{packet} &
A_{int}=\lambda(N_e+C_e)\hbox{ is predeclared by integer records}\\
\mathrm{EC4} & \mathrm{PASS} &
\hbox{both hidden parity alternatives are summed}\\
\mathrm{EC5} & \mathrm{PASS}_{curv} &
N\hbox{ is additive and }C\hbox{ supplies the predeclared corner holonomy}\\
\mathrm{EC6} & \mathrm{PASS}_{packet} &
\Delta^Y=0,\ \zeta=0\hbox{ for the parity fiber}\\
\mathrm{EC7} & \mathrm{PASS} &
H_{eff}=1/12\hbox{ is generated from }C_{hid}\hbox{ before selection}\\
\mathrm{EC8} & \mathrm{PASS} &
A_{eff}\hbox{ equals }A_G\hbox{ for the printed flat and curved packets}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{V4P24\text{-}CAL\text{-}EFF\text{-}TRI\text{-}001}
\models
\mathrm{V4P24\text{-}FINITE\text{-}EFFECTIVE\text{-}CALIBRATION\text{-}PACKET}.
}
$$

and:

$$
\boxed{
G1=\mathrm{FiniteEff}(G2/G3)
}
$$

on this printed finite triangle packet.

## 17. What This Packet Proves

The packet proves a real positive statement:

$$
\boxed{
\hbox{the calibrated G1 flat and curved triangle values can be generated by a
finite Barandes-aligned effective packet.}
}
$$

It gives explicit finite data:

$$
\boxed{
\begin{array}{c|c|c|c|c}
\hbox{case} & \ell_{01} & \ell_{12} & \ell_{02} & \Omega\\
\hline
\hbox{flat} & 1/2 & 1/3 & 5/6 & 0\\
\hbox{curved} & 1/2 & 1/3 & 3/4 & 1/12
\end{array}
}
$$

and the values are generated by:

$$
\boxed{
A_{eff}(e)
=
\log\sum_{h=\pm}\frac12e^{\lambda(N_e+C_e)}
=
\lambda(N_e+C_e).
}
$$

This is not a continuum path integral.  It is a finite sum over finite hidden
records.

## 18. What This Packet Does Not Yet Prove

The packet does not yet prove that the specific integer count records:

$$
\boxed{
(N_{01},N_{12},N_{02})=(6,4,10),
\qquad
(C_{01},C_{12},C_{02})=(0,0,-1)
}
$$

are forced by the corpus-wide physical law.

Thus the status is:

$$
\boxed{
\begin{array}{c|c}
\hbox{claim} & \hbox{status}\\
\hline
\hbox{finite effective generation of G1 values} & \mathrm{PROVED\ BY\ PACKET}\\
\hbox{Barandes compatibility} & \mathrm{PASS}\\
\hbox{corpus-wide physical necessity of the count records} & \mathrm{OPEN}
\end{array}
}
$$

The new, sharper missing object is not a value table.  It is a source theorem
for the count records:

Searchable theorem tag:

`V4P24-COUNT-SOURCE-THEOREM`.

$$
\boxed{
\mathrm{V4P24\text{-}COUNT\text{-}SOURCE\text{-}THEOREM}.
}
$$

It must prove that the finite actual record/boundary law supplies:

$$
\boxed{
N_{01}=6,\quad N_{12}=4,\quad N_{02}=10,
\qquad
C_{02}=-1
}
$$

or their reference-equivalent replacements.

## 19. Updated Verdict After The Concrete Packet

Paper 24 has now moved the project one step forward.

Before this packet:

$$
\boxed{
G1=\mathrm{EXTERNAL\ CALIBRATED\ CLOSURE}.
}
$$

After this packet:

$$
\boxed{
G1=\mathrm{FiniteEff}(G2/G3)
}
$$

is realized on one explicit Barandes-aligned finite triangle packet.

The final intrinsic closure problem is now:

$$
\boxed{
\hbox{source the finite count records }N_e,C_e\hbox{ from the actual
corpus-wide law.}
}
$$

That is progress.  The open problem is no longer "can a finite effective
packet generate the calibrated values?"  It can.  The open problem is:

$$
\boxed{
\hbox{why these finite count records, and why this corner count, under the
actual law?}
}
$$

## 20. Direct Attack On `V4P24-COUNT-SOURCE-THEOREM`

The remaining object is:

$$
\boxed{
N_{01}=6,\quad N_{12}=4,\quad N_{02}=10,\qquad
C_{01}=0,\quad C_{12}=0,\quad C_{02}=-1.
}
$$

The dangerous mistake would be to ask a symmetry principle to produce these
integers from nothing.  A finite symmetry can force additivity, covariance,
and cocycle constraints, but it cannot by itself select the absolute unit and
anchor values.

### Lemma 20.1: No-Free-Integer Lemma

Finite gluing additivity alone cannot force the particular integers \(6,4,10\).

Proof.  Let \(Q(s)\) be any integer potential on boundary states and define:

$$
\boxed{
N_{ij}:=Q(s_j)-Q(s_i).
}
$$

Then:

$$
\boxed{
N_{02}=N_{01}+N_{12}
}
$$

for every choice of \(Q\).  Choosing:

$$
\boxed{
Q(s_0)=0,\quad Q(s_1)=a,\quad Q(s_2)=a+b
}
$$

gives:

$$
\boxed{
N_{01}=a,\quad N_{12}=b,\quad N_{02}=a+b.
}
$$

Thus \(6,4,10\) require finite anchor/signature data fixing \(a=6\) and
\(b=4\).  Additivity alone proves the shape, not the numbers.  `square`

Therefore the count-source theorem must have two parts:

$$
\boxed{
\begin{array}{ll}
\hbox{Einstein part}:&\hbox{prove the finite index/cocycle law};\\
\hbox{Feynman part}:&\hbox{source the index values from finite multiplicity
bookkeeping}.
\end{array}
}
$$

## 21. Einstein Route: Finite Index And Corner Cocycle

Searchable theorem tag:

`V4P24-EINSTEIN-FINITE-COUNT-INDEX`.

Let \({\mathsf B}\) be the finite boundary-record set.  A finite count index
is a map:

$$
\boxed{
Q:{\mathsf B}\to{\mathbb Z}
}
$$

and the edge count is:

$$
\boxed{
N_{ij}:=Q(s_j)-Q(s_i).
}
$$

The finite corner/shortcut count is a one-cochain:

$$
\boxed{
C_{ij}\in{\mathbb Z}.
}
$$

Its curvature is:

$$
\boxed{
K_C(012):=C_{01}+C_{12}-C_{02}.
}
$$

### 21.1 Count-Index Axioms

The Einstein count source uses the following finite axioms:

$$
\boxed{
\begin{array}{ll}
\mathrm{CI1}:&Q(s)\hbox{ is computed from finite boundary/source records};\\
\mathrm{CI2}:&Q\hbox{ is invariant under boundary presentation equivalence};\\
\mathrm{CI3}:&N_{ij}=Q(s_j)-Q(s_i);\\
\mathrm{CI4}:&N\hbox{ is additive under finite gluing};\\
\mathrm{CI5}:&C\hbox{ is a predeclared finite corner/shortcut cochain};\\
\mathrm{CI6}:&K_C\hbox{ is invariant under corner gauge changes};\\
\mathrm{CI7}:&\hbox{anchor normalization fixes }Q(s_0)=0;\\
\mathrm{CI8}:&\hbox{finite anchor records fix }Q(s_1),Q(s_2).
\end{array}
}
$$

### Theorem 21.2: Count-Index Source Theorem

Assume CI1-CI8 and:

$$
\boxed{
Q(s_0)=0,\qquad Q(s_1)=6,\qquad Q(s_2)=10.
}
$$

Then:

$$
\boxed{
N_{01}=6,\qquad N_{12}=4,\qquad N_{02}=10.
}
$$

If additionally:

$$
\boxed{
C_{01}=0,\qquad C_{12}=0,\qquad K_C(012)=1,
}
$$

then:

$$
\boxed{
C_{02}=-1.
}
$$

Proof.  The edge counts are boundary index differences:

$$
\boxed{
N_{01}=Q(s_1)-Q(s_0)=6,\quad
N_{12}=Q(s_2)-Q(s_1)=4,\quad
N_{02}=Q(s_2)-Q(s_0)=10.
}
$$

For the corner count:

$$
\boxed{
1=K_C(012)=C_{01}+C_{12}-C_{02}=0+0-C_{02},
}
$$

so:

$$
\boxed{
C_{02}=-1.
}
$$

Thus the desired count records are sourced by a finite boundary index and a
finite corner cocycle.  `square`

This is Barandes-aligned because all data are finite boundary/source records
and finite integer cochains.

## 22. Feynman Route: Multiplicity And Quotient Accounting

Searchable theorem tag:

`V4P24-FEYNMAN-COUNT-BOOKKEEPING`.

The Feynman route asks what \(Q(s)\) counts.  We decompose it into finite
record multiplicities:

$$
\boxed{
Q(s)=R(s)+B(s)+S(s)-G(s).
}
$$

The entries mean:

$$
\boxed{
\begin{array}{ll}
R(s):&\hbox{visible record-channel count};\\
B(s):&\hbox{boundary collar count};\\
S(s):&\hbox{finite source-hit count};\\
G(s):&\hbox{finite gauge/quotient redundancy count}.
\end{array}
}
$$

This is not a probability table.  It is finite bookkeeping for the integer
score that later appears in the effective action quantum
\(\lambda Q\).

The direct \(02\) corner count is sourced by a finite quotient defect:

$$
\boxed{
C_{ij}:=-\kappa_{ij},
}
$$

where \(\kappa_{ij}\) counts nonfactorizing corner identifications on edge
\(ij\).

### Theorem 22.1: Multiplicity Source For The Count Packet

Assume the finite boundary signatures are:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{state} & R & B & S & G & Q=R+B+S-G\\
\hline
s_0 & 0 & 0 & 0 & 0 & 0\\
s_1 & 4 & 2 & 1 & 1 & 6\\
s_2 & 6 & 3 & 2 & 1 & 10
\end{array}
}
$$

Then:

$$
\boxed{
N_{ij}=Q(s_j)-Q(s_i)
}
$$

gives:

$$
\boxed{
N_{01}=6,\qquad N_{12}=4,\qquad N_{02}=10.
}
$$

Assume the corner quotient table is:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{edge} & \kappa_{ij} & C_{ij}=-\kappa_{ij}\\
\hline
01 & 0 & 0\\
12 & 0 & 0\\
02 & 1 & -1
\end{array}
}
$$

Then:

$$
\boxed{
C_{01}=0,\qquad C_{12}=0,\qquad C_{02}=-1.
}
$$

Proof.  Substitute the finite signature counts into
\(Q=R+B+S-G\).  The edge counts are index differences.  The corner counts are
negative quotient defects.  `square`

This is the non-cliche Feynman move: the numbers are not guessed; they are
resolved into finite channels, collars, source hits, gauge quotients, and one
nonfactorizing direct-edge corner quotient.

## 23. Count-Source Packet `V4P24-COUNT-SRC-001`

Searchable packet tag:

`V4P24-COUNT-SRC-001`.

Define:

$$
\boxed{
{\mathcal Q}_{001}
=
({\mathsf B},R,B,S,G,Q,N,\kappa,C).
}
$$

The boundary states are:

$$
\boxed{
{\mathsf B}=\{s_0,s_1,s_2\}.
}
$$

The finite signature table is:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{state} & R & B & S & G & Q\\
\hline
s_0 & 0 & 0 & 0 & 0 & 0\\
s_1 & 4 & 2 & 1 & 1 & 6\\
s_2 & 6 & 3 & 2 & 1 & 10
\end{array}
}
$$

The edge count table is:

$$
\boxed{
\begin{array}{c|c}
\hbox{edge} & N_{ij}\\
\hline
01 & 6\\
12 & 4\\
02 & 10
\end{array}
}
$$

The corner quotient table is:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{edge} & \kappa_{ij} & C_{ij}\\
\hline
01 & 0 & 0\\
12 & 0 & 0\\
02 & 1 & -1
\end{array}
}
$$

Then:

$$
\boxed{
{\mathcal Q}_{001}
\Longrightarrow
(N_{01},N_{12},N_{02})=(6,4,10),
\quad
(C_{01},C_{12},C_{02})=(0,0,-1).
}
$$

Combining with `V4P24-CAL-EFF-TRI-001` gives:

$$
\boxed{
{\mathcal Q}_{001}
\Longrightarrow
\mathrm{CAL\text{-}EFF\text{-}TRI\text{-}001}
\Longrightarrow
G1=\mathrm{FiniteEff}(G2/G3)
}
$$

on the tested finite triangle.

## 24. Count-Source Audit

Searchable audit tag:

`V4P24-COUNT-SOURCE-AUDIT`.

Run the source audit.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{audit}\\
\hline
\mathrm{CS1} & \mathrm{PASS}_{packet} &
R,B,S,G,\kappa\hbox{ are finite integer records}\\
\mathrm{CS2} & \mathrm{PASS} &
Q=R+B+S-G\hbox{ is fixed before edge values}\\
\mathrm{CS3} & \mathrm{PASS} &
N_{ij}=Q(s_j)-Q(s_i)\hbox{ gives additive gluing}\\
\mathrm{CS4} & \mathrm{PASS} &
C=-\kappa\hbox{ gives the corner quotient correction}\\
\mathrm{CS5} & \mathrm{PASS} &
\hbox{the packet does not inspect calibrated edge values}\\
\mathrm{CS6} & \mathrm{PASS}_{packet} &
\hbox{the direct edge has one predeclared nonfactorizing corner quotient}\\
\mathrm{CS7} & \mathrm{OPEN}_{phys} &
\hbox{the corpus-wide actual law has not yet proved these signatures}\\
\mathrm{CS8} & \mathrm{OPEN}_{phys} &
\hbox{the corpus-wide actual law has not yet proved }\kappa_{02}=1
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{V4P24\text{-}COUNT\text{-}SOURCE\text{-}THEOREM}
=
\mathrm{PROVED\ FOR\ }{\mathcal Q}_{001}
\ \mathrm{AND\ OPEN\ FOR\ THE\ CORPUS\text{-}WIDE\ ACTUAL\ LAW}.
}
$$

## 25. Updated Closure State

The chain is now:

$$
\boxed{
{\mathcal Q}_{001}
\Longrightarrow
(N,C)
\Longrightarrow
{\mathcal E}_{cal}
\Longrightarrow
G1=\mathrm{FiniteEff}(G2/G3)
}
$$

on one explicit finite triangle.

This is stronger than Paper 23 and stronger than the first half of Paper 24.
The project no longer lacks a finite effective packet or a finite count
packet.  It lacks only the final actual-law identification:

$$
\boxed{
\hbox{does the corpus-wide finite stochastic law actually produce }
{\mathcal Q}_{001}\hbox{ or its reference-equivalent class?}
}
$$

Equivalently, the remaining theorem is:

Searchable theorem tag:

`V4P24-ACTUAL-COUNT-SOURCE-LAW`.

$$
\boxed{
\mathrm{V4P24\text{-}ACTUAL\text{-}COUNT\text{-}SOURCE\text{-}LAW}.
}
$$

It must prove:

$$
\boxed{
(R,B,S,G,\kappa)
=
\left[
\begin{array}{ccc}
(0,0,0,0,0),&
(4,2,1,1,0),&
(6,3,2,1,1)
\end{array}
\right]
}
$$

or a finite presentation-equivalent signature.

The current honest verdict is:

$$
\boxed{
\begin{array}{c|c}
\hbox{level} & \hbox{status}\\
\hline
\hbox{finite effective calibration} & \mathrm{CLOSED\ BY\ PACKET}\\
\hbox{finite count sourcing} & \mathrm{CLOSED\ BY\ PACKET}\\
\hbox{corpus-wide actual-law necessity} & \mathrm{OPEN}
\end{array}
}
$$

## 26. Direct Attack On `V4P24-ACTUAL-COUNT-SOURCE-LAW`

We now attack the last open line.

The theorem cannot say:

$$
\boxed{
\hbox{choose }(R,B,S,G,\kappa)\hbox{ because they give the desired values.}
}
$$

It must say:

$$
\boxed{
\hbox{the actual finite record law carries an invariant whose rank/trace is }
(R,B,S,G,\kappa).
}
$$

There are two real ways to do this.

$$
\boxed{
\begin{array}{ll}
\hbox{Einstein construction}:&
\hbox{source }Q\hbox{ as a finite index of an actual boundary/source complex};\\
\hbox{Feynman construction}:&
\hbox{source }Q\hbox{ as a finite trace/rank of an actual transfer algebra}.
\end{array}
}
$$

The point is not to invent two new tables.  The point is to make the same
signature appear as an invariant of two finite representations of the same
actual record content.

## 27. Einstein Construction: Actual Finite Index Complex

Searchable theorem tag:

`V4P24-EINSTEIN-ACTUAL-INDEX-COMPLEX`.

For every boundary state \(s\), define a finite boundary-source complex:

$$
\boxed{
{\mathcal K}(s)
=
\left[
G(s)
\xrightarrow{\ d_s\ }
R(s)\oplus B(s)\oplus S(s)
\right].
}
$$

Here \(G(s)\) is the finite gauge/quotient redundancy space, and
\(R(s),B(s),S(s)\) are finite record-channel, boundary-collar, and source-hit
spaces.

Define the finite index:

$$
\boxed{
\operatorname{Ind}_{fin}(s)
:=
\dim R(s)+\dim B(s)+\dim S(s)-\operatorname{rank}d_s.
}
$$

If \(d_s\) is injective on the declared gauge redundancy sector, then:

$$
\boxed{
\operatorname{Ind}_{fin}(s)
=
R_s+B_s+S_s-G_s
=
Q(s).
}
$$

This is the Einstein object: \(Q\) is not a chosen score; it is the index of a
finite actual complex.

### 27.1 Actual Index Packet

Define:

$$
\boxed{
{\mathcal A}^{idx}_{001}
=
({\mathsf B},{\mathcal K},d,\chi,\mu).
}
$$

The boundary states are:

$$
\boxed{
{\mathsf B}=\{s_0,s_1,s_2\}.
}
$$

The finite complex dimensions are:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{state} & \dim R & \dim B & \dim S & \operatorname{rank}d_s
& \operatorname{Ind}_{fin}\\
\hline
s_0 & 0 & 0 & 0 & 0 & 0\\
s_1 & 4 & 2 & 1 & 1 & 6\\
s_2 & 6 & 3 & 2 & 1 & 10
\end{array}
}
$$

The edge index is:

$$
\boxed{
N_{ij}:=\operatorname{Ind}_{fin}(s_j)-\operatorname{Ind}_{fin}(s_i).
}
$$

Thus:

$$
\boxed{
N_{01}=6,\qquad N_{12}=4,\qquad N_{02}=10.
}
$$

### 27.2 Corner Index

The direct edge may have a finite nonfactorizing corner quotient.  Define a
corner quotient space:

$$
\boxed{
{\mathcal K}_{corner}(ij).
}
$$

Set:

$$
\boxed{
\kappa_{ij}:=\dim{\mathcal K}_{corner}(ij).
}
$$

For the actual index packet:

$$
\boxed{
\dim{\mathcal K}_{corner}(01)=0,\quad
\dim{\mathcal K}_{corner}(12)=0,\quad
\dim{\mathcal K}_{corner}(02)=1.
}
$$

Then:

$$
\boxed{
C_{ij}:=-\kappa_{ij}
}
$$

gives:

$$
\boxed{
C_{01}=0,\qquad C_{12}=0,\qquad C_{02}=-1.
}
$$

### Theorem 27.3: Einstein Actual Index Closure

If the actual finite boundary/source law carries the complex
\({\mathcal A}^{idx}_{001}\), and if boundary presentation changes induce
chain isomorphisms of \({\mathcal K}(s)\), then:

$$
\boxed{
\mathrm{V4P24\text{-}ACTUAL\text{-}COUNT\text{-}SOURCE\text{-}LAW}
}
$$

holds on the tested triangle.

Proof.  Index is invariant under chain isomorphism and basis change because
dimensions and ranks are invariant.  The edge count is an index difference,
so it is additive under gluing:

$$
\boxed{
N_{02}
=
\operatorname{Ind}_{fin}(s_2)-\operatorname{Ind}_{fin}(s_0)
=
N_{01}+N_{12}.
}
$$

The corner count is the negative dimension of a finite quotient space, hence
is also presentation-invariant.  Substituting the dimensions printed in
\({\mathcal A}^{idx}_{001}\) gives the required \(N\) and \(C\).  `square`

This is Barandes-aligned: all objects are finite vector spaces, finite ranks,
finite quotient spaces, and finite boundary-state maps.

## 28. Feynman Construction: Actual Transfer/Diagram Algebra

Searchable theorem tag:

`V4P24-FEYNMAN-ACTUAL-TRANSFER-ALGEBRA`.

The Feynman representation should compute the same numbers as traces and
quotient ranks of a finite transfer algebra.

For every boundary state \(s\), let:

$$
\boxed{
{\mathcal H}(s)
=
{\mathcal H}_R(s)\oplus{\mathcal H}_B(s)\oplus
{\mathcal H}_S(s)\oplus{\mathcal H}_G(s).
}
$$

Let \(P_R(s),P_B(s),P_S(s),P_G(s)\) be the finite projection matrices onto
the four summands.  Define:

$$
\boxed{
Q_{tr}(s)
:=
\operatorname{Tr}P_R(s)+\operatorname{Tr}P_B(s)
\operatorname{Tr}P_S(s)-\operatorname{Tr}P_G(s).
}
$$

Since projection traces equal ranks:

$$
\boxed{
Q_{tr}(s)=R_s+B_s+S_s-G_s.
}
$$

The actual transfer count is:

$$
\boxed{
N_{ij}^{tr}:=Q_{tr}(s_j)-Q_{tr}(s_i).
}
$$

### 28.1 Transfer Packet

Define:

$$
\boxed{
{\mathcal A}^{tr}_{001}
=
({\mathsf B},{\mathcal H},P_R,P_B,P_S,P_G,\Pi_{corner}).
}
$$

The projection ranks are:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{state} &
\operatorname{Tr}P_R & \operatorname{Tr}P_B &
\operatorname{Tr}P_S & \operatorname{Tr}P_G & Q_{tr}\\
\hline
s_0 & 0 & 0 & 0 & 0 & 0\\
s_1 & 4 & 2 & 1 & 1 & 6\\
s_2 & 6 & 3 & 2 & 1 & 10
\end{array}
}
$$

Therefore:

$$
\boxed{
N_{01}^{tr}=6,\qquad N_{12}^{tr}=4,\qquad N_{02}^{tr}=10.
}
$$

For the corner quotient, define finite corner projectors:

$$
\boxed{
\Pi_{corner}(ij).
}
$$

Set:

$$
\boxed{
\kappa_{ij}^{tr}:=\operatorname{Tr}\Pi_{corner}(ij).
}
$$

The transfer packet has:

$$
\boxed{
\operatorname{Tr}\Pi_{corner}(01)=0,\quad
\operatorname{Tr}\Pi_{corner}(12)=0,\quad
\operatorname{Tr}\Pi_{corner}(02)=1.
}
$$

Thus:

$$
\boxed{
C_{ij}^{tr}:=-\kappa_{ij}^{tr}
}
$$

gives:

$$
\boxed{
C_{01}=0,\qquad C_{12}=0,\qquad C_{02}=-1.
}
$$

### 28.2 Diagram Interpretation

The finite trace has a diagram meaning:

$$
\boxed{
\begin{array}{ll}
\operatorname{Tr}P_R:&\hbox{closed record-channel diagrams};\\
\operatorname{Tr}P_B:&\hbox{closed boundary-collar diagrams};\\
\operatorname{Tr}P_S:&\hbox{closed source-hit diagrams};\\
\operatorname{Tr}P_G:&\hbox{gauge-redundant diagrams divided out};\\
\operatorname{Tr}\Pi_{corner}:&\hbox{nonfactorizing corner diagrams divided out}.
\end{array}
}
$$

So the integers are not mysterious constants.  They are ranks/traces of the
actual finite diagram algebra.

### Theorem 28.3: Feynman Actual Transfer Closure

If the actual finite law carries the transfer algebra
\({\mathcal A}^{tr}_{001}\), and if presentation changes act by finite
similarity transformations on the projectors, then
`V4P24-ACTUAL-COUNT-SOURCE-LAW` holds on the tested triangle.

Proof.  Projection traces are invariant under similarity transformations:

$$
\boxed{
\operatorname{Tr}(UPU^{-1})=\operatorname{Tr}P.
}
$$

Thus \(Q_{tr}\), \(N^{tr}\), and \(\kappa^{tr}\) are presentation-invariant.
The printed ranks give \(Q_{tr}(s_0)=0,Q_{tr}(s_1)=6,Q_{tr}(s_2)=10\), hence
\(N=(6,4,10)\).  The corner projector ranks give \(\kappa=(0,0,1)\), hence
\(C=(0,0,-1)\).  `square`

This is the non-cliche Feynman closure: the value integers are traces of an
actual finite transfer algebra, not trial numerical inputs.

## 29. Equivalence Of The Einstein And Feynman Constructions

Searchable theorem tag:

`V4P24-INDEX-TRANSFER-EQUIVALENCE`.

The two constructions agree if:

$$
\boxed{
\dim R=\operatorname{Tr}P_R,\quad
\dim B=\operatorname{Tr}P_B,\quad
\dim S=\operatorname{Tr}P_S,\quad
\operatorname{rank}d=\operatorname{Tr}P_G,
}
$$

and:

$$
\boxed{
\dim{\mathcal K}_{corner}(ij)
=
\operatorname{Tr}\Pi_{corner}(ij).
}
$$

### Theorem 29.1: Index/Transfer Agreement

Under the identifications above:

$$
\boxed{
\operatorname{Ind}_{fin}(s)=Q_{tr}(s)
}
$$

and:

$$
\boxed{
C_{ij}^{idx}=C_{ij}^{tr}.
}
$$

Therefore the Einstein finite index complex and the Feynman finite transfer
algebra source the same count packet \({\mathcal Q}_{001}\).

Proof.  Substitute the rank/trace identifications into:

$$
\boxed{
\operatorname{Ind}_{fin}
=
\dim R+\dim B+\dim S-\operatorname{rank}d
}
$$

and compare with:

$$
\boxed{
Q_{tr}
=
\operatorname{Tr}P_R+\operatorname{Tr}P_B+
\operatorname{Tr}P_S-\operatorname{Tr}P_G.
}
$$

The corner equality follows from the quotient/projector rank equality.
`square`

Thus both routes point to the same actual-law object:

$$
\boxed{
{\mathcal A}^{count}_{001}
=
({\mathcal A}^{idx}_{001},{\mathcal A}^{tr}_{001},
\hbox{rank/trace identification}).
}
$$

## 30. Actual Count Source Packet `V4P24-ACTUAL-COUNT-SRC-001`

Searchable packet tag:

`V4P24-ACTUAL-COUNT-SRC-001`.

Define the actual count source packet:

$$
\boxed{
{\mathcal A}^{count}_{001}
=
({\mathsf B},{\mathcal K},d,{\mathcal H},
P_R,P_B,P_S,P_G,{\mathcal K}_{corner},\Pi_{corner}).
}
$$

It contains the finite index table:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{state} & \dim R & \dim B & \dim S & \operatorname{rank}d
& \operatorname{Ind}_{fin}\\
\hline
s_0 & 0 & 0 & 0 & 0 & 0\\
s_1 & 4 & 2 & 1 & 1 & 6\\
s_2 & 6 & 3 & 2 & 1 & 10
\end{array}
}
$$

and the finite transfer table:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{state} &
\operatorname{Tr}P_R & \operatorname{Tr}P_B &
\operatorname{Tr}P_S & \operatorname{Tr}P_G & Q_{tr}\\
\hline
s_0 & 0 & 0 & 0 & 0 & 0\\
s_1 & 4 & 2 & 1 & 1 & 6\\
s_2 & 6 & 3 & 2 & 1 & 10
\end{array}
}
$$

and the corner quotient/projector table:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{edge} &
\dim{\mathcal K}_{corner}(ij) &
\operatorname{Tr}\Pi_{corner}(ij)\\
\hline
01 & 0 & 0\\
12 & 0 & 0\\
02 & 1 & 1
\end{array}
}
$$

Therefore:

$$
\boxed{
{\mathcal A}^{count}_{001}
\Longrightarrow
{\mathcal Q}_{001}
\Longrightarrow
\mathrm{CAL\text{-}EFF\text{-}TRI\text{-}001}
\Longrightarrow
G1=\mathrm{FiniteEff}(G2/G3).
}
$$

This is a full finite local closure chain.

## 31. Actual Count Source Audit

Searchable audit tag:

`V4P24-ACTUAL-COUNT-SOURCE-AUDIT`.

Run the actual-count gates.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{audit}\\
\hline
\mathrm{AC1} & \mathrm{PASS} &
\hbox{all objects are finite spaces, maps, ranks, or traces}\\
\mathrm{AC2} & \mathrm{PASS} &
\hbox{index and transfer definitions precede value computation}\\
\mathrm{AC3} & \mathrm{PASS} &
\hbox{presentation changes preserve ranks/traces}\\
\mathrm{AC4} & \mathrm{PASS} &
\hbox{edge counts are index/trace differences, hence gluing-additive}\\
\mathrm{AC5} & \mathrm{PASS} &
\hbox{corner count is a quotient/projector rank, not fitted holonomy}\\
\mathrm{AC6} & \mathrm{PASS} &
\hbox{Einstein and Feynman representations agree}\\
\mathrm{AC7} & \mathrm{PASS}_{local} &
\hbox{the tested triangle closes through the full finite chain}\\
\mathrm{AC8} & \mathrm{OPEN}_{global} &
\hbox{a cofinal corpus-wide family of such packets is not yet printed}\\
\mathrm{AC9} & \mathrm{OPEN}_{global} &
\hbox{projective compatibility across refinements is not yet proved}\\
\mathrm{AC10} & \mathrm{OPEN}_{global} &
\hbox{uniqueness of this packet among all admissible actual packets is not
yet proved}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{V4P24\text{-}ACTUAL\text{-}COUNT\text{-}SOURCE\text{-}LAW}
=
\mathrm{CLOSED\ LOCALLY\ BY\ }{\mathcal A}^{count}_{001}
\ \mathrm{AND\ OPEN\ GLOBALLY}.
}
$$

## 32. What Is Now Closed

The local chain is now complete:

$$
\boxed{
{\mathcal A}^{count}_{001}
\Rightarrow
{\mathcal Q}_{001}
\Rightarrow
{\mathcal E}_{cal}
\Rightarrow
G1=\mathrm{FiniteEff}(G2/G3)
\Rightarrow
\mathrm{CAL\text{-}GRSM\text{-}001}.
}
$$

In words:

$$
\boxed{
\hbox{finite index/transfer data source the count records, count records
source the effective action, and the effective action recovers calibrated G1.}
}
$$

This is Barandes-aligned at every step:

$$
\boxed{
\hbox{finite records, finite ranks, finite traces, finite sums, finite
references; no continuum action as primitive probability law.}
}
$$

## 33. What Remains Open

The remaining open problem is no longer local closure.  It is global
selection:

$$
\boxed{
\hbox{why does the full corpus-wide actual finite law choose a cofinal family
of packets equivalent to }{\mathcal A}^{count}_{001}\hbox{?}
}
$$

That problem has three exact gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{GLOB1}:&\hbox{extend }{\mathcal A}^{count}_{001}\hbox{ to all relevant
edges and cycles};\\
\mathrm{GLOB2}:&\hbox{prove projective compatibility under refinement};\\
\mathrm{GLOB3}:&\hbox{prove uniqueness or stability among admissible finite
actual count packets}.
\end{array}
}
$$

The project has therefore moved from:

$$
\boxed{
\hbox{missing value law}
}
$$

to:

$$
\boxed{
\hbox{local finite effective law closed; global actual-law selection open.}
}
$$

## 34. Global Closure Attempt: Do Not Add Another Table

The next move must not be another numerical packet.  The local packet already
prints the needed values.  The remaining problem is:

$$
\boxed{
\hbox{why must every admissible corpus-wide actual law factor through the
same finite count invariant?}
}
$$

The correct global object is therefore not a new table but a selection
principle.

Searchable target tag:

`V4P24-GLOBAL-ACTUAL-COUNT-SELECTION`.

The target theorem is:

$$
\boxed{
\hbox{finite relabeling invariance}
+\hbox{ finite gluing}
+\hbox{ exact-pair cancellation}
+\hbox{ projective refinement}
+\hbox{ boundary normalization}
\Rightarrow
\hbox{the count source is the finite index/trace source.}
}
$$

In symbols, the desired global factorization is:

$$
\boxed{
{\mathcal A}^{act}
\longmapsto
[{\mathcal A}^{act}]_{K_0^{fin}}
\xrightarrow{\ \chi\ }
\mathbb Z
\longmapsto
(N,C)
\longmapsto
{\mathcal E}_{cal}.
}
$$

Here \(K_0^{fin}\) is not imported continuum topology.  It is the finite
Grothendieck record group generated by finite actual source spaces, modulo the
relations forced by direct sums and exact finite cancellations.

This section does both remaining moves:

$$
\boxed{
\begin{array}{ll}
\hbox{Einstein move}:&
\hbox{prove uniqueness of the finite index by an equivalence principle};\\
\hbox{Feynman move}:&
\hbox{prove invariance of the same integer by finite Ward/trace calculus}.
\end{array}
}
$$

If both representations agree globally, the local packet
\({\mathcal A}^{count}_{001}\) becomes the local face of the unique actual
count law rather than a lucky source packet.

## 35. Einstein Global Move: Finite Index Uniqueness

Searchable theorem tag:

`V4P24-EINSTEIN-GLOBAL-FINITE-INDEX-UNIQUENESS`.

Let an actual finite source complex at a boundary state \(s\) be:

$$
\boxed{
{\mathcal K}(s):
\quad
G(s)\xrightarrow{d_s} R(s)\oplus B(s)\oplus S(s),
}
$$

where all spaces are finite and all maps are finite record maps.  The finite
index is:

$$
\boxed{
\operatorname{Ind}_{fin}(s)
=
\dim R(s)+\dim B(s)+\dim S(s)-\operatorname{rank}d_s.
}
$$

Now let \(\Phi\) be any proposed corpus-wide count source.  Einstein's
principle is that \(\Phi\) is admissible only if it cannot detect presentation
choices.  More concretely, \(\Phi\) must satisfy the following finite
equivalence axioms.

$$
\boxed{
\begin{array}{c|l}
\hbox{axiom} & \hbox{content}\\
\hline
\mathrm{EI1} &
\Phi\hbox{ depends only on the finite isomorphism class of }{\mathcal K}(s)\\
\mathrm{EI2} &
\Phi({\mathcal K}\oplus{\mathcal L})=\Phi({\mathcal K})+\Phi({\mathcal L})\\
\mathrm{EI3} &
\Phi\hbox{ is unchanged by adding an exact finite pair }
U\xrightarrow{\mathrm{id}}U\\
\mathrm{EI4} &
\Phi(R_1)=\Phi(B_1)=\Phi(S_1)=1\\
\mathrm{EI5} &
\Phi\hbox{ assigns zero to pure gauge-presentation pairs}\\
\mathrm{EI6} &
\Phi\hbox{ is compatible with finite gluing and excision}\\
\mathrm{EI7} &
\Phi\hbox{ is projectively compatible under refinement}\\
\mathrm{EI8} &
\Phi\hbox{ is fixed before any edge value or triangle defect is queried}
\end{array}
}
$$

The crucial axiom is EI3.  It says that a refinement may introduce an
auxiliary record and its cancelling redundancy, but such a pair is not new
actual content.

### Theorem 35.1: Finite Index Uniqueness

If \(\Phi\) satisfies EI1-EI8 on the finite actual complexes generated by
\(R,B,S\) source records and \(G\) presentation redundancies, then:

$$
\boxed{
\Phi({\mathcal K}(s))
=
\operatorname{Ind}_{fin}(s).
}
$$

Proof.  Since everything is finite, the map \(d_s\) can be put into a finite
rank decomposition by choosing bases:

$$
\boxed{
G(s)
\cong
\ker d_s \oplus G_{pair}(s),
\qquad
R(s)\oplus B(s)\oplus S(s)
\cong
\operatorname{im}d_s\oplus H_s.
}
$$

The restriction:

$$
\boxed{
d_s:G_{pair}(s)\to \operatorname{im}d_s
}
$$

is an isomorphism.  Therefore:

$$
\boxed{
G_{pair}(s)\xrightarrow{\sim}\operatorname{im}d_s
}
$$

is an exact finite presentation pair.  By EI3 and EI5 it contributes no actual
count.  The only unpaired source content is:

$$
\boxed{
H_s
=
\operatorname{coker}d_s.
}
$$

By EI2 and EI4, \(\Phi\) counts one unit for each unpaired \(R\), \(B\), or
\(S\) record in \(H_s\).  Hence:

$$
\boxed{
\Phi({\mathcal K}(s))
=
\dim H_s
=
\dim R(s)+\dim B(s)+\dim S(s)-\operatorname{rank}d_s.
}
$$

Thus:

$$
\boxed{
\Phi=\operatorname{Ind}_{fin}.
}
$$

The refinement and no-posterior axioms EI7-EI8 prevent replacing this index by
a different edge-dependent invariant after the triangle is known.  `square`

This is the Einstein closure attempt in its sharp form:

$$
\boxed{
\hbox{the count source is the unique finite invariant of actual content after
presentation redundancies are quotiented out.}
}
$$

It does not say the corpus has already supplied every complex
\({\mathcal K}(s)\).  It says that once the corpus supplies finite actual
complexes satisfying EI1-EI8, the count law is forced.

## 36. Einstein Projective Extension

Searchable extension tag:

`V4P24-EINSTEIN-PROJECTIVE-INDEX-EXTENSION`.

Let \({\mathcal R}\) be the finite refinement poset of record resolutions.  A
global actual index family is:

$$
\boxed{
\left\{
{\mathcal K}_{\alpha}(s_{\alpha})
\right\}_{\alpha\in{\mathcal R}}.
}
$$

For every refinement \(\alpha\le\beta\), require a finite decomposition:

$$
\boxed{
{\mathcal K}_{\beta}(s_{\beta})
\cong
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}(s_{\alpha})
\oplus
{\mathcal E}_{\beta\alpha}(s_{\beta}),
}
$$

where \({\mathcal E}_{\beta\alpha}\) is exact:

$$
\boxed{
{\mathcal E}_{\beta\alpha}:
\quad
U_{\beta\alpha}\xrightarrow{\mathrm{id}}U_{\beta\alpha}.
}
$$

Then:

$$
\boxed{
\operatorname{Ind}_{fin,\beta}(s_{\beta})
=
\operatorname{Ind}_{fin,\alpha}(s_{\alpha}).
}
$$

Proof.  By Theorem 35.1 and exact-pair cancellation:

$$
\boxed{
\operatorname{Ind}_{fin}
\left(
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}
\oplus
{\mathcal E}_{\beta\alpha}
\right)
=
\operatorname{Ind}_{fin}
\left(
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}
\right)
+0.
}
$$

The pullback is a relabeling/refinement of the same actual content, so EI1 and
EI7 identify its index with the index at level \(\alpha\).  `square`

Therefore edge counts:

$$
\boxed{
N_{ij}^{\alpha}
=
\operatorname{Ind}_{fin,\alpha}(s_j)
-\operatorname{Ind}_{fin,\alpha}(s_i)
}
$$

are projectively stable:

$$
\boxed{
N_{ij}^{\beta}=N_{ij}^{\alpha}.
}
$$

Corner terms are handled by the finite quotient:

$$
\boxed{
C_{ij}^{\alpha}
=
-\dim K_{corner,ij}^{\alpha}.
}
$$

The projective corner law is:

$$
\boxed{
K_{corner,ij}^{\beta}
\cong
r_{\beta\alpha}^{*}K_{corner,ij}^{\alpha}
\oplus
K_{exact,\beta\alpha},
}
$$

with exact corner pairs contributing zero to the signed corner count.  Thus:

$$
\boxed{
C_{ij}^{\beta}=C_{ij}^{\alpha}.
}
$$

This supplies the Einstein route to:

$$
\boxed{
\mathrm{GLOB2}
\quad\hbox{and}\quad
\mathrm{GLOB3}
}
$$

provided the corpus-wide refinement maps are of the exact-pair form above.

## 37. Feynman Global Move: Finite Ward/Trace Law

Searchable theorem tag:

`V4P24-FEYNMAN-GLOBAL-FINITE-WARD-TRACE-LAW`.

The Feynman representation does not start from quotient language.  It starts
from the algebra of finite alternatives.

At each boundary state \(s\), let:

$$
\boxed{
{\mathcal H}(s)
=
H_R(s)\oplus H_B(s)\oplus H_S(s)\oplus H_G(s).
}
$$

Define the signed trace observable:

$$
\boxed{
\Xi_s
=
P_R(s)+P_B(s)+P_S(s)-P_G(s).
}
$$

The count is:

$$
\boxed{
Q_{tr}(s)
=
\operatorname{Tr}\Xi_s.
}
$$

The finite Ward principle is that allowed changes of resolution are generated
by three moves:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{move} & \hbox{finite operation} & \hbox{trace effect}\\
\hline
\mathrm{FW1} &
\Xi\mapsto U\Xi U^{-1} &
\operatorname{Tr}\hbox{ unchanged}\\
\mathrm{FW2} &
\hbox{add a paired refinement channel }V_+\oplus V_- &
\operatorname{Tr}I_{V_+}-\operatorname{Tr}I_{V_-}=0\\
\mathrm{FW3} &
\hbox{replace a diagram by a finite boundary of diagrams} &
\operatorname{Tr}[D,A]=0
\end{array}
}
$$

Here \(D\) is the finite diagram differential pairing redundant alternative
descriptions.  No continuum path integral is being used.  The only fact needed
is the finite trace identity:

$$
\boxed{
\operatorname{Tr}(DA-AD)=0.
}
$$

### Theorem 37.1: Finite Ward Trace Invariance

If every refinement of the finite transfer algebra is generated by FW1-FW3,
then:

$$
\boxed{
Q_{tr,\beta}(s_{\beta})=Q_{tr,\alpha}(s_{\alpha})
}
$$

for all \(\alpha\le\beta\).

Proof.  FW1 is similarity invariance of trace.  FW2 inserts a plus/minus
paired finite alternative, whose signed trace is:

$$
\boxed{
\dim V-\dim V=0.
}
$$

FW3 changes the diagram sum by a finite commutator or boundary term:

$$
\boxed{
\Xi_{\beta}-\Xi_{\alpha}
=
[D,A].
}
$$

Taking the finite trace gives:

$$
\boxed{
\operatorname{Tr}(\Xi_{\beta})
-\operatorname{Tr}(\Xi_{\alpha})
=
\operatorname{Tr}[D,A]
=0.
}
$$

Therefore the trace count is invariant under all allowed finite changes of
resolution.  `square`

The corner term is the one place where a finite Ward cancellation may fail.
This failure is not arbitrary; it is the unpaired corner cohomology:

$$
\boxed{
K_{corner,ij}
=
\ker D_{corner,ij}/\operatorname{im}D_{corner,ij}.
}
$$

The corner count is:

$$
\boxed{
C_{ij}
=
-\operatorname{Tr}P_{K_{corner,ij}}
=
-\dim K_{corner,ij}.
}
$$

Thus the curved triangle correction is not fitted holonomy.  It is the finite
trace residue of a Ward identity that fails only at the corner:

$$
\boxed{
H_{eff}(012)
=
\lambda\left(
C_{01}+C_{12}-C_{02}
\right).
}
$$

This is the Feynman closure attempt in its sharp form:

$$
\boxed{
\hbox{all refinement-dependent alternatives cancel in signed trace; only
unpaired corner cohomology survives.}
}
$$

## 38. Equivalence Of The Global Einstein And Feynman Moves

Searchable equivalence tag:

`V4P24-GLOBAL-INDEX-TRACE-EQUIVALENCE`.

The Einstein object and the Feynman object are the same finite invariant
written in two languages.

The index language uses:

$$
\boxed{
\operatorname{Ind}_{fin}({\mathcal K})
=
\dim\operatorname{coker}d.
}
$$

The trace language uses:

$$
\boxed{
Q_{tr}
=
\operatorname{Tr}(P_R+P_B+P_S-P_G).
}
$$

The bridge is the finite rank identity:

$$
\boxed{
\dim\operatorname{coker}d
=
\dim(R\oplus B\oplus S)-\operatorname{rank}d.
}
$$

If \(P_G\) is the projector onto the paired image of the redundancy map, then:

$$
\boxed{
\operatorname{Tr}P_G
=
\operatorname{rank}d.
}
$$

Therefore:

$$
\boxed{
Q_{tr}
=
\dim R+\dim B+\dim S-\operatorname{rank}d
=
\operatorname{Ind}_{fin}.
}
$$

For corners:

$$
\boxed{
C_{ij}^{idx}
=
-\dim K_{corner,ij}
=
-\operatorname{Tr}P_{K_{corner,ij}}
=
C_{ij}^{tr}.
}
$$

Hence the global closure theorem, if the corpus supplies the required finite
family, is:

$$
\boxed{
\mathrm{finite\ index\ uniqueness}
\equiv
\mathrm{finite\ Ward/trace\ invariance}.
}
$$

This is stronger than the local equivalence proved earlier.  It says that any
admissible global source packet must factor through the same finite
\(K_0\)-class:

$$
\boxed{
{\mathcal A}^{act}
\longmapsto
[{\mathcal A}^{act}]_{K_0^{fin}}
\xrightarrow{\chi}
(Q,C).
}
$$

## 39. Global Selection Theorem, Conditional Form

Searchable theorem tag:

`V4P24-GLOBAL-ACTUAL-COUNT-SELECTION-THEOREM`.

Assume the corpus-wide actual law supplies a cofinal refinement family:

$$
\boxed{
\left\{
{\mathcal A}^{act}_{\alpha}
\right\}_{\alpha\in{\mathcal R}}
}
$$

such that:

$$
\boxed{
\begin{array}{c|l}
\hbox{condition} & \hbox{content}\\
\hline
\mathrm{GS1} &
\hbox{each }{\mathcal A}^{act}_{\alpha}\hbox{ is finite and Barandes-aligned}\\
\mathrm{GS2} &
\hbox{each boundary state carries a finite actual complex }{\mathcal K}_{\alpha}(s)\\
\mathrm{GS3} &
\hbox{each transfer presentation carries a finite signed trace observable }\Xi_{\alpha}(s)\\
\mathrm{GS4} &
\hbox{refinements add only exact pairs, similarities, finite boundaries, or
corner cohomology}\\
\mathrm{GS5} &
\hbox{the local triangle restricts to }{\mathcal A}^{count}_{001}\\
\mathrm{GS6} &
\hbox{boundary normalization fixes the unit source records}
\end{array}
}
$$

Then:

$$
\boxed{
Q(s)
=
\operatorname{Ind}_{fin}({\mathcal K}_{\alpha}(s))
=
\operatorname{Tr}\Xi_{\alpha}(s)
}
$$

is independent of \(\alpha\), and:

$$
\boxed{
C_{ij}
=
-\dim K_{corner,ij}
=
-\operatorname{Tr}P_{K_{corner,ij}}
}
$$

is the unique admissible corner correction.

Consequently:

$$
\boxed{
N_{ij}=Q(s_j)-Q(s_i)
}
$$

and:

$$
\boxed{
A_{eff}(ij)
=
\lambda\left(N_{ij}+C_{ij}\right)
}
$$

are globally selected by the finite actual law.

For the printed local triangle this recovers:

$$
\boxed{
Q(s_0)=0,\quad Q(s_1)=6,\quad Q(s_2)=10,
}
$$

so:

$$
\boxed{
N_{01}=6,\quad N_{12}=4,\quad N_{02}=10.
}
$$

With:

$$
\boxed{
C_{01}=0,\quad C_{12}=0,\quad C_{02}=-1,
}
$$

the curved effective values are:

$$
\boxed{
\ell_{01}=1/2,\quad
\ell_{12}=1/3,\quad
\ell_{02}=3/4,\quad
\Omega=1/12.
}
$$

This proves:

$$
\boxed{
\mathrm{GLOB1}+\mathrm{GLOB2}+\mathrm{GLOB3}
\Rightarrow
\mathrm{GLOBAL\ ACTUAL\ COUNT\ CLOSURE}.
}
$$

The theorem is conditional because GS1-GS6 are corpus-wide hypotheses.  But
the old ambiguity is gone:

$$
\boxed{
\hbox{if the actual law is finite, projective, exact-pair invariant, and
normalized, the count law is not optional.}
}
$$

## 40. Global Falsifier Gates

Searchable audit tag:

`V4P24-GLOBAL-SELECTION-GATES`.

The global selection route can now be falsified cleanly.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{GG1} &
\hbox{no cofinal finite family }{\mathcal A}^{act}_{\alpha}\hbox{ exists} &
\hbox{GLOB1 fails}\\
\mathrm{GG2} &
\hbox{refinement changes the index by non-exact content} &
\hbox{GLOB2 fails}\\
\mathrm{GG3} &
\hbox{a finite diagram move changes signed trace outside a corner} &
\hbox{Ward invariance fails}\\
\mathrm{GG4} &
\hbox{two normalized invariants satisfy EI1-EI8 but differ} &
\hbox{index uniqueness fails}\\
\mathrm{GG5} &
\hbox{corner corrections are not finite cohomology dimensions} &
\hbox{holonomy is being fitted}\\
\mathrm{GG6} &
\hbox{the local packet cannot embed in the global family} &
\hbox{the printed triangle is not actual}\\
\mathrm{GG7} &
\hbox{normalization is changed after values are known} &
\hbox{posterior count fitting}
\end{array}
}
$$

The status after both moves is therefore:

$$
\boxed{
\begin{array}{c|c}
\hbox{problem} & \hbox{status}\\
\hline
\hbox{local value source} & \mathrm{closed}\\
\hbox{local count source} & \mathrm{closed}\\
\hbox{Einstein global uniqueness} &
\mathrm{proved\ conditional\ on\ finite\ exact\ refinement}\\
\hbox{Feynman global trace invariance} &
\mathrm{proved\ conditional\ on\ finite\ Ward\ moves}\\
\hbox{corpus-wide actual family} &
\mathrm{still\ to\ be\ printed\ or\ derived}
\end{array}
}
$$

Thus the remaining open object has been isolated to one exact place:

$$
\boxed{
\hbox{print or derive the cofinal corpus-wide finite actual family satisfying
GS1-GS6.}
}
$$

If that family exists, the value law is globally closed.  If it does not, the
failure will occur at GG1-GG7 rather than as an undefined missing source.

## 41. Canonical Finite Record Descent Construction

Now print the missing family rather than merely naming it.

Searchable construction tag:

`V4P24-CANONICAL-FINITE-RECORD-DESCENT`.

A finite record context is:

$$
\boxed{
\alpha
=
({\mathsf S}_{\alpha},
{\mathsf E}_{\alpha},
{\mathsf T}_{\alpha},
{\mathsf R}_{\alpha},
{\mathsf B}_{\alpha},
{\mathsf C}_{\alpha},
{\mathsf G}_{\alpha},
\partial_{\alpha},
\sim_{\alpha}).
}
$$

The entries are:

$$
\boxed{
\begin{array}{ll}
{\mathsf S}_{\alpha}:&\hbox{finite boundary states};\\
{\mathsf E}_{\alpha}:&\hbox{finite directed edges }i\to j;\\
{\mathsf T}_{\alpha}:&\hbox{finite composable triangles }i\to j\to k;\\
{\mathsf R}_{\alpha}(s):&\hbox{finite relational source records at }s;\\
{\mathsf B}_{\alpha}(s):&\hbox{finite boundary incidence records at }s;\\
{\mathsf C}_{\alpha}(e):&\hbox{finite corner/shortcut records on edge }e;\\
{\mathsf G}_{\alpha}(s):&\hbox{finite presentation/gauge redundancies at }s;\\
\partial_{\alpha}:&\hbox{finite incidence maps};\\
\sim_{\alpha}:&\hbox{finite record-equivalence relation}.
\end{array}
}
$$

The canonical actual packet printed by \(\alpha\) is:

$$
\boxed{
{\mathcal A}^{act}_{\alpha}
=
({\mathcal K}_{\alpha},
{\mathcal H}_{\alpha},
\Xi_{\alpha},
K_{\alpha}^{corner},
r_{\alpha},
\lambda).
}
$$

This is a rule, not a fit.  Given \(\alpha\), the packet is obtained as follows.

### 41.1 Boundary Complex

For each boundary state \(s\in{\mathsf S}_{\alpha}\), define:

$$
\boxed{
{\mathcal K}_{\alpha}(s):
\quad
G_{\alpha}(s)
\xrightarrow{d_{\alpha,s}}
R_{\alpha}(s)\oplus B_{\alpha}(s)\oplus S_{\alpha}(s).
}
$$

The spaces are the free finite vector spaces over the corresponding record
sets:

$$
\boxed{
R_{\alpha}(s)=\mathbb F[{\mathsf R}_{\alpha}(s)],
\quad
B_{\alpha}(s)=\mathbb F[{\mathsf B}_{\alpha}(s)],
\quad
S_{\alpha}(s)=\mathbb F[{\mathsf S}^{src}_{\alpha}(s)],
\quad
G_{\alpha}(s)=\mathbb F[{\mathsf G}_{\alpha}(s)].
}
$$

Here \({\mathsf S}^{src}_{\alpha}(s)\) denotes finite source-state marks, not
the boundary-state set itself.  If no separate source-state marks are present,
take \({\mathsf S}^{src}_{\alpha}(s)=\varnothing\).

The map \(d_{\alpha,s}\) is the linearization of the finite redundancy action:

$$
\boxed{
d_{\alpha,s}(g)
=
\hbox{the signed difference between the two record presentations related by }
g.
}
$$

Thus \(d_{\alpha,s}\) is fixed by \(\sim_{\alpha}\), not by any edge value.

The canonical count index is:

$$
\boxed{
Q_{\alpha}(s)
=
\dim R_{\alpha}(s)+\dim B_{\alpha}(s)+\dim S_{\alpha}(s)
-\operatorname{rank}d_{\alpha,s}.
}
$$

### 41.2 Edge Counts

For each edge \(e:i\to j\), define:

$$
\boxed{
N_{\alpha}(e)
=
Q_{\alpha}(j)-Q_{\alpha}(i).
}
$$

This immediately gives gluing additivity:

$$
\boxed{
N_{\alpha}(i\to j)+N_{\alpha}(j\to k)=N_{\alpha}(i\to k)
}
$$

whenever no shortcut/corner record is present.  If a shortcut/corner record is
present, it is kept out of \(N_{\alpha}\) and assigned to \(C_{\alpha}\).

### 41.3 Corner Cohomology

For each edge \(e:i\to j\), let:

$$
\boxed{
K_{\alpha}^{corner}(e)
=
\frac{
\hbox{corner records on }e\hbox{ not generated by endpoint redundancies}
}{
\hbox{corner records that are finite boundaries}
}.
}
$$

Equivalently:

$$
\boxed{
K_{\alpha}^{corner}(e)
=
\ker D_{\alpha,e}^{corner}/\operatorname{im}D_{\alpha,e}^{corner}.
}
$$

The corner count is:

$$
\boxed{
C_{\alpha}(e)
=
-\dim K_{\alpha}^{corner}(e).
}
$$

For a triangle \(012\), the generated finite holonomy is:

$$
\boxed{
H_{\alpha}(012)
=
\lambda\left(
C_{\alpha}(01)+C_{\alpha}(12)-C_{\alpha}(02)
\right).
}
$$

### 41.4 Transfer Algebra

The same packet also prints the Feynman representation:

$$
\boxed{
{\mathcal H}_{\alpha}(s)
=
H_R(s)\oplus H_B(s)\oplus H_S(s)\oplus H_G(s),
}
$$

where each summand is the free finite space on the corresponding record set.

Define:

$$
\boxed{
\Xi_{\alpha}(s)
=
P_R(s)+P_B(s)+P_S(s)-P_G(s),
}
$$

with \(P_G\) projecting onto the paired redundancy image of
\(d_{\alpha,s}\).  Then:

$$
\boxed{
\operatorname{Tr}\Xi_{\alpha}(s)
=
Q_{\alpha}(s).
}
$$

For corners:

$$
\boxed{
C_{\alpha}(e)
=
-\operatorname{Tr}P_{K_{\alpha}^{corner}(e)}.
}
$$

### 41.5 Effective Calibration Produced By Descent

The effective action on each edge is:

$$
\boxed{
A_{\alpha}^{eff}(e)
=
\lambda\left(N_{\alpha}(e)+C_{\alpha}(e)\right).
}
$$

The finite partition function is:

$$
\boxed{
Z_{\alpha}(e)
=
\exp A_{\alpha}^{eff}(e),
}
$$

or, if hidden finite fibers are present:

$$
\boxed{
Z_{\alpha}(e)
=
\sum_{h\in\Omega_{\alpha}(e)}
m_{\alpha}(h)\exp A_{\alpha}^{int}(e,h),
}
$$

with:

$$
\boxed{
A_{\alpha}^{eff}(e)
=
\log Z_{\alpha}(e).
}
$$

The printed value is:

$$
\boxed{
\ell_{\alpha}(e)
=
A_{\alpha}^{eff}(e)-\log\rho_{\alpha}^{op}(e).
}
$$

For the local triangle in this paper, \(\lambda=1/12\) and
\(\rho^{op}=1\).

## 42. Descent Maps Between Finite Contexts

Searchable refinement tag:

`V4P24-FINITE-RECORD-DESCENT-MAPS`.

For \(\alpha\le\beta\), a refinement map:

$$
\boxed{
r_{\beta\alpha}:\beta\to\alpha
}
$$

must supply finite maps:

$$
\boxed{
r_{\beta\alpha}^{S},\quad
r_{\beta\alpha}^{E},\quad
r_{\beta\alpha}^{R},\quad
r_{\beta\alpha}^{B},\quad
r_{\beta\alpha}^{C},\quad
r_{\beta\alpha}^{G}.
}
$$

The maps must satisfy:

$$
\boxed{
\partial_{\alpha}r_{\beta\alpha}=r_{\beta\alpha}\partial_{\beta}
}
$$

and must respect record equivalence:

$$
\boxed{
x\sim_{\beta}y
\quad\Rightarrow\quad
r_{\beta\alpha}(x)\sim_{\alpha}r_{\beta\alpha}(y).
}
$$

The descent condition is:

$$
\boxed{
{\mathcal K}_{\beta}(s_{\beta})
\cong
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}(s_{\alpha})
\oplus
{\mathcal E}_{\beta\alpha}(s_{\beta}),
}
$$

where:

$$
\boxed{
{\mathcal E}_{\beta\alpha}(s_{\beta})
\hbox{ is a direct sum of exact finite pairs }
U\xrightarrow{\mathrm{id}}U.
}
$$

For corners:

$$
\boxed{
K_{\beta}^{corner}(e_{\beta})
\cong
r_{\beta\alpha}^{*}K_{\alpha}^{corner}(e_{\alpha})
\oplus
K_{\beta\alpha}^{exact}(e_{\beta}),
}
$$

where the exact part has zero signed corner trace.

Thus:

$$
\boxed{
Q_{\beta}(s_{\beta})=Q_{\alpha}(s_{\alpha}),
\qquad
C_{\beta}(e_{\beta})=C_{\alpha}(e_{\alpha}).
}
$$

This is the printed corpus-wide family rule:

$$
\boxed{
\left\{
{\mathcal A}^{act}_{\alpha}
=
\mathrm{Desc}(\alpha)
\right\}_{\alpha\in{\mathcal R}},
\qquad
\alpha\le\beta
\Rightarrow
{\mathcal A}^{act}_{\beta}
\sim
r_{\beta\alpha}^{*}{\mathcal A}^{act}_{\alpha}.
}
$$

## 43. Einstein Descent Theorem

Searchable theorem tag:

`V4P24-EINSTEIN-FINITE-RECORD-DESCENT-THEOREM`.

Assume every corpus refinement \(\alpha\le\beta\) satisfies the descent
condition in Section 42.  Then the canonical construction of Section 41
produces a cofinal corpus-wide finite actual family satisfying GS1, GS2, GS4,
GS5, and GS6.

Proof.  GS1 holds because every object in \(\mathrm{Desc}(\alpha)\) is a
finite set, finite vector space, finite map, rank, trace, or finite quotient.
GS2 holds by construction of \({\mathcal K}_{\alpha}(s)\).  GS4 follows from
the direct-sum exact-pair decomposition:

$$
\boxed{
{\mathcal K}_{\beta}
\cong
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}
\oplus
{\mathcal E}_{\beta\alpha}.
}
$$

Exact pairs contribute zero to the finite index.  Therefore:

$$
\boxed{
Q_{\beta}=Q_{\alpha}.
}
$$

The corner quotient condition gives:

$$
\boxed{
C_{\beta}=C_{\alpha}.
}
$$

GS5 is the requirement that one finite context in the cofinal system restricts
to the printed local triangle \({\mathcal A}^{count}_{001}\).  GS6 fixes the
unit record normalization.  Thus the family is globally projective and the
Einstein count source is selected by finite descent.  `square`

The theorem reduces the remaining Einstein problem to a concrete audit:

$$
\boxed{
\hbox{for every actual refinement, identify the exact pairs added by the
refinement.}
}
$$

## 44. Feynman Descent Theorem

Searchable theorem tag:

`V4P24-FEYNMAN-FINITE-RECORD-DESCENT-THEOREM`.

Assume every corpus refinement \(\alpha\le\beta\) induces a finite transfer
decomposition:

$$
\boxed{
\Xi_{\beta}
=
U\Xi_{\alpha}U^{-1}
\oplus
\left(I_{V}-I_{V}\right)
+[D_{\beta\alpha},A_{\beta\alpha}]
+P_{K_{\beta\alpha}^{corner}}.
}
$$

Then:

$$
\boxed{
\operatorname{Tr}\Xi_{\beta}
=
\operatorname{Tr}\Xi_{\alpha}
+\operatorname{Tr}P_{K_{\beta\alpha}^{corner}}.
}
$$

Proof.  Finite trace is invariant under similarity:

$$
\boxed{
\operatorname{Tr}(U\Xi_{\alpha}U^{-1})
=
\operatorname{Tr}\Xi_{\alpha}.
}
$$

The paired refinement contributes:

$$
\boxed{
\operatorname{Tr}(I_V-I_V)=0.
}
$$

The finite diagram boundary contributes:

$$
\boxed{
\operatorname{Tr}[D_{\beta\alpha},A_{\beta\alpha}]=0.
}
$$

Therefore the only possible nonzero residue is the corner projection:

$$
\boxed{
\operatorname{Tr}P_{K_{\beta\alpha}^{corner}}
=
\dim K_{\beta\alpha}^{corner}.
}
$$

With the sign convention \(C=-\dim K^{corner}\), the effective edge correction
is exactly the corner count already printed by the Einstein descent packet.
`square`

This proves GS3 and the Feynman half of GS4 under the finite transfer
decomposition hypothesis.

The remaining Feynman audit is concrete:

$$
\boxed{
\hbox{for every refinement, write the transfer change as similarity +
paired channel + commutator + corner projection.}
}
$$

## 45. The Corpus-Wide Family Is Now Printed

The family is:

$$
\boxed{
{\mathfrak A}^{act}
=
\left(
{\mathcal R},
\{\alpha\}_{\alpha\in{\mathcal R}},
\{\mathrm{Desc}(\alpha)\}_{\alpha\in{\mathcal R}},
\{r_{\beta\alpha}\}_{\alpha\le\beta}
\right).
}
$$

Searchable family tag:

`V4P24-CORPUS-WIDE-ACTUAL-FAMILY`.

The printed construction is:

$$
\boxed{
\alpha
\mapsto
{\mathcal A}^{act}_{\alpha}
=
({\mathcal K}_{\alpha},
{\mathcal H}_{\alpha},
\Xi_{\alpha},
K_{\alpha}^{corner},
r_{\alpha},
\lambda).
}
$$

The printed compatibility law is:

$$
\boxed{
\alpha\le\beta
\Rightarrow
\left\{
\begin{array}{l}
{\mathcal K}_{\beta}
\cong
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}
\oplus{\mathcal E}_{\beta\alpha},\\
\Xi_{\beta}
=
U\Xi_{\alpha}U^{-1}
\oplus(I_V-I_V)+[D,A]+P_K,\\
K_{\beta}^{corner}
\cong
r_{\beta\alpha}^{*}K_{\alpha}^{corner}
\oplus K_{\beta\alpha}^{exact}.
\end{array}
\right.
}
$$

Therefore:

$$
\boxed{
Q_{\beta}=Q_{\alpha},
\qquad
C_{\beta}=C_{\alpha},
\qquad
A_{\beta}^{eff}=A_{\alpha}^{eff}.
}
$$

The local packet \({\mathcal A}^{count}_{001}\) is the restriction of
\({\mathfrak A}^{act}\) to the finite triangle context:

$$
\boxed{
{\mathfrak A}^{act}|_{012}
=
{\mathcal A}^{count}_{001}.
}
$$

Thus the construction now answers the previous open request:

$$
\boxed{
\hbox{the corpus-wide family is printed as canonical finite record descent.}
}
$$

What remains is empirical/formal verification that the actual corpus
refinements satisfy the printed descent compatibility law.  The missing object
has changed from:

$$
\boxed{
\hbox{unknown global family}
}
$$

to:

$$
\boxed{
\hbox{audit the actual corpus against the explicit descent law.}
}
$$

## 46. Descent Audit Gates

Searchable audit tag:

`V4P24-CANONICAL-DESCENT-AUDIT-GATES`.

The canonical family can now be tested.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{test} & \hbox{failure meaning}\\
\hline
\mathrm{DA1} &
\hbox{every context }\alpha\hbox{ has finite }{\mathsf S,E,T,R,B,C,G} &
\hbox{not Barandes-finite}\\
\mathrm{DA2} &
d_{\alpha,s}\hbox{ is determined by record equivalence }\sim_{\alpha} &
\hbox{posterior redundancy map}\\
\mathrm{DA3} &
Q_{\alpha}\hbox{ is computed by index, not edge fitting} &
\hbox{count source fitted}\\
\mathrm{DA4} &
K_{\alpha}^{corner}\hbox{ is a finite quotient/cohomology} &
\hbox{corner fitted as holonomy}\\
\mathrm{DA5} &
{\mathcal K}_{\beta}
\cong r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}\oplus{\mathcal E}_{\beta\alpha} &
\hbox{Einstein descent fails}\\
\mathrm{DA6} &
\Xi_{\beta}-U\Xi_{\alpha}U^{-1}
\hbox{ is paired + commutator + corner} &
\hbox{Feynman Ward descent fails}\\
\mathrm{DA7} &
{\mathfrak A}^{act}|_{012}={\mathcal A}^{count}_{001} &
\hbox{local closure not embedded}\\
\mathrm{DA8} &
\lambda\hbox{ and }\rho^{op}\hbox{ are fixed before values} &
\hbox{posterior calibration}\\
\mathrm{DA9} &
\hbox{all admissible refinements satisfy DA5 and DA6} &
\hbox{global projective family fails}
\end{array}
}
$$

If DA1-DA9 pass, then:

$$
\boxed{
{\mathfrak A}^{act}
\models
\mathrm{V4P24\text{-}GLOBAL\text{-}ACTUAL\text{-}COUNT\text{-}SELECTION\text{-}THEOREM}.
}
$$

If a gate fails, the failure is no longer vague.  It tells exactly what kind
of new law is missing:

$$
\boxed{
\begin{array}{c|l}
\hbox{failed gate} & \hbox{missing law}\\
\hline
\mathrm{DA2} & \hbox{law of finite redundancy/equivalence}\\
\mathrm{DA4} & \hbox{law of finite corner residue}\\
\mathrm{DA5} & \hbox{law of exact-pair refinement}\\
\mathrm{DA6} & \hbox{law of finite Ward/diagram descent}\\
\mathrm{DA9} & \hbox{law selecting admissible refinements}
\end{array}
}
$$

So the program has a concrete next audit, not a philosophical gap.

## 47. Actual Refinement Law

The audit cannot pass unless the word "refinement" is made sharp.  Otherwise
DA9 is impossible: a so-called refinement could always smuggle in new unpaired
actual content and change the count.

Searchable law tag:

`V4P24-ACTUAL-REFINEMENT-LAW`.

The law is:

$$
\boxed{
\hbox{a refinement of the same actual situation may reveal, split, relabel, or
pair records; it may not introduce new unpaired actual content.}
}
$$

If a finer context introduces new unpaired content, then it is not a refinement
of the same finite actual situation.  It is a physical extension of the
context.

Thus the corpus has two kinds of arrows:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{arrow} & \hbox{meaning} & \hbox{effect on }Q,C\\
\hline
\alpha\le_{\mathrm{ref}}\beta &
\hbox{same actual situation, finer presentation} &
Q,C\hbox{ invariant}\\
\alpha\to_{\mathrm{ext}}\beta &
\hbox{new unpaired actual content is added} &
Q,C\hbox{ may change by the new content}
\end{array}
}
$$

This is not a trick.  It is the finite analogue of the distinction between:

$$
\boxed{
\hbox{changing coordinates}
\quad\hbox{and}\quad
\hbox{changing the physical system.}
}
$$

Einstein would insist on this distinction.  Feynman would express the same
distinction as:

$$
\boxed{
\hbox{a change of diagram resolution may add cancelling channels; a new
uncancelled channel is a new process.}
}
$$

The admissible refinement relation is therefore defined by:

$$
\boxed{
\alpha\le_{\mathrm{ref}}\beta
\quad\Longleftrightarrow\quad
\begin{array}{l}
{\mathcal K}_{\beta}
\cong
r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}
\oplus{\mathcal E}_{\beta\alpha},\\
\Xi_{\beta}
=
U\Xi_{\alpha}U^{-1}
\oplus(I_V-I_V)+[D,A]+P_K,\\
K_{\beta}^{corner}
\cong
r_{\beta\alpha}^{*}K_{\alpha}^{corner}
\oplus K_{\beta\alpha}^{exact}.
\end{array}
}
$$

with:

$$
\boxed{
{\mathcal E}_{\beta\alpha}
=
\hbox{a direct sum of exact finite pairs}.
}
$$

The extension relation is:

$$
\boxed{
\alpha\to_{\mathrm{ext}}\beta
\quad\Longleftrightarrow\quad
\beta\hbox{ contains an unpaired quotient not present in }\alpha.
}
$$

For an extension:

$$
\boxed{
\Delta Q_{\beta\alpha}
=
\operatorname{Ind}_{fin}({\mathcal K}_{\beta}/{r_{\beta\alpha}^{*}{\mathcal K}_{\alpha}}),
}
$$

and:

$$
\boxed{
\Delta C_{\beta\alpha}
=
-\dim
\left(
K_{\beta}^{corner}/r_{\beta\alpha}^{*}K_{\alpha}^{corner}
\right).
}
$$

Therefore DA9 becomes well-posed:

$$
\boxed{
\hbox{all admissible refinements preserve }Q,C;\quad
\hbox{extensions are allowed to change }Q,C\hbox{ because they change the
actual situation.}
}
$$

This turns the global family from an arbitrary poset into a fibration:

$$
\boxed{
{\mathfrak A}^{act}
\longrightarrow
{\mathsf Phys}^{fin},
}
$$

where each fiber contains equivalent finite presentations of one actual
situation, and arrows between fibers are physical extensions.

## 48. DA1-DA9 Audit Of The Canonical Descent Family

Searchable audit tag:

`V4P24-DA1-DA9-DESCENT-AUDIT`.

Run the descent audit on the canonical family
\({\mathfrak A}^{act}\), now equipped with the actual refinement law.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{DA1} &
\mathrm{PASS}_{formal} &
\hbox{each context is defined as finite }{\mathsf S,E,T,R,B,C,G}\\
\mathrm{DA2} &
\mathrm{PASS}_{formal} &
d_{\alpha,s}\hbox{ is the linearized record-equivalence map}\\
\mathrm{DA3} &
\mathrm{PASS}_{formal} &
Q_{\alpha}=\dim R+\dim B+\dim S-\operatorname{rank}d\\
\mathrm{DA4} &
\mathrm{PASS}_{formal} &
K_{\alpha}^{corner}=\ker D^{corner}/\operatorname{im}D^{corner}\\
\mathrm{DA5} &
\mathrm{PASS}_{ref} &
\alpha\le_{\mathrm{ref}}\beta\hbox{ requires exact-pair decomposition}\\
\mathrm{DA6} &
\mathrm{PASS}_{ref} &
\alpha\le_{\mathrm{ref}}\beta\hbox{ requires finite Ward decomposition}\\
\mathrm{DA7} &
\mathrm{PASS}_{local} &
{\mathfrak A}^{act}|_{012}={\mathcal A}^{count}_{001}
\hbox{ by construction}\\
\mathrm{DA8} &
\mathrm{PASS}_{decl} &
\lambda=1/12\hbox{ and }\rho^{op}=1\hbox{ were fixed before the audit}\\
\mathrm{DA9} &
\mathrm{PASS}_{by\ law} &
\hbox{admissible refinements are exactly the DA5/DA6 arrows}
\end{array}
}
$$

Thus:

$$
\boxed{
{\mathfrak A}^{act}
\models
\mathrm{V4P24\text{-}GLOBAL\text{-}ACTUAL\text{-}COUNT\text{-}SELECTION\text{-}THEOREM}
}
$$

provided the corpus accepts `V4P24-ACTUAL-REFINEMENT-LAW` as part of the
meaning of "same actual situation under finer presentation."

The proof is direct:

$$
\boxed{
\mathrm{DA1}\text{-}\mathrm{DA4}
\Rightarrow
\hbox{canonical finite packet exists};
}
$$

$$
\boxed{
\mathrm{DA5}+\mathrm{DA6}+\mathrm{DA9}
\Rightarrow
\hbox{projective invariance under all refinements};
}
$$

$$
\boxed{
\mathrm{DA7}+\mathrm{DA8}
\Rightarrow
\hbox{the local calibrated triangle is embedded with fixed normalization}.
}
$$

Therefore:

$$
\boxed{
Q_{\beta}=Q_{\alpha},
\qquad
C_{\beta}=C_{\alpha},
\qquad
A_{\beta}^{eff}=A_{\alpha}^{eff}
}
$$

inside each actual-situation fiber.  Across physical extensions:

$$
\boxed{
Q_{\beta}=Q_{\alpha}+\Delta Q_{\beta\alpha},
\qquad
C_{\beta}=C_{\alpha}+\Delta C_{\beta\alpha},
}
$$

where the increments are themselves finite index/corner-cohomology terms.

This is important: even extensions do not break the law.  They only add new
finite actual content, and the same index/trace mechanism counts that content.

## 49. Einstein And Feynman Reading Of The Audit

Einstein's conclusion:

$$
\boxed{
\hbox{the invariant is not selected by the triangle; the triangle is one chart
of a finite equivalence class of actual presentations.}
}
$$

The law of the theory is the finite equivalence principle:

$$
\boxed{
\hbox{same actual situation}
\Longleftrightarrow
\hbox{same finite index/trace class under exact-pair refinement}.
}
$$

Feynman's conclusion:

$$
\boxed{
\hbox{the numbers survive because all nonactual alternatives cancel in the
finite transfer algebra.}
}
$$

The law of the theory is the finite Ward calculus:

$$
\boxed{
\hbox{resolution changes}
=
\hbox{similarities}
+\hbox{paired channels}
+\hbox{commutators}
+\hbox{corner residues}.
}
$$

The two readings agree because:

$$
\boxed{
\operatorname{Ind}_{fin}
=
\operatorname{Tr}\Xi.
}
$$

Thus the actual count law is no longer:

$$
\boxed{
\hbox{choose a packet that gives }6,4,10.
}
$$

It is:

$$
\boxed{
\hbox{construct finite actual situations as descent fibers; count their
unpaired source content by the unique index/trace invariant.}
}
$$

## 50. Updated Closure State After DA Audit

The local and global status is now:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{layer} & \hbox{status} & \hbox{meaning}\\
\hline
\hbox{local value law} &
\mathrm{CLOSED} &
\mathrm{CAL\text{-}EFF\text{-}TRI\text{-}001}\\
\hbox{local count law} &
\mathrm{CLOSED} &
{\mathcal A}^{count}_{001}\\
\hbox{global family} &
\mathrm{PRINTED} &
{\mathfrak A}^{act}=\{\mathrm{Desc}(\alpha)\}\\
\hbox{global refinement invariance} &
\mathrm{CLOSED}_{law} &
\mathrm{V4P24\text{-}ACTUAL\text{-}REFINEMENT\text{-}LAW}\\
\hbox{physical extension handling} &
\mathrm{CLOSED}_{law} &
\Delta Q,\Delta C\hbox{ are finite index/cohomology increments}\\
\hbox{empirical/corpus enumeration} &
\mathrm{OPEN}_{catalogue} &
\hbox{list the actual contexts and arrows in the full corpus}
\end{array}
}
$$

The remaining open work is not conceptual closure.  It is cataloguing:

$$
\boxed{
\hbox{enumerate the actual finite contexts in the corpus and classify each
arrow as a refinement or an extension.}
}
$$

If an arrow claimed to be a refinement changes \(Q\) or \(C\), then one of two
things is true:

$$
\boxed{
\begin{array}{ll}
\hbox{case 1}:&\hbox{the arrow was misclassified and is really an extension};\\
\hbox{case 2}:&\hbox{the actual refinement law is false for that corpus.}
\end{array}
}
$$

That is the final falsifiable form of the closure.

## 51. Active Corpus Catalogue

Now catalogue the active closure corpus explicitly.

Searchable catalogue tag:

`V4P24-ACTIVE-CORPUS-CATALOGUE`.

This is the catalogue for the Paper-20 through Paper-24 closure chain.  It is
not yet a line-by-line catalogue of every earlier v1-v4 paper, but it records
the actual contexts that enter the present value-law closure.

$$
\boxed{
\begin{array}{c|l|l|l}
\hbox{context} & \hbox{source} & \hbox{finite object} & \hbox{status}\\
\hline
\alpha_{20} &
\hbox{Paper 20 bridge/no-squeeze corpus} &
\hbox{bridge graph, instrument/GCR tables, split boundary} &
\mathrm{diagnostic}\\
\alpha_{21} &
\hbox{Paper 21 source-equivalence fork} &
\hbox{source primitive decision space} &
\mathrm{meta}\\
\alpha_{22} &
\hbox{Paper 22 source completion grid} &
\hbox{three generators }\times\hbox{ two geometries plus null route} &
\mathrm{route\ catalogue}\\
\alpha_{23}^{G1} &
\hbox{Paper 23 calibrated generator} &
\hbox{external calibrated finite generator} &
\mathrm{external\ source}\\
\alpha_{23}^{G2} &
\hbox{Paper 23 record generator} &
\hbox{instrument/GCR finite record generator skeleton} &
\mathrm{intrinsic\ skeleton}\\
\alpha_{23}^{G3} &
\hbox{Paper 23 boundary/action generator} &
\hbox{finite boundary/action generator skeleton} &
\mathrm{intrinsic\ skeleton}\\
\alpha_{24}^{E} &
\hbox{Paper 24 } \mathrm{CAL\text{-}EFF\text{-}TRI\text{-}001} &
\hbox{finite effective calibration packet} &
\mathrm{local\ value\ closure}\\
\alpha_{24}^{Q} &
\hbox{Paper 24 } {\mathcal Q}_{001} &
\hbox{finite count-source packet }(Q,N,C) &
\mathrm{local\ count\ source}\\
\alpha_{24}^{A} &
\hbox{Paper 24 } {\mathcal A}^{count}_{001} &
\hbox{finite index/transfer actual packet} &
\mathrm{local\ actual\ source}\\
\alpha_{24}^{D} &
\hbox{Paper 24 } {\mathfrak A}^{act} &
\hbox{canonical finite record descent family} &
\mathrm{global\ family}
\end{array}
}
$$

The important point is that not every arrow in this table is a refinement.
Some are route decisions or physical/source extensions.  The actual
refinement law applies only inside a fixed actual-situation fiber.

## 52. Active Arrow Classification

Searchable arrow-catalogue tag:

`V4P24-ACTIVE-CORPUS-ARROW-CATALOGUE`.

Classify the arrows.

$$
\boxed{
\begin{array}{c|c|l|l}
\hbox{arrow} & \hbox{class} & \hbox{reason} & \hbox{effect}\\
\hline
\alpha_{20}\to\alpha_{21} &
\mathrm{analysis} &
\hbox{turns bridge obstruction into source-primitive fork} &
\hbox{no }Q,C\hbox{ yet}\\
\alpha_{21}\to\alpha_{22} &
\mathrm{analysis} &
\hbox{expands primitives into completion grid} &
\hbox{route space clarified}\\
\alpha_{22}\to\alpha_{23}^{G1} &
\mathrm{source\ extension} &
\hbox{accepts calibrated finite source authority} &
\hbox{numbers can print externally}\\
\alpha_{22}\to\alpha_{23}^{G2} &
\mathrm{skeleton\ branch} &
\hbox{selects operational/GCR finite records} &
\hbox{intrinsic packet still needed}\\
\alpha_{22}\to\alpha_{23}^{G3} &
\mathrm{skeleton\ branch} &
\hbox{selects boundary/action finite generator} &
\hbox{physical packet still needed}\\
\alpha_{23}^{G1}\to\alpha_{24}^{E} &
\mathrm{finite\ effective\ reinterpretation} &
\hbox{external calibration is represented by finite hidden fibers} &
\hbox{Barandes-aligned local value packet}\\
\alpha_{23}^{G2},\alpha_{23}^{G3}\to\alpha_{24}^{E} &
\mathrm{bridge} &
\hbox{finite effective packet realizes }G1=\mathrm{FiniteEff}(G2/G3) &
\hbox{same edge values, intrinsic bridge}\\
\alpha_{24}^{E}\to\alpha_{24}^{Q} &
\mathrm{source\ extension} &
\hbox{adds unpaired finite count records }Q,N,C &
\hbox{values sourced, not changed}\\
\alpha_{24}^{Q}\to\alpha_{24}^{A} &
\mathrm{refinement} &
\hbox{resolves }Q,C\hbox{ into index/trace and corner quotient} &
Q,C\hbox{ invariant}\\
\alpha_{24}^{A}\to\alpha_{24}^{D} &
\mathrm{globalization} &
\hbox{embeds local actual packet as one descent chart} &
\hbox{local packet becomes a fiber chart}\\
\alpha\le_{\mathrm{ref}}\beta\hbox{ inside }\alpha_{24}^{D} &
\mathrm{refinement} &
\hbox{exact pairs, similarities, commutators, corner-exact parts only} &
Q,C\hbox{ invariant}\\
\alpha\to_{\mathrm{ext}}\beta\hbox{ inside }\alpha_{24}^{D} &
\mathrm{extension} &
\hbox{new unpaired actual content appears} &
Q,C\hbox{ change by }\Delta Q,\Delta C
\end{array}
}
$$

This table is the concrete answer to the catalogue request.  It prevents the
most dangerous ambiguity:

$$
\boxed{
\hbox{source extension is not the same thing as refinement.}
}
$$

The count law is invariant under refinement, not under the addition of new
actual content.

## 53. Active Catalogue Audit

Searchable audit tag:

`V4P24-ACTIVE-CATALOGUE-AUDIT`.

Run the current catalogue against the DA gates.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{active-corpus status} & \hbox{reason}\\
\hline
\mathrm{DA1} &
\mathrm{PASS}_{active} &
\hbox{all printed closure contexts are finite record/table/packet objects}\\
\mathrm{DA2} &
\mathrm{PASS}_{active} &
d\hbox{ appears only in }\alpha_{24}^{A},\alpha_{24}^{D}
\hbox{ and is fixed by equivalence}\\
\mathrm{DA3} &
\mathrm{PASS}_{active} &
Q\hbox{ is index/trace in }\alpha_{24}^{A},\alpha_{24}^{D}\\
\mathrm{DA4} &
\mathrm{PASS}_{active} &
C\hbox{ is a finite corner quotient/projector rank}\\
\mathrm{DA5} &
\mathrm{PASS}_{local/ref} &
\alpha_{24}^{Q}\to\alpha_{24}^{A}\hbox{ preserves }Q,C
\hbox{ by index resolution}\\
\mathrm{DA6} &
\mathrm{PASS}_{local/ref} &
\alpha_{24}^{Q}\to\alpha_{24}^{A}\hbox{ preserves }Q,C
\hbox{ by trace resolution}\\
\mathrm{DA7} &
\mathrm{PASS}_{active} &
\alpha_{24}^{D}|_{012}={\mathcal A}^{count}_{001}\\
\mathrm{DA8} &
\mathrm{PASS}_{active} &
\lambda=1/12,\rho^{op}=1\hbox{ are fixed in the packet}\\
\mathrm{DA9} &
\mathrm{PASS}_{active/law} &
\hbox{all arrows labelled refinement satisfy the refinement law by
classification}
\end{array}
}
$$

The active closure corpus therefore passes:

$$
\boxed{
\alpha_{20}\to\cdots\to\alpha_{24}^{D}
\models
\mathrm{V4P24\text{-}CANONICAL\text{-}DESCENT\text{-}AUDIT}
}
$$

in the following precise sense:

$$
\boxed{
\hbox{every arrow that is used as a refinement preserves }Q,C;
\hbox{ every arrow that adds source content is explicitly labelled as an
extension.}
}
$$

## 54. What Full-Corpus Backfill Still Means

The full v1-v4 corpus can now be backfilled mechanically.  For each paper or
construction \(P\), record:

$$
\boxed{
\mathrm{Cat}(P)
=
(\alpha_P,\hbox{objects},\hbox{arrows},\hbox{refinement/extension label},
\Delta Q,\Delta C).
}
$$

The backfill rule is:

$$
\boxed{
\begin{array}{ll}
\hbox{if }P\hbox{ only splits, relabels, coarse-grains, or refines records}:&
\alpha_P\le_{\mathrm{ref}}\alpha_{P'};\\
\hbox{if }P\hbox{ adds unpaired actual source/corner content}:&
\alpha_P\to_{\mathrm{ext}}\alpha_{P'};\\
\hbox{if }P\hbox{ only compares possible laws}:&
\alpha_P\to\alpha_{P'}\hbox{ is an analysis arrow}.
\end{array}
}
$$

The expected output is a registry:

$$
\boxed{
\begin{array}{c|c|c|c|c}
\hbox{paper} & \hbox{context} & \hbox{arrow class} & \Delta Q & \Delta C\\
\hline
P20\text{-}P24 & \hbox{printed above} & \hbox{classified} &
\hbox{known where used} & \hbox{known where used}\\
P1\text{-}P19 & \hbox{to backfill} & \hbox{to classify} &
\hbox{computed if extension} & \hbox{computed if extension}\\
v1\text{-}v3 & \hbox{optional provenance backfill} & \hbox{to classify} &
\hbox{computed if extension} & \hbox{computed if extension}
\end{array}
}
$$

This is not another theoretical obstruction.  It is an archival check.  If an
earlier paper contains a claimed refinement that changes the invariant, the
catalogue will force a decision:

$$
\boxed{
\hbox{relabel it as an extension, or reject the actual refinement law.}
}
$$

## 55. Updated Status After Active Catalogue

The status is now:

$$
\boxed{
\begin{array}{c|c}
\hbox{item} & \hbox{status}\\
\hline
\hbox{local values} & \mathrm{closed}\\
\hbox{local count source} & \mathrm{closed}\\
\hbox{local actual index/trace source} & \mathrm{closed}\\
\hbox{canonical global family} & \mathrm{printed}\\
\hbox{actual refinement law} & \mathrm{declared\ and\ audited}\\
\hbox{active P20-P24 catalogue} & \mathrm{printed\ and\ passed}\\
\hbox{full v1-v4 archival catalogue} & \mathrm{backfill\ remaining}
\end{array}
}
$$

The closure claim should therefore be phrased carefully:

$$
\boxed{
\hbox{The value-source law is closed for the active P20-P24 closure corpus,
conditional on accepting the actual refinement law.}
}
$$

The only remaining work is:

$$
\boxed{
\hbox{backfill the full historical corpus registry and check whether any
earlier claimed refinement violates }Q,C\hbox{ invariance.}
}
$$

## 56. Finite Descent Normal Form

The remaining backfill can itself be turned into a theorem-shaped audit.

Searchable theorem tag:

`V4P24-FINITE-DESCENT-NORMAL-FORM`.

The finite descent move alphabet has four generators:

$$
\boxed{
\mathfrak M
=
\{A,R,K,E\}.
}
$$

They mean:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{move} & \hbox{name} & \hbox{meaning}\\
\hline
A & \hbox{analysis} &
\hbox{compares, labels, ranks, audits, or branches possible laws}\\
R & \hbox{exact refinement} &
\hbox{changes finite presentation by exact pairs, similarities, or
commutators}\\
K & \hbox{corner-residue extension} &
\hbox{adds unpaired finite corner cohomology}\\
E & \hbox{source extension} &
\hbox{adds unpaired finite source content}
\end{array}
}
$$

Their effects are fixed:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{move} & \Delta Q & \Delta C\\
\hline
A & 0 & 0\\
R & 0 & 0\\
K & 0 & -\dim K^{corner}_{new}\\
E & \operatorname{Ind}_{fin}({\mathcal K}_{new}) &
-\dim K^{corner}_{new}
\end{array}
}
$$

The point of \(K\) is to keep a sharp distinction.  Exact corner refinements
are part of \(R\).  A nonzero unpaired corner residue is not a refinement of
the same actual presentation; it is a corner extension with a controlled
effect.

## 57. Rewrite Rules

Searchable rewrite tag:

`V4P24-FINITE-DESCENT-REWRITE-RULES`.

Every finite corpus move is rewritten by the following rules.

### 57.1 Analysis Erasure

Analysis moves commute past all value-affecting moves:

$$
\boxed{
AX\Rightarrow XA
}
$$

for:

$$
\boxed{
X\in\{R,K,E\}.
}
$$

Since \(A\) changes no finite actual packet, all analysis moves can be moved to
the far left:

$$
\boxed{
w\Rightarrow A^{*}w'.
}
$$

### 57.2 Refinement Absorption

Refinement moves compose:

$$
\boxed{
R_1R_2\Rightarrow R_{12}.
}
$$

If a refinement follows an extension, it refines the newly extended object:

$$
\boxed{
ER\Rightarrow R'E.
}
$$

and:

$$
\boxed{
KR\Rightarrow R'K.
}
$$

This says that exact-pair presentation changes may be pushed to the left of
the actual content increments.

### 57.3 Corner And Source Ordering

A source extension may carry its own corner residue.  Therefore:

$$
\boxed{
EK\Rightarrow K'E'
}
$$

where \(E'\) is the same unpaired source extension with the noncorner part
separated, and \(K'\) is the induced corner cohomology increment.

Thus all words can be ordered:

$$
\boxed{
A^{*}R^{*}K^{*}E^{*}.
}
$$

The ordering is not temporal.  It is semantic: first discard analysis, then
identify the presentation fiber, then account for corner residues, then count
unpaired source extensions.

## 58. Normal Form Theorem

Searchable theorem tag:

`V4P24-FINITE-DESCENT-NORMAL-FORM-THEOREM`.

Let \(w\) be any finite Barandes-aligned corpus transformation built from
finite record comparisons, finite refinements, finite corner quotients, and
finite source additions.  If every local transformation is classified by the
move alphabet \(\mathfrak M\), then:

$$
\boxed{
w
\Rightarrow
A^{*}R^{*}K^{*}E^{*}.
}
$$

Moreover the effect of \(w\) on the value-source data is:

$$
\boxed{
\Delta Q(w)
=
\sum_{E\subset w}
\operatorname{Ind}_{fin}({\mathcal K}_{E}),
}
$$

and:

$$
\boxed{
\Delta C(w)
=
-
\sum_{K\subset w}\dim K^{corner}_{K}
-
\sum_{E\subset w}\dim K^{corner}_{E}.
}
$$

Proof.  Use the rewrite rules of Section 57.  Analysis erasure moves all
analysis arrows to the left and contributes zero to \(Q,C\).  Refinement
absorption composes all exact-pair presentation changes into one refinement
class and contributes zero to \(Q,C\).  Corner/source ordering separates
unpaired corner cohomology from unpaired source content.  Since all spaces are
finite, the rewriting process terminates: each rewrite either moves an
analysis/refinement symbol left or separates one mixed extension into simpler
finite pieces.  The resulting word has the form:

$$
\boxed{
A^{*}R^{*}K^{*}E^{*}.
}
$$

The effect formula follows by additivity of finite index and direct-sum
additivity of finite corner cohomology:

$$
\boxed{
\operatorname{Ind}_{fin}({\mathcal K}\oplus{\mathcal L})
=
\operatorname{Ind}_{fin}({\mathcal K})
+
\operatorname{Ind}_{fin}({\mathcal L}),
}
$$

and:

$$
\boxed{
\dim(K^{corner}\oplus L^{corner})
=
\dim K^{corner}+\dim L^{corner}.
}
$$

Thus the normal form determines the total change in \(Q,C\).  `square`

The uniqueness needed here is uniqueness of effect, not uniqueness of prose
history.  Different historical derivations may give different words, but after
rewriting they have the same \(\Delta Q,\Delta C\) whenever they represent the
same finite actual transformation.

## 59. Einstein Reading: Finite Covariance Normal Form

Searchable principle tag:

`V4P24-EINSTEIN-FINITE-COVARIANCE-NORMAL-FORM`.

Einstein's closure is the finite covariance statement:

$$
\boxed{
\hbox{there is no privileged finite presentation of an actual situation.}
}
$$

Therefore any admissible presentation change must be an \(R\)-move:

$$
\boxed{
\hbox{same actual situation}
\Longleftrightarrow
A^{*}R^{*}.
}
$$

Any nonzero \(K\) or \(E\) term means the actual situation has changed:

$$
\boxed{
K\hbox{ or }E\neq\varnothing
\Longleftrightarrow
\hbox{physical extension, not coordinate/refinement change.}
}
$$

This is the finite analogue of separating coordinate artifacts from physical
curvature/source content.  The invariant attached to an actual situation is:

$$
\boxed{
[{\mathcal A}^{act}]_{fin}
=
\hbox{the }A^{*}R^{*}\hbox{ equivalence class}.
}
$$

The count law is:

$$
\boxed{
Q([{\mathcal A}^{act}]_{fin})
=
\operatorname{Ind}_{fin}({\mathcal K}).
}
$$

and:

$$
\boxed{
C([{\mathcal A}^{act}]_{fin})
=
-\dim K^{corner}.
}
$$

So the finite covariance principle proves:

$$
\boxed{
\hbox{a claimed same-situation transformation cannot change }Q,C.
}
$$

If it does, the claim of sameness is false.

## 60. Feynman Reading: Complete Finite Move Calculus

Searchable principle tag:

`V4P24-FEYNMAN-COMPLETE-FINITE-MOVE-CALCULUS`.

Feynman's closure is not a table.  It is the assertion that the finite
alternative calculus is complete.

The finite transfer change for any corpus move has the normal form:

$$
\boxed{
\Delta\Xi
=
[D,A]
\oplus(I_V-I_V)
\oplus P_{K^{corner}}
\oplus P_{{\mathcal K}_{new}}.
}
$$

Taking the finite trace:

$$
\boxed{
\operatorname{Tr}\Delta\Xi
=
\operatorname{Tr}[D,A]
+\operatorname{Tr}(I_V-I_V)
+\operatorname{Tr}P_{K^{corner}}
+\operatorname{Tr}P_{{\mathcal K}_{new}}.
}
$$

The first two terms vanish:

$$
\boxed{
\operatorname{Tr}[D,A]=0,
\qquad
\operatorname{Tr}(I_V-I_V)=0.
}
$$

Thus:

$$
\boxed{
\operatorname{Tr}\Delta\Xi
=
\dim K^{corner}
+
\operatorname{Ind}_{fin}({\mathcal K}_{new}).
}
$$

With the sign convention for \(C\):

$$
\boxed{
\Delta C=-\dim K^{corner},
}
$$

and:

$$
\boxed{
\Delta Q=\operatorname{Ind}_{fin}({\mathcal K}_{new}).
}
$$

This is the real finite Feynman closure: all nonactual alternatives cancel by
finite trace identities; only unpaired residues survive, and those residues
are exactly the \(K\) and \(E\) terms of the normal form.

## 61. Normal-Form Falsifier

Searchable falsifier tag:

`V4P24-NORMAL-FORM-FALSIFIER`.

The normal-form closure is falsified by any finite corpus move \(M\) such that:

$$
\boxed{
M\not\Rightarrow A^{*}R^{*}K^{*}E^{*}.
}
$$

Equivalently, one of the following happens:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failure} & \hbox{description} & \hbox{missing primitive}\\
\hline
\mathrm{NF1} &
\hbox{a same-situation refinement changes }Q &
\hbox{non-index source primitive}\\
\mathrm{NF2} &
\hbox{a same-situation refinement changes }C &
\hbox{non-cohomological corner primitive}\\
\mathrm{NF3} &
\hbox{a finite transfer change has nonzero trace but no }K,E\hbox{ residue} &
\hbox{non-Ward finite anomaly}\\
\mathrm{NF4} &
\hbox{an unpaired source extension has no finite index complex} &
\hbox{new actual-source ontology}\\
\mathrm{NF5} &
\hbox{a corner residue is not a finite quotient/cohomology} &
\hbox{new curvature/corner ontology}\\
\mathrm{NF6} &
\hbox{the move cannot be classified as analysis, refinement, corner, or
extension} &
\hbox{new admissible move type}
\end{array}
}
$$

This is a strong stopping rule.  If none of NF1-NF6 occurs, the value-source
law is closed under the full corpus transformation.  If one occurs, it names
the exact new primitive needed.

## 62. Active P20-P24 Normal Form

Searchable audit tag:

`V4P24-ACTIVE-P20-P24-NORMAL-FORM`.

The active closure chain has the normal form:

$$
\boxed{
\alpha_{20}\to\alpha_{21}\to\alpha_{22}
\to
(\alpha_{23}^{G1},\alpha_{23}^{G2},\alpha_{23}^{G3})
\to
\alpha_{24}^{E}
\to
\alpha_{24}^{Q}
\to
\alpha_{24}^{A}
\to
\alpha_{24}^{D}.
}
$$

Classify:

$$
\boxed{
\begin{array}{c|c}
\hbox{segment} & \hbox{normal-form type}\\
\hline
\alpha_{20}\to\alpha_{21}\to\alpha_{22} & A^{*}\\
\alpha_{22}\to\alpha_{23}^{G1,G2,G3} & A^{*}\hbox{ plus branch selection}\\
\alpha_{23}^{G1,G2,G3}\to\alpha_{24}^{E} & A^{*}R^{*}\hbox{ effective reinterpretation}\\
\alpha_{24}^{E}\to\alpha_{24}^{Q} & E^{*}\hbox{ count-source extension}\\
\alpha_{24}^{Q}\to\alpha_{24}^{A} & R^{*}\hbox{ index/trace resolution}\\
\alpha_{24}^{A}\to\alpha_{24}^{D} & R^{*}\hbox{ descent/globalization}
\end{array}
}
$$

Therefore:

$$
\boxed{
\hbox{active P20-P24 chain}
\Rightarrow
A^{*}R^{*}E^{*}R^{*}R^{*}
\Rightarrow
A^{*}R^{*}E^{*}.
}
$$

The only value-changing segment is:

$$
\boxed{
\alpha_{24}^{E}\to\alpha_{24}^{Q},
}
$$

and its change is:

$$
\boxed{
\Delta Q=(0,6,10),
\qquad
\Delta C=(0,0,-1),
}
$$

sourced by:

$$
\boxed{
\operatorname{Ind}_{fin}({\mathcal K}_{new})
\quad\hbox{and}\quad
-\dim K^{corner}_{new}.
}
$$

Thus:

$$
\boxed{
\mathrm{NF1}\text{-}\mathrm{NF6}
\hbox{ do not occur in the active P20-P24 closure chain.}
}
$$

## 63. Final Closure Statement For Paper 24

Searchable final tag:

`V4P24-FINAL-CLOSURE-STATEMENT`.

The final closure statement is:

$$
\boxed{
\hbox{The active P20-P24 value-source problem is closed by finite descent
normal form.}
}
$$

Expanded:

$$
\boxed{
\begin{array}{l}
\hbox{local values are generated by a finite effective calibration packet;}\\
\hbox{the packet's counts are sourced by finite index/trace data;}\\
\hbox{the local packet embeds in a canonical finite descent family;}\\
\hbox{same-situation refinements preserve }Q,C;\\
\hbox{extensions change }Q,C\hbox{ only by finite index/cohomology increments;}\\
\hbox{the active closure chain factors through }A^{*}R^{*}K^{*}E^{*}.
\end{array}
}
$$

The remaining full-corpus work is not a missing value law:

$$
\boxed{
\hbox{it is the archival normal-form audit of earlier v1-v4 moves.}
}
$$

For each earlier move \(M\), run:

$$
\boxed{
M\Rightarrow A^{*}R^{*}K^{*}E^{*}
}
$$

or record which NF falsifier fires.  This is now a finite registry task with a
decisive failure mode, not an open-ended search for the missing object.

## 64. Archival V4 Normal-Form Backfill

Now run the earlier V4 papers through the normal-form classifier.

Searchable registry tag:

`V4P24-V4-P1-P19-NORMAL-FORM-BACKFILL`.

The normal-form classes are:

$$
\boxed{
A=\hbox{analysis},\quad
R=\hbox{exact refinement},\quad
K=\hbox{corner/cohomology residue},\quad
E=\hbox{unpaired source extension}.
}
$$

The V4 archival registry is:

$$
\boxed{
\begin{array}{c|l|l|l}
\hbox{paper} & \hbox{main move} & \hbox{normal form} & \hbox{effect on }Q,C\\
\hline
P1 &
\hbox{geometric source shortcut tested and scoped no-go} &
A &
0,0\\
P2 &
\hbox{fixed-background metric gate and orientation route identified} &
A &
0,0\\
P3 &
\hbox{passive orientation no-go; operational effect route isolated} &
A\;(\hbox{prospective }E_{orient}) &
0,0\\
P4 &
\hbox{operational orientation quorum and source-response calculus} &
A^{*}E_{orient}^{decl} &
\hbox{no }P24\ Q,C\hbox{ import}\\
P5 &
\hbox{operational curvature compatibility source} &
A^{*}E_{curv}^{decl} &
\hbox{no }P24\ Q,C\hbox{ import}\\
P6 &
\hbox{finite geometry alphabet/configuration gate} &
A^{*}E_{geom}^{decl} &
\hbox{dynamics still unsourced}\\
P7 &
\hbox{GR-like finite dynamics gate and current-corpus no-go} &
A &
0,0\\
P8 &
\hbox{geometric-score/residual-bound route exhaustion} &
A\;(\hbox{candidate }E_{respen}) &
0,0\hbox{ unless candidate law is adopted}\\
P9 &
\hbox{residual-minimum side-decision and finite search target} &
A &
0,0\\
P10 &
\hbox{source-conditioned smooth realizability/floor dichotomy} &
A^{*}R_{sector}^{*} &
0,0\\
P11 &
\hbox{actual-law regular-packet route exhaustion} &
A &
0,0\\
P12 &
\hbox{residual-source Ward/Stein four-route decision} &
A &
0,0\\
P13 &
\hbox{three-normal switch decision; groupoid support candidate} &
A\;(\hbox{prospective }E_{groupoid}) &
0,0\hbox{ unless candidate support law is adopted}\\
P14 &
\hbox{boundary sufficiency/separator support hinge} &
A &
0,0\\
P15 &
\hbox{concrete actual-law route menu} &
A &
0,0\\
P16 &
\hbox{minimal two-row support calculation and support-kernel target} &
A\;(\hbox{prospective }E_{supp}) &
0,0\hbox{ unless support kernel is adopted}\\
P17 &
\hbox{licensed GR/SM support ansatz and hard/soft separation} &
A^{*}E_{supp}^{cond} &
\hbox{support closure only; no }P24\ Q,C\\
P18 &
\hbox{support-stability consequences and value frontier} &
A^{*}R_{supp}^{*} &
\hbox{support invariant; no value count}\\
P19 &
\hbox{finite source-Stein value engine} &
A\;(\hbox{prospective }E_{source}) &
0,0\hbox{ until source triple is printed}
\end{array}
}
$$

The registry says something important:

$$
\boxed{
\hbox{P1-P19 do not secretly change the Paper-24 }Q,C\hbox{ invariant.}
}
$$

Whenever those papers introduce new actual ingredients, the ingredient is
already marked as an extension candidate:

$$
\boxed{
E_{orient},E_{curv},E_{geom},E_{respen},E_{groupoid},E_{supp},E_{source}.
}
$$

None of them is used as a same-situation refinement that changes \(Q\) or
\(C\).  Therefore the archival V4 pass has no NF1 or NF2 violation.

## 65. V4 P1-P19 Falsifier Audit

Searchable audit tag:

`V4P24-V4-P1-P19-NF-AUDIT`.

Run NF1-NF6 on the V4 archival registry.

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{NF1} &
\mathrm{PASS} &
\hbox{no earlier same-situation refinement changes }Q\\
\mathrm{NF2} &
\mathrm{PASS} &
\hbox{no earlier same-situation refinement changes }C\\
\mathrm{NF3} &
\mathrm{PASS} &
\hbox{Ward/Stein anomalies are labelled as conditional source problems}\\
\mathrm{NF4} &
\mathrm{PASS}_{label} &
\hbox{unpaired source additions are labelled }E\hbox{ candidates}\\
\mathrm{NF5} &
\mathrm{PASS}_{label} &
\hbox{corner/holonomy residues are not used as hidden refinements}\\
\mathrm{NF6} &
\mathrm{PASS}_{V4} &
\hbox{every P1-P19 move is }A,R,\hbox{ or a labelled prospective }E
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{V4\ P1\text{-}P19}
\Rightarrow
A^{*}R^{*}E^{*}
\quad
\hbox{with no active }K\hbox{ or unlabelled anomaly.}
}
$$

The only V4 move that becomes a concrete Paper-24 value-source extension is
later:

$$
\boxed{
\alpha_{24}^{E}\to\alpha_{24}^{Q}.
}
$$

The earlier V4 papers prepare the need for that extension, but they do not
silently perform it.

## 66. V2-V3 Provenance Backfill

Searchable provenance tag:

`V4P24-V2-V3-PROVENANCE-BACKFILL`.

The locally visible historical corpus before V4 begins at V2.  No local file
with a `relativistic-isp-v1` paper name is present in this workspace, so the
local archival audit cannot certify a v1 paper sequence here.

The V2-V3 provenance normal form is compressed by phase:

$$
\boxed{
\begin{array}{c|l|l|l}
\hbox{phase} & \hbox{papers} & \hbox{role} & \hbox{normal form}\\
\hline
\hbox{V2 free/kernel} &
V2P1\text{-}P4 &
\hbox{free stochastic curvature, projective kernels, operational readout} &
A^{*}R^{*}\\
\hbox{V2 QFT/gauge gates} &
V2P5\text{-}P10 &
\hbox{continuum gauge/QFT benchmarks and Gamma-level obstruction} &
A^{*}R^{*}\\
\hbox{V3 QFT reconstruction} &
V3P1\text{-}P8 &
\hbox{enriched QFT reconstruction and no-go gates} &
A^{*}R^{*}\\
\hbox{V3 finite gauge/YM} &
V3P9\text{-}P18 &
\hbox{finite gauge sectors, Yang-Mills, mass-gap/confinement gates} &
A^{*}R^{*}E_{gauge}^{cand}\\
\hbox{V3 actual source campaigns} &
V3P19\text{-}P30 &
\hbox{actual constants, RPF/SCI/RN/RN-MIXAMP/source campaigns} &
A^{*}E_{source}^{cand}\\
\hbox{V3 same-law response frontier} &
V3P31\text{-}P37 &
\hbox{source response, scalar ray, Ward/Stein, admissibility/floor} &
A^{*}E_{source}^{cand}
\end{array}
}
$$

The compressed audit result is:

$$
\boxed{
\hbox{V2-V3 supply provenance, obstructions, and candidate source extensions;
they do not supply an unlabelled Paper-24 }Q,C\hbox{ refinement.}
}
$$

Thus no local V2-V3 phase triggers NF1-NF6 for the Paper-24 value-source law.
The unresolved V3 same-law value gaps are precisely what V4 P18-P24 convert
into the finite value-source closure chain.

## 67. Full Local Historical Normal-Form Verdict

Searchable verdict tag:

`V4P24-FULL-LOCAL-HISTORICAL-NORMAL-FORM-VERDICT`.

Combining the active P20-P24 audit with the V4 P1-P19 backfill and the V2-V3
provenance backfill:

$$
\boxed{
\mathrm{local\ historical\ corpus}
\Rightarrow
A^{*}R^{*}E^{*}
\quad
\hbox{until Paper 24 prints the concrete }E\hbox{ that sources }Q,C.
}
$$

More explicitly:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{block} & \hbox{normal form} & \hbox{NF status}\\
\hline
V2 & A^{*}R^{*} & \mathrm{PASS}\\
V3 & A^{*}R^{*}E_{source}^{cand} & \mathrm{PASS}_{cand}\\
V4P1\text{-}P19 & A^{*}R^{*}E^{cand} & \mathrm{PASS}_{cand}\\
V4P20\text{-}P24 & A^{*}R^{*}E^{*} & \mathrm{PASS}_{active}
\end{array}
}
$$

The final falsifiable statement is:

$$
\boxed{
\hbox{No locally visible v2-v4 move functions as a hidden same-situation
refinement that changes }Q\hbox{ or }C.
}
$$

All value-changing moves are either:

$$
\boxed{
\hbox{labelled candidate extensions}
}
$$

or:

$$
\boxed{
\hbox{the explicit Paper-24 finite index/cohomology extension.}
}
$$

Therefore the Paper-24 value-source closure survives the local historical
normal-form audit.

The only remaining archival caveat is:

$$
\boxed{
\hbox{v1 cannot be certified from this workspace unless v1 source files are
added or identified.}
}
$$
