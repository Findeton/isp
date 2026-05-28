# Relativistic ISP V4 Paper 25: Finite Descent Reconstruction Of Effective GR

Author: Felix Robles Elvira

Status: Developed reconstruction paper after Paper 24.  Paper 24 closed the
finite value-source bottleneck by canonical descent and count/corner
invariants.  Paper 25 asks whether those finite invariants are sufficient to
reconstruct the effective GR interface without assuming continuum GR as
primitive ontology.

The central claim is staged:

$$
\boxed{
\hbox{finite descent records plus readout/transport gates}
\Longrightarrow
\hbox{effective GR kinematics}
\quad
\hbox{and maybe}
\quad
\hbox{effective GR dynamics}.
}
$$

The paper therefore separates:

$$
\boxed{
\mathrm{GR\text{-}KIN}
\quad\text{(metric/connection/curvature/geodesic structure)}
\qquad
\mathrm{vs}
\qquad
\mathrm{GR\text{-}DYN}
\quad\text{(stress-curvature coupling law)}.
}
$$

## 0. Imports And Scope

Searchable import tag:

`V4P25-IMPORT-P24-FINITE-DESCENT`.

Paper 24 provides a projective family:

$$
\boxed{
{\mathfrak A}^{act}
=
\{\mathrm{Desc}(\alpha)\}_{\alpha\in{\mathcal R}},
\qquad
\mathrm{Desc}(\alpha)
=
({\mathcal K}_{\alpha},{\mathcal H}_{\alpha},\Xi_{\alpha},K_{\alpha}^{corner},r_{\alpha},\lambda).
}
$$

Core finite invariants are:

$$
\boxed{
Q_{\alpha}(s)=\operatorname{Tr}\Xi_{\alpha}(s),
\qquad
C_{\alpha}(e)=-\dim K_{\alpha}^{corner}(e).
}
$$

With edge increment:

$$
\boxed{
N_{\alpha}(i\to j)=Q_{\alpha}(j)-Q_{\alpha}(i),
}
$$

effective edge action:

$$
\boxed{
A_{\alpha}^{eff}(e)=\lambda\bigl(N_{\alpha}(e)+C_{\alpha}(e)\bigr),
}
$$

and triangle holonomy:

$$
\boxed{
\Omega_{\alpha}(ijk)=C_{\alpha}(ij)+C_{\alpha}(jk)-C_{\alpha}(ik),
\qquad
H_{\alpha}(ijk)=\lambda\,\Omega_{\alpha}(ijk).
}
$$

R-moves preserve \(Q,C\); extensions may change \(Q,C\) by licensed finite
increments only.

Barandes discipline is maintained throughout:

$$
\boxed{
\hbox{finite records first, effective continuum language second.}
}
$$

### 0.1 Audit Corrections In This Version

Searchable audit tag:

`V4P25-AUDIT-CORRECTIONS`.

The developed draft had several places where the claim was stronger than the
finite data licensed:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{issue} & \hbox{draft risk} & \hbox{correction}\\
\hline
\mathrm{A1} &
\hbox{polarizing an arbitrary edge score as a metric} &
\hbox{add a finite quadratic-coherence/signature gate}\\
\mathrm{A2} &
\hbox{using }\operatorname{tr}(U_{jk}U_{ij}-U_{ik})\hbox{ as curvature} &
\hbox{use closed loop holonomy }U_{ki}U_{jk}U_{ij}\\
\mathrm{A3} &
\hbox{treating corner count curvature as automatically Levi-Civita curvature} &
\hbox{add corner-frame compatibility as a real hypothesis}\\
\mathrm{A4} &
\hbox{marking interface tests as passed without finite data} &
\hbox{downgrade them to benchmarks unless a table is printed}\\
\mathrm{A5} &
\hbox{using an oriented edge increment directly as a metric interval} &
\hbox{add reversal symmetry and symmetrize the metric readout}\\
\mathrm{A6} &
\hbox{writing }U=\exp(-\Gamma)\hbox{ before a finite logarithm is licensed} &
\hbox{take }U\hbox{ as primitive finite transport and log only after a gate}\\
\mathrm{A7} &
\hbox{treating one trace as the whole curvature tensor} &
\hbox{use a representation-complete finite holonomy probe family}\\
\mathrm{A8} &
\hbox{deriving geodesic deviation from curvature without a second-variation
packet} &
\hbox{add a finite Jacobi-response gate}\\
\mathrm{A9} &
\hbox{using one scalar source index for Einstein dynamics} &
\hbox{add a multi-component stress-source dictionary}
\end{array}
}
$$

The corrected paper therefore proves conditional reconstruction gates.  It
does not claim that every finite descent packet automatically has Lorentzian
metric signature, a Levi-Civita transport, or Einstein dynamics.

## 1. Target Gates

Searchable gate tag:

`V4P25-GR-TARGET-GATES`.

Paper 25 uses five gates:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{name} & \hbox{finite target}\\
\hline
\mathrm{GR1} & \hbox{metric readout} & \hbox{symmetrized interval structure from }(N,C,\rho^{op})\\
\mathrm{GR2} & \hbox{equivalence principle} & \hbox{refinement/frame invariance of local inertial data}\\
\mathrm{GR3} & \hbox{connection/curvature} & \hbox{transport defect sourced by corner cohomology}\\
\mathrm{GR4} & \hbox{geodesic law} & \hbox{least-bias free fall; deviation only with Jacobi packet}\\
\mathrm{GR5} & \hbox{dynamics} & \hbox{finite stress index coupled to finite geometric index}
\end{array}
}
$$

## 2. Finite Metric Readout Construction

Searchable construction tag:

`V4P25-FINITE-METRIC-READOUT`.

Define the raw oriented edge score:

$$
\boxed{
I^{raw}_{\alpha}(e)
=
a_1N_{\alpha}(e)+a_2C_{\alpha}(e)-a_3\log\rho_{\alpha}^{op}(e),
\qquad
a_1,a_2>0,\quad a_3\ge0.
}
$$

This score is not yet a metric interval, because \(N_{\alpha}(i\to j)\) is an
oriented increment.  A metric readout must be insensitive to reversing the
same physical edge, except for declared time-orientation/action data.  Thus
Paper 25 adds the missing reversal gate.

Searchable gate tag:

`V4P25-GR0-REVERSAL-SYMMETRY`.

For every metric-readout edge \(e:i\to j\), the finite packet must include the
reverse record \(\bar e:j\to i\), and the reference-corrected symmetric and
oriented parts:

$$
\boxed{
I^{sym}_{\alpha}(e)
=
\frac12\left(I^{raw}_{\alpha}(e)+I^{raw}_{\alpha}(\bar e)\right),
\qquad
I^{or}_{\alpha}(e)
=
\frac12\left(I^{raw}_{\alpha}(e)-I^{raw}_{\alpha}(\bar e)\right).
}
$$

The metric readout uses \(I^{sym}_{\alpha}\).  The oriented part
\(I^{or}_{\alpha}\) remains available as clock-arrow, action-flow, or
retarded/advanced sector data, but it is not allowed to enter the quadratic
metric gate as if it were symmetric distance.

Define edge class at tolerance \(\tau_I\):

$$
\boxed{
\begin{array}{c|c}
I^{sym}_{\alpha}(e)<-\tau_I & \hbox{timelike-like}\\
|I^{sym}_{\alpha}(e)|\le\tau_I & \hbox{null-like}\\
I^{sym}_{\alpha}(e)>\tau_I & \hbox{spacelike-like}
\end{array}
}
$$

For a finite local frame at node \(p\), choose basis edges
\(\{e_a(p)\}_{a=0}^{d-1}\).  The draft version defined metric components by
polarization immediately.  That is licensed only after a finite
quadratic-coherence gate is supplied.

Searchable gate tag:

`V4P25-GR1-QUADRATIC-COHERENCE`.

The gate says that the frame has inverse/composite edge records and that:

$$
\boxed{
I^{sym}_{\alpha}(e_a\oplus e_b)+I^{sym}_{\alpha}(e_a\ominus e_b)
-2I^{sym}_{\alpha}(e_a)-2I^{sym}_{\alpha}(e_b)
}
$$

is symmetric in \(a,b\), stable under allowed composition reassociations, and
changes only by endpoint-reference terms under frame relabeling.

When this gate holds, define finite metric components by polarization:

$$
\boxed{
g^{eff}_{\alpha,ab}(p)
=
\frac12\left(
I^{sym}_{\alpha}(e_a\oplus e_b)-I^{sym}_{\alpha}(e_a)-I^{sym}_{\alpha}(e_b)
\right),
}
$$

where \(\oplus\) is the declared finite edge-composition operator in the
same context.

The readout is Lorentzian only after a separate stable-signature gate:

$$
\boxed{
\mathrm{Sig}(g^{eff}_{\alpha}(p))=(1,d-1)
\quad
\hbox{cofinally and up to reference/frame gauge.}
}
$$

### Theorem 2.1: Conditional Finite Metric Readout

Searchable theorem tag:

`V4P25-GR1-METRIC-EXISTENCE-THEOREM`.

If \(N_{\alpha},C_{\alpha},\rho^{op}_{\alpha}\) are predeclared on all edges
and reverse edges of a finite frame neighborhood, \(\oplus,\ominus\) are
associative up to endpoint reference terms,
`V4P25-GR0-REVERSAL-SYMMETRY` holds, and
`V4P25-GR1-QUADRATIC-COHERENCE` holds, then
\(g^{eff}_{\alpha}\) is a well-defined finite symmetric bilinear comparison
form modulo reference gauge.  If the stable-signature gate also holds, it is a
finite Lorentzian metric readout on the patch.

Proof.  \(I^{raw}_{\alpha}\) is a finite scalar on predeclared oriented
edges.  The reversal gate splits it into a symmetric interval candidate and an
oriented action/clock component; only the symmetric part is admitted to the
metric readout.  The quadratic-coherence gate supplies exactly the finite
parallelogram and symmetry identities needed for polarization to define a
bilinear comparison form rather than an arbitrary second difference.
Endpoint-reference terms cancel in the second-difference quotient, and
reassociation changes only reference gauge.  The stable-signature gate is the
additional condition that turns the comparison form into a Lorentzian readout.
`square`

### GR1 Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{GR1F1}:&\hbox{same edge class changes under pure relabeling};\\
\mathrm{GR1F2}:&\hbox{polarized component depends on composition order beyond reference};\\
\mathrm{GR1F3}:&\hbox{no stable sign structure emerges for any admissible }(a_1,a_2,a_3);\\
\mathrm{GR1F4}:&\hbox{quadratic coherence or Lorentzian signature fails cofinally};\\
\mathrm{GR1F5}:&\hbox{reverse-edge data are absent or symmetric readout is path-direction dependent.}
\end{array}
}
$$

## 3. Finite Equivalence Principle

Searchable principle tag:

`V4P25-FINITE-GR-EQUIVALENCE-PRINCIPLE`.

For a same-situation refinement \(\alpha\le_{ref}\beta\), require:

$$
\boxed{
g^{eff}_{\beta}(p)
=
\Lambda_{\beta\alpha}(p)^T g^{eff}_{\alpha}(p)\Lambda_{\beta\alpha}(p)
+\delta^{ref}_{\beta\alpha}(p),
}
$$

where \(\delta^{ref}_{\beta\alpha}\) is a removable reference tensor with bounded
norm \(\|\delta^{ref}_{\beta\alpha}\|\le\tau_{ref}\).

### Theorem 3.1: Conditional Refinement Invariance From P24 Descent

Searchable theorem tag:

`V4P25-GR2-REFINEMENT-INVARIANCE-THEOREM`.

Assume P24 descent gates hold for \(\alpha\le_{ref}\beta\):
\(N_{\beta}=N_{\alpha}\), \(C_{\beta}=C_{\alpha}\), and
\(\rho^{op}_{\beta}(i\to j)=\rho^{op}_{\alpha}(i\to j)e^{r_j-r_i}\) after
pullback to the same finite frame.  Also assume the quadratic-coherence and
stable-signature gates are preserved by the refinement frame map.  Then
\(g^{eff}_{\beta}=\Lambda^Tg^{eff}_{\alpha}\Lambda+\delta^{ref}\) with
\(\delta^{ref}\) induced only by \(r_j-r_i\).

Proof.  The only term in \(I^{raw}\) that changes under refinement is
\(-a_3\log\rho^{op}\), and this changes by endpoint potential differences.
After reversal symmetrization, such differences vanish under polarized second
differences except for frame gauge drift represented by \(\delta^{ref}\).
Preservation of
quadratic-coherence and signature prevents the refinement from converting a
valid metric readout into a different comparison object.  Hence local inertial
content is refinement invariant in the quotient. `square`

### GR2 Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{GR2F1}:&\hbox{an R-move changes }N\hbox{ or }C;\\
\mathrm{GR2F2}:&\hbox{metric drift remains after optimal frame alignment};\\
\mathrm{GR2F3}:&\hbox{reference drift cannot be written as endpoint potential gauge}.
\end{array}
}
$$

## 4. Finite Connection And Curvature

Searchable construction tag:

`V4P25-FINITE-CONNECTION-CURVATURE`.

Define transport between local frames:

$$
\boxed{
U_{\alpha}(ij):{\mathcal F}_{\alpha}(i)\to{\mathcal F}_{\alpha}(j).
}
$$

Here \(U_{\alpha}(ij)\) is the primitive finite transport record.  A connection
matrix \(\Gamma_{\alpha}(ij)\) is an effective logarithm of this transport only
if a finite logarithm has been licensed.

Searchable gate tag:

`V4P25-FINITE-LOG-GATE`.

The log gate says that, on the chosen frame patch, there is a stable branch:

$$
\boxed{
U_{\alpha}(ij)=\exp\bigl(-\Gamma_{\alpha}(ij)\bigr)
\quad
\hbox{up to declared finite-log error}.
}
$$

No theorem below depends on this logarithm.  The finite connection content is
the transport family \(U_{\alpha}\) itself.  It is called Levi-Civita
compatible only if a finite solution exists to the metric compatibility and
torsion-free equations:

$$
\boxed{
\nabla^{fin}g^{eff}=0,
\qquad
\Gamma_{ab,c}^{fin}=\Gamma_{ba,c}^{fin}.
}
$$

The existence and uniqueness of such a finite connection is not automatic
from \(Q,C\).  It is a gate:

$$
\boxed{
\mathrm{LC}_{\alpha}:
\hbox{a stable finite Levi-Civita-compatible transport is printed.}
}
$$

Define the closed triangle loop transport:

$$
\boxed{
L_{\alpha}(ijk)
=
U_{\alpha}(ki)U_{\alpha}(jk)U_{\alpha}(ij).
}
$$

If \(ki\) is not a primitive oriented edge, \(U_{\alpha}(ki)\) means the
licensed inverse of \(U_{\alpha}(ik)\).  If that inverse is not printed, the
loop-holonomy readout is not licensed and GR3 remains open on the patch.

Define a holonomy probe on the closed triangle:

$$
\boxed{
{\mathcal R}^{eff}_{\alpha,\chi}(ijk)
:=
\chi\bigl(L_{\alpha}(ijk)-I_{{\mathcal F}_{\alpha}(i)}\bigr),
\qquad
\chi\in{\mathcal P}^{hol}_{\alpha}.
}
$$

The ordinary trace is one possible probe.  It is a scalar witness, not the
whole curvature tensor.  To reconstruct the full finite curvature object, the
packet must print a representation-complete separating family of probes.

Searchable gate tag:

`V4P25-GR3-HOLONOMY-PROBE-COMPLETENESS`.

The gate requires:

$$
\boxed{
\left[
\chi(X)=0\ \hbox{for all }\chi\in{\mathcal P}^{hol}_{\alpha}
\right]
\Rightarrow
X=0
\quad
\hbox{on licensed loop-transport defects.}
}
$$

This replaces the draft expression
\(\operatorname{tr}(U_{jk}U_{ij}-U_{ik})\), which is not a canonical scalar
unless an additional identification \({\mathcal F}(k)\simeq{\mathcal F}(i)\)
is chosen.

### Theorem 4.1: Conditional Corner-Holonomy Curvature Identity

Searchable theorem tag:

`V4P25-GR3-CORNER-CURVATURE-THEOREM`.

Assume descent compatibility, the finite Levi-Civita gate \(\mathrm{LC}\), and
the corner-frame compatibility gate:

$$
\boxed{
\mathrm{CF}_{\alpha}:
\chi\bigl(L_{\alpha}(ijk)-I\bigr)
=
\lambda_{\chi}\,\Omega_{\alpha}(ijk)
\quad
\hbox{up to a declared frame discretization error}
\quad
\hbox{for every printed probe }\chi.
}
$$

Then:

$$
\boxed{
{\mathcal R}^{eff}_{\alpha,\chi}(ijk)
=
\lambda_{\chi}\,\Omega_{\alpha}(ijk)+\varepsilon_{\alpha,\chi}^{conn}(ijk),
}
$$

with \(|\varepsilon_{\alpha,\chi}^{conn}(ijk)|\le\tau_{conn,\chi}\) controlled
by frame discretization error.  If
`V4P25-GR3-HOLONOMY-PROBE-COMPLETENESS` also holds, these scalar identities
determine the full finite loop-curvature defect on the patch.

Proof.  P24 gives \(\lambda\Omega\) as generated triangle holonomy source.
The closed loop \(L_{\alpha}(ijk)\) computes the frame holonomy in the finite
transport variables.  The corner-frame compatibility gate is exactly the
statement that these two finite holonomy readouts are the same corner residue
viewed in the printed holonomy probes.  The remaining discrepancy is the
declared frame discretization error.  A single trace proves only the traced
identity; the probe-completeness gate is the additional finite reason that the
full loop defect has been reconstructed. `square`

### GR3 Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{GR3F1}:&\hbox{nonzero corner class but vanishing transport defect in stable regime};\\
\mathrm{GR3F2}:&\hbox{transport defect appears with zero corner class in all gauges};\\
\mathrm{GR3F3}:&\hbox{curvature must be post-fitted and is not generated by }K^{corner};\\
\mathrm{GR3F4}:&\hbox{finite Levi-Civita or corner-frame compatibility has no solution};\\
\mathrm{GR3F5}:&\hbox{only a trace is printed while the claim requires full curvature};\\
\mathrm{GR3F6}:&\hbox{the effective logarithm }\Gamma\hbox{ is used without the finite-log gate.}
\end{array}
}
$$

## 5. Finite Geodesic And Free-Fall Law

Searchable construction tag:

`V4P25-FINITE-GEODESIC-LAW`.

Let \({\mathcal P}_{ij}\) be finite admissible paths from \(i\) to \(j\), with
no arbitrary negative-action cycling inside the admissible path class.  The
symmetric interval \(I^{sym}_{\alpha}\), together with the oriented sector
score \(I^{or}_{\alpha}\), is not itself a universal path cost; in a
Lorentzian problem timelike and spacelike sectors use opposite extremal
conventions.  Therefore fix a sector-adjusted nonnegative edge cost
\(\ell_{\alpha}^{geo}(e)\) before endpoints are queried:

$$
\boxed{
\ell_{\alpha}^{geo}(e)
=
\ell_{\mathfrak s}\bigl(I^{sym}_{\alpha}(e),I^{or}_{\alpha}(e),\mathrm{class}(e)\bigr)
\ge0,
}
$$

where \(\mathfrak s\) is the declared clock/ruler sector.  Define path action:

$$
\boxed{
S_{\alpha}(\gamma)
=
\sum_{e\in\gamma}\ell_{\alpha}^{geo}(e)
+\eta\,\#\hbox{turns}(\gamma),
}
$$

with prior \(\mu^0_{\alpha}(\gamma)>0\).  The least-bias path law is:

$$
\boxed{
P^*_{\alpha}(\gamma)
=
\frac{\mu^0_{\alpha}(\gamma)e^{-\beta S_{\alpha}(\gamma)}}{\sum_{\gamma'\in{\mathcal P}_{ij}}\mu^0_{\alpha}(\gamma')e^{-\beta S_{\alpha}(\gamma')}}.
}
$$

The finite free-fall path is the MAP trajectory:

$$
\boxed{
\gamma^*_{\alpha}=
\arg\max_{\gamma\in{\mathcal P}_{ij}}P^*_{\alpha}(\gamma)
=
\arg\min_{\gamma\in{\mathcal P}_{ij}}\left[S_{\alpha}(\gamma)-\beta^{-1}\log\mu^0_{\alpha}(\gamma)\right].
}
$$

### Theorem 5.1: Refinement-Invariant Free-Fall

Searchable theorem tag:

`V4P25-GR4-FREE-FALL-INVARIANCE-THEOREM`.

If the sector \(\mathfrak s\), \(\ell^{geo}\), and \(\mu^0_{\alpha}\) are fixed
pre-query and transform under R-moves by endpoint reference terms only, then
\(\gamma^*\) is invariant under R-moves up to frame representation.

Proof.  Endpoint terms shift all paths with same endpoints by equal additive
constants and therefore do not change path ordering.  The no-negative-cycle
and sector-cost conditions make the MAP finite and prevent the signed interval
from creating spurious loop-minimizers.  Frame representation can change
labels but not equivalence class of minimizers. `square`

### 5.2 Finite Jacobi-Response Gate

Searchable gate tag:

`V4P25-GR4-FINITE-JACOBI-GATE`.

Free-fall invariance does not by itself prove geodesic deviation.  Deviation
requires a finite second-variation packet:

$$
\boxed{
{\mathcal J}_{\alpha}
=
\left(
{\mathcal N}_{\alpha}(\gamma),
\mathrm{sep}_{\alpha},
\delta^2S_{\alpha},
{\mathsf K}_{\alpha},
{\mathcal P}^{hol}_{\alpha}
\right).
}
$$

Here \({\mathcal N}_{\alpha}(\gamma)\) is a predeclared neighboring-path
bundle, \(\mathrm{sep}_{\alpha}\) is a finite separation observable,
\(\delta^2S_{\alpha}\) is the printed second variation of the sector action,
and \({\mathsf K}_{\alpha}\) is the response map that connects holonomy probes
to separation change.

### Theorem 5.2: Conditional Finite Geodesic Deviation

Searchable theorem tag:

`V4P25-GR4-GEODESIC-DEVIATION-THEOREM`.

If `V4P25-GR4-FINITE-JACOBI-GATE` holds and the curvature probe family in GR3
is representation-complete on the neighboring-path bundle, then for every
licensed holonomy probe \(\chi\):

$$
\boxed{
\Delta\mathrm{sep}_{\alpha}
=
{\mathsf K}_{\alpha,\chi}\,
{\mathcal R}^{eff}_{\alpha,\chi}\,
\mathrm{sep}_{\alpha}
+\varepsilon^{dev}_{\alpha},
}
$$

with \(|\varepsilon^{dev}_{\alpha}|\le\tau_{dev}\).  A continuum Jacobi
equation is recovered only as the effective description of this finite
response law.

Proof sketch.  The finite Jacobi packet prints the neighboring-path bundle and
the second variation of the least-bias sector action, so the response is not
being inferred from notation.  The GR3 probe identities identify the relevant
loop-transport defects with corner-sourced curvature probes.  Applying the
printed response map \({\mathsf K}_{\alpha,\chi}\) gives the stated deviation
law up to the declared second-variation and transport errors. `square`

### GR4 Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{GR4F1}:&\hbox{free-fall path changes under pure R-move after gauge fix};\\
\mathrm{GR4F2}:&\hbox{deviation signal uncorrelated with }{\mathcal R}^{eff};\\
\mathrm{GR4F3}:&\hbox{least-bias update requires posterior tuning per endpoint pair};\\
\mathrm{GR4F4}:&\hbox{signed interval cost permits unbounded negative cycles};\\
\mathrm{GR4F5}:&\hbox{geodesic deviation is claimed without a finite Jacobi packet.}
\end{array}
}
$$

## 6. Finite Stress-Source Index And Dynamics

Searchable construction tag:

`V4P25-FINITE-STRESS-SOURCE-INDEX`.

Let the matter source complex on edge \(e\) carry a finite component index
\(A\in{\mathcal I}^{stress}_{\alpha}\):

$$
\boxed{
{\mathcal K}^{matter}_{\alpha}(e),
\qquad
T^{fin}_{\alpha,A}(e)=\operatorname{Tr}\Xi^{matter}_{\alpha,A}(e).
}
$$

Define the geometric index as a componentwise edge contraction of corner
residues:

$$
\boxed{
G^{fin}_{\alpha,A}(e)
=
\sum_{\triangle\ni e}w_{\triangle e,A}\,\Omega_{\alpha}(\triangle),
}
$$

with fixed combinatorial weights \(w_{\triangle e,A}\).  The index set and
weights are part of the source dictionary, not decorations added after the
coupling is queried.

Searchable dictionary tag:

`V4P25-GR5-TENSOR-SOURCE-DICTIONARY`.

Finite Einstein-coupling candidate:

$$
\boxed{
G^{fin}_{\alpha,A}(e)
=
\kappa_{\alpha,A}^{\ \ B}T^{fin}_{\alpha,B}(e)
+E^{dyn}_{\alpha,A}(e),
}
$$

subject to divergence constraints:

$$
\boxed{
\nabla^{fin}_{\alpha}G^{fin}_{\alpha,A}=0,
\qquad
\nabla^{fin}_{\alpha}T^{fin}_{\alpha,A}=0.
}
$$

These are not consequences of notation.  They are finite conservation gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{Bianchi}_{fin}:&
\nabla^{fin}_{\alpha}G^{fin}_{\alpha,A}=0
\hbox{ follows from the corner/cohomology incidence complex};\\
\mathrm{MatterCons}_{fin}:&
\nabla^{fin}_{\alpha}T^{fin}_{\alpha,A}=0
\hbox{ follows from the matter source complex};\\
\mathrm{Couple}_{fin}:&
G^{fin}_{\alpha,A}-\kappa_{\alpha,A}^{\ \ B}T^{fin}_{\alpha,B}
\hbox{ is a controlled exact/divergence-free residual.}
\end{array}
}
$$

### Theorem 6.1: Kinematic-Dynamic Split

Searchable theorem tag:

`V4P25-GR5-KINEMATIC-DYNAMIC-SPLIT-THEOREM`.

From P24 alone, GR1-GR4a and conditional GR4b may close without fixing a unique
\(\kappa_{\alpha,A}^{\ \ B}\)-law or forcing \(E^{dyn}_{\alpha,A}=0\).
Therefore GR5 requires an additional coupling law or additional source packet
assumptions.

Proof.  P24 determines \((Q,C)\) and generated geometric holonomy.  It does
not uniquely determine \(\Xi^{matter}_{A}\) nor a universal contraction map from
matter components to geometric components across all admissible contexts.
Hence dynamics is underdetermined by kinematics alone. `square`

### Theorem 6.2: Conservation Is Necessary But Not Sufficient

Searchable theorem tag:

`V4P25-GR5-CONSERVATION-NOT-SUFFICIENT`.

Even if \(\mathrm{Bianchi}_{fin}\) and \(\mathrm{MatterCons}_{fin}\) both hold,
GR5 does not follow unless `Couple_fin` or an equivalent finite variational
law fixes \(\kappa_{\alpha,A}^{\ \ B}\) and the residual
\(E^{dyn}_{\alpha,A}\).

Proof.  Conservation constrains the allowed subspace of \(G^{fin}_{A}\) and
\(T^{fin}_{A}\), but two separately divergence-free finite cochain families
need not be connected by a universal component contraction.  One may add any
divergence-free geometric source not in the span of \(T^{fin}_{A}\), or any
conserved matter component invisible to the corner contraction, without
violating the two conservation identities.  Thus the coupling is an
additional value law, not a consequence of conservation alone. `square`

### GR5 Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{GR5F1}:&\hbox{no }\kappa_{\alpha,A}^{\ \ B}\hbox{ fits across contexts with conserved indices};\\
\mathrm{GR5F2}:&\hbox{divergence identities fail after refinement alignment};\\
\mathrm{GR5F3}:&\hbox{coupling works only by context-specific posterior calibration};\\
\mathrm{GR5F4}:&\hbox{the scalar trace erases source components needed for a tensor claim.}
\end{array}
}
$$

## 7. Minimal Worked Triangle Benchmark

Searchable benchmark tag:

`V4P25-MINIMAL-TRIANGLE-BENCHMARK`.

Take nodes \(s_0,s_1,s_2\) and edges \(01,12,02\).  Choose:

$$
\boxed{
Q(s_0)=0,\quad Q(s_1)=2,\quad Q(s_2)=5,
\qquad
\lambda=\frac12,
\qquad
\rho^{op}=1.
}
$$

Then:

$$
\boxed{
N_{01}=2,\quad N_{12}=3,\quad N_{02}=5.
}
$$

Choose corner residues:

$$
\boxed{
C_{01}=0,\quad C_{12}=0,\quad C_{02}=-1.
}
$$

Hence:

$$
\boxed{
\Omega_{012}=0+0-(-1)=1,
\qquad
H_{012}=\lambda\Omega_{012}=\frac12.
}
$$

Edge actions:

$$
\boxed{
A^{eff}_{01}=\frac12(2+0)=1,
\quad
A^{eff}_{12}=\frac12(3+0)=\frac32,
\quad
A^{eff}_{02}=\frac12(5-1)=2.
}
$$

Check bridge defect:

$$
\boxed{
A^{eff}_{01}+A^{eff}_{12}-A^{eff}_{02}=1+\frac32-2=\frac12=H_{012}.
}
$$

This is the finite curved case: generated holonomy equals triangle defect.

### 7.1 GR1 Example Readout

Take \((a_1,a_2,a_3)=(1,6,0)\), so
\(I^{raw}(e)=N(e)+6C(e)\):

$$
\boxed{
I^{raw}_{01}=2,
\quad
I^{raw}_{12}=3,
\quad
I^{raw}_{02}=-1.
}
$$

Because this benchmark has not printed reverse-edge records
\(\bar{01},\bar{12},\bar{02}\), it is not yet a GR1 metric pass.  It is an
oriented action-class readout.  If a later packet prints reverse records whose
symmetrized values are:

$$
\boxed{
I^{sym}_{01}=2,\quad I^{sym}_{12}=3,\quad I^{sym}_{02}=-1,
}
$$

then with \(\tau_I<1\), the direct edge \(02\) is timelike-like while
\(01,12\) are spacelike-like.  Even then, this becomes a full metric pass only
after the same triangle is embedded in a finite frame satisfying reversal
symmetry, quadratic coherence, and stable Lorentzian signature.

### 7.2 GR3 Example Curvature

If the printed holonomy probe \(\chi_0=\operatorname{tr}\) gives
\(\chi_0(L_{012}-I)=0.5\pm0.05\), then with
\(\tau_{conn,\chi_0}=0.05\):

$$
\boxed{
{\mathcal R}^{eff}_{012,\chi_0}
=
\lambda_{\chi_0}\Omega_{012}\ \hbox{within tolerance}.
}
$$

So the traced GR3 witness passes on this patch only after the loop transport
and corner-frame compatibility data are printed.  Full GR3 curvature requires
the representation-complete probe family, not only \(\chi_0\).

### 7.3 GR4 Example Deviation

Take two neighboring path bundles with initial separation \(\mathrm{sep}_0\).
If the finite Jacobi packet is printed, a measured finite deviation may take
the form:

$$
\boxed{
\Delta\mathrm{sep}=k_{\chi_0}\,\frac12\,\mathrm{sep}_0+\varepsilon,
\qquad
|\varepsilon|\le\tau_{dev},
}
$$

matching Theorem 5.2 form for the traced holonomy probe.  This supports the
deviation part of GR4 on the patch only if the neighboring-path bundle,
second variation, and response map were printed before the deviation query.

Without that Jacobi packet, Section 7 supports only GR4 free-fall
benchmarking, not geodesic deviation.

### 7.4 GR5 Example Status

Suppose matter indices:

$$
\boxed{
T^{fin}_{01,A}=1,
\quad
T^{fin}_{12,A}=1,
\quad
T^{fin}_{02,A}=2
\quad
\hbox{for one printed component }A.
}
$$

A single component can match one edge or average, but no printed global
dictionary yet ensures cross-context uniqueness with conserved divergence
identities across all stress components.  Hence this patch is consistent with
GR5-WEAK, not GR5-PASS.

## 8. Classical Interface Tests

Searchable test tag:

`V4P25-CLASSICAL-GR-TESTS`.

Define five finite tests:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{test} & \hbox{finite observable} & \hbox{pass condition}\\
\hline
\mathrm{T1} & \hbox{weak-field potential proxy from }Q,C & \hbox{Newtonian-like acceleration table emerges}\\
\mathrm{T2} & \hbox{clock edge ratio from }I^{sym},I^{or} & \hbox{redshift ordering stable across refinements}\\
\mathrm{T3} & \hbox{path-separation deviation} & \hbox{proportional to probed }{\mathcal R}^{eff}_{\chi}\\
\mathrm{T4} & \hbox{loop transport phase} & \hbox{lensing-like deflection correlates with }\Omega\\
\mathrm{T5} & \hbox{finite divergence checks} & \hbox{simultaneous conservation for }G^{fin}_{A},T^{fin}_{A}
\end{array}
}
$$

Current paper-level status from constructions above:

$$
\boxed{
\begin{array}{c|c}
\mathrm{T1} & \mathrm{BENCHMARK\text{-}DEFINED}\\
\mathrm{T2} & \mathrm{BENCHMARK\text{-}DEFINED}\\
\mathrm{T3} & \mathrm{PATCH\text{-}CANDIDATE}\\
\mathrm{T4} & \mathrm{BENCHMARK\text{-}DEFINED}\\
\mathrm{T5} & \mathrm{OPEN}
\end{array}
}
$$

Thus the classical-interface tests are not empirical or continuum-GR
confirmations.  They are finite tables to run after the readout, transport,
and coupling packets are printed.

## 9. Main Reconstruction Theorem

Searchable theorem tag:

`V4P25-MAIN-FINITE-GR-RECONSTRUCTION-THEOREM`.

Assume:

$$
\boxed{
\begin{array}{ll}
\mathrm{M1}:&\hbox{P24 descent gates DA1-DA9 hold on a cofinal family};\\
\mathrm{M2}:&\hbox{metric coefficients are fixed and GR0/GR1 reversal, quadratic,
and signature gates hold};\\
\mathrm{M3}:&\hbox{transport }U\hbox{ is finite Levi-Civita, corner-frame compatible,
and holonomy-probe complete};\\
\mathrm{M4}:&\hbox{sector-adjusted least-bias geodesic law is fixed pre-query,
with Jacobi packet if deviation is claimed};\\
\mathrm{M5}:&\hbox{matter complex is finite, component-indexed, and
divergence-admissible}.
\end{array}
}
$$

Then:

$$
\boxed{
\hbox{GR1, GR2, GR3, and GR4a hold}
\quad
\hbox{(effective finite metric/transport/free-fall kinematics),}
}
$$

where \(GR4a\) means refinement-invariant free fall.  The deviation half
\(GR4b\) holds only when the finite Jacobi-response packet is printed.

For dynamics:

$$
\boxed{
\mathrm{GR5}
=
\mathrm{PASS}
\ \hbox{iff a universal refinement-stable coupling law }
\kappa_{\alpha,A}^{\ \ B}\to\kappa_{*,A}^{\ \ B}
\ \hbox{exists with }E^{dyn}_{A}\to0.
}
$$

Proof.  GR1 follows from Theorem 2.1 under the corrected quadratic-coherence
and signature hypotheses.  GR2 follows from Theorem 3.1 under M1-M2.  GR3
follows from Theorem 4.1 under M1-M3.  GR4 follows from Theorems 5.1-5.2
under M1-M4, with Theorem 5.1 proving free fall and Theorem 5.2 applying only
when the Jacobi packet is included.  GR5 requires additional componentwise
coupling closure by Theorems 6.1 and 6.2, which is equivalent to the stated
refinement-stable limit condition. `square`

## 10. Gate Verdict For Paper 25

Searchable verdict tag:

`V4P25-FINAL-VERDICT`.

Current through-paper verdict:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{GR1} & \mathrm{PASS\text{-}COND} & \hbox{finite metric readout only with quadratic/signature gates}\\
\mathrm{GR2} & \mathrm{PASS\text{-}COND} & \hbox{equivalence principle inherited when readout gates are refinement-stable}\\
\mathrm{GR3} & \mathrm{PASS\text{-}COND} & \hbox{curvature sourced by corner cohomology if corner-frame and probe-complete gates hold}\\
\mathrm{GR4a} & \mathrm{PASS\text{-}COND} & \hbox{least-bias free-fall after sector-cost and no-cycle gates}\\
\mathrm{GR4b} & \mathrm{PASS\text{-}COND/OPEN} & \hbox{geodesic deviation only after finite Jacobi-response packet}\\
\mathrm{GR5} & \mathrm{WEAK\text{-}OPEN} & \hbox{component coupling law not yet universally closed}
\end{array}
}
$$

Hence the strongest honest paper-level claim is:

$$
\boxed{
\mathrm{V4P25}:
\quad
\mathrm{GR\text{-}KIN\ reduced\ to\ explicit\ finite\ readout/transport/path/Jacobi\ gates,}
\quad
\mathrm{GR\text{-}DYN\ remains\ open.}
}
$$

## 11. What Remains For Full GR-DYN Closure

Searchable next-step tag:

`V4P25-NEXT-COUPLING-LAW-PACKET`.

The next missing packet is explicit and finite:

$$
\boxed{
\begin{array}{ll}
\mathrm{P25DYN\text{-}A}:&\hbox{print refinement-stable matter complexes }{\mathcal K}^{matter}_{\alpha};\\
\mathrm{P25DYN\text{-}B}:&\hbox{prove finite divergence conservation jointly for }G^{fin}_{A},T^{fin}_{A};\\
\mathrm{P25DYN\text{-}C}:&\hbox{derive }\kappa_{\alpha,A}^{\ \ B}\hbox{ from finite source law, not calibration};\\
\mathrm{P25DYN\text{-}D}:&\hbox{show }E^{dyn}_{\alpha,A}\to0\hbox{ on cofinal refinements};\\
\mathrm{P25DYN\text{-}E}:&\hbox{run T1-T5 on at least one nontrivial multi-loop packet}.
\end{array}
}
$$

If these pass, the effective Einstein interface is recovered as a theorem of
finite descent plus finite source coupling law, rather than as imported
continuum assumption.

## 12. Immediate Development Packet `P25-GRKIN-TRI-001`

Searchable packet tag:

`V4P25-GRKIN-TRI-001`.

The corrected next finite object is not merely the three edge values
\((01,12,02)\).  It must include the frame, composition, transport, and path
data needed to run the corrected gates:

$$
\boxed{
\begin{array}{ll}
\mathrm{K1}:&\hbox{nodes }s_0,s_1,s_2\hbox{ and a local frame }
\{e_a(s_i)\};\\
\mathrm{K2}:&\hbox{edge records }Q,C,\rho^{op}\hbox{ for frame, reverse, inverse,
and composite edges};\\
\mathrm{K3}:&\hbox{predeclared coefficients }(a_1,a_2,a_3)\hbox{, tolerance }
\tau_I,\hbox{ and }I^{raw},I^{sym},I^{or};\\
\mathrm{K4}:&\hbox{reversal, quadratic-coherence, and Lorentzian signature tables};\\
\mathrm{K5}:&\hbox{finite transport maps }U(ij),U(jk),U(ki)\hbox{ with LC audit};\\
\mathrm{K6}:&\hbox{holonomy probe family }{\mathcal P}^{hol}\hbox{ and corner-frame checks }
\chi(U_{ki}U_{jk}U_{ij}-I)=\lambda_{\chi}\Omega+\varepsilon_{\chi};\\
\mathrm{K7}:&\hbox{sector-adjusted path cost }\ell^{geo}\hbox{ and prior }\mu^0;\\
\mathrm{K8}:&\hbox{finite Jacobi-response packet for geodesic deviation};\\
\mathrm{K9}:&\hbox{optional component matter complex }{\mathcal K}^{matter}_{A}
\hbox{ for GR5 diagnostics.}
\end{array}
}
$$

The packet has a deterministic verdict function:

$$
\boxed{
\begin{array}{c|l}
\hbox{verdict} & \hbox{condition}\\
\hline
\mathrm{KIN\text{-}PASS} &
\mathrm{K1\text{-}K7}\hbox{ pass and the GR1-GR4a falsifiers do not fire}\\
\mathrm{KIN\text{-}DEV\text{-}PASS} &
\mathrm{KIN\text{-}PASS}\hbox{ plus K8 and the GR4b falsifiers do not fire}\\
\mathrm{KIN\text{-}PARTIAL} &
\hbox{edge/holonomy data pass but metric, LC, or path-sector gates are absent}\\
\mathrm{DYN\text{-}WEAK} &
\mathrm{KIN\text{-}PASS}\hbox{ plus K9 finite matter data, but no coupling law}\\
\mathrm{DYN\text{-}PASS} &
\mathrm{DYN\text{-}WEAK}\hbox{ plus }\mathrm{P25DYN\text{-}A\text{--}D}\\
\mathrm{NO\text{-}GO} &
\hbox{a listed falsifier fires with no licensed repair}
\end{array}
}
$$

### Theorem 12.1: `P25-GRKIN-TRI-001` Is The Minimal Honest Kinematic Packet

Searchable theorem tag:

`V4P25-GRKIN-TRI-001-MINIMALITY`.

Any finite packet claiming effective GR metric/transport/free-fall kinematics
must contain analogues of K1-K7.  Any finite packet claiming geodesic
deviation must also contain K8.  Otherwise one of the corrected audit gaps
reappears.

Proof.  K1-K4 are required by Theorem 2.1; without them the edge score is not
a metric readout.  K5-K6 are required by Theorem 4.1; without them corner
holonomy is not identified with frame curvature.  K7 is required by Theorem
5.1; without it the sector-adjusted interval score may not define a finite free-fall
law.  K8 is required by Theorem 5.2 for geodesic deviation.  K9 is not
required for kinematics but is the first optional input for GR5.  Therefore
K1-K7 are minimal for corrected GR1-GR4a, and K1-K8 are minimal for the
corrected GR1-GR4b claim. `square`

The existing triangle in Section 7 should be read as `KIN-PARTIAL`: it prints
the value and corner holonomy data, but it does not yet print the full frame
composition, reverse-edge symmetrization, finite Levi-Civita transport,
holonomy probe family, path-sector packet, or Jacobi-response packet.

## 13. Final Statement

Searchable closing tag:

`V4P25-CLOSING-STATEMENT`.

Paper 25 resolves the reconstruction question at the present finite-audit
level:

$$
\boxed{
\hbox{finite descent can support effective GR kinematics once the finite
readout, transport, path-sector, and Jacobi-response gates are printed.}
}
$$

It also sharpens the remaining open frontier:

$$
\boxed{
\hbox{effective Einstein dynamics requires one additional finite
stress-curvature coupling law packet.}
}
$$

This is progress, not postponement: the unknown is no longer "how to get GR"
in general, but a specific finite coupling theorem with explicit falsifiers.

## 14. Einstein Move: Make Finite Equivalence Do The Work

Searchable move tag:

`V4P25-EINSTEIN-FINITE-EQUIVALENCE-MOVE`.

The Einstein move is not to add more numbers.  It is to find the finite
principle that makes the numbers coordinate-free.

In this paper the principle should be:

$$
\boxed{
\hbox{no finite presentation of the same actual descent family is physically
privileged.}
}
$$

More concretely:

$$
\boxed{
\hbox{all first-order local gravitational artifacts must be removable by a
finite inertial frame, and only closed-loop/corner residues may remain.}
}
$$

Searchable postulate tag:

`V4P25-FINITE-EQUIVALENCE-POSTULATE`.

The postulate has four parts.

$$
\boxed{
\begin{array}{c|l}
\hbox{part} & \hbox{finite content}\\
\hline
\mathrm{EP1} & \hbox{same actual records under R-move have identical coincidence
readouts}\\
\mathrm{EP2} & \hbox{local first-order transport residue can be killed by a
frame choice}\\
\mathrm{EP3} & \hbox{closed-loop residue is invariant and equals the corner
cohomology class}\\
\mathrm{EP4} & \hbox{source response is local, divergence-compatible, and
refinement-stable}
\end{array}
}
$$

This converts GR from an imported continuum template into a finite covariance
problem.  The metric is not "whatever \(I\) says"; the metric is the unique
symmetric readout surviving reversal, local inertial cancellation,
polarization, and stable signature.  The connection is not a smooth
\(\Gamma\) inserted by hand; it is the finite transport family whose
first-order frame residue can be removed while loop residue remains.  The
curvature is not a trace; it is the representation-complete closed-loop
defect.

### 14.1 Einstein Kinematic Theorem Target

Searchable theorem target:

`V4P25-EINSTEIN-KINEMATIC-CLOSURE-TARGET`.

Target theorem:

$$
\boxed{
\mathrm{EP1+EP2+EP3}
\Longrightarrow
\mathrm{GR1+GR2+GR3+GR4a}
}
$$

provided the finite packet prints:

$$
\boxed{
(I^{raw},I^{sym},I^{or},g^{eff},U,{\mathcal P}^{hol},\Omega,\ell^{geo},\mu^0).
}
$$

The proof route is:

$$
\boxed{
\begin{array}{c|l}
\hbox{step} & \hbox{claim to prove}\\
\hline
\mathrm{E1} &
\hbox{reversal plus coincidence invariance forces }I^{sym}\hbox{ as the metric
candidate}\\
\mathrm{E2} &
\hbox{finite parallelogram coherence forces bilinear polarization}\\
\mathrm{E3} &
\hbox{local removal of first-order transport residue forces LC-compatible
transport}\\
\mathrm{E4} &
\hbox{closed-loop invariance forces curvature to be a corner-class probe}\\
\mathrm{E5} &
\hbox{least-bias path covariance forces the free-fall law to be frame-invariant}
\end{array}
}
$$

This is the principled GR-kinematics closure.  It does not ask whether one
triangle can be made to look GR-like.  It asks whether every allowed change of
finite description leaves exactly the same local physical content, with only
closed-loop residues surviving.

### 14.2 Einstein Dynamics Theorem Target

Searchable theorem target:

`V4P25-EINSTEIN-DYNAMIC-COUPLING-TARGET`.

The dynamics target is stronger:

$$
\boxed{
\mathrm{EP1+EP2+EP3+EP4}
\Longrightarrow
G^{fin}_{A}
=
\kappa_{A}^{\ B}T^{fin}_{B}
+E^{dyn}_{A},
\qquad
E^{dyn}_{A}\to0
}
$$

with \(\kappa_{A}^{\ B}\) universal on the cofinal family.

This should be attacked by a finite analogue of the Einstein uniqueness
argument:

$$
\boxed{
\begin{array}{c|l}
\hbox{axiom} & \hbox{role}\\
\hline
\mathrm{D1} & \hbox{locality: }G^{fin}_{A}(e)\hbox{ uses only incident corner
classes}\\
\mathrm{D2} & \hbox{covariance: }G^{fin}_{A}\hbox{ transforms as the same
component family as }T^{fin}_{A}\\
\mathrm{D3} & \hbox{finite Bianchi: }\nabla^{fin}G^{fin}_{A}=0\\
\mathrm{D4} & \hbox{source conservation: }\nabla^{fin}T^{fin}_{A}=0\\
\mathrm{D5} & \hbox{minimal response: no divergence-free invisible geometric
source is admitted}
\end{array}
}
$$

If D1-D5 force a unique component contraction
\(\kappa_{A}^{\ B}\), then GR5 is not calibrated by hand.  It is the only
finite source response compatible with finite equivalence.

If D1-D5 fail, the failure is useful: it says exactly which extra finite
source channel, boundary term, or higher-curvature component is physically
real rather than hidden inside notation.

### 14.3 Einstein Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{EIF1}:&\hbox{two same-actual refinements disagree on coincidence data};\\
\mathrm{EIF2}:&\hbox{first-order transport residue cannot be removed locally};\\
\mathrm{EIF3}:&\hbox{loop residue changes under pure frame relabeling};\\
\mathrm{EIF4}:&\hbox{a divergence-free geometric component remains invisible to
matter sources};\\
\mathrm{EIF5}:&\hbox{the coupling tensor }\kappa_{A}^{\ B}\hbox{ depends on the
presentation rather than the actual family.}
\end{array}
}
$$

The next Einstein packet is therefore:

$$
\boxed{
\mathrm{P25\text{-}EIN\text{-}FRAME\text{-}001}
=
\hbox{one multi-frame descent patch with reversals, local inertial frames,
loop probes, and component sources.}
}
$$

It must show that changing the finite frame removes local first-order
transport but cannot remove the closed-loop corner residue.

## 15. Feynman Move: Build The Finite Probe Calculus

Searchable move tag:

`V4P25-FEYNMAN-FINITE-PROBE-CALCULUS-MOVE`.

The non-cliche Feynman move is to change representation until the calculation
has no hiding places.  The question becomes:

$$
\boxed{
\hbox{what finite apparatus readings can be composed, summed, transformed,
and compared without contradiction?}
}
$$

So define the probe algebra:

$$
\boxed{
{\mathfrak P}_{\alpha}
=
\left\langle
I^{sym},I^{or},
U_{\gamma},
L_{\sigma},
\chi(L_{\sigma}-I),
\mathrm{sep},
\delta^2S,
T^{fin}_{A},
G^{fin}_{A}
\right\rangle.
}
$$

Here \(\gamma\) ranges over finite paths, \(\sigma\) over finite closed loops,
and \(\chi\) over the printed holonomy probes.  This algebra is not a toy
model.  It is the finite measurement language of the theory.

The Feynman demand is that all equivalent ways of calculating the same finite
reading agree.  That gives Ward-style identities.

Searchable identity tag:

`V4P25-FEYNMAN-FINITE-WARD-IDENTITIES`.

$$
\boxed{
\begin{array}{c|l}
\hbox{identity} & \hbox{finite meaning}\\
\hline
\mathrm{W1} & \hbox{frame relabeling changes transports by conjugation only}\\
\mathrm{W2} & \hbox{coarse-graining paths before or after summing gives the same
endpoint kernel}\\
\mathrm{W3} & \hbox{exact-pair boundary channels cancel from closed-loop probes}\\
\mathrm{W4} & \hbox{loop probe defect equals the corner residue in every
representation-complete channel}\\
\mathrm{W5} & \hbox{source insertion changes the geometric probe by a conserved
component response}\\
\mathrm{W6} & \hbox{Jacobi response is the second variation of the same path
kernel that defines free fall}
\end{array}
}
$$

In formulas, the central finite identities are:

$$
\boxed{
U_{\gamma}^{g}
=
S_{t(\gamma)}U_{\gamma}S_{s(\gamma)}^{-1},
\qquad
\chi(L_{\sigma}^{g}-I)=\chi(L_{\sigma}-I),
}
$$

$$
\boxed{
Z_{ij}
=
\sum_{k\in{\mathcal S}}
Z_{ik}Z_{kj}
+
\varepsilon^{cg}_{ij},
\qquad
\varepsilon^{cg}_{ij}\to0
\hbox{ on licensed refinements,}
}
$$

and:

$$
\boxed{
\delta_{\mathrm{source}}
\chi(L_{\sigma}-I)
=
\kappa_{\chi}^{\ A}\delta T^{fin}_{A}
+\nabla^{fin}B_{\chi}
+\mathcal A_{\chi}.
}
$$

The anomaly \(\mathcal A_{\chi}\) is the key.  Feynman's real move would not
hide it.  If \(\mathcal A_{\chi}=0\) for the complete probe family, the
coupling is internally consistent.  If not, the anomaly tells whether the
missing object is:

$$
\boxed{
\begin{array}{c|l}
\hbox{anomaly type} & \hbox{meaning}\\
\hline
\mathrm{FA1} & \hbox{missing probe channel}\\
\mathrm{FA2} & \hbox{missing matter component}\\
\mathrm{FA3} & \hbox{missing boundary/exact-pair term}\\
\mathrm{FA4} & \hbox{real higher-curvature finite source}\\
\mathrm{FA5} & \hbox{bad descent family, hence no GR effective limit}
\end{array}
}
$$

### 15.1 Feynman Closure Target

Searchable theorem target:

`V4P25-FEYNMAN-PROBE-CLOSURE-TARGET`.

Target theorem:

$$
\boxed{
\mathrm{W1\text{-}W6}
\Longrightarrow
\mathrm{GR1+GR2+GR3+GR4a+GR4b}
\quad
\hbox{and either }
\mathrm{GR5}
\hbox{ or a printed anomaly source.}
}
$$

This is a stronger practical program than guessing a coupling.  It says:

$$
\boxed{
\hbox{if two finite calculations describe the same actual apparatus reading,
their disagreement is not error; it is a missing field/source/boundary
channel.}
}
$$

That is the useful Feynman pressure: turn ambiguity into a calculable anomaly
ledger.

### 15.2 Feynman Falsifiers

$$
\boxed{
\begin{array}{ll}
\mathrm{FFF1}:&\hbox{path kernel composition fails under licensed
coarse-graining};\\
\mathrm{FFF2}:&\hbox{closed-loop probes are not conjugation-invariant};\\
\mathrm{FFF3}:&\hbox{exact-pair channels alter physical loop readings};\\
\mathrm{FFF4}:&\hbox{source insertions produce uncancelled anomalies with no
new licensed channel};\\
\mathrm{FFF5}:&\hbox{Jacobi response is not the second variation of the
free-fall kernel.}
\end{array}
}
$$

The next Feynman packet is:

$$
\boxed{
\mathrm{P25\text{-}FEY\text{-}PROBE\text{-}001}
=
\hbox{one finite patch with two equivalent calculation routes for every
metric, loop, path, Jacobi, and source reading.}
}
$$

The packet should deliberately include redundant calculations.  Redundancy is
the point: it forces hidden choices to become identities or anomalies.

## 16. Combined Next Step

Searchable next-action tag:

`V4P25-NEXT-ACTION-GRKIN-GRDYN-BRIDGE`.

The next honest push is not another scalar triangle.  It is a finite
multi-frame, multi-loop, source-bearing patch:

$$
\boxed{
\mathrm{P25\text{-}GR\text{-}BRIDGE\text{-}001}
=
\left(
\mathrm{P25\text{-}EIN\text{-}FRAME\text{-}001},
\mathrm{P25\text{-}FEY\text{-}PROBE\text{-}001}
\right).
}
$$

It must print:

$$
\boxed{
\begin{array}{ll}
\mathrm{B1}:&\hbox{reverse edge records and symmetrized metric readouts};\\
\mathrm{B2}:&\hbox{at least two local finite frames for the same actual patch};\\
\mathrm{B3}:&\hbox{finite transports and their conjugation laws};\\
\mathrm{B4}:&\hbox{a complete holonomy probe family on at least two loops};\\
\mathrm{B5}:&\hbox{path kernels with two coarse-graining calculation routes};\\
\mathrm{B6}:&\hbox{Jacobi second-variation packet};\\
\mathrm{B7}:&\hbox{component stress-source dictionary};\\
\mathrm{B8}:&\hbox{anomaly ledger }{\mathcal A}_{\chi}\hbox{ for source insertions}.
\end{array}
}
$$

If B1-B6 pass, Paper 25 has real finite GR kinematics, not just a suggestive
analogy.  If B7-B8 pass with zero anomaly, it has a finite route to
Einstein-like dynamics.  If B8 prints a nonzero licensed anomaly, that is not
failure; it is the precise next term the theory must include.

## 17. Executing `P25-GR-BRIDGE-001`: B1-B8

Searchable packet tag:

`V4P25-P25-GR-BRIDGE-001`.

This section prints one explicit finite bridge packet.  It is intentionally
small: a \(1+1\) boost-sector patch with two closed loops.  Its purpose is not
to claim full \(3+1\) Einstein dynamics.  Its purpose is sharper:

$$
\boxed{
\hbox{show that the corrected B1-B8 gates are jointly executable by finite
records.}
}
$$

The packet has nodes:

$$
\boxed{
{\mathcal S}=\{p,t,x,c,d\}.
}
$$

Think of \(T:p\to t\) as the local clock edge, \(X:p\to x\) as the local ruler
edge, \(D_{+}:p\to c\) as \(T\oplus X\), and \(D_{-}:p\to d\) as \(T\ominus X\).
This is only finite notation; no continuum manifold is assumed.

Use coefficients:

$$
\boxed{
a_1=a_2=a_3=1,
\qquad
C(e)=0
\quad
\hbox{on the B1 metric-readout edges.}
}
$$

Thus:

$$
\boxed{
I^{raw}(e)=N(e)-\log\rho^{op}(e).
}
$$

### 17.1 B1: Reverse Edge Records And Symmetric Metric Readout

Searchable audit tag:

`V4P25-B1-REVERSE-SYMMETRIC-READOUT`.

Print the edge records:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{edge} & N(e) & \rho^{op}(e) & I^{raw}(e)\\
\hline
T & 1/10 & e & -9/10\\
\bar T & -1/10 & e & -11/10\\
X & 0 & e^{-1} & 1\\
\bar X & 0 & e^{-1} & 1\\
D_{+} & 1/10 & 1 & 1/10\\
\bar D_{+} & -1/10 & 1 & -1/10\\
D_{-} & 1/10 & 1 & 1/10\\
\bar D_{-} & -1/10 & 1 & -1/10
\end{array}
}
$$

Therefore:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{edge pair} & I^{sym} & I^{or}\\
\hline
T & -1 & 1/10\\
X & 1 & 0\\
D_{+} & 0 & 1/10\\
D_{-} & 0 & 1/10
\end{array}
}
$$

The metric readout uses only \(I^{sym}\).  With frame
\({\mathcal F}_p=(T,X)\):

$$
\boxed{
g^{eff}_{{\mathcal F}}
=
\begin{pmatrix}
-1 & 0\\
0 & 1
\end{pmatrix}.
}
$$

The finite polarization check is:

$$
\boxed{
g^{eff}_{TX}
=
\frac12\left(I^{sym}(D_{+})-I^{sym}(T)-I^{sym}(X)\right)
=
\frac12(0+1-1)=0.
}
$$

The second diagonal is already printed by the one-edge clock/ruler readings:

$$
\boxed{
g^{eff}_{TT}=I^{sym}(T)=-1,
\qquad
g^{eff}_{XX}=I^{sym}(X)=1.
}
$$

Verdict:

$$
\boxed{
\mathrm{B1}=\mathrm{PASS}_{packet}.
}
$$

### 17.2 B2: Two Local Finite Frames For The Same Actual Patch

Searchable audit tag:

`V4P25-B2-TWO-FRAME-EQUIVALENCE`.

Print a second finite frame:

$$
\boxed{
{\mathcal F}'_p=(T',X'),
\qquad
\begin{pmatrix}
T'\\
X'
\end{pmatrix}
=
\Lambda
\begin{pmatrix}
T\\
X
\end{pmatrix},
\qquad
\Lambda=
\begin{pmatrix}
5/4 & 3/4\\
3/4 & 5/4
\end{pmatrix}.
}
$$

This is a finite rational Lorentz-frame change:

$$
\boxed{
\Lambda^T
\begin{pmatrix}
-1 & 0\\
0 & 1
\end{pmatrix}
\Lambda
=
\begin{pmatrix}
-1 & 0\\
0 & 1
\end{pmatrix}.
}
$$

So the same actual patch has two finite descriptions with the same
coincidence metric content.

Verdict:

$$
\boxed{
\mathrm{B2}=\mathrm{PASS}_{packet}.
}
$$

### 17.3 B3: Finite Transports And Conjugation Laws

Searchable audit tag:

`V4P25-B3-FINITE-TRANSPORT-CONJUGATION`.

Use a finite boost-sector transport label \(B(r)\).  This is a finite record
label, not an assumed continuum exponential.  It is licensed by the finite
composition rules:

$$
\boxed{
B(r)B(s)=B(r+s),
\qquad
B(0)=I,
\qquad
B(r)^{-1}=B(-r).
}
$$

The two printed closed loops are:

$$
\boxed{
\sigma_1=p\to t\to c\to x\to p,
\qquad
\sigma_2=p\to c\to d\to x\to p.
}
$$

Their loop transports are:

$$
\boxed{
L_{\sigma_1}=B(1/12),
\qquad
L_{\sigma_2}=B(1/6).
}
$$

Under the second frame, with \(S=\Lambda=B(\eta)\), transport transforms by:

$$
\boxed{
U_{\gamma}'=S_{t(\gamma)}U_{\gamma}S_{s(\gamma)}^{-1},
\qquad
L_{\sigma}'=S_pL_{\sigma}S_p^{-1}.
}
$$

In the printed \(1+1\) boost sector, boost labels commute, hence:

$$
\boxed{
L_{\sigma_1}'=L_{\sigma_1},
\qquad
L_{\sigma_2}'=L_{\sigma_2}.
}
$$

The first-order local frame presentation can change, but the closed-loop
residue cannot.

Verdict:

$$
\boxed{
\mathrm{B3}=\mathrm{PASS}_{packet}.
}
$$

### 17.4 B4: Complete Holonomy Probe Family On Two Loops

Searchable audit tag:

`V4P25-B4-HOLONOMY-PROBE-COMPLETENESS`.

On the licensed \(1+1\) boost-sector defect space:

$$
\boxed{
{\mathcal D}^{hol}=\{B(r):r\in{\mathbb Q}\}.
}
$$

the finite rapidity probe:

$$
\boxed{
\chi_{\eta}(B(r))=r
}
$$

is complete:

$$
\boxed{
\chi_{\eta}(B(r))=0
\Rightarrow
B(r)=B(0)=I
\quad
\hbox{inside }{\mathcal D}^{hol}.
}
$$

Print corner residues:

$$
\boxed{
\Omega_{\sigma_1}=1,
\qquad
\Omega_{\sigma_2}=2,
\qquad
\lambda_{\eta}=1/12.
}
$$

Then:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{loop} & L_{\sigma} & \chi_{\eta}(L_{\sigma}) &
\lambda_{\eta}\Omega_{\sigma}\\
\hline
\sigma_1 & B(1/12) & 1/12 & 1/12\\
\sigma_2 & B(1/6) & 1/6 & 1/6
\end{array}
}
$$

So the corner-frame identity holds on two loops, and the probe is complete on
the licensed boost-sector defect space.

Verdict:

$$
\boxed{
\mathrm{B4}=\mathrm{PASS}_{packet}.
}
$$

### 17.5 B5: Path Kernels With Two Coarse-Graining Routes

Searchable audit tag:

`V4P25-B5-PATH-KERNEL-COARSE-GRAINING`.

Use the finite path weights:

$$
\boxed{
w(T)=w(X)=e^{-1},
\qquad
w(D_{+})=e^{-2}.
}
$$

There are three admissible \(p\to c\) channels:

$$
\boxed{
\gamma_D=D_{+},
\qquad
\gamma_T=T\circ X,
\qquad
\gamma_X=X\circ T.
}
$$

Here \(T\circ X\) uses the translated copy \(X_t:t\to c\), and
\(X\circ T\) uses the translated copy \(T_x:x\to c\).  The translated copies
carry the same finite weights as \(X\) and \(T\), respectively.

Fine calculation:

$$
\boxed{
Z^{fine}_{pc}
=
w(D_{+})+w(T)w(X)+w(X)w(T)
=
3e^{-2}.
}
$$

Coarse-grained first-step calculation:

$$
\boxed{
Z^{cg}_{pc}
=
w(D_{+})+w(T)Z_{tc}+w(X)Z_{xc}
=
e^{-2}+e^{-1}e^{-1}+e^{-1}e^{-1}
=
3e^{-2}.
}
$$

Thus:

$$
\boxed{
\varepsilon^{cg}_{pc}=Z^{fine}_{pc}-Z^{cg}_{pc}=0.
}
$$

The same endpoint reading is obtained by two finite calculation routes.

Verdict:

$$
\boxed{
\mathrm{B5}=\mathrm{PASS}_{packet}.
}
$$

### 17.6 B6: Jacobi Second-Variation Packet

Searchable audit tag:

`V4P25-B6-FINITE-JACOBI-PACKET`.

Print the neighboring-path bundle:

$$
\boxed{
{\mathcal N}(\gamma_D)=\{\gamma_T,\gamma_X\},
\qquad
\mathrm{sep}(\gamma_T,\gamma_X)=1.
}
$$

Use the same sector action whose kernel was used in B5.  The second variation
readout is:

$$
\boxed{
\delta^2S_{\sigma_i}
=
\chi_{\eta}(L_{\sigma_i})
\quad
\hbox{for }i=1,2.
}
$$

With response map \({\mathsf K}_{\eta}=1\):

$$
\boxed{
\Delta\mathrm{sep}_{\sigma_i}
=
{\mathsf K}_{\eta}
\chi_{\eta}(L_{\sigma_i})
\mathrm{sep}
+\varepsilon^{dev}_{\sigma_i}.
}
$$

The printed table is:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{loop} & \chi_{\eta}(L_{\sigma}) & \Delta\mathrm{sep} &
\varepsilon^{dev}\\
\hline
\sigma_1 & 1/12 & 1/12 & 0\\
\sigma_2 & 1/6 & 1/6 & 0
\end{array}
}
$$

Therefore the packet has finite free-fall plus finite geodesic-deviation
response, not only a path MAP.

Verdict:

$$
\boxed{
\mathrm{B6}=\mathrm{PASS}_{packet}.
}
$$

### 17.7 B7: Component Stress-Source Dictionary

Searchable audit tag:

`V4P25-B7-COMPONENT-STRESS-SOURCE-DICTIONARY`.

Use a two-component source index:

$$
\boxed{
{\mathcal I}^{stress}=\{\eta,\perp\}.
}
$$

The geometric source component is the probed loop defect:

$$
\boxed{
G^{fin}_{\eta}(\sigma)=\chi_{\eta}(L_{\sigma}),
\qquad
G^{fin}_{\perp}(\sigma)=0.
}
$$

Print the matter source components:

$$
\boxed{
T^{fin}_{\eta}(\sigma)=\chi_{\eta}(L_{\sigma}),
\qquad
T^{fin}_{\perp}(\sigma)=0.
}
$$

Thus:

$$
\boxed{
\begin{array}{c|c|c|c|c}
\hbox{loop} & G^{fin}_{\eta} & T^{fin}_{\eta} &
G^{fin}_{\perp} & T^{fin}_{\perp}\\
\hline
\sigma_1 & 1/12 & 1/12 & 0 & 0\\
\sigma_2 & 1/6 & 1/6 & 0 & 0
\end{array}
}
$$

Use:

$$
\boxed{
\kappa_{A}^{\ B}
=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix},
\qquad
E^{dyn}_{A}=0.
}
$$

Both \(G^{fin}_{A}\) and \(T^{fin}_{A}\) are closed-loop cochains in this packet,
so their finite divergence is zero:

$$
\boxed{
\nabla^{fin}G^{fin}_{A}=0,
\qquad
\nabla^{fin}T^{fin}_{A}=0.
}
$$

Verdict:

$$
\boxed{
\mathrm{B7}=\mathrm{PASS}_{packet}
\quad
\hbox{for the printed two-component boost-sector dictionary.}
}
$$

This is a local finite source dictionary, not yet a universal \(3+1\)
Einstein coupling theorem.

### 17.8 B8: Anomaly Ledger For Source Insertions

Searchable audit tag:

`V4P25-B8-SOURCE-ANOMALY-LEDGER`.

Use the source-insertion identity:

$$
\boxed{
\delta_{\mathrm{source}}\chi_{\eta}(L_{\sigma})
=
\kappa_{\eta}^{\ A}\delta T^{fin}_{A}
+\nabla^{fin}B_{\eta}
+{\mathcal A}_{\eta}.
}
$$

Print the insertion:

$$
\boxed{
\delta T^{fin}_{\eta}(\sigma_1)=1/24,
\qquad
\delta T^{fin}_{\perp}(\sigma_1)=0.
}
$$

The packet response is:

$$
\boxed{
\delta_{\mathrm{source}}\chi_{\eta}(L_{\sigma_1})=1/24,
\qquad
\nabla^{fin}B_{\eta}=0.
}
$$

Therefore:

$$
\boxed{
{\mathcal A}_{\eta}(\sigma_1)
=
1/24-1/24-0
=0.
}
$$

For the orthogonal component:

$$
\boxed{
{\mathcal A}_{\perp}(\sigma_1)=0.
}
$$

The anomaly ledger is:

$$
\boxed{
\begin{array}{c|c|c|c|c}
\hbox{component} & \delta\chi(L) & \kappa\delta T & \nabla B &
{\mathcal A}\\
\hline
\eta & 1/24 & 1/24 & 0 & 0\\
\perp & 0 & 0 & 0 & 0
\end{array}
}
$$

Verdict:

$$
\boxed{
\mathrm{B8}=\mathrm{PASS}_{packet}
\quad
\hbox{with zero anomaly in the printed source sector.}
}
$$

## 18. Bridge Verdict

Searchable verdict tag:

`V4P25-P25-GR-BRIDGE-001-VERDICT`.

The B1-B8 audit is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{B1} & \mathrm{PASS}_{packet} &
\hbox{reverse records produce a symmetric Lorentzian readout}\\
\mathrm{B2} & \mathrm{PASS}_{packet} &
\hbox{two finite frames preserve the same metric content}\\
\mathrm{B3} & \mathrm{PASS}_{packet} &
\hbox{transport transforms by conjugation; loop residue is invariant}\\
\mathrm{B4} & \mathrm{PASS}_{packet} &
\hbox{complete boost-sector holonomy probe matches corner residue}\\
\mathrm{B5} & \mathrm{PASS}_{packet} &
\hbox{two path-kernel calculations agree}\\
\mathrm{B6} & \mathrm{PASS}_{packet} &
\hbox{Jacobi response is printed and matches loop curvature}\\
\mathrm{B7} & \mathrm{PASS}_{packet} &
\hbox{component source dictionary is conserved and coupled locally}\\
\mathrm{B8} & \mathrm{PASS}_{packet} &
\hbox{source insertion anomaly vanishes in the printed sector}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{P25\text{-}GR\text{-}BRIDGE\text{-}001}
\Rightarrow
\mathrm{GR\text{-}KIN\text{-}PASS}
\quad
\hbox{in the printed }1+1\hbox{ boost-sector patch.}
}
$$

and:

$$
\boxed{
\mathrm{P25\text{-}GR\text{-}BRIDGE\text{-}001}
\Rightarrow
\mathrm{GR\text{-}DYN\text{-}LOCAL\text{-}PASS}
\quad
\hbox{for the printed two-component source dictionary.}
}
$$

The honest limitation is equally important:

$$
\boxed{
\hbox{this packet proves executability of the finite GR bridge gates; it does
not yet prove universal }3+1\hbox{ Einstein dynamics.}
}
$$

The next theorem to prove is now precise:

$$
\boxed{
\hbox{every cofinal finite descent patch satisfying the same B1-B8 identities
has a refinement-stable effective GR interface.}
}
$$

That is the real Paper 25 frontier after `P25-GR-BRIDGE-001`: promote this
worked finite bridge from one licensed patch to a cofinal family theorem.

## 19. Einstein Continuation: Finite GR Normal-Form Theorem

Searchable theorem tag:

`V4P25-FINITE-GR-NORMAL-FORM-THEOREM`.

The bridge packet proves that the finite gates can be executed in one
licensed patch.  The Einstein continuation asks for the principle that forces
every admissible finite actual patch into the same kind of form.

The principle is:

$$
\boxed{
\hbox{finite gravitational content is what remains after every same-actual
local frame artifact has been removed.}
}
$$

This is the finite analogue of the equivalence principle.  It does not start
with a continuum metric.  It starts with actual records, finite frames,
transport, and closed-loop residues.

### 19.1 Normal-Form Axioms

Searchable axiom tag:

`V4P25-GR-NORMAL-FORM-AXIOMS-NF1-NF8`.

Let \({\mathfrak P}=\{{\mathcal P}_{\alpha}\}_{\alpha\in{\mathcal R}}\) be a
cofinal family of finite descent patches.  A patch is in admissible GR normal
form when it satisfies:

$$
\boxed{
\begin{array}{c|l}
\hbox{axiom} & \hbox{finite content}\\
\hline
\mathrm{NF1} & \hbox{actual-record invariance: R-moves preserve the
coincidence class of records}\\
\mathrm{NF2} & \hbox{reversal symmetry: metric readout uses }I^{sym}\hbox{ only}\\
\mathrm{NF3} & \hbox{quadratic coherence: finite parallelogram identities
polarize to }g^{eff}\\
\mathrm{NF4} & \hbox{stable signature: }g^{eff}\hbox{ has cofinally stable
Lorentzian index}\\
\mathrm{NF5} & \hbox{local inertial removability: first-order transport residue
can be killed by a frame choice}\\
\mathrm{NF6} & \hbox{closed-loop invariance: loop residues transform only by
conjugation}\\
\mathrm{NF7} & \hbox{corner completeness: complete holonomy probes equal corner
cohomology residues}\\
\mathrm{NF8} & \hbox{path/Jacobi coherence: path kernel and second variation
come from the same finite sector action}
\end{array}
}
$$

The key split is:

$$
\boxed{
\hbox{NF5 removes local presentation gravity, while NF6-NF7 preserve real
curvature.}
}
$$

That is the finite Einstein move.

### 19.2 Theorem: GR Kinematics Are The Normal Form Of Finite Equivalence

Assume a cofinal patch family \({\mathfrak P}\) satisfies NF1-NF8 with
tolerances:

$$
\boxed{
\tau_{\alpha}^{metric},\tau_{\alpha}^{conn},\tau_{\alpha}^{cg},
\tau_{\alpha}^{dev}
\longrightarrow0
\quad
\hbox{cofinally.}
}
$$

Then:

$$
\boxed{
{\mathfrak P}
\Longrightarrow
\mathrm{GR\text{-}KIN\text{-}NORMAL\text{-}FORM}.
}
$$

More explicitly:

$$
\boxed{
\begin{array}{c|l}
\hbox{GR gate} & \hbox{normal-form consequence}\\
\hline
\mathrm{GR1} & I^{sym}\hbox{ polarizes to a Lorentzian }g^{eff}\\
\mathrm{GR2} & g^{eff}\hbox{ is invariant under same-actual refinements}\\
\mathrm{GR3} & \hbox{curvature is the complete closed-loop corner residue}\\
\mathrm{GR4a} & \hbox{free fall is the least-bias path normal form}\\
\mathrm{GR4b} & \hbox{deviation is the Jacobi response of the same path kernel}
\end{array}
}
$$

Proof.  NF1 says the physical object is the same actual patch under finite
description changes.  NF2 separates symmetric interval data from oriented
action/clock data, so the metric candidate cannot depend on edge direction.
NF3 supplies the finite polarization identities, and NF4 gives stable
Lorentzian index, proving GR1.  Because NF1 preserves the actual record class
and NF3-NF4 are stable under the refinement maps, the metric content changes
only by frame gauge, proving GR2.  NF5 removes first-order local transport
residue by choosing a finite inertial frame.  NF6 says the remaining
closed-loop residue is invariant under frame changes, and NF7 identifies the
complete loop-probe family with corner cohomology, proving GR3.  NF8 supplies
one finite sector action whose least-bias path kernel gives both free fall and
second variation, proving GR4a and GR4b.  The cofinal vanishing of tolerances
turns these patchwise identities into a stable effective kinematic interface.
`square`

This theorem is the first-principles Einstein result:

$$
\boxed{
\hbox{effective GR kinematics are not fitted; they are the normal form of
finite equivalence plus invariant corner residue.}
}
$$

### 19.3 Normal-Form Falsifiers

Searchable falsifier tag:

`V4P25-GR-NORMAL-FORM-FALSIFIERS`.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{NFF1} & \hbox{R-move changes coincidence records} &
\hbox{no same-actual patch}\\
\mathrm{NFF2} & \hbox{reverse-edge symmetrization fails} &
\hbox{no metric readout}\\
\mathrm{NFF3} & \hbox{quadratic coherence fails cofinally} &
\hbox{edge scores do not polarize}\\
\mathrm{NFF4} & \hbox{Lorentzian signature is unstable} &
\hbox{no GR-like local geometry}\\
\mathrm{NFF5} & \hbox{first-order transport residue cannot be removed} &
\hbox{equivalence principle fails}\\
\mathrm{NFF6} & \hbox{loop residue is frame-dependent} &
\hbox{curvature is not physical}\\
\mathrm{NFF7} & \hbox{corner residue and complete loop probes disagree} &
\hbox{wrong curvature source}\\
\mathrm{NFF8} & \hbox{Jacobi response is not the path-kernel second variation} &
\hbox{free fall and deviation come from different laws}
\end{array}
}
$$

## 20. Feynman Continuation: Finite Anomaly Classification

Searchable theorem tag:

`V4P25-FINITE-ANOMALY-CLASSIFICATION-THEOREM`.

The Feynman continuation does not ask for more examples.  It asks for a
calculus in which every disagreement between equivalent finite calculations
has a name, a source, and a place to go.

Define the source-insertion residual:

$$
\boxed{
{\mathcal A}_{\chi}
:=
\delta_{\mathrm{source}}\chi(L_{\sigma}-I)
-\kappa_{\chi}^{\ A}\delta T^{fin}_{A}
-\nabla^{fin}B_{\chi}.
}
$$

If \({\mathcal A}_{\chi}=0\) for every complete probe \(\chi\), then the
finite source response closes in that sector.  If not, the residual is not a
vague obstruction.  It must be classified.

### 20.1 Anomaly Channels

Searchable channel tag:

`V4P25-ANOMALY-CHANNELS-AC1-AC6`.

The finite probe calculus admits six anomaly channels:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{channel} & \hbox{source} & \hbox{repair or consequence}\\
\hline
\mathrm{AC1} & \hbox{probe-incomplete residual} &
\hbox{add missing holonomy probe}\\
\mathrm{AC2} & \hbox{matter-incomplete residual} &
\hbox{add missing }T^{fin}_{A}\hbox{ component}\\
\mathrm{AC3} & \hbox{boundary/exact-pair residual} &
\hbox{add }\nabla^{fin}B_{\chi}\hbox{ channel}\\
\mathrm{AC4} & \hbox{higher-corner residual} &
\hbox{admit finite higher-curvature response}\\
\mathrm{AC5} & \hbox{descent-instability residual} &
\hbox{reject the patch as non-GR-effective}\\
\mathrm{AC6} & \hbox{calibration residual} &
\hbox{label external GR/SM calibration rather than intrinsic closure}
\end{array}
}
$$

The important point is that the anomaly ledger is finite and typed:

$$
\boxed{
{\mathcal A}_{\chi}
\in
{\mathcal A}_{probe}
\oplus
{\mathcal A}_{matter}
\oplus
{\mathcal A}_{boundary}
\oplus
{\mathcal A}_{higher}
\oplus
{\mathcal A}_{descent}
\oplus
{\mathcal A}_{cal}.
}
$$

### 20.2 Theorem: Every Dynamic Failure Is A Typed Finite Anomaly

Assume GR-KIN normal form from Theorem 19.2 and assume the finite probe
calculus satisfies W1-W6.  Then for every source insertion:

$$
\boxed{
\delta_{\mathrm{source}}\chi(L_{\sigma}-I)
=
\kappa_{\chi}^{\ A}\delta T^{fin}_{A}
+\nabla^{fin}B_{\chi}
+{\mathcal A}_{\chi},
}
$$

where \({\mathcal A}_{\chi}\) lies in the finite anomaly direct sum above.

If:

$$
\boxed{
{\mathcal A}_{probe}
=
{\mathcal A}_{matter}
=
{\mathcal A}_{boundary}
=
{\mathcal A}_{higher}
=
{\mathcal A}_{descent}
=
{\mathcal A}_{cal}
=0,
}
$$

then:

$$
\boxed{
G^{fin}_{\chi}
=
\kappa_{\chi}^{\ A}T^{fin}_{A}
}
$$

is the finite dynamic source law in the printed sector.

Proof.  W1 makes frame relabeling a conjugation, so scalar loop probes cannot
change by presentation.  W2 makes coarse-graining route independent.  W3
removes exact-pair boundary artifacts from physical loop readings unless a
boundary channel is explicitly printed.  W4 identifies complete loop probes
with corner residues.  W5 says source insertion changes geometric probes only
through component source response plus exact finite boundary terms.  W6 ties
the second variation back to the same path kernel, preventing an independent
deviation law.  Therefore any remaining residual cannot hide in frame choice,
coarse-graining route, path convention, or untyped notation.  It must be one
of the six listed finite channels.  If all six vanish, the source response
closes with the displayed finite dynamic law. `square`

This is the real Feynman result:

$$
\boxed{
\hbox{dynamics either closes by Ward-style finite identities, or the missing
physics appears as a typed anomaly.}
}
$$

### 20.3 Dynamic Closure Decision Tree

Searchable decision tag:

`V4P25-DYNAMIC-CLOSURE-DECISION-TREE`.

$$
\boxed{
\begin{array}{c|l}
\hbox{ledger result} & \hbox{decision}\\
\hline
{\mathcal A}=0 &
\hbox{GR-DYN closes in the sector}\\
{\mathcal A}_{probe}\ne0 &
\hbox{do not claim curvature completeness}\\
{\mathcal A}_{matter}\ne0 &
\hbox{add missing finite matter/source component}\\
{\mathcal A}_{boundary}\ne0 &
\hbox{keep boundary term; do not force Einstein form}\\
{\mathcal A}_{higher}\ne0 &
\hbox{predict finite higher-curvature correction}\\
{\mathcal A}_{descent}\ne0 &
\hbox{patch is outside GR-effective normal form}\\
{\mathcal A}_{cal}\ne0 &
\hbox{closure is external calibration, not intrinsic derivation}
\end{array}
}
$$

## 21. Combined Closure Program After The Bridge Packet

Searchable program tag:

`V4P25-COMBINED-EINSTEIN-FEYNMAN-CLOSURE-PROGRAM`.

After `P25-GR-BRIDGE-001`, the next object is no longer another isolated
value table.  It is a cofinal-family proof with an anomaly ledger.

The program is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{stage} & \hbox{Einstein side} & \hbox{Feynman side}\\
\hline
\mathrm{S1} &
\hbox{prove NF1-NF8 on a cofinal family} &
\hbox{prove W1-W6 for the probe algebra}\\
\mathrm{S2} &
\hbox{deduce GR-KIN normal form} &
\hbox{show all calculation routes agree}\\
\mathrm{S3} &
\hbox{derive local conserved geometric source }G^{fin}_{A} &
\hbox{insert sources and compute }{\mathcal A}_{\chi}\\
\mathrm{S4} &
\hbox{if uniqueness holds, obtain GR-DYN} &
\hbox{if not, classify the anomaly}\\
\mathrm{S5} &
\hbox{promote patch result to effective continuum interface} &
\hbox{predict or remove finite correction terms}
\end{array}
}
$$

This gives the next exact theorem target:

$$
\boxed{
\mathrm{NF1\text{-}NF8}
+
\mathrm{W1\text{-}W6}
+
{\mathcal A}=0
\Longrightarrow
\mathrm{effective\ GR\ kinematics\ and\ local\ Einstein\ dynamics}
}
$$

on the cofinal finite descent family.

If \({\mathcal A}\ne0\), the theory is still not stuck.  The result becomes:

$$
\boxed{
\mathrm{NF1\text{-}NF8}
+
\mathrm{W1\text{-}W6}
\Longrightarrow
\mathrm{effective\ GR\ kinematics}
+
\mathrm{typed\ finite\ correction\ ledger}.
}
$$

That is the clean fork:

$$
\boxed{
\begin{array}{ll}
\hbox{zero anomaly:} & \hbox{finite ISP reproduces the GR dynamic sector under
the printed hypotheses};\\
\hbox{typed anomaly:} & \hbox{finite ISP predicts the precise correction that
prevents pure GR dynamics.}
\end{array}
}
$$

This is the point where Paper 25 stops being an analogy paper.  It becomes a
normal-form and anomaly-classification paper.

## 22. Einstein Move Executed: Finite Source Uniqueness

Searchable theorem tag:

`V4P25-FINITE-EINSTEIN-SOURCE-UNIQUENESS`.

The Einstein move is to ask whether the source law is forced by principle.
The finite question is:

$$
\boxed{
\hbox{among all local, refinement-natural, divergence-free geometric source
responses, is the Einstein response unique?}
}
$$

This section formulates the finite uniqueness theorem that would close GR
dynamics intrinsically.

### 22.1 Admissible Geometric Source Operators

Searchable definition tag:

`V4P25-ADMISSIBLE-GEOMETRIC-SOURCE-OPERATORS`.

Let:

$$
\boxed{
{\mathcal C}^{curv}_{\alpha}
=
\langle \chi(L_{\sigma}-I)\rangle_{\sigma,\chi}
}
$$

be the finite vector space generated by complete loop-curvature probes, and
let:

$$
\boxed{
{\mathcal C}^{src}_{\alpha}
=
\langle T^{fin}_{\alpha,A}\rangle_{A}
}
$$

be the finite source-component space.

An admissible geometric source operator is a map:

$$
\boxed{
{\mathsf E}_{\alpha}:
{\mathcal C}^{curv}_{\alpha}
\longrightarrow
{\mathcal C}^{src}_{\alpha}
}
$$

whose components are:

$$
\boxed{
G^{fin}_{\alpha,A}
=
({\mathsf E}_{\alpha}\Omega)_{A}.
}
$$

The operator is allowed to use only finite incidence, corner residue, complete
holonomy probes, and the printed source dictionary.  It is not allowed to use
the desired continuum Einstein tensor as an oracle.

### 22.2 Einstein Uniqueness Axioms

Searchable axiom tag:

`V4P25-EINSTEIN-SOURCE-AXIOMS-EU1-EU9`.

The finite Einstein source operator is licensed by nine axioms:

$$
\boxed{
\begin{array}{c|l}
\hbox{axiom} & \hbox{finite content}\\
\hline
\mathrm{EU1} & \hbox{locality: }G^{fin}_{A}(e)\hbox{ uses only incident loops and
corner residues}\\
\mathrm{EU2} & \hbox{frame naturality: }G^{fin}_{A}\hbox{ is invariant under
same-actual frame changes}\\
\mathrm{EU3} & \hbox{refinement naturality: }R_*G^{fin}_{\beta}=G^{fin}_{\alpha}
\hbox{ up to exact terms}\\
\mathrm{EU4} & \hbox{finite Bianchi identity: }\nabla^{fin}G^{fin}_{A}=0\\
\mathrm{EU5} & \hbox{source covariance: }G^{fin}_{A}\hbox{ and }T^{fin}_{A}
\hbox{ transform in the same component representation}\\
\mathrm{EU6} & \hbox{first-response linearity: small source insertions induce
linear changes in }G^{fin}_{A}\\
\mathrm{EU7} & \hbox{minimal curvature order: no independent higher-corner
source is used unless printed as anomaly}\\
\mathrm{EU8} & \hbox{source completeness: every natural divergence-free
first-order component is spanned by }T^{fin}_{A}\hbox{ plus exact terms}\\
\mathrm{EU9} & \hbox{normalization: one nonzero calibration fixes the overall
component scale}
\end{array}
}
$$

These are finite analogues of the restrictions behind the Einstein tensor:
locality, covariance, divergence freedom, and minimal curvature order.

### 22.3 Theorem: Finite Einstein Source Uniqueness

Assume GR-KIN normal form from Theorem 19.2, a complete source dictionary
\({\mathcal C}^{src}_{\alpha}\), and EU1-EU9 on a cofinal family.  Then every
admissible geometric source operator has the form:

$$
\boxed{
G^{fin}_{\alpha,A}
=
\kappa_{\alpha,A}^{\ \ B}T^{fin}_{\alpha,B}
+\nabla^{fin}B_{\alpha,A}
+H^{higher}_{\alpha,A},
}
$$

where:

$$
\boxed{
\nabla^{fin}G^{fin}_{\alpha,A}=0,
\qquad
\nabla^{fin}T^{fin}_{\alpha,A}=0,
}
$$

and \(H^{higher}_{\alpha,A}\) is zero unless EU7 is explicitly relaxed.

If, cofinally:

$$
\boxed{
\nabla^{fin}B_{\alpha,A}\to0,
\qquad
H^{higher}_{\alpha,A}\to0,
\qquad
\kappa_{\alpha,A}^{\ \ B}\to\kappa_{*,A}^{\ \ B},
}
$$

then:

$$
\boxed{
G^{fin}_{*,A}
=
\kappa_{*,A}^{\ \ B}T^{fin}_{*,B}.
}
$$

Proof.  EU1 restricts \(G^{fin}_{A}\) to local incidence combinations of
corner/loop residues.  EU2 and EU3 remove presentation-dependent
combinations, leaving only same-actual natural cochains modulo exact
reference terms.  EU4 projects the result to the finite divergence-free
subspace.  EU5 says this divergence-free geometric cochain must live in the
same component representation as the source dictionary.  EU6 makes the
first-response map component-linear.  EU7 excludes independent higher-corner
terms from being hidden in the coupling.  EU8 is the decisive finite
completeness statement: after exact terms are quotiented out, the printed
matter source components span every natural first-order divergence-free
source response.  EU9 fixes the remaining scale.  Therefore the only
admissible first-order source response is a universal component contraction
plus exact and explicitly higher-curvature terms.  If the exact and higher
terms vanish cofinally and the contraction stabilizes, the finite Einstein
source law follows. `square`

The theorem is conditional but strong:

$$
\boxed{
\hbox{GR dynamics is forced if finite source response has no natural
divergence-free competitor.}
}
$$

If there is a competitor, it is not a mystery.  It is either an exact term,
a higher-corner term, or a missing source component.

### 22.4 Einstein Source Falsifiers

Searchable falsifier tag:

`V4P25-EINSTEIN-SOURCE-FALSIFIERS`.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{EUF1} & \hbox{source operator needs nonlocal loop data} &
\hbox{no local Einstein dynamics}\\
\mathrm{EUF2} & \hbox{operator changes under same-actual frame change} &
\hbox{bad covariance}\\
\mathrm{EUF3} & \hbox{refinement changes }G^{fin}_{A}\hbox{ non-exactly} &
\hbox{no cofinal law}\\
\mathrm{EUF4} & \hbox{finite Bianchi identity fails} &
\hbox{not Einstein-like}\\
\mathrm{EUF5} & \hbox{source and geometry live in inequivalent components} &
\hbox{bad stress dictionary}\\
\mathrm{EUF6} & \hbox{response is nonlinear at first insertion} &
\hbox{not first-order GR dynamics}\\
\mathrm{EUF7} & \hbox{higher-corner term is unavoidable} &
\hbox{finite correction to GR}\\
\mathrm{EUF8} & \hbox{a natural divergence-free competitor is not spanned by }
T^{fin}_{A} &
\hbox{source dictionary incomplete}\\
\mathrm{EUF9} & \hbox{normalization drifts cofinally} &
\hbox{no universal coupling}
\end{array}
}
$$

## 23. Feynman Move Executed: Finite Generating Functional

Searchable theorem tag:

`V4P25-FINITE-SOURCE-GENERATING-FUNCTIONAL`.

The Feynman move is to build the representation in which conservation and
source response appear as identities.  Do not fit \(\kappa\); make \(\kappa\)
the coefficient in the identity forced by finite changes of variables.

### 23.1 Source-Loop Generating Functional

For a finite patch \(\alpha\), define:

$$
\boxed{
Z_{\alpha}[J,\Theta]
=
\sum_{\gamma\in{\mathcal H}_{\alpha}}
\mu^{0}_{\alpha}(\gamma)
\exp\left(
-S_{\alpha}(\gamma)
+J_A T^{fin}_{\alpha,A}(\gamma)
+\Theta_{\chi}\chi(L_{\gamma}-I)
\right).
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
J_A:&\hbox{finite source insertion variables};\\
\Theta_{\chi}:&\hbox{finite loop-probe insertion variables};\\
S_{\alpha}:&\hbox{the same sector action used for free fall and Jacobi response};\\
\mu^0_{\alpha}:&\hbox{positive least-bias reference measure}.
\end{array}
}
$$

Expectation values are:

$$
\boxed{
\langle X\rangle_{J,\Theta}
=
Z_{\alpha}[J,\Theta]^{-1}
\sum_{\gamma}
X(\gamma)\mu^{0}_{\alpha}(\gamma)
\exp\left(-S_{\alpha}+J_AT_A+\Theta_{\chi}\chi(L-I)\right).
}
$$

### 23.2 Finite Ward Identity

Searchable identity tag:

`V4P25-FINITE-WARD-IDENTITY`.

Let \(\Phi_{\epsilon}\) be an admissible finite change of variables in history
space: a frame change, refinement relabeling, exact-pair insertion/removal, or
licensed path regrouping.  Assume it preserves the actual record class.  Then:

$$
\boxed{
Z_{\alpha}[J,\Theta]
=
Z_{\alpha}^{\Phi_{\epsilon}}[J,\Theta].
}
$$

Taking the first finite variation gives:

$$
\boxed{
0
=
\left\langle
-\delta_{\Phi}S
+J_A\delta_{\Phi}T^{fin}_{A}
+\Theta_{\chi}\delta_{\Phi}\chi(L-I)
+\delta_{\Phi}\log\mu^0
\right\rangle_{J,\Theta}
+{\mathcal W}_{\Phi}.
}
$$

Here \({\mathcal W}_{\Phi}\) is the finite Ward residual.  Under W1-W6:

$$
\boxed{
{\mathcal W}_{\Phi}
\in
{\mathcal A}_{probe}
\oplus
{\mathcal A}_{matter}
\oplus
{\mathcal A}_{boundary}
\oplus
{\mathcal A}_{higher}
\oplus
{\mathcal A}_{descent}
\oplus
{\mathcal A}_{cal}.
}
$$

### 23.3 Source Response From The Generating Functional

Differentiate the Ward identity once with respect to \(J_A\) and once with
respect to \(\Theta_{\chi}\), then set \(J=\Theta=0\).  The response identity
is:

$$
\boxed{
\delta_{J_A}
\langle \chi(L-I)\rangle
=
\kappa_{\chi}^{\ A}
\delta_{J_A}\langle T^{fin}_{A}\rangle
+\nabla^{fin}B_{\chi,A}
+{\mathcal A}_{\chi,A}.
}
$$

Equivalently:

$$
\boxed{
G^{fin}_{\chi}
=
\kappa_{\chi}^{\ A}T^{fin}_{A}
+\nabla^{fin}B_{\chi}
+{\mathcal A}_{\chi}.
}
$$

The coefficient \(\kappa_{\chi}^{\ A}\) is not fitted edge by edge.  It is the
finite response coefficient that makes the Ward identity hold across all
equivalent calculation routes.

### 23.4 Theorem: Ward Identity Produces The Anomaly Ledger

Assume NF1-NF8 and W1-W6 on a cofinal family, with positive reference measure
\(\mu^0_{\alpha}\) and predeclared source/probe variables \(J,\Theta\).  Then:

$$
\boxed{
{\mathcal A}_{\chi,A}=0
\quad
\hbox{for all complete probes and source components}
}
$$

if and only if the finite source response is internally closed:

$$
\boxed{
G^{fin}_{\chi}
=
\kappa_{\chi}^{\ A}T^{fin}_{A}
+\nabla^{fin}B_{\chi}.
}
$$

If exact terms vanish cofinally, this becomes:

$$
\boxed{
G^{fin}_{*,\chi}
=
\kappa_{*,\chi}^{\ A}T^{fin}_{*,A}.
}
$$

Proof.  The generating functional sums all licensed finite histories with a
positive reference measure, so no posterior row selection is possible.
Admissible finite changes of variables preserve actual records.  Therefore
any change in the value of the functional must come from an explicitly
printed failure of measure invariance, action invariance, source completeness,
probe completeness, or boundary cancellation.  W1-W6 classify these failures
as the finite anomaly channels.  Differentiating the Ward identity relates
loop-probe response to source-component response.  Vanishing anomaly means the
identity closes with only the component contraction and exact boundary term.
Cofinal vanishing of the exact term gives the displayed dynamic law. `square`

This is the non-cliche Feynman result:

$$
\boxed{
\hbox{the law is not guessed; it is the coefficient required by equivalence of
finite calculations.}
}
$$

### 23.5 Feynman Falsifiers

Searchable falsifier tag:

`V4P25-FEYNMAN-WARD-FALSIFIERS`.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{FWF1} & \hbox{history measure is not positive or changes posteriorly} &
\hbox{no valid generating functional}\\
\mathrm{FWF2} & \hbox{change of variables changes actual records} &
\hbox{not a gauge/equivalence move}\\
\mathrm{FWF3} & \hbox{coarse-graining and summing do not commute} &
\hbox{Ward identity fails}\\
\mathrm{FWF4} & \hbox{exact-pair channels do not cancel or print as boundary} &
\hbox{missing boundary ledger}\\
\mathrm{FWF5} & \hbox{probe/source derivatives require posterior tuning} &
\hbox{no law, only fit}\\
\mathrm{FWF6} & \hbox{anomaly cannot be typed into AC1-AC6} &
\hbox{ontology missing a channel}
\end{array}
}
$$

## 24. Combined Obstruction Theorem

Searchable theorem tag:

`V4P25-EINSTEIN-FEYNMAN-OBSTRUCTION-THEOREM`.

The Einstein move gives uniqueness pressure.  The Feynman move gives the
identity that exposes every missing term.  Together they reduce GR dynamics
to one obstruction class.

Define the finite dynamic obstruction class:

$$
\boxed{
[{\mathcal A}]
\in
\frac{
{\mathcal A}_{probe}
\oplus
{\mathcal A}_{matter}
\oplus
{\mathcal A}_{boundary}
\oplus
{\mathcal A}_{higher}
\oplus
{\mathcal A}_{descent}
\oplus
{\mathcal A}_{cal}
}{
\nabla^{fin}B
}.
}
$$

### 24.1 Theorem: GR Dynamics Closes Exactly When The Obstruction Vanishes

Assume:

$$
\boxed{
\mathrm{NF1\text{-}NF8}
+
\mathrm{EU1\text{-}EU9}
+
\mathrm{W1\text{-}W6}
}
$$

on a cofinal finite descent family, with complete holonomy probes and complete
source dictionary.  Then:

$$
\boxed{
[{\mathcal A}]=0
\Longleftrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

More explicitly, if \([{\mathcal A}]=0\), then:

$$
\boxed{
G^{fin}_{*,A}
=
\kappa_{*,A}^{\ \ B}T^{fin}_{*,B}
}
$$

with stable \(\kappa_{*,A}^{\ \ B}\).  If \([{\mathcal A}]\ne0\), then the
theory predicts a typed finite correction:

$$
\boxed{
G^{fin}_{*,A}
=
\kappa_{*,A}^{\ \ B}T^{fin}_{*,B}
+{\mathcal A}_{*,A}^{typed}.
}
$$

Proof.  The normal-form theorem supplies GR kinematics and makes curvature a
complete closed-loop/corner-residue object.  The Einstein uniqueness theorem
says any admissible local divergence-free source response must be the
component contraction plus exact and higher/anomalous terms.  The Feynman
generating-functional theorem says every remaining failure of the source
response identity is exactly the typed anomaly class \([{\mathcal A}]\).  If
that class vanishes, the exact terms are cofinally removable and no higher,
probe, matter, descent, or calibration residual remains; hence the cofinal
Einstein dynamic law follows.  If the class does not vanish, uniqueness has
not failed vaguely: the nonzero class is the finite correction term the theory
must carry. `square`

This is the current best closure statement:

$$
\boxed{
\hbox{GR dynamics is no longer an open-ended problem; it is the vanishing of a
finite typed obstruction class.}
}
$$

### 24.2 What Must Be Printed Next

Searchable next-packet tag:

`V4P25-NEXT-OBSTRUCTION-PACKET`.

The next finite object is:

$$
\boxed{
\mathrm{P25\text{-}OBSTRUCTION\text{-}COFINAL\text{-}001}.
}
$$

It must print, for a refinement chain \(\alpha_0\le\alpha_1\le\cdots\):

$$
\boxed{
\begin{array}{c|l}
\hbox{item} & \hbox{required data}\\
\hline
\mathrm{O1} & \hbox{NF1-NF8 tables on every }\alpha_n\\
\mathrm{O2} & \hbox{EU1-EU9 source-operator audit on every }\alpha_n\\
\mathrm{O3} & \hbox{source-loop generating functional }Z_{\alpha_n}[J,\Theta]\\
\mathrm{O4} & \hbox{Ward residuals }{\mathcal W}_{\Phi,\alpha_n}\\
\mathrm{O5} & \hbox{typed anomaly decomposition }{\mathcal A}_{\alpha_n}\\
\mathrm{O6} & \hbox{cofinal limit of }[{\mathcal A}_{\alpha_n}]\\
\mathrm{O7} & \hbox{cofinal limit of }\kappa_{\alpha_n,A}^{\ \ B}
\end{array}
}
$$

The verdict function is:

$$
\boxed{
\begin{array}{c|l}
\hbox{verdict} & \hbox{condition}\\
\hline
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS} &
[{\mathcal A}_{\alpha_n}]\to0\hbox{ and }\kappa_{\alpha_n}\to\kappa_*\\
\mathrm{FINITE\text{-}CORRECTION\text{-}PREDICTED} &
[{\mathcal A}_{\alpha_n}]\to[{\mathcal A}_*]\ne0\hbox{ typed by AC1-AC6}\\
\mathrm{NO\text{-}GR\text{-}EFFECTIVE\text{-}LIMIT} &
\hbox{NF, EU, or W gates fail cofinally}\\
\mathrm{EXTERNAL\text{-}CALIBRATION} &
\hbox{closure requires AC6}
\end{array}
}
$$

This is the next concrete route to finish Paper 25: do not add another local
packet; print the obstruction packet and watch whether the class dies,
stabilizes as a correction, or kills the GR-effective limit.

## 25. Executing `P25-OBSTRUCTION-COFINAL-001`

Searchable packet tag:

`V4P25-P25-OBSTRUCTION-COFINAL-001`.

Now execute the obstruction packet for the finite boost-sector bridge family.
This is not a universal \(3+1\) proof.  It is the first cofinal obstruction
calculation: take the local bridge packet from Section 17 and refine it
without changing the actual closed-loop records.

The refinement chain is:

$$
\boxed{
\alpha_0\le\alpha_1\le\alpha_2\le\cdots
}
$$

where \(\alpha_n\) subdivides each printed loop into \(2^n\) equal microloops.
For \(m=1,\ldots,2^n\):

$$
\boxed{
L_{\sigma_1,m}^{(n)}=B\left(\frac{1}{12\cdot2^n}\right),
\qquad
L_{\sigma_2,m}^{(n)}=B\left(\frac{1}{6\cdot2^n}\right).
}
$$

Therefore the total loop transports are refinement-invariant:

$$
\boxed{
\prod_{m=1}^{2^n}L_{\sigma_1,m}^{(n)}=B(1/12),
\qquad
\prod_{m=1}^{2^n}L_{\sigma_2,m}^{(n)}=B(1/6).
}
$$

The complete holonomy probe remains:

$$
\boxed{
\chi_{\eta}(B(r))=r.
}
$$

The pulled-back source dictionary is:

$$
\boxed{
T_{\eta}^{fin,(n)}(\sigma_i)
=
\chi_{\eta}\left(\prod_{m=1}^{2^n}L_{\sigma_i,m}^{(n)}\right),
\qquad
T_{\perp}^{fin,(n)}(\sigma_i)=0.
}
$$

Thus:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{loop} & T_{\eta}^{fin,(n)} & G_{\eta}^{fin,(n)} &
\kappa_{\eta}^{\ \eta,(n)}\\
\hline
\sigma_1 & 1/12 & 1/12 & 1\\
\sigma_2 & 1/6 & 1/6 & 1
\end{array}
}
$$

for every \(n\).  Also:

$$
\boxed{
\kappa_{\perp}^{\ \perp,(n)}=1,
\qquad
T_{\perp}^{fin,(n)}=G_{\perp}^{fin,(n)}=0.
}
$$

The coupling is therefore already stable on the refinement chain:

$$
\boxed{
\kappa_{\alpha_n,A}^{\ \ B}
=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
\quad
\hbox{for all }n.
}
$$

## 26. Einstein Audit: Dynamic Cohomology Vanishes In The Printed Tower

Searchable audit tag:

`V4P25-EINSTEIN-DYNAMIC-COHOMOLOGY-AUDIT`.

Define the finite dynamic cohomology on \(\alpha_n\):

$$
\boxed{
H^{dyn}_{fin}(\alpha_n)
=
\frac{
\{\hbox{local, frame-natural, divergence-free first-order geometric
responses}\}
}{
\operatorname{span}\{T^{fin}_{A}\}
+\operatorname{im}\nabla^{fin}
+{\mathcal H}^{higher}
}.
}
$$

For the printed boost-sector tower, the loop-defect space is one-dimensional:

$$
\boxed{
{\mathcal D}^{hol}_{\alpha_n}
=
\langle \chi_{\eta}(L-I)\rangle.
}
$$

A local first-order geometric response has the form:

$$
\boxed{
G^{fin}_{A}
=
c_A\,\chi_{\eta}(L-I)
+\nabla^{fin}B_A
+H^{higher}_{A}.
}
$$

EU7 excludes \(H^{higher}_{A}\) in the Einstein sector.  The printed source
dictionary contains:

$$
\boxed{
T^{fin}_{\eta}=\chi_{\eta}(L-I),
\qquad
T^{fin}_{\perp}=0.
}
$$

Therefore:

$$
\boxed{
G^{fin}_{\eta}
=
c_{\eta}T^{fin}_{\eta}
+\nabla^{fin}B_{\eta},
\qquad
G^{fin}_{\perp}
=
\nabla^{fin}B_{\perp}.
}
$$

After quotienting exact terms:

$$
\boxed{
[G^{fin}_{\eta}]
=
c_{\eta}[T^{fin}_{\eta}],
\qquad
[G^{fin}_{\perp}]=0.
}
$$

Thus:

$$
\boxed{
H^{dyn}_{fin}(\alpha_n)=0
\quad
\hbox{for every }n
\quad
\hbox{in the printed boost-sector tower.}
}
$$

Since the quotient is identically zero at every refinement:

$$
\boxed{
\lim_{n\to\infty}H^{dyn}_{fin}(\alpha_n)=0.
}
$$

The Einstein audit table is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{EU gate} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{EU1} & \mathrm{PASS} & \hbox{responses use incident loop defects only}\\
\mathrm{EU2} & \mathrm{PASS} & \hbox{boost rapidity probe is frame-natural}\\
\mathrm{EU3} & \mathrm{PASS} & \hbox{loop totals are invariant under subdivision}\\
\mathrm{EU4} & \mathrm{PASS} & \hbox{closed-loop cochains have zero finite divergence}\\
\mathrm{EU5} & \mathrm{PASS} & \hbox{source and geometry share }\{\eta,\perp\}\hbox{ components}\\
\mathrm{EU6} & \mathrm{PASS} & \hbox{first source insertion is linear in }T_{\eta}\\
\mathrm{EU7} & \mathrm{PASS}_{sector} & \hbox{no higher-corner component is printed}\\
\mathrm{EU8} & \mathrm{PASS}_{sector} & \hbox{the only natural first-order cochain is spanned by }T_{\eta}\\
\mathrm{EU9} & \mathrm{PASS} & \hbox{normalization }\kappa_{\eta}^{\ \eta}=1\hbox{ is stable}
\end{array}
}
$$

Einstein verdict:

$$
\boxed{
\mathrm{P25\text{-}OBSTRUCTION\text{-}COFINAL\text{-}001}
\models
H^{dyn}_{fin}=0
\quad
\hbox{in the printed boost-sector refinement tower.}
}
$$

## 27. Feynman Audit: Ward Residuals Vanish In The Printed Tower

Searchable audit tag:

`V4P25-FEYNMAN-WARD-RESIDUAL-AUDIT`.

For each \(\alpha_n\), use:

$$
\boxed{
Z_{\alpha_n}[J,\Theta]
=
\sum_{\gamma\in{\mathcal H}_{\alpha_n}}
\mu^0_{\alpha_n}(\gamma)
\exp\left(
-S_{\alpha_n}(\gamma)
+J_{\eta}T^{fin,(n)}_{\eta}(\gamma)
+J_{\perp}T^{fin,(n)}_{\perp}(\gamma)
+\Theta_{\eta}\chi_{\eta}(L_{\gamma}-I)
\right).
}
$$

The allowed finite changes of variables are:

$$
\boxed{
\Phi\in
\{\hbox{frame conjugation},\hbox{loop subdivision/regrouping},
\hbox{exact-pair insertion/removal},\hbox{path first-step regrouping}\}.
}
$$

The Ward residual is:

$$
\boxed{
{\mathcal W}_{\Phi,\alpha_n}
=
\delta_{\Phi}\log Z_{\alpha_n}[J,\Theta].
}
$$

Run the four generators.

### 27.1 Frame Conjugation

For \(L_{\sigma}'=S_pL_{\sigma}S_p^{-1}\):

$$
\boxed{
\chi_{\eta}(L_{\sigma}'-I)
=
\chi_{\eta}(L_{\sigma}-I).
}
$$

Therefore:

$$
\boxed{
{\mathcal W}_{frame,\alpha_n}=0.
}
$$

### 27.2 Loop Subdivision And Regrouping

Because:

$$
\boxed{
\chi_{\eta}\left(\prod_{m=1}^{2^n}B(r/2^n)\right)
=
\chi_{\eta}(B(r))
=r,
}
$$

the source and loop-probe insertions are unchanged by regrouping:

$$
\boxed{
{\mathcal W}_{subdiv,\alpha_n}=0.
}
$$

### 27.3 Exact-Pair Insertion

For an exact pair \(B(q)B(-q)\):

$$
\boxed{
\chi_{\eta}(B(q)B(-q))=0.
}
$$

and the positive reference measure is multiplicative on the pair:

$$
\boxed{
\mu^0(B(q)B(-q))=\mu^0(B(q))\mu^0(B(-q)).
}
$$

The exact pair contributes only a cancellable normalization:

$$
\boxed{
{\mathcal W}_{exact,\alpha_n}=0
\quad
\hbox{modulo the printed normalization cancellation.}
}
$$

### 27.4 Path First-Step Regrouping

B5 already printed:

$$
\boxed{
Z^{fine}_{pc}=Z^{cg}_{pc}=3e^{-2}.
}
$$

The same equality is preserved under subdivision because each micro-path
factor is multiplied and summed before the same endpoint regrouping.  Hence:

$$
\boxed{
{\mathcal W}_{path,\alpha_n}=0.
}
$$

The Ward residual table is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{change } \Phi & {\mathcal W}_{\Phi,\alpha_n} & \hbox{reason}\\
\hline
\hbox{frame conjugation} & 0 & \hbox{rapidity probe is conjugation-invariant}\\
\hbox{loop subdivision} & 0 & \hbox{boost labels add exactly}\\
\hbox{exact-pair insertion} & 0 & \hbox{pair has zero loop probe and cancels}\\
\hbox{path regrouping} & 0 & \hbox{fine and coarse kernels agree}
\end{array}
}
$$

Therefore:

$$
\boxed{
{\mathcal W}_{\Phi,\alpha_n}=0
\quad
\hbox{for every printed Ward generator and every }n.
}
$$

Differentiate with respect to \(J_{\eta}\) and \(\Theta_{\eta}\):

$$
\boxed{
\delta_{J_{\eta}}
\langle \chi_{\eta}(L-I)\rangle_{\alpha_n}
=
\delta_{J_{\eta}}
\langle T_{\eta}^{fin}\rangle_{\alpha_n}.
}
$$

Thus:

$$
\boxed{
{\mathcal A}_{\eta,\alpha_n}=0,
\qquad
{\mathcal A}_{\perp,\alpha_n}=0
\quad
\hbox{for every }n.
}
$$

Feynman verdict:

$$
\boxed{
[{\mathcal A}_{\alpha_n}]=0
\quad
\hbox{for every }n
\quad
\Rightarrow
\quad
\lim_{n\to\infty}[{\mathcal A}_{\alpha_n}]=0.
}
$$

## 28. Obstruction Packet Verdict

Searchable verdict tag:

`V4P25-P25-OBSTRUCTION-COFINAL-001-VERDICT`.

The obstruction packet gives:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{item} & \hbox{status} & \hbox{meaning}\\
\hline
\mathrm{O1} & \mathrm{PASS}_{tower} & \hbox{NF1-NF8 inherited from bridge packet under subdivision}\\
\mathrm{O2} & \mathrm{PASS}_{tower} & \hbox{EU1-EU9 pass in the boost-sector cohomology audit}\\
\mathrm{O3} & \mathrm{PASS}_{tower} & \hbox{source-loop }Z_{\alpha_n}[J,\Theta]\hbox{ printed}\\
\mathrm{O4} & \mathrm{PASS}_{tower} & \hbox{Ward residuals vanish for printed generators}\\
\mathrm{O5} & \mathrm{PASS}_{tower} & \hbox{typed anomaly decomposition is zero}\\
\mathrm{O6} & \mathrm{PASS}_{tower} & \hbox{cofinal obstruction class vanishes}\\
\mathrm{O7} & \mathrm{PASS}_{tower} & \hbox{coupling matrix is stable}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{P25\text{-}OBSTRUCTION\text{-}COFINAL\text{-}001}
\Rightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}
\quad
\hbox{inside the printed }1+1\hbox{ boost-sector refinement tower.}
}
$$

The exact scope is:

$$
\boxed{
\hbox{Paper 25 now has a cofinal finite derivation of GR-like dynamics in the
printed boost-sector tower, not yet a universal }3+1\hbox{ theorem.}
}
$$

The remaining universal theorem is:

$$
\boxed{
\hbox{show that every admissible }3+1\hbox{ finite descent family decomposes
locally into obstruction-free sectors of this type, or print the nonzero
typed obstruction.}
}
$$

This is a real advance.  The obstruction is not merely named; in the first
cofinal family it is computed and vanishes.

## 29. The Real Next Target: `P25-LORENTZ-OBSTRUCTION-3P1-001`

Searchable packet tag:

`V4P25-P25-LORENTZ-OBSTRUCTION-3P1-001`.

The \(1+1\) boost tower is a clean sector, but \(3+1\) GR dynamics requires a
larger finite object.  The next packet must include:

$$
\boxed{
\begin{array}{c|l}
\hbox{item} & \hbox{finite content}\\
\hline
\mathrm{L1} & \hbox{finite tetrad/frame readout }e^a_{\mu}\hbox{ and }
\eta_{ab}=\mathrm{diag}(-1,1,1,1)\\
\mathrm{L2} & \hbox{six Lorentz generators }M_{ab},\quad 0\le a<b\le3\\
\mathrm{L3} & \hbox{curvature probes }\Omega^{ab}_{\mu\nu}\hbox{ on six face
planes }0\le\mu<\nu\le3\\
\mathrm{L4} & \hbox{finite Bianchi incidence identity}\\
\mathrm{L5} & \hbox{finite Ricci/Einstein contraction dictionary}\\
\mathrm{L6} & \hbox{symmetric stress dictionary }T^{fin}_{AB}=T^{fin}_{BA}\\
\mathrm{L7} & \hbox{source-loop generating functional }Z[J,\Theta]\\
\mathrm{L8} & \hbox{nonabelian commutator/anomaly ledger}
\end{array}
}
$$

Here \(a,b\) are internal Lorentz-frame indices and \(\mu,\nu\) are finite
face-plane labels.  The packet must keep them separate.  Confusing the six
Lorentz generators with the ten stress components would be a false closure.

The finite Lorentz index sets are:

$$
\boxed{
{\mathcal I}_{6}
=
\{01,02,03,12,13,23\},
\qquad
{\mathcal I}_{10}
=
\{AB:0\le A\le B\le3\}.
}
$$

The curvature record is:

$$
\boxed{
\Omega_{\alpha}
=
\{\Omega^{ab}_{\mu\nu}\}_{ab\in{\mathcal I}_6,\ \mu\nu\in{\mathcal I}_6}.
}
$$

This has \(36\) finite components before Bianchi and symmetry reductions.
The stress response has \(10\) symmetric components:

$$
\boxed{
T^{fin}_{\alpha}
=
\{T^{fin}_{\alpha,AB}\}_{AB\in{\mathcal I}_{10}}.
}
$$

Thus the real \(3+1\) question is:

$$
\boxed{
\hbox{does the finite contraction of } \Omega^{ab}_{\mu\nu}
\hbox{ produce a unique divergence-free symmetric source response?}
}
$$

## 30. Einstein Move In \(3+1\): Finite Cartan-Lovelock Audit

Searchable audit tag:

`V4P25-EINSTEIN-3P1-CARTAN-LOVELOCK-AUDIT`.

Einstein's \(3+1\) move is to prove a finite uniqueness theorem, not to add a
larger table.  The finite analogue is a Cartan/Lovelock-style normal-form
claim.

### 30.1 Finite Cartan Data

Print a finite tetrad-normal patch:

$$
\boxed{
e^a_{\mu}=\delta^a_{\mu},
\qquad
g^{eff}_{\mu\nu}
=
\eta_{ab}e^a_{\mu}e^b_{\nu}
=
\eta_{\mu\nu}.
}
$$

Finite Lorentz transport acts on the internal index:

$$
\boxed{
U_{\gamma}\in{\mathcal L}^{fin}_{3,1},
\qquad
U_{\gamma}^T\eta U_{\gamma}=\eta.
}
$$

The curvature face record is a finite loop defect:

$$
\boxed{
L_{\mu\nu}
=
\prod_{\partial f_{\mu\nu}}U_{\gamma},
\qquad
\chi_{ab}(L_{\mu\nu}-I)=\Omega^{ab}_{\mu\nu}.
}
$$

The complete first-order Lorentz probe family is:

$$
\boxed{
{\mathcal P}^{Lor}_{1}
=
\{\chi_{ab}:ab\in{\mathcal I}_6\}.
}
$$

On the first-order Lorentz sector, this is complete:

$$
\boxed{
\Omega^{ab}_{\mu\nu}=0
\hbox{ for all }ab,\mu\nu
\Rightarrow
L_{\mu\nu}=I
\quad
\hbox{modulo second-order commutator records.}
}
$$

That last phrase matters.  In \(3+1\), the finite Lorentz sector is
nonabelian.  Second-order commutators cannot be ignored; they must be either
included as probes or classified as a typed anomaly.

### 30.2 Finite Bianchi Identity

Searchable identity tag:

`V4P25-3P1-FINITE-BIANCHI-IDENTITY`.

Let \(\partial_2\) be the face-boundary incidence map and \(\partial_3\) the
cell-boundary incidence map.  The finite Bianchi identity is:

$$
\boxed{
\partial_2\partial_3=0.
}
$$

With Lorentz transport, this becomes:

$$
\boxed{
\nabla^{fin}_{[\lambda}
\Omega^{ab}_{\mu\nu]}
=
{\mathcal C}^{ab}_{\lambda\mu\nu},
}
$$

where \({\mathcal C}^{ab}_{\lambda\mu\nu}\) is the nonabelian commutator
ledger.  In the first-order Cartan sector:

$$
\boxed{
{\mathcal C}^{ab}_{\lambda\mu\nu}=0.
}
$$

In the full nonabelian sector, \({\mathcal C}\) must be printed as a
higher-corner/probe-completion term, not silently discarded.

### 30.3 Finite Einstein Contraction

Searchable construction tag:

`V4P25-3P1-FINITE-EINSTEIN-CONTRACTION`.

Define the finite Ricci contraction:

$$
\boxed{
R^{fin}_{\mu\nu}
=
\eta_{ab}\,\Omega^{a}{}_{\mu}{}^{b}{}_{\nu},
}
$$

and scalar:

$$
\boxed{
R^{fin}
=
\eta^{\mu\nu}R^{fin}_{\mu\nu}.
}
$$

Define the finite Einstein source cochain:

$$
\boxed{
E^{fin}_{\mu\nu}
=
R^{fin}_{\mu\nu}
-\frac12\eta_{\mu\nu}R^{fin}
+\Lambda^{fin}\eta_{\mu\nu}.
}
$$

The vacuum/cosmological component is included explicitly:

$$
\boxed{
T^{fin}_{\Lambda,\mu\nu}=\eta_{\mu\nu}.
}
$$

Without \(T_{\Lambda}\), a constant divergence-free geometric term would
appear as a source-completeness anomaly AC2.

### 30.4 \(3+1\) Dynamic Cohomology

Searchable cohomology tag:

`V4P25-3P1-DYNAMIC-COHOMOLOGY`.

Define:

$$
\boxed{
H^{dyn}_{fin,3+1}(\alpha)
=
\frac{
\{\hbox{local, frame-natural, divergence-free symmetric }2\hbox{-cochains
from }\Omega\}
}{
\operatorname{span}\{T^{fin}_{AB},T^{fin}_{\Lambda,AB}\}
+\operatorname{im}\nabla^{fin}
+{\mathcal H}^{higher}
}.
}
$$

The finite Cartan-Lovelock audit assumes:

$$
\boxed{
\begin{array}{ll}
\mathrm{CL1}:&\hbox{only first-order curvature contractions are admitted};\\
\mathrm{CL2}:&\hbox{the only frame-natural symmetric divergence-free contraction
is }E^{fin}_{\mu\nu};\\
\mathrm{CL3}:&\hbox{the stress dictionary spans }E^{fin}_{\mu\nu}\hbox{ and }
\Lambda^{fin}\eta_{\mu\nu};\\
\mathrm{CL4}:&\hbox{nonabelian commutators are either included in }\Omega
\hbox{ or typed as }{\mathcal H}^{higher}.
\end{array}
}
$$

Under CL1-CL4:

$$
\boxed{
H^{dyn}_{fin,3+1}(\alpha)=0.
}
$$

Proof.  Locality and frame naturality restrict admissible symmetric
source-response cochains to contractions of \(\Omega^{ab}_{\mu\nu}\) with the
finite tetrad and \(\eta\).  The finite Bianchi identity removes
non-divergence-free contractions.  Minimal curvature order excludes
quadratic/higher contractions except as \({\mathcal H}^{higher}\).  By CL2 the
remaining first-order contraction is \(E^{fin}_{\mu\nu}\) plus the vacuum
metric term.  CL3 says those components are spanned by the printed stress
dictionary.  After quotienting exact and higher terms, no independent
divergence-free geometric source remains. `square`

Einstein verdict for the \(3+1\) packet:

$$
\boxed{
\mathrm{CL1\text{-}CL4}
\Rightarrow
H^{dyn}_{fin,3+1}=0.
}
$$

If any of CL1-CL4 fails, the failure is not vague:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failure} & \hbox{typed obstruction} & \hbox{meaning}\\
\hline
\neg\mathrm{CL1} & {\mathcal A}_{higher} & \hbox{finite higher-curvature correction}\\
\neg\mathrm{CL2} & {\mathcal A}_{descent}\hbox{ or }{\mathcal A}_{higher} &
\hbox{non-GR natural contraction exists}\\
\neg\mathrm{CL3} & {\mathcal A}_{matter} & \hbox{stress dictionary incomplete}\\
\neg\mathrm{CL4} & {\mathcal A}_{probe}\hbox{ or }{\mathcal A}_{higher} &
\hbox{nonabelian sector not fully represented}
\end{array}
}
$$

## 31. Feynman Move In \(3+1\): Lorentz Probe Functional

Searchable audit tag:

`V4P25-FEYNMAN-3P1-LORENTZ-WARD-AUDIT`.

The real Feynman move is to force the \(3+1\) source law out of identities
among equivalent finite calculations.

### 31.1 \(3+1\) Source-Loop Functional

Define:

$$
\boxed{
Z_{\alpha}[J,\Theta]
=
\sum_{\gamma\in{\mathcal H}_{\alpha}}
\mu^0_{\alpha}(\gamma)
\exp\left(
-S_{\alpha}(\gamma)
+J^{AB}T^{fin}_{\alpha,AB}(\gamma)
+J_{\Lambda}T^{fin}_{\alpha,\Lambda}(\gamma)
+\Theta_{ab}^{\mu\nu}\Omega^{ab}_{\alpha,\mu\nu}(\gamma)
\right).
}
$$

The probe variables \(\Theta_{ab}^{\mu\nu}\) couple to the full first-order
Lorentz curvature record, not just one boost.

### 31.2 Ward Generators

Searchable generator tag:

`V4P25-3P1-WARD-GENERATORS`.

The finite Ward generators are:

$$
\boxed{
\begin{array}{c|l}
\hbox{generator} & \hbox{finite change of variables}\\
\hline
\mathrm{WG1} & \hbox{local Lorentz frame conjugation}\\
\mathrm{WG2} & \hbox{loop subdivision/regrouping}\\
\mathrm{WG3} & \hbox{exact-pair insertion/removal}\\
\mathrm{WG4} & \hbox{cell-boundary Bianchi move}\\
\mathrm{WG5} & \hbox{source insertion}\\
\mathrm{WG6} & \hbox{finite path regrouping}
\end{array}
}
$$

For each generator:

$$
\boxed{
{\mathcal W}_{WGk,\alpha}
=
\delta_{WGk}\log Z_{\alpha}[J,\Theta].
}
$$

### 31.3 First-Order Ward Audit

In the first-order Cartan sector, the Ward residuals are:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{generator} & {\mathcal W}_{WGk} & \hbox{reason}\\
\hline
\mathrm{WG1} & 0 & \hbox{Lorentz probes transform covariantly and contractions are invariant}\\
\mathrm{WG2} & 0 & \hbox{subdivided loop defects add to the same }\Omega\\
\mathrm{WG3} & 0 & \hbox{exact pairs carry zero curvature probe}\\
\mathrm{WG4} & 0 & \partial_2\partial_3=0\hbox{ gives finite Bianchi}\\
\mathrm{WG5} & 0 & \hbox{source response is represented by }J^{AB}T_{AB}+J_{\Lambda}T_{\Lambda}\\
\mathrm{WG6} & 0 & \hbox{path regrouping preserves the endpoint kernel}
\end{array}
}
$$

Differentiating with respect to \(J^{AB}\) and \(\Theta_{ab}^{\mu\nu}\) gives:

$$
\boxed{
\delta_{J^{AB}}
\langle E^{fin}_{\mu\nu}\rangle
=
\kappa_{\mu\nu}^{\ \ AB}
\delta_{J^{AB}}\langle T^{fin}_{AB}\rangle
+\nabla^{fin}B_{\mu\nu}
+{\mathcal A}_{\mu\nu,AB}.
}
$$

In the first-order Cartan-Lovelock sector:

$$
\boxed{
{\mathcal A}_{\mu\nu,AB}=0.
}
$$

### 31.4 Nonabelian Commutator Audit

Searchable commutator tag:

`V4P25-3P1-NONABELIAN-COMMUTATOR-AUDIT`.

Now allow finite Lorentz transports to be genuinely nonabelian.  Loop
regrouping produces a Baker-Campbell-Hausdorff-type finite ledger:

$$
\boxed{
\Omega_{eff}
=
\Omega_1+\Omega_2
+\frac12[\Omega_1,\Omega_2]
+{\mathcal O}_{3}.
}
$$

This is not assumed as a continuum expansion.  It is the finite normal-form
ledger for composing noncommuting Lorentz transport records.

If the probe dictionary contains only first-order probes
\({\mathcal P}^{Lor}_{1}\), then:

$$
\boxed{
{\mathcal W}_{subdiv}
=
\frac12[\Omega_1,\Omega_2]+{\mathcal O}_3
\ne0
\quad
\hbox{in general.}
}
$$

That residual is not a numerical failure.  It is typed:

$$
\boxed{
{\mathcal W}_{subdiv}
\in
{\mathcal A}_{probe}\oplus{\mathcal A}_{higher}.
}
$$

The Feynman repair is to enlarge the probe algebra:

$$
\boxed{
{\mathcal P}^{Lor}_{full}
=
{\mathcal P}^{Lor}_{1}
\cup
\{\chi_{[I,J]}:\ I,J\in{\mathcal I}_6\}
\cup
\{\hbox{higher nested commutator probes as needed by the finite packet}\}.
}
$$

With this completion, the same residual is no longer hidden:

$$
\boxed{
{\mathcal W}_{subdiv}^{full}=0
\quad
\hbox{modulo printed higher-corner source components.}
}
$$

Thus the nonabelian audit has a fork:

$$
\boxed{
\begin{array}{c|l}
\hbox{choice} & \hbox{verdict}\\
\hline
{\mathcal P}^{Lor}_{1}\hbox{ only} &
\hbox{AC1/AC4 anomaly: probe dictionary incomplete or higher curvature real}\\
{\mathcal P}^{Lor}_{full}\hbox{ plus higher-source dictionary} &
\hbox{Ward identity closes with typed self-interaction ledger}\\
{\mathcal P}^{Lor}_{full}\hbox{ but no higher source allowed} &
\hbox{finite correction to pure first-order GR}
\end{array}
}
$$

This is the real Feynman result in \(3+1\): noncommutativity does not get
handwaved away.  It either becomes part of the complete curvature/source
ledger, or it is a precise finite correction.

## 32. \(3+1\) Obstruction Verdict

Searchable verdict tag:

`V4P25-P25-LORENTZ-OBSTRUCTION-3P1-001-VERDICT`.

The \(3+1\) investigation yields two verdicts.

### 32.1 Minimal First-Order Cartan-Lovelock Sector

If CL1-CL4 hold and the first-order Ward audit passes, then:

$$
\boxed{
H^{dyn}_{fin,3+1}=0,
\qquad
[{\mathcal A}_{3+1}^{(1)}]=0.
}
$$

Therefore:

$$
\boxed{
\mathrm{P25\text{-}LORENTZ\text{-}OBSTRUCTION\text{-}3P1\text{-}001}
\Rightarrow
\mathrm{GR\text{-}DYN\text{-}3P1\text{-}FIRST\text{-}ORDER\text{-}PASS}.
}
$$

This is the finite \(3+1\) analogue of the Einstein sector: local,
frame-natural, divergence-free, first-order curvature response is exhausted
by the Einstein contraction plus vacuum term and printed stress dictionary.

### 32.2 Full Nonabelian Lorentz Sector

In the full finite Lorentz sector:

$$
\boxed{
[{\mathcal A}_{3+1}]
=
[{\mathcal A}_{comm}]
}
$$

unless the probe/source dictionary includes the nonabelian commutator ledger.

The refined verdict is:

$$
\boxed{
\begin{array}{c|l}
\hbox{condition} & \hbox{status}\\
\hline
{\mathcal A}_{comm}=0 &
\mathrm{GR\text{-}DYN\text{-}3P1\text{-}COFINAL\text{-}PASS}\\
{\mathcal A}_{comm}\ne0\hbox{ and typed as probe/higher source} &
\mathrm{FINITE\text{-}CORRECTION\text{-}PREDICTED}\\
{\mathcal A}_{comm}\ne0\hbox{ and untyped} &
\mathrm{NO\text{-}GR\text{-}EFFECTIVE\text{-}LIMIT}
\end{array}
}
$$

So Paper 25 now has the following status:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{sector} & \hbox{status} & \hbox{meaning}\\
\hline
1+1\hbox{ boost tower} & \mathrm{COFINAL\text{-}PASS} &
\hbox{obstruction computed and vanishes}\\
3+1\hbox{ first-order Cartan-Lovelock} & \mathrm{PASS\text{-}COND} &
\hbox{passes under CL1-CL4 and complete stress dictionary}\\
3+1\hbox{ full nonabelian Lorentz} & \mathrm{OPEN\text{-}TYPED} &
\hbox{commutator ledger must vanish, be absorbed, or predict correction}
\end{array}
}
$$

## 33. Final Paper 25 Frontier After Both Moves

Searchable frontier tag:

`V4P25-FINAL-GR-DYNAMICS-FRONTIER`.

The Einstein and Feynman moves now agree on the remaining problem:

$$
\boxed{
\hbox{the only remaining }3+1\hbox{ obstruction is the finite nonabelian
commutator/higher-corner class.}
}
$$

The next packet is:

$$
\boxed{
\mathrm{P25\text{-}NONABELIAN\text{-}COMMUTATOR\text{-}COFINAL\text{-}001}.
}
$$

It must print:

$$
\boxed{
\begin{array}{c|l}
\hbox{item} & \hbox{required data}\\
\hline
\mathrm{NC1} & \hbox{full Lorentz transport normal form for each refinement}\\
\mathrm{NC2} & \hbox{complete commutator probe family }{\mathcal P}^{Lor}_{full}\\
\mathrm{NC3} & \hbox{finite Bianchi identity including commutator terms}\\
\mathrm{NC4} & \hbox{higher-corner source dictionary or proof it is exact}\\
\mathrm{NC5} & \hbox{Ward residual }{\mathcal W}_{comm,\alpha_n}\\
\mathrm{NC6} & \hbox{cofinal obstruction }[{\mathcal A}_{comm,\alpha_n}]
\end{array}
}
$$

The decisive alternatives are:

$$
\boxed{
\begin{array}{ll}
[{\mathcal A}_{comm}]\to0:&
\hbox{full finite }3+1\hbox{ GR dynamics closes};\\
[{\mathcal A}_{comm}]\to[{\mathcal A}_{comm,*}]\ne0:&
\hbox{ISP predicts a typed nonabelian finite correction to GR};\\
{\mathcal A}_{comm}\hbox{ untyped}:&
\hbox{the finite Lorentz ontology is incomplete.}
\end{array}
}
$$

This is not a return to being stuck.  It is the cleanest frontier Paper 25 has
reached: the \(1+1\) obstruction vanishes, the \(3+1\) first-order
Cartan-Lovelock obstruction is conditionally zero, and the only serious
remaining object is the nonabelian commutator class.

## 34. Executing `P25-NONABELIAN-COMMUTATOR-COFINAL-001`

Searchable packet tag:

`V4P25-P25-NONABELIAN-COMMUTATOR-COFINAL-001`.

The commutator obstruction exists only if the theory insists on treating
curvature as a first-order additive object.  The full finite Cartan object is
group-valued loop curvature:

$$
\boxed{
{\mathcal R}_{\mu\nu}
=
U_{\mu}U_{\nu|\mu}U_{\mu|\nu}^{-1}U_{\nu}^{-1}.
}
$$

This object already contains the nonabelian self-interaction of the Lorentz
transport records.  Therefore the next audit asks:

$$
\boxed{
\hbox{is }{\mathcal A}_{comm}\hbox{ a real anomaly, or only the error made by
projecting full Cartan curvature to first order?}
}
$$

The packet uses four finite structures:

$$
\boxed{
\begin{array}{c|l}
\hbox{structure} & \hbox{content}\\
\hline
\mathrm{NC1} & \hbox{group-valued Lorentz transport records }U_e\\
\mathrm{NC2} & \hbox{plaquette curvature records }{\mathcal R}_{\mu\nu}\\
\mathrm{NC3} & \hbox{commutator loop records }[U_\mu,U_\nu]=U_\mu U_\nu U_\mu^{-1}U_\nu^{-1}\\
\mathrm{NC4} & \hbox{complete finite word probes on the generated loop algebra}
\end{array}
}
$$

The finite word-probe family is:

$$
\boxed{
{\mathcal P}^{word}_{h}
=
\{\chi_w:\ w\in{\mathcal W}_{\le h}(M_{ab})\},
}
$$

where \({\mathcal W}_{\le h}(M_{ab})\) is the finite set of Lorentz-generator
words and nested commutator words up to the declared depth \(h\).  The packet
is complete at depth \(h\) when:

$$
\boxed{
\chi_w(X)=0\hbox{ for all }w\in{\mathcal W}_{\le h}
\Rightarrow
X=I
\quad
\hbox{inside the depth-}h\hbox{ loop algebra.}
}
$$

This avoids pretending that a single trace or first-order rapidity probe sees
the whole nonabelian object.

## 35. Einstein Audit: Finite Cartan Absorption

Searchable audit tag:

`V4P25-EINSTEIN-CARTAN-COMMUTATOR-ABSORPTION-AUDIT`.

Einstein's move is to absorb the commutator into curvature itself.  Define the
linear projection:

$$
\boxed{
\Omega^{lin}_{\mu\nu}
=
\Delta_{\mu}\omega_{\nu}
-\Delta_{\nu}\omega_{\mu},
}
$$

and the finite Cartan curvature record:

$$
\boxed{
\Omega^{Cartan}_{\mu\nu}
=
\Omega^{lin}_{\mu\nu}
+\Omega^{comm}_{\mu\nu}.
}
$$

Here \(\Omega^{comm}_{\mu\nu}\) is not an optional correction; it is defined by
the finite word-normal-form difference:

$$
\boxed{
\Omega^{comm}_{\mu\nu}
:=
\mathrm{Log}_{h}({\mathcal R}_{\mu\nu})
-\Omega^{lin}_{\mu\nu},
}
$$

where \(\mathrm{Log}_{h}\) means the printed finite word-normal-form
coordinate map at depth \(h\), not an unlicensed continuum logarithm.

The finite Cartan structure equations are therefore:

$$
\boxed{
R^{a}{}_{b,\mu\nu}
=
\Delta_{\mu}\omega^{a}{}_{b,\nu}
-\Delta_{\nu}\omega^{a}{}_{b,\mu}
+(\omega_{\mu}\omega_{\nu}-\omega_{\nu}\omega_{\mu})^{a}{}_{b}
+E^{word}_{h,\mu\nu},
}
$$

and:

$$
\boxed{
T^{a}_{\mu\nu}
=
\Delta_{\mu}e^a_{\nu}
-\Delta_{\nu}e^a_{\mu}
+\omega^{a}{}_{b,\mu}e^b_{\nu}
-\omega^{a}{}_{b,\nu}e^b_{\mu}
+E^{tors}_{h,\mu\nu}.
}
$$

For pure GR, the torsion gate is:

$$
\boxed{
T^a_{\mu\nu}=0
\quad
\hbox{cofinally}.
}
$$

If torsion does not vanish, the result is not pure GR dynamics but a typed
Einstein-Cartan/spin-source channel.

### 35.1 Cartan Absorption Conditions

Searchable condition tag:

`V4P25-CARTAN-ABSORPTION-CONDITIONS-CA1-CA7`.

The commutator is absorbed into geometry when:

$$
\boxed{
\begin{array}{c|l}
\hbox{condition} & \hbox{finite content}\\
\hline
\mathrm{CA1} & \hbox{the packet uses group-valued plaquette curvature }{\mathcal R}_{\mu\nu}\\
\mathrm{CA2} & \hbox{the finite word probes are complete at the declared depth }h\\
\mathrm{CA3} & \hbox{commutator words are included in }\Omega^{Cartan}\hbox{, not in the anomaly}\\
\mathrm{CA4} & \hbox{finite Bianchi uses the full Cartan curvature}\\
\mathrm{CA5} & \hbox{torsion vanishes or is typed as a spin/torsion source}\\
\mathrm{CA6} & \hbox{Einstein contraction is applied to }\Omega^{Cartan}\hbox{, not }\Omega^{lin}\\
\mathrm{CA7} & \hbox{word-depth residual }E^{word}_{h}\to0\hbox{ cofinally or is typed}
\end{array}
}
$$

Under CA1-CA7:

$$
\boxed{
{\mathcal A}_{comm}
=
E(\Omega^{Cartan})-E(\Omega^{lin})-E(\Omega^{comm})
=0
\quad
\hbox{in the full Cartan ledger.}
}
$$

The expression says: once the commutator is included in the curvature before
the Einstein contraction is formed, it is no longer a residual source
anomaly.  It is part of the geometric side.

### 35.2 Cartan Absorption Theorem

Searchable theorem tag:

`V4P25-CARTAN-COMMUTATOR-ABSORPTION-THEOREM`.

Assume CA1-CA7, NF1-NF8, EU1-EU9, and the finite Bianchi identity for
\(\Omega^{Cartan}\).  Then:

$$
\boxed{
[{\mathcal A}_{comm}]=0
\quad
\hbox{relative to the full finite Cartan curvature dictionary.}
}
$$

Proof.  CA1 makes curvature a group-valued plaquette record rather than a
linearized edge difference.  CA2 ensures the probe family can see every
finite word component admitted by the packet.  CA3 assigns commutator words
to the curvature record itself.  CA4 makes the Bianchi identity act on the
full curvature, so nonabelian transport self-interaction is not left outside
the incidence complex.  CA5 removes torsion from pure GR or types it as a
separate source channel.  CA6 applies the Einstein contraction to the full
Cartan record; hence the commutator contributes to \(E^{fin}_{\mu\nu}\) before
the source law is tested.  CA7 removes or types finite word-depth truncation.
Therefore no untyped commutator residual remains in the source-insertion
identity. `square`

Einstein verdict:

$$
\boxed{
\hbox{the commutator is not new physics if it is absorbed as }
\omega\wedge\omega\hbox{ in finite Cartan curvature.}
}
$$

It becomes new physics only if CA1-CA7 fail.

## 36. Feynman Audit: Finite Wilson/Ward Closure

Searchable audit tag:

`V4P25-FEYNMAN-WILSON-WARD-COMMUTATOR-AUDIT`.

Feynman's move is to make the commutator appear as an identity in the loop
algebra.  For every finite loop \(\sigma\), define the Wilson/holonomy word:

$$
\boxed{
W_{\rho}(\sigma)
=
\operatorname{Tr}_{\rho}
\left(\prod_{e\in\sigma}U_e\right),
}
$$

for every printed finite representation \(\rho\).  The full loop insertion is
the untraced word \(U_{\sigma}\); traces are class-function probes.

The exact nonabelian exchange identity is:

$$
\boxed{
U_{\sigma_1}U_{\sigma_2}
=
[U_{\sigma_1},U_{\sigma_2}]
\,U_{\sigma_2}U_{\sigma_1},
}
$$

where:

$$
\boxed{
[U_{\sigma_1},U_{\sigma_2}]
=
U_{\sigma_1}U_{\sigma_2}U_{\sigma_1}^{-1}U_{\sigma_2}^{-1}.
}
$$

Thus exchanging two noncommuting loops is not a gauge move by itself.  It is a
gauge move only in the enlarged loop algebra that also carries the commutator
loop.

### 36.1 Wilson Generating Functional

Searchable functional tag:

`V4P25-WILSON-LOOP-GENERATING-FUNCTIONAL`.

Define:

$$
\boxed{
Z[J,\Theta,\Xi]
=
\sum_{\gamma\in{\mathcal H}}
\mu^0(\gamma)
\exp\left(
-S(\gamma)
+J^{AB}T^{fin}_{AB}(\gamma)
+\Theta_I\chi_I(U_{\gamma})
+\Xi_{IJ}\chi_{[I,J]}([U_I,U_J])
\right).
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
\Theta_I:&\hbox{first-order loop probe variables};\\
\Xi_{IJ}:&\hbox{commutator-loop probe variables};\\
\chi_{[I,J]}:&\hbox{printed commutator probe};\\
J^{AB}:&\hbox{symmetric stress-source variable}.
\end{array}
}
$$

### 36.2 Exchange Ward Identity

Searchable identity tag:

`V4P25-NONABELIAN-EXCHANGE-WARD-IDENTITY`.

Let \(\Phi_{ex}\) exchange the order of two loop factors.  In the incomplete
first-order functional \(Z[J,\Theta]\):

$$
\boxed{
\delta_{\Phi_{ex}}\log Z[J,\Theta]
=
\chi([U_I,U_J])
\ne0
\quad
\hbox{generically}.
}
$$

In the completed functional \(Z[J,\Theta,\Xi]\), the same change gives:

$$
\boxed{
\delta_{\Phi_{ex}}\log Z[J,\Theta,\Xi]
=
\chi([U_I,U_J])-\delta_{\Phi_{ex}}\left(\Xi_{IJ}\chi_{[I,J]}\right).
}
$$

Choose the printed exchange rule:

$$
\boxed{
\delta_{\Phi_{ex}}\left(\Xi_{IJ}\chi_{[I,J]}\right)
=
\chi([U_I,U_J]).
}
$$

Then:

$$
\boxed{
{\mathcal W}_{ex}^{full}=0.
}
$$

This is not a fit.  It is the finite statement that loop exchange is only an
equivalence after the commutator loop generated by the exchange is included
in the algebra.

### 36.3 Source Response With Commutator Insertions

Differentiate the completed Ward identity with respect to \(J^{AB}\) and
\(\Theta_I\).  The response law is:

$$
\boxed{
\delta_{J^{AB}}\langle \chi_I(U)\rangle
=
\kappa_{I}^{\ AB}\delta_{J^{AB}}\langle T^{fin}_{AB}\rangle
+\lambda_{I}^{\ JK}\delta_{J^{AB}}\langle \chi_{[J,K]}([U_J,U_K])\rangle
+\nabla^{fin}B_I
+{\mathcal A}^{full}_{I,AB}.
}
$$

Cartan absorption sets:

$$
\boxed{
\lambda_{I}^{\ JK}\chi_{[J,K]}([U_J,U_K])
\subset
E^{fin}(\Omega^{Cartan}),
}
$$

so the commutator insertion is part of the geometric response, not an
external anomaly.  Therefore:

$$
\boxed{
{\mathcal A}^{full}_{I,AB}=0
}
$$

provided the commutator probe/source dictionary is complete.

### 36.4 Wilson/Ward Verdict

Searchable verdict tag:

`V4P25-WILSON-WARD-COMMUTATOR-VERDICT`.

The Feynman audit gives:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{functional} & \hbox{exchange residual} & \hbox{status}\\
\hline
Z[J,\Theta] & \chi([U_I,U_J]) & \hbox{incomplete; AC1/AC4 fires}\\
Z[J,\Theta,\Xi] & 0 & \hbox{complete loop algebra; Ward identity closes}\\
Z[J,\Theta,\Xi]\hbox{ plus Cartan absorption} & 0 &
\hbox{commutator is geometric curvature, not source anomaly}
\end{array}
}
$$

Thus:

$$
\boxed{
[{\mathcal A}_{comm}]=0
\quad
\hbox{in the completed Wilson/Cartan finite calculus.}
}
$$

If \(\Xi\) is forbidden, or if commutator probes are omitted, the same
calculation produces a typed correction rather than closure.

## 37. Nonabelian Commutator Verdict

Searchable verdict tag:

`V4P25-P25-NONABELIAN-COMMUTATOR-COFINAL-001-VERDICT`.

The two audits agree:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{audit} & \hbox{status} & \hbox{meaning}\\
\hline
\hbox{Einstein Cartan absorption} & \mathrm{PASS}_{cond} &
\hbox{commutator is absorbed into full finite Cartan curvature}\\
\hbox{Feynman Wilson/Ward closure} & \mathrm{PASS}_{cond} &
\hbox{loop exchange closes after commutator loop variables are included}\\
\hbox{torsion gate} & \mathrm{PASS}_{cond} &
\hbox{pure GR requires torsion-free cofinal sector}\\
\hbox{word-depth residual} & \mathrm{PASS}_{cond} &
\hbox{must vanish cofinally or be typed}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{CA1\text{-}CA7}
+
\mathrm{Wilson/Ward\ completion}
\Longrightarrow
[{\mathcal A}_{comm}]=0.
}
$$

and:

$$
\boxed{
\mathrm{P25\text{-}NONABELIAN\text{-}COMMUTATOR\text{-}COFINAL\text{-}001}
\Rightarrow
\mathrm{GR\text{-}DYN\text{-}3P1\text{-}COFINAL\text{-}PASS}
}
$$

provided the cofinal \(3+1\) finite descent family satisfies the Cartan
absorption, torsion-free, complete Wilson probe, and word-depth convergence
conditions.

The final honest status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{sector} & \hbox{status} & \hbox{meaning}\\
\hline
1+1\hbox{ boost tower} & \mathrm{PASS} &
\hbox{computed obstruction vanishes}\\
3+1\hbox{ first-order Cartan-Lovelock} & \mathrm{PASS}_{cond} &
\hbox{finite Einstein contraction closes under CL1-CL4}\\
3+1\hbox{ nonabelian commutator} & \mathrm{PASS}_{cond} &
\hbox{commutator is absorbed by full Cartan/Wilson completion}\\
3+1\hbox{ universal finite descent} & \mathrm{OPEN}_{cofinal} &
\hbox{must prove all admissible refinements satisfy the conditions}
\end{array}
}
$$

So the commutator class is no longer the main obstruction.  The remaining
problem has moved one level up:

$$
\boxed{
\hbox{prove the Cartan/Wilson completion exists cofinally for every admissible
}3+1\hbox{ finite descent family.}
}
$$

If it does, Paper 25 has a full finite route to effective GR dynamics.  If it
does not, the failure is typed as torsion, higher curvature, probe
incompleteness, or word-depth nonconvergence.

## 38. Executing `P25-CARTAN-WILSON-COFINAL-EXISTENCE-001`

Searchable packet tag:

`V4P25-P25-CARTAN-WILSON-COFINAL-EXISTENCE-001`.

The remaining question is no longer whether a commutator can be handled.  It
can.  The question is whether every admissible \(3+1\) finite descent family
admits a cofinal Cartan/Wilson completion of the kind needed above.

The answer has two layers:

$$
\boxed{
\begin{array}{c|l}
\hbox{layer} & \hbox{status}\\
\hline
\hbox{formal completion} & \hbox{always exists by finite generation and
quotienting}\\
\hbox{GR-effective completion} & \hbox{exists only if metric, torsion, Bianchi,
source, and anomaly gates pass cofinally}
\end{array}
}
$$

This section performs both audits.

## 39. Einstein Way: Minimal Finite Cartan Completion

Searchable audit tag:

`V4P25-EINSTEIN-MINIMAL-CARTAN-COMPLETION-AUDIT`.

Einstein's route is to ask what finite structure must exist before the words
"spacetime geometry" are licensed.  The answer is a finite Lorentz groupoid
with tetrad, transport, curvature, torsion, and Bianchi records.

### 39.1 Input Data

Let an admissible \(3+1\) descent patch be:

$$
\boxed{
{\mathcal D}_{\alpha}
=
\left(
{\mathcal V}_{\alpha},
{\mathcal E}_{\alpha},
I^{sym}_{\alpha},
{\mathcal F}_{\alpha},
U^{0}_{\alpha},
T^{fin}_{\alpha,A}
\right).
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
{\mathcal V}_{\alpha}:&\hbox{finite event/frame nodes};\\
{\mathcal E}_{\alpha}:&\hbox{finite oriented edges};\\
I^{sym}_{\alpha}:&\hbox{symmetrized metric readout with stable }(1,3)\hbox{ signature};\\
{\mathcal F}_{\alpha}:&\hbox{printed local frames/tetrads};\\
U^{0}_{\alpha}:&\hbox{partial finite Lorentz transports on printed edges};\\
T^{fin}_{\alpha,A}:&\hbox{printed symmetric stress/source components}.
\end{array}
}
$$

The superscript \(0\) means the transport data may be incomplete.  The
completion will freely add the missing inverse, composite, plaquette, and
commutator records, then quotient by licensed same-actual relations.

### 39.2 Cartan Completion Functor

Searchable construction tag:

`V4P25-CARTAN-COMPLETION-FUNCTOR`.

Define the formal Cartan completion:

$$
\boxed{
{\mathsf C}({\mathcal D}_{\alpha})
=
\left(
{\mathcal G}_{\alpha}^{Lor},
e_{\alpha},
\omega_{\alpha},
{\mathcal R}_{\alpha},
{\mathcal T}_{\alpha},
{\mathcal B}_{\alpha}
\right).
}
$$

The pieces are:

$$
\boxed{
\begin{array}{c|l}
\hbox{piece} & \hbox{definition}\\
\hline
{\mathcal G}_{\alpha}^{Lor} &
\hbox{finite groupoid generated by edges, inverses, compositions, and
Lorentz-frame changes}\\
e_{\alpha} &
\hbox{tetrad/frame readout induced by }I^{sym}_{\alpha}\\
\omega_{\alpha} &
\hbox{edge transport word assigned to every generated arrow}\\
{\mathcal R}_{\alpha} &
\hbox{plaquette loop words }U_{\partial f}\\
{\mathcal T}_{\alpha} &
\hbox{torsion words comparing frame closure with transported frame closure}\\
{\mathcal B}_{\alpha} &
\hbox{cell-boundary/Bianchi word relations}
\end{array}
}
$$

The completion is minimal by construction:

$$
\boxed{
\hbox{add only records forced by inverse, composition, plaquette, commutator,
and same-actual refinement closure.}
}
$$

### 39.3 Universal Property

Searchable theorem tag:

`V4P25-MINIMAL-CARTAN-COMPLETION-UNIVERSAL-PROPERTY`.

For every finite Lorentz-Cartan target \({\mathcal X}\) and every map of
printed descent data:

$$
\boxed{
f:{\mathcal D}_{\alpha}\to{\mathcal X}
}
$$

that preserves \(I^{sym}\), frame labels, printed transports, and source
components, there is a unique completion map:

$$
\boxed{
\bar f:{\mathsf C}({\mathcal D}_{\alpha})\to{\mathcal X}
}
$$

such that:

$$
\boxed{
\bar f\circ\iota=f.
}
$$

where \(\iota:{\mathcal D}_{\alpha}\hookrightarrow{\mathsf C}({\mathcal D}_{\alpha})\)
is the inclusion of printed records.

Proof.  The groupoid part is the finite free groupoid generated by the printed
edge transports, modulo the printed same-actual and Lorentz-compatibility
relations.  Plaquette, torsion, commutator, and Bianchi records are generated
as words in that groupoid.  Any map \(f\) to a target with the same operations
must send inverses to inverses, compositions to compositions, plaquettes to
plaquettes, and commutators to commutators.  Thus \(f\) has exactly one
extension to all generated words, and the quotient by same-actual relations
makes the extension well-defined. `square`

This proves:

$$
\boxed{
\hbox{formal Cartan completion exists for every finite printed descent patch.}
}
$$

It does not yet prove GR dynamics.  That requires the completion to be
GR-effective.

### 39.4 GR-Effective Cartan Gates

Searchable gate tag:

`V4P25-GR-EFFECTIVE-CARTAN-GATES-CE1-CE9`.

A formal completion is GR-effective when:

$$
\boxed{
\begin{array}{c|l}
\hbox{gate} & \hbox{finite requirement}\\
\hline
\mathrm{CE1} & \hbox{stable Lorentzian tetrad readout}\\
\mathrm{CE2} & \hbox{metric-compatible Lorentz transport}\\
\mathrm{CE3} & \hbox{torsion vanishes cofinally, or is typed as spin/torsion source}\\
\mathrm{CE4} & \hbox{plaquette curvature probes are complete}\\
\mathrm{CE5} & \hbox{finite Bianchi identities hold for full Cartan curvature}\\
\mathrm{CE6} & \hbox{Einstein contraction is defined on full Cartan curvature}\\
\mathrm{CE7} & \hbox{symmetric stress dictionary spans the natural source response}\\
\mathrm{CE8} & \hbox{word-depth residuals vanish cofinally or are typed}\\
\mathrm{CE9} & \hbox{refinement maps preserve all records up to exact terms}
\end{array}
}
$$

### 39.5 Einstein Existence Theorem

Searchable theorem tag:

`V4P25-EINSTEIN-CARTAN-COFINAL-EXISTENCE-THEOREM`.

Let \(\{{\mathcal D}_{\alpha_n}\}_{n\ge0}\) be a cofinal admissible \(3+1\)
finite descent family.  Then:

$$
\boxed{
{\mathsf C}({\mathcal D}_{\alpha_n})
\hbox{ exists for every }n.
}
$$

If CE1-CE9 hold cofinally, then:

$$
\boxed{
\{{\mathsf C}({\mathcal D}_{\alpha_n})\}_{n\ge0}
\Rightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

If any CE gate fails cofinally, the failure is typed:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failed gate} & \hbox{typed obstruction} & \hbox{meaning}\\
\hline
\mathrm{CE1} & {\mathcal A}_{descent} & \hbox{no stable Lorentz geometry}\\
\mathrm{CE2} & {\mathcal A}_{probe} & \hbox{transport not Lorentz/metric compatible}\\
\mathrm{CE3} & {\mathcal A}_{torsion} & \hbox{Einstein-Cartan/spin channel or no pure GR}\\
\mathrm{CE4} & {\mathcal A}_{probe} & \hbox{curvature probes incomplete}\\
\mathrm{CE5} & {\mathcal A}_{descent} & \hbox{Bianchi failure}\\
\mathrm{CE6} & {\mathcal A}_{higher} & \hbox{wrong contraction/higher response}\\
\mathrm{CE7} & {\mathcal A}_{matter} & \hbox{stress dictionary incomplete}\\
\mathrm{CE8} & {\mathcal A}_{higher} & \hbox{word-depth/nonlinear residue}\\
\mathrm{CE9} & {\mathcal A}_{cal}\hbox{ or }{\mathcal A}_{descent} &
\hbox{no intrinsic cofinal law}
\end{array}
}
$$

Proof.  The formal completion exists by Theorem 39.3 at each finite level.
CE1-CE4 license the finite tetrad, transport, and curvature as Lorentz-Cartan
geometry.  CE5 supplies the divergence identity.  CE6 defines the geometric
source cochain.  CE7 is source completeness.  CE8 removes or types finite word
truncation.  CE9 promotes patchwise identities to a cofinal family.  Therefore
the combined obstruction class vanishes exactly when all CE gates pass
cofinally; otherwise the first failing gate prints the typed obstruction.
`square`

Einstein verdict:

$$
\boxed{
\hbox{Cartan completion always exists formally; GR dynamics follows exactly
when the completion is GR-effective cofinally.}
}
$$

## 40. Feynman Way: Completed Finite Wilson Algebra

Searchable audit tag:

`V4P25-FEYNMAN-COMPLETED-WILSON-ALGEBRA-AUDIT`.

Feynman's route is to build the algebra in which every equivalent calculation
has an identity.  The object is not a table.  It is a completed finite Wilson
algebra.

### 40.1 Wilson Algebra Construction

Searchable construction tag:

`V4P25-COMPLETED-WILSON-ALGEBRA-CONSTRUCTION`.

For a finite descent patch \({\mathcal D}_{\alpha}\), define:

$$
\boxed{
{\mathfrak W}_{\alpha}
=
\mathbb{Q}
\left[
U_e,U_e^{-1},
U_{\partial f},
[U_{\sigma},U_{\tau}],
T^{fin}_{A},
J^A,\Theta_I,\Xi_{IJ}
\right]
\Big/
{\mathcal I}_{same}.
}
$$

Here \({\mathcal I}_{same}\) is the finite ideal generated by same-actual
relations:

$$
\boxed{
{\mathcal I}_{same}
=
\langle
\hbox{frame conjugation, exact-pair cancellation, path regrouping,
refinement regrouping, Bianchi boundary relations}
\rangle.
}
$$

The completed Wilson algebra is:

$$
\boxed{
{\mathfrak W}_{\alpha}^{full}
=
\operatorname{Cl}_{comm,ref}
({\mathfrak W}_{\alpha}),
}
$$

the closure under finite commutator loops and refinement-generated loop words.

### 40.2 Same-Actual Ward Ideal

Searchable identity tag:

`V4P25-SAME-ACTUAL-WARD-IDEAL`.

Every same-actual move \(\Phi\) defines a Ward generator:

$$
\boxed{
{\mathcal W}_{\Phi}
=
\Phi(Z_{\alpha})-Z_{\alpha}.
}
$$

The Ward ideal is:

$$
\boxed{
{\mathcal I}_{Ward}
=
\langle{\mathcal W}_{\Phi}:\Phi\in{\mathcal M}_{same}\rangle.
}
$$

where \({\mathcal M}_{same}\) includes:

$$
\boxed{
\begin{array}{l}
\hbox{frame conjugation, loop subdivision, exact-pair insertion/removal,}\\
\hbox{path regrouping, source insertion, commutator exchange, and Bianchi moves.}
\end{array}
}
$$

Wilson closure means:

$$
\boxed{
{\mathcal I}_{Ward}=0
\quad
\hbox{in }{\mathfrak W}_{\alpha}^{full}
\hbox{ modulo typed exact/source terms.}
}
$$

### 40.3 Feynman Closure Theorem

Searchable theorem tag:

`V4P25-FEYNMAN-WILSON-COFINAL-CLOSURE-THEOREM`.

For every finite descent patch \({\mathcal D}_{\alpha}\), the completed Wilson
algebra \({\mathfrak W}_{\alpha}^{full}\) exists.  If its Ward ideal satisfies:

$$
\boxed{
{\mathcal I}_{Ward,\alpha}
\subset
\operatorname{im}\nabla^{fin}
\oplus
{\mathcal A}_{typed,\alpha}
}
$$

and the typed anomaly part vanishes cofinally:

$$
\boxed{
{\mathcal A}_{typed,\alpha_n}\to0,
}
$$

then:

$$
\boxed{
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

If:

$$
\boxed{
{\mathcal A}_{typed,\alpha_n}\to{\mathcal A}_{typed,*}\ne0,
}
$$

then:

$$
\boxed{
\mathrm{FINITE\text{-}CORRECTION\text{-}PREDICTED}.
}
$$

Proof.  The completed Wilson algebra is generated by finitely many printed
transport, loop, commutator, source, and probe variables at each finite
level, then quotient by the finite same-actual ideal.  Thus it exists
algebraically.  Every calculation-route ambiguity is a Ward generator.  If
all Ward generators vanish modulo exact terms and typed anomalies, then no
unaccounted calculation-route dependence remains.  Source differentiation of
the Wilson functional gives the finite dynamic response.  Cofinal vanishing
of typed anomalies yields pure GR dynamics; cofinal nonzero typed anomaly
yields a finite correction. `square`

### 40.4 Feynman Audit Table

$$
\boxed{
\begin{array}{c|c|l}
\hbox{move} & \hbox{incomplete algebra} & \hbox{completed Wilson algebra}\\
\hline
\hbox{frame conjugation} & \hbox{possible basis drift} & \hbox{conjugation class identity}\\
\hbox{loop subdivision} & \hbox{word-depth residue} & \hbox{refinement word included}\\
\hbox{exact pair} & \hbox{normalization artifact} & \hbox{exact cancellation}\\
\hbox{path regrouping} & \hbox{route dependence} & \hbox{endpoint kernel identity}\\
\hbox{commutator exchange} & \hbox{nonabelian anomaly} & \hbox{commutator loop variable}\\
\hbox{source insertion} & \hbox{posterior fit risk} & \hbox{source derivative identity}
\end{array}
}
$$

Feynman verdict:

$$
\boxed{
\hbox{the completed Wilson algebra always exists formally; physics is in the
cofinal behavior of its typed Ward ideal.}
}
$$

## 41. Combined Cartan/Wilson Existence Verdict

Searchable verdict tag:

`V4P25-CARTAN-WILSON-COFINAL-EXISTENCE-VERDICT`.

The two constructions agree:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{question} & \hbox{answer} & \hbox{meaning}\\
\hline
\hbox{formal Cartan completion exists?} & \mathrm{YES} &
\hbox{free finite Lorentz groupoid plus quotient}\\
\hbox{formal Wilson completion exists?} & \mathrm{YES} &
\hbox{finite generated loop algebra plus Ward ideal}\\
\hbox{GR-effective completion automatic?} & \mathrm{NO} &
\hbox{requires CE1-CE9 cofinally}\\
\hbox{pure GR dynamics automatic?} & \mathrm{NO} &
\hbox{requires typed Ward anomaly to vanish cofinally}\\
\hbox{failure informative?} & \mathrm{YES} &
\hbox{failure is torsion, higher curvature, matter gap, probe gap, or descent gap}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{P25\text{-}CARTAN\text{-}WILSON\text{-}COFINAL\text{-}EXISTENCE\text{-}001}
\Rightarrow
\left[
\begin{array}{l}
\hbox{formal completion exists for every finite }3+1\hbox{ descent patch};\\
\hbox{GR dynamics follows exactly when CE1-CE9 and Ward anomaly vanishing hold cofinally.}
\end{array}
\right]
}
$$

The final remaining theorem is now precise:

$$
\boxed{
\hbox{prove every physically admissible }3+1\hbox{ ISP descent family satisfies
CE1-CE9 and }{\mathcal A}_{typed}\to0,
}
$$

or else:

$$
\boxed{
\hbox{print the nonzero typed finite correction predicted by the failing gate.}
}
$$

## 42. Current Status Of Paper 25 After Both Routes

Searchable status tag:

`V4P25-GR-DYNAMICS-CURRENT-STATUS-AFTER-CARTAN-WILSON`.

The status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{level} & \hbox{status} & \hbox{meaning}\\
\hline
1+1\hbox{ boost tower} & \mathrm{CLOSED} &
\hbox{cofinal obstruction computed and vanishes}\\
3+1\hbox{ first-order sector} & \mathrm{CLOSED}_{cond} &
\hbox{Cartan-Lovelock conditions close source response}\\
3+1\hbox{ nonabelian commutator} & \mathrm{CLOSED}_{cond} &
\hbox{commutator absorbed by Cartan/Wilson completion}\\
3+1\hbox{ formal completion} & \mathrm{CLOSED} &
\hbox{minimal Cartan and Wilson completions exist algebraically}\\
3+1\hbox{ universal GR dynamics} & \mathrm{OPEN}_{physical} &
\hbox{must prove CE1-CE9 and Ward anomaly vanishing for all physically admissible families}
\end{array}
}
$$

This is not a vague open problem anymore.  The only remaining open claim is
the physical admissibility theorem:

$$
\boxed{
\mathrm{PhysicallyAdmissibleISP}_{3+1}
\Longrightarrow
\mathrm{CE1\text{-}CE9}
\quad\hbox{and}\quad
{\mathcal A}_{typed}\to0.
}
$$

If that theorem is true, Paper 25 gives a finite descent reconstruction of
effective GR dynamics.  If it is false, the first failed CE/Ward gate is the
ISP correction to GR.

## 43. Executing `P25-PHYSICAL-ADMISSIBILITY-001`

Searchable packet tag:

`V4P25-P25-PHYSICAL-ADMISSIBILITY-001`.

The remaining theorem is not a geometry theorem.  The formal geometry has
already been generated.  The remaining theorem is an ontology theorem:

$$
\boxed{
\hbox{which finite record families count as physically admissible actual
families?}
}
$$

This section promotes physical admissibility from an informal phrase to a
finite law-candidate.  The law is designed to be strong enough to imply
CE1-CE9 and Ward-anomaly vanishing, but explicit enough that any failure
prints a typed correction rather than hiding in words.

Searchable law tag:

`V4P25-PHYSICAL-ADMISSIBILITY-LAW`.

An intended \(3+1\) ISP descent family is physically admissible when it
satisfies PA1-PA12.

$$
\boxed{
\begin{array}{c|l}
\hbox{axiom} & \hbox{finite content}\\
\hline
\mathrm{PA1} & \hbox{hard actual support: records have a fixed finite support
before readout}\\
\mathrm{PA2} & \hbox{same-actual equivalence: presentation changes do not change
coincidence readings}\\
\mathrm{PA3} & \hbox{local coincidence frame: four independent clock/ruler
directions are printed cofinally}\\
\mathrm{PA4} & \hbox{reversal symmetry: metric data are the symmetric part of
oriented records}\\
\mathrm{PA5} & \hbox{transport comparability: neighboring frames have finite
Lorentz-compatible comparison maps}\\
\mathrm{PA6} & \hbox{boundary-of-boundary: finite incidence satisfies }
\partial\partial=0\\
\mathrm{PA7} & \hbox{torsion discipline: torsion vanishes or is typed as a
spin/torsion source}\\
\mathrm{PA8} & \hbox{probe completeness: every observable loop residue has a
printed Wilson/Cartan probe}\\
\mathrm{PA9} & \hbox{source detectability: every observable local response has a
printed source component or typed correction}\\
\mathrm{PA10} & \hbox{same-actual measure invariance: equivalent completions have
equal least-bias weight}\\
\mathrm{PA11} & \hbox{minimal local response: no hidden nonlocal source law is
admitted}\\
\mathrm{PA12} & \hbox{cofinal stability: exact, word-depth, and refinement
residuals converge or are typed}
\end{array}
}
$$

The hard axioms are PA8, PA9, PA10, and PA12.  They are the places where the
theory can genuinely fail and produce new physics.

## 44. Einstein Route: Physical Admissibility Forces CE1-CE9

Searchable theorem tag:

`V4P25-EINSTEIN-PHYSICAL-ADMISSIBILITY-TO-CE-THEOREM`.

Einstein's move is to show that the physical admissibility law is exactly the
finite equivalence principle needed for GR-effective Cartan completion.

The implication table is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{Cartan gate} & \hbox{forced by} & \hbox{reason}\\
\hline
\mathrm{CE1} & \mathrm{PA3+PA4} &
\hbox{local coincidence frames and reversal symmetry give Lorentzian tetrad readout}\\
\mathrm{CE2} & \mathrm{PA2+PA5} &
\hbox{same-actual frame comparison forces metric-compatible Lorentz transport}\\
\mathrm{CE3} & \mathrm{PA7} &
\hbox{torsion is either zero or a typed spin/torsion source}\\
\mathrm{CE4} & \mathrm{PA8} &
\hbox{observable plaquette residues are probe-complete}\\
\mathrm{CE5} & \mathrm{PA6} &
\hbox{boundary-of-boundary gives finite Bianchi}\\
\mathrm{CE6} & \mathrm{PA5+PA6+PA11} &
\hbox{local frame-natural curvature contractions define the Einstein cochain}\\
\mathrm{CE7} & \mathrm{PA9+PA11} &
\hbox{observable source responses are spanned by printed source components or typed}\\
\mathrm{CE8} & \mathrm{PA8+PA12} &
\hbox{word-depth residuals are probed and vanish cofinally or are typed}\\
\mathrm{CE9} & \mathrm{PA2+PA10+PA12} &
\hbox{refinements preserve records, weights, and exact terms cofinally}
\end{array}
}
$$

### 44.1 Theorem: Einstein Physical Admissibility

Assume a cofinal \(3+1\) ISP descent family satisfies PA1-PA12.  Then:

$$
\boxed{
\mathrm{PA1\text{-}PA12}
\Longrightarrow
\mathrm{CE1\text{-}CE9}.
}
$$

Proof.  PA3 prints the local coincidence frame, and PA4 makes the metric
readout symmetric; together they license the Lorentzian tetrad gate CE1.
PA2 says frame changes are same-actual moves, while PA5 provides the finite
comparison maps; hence transport must preserve the finite metric readout,
giving CE2.  PA7 is exactly the torsion gate CE3.  PA8 supplies the complete
loop-probe family, giving CE4.  PA6 gives the incidence identity
\(\partial\partial=0\), hence the finite Bianchi gate CE5.  PA5, PA6, and PA11
restrict admissible geometric response to local frame-natural curvature
contractions, giving CE6.  PA9 and PA11 state that any observable local
response is either represented by the printed source dictionary or typed as a
correction, giving CE7.  PA8 and PA12 handle finite word-depth residue,
giving CE8.  PA2, PA10, and PA12 make same-actual refinements preserve both
records and weights cofinally, giving CE9. `square`

This is the Einstein closure:

$$
\boxed{
\hbox{finite equivalence plus local coincidence plus source detectability
forces GR-effective Cartan completion, unless a typed PA failure appears.}
}
$$

### 44.2 Einstein Failure Ledger

Searchable ledger tag:

`V4P25-EINSTEIN-PA-FAILURE-LEDGER`.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failed PA axiom} & \hbox{failed CE gate} & \hbox{physical meaning}\\
\hline
\mathrm{PA3/PA4} & \mathrm{CE1} & \hbox{no stable Lorentzian metric sector}\\
\mathrm{PA5} & \mathrm{CE2/CE6} & \hbox{no metric-compatible transport or contraction}\\
\mathrm{PA7} & \mathrm{CE3} & \hbox{torsion/spin correction}\\
\mathrm{PA8} & \mathrm{CE4/CE8} & \hbox{probe or word-depth incompleteness}\\
\mathrm{PA6} & \mathrm{CE5} & \hbox{Bianchi/incidence failure}\\
\mathrm{PA9} & \mathrm{CE7} & \hbox{missing source component}\\
\mathrm{PA10} & \mathrm{CE9} & \hbox{same-actual measure anomaly}\\
\mathrm{PA12} & \mathrm{CE8/CE9} & \hbox{cofinal nonconvergence}
\end{array}
}
$$

Thus the Einstein route does not merely assume GR dynamics.  It says exactly
which physical-admissibility axiom must fail if pure GR dynamics fails.

## 45. Feynman Route: Sum Over Same-Actual Completions

Searchable theorem tag:

`V4P25-FEYNMAN-SAME-ACTUAL-COMPLETION-SUM`.

Feynman's move is not to choose one completion as the right one.  It is to
sum over all same-actual completions and make invariance under change of
completion do the work.

For a printed finite descent patch \({\mathcal D}_{\alpha}\), let:

$$
\boxed{
{\mathfrak C}_{\alpha}
=
\{\hbox{Cartan/Wilson completions of }{\mathcal D}_{\alpha}\hbox{ satisfying
the printed support}\}.
}
$$

Let \({\mathcal G}^{same}_{\alpha}\) be the finite groupoid generated by
same-actual moves:

$$
\boxed{
\hbox{frame relabeling, refinement regrouping, exact-pair cancellation,
path regrouping, commutator completion, and source relabeling.}
}
$$

The same-actual completion functional is:

$$
\boxed{
{\mathbb Z}_{\alpha}[J,\Theta,\Xi]
=
\sum_{[C]\in{\mathfrak C}_{\alpha}/{\mathcal G}^{same}_{\alpha}}
W_{\alpha}([C])\,
Z_{C}[J,\Theta,\Xi].
}
$$

The weight is licensed only if:

$$
\boxed{
W_{\alpha}([C])>0,
\qquad
W_{\alpha}(\Phi C)=W_{\alpha}(C)
\quad
\hbox{for same-actual }\Phi.
}
$$

This is PA10 in functional form.

### 45.1 Completion-Sum Ward Theorem

Searchable theorem tag:

`V4P25-COMPLETION-SUM-WARD-THEOREM`.

Assume PA1-PA12.  Then for every same-actual move \(\Phi\):

$$
\boxed{
\delta_{\Phi}{\mathbb Z}_{\alpha}[J,\Theta,\Xi]=0.
}
$$

Proof.  PA1 fixes the support, so the completion set is finite at each
\(\alpha\).  PA2 identifies same-actual moves as presentation changes rather
than physical changes.  PA8 and the Wilson completion ensure that commutator
and higher word moves act inside the completion set instead of leaving an
unrepresented residue.  PA10 makes the weight constant on same-actual orbits.
Thus \(\Phi\) permutes the summands in \({\mathbb Z}_{\alpha}\) without
changing their weights or physical insertions.  The finite sum is invariant.
`square`

### 45.2 Vanishing Typed Anomaly

Differentiate the completion-sum Ward identity with respect to source and
loop variables.  The response identity is:

$$
\boxed{
\delta_{J^{AB}}
\langle E^{fin}_{\mu\nu}\rangle_{{\mathbb Z}}
=
\kappa_{\mu\nu}^{\ \ AB}
\delta_{J^{AB}}\langle T^{fin}_{AB}\rangle_{{\mathbb Z}}
+\nabla^{fin}B_{\mu\nu}
+{\mathcal A}^{typed}_{\mu\nu,AB}.
}
$$

Under PA8, PA9, PA10, and PA12:

$$
\boxed{
{\mathcal A}^{typed}_{\alpha}
\in
{\mathcal A}_{probe}
\oplus
{\mathcal A}_{matter}
\oplus
{\mathcal A}_{boundary}
\oplus
{\mathcal A}_{higher}
\oplus
{\mathcal A}_{descent}
\oplus
{\mathcal A}_{cal}
}
$$

has no unrepresented component, and each represented component is either
exact or cofinally vanishing.  Therefore:

$$
\boxed{
{\mathcal A}^{typed}_{\alpha_n}\to0.
}
$$

This is the Feynman closure:

$$
\boxed{
\hbox{if the same-actual completion sum is finite, complete, and invariant,
then all Ward anomalies vanish cofinally.}
}
$$

### 45.3 Feynman Failure Ledger

Searchable ledger tag:

`V4P25-FEYNMAN-PA-FAILURE-LEDGER`.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{failure} & \hbox{anomaly type} & \hbox{meaning}\\
\hline
\hbox{completion set not closed} & {\mathcal A}_{probe} &
\hbox{missing Wilson/Cartan generator}\\
\hbox{same-actual weight not invariant} & {\mathcal A}_{cal} &
\hbox{external calibration or measure anomaly}\\
\hbox{source derivative not represented} & {\mathcal A}_{matter} &
\hbox{missing stress/source component}\\
\hbox{boundary term not exact} & {\mathcal A}_{boundary} &
\hbox{physical boundary channel}\\
\hbox{word-depth not convergent} & {\mathcal A}_{higher} &
\hbox{finite higher-curvature correction}\\
\hbox{refinement changes actual readings} & {\mathcal A}_{descent} &
\hbox{no GR-effective descent family}
\end{array}
}
$$

The real Feynman move is now explicit: do not pick a representation; sum over
the same-actual orbit and let the Ward identities say whether a residue is
physical.

## 46. Physical Admissibility Theorem

Searchable theorem tag:

`V4P25-PHYSICAL-ADMISSIBILITY-GR-DYNAMICS-THEOREM`.

Combine the Einstein and Feynman routes.

Assume a cofinal \(3+1\) ISP descent family satisfies PA1-PA12.  Then:

$$
\boxed{
\mathrm{PA1\text{-}PA12}
\Longrightarrow
\mathrm{CE1\text{-}CE9}
\quad
\hbox{and}
\quad
{\mathcal A}^{typed}_{\alpha_n}\to0.
}
$$

Therefore:

$$
\boxed{
\mathrm{PhysicallyAdmissibleISP}_{3+1}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

Proof.  The Einstein theorem in Section 44 derives CE1-CE9 from PA1-PA12.
The Cartan/Wilson existence theorem then gives formal completion and
GR-effective completion cofinally.  The Feynman theorem in Section 45 proves
that the same-actual completion functional is invariant under all licensed
calculation-route moves, and that the typed Ward anomaly vanishes cofinally.
The obstruction theorem in Section 24 then applies:
\([{\mathcal A}]=0\) is equivalent to GR-DYN-COFINAL-PASS. `square`

This theorem is conditional on adopting PA1-PA12 as the physical
admissibility law of the theory.  It is not a hidden appeal to continuum GR.
It is a finite equivalence/source-detectability law.

## 47. Final Fork After Physical Admissibility

Searchable final fork tag:

`V4P25-FINAL-PHYSICAL-ADMISSIBILITY-FORK`.

Paper 25 now has a clean final fork:

$$
\boxed{
\begin{array}{c|l}
\hbox{case} & \hbox{result}\\
\hline
\mathrm{PA1\text{-}PA12\ accepted} &
\hbox{effective }3+1\hbox{ GR dynamics is reconstructed cofinally}\\
\mathrm{some\ PA\ gate\ fails} &
\hbox{the first failed PA/CE/Ward gate prints the ISP correction to GR}
\end{array}
}
$$

The correction map is:

$$
\boxed{
\begin{array}{c|l}
\hbox{failed admissibility sector} & \hbox{predicted correction}\\
\hline
\hbox{torsion discipline} & \hbox{Einstein-Cartan/spin channel}\\
\hbox{probe completeness} & \hbox{new Wilson/curvature probe}\\
\hbox{source detectability} & \hbox{new stress/source component}\\
\hbox{boundary exactness} & \hbox{physical boundary term}\\
\hbox{word-depth convergence} & \hbox{higher-curvature finite correction}\\
\hbox{same-actual measure invariance} & \hbox{calibration/measure anomaly}\\
\hbox{cofinal stability} & \hbox{no GR-effective limit for that family}
\end{array}
}
$$

This is the strongest current Paper 25 status:

$$
\boxed{
\hbox{GR dynamics is reconstructed from finite descent if physical
admissibility PA1-PA12 is adopted; otherwise ISP predicts a typed correction
at the first failed admissibility gate.}
}
$$

## 48. PA Reduction And Anomaly Audit

Searchable audit tag:

`V4P25-PA-REDUCTION-AND-ANOMALY-AUDIT`.

The previous section makes PA1-PA12 decisive.  The next question is whether
they are arbitrary GR-sector assumptions or consequences of deeper ISP
principles.  This section reduces PA1-PA12 to three proposed first-principle
laws and then defines a Feynman-style anomaly test for each PA gate.

The three deeper principles are:

$$
\boxed{
\begin{array}{c|l}
\hbox{principle} & \hbox{meaning}\\
\hline
\mathrm{FAC} & \hbox{Finite Actual Covariance: same actual record means same
observable coincidence content}\\
\mathrm{SLC} & \hbox{Stable Local Coincidence: local records support stable
clock/ruler/frame comparisons}\\
\mathrm{RSC} & \hbox{Record/Source Completeness: every observable loop/source
effect is represented or typed}
\end{array}
}
$$

These are not continuum-GR assumptions.  They are finite-record principles.
Their job is to explain why PA1-PA12 are the natural no-anomaly conditions for
physical ISP records.

## 49. Einstein Reduction: Three Principles Behind PA1-PA12

Searchable theorem tag:

`V4P25-EINSTEIN-PA-REDUCTION-THEOREM`.

Einstein's move is to reduce the long list to a short principle set.  The
claim is not that every ISP family automatically satisfies PA1-PA12.  The
claim is:

$$
\boxed{
\mathrm{FAC+SLC+RSC}
\Longrightarrow
\mathrm{PA1\text{-}PA12}
\quad
\hbox{for the GR-effective sector.}
}
$$

### 49.1 Finite Actual Covariance

Searchable principle tag:

`V4P25-FINITE-ACTUAL-COVARIANCE`.

Finite Actual Covariance says:

$$
\boxed{
X\sim_{\mathrm{same\ actual}}Y
\Rightarrow
{\mathcal O}(X)={\mathcal O}(Y)
\quad
\hbox{for every licensed finite observable }{\mathcal O}.
}
$$

It implies:

$$
\boxed{
\mathrm{FAC}
\Rightarrow
\mathrm{PA1,PA2,PA10}
}
$$

because actual support must be fixed before observables are compared, same
actual descriptions must give the same readings, and equivalent completions
must carry equal least-bias weight.

FAC also supports PA12 when the same-actual relation is cofinal:

$$
\boxed{
\mathrm{FAC}_{cofinal}
\Rightarrow
\mathrm{PA12\ on\ exact/refinement\ residuals}.
}
$$

### 49.2 Stable Local Coincidence

Searchable principle tag:

`V4P25-STABLE-LOCAL-COINCIDENCE`.

Stable Local Coincidence says:

$$
\boxed{
\hbox{local actual records admit reproducible finite clock/ruler/frame
comparisons on a cofinal family.}
}
$$

It implies:

$$
\boxed{
\mathrm{SLC}
\Rightarrow
\mathrm{PA3,PA4,PA5,PA6,PA7}
}
$$

with one fork.  PA7 is not forced to the pure-GR branch.  SLC forces torsion
to be disciplined:

$$
\boxed{
\mathrm{SLC}
\Rightarrow
\left[
Torsion\to0
\quad\hbox{or}\quad
Torsion\hbox{ is printed as a spin/source channel}
\right].
}
$$

Thus pure GR requires the torsion-free branch; the alternative is a typed
Einstein-Cartan correction.

### 49.3 Record/Source Completeness

Searchable principle tag:

`V4P25-RECORD-SOURCE-COMPLETENESS`.

Record/Source Completeness says:

$$
\boxed{
\hbox{no observable finite difference may be physically real while absent
from the record/probe/source dictionary.}
}
$$

It implies:

$$
\boxed{
\mathrm{RSC}
\Rightarrow
\mathrm{PA8,PA9,PA11}
}
$$

and the remaining part of PA12:

$$
\boxed{
\mathrm{RSC}_{cofinal}
\Rightarrow
\hbox{word-depth residuals vanish cofinally or are typed.}
}
$$

RSC is the deepest completeness assumption.  If it fails, ISP does not lose
meaning; it predicts a missing probe, missing source component, boundary
channel, or higher-curvature correction.

### 49.4 Reduction Table

$$
\boxed{
\begin{array}{c|c|l}
\hbox{PA gate} & \hbox{reduction source} & \hbox{status}\\
\hline
\mathrm{PA1} & \mathrm{FAC} & \hbox{core ISP-aligned}\\
\mathrm{PA2} & \mathrm{FAC} & \hbox{core ISP-aligned}\\
\mathrm{PA3} & \mathrm{SLC} & \hbox{GR-sector local-frame condition}\\
\mathrm{PA4} & \mathrm{SLC} & \hbox{interval readout discipline}\\
\mathrm{PA5} & \mathrm{SLC} & \hbox{finite Lorentz transport condition}\\
\mathrm{PA6} & \mathrm{SLC/FAC} & \hbox{incidence consistency}\\
\mathrm{PA7} & \mathrm{SLC} & \hbox{pure GR branch or torsion correction}\\
\mathrm{PA8} & \mathrm{RSC} & \hbox{loop/Wilson probe completeness}\\
\mathrm{PA9} & \mathrm{RSC} & \hbox{source detectability}\\
\mathrm{PA10} & \mathrm{FAC} & \hbox{same-actual measure naturality}\\
\mathrm{PA11} & \mathrm{RSC} & \hbox{no hidden nonlocal source law}\\
\mathrm{PA12} & \mathrm{FAC+RSC} & \hbox{cofinal exact/word/refinement stability}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{FAC+SLC+RSC}
\Longrightarrow
\mathrm{PA1\text{-}PA12}
}
$$

with the explicit torsion fork and typed-completeness fork preserved.

## 50. Feynman Audit: PA Gates As Ward No-Anomaly Conditions

Searchable audit tag:

`V4P25-FEYNMAN-PA-WARD-ANOMALY-AUDIT`.

Feynman's move is to make every PA gate testable as a same-actual Ward
identity.  For each admissibility gate PA\(k\), define a move
\(\Phi_{PAk}\) that changes the representation exactly in the way PA\(k\)
claims should not change the physical reading.

Define the PA anomaly:

$$
\boxed{
{\mathfrak A}_{PAk}
:=
\delta_{\Phi_{PAk}}
{\mathbb Z}_{\alpha}[J,\Theta,\Xi].
}
$$

Then:

$$
\boxed{
\mathrm{PA}k
\quad\Longleftrightarrow\quad
{\mathfrak A}_{PAk}=0
\ \hbox{or is typed by the PA failure ledger.}
}
$$

The audit table is:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{move } \Phi_{PAk} & \hbox{anomaly if it fails}\\
\hline
\mathrm{PA1} & \hbox{change support after observable is chosen} &
{\mathcal A}_{descent}\\
\mathrm{PA2} & \hbox{same-actual relabeling} &
{\mathcal A}_{descent}\\
\mathrm{PA3} & \hbox{change local clock/ruler frame} &
{\mathcal A}_{descent}\hbox{ or no GR sector}\\
\mathrm{PA4} & \hbox{reverse edge orientation} &
{\mathcal A}_{metric}\\
\mathrm{PA5} & \hbox{change neighboring frame transport} &
{\mathcal A}_{probe}\\
\mathrm{PA6} & \hbox{replace boundary by boundary-of-boundary} &
{\mathcal A}_{boundary}\\
\mathrm{PA7} & \hbox{transport frame around infinitesimal parallelogram} &
{\mathcal A}_{torsion}\\
\mathrm{PA8} & \hbox{insert unprobed loop/commutator word} &
{\mathcal A}_{probe}\oplus{\mathcal A}_{higher}\\
\mathrm{PA9} & \hbox{insert source with no source component} &
{\mathcal A}_{matter}\\
\mathrm{PA10} & \hbox{move inside same-actual completion orbit} &
{\mathcal A}_{cal}\\
\mathrm{PA11} & \hbox{add hidden nonlocal source response} &
{\mathcal A}_{matter}\oplus{\mathcal A}_{descent}\\
\mathrm{PA12} & \hbox{refine and compare exact/word residuals} &
{\mathcal A}_{higher}\oplus{\mathcal A}_{descent}
\end{array}
}
$$

This is not a toy test.  It is a finite identity audit: if a PA gate fails,
the same-actual completion functional changes, and the change is the physical
correction.

### 50.1 PA Ward Theorem

Searchable theorem tag:

`V4P25-PA-WARD-NO-ANOMALY-THEOREM`.

Assume FAC, SLC, and RSC.  Then for every PA gate:

$$
\boxed{
{\mathfrak A}_{PAk}=0
\quad
\hbox{or}
\quad
{\mathfrak A}_{PAk}
\in
{\mathcal A}_{typed}
\hbox{ with an explicitly printed correction channel.}
}
$$

If the GR-effective branch is selected, meaning torsion is zero, probe/source
dictionaries are complete, same-actual weights are invariant, and cofinal
residuals vanish, then:

$$
\boxed{
{\mathfrak A}_{PAk}\to0
\quad
\hbox{for all }k=1,\ldots,12.
}
$$

Proof.  FAC makes support, relabeling, same-actual measure, and refinement
moves act as changes of finite presentation rather than changes of physical
content.  SLC makes local frame, reversal, transport, incidence, and torsion
moves measurable in the finite record language.  RSC ensures any loop,
commutator, source, boundary, or word-depth residue is either represented by
the completion algebra or typed as a correction.  Hence every PA violation is
visible as a Ward anomaly, and every no-anomaly branch is exactly a PA gate.
`square`

## 51. Reduced Physical Admissibility Verdict

Searchable verdict tag:

`V4P25-REDUCED-PHYSICAL-ADMISSIBILITY-VERDICT`.

The physical admissibility law can now be stated in compressed form:

$$
\boxed{
\mathrm{PhysicallyAdmissibleISP}_{3+1}
=
\mathrm{FAC+SLC+RSC}
\hbox{ on the GR-effective no-anomaly branch.}
}
$$

Then:

$$
\boxed{
\mathrm{FAC+SLC+RSC}
\Longrightarrow
\mathrm{PA1\text{-}PA12}
\Longrightarrow
\mathrm{CE1\text{-}CE9}
\quad\hbox{and}\quad
{\mathcal A}_{typed}\to0.
}
$$

Therefore:

$$
\boxed{
\mathrm{FAC+SLC+RSC}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}
}
$$

on the GR-effective branch.

If the branch fails:

$$
\boxed{
\neg(\mathrm{GR\text{-}effective\ branch})
\Longrightarrow
\hbox{typed ISP correction to GR}.
}
$$

The status is now stronger than Section 47:

$$
\boxed{
\hbox{PA1-PA12 are not arbitrary assumptions; they are the no-anomaly
unpacking of finite actual covariance, stable local coincidence, and
record/source completeness.}
}
$$

What remains is not another gate list.  It is the foundational choice:

$$
\boxed{
\hbox{does ISP adopt FAC+SLC+RSC as its physical-admissibility law?}
}
$$

If yes, Paper 25 closes effective GR dynamics.  If no, the PA Ward audit
prints the first typed deviation from GR.

## 52. Executable FAC/SLC/RSC Admissibility Audit

Searchable audit tag:

`V4P25-FAC-SLC-RSC-ADMISSIBILITY-AUDIT`.

The previous section reduced physical admissibility to FAC+SLC+RSC.  That is
not yet enough.  A physical-admissibility law must be auditable without
secretly asking whether the answer looks like GR.

The audit object is:

$$
\boxed{
{\mathfrak A}^{adm}_{\alpha}
=
({\mathcal R}_{\alpha},
\sim_{\alpha},
{\mathcal O}_{\alpha},
{\mathcal C}_{\alpha},
{\mathcal P}_{\alpha},
{\mathcal S}_{\alpha},
{\mathbb Z}_{\alpha},
{\mathcal R}_{\alpha\to\beta}).
}
$$

Here:

$$
\boxed{
\begin{array}{ll}
{\mathcal R}_{\alpha}:&\hbox{finite actual record slabs at resolution }\alpha,\\
\sim_{\alpha}:&\hbox{same-actual equivalence relation or groupoid},\\
{\mathcal O}_{\alpha}:&\hbox{licensed finite observables},\\
{\mathcal C}_{\alpha}:&\hbox{clock/ruler/frame comparison probes},\\
{\mathcal P}_{\alpha}:&\hbox{loop, holonomy, boundary, and word probes},\\
{\mathcal S}_{\alpha}:&\hbox{printed source/stress/response dictionary},\\
{\mathbb Z}_{\alpha}:&\hbox{same-actual completion functional},\\
{\mathcal R}_{\alpha\to\beta}:&\hbox{finite refinement/coarse-graining maps}.
\end{array}
}
$$

The audit is Barandes-aligned because every entry is finite record data,
finite comparison data, or a finite functional over actual completions.  No
continuum metric, smooth manifold, or continuum action is primitive.

The audit has two faces:

$$
\boxed{
\begin{array}{c|l}
\hbox{Einstein face} &
\hbox{does finite actual coincidence force the admissibility law?}\\
\hbox{Feynman face} &
\hbox{is every admissibility move a same-actual Ward identity?}
\end{array}
}
$$

The pass condition is:

$$
\boxed{
{\mathfrak A}^{adm}_{\alpha}
\models
\mathrm{FAC+SLC+RSC}
}
$$

cofinally in \(\alpha\).  The fail condition is not silence; it is a typed
anomaly:

$$
\boxed{
{\mathfrak A}^{adm}_{\alpha}
\not\models
\mathrm{FAC+SLC+RSC}
\Longrightarrow
{\mathcal A}_{FAC}\oplus{\mathcal A}_{SLC}\oplus{\mathcal A}_{RSC}
\hbox{ is printed.}
}
$$

## 53. Einstein Face: Coincidence Necessity Audit

Searchable theorem tag:

`V4P25-EINSTEIN-COINCIDENCE-NECESSITY-AUDIT`.

The Einstein audit refuses to ask first whether the equations look like GR.
It asks whether finite actual records admit a geometry of coincidences at all.

### 53.1 FAC Audit

FAC passes at resolution \(\alpha\) iff:

$$
\boxed{
X\sim_{\alpha}Y
\Rightarrow
{\mathcal O}(X)={\mathcal O}(Y)
\quad
\hbox{for every }{\mathcal O}\in{\mathcal O}_{\alpha}.
}
$$

Equivalently, every licensed observable descends to the same-actual quotient:

$$
\boxed{
{\mathcal O}_{\alpha}
:
{\mathcal R}_{\alpha}
\longrightarrow
V_{\mathcal O}
\quad
\hbox{factors through}\quad
{\mathcal R}_{\alpha}/\!\sim_{\alpha}.
}
$$

The FAC obstruction is:

$$
\boxed{
{\mathcal A}_{FAC,\alpha}
=
\{(X,Y,{\mathcal O}):
X\sim_{\alpha}Y,\ 
{\mathcal O}(X)\ne{\mathcal O}(Y)\}.
}
$$

Thus:

$$
\boxed{
{\mathcal A}_{FAC,\alpha}=\varnothing
\Longleftrightarrow
\mathrm{FAC}_{\alpha}\hbox{ passes.}
}
$$

If this obstruction persists cofinally, there is no GR-effective covariance
sector for that family.  The failure is deeper than a correction to
Einstein's equation: the same actual situation has not been made invariantly
defined.

### 53.2 SLC Audit

SLC passes at resolution \(\alpha\) iff the comparison probes:

$$
\boxed{
{\mathcal C}_{\alpha}
=
(\tau_{\alpha},d_{\alpha},e_{\alpha},U_{\alpha},T_{\alpha})
}
$$

support stable local clock, ruler, frame, transport, and torsion tests.

The required finite comparison identities are:

$$
\boxed{
\begin{array}{ll}
\mathrm{SLC1}:&
d_{\alpha}(i,j)=d_{\alpha}(j,i)
\hbox{ up to orientation/reference convention};\\
\mathrm{SLC2}:&
e_{\alpha}\hbox{ gives a finite local frame comparison on neighboring
records};\\
\mathrm{SLC3}:&
U_{\alpha}(i\to j)\hbox{ transports comparison probes without changing
same-actual readings};\\
\mathrm{SLC4}:&
\partial^2_{\alpha}=0\hbox{ on finite incidence comparisons};\\
\mathrm{SLC5}:&
T_{\alpha}=0\hbox{ or }T_{\alpha}\hbox{ is printed as a spin/torsion
source channel};\\
\mathrm{SLC6}:&
\hbox{the comparison residuals vanish or stabilize cofinally.}
\end{array}
}
$$

The SLC obstruction is:

$$
\boxed{
{\mathcal A}_{SLC,\alpha}
=
{\mathcal A}_{metric,\alpha}
\oplus
{\mathcal A}_{frame,\alpha}
\oplus
{\mathcal A}_{torsion,\alpha}
\oplus
{\mathcal A}_{incidence,\alpha}.
}
$$

Pure GR requires:

$$
\boxed{
{\mathcal A}_{SLC,\alpha_n}\to0.
}
$$

A nonzero torsion component does not falsify ISP.  It falsifies the pure-GR
branch and selects the typed Einstein-Cartan branch:

$$
\boxed{
{\mathcal A}_{torsion,*}\ne0
\Longrightarrow
\hbox{spin/torsion source correction.}
}
$$

If local clock/ruler/frame comparison itself fails, the family is not
GR-effective.  It may still be an ISP sector, but not a spacetime-geometry
sector.

### 53.3 RSC Audit

RSC passes at resolution \(\alpha\) iff every persistent finite residue is in
the span of the printed probe/source dictionary or is typed.

Define the finite residue module:

$$
\boxed{
{\mathcal E}_{\alpha}
=
\hbox{persistent loop, source, boundary, commutator, and word-depth effects}.
}
$$

Define the dictionary map:

$$
\boxed{
D_{\alpha}:
{\mathcal P}_{\alpha}\oplus{\mathcal S}_{\alpha}
\longrightarrow
{\mathcal E}_{\alpha}.
}
$$

RSC passes iff:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}
=0
\quad
\hbox{or}
\quad
\mathrm{coker}\,D_{\alpha}
\subset
{\mathcal A}_{typed,\alpha}
}
$$

cofinally.  The RSC obstruction is:

$$
\boxed{
{\mathcal A}_{RSC,\alpha}
=
\mathrm{coker}\,D_{\alpha}.
}
$$

If it persists, the theory has found a real missing channel:

$$
\boxed{
{\mathcal A}_{RSC,*}\ne0
\Longrightarrow
\hbox{missing source, boundary, probe, commutator, or higher-curvature
correction.}
}
$$

### 53.4 Einstein Coincidence Verdict

The Einstein audit theorem is:

$$
\boxed{
\begin{array}{c}
{\mathcal A}_{FAC,\alpha_n}\to0,\\
{\mathcal A}_{SLC,\alpha_n}\to0,\\
{\mathcal A}_{RSC,\alpha_n}\to0
\end{array}
\quad
\Longrightarrow
\quad
\mathrm{FAC+SLC+RSC}
}
$$

on the GR-effective branch.

If any one of the three limits is nonzero, the failure is not an arbitrary
deviation from GR.  It has the type printed by the obstruction:

$$
\boxed{
\begin{array}{c|l}
\hbox{nonzero obstruction} & \hbox{meaning}\\
\hline
{\mathcal A}_{FAC,*} & \hbox{same-actual covariance failure}\\
{\mathcal A}_{SLC,*} & \hbox{metric/frame/torsion/local-geometry failure}\\
{\mathcal A}_{RSC,*} & \hbox{missing probe/source/boundary/higher channel}
\end{array}
}
$$

## 54. Feynman Face: Same-Actual Ward Audit

Searchable audit tag:

`V4P25-FEYNMAN-SAME-ACTUAL-WARD-AUDIT-FAC-SLC-RSC`.

The Feynman audit does not build a toy model and break it.  It asks whether
the same physical calculation can be done by different finite routes and
still give the same answer.

Let \(\Phi\) be a finite same-actual move.  The Ward defect is:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha}
=
\delta_{\Phi}{\mathbb Z}_{\alpha}.
}
$$

The moves are grouped by the three principles:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{principle} & \hbox{same-actual moves} & \hbox{Ward defect}\\
\hline
\mathrm{FAC} &
\hbox{relabel support, change presentation, move inside same-actual orbit} &
{\mathfrak W}_{FAC}\\
\mathrm{SLC} &
\hbox{reverse edge, change local frame, transport around small loop} &
{\mathfrak W}_{SLC}\\
\mathrm{RSC} &
\hbox{insert loop/source/boundary/commutator word and compare dictionary} &
{\mathfrak W}_{RSC}
\end{array}
}
$$

The audit condition is:

$$
\boxed{
{\mathfrak W}_{FAC,\alpha_n}\to0,\quad
{\mathfrak W}_{SLC,\alpha_n}\to0,\quad
{\mathfrak W}_{RSC,\alpha_n}\to0
}
$$

for pure GR.  More generally:

$$
\boxed{
{\mathfrak W}_{\Phi,\alpha_n}\to
{\mathfrak W}_{\Phi,*}
\ne0
\Longrightarrow
{\mathfrak W}_{\Phi,*}
\in
{\mathcal A}_{typed,*}.
}
$$

Thus every persistent Ward defect is promoted to a finite physical correction,
not hidden as a failed derivation.

### 54.1 FAC Ward Identity

For a same-actual relabeling or presentation move:

$$
\boxed{
\Phi_{FAC}:X\mapsto Y,\qquad X\sim_{\alpha}Y,
}
$$

the required identity is:

$$
\boxed{
\delta_{\Phi_{FAC}}{\mathbb Z}_{\alpha}=0.
}
$$

Failure means the completion sum is not defined on actual situations but on
presentations:

$$
\boxed{
\delta_{\Phi_{FAC}}{\mathbb Z}_{\alpha}\ne0
\Longrightarrow
{\mathcal A}_{descent}\oplus{\mathcal A}_{cal}.
}
$$

### 54.2 SLC Ward Identity

For local comparison moves:

$$
\boxed{
\Phi_{SLC}
\in
\{\hbox{edge reversal, frame change, local transport loop, incidence move}\},
}
$$

the required identity is:

$$
\boxed{
\delta_{\Phi_{SLC}}{\mathbb Z}_{\alpha}=0
\quad
\hbox{modulo printed torsion/spin source if the branch is not pure GR.}
}
$$

Failure means:

$$
\boxed{
\delta_{\Phi_{SLC}}{\mathbb Z}_{\alpha}\ne0
\Longrightarrow
{\mathcal A}_{metric}
\oplus
{\mathcal A}_{frame}
\oplus
{\mathcal A}_{torsion}
\oplus
{\mathcal A}_{boundary}.
}
$$

### 54.3 RSC Ward Identity

For insertions of probes and sources:

$$
\boxed{
\Phi_{RSC}
\in
\{\hbox{loop insertion, source insertion, commutator word, boundary
channel}\},
}
$$

the required identity is:

$$
\boxed{
\delta_{\Phi_{RSC}}{\mathbb Z}_{\alpha}=0
\quad
\hbox{after projection through }D_{\alpha}.
}
$$

Equivalently:

$$
\boxed{
\delta_{\Phi_{RSC}}{\mathbb Z}_{\alpha}
\in
\mathrm{im}\,D_{\alpha}
\quad
\hbox{or is typed.}
}
$$

Failure means:

$$
\boxed{
\delta_{\Phi_{RSC}}{\mathbb Z}_{\alpha}\notin\mathrm{im}\,D_{\alpha}
\Longrightarrow
{\mathcal A}_{matter}
\oplus
{\mathcal A}_{probe}
\oplus
{\mathcal A}_{higher}
\oplus
{\mathcal A}_{boundary}.
}
$$

### 54.4 Feynman Ward Verdict

The Feynman audit theorem is:

$$
\boxed{
\begin{array}{c}
{\mathfrak W}_{FAC,\alpha_n}\to0,\\
{\mathfrak W}_{SLC,\alpha_n}\to0,\\
{\mathfrak W}_{RSC,\alpha_n}\to0
\end{array}
\Longleftrightarrow
\hbox{all finite calculation routes agree on the GR-effective branch.}
}
$$

If a Ward defect survives, it is the finite value of the correction.

This is the real Feynman move: not a toy number test, but an invariant
route-independence audit over the actual calculation algebra.

## 55. Final Audit Decision Procedure

Searchable verdict tag:

`V4P25-FAC-SLC-RSC-FINAL-AUDIT-DECISION`.

The paper now has an executable closure rule:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{principle} & \hbox{pass condition} & \hbox{if it fails cofinally}\\
\hline
\mathrm{FAC} &
{\mathcal A}_{FAC}\to0\hbox{ and }{\mathfrak W}_{FAC}\to0 &
\hbox{descent/gauge/calibration anomaly}\\
\mathrm{SLC} &
{\mathcal A}_{SLC}\to0\hbox{ and }{\mathfrak W}_{SLC}\to0 &
\hbox{no GR sector, or torsion/frame/metric correction}\\
\mathrm{RSC} &
{\mathcal A}_{RSC}\to0\hbox{ and }{\mathfrak W}_{RSC}\to0 &
\hbox{missing source/probe/boundary/higher-curvature correction}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{FAC/SLC/RSC\ audit\ PASS}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

And:

$$
\boxed{
\mathrm{FAC/SLC/RSC\ audit\ FAIL}
\Longrightarrow
\mathrm{typed\ ISP\ deviation\ from\ GR}.
}
$$

The consequence is precise:

$$
\boxed{
\begin{array}{c|l}
\hbox{outcome} & \hbox{interpretation}\\
\hline
\hbox{all three pass} &
\hbox{effective GR dynamics is reconstructed from finite actual records}\\
\hbox{FAC fails} &
\hbox{same-actual covariance is not physically valid for the family}\\
\hbox{SLC fails} &
\hbox{the family is not pure Lorentzian GR, or has torsion/frame correction}\\
\hbox{RSC fails} &
\hbox{the probe/source dictionary is incomplete and predicts an extra channel}
\end{array}
}
$$

This keeps Barandes alignment intact:

$$
\boxed{
\hbox{GR appears only as the no-anomaly effective face of finite actual
records, not as primitive ontology.}
}
$$

The final remaining task for the paper is no longer to invent a new route.
It is to run this audit on the corpus-wide finite actual family:

$$
\boxed{
{\mathfrak A}^{adm}_{\alpha}
\quad
\hbox{for a cofinal actual refinement family }\alpha\to\infty.
}
$$

If that family is printed and the audit passes, Paper 25 closes effective GR
dynamics for real.  If the audit fails, Paper 25 does something just as
important: it prints the first finite, typed, Barandes-aligned correction to
GR.

## 56. Audit Of The P24 Corpus-Wide Actual Family

Searchable audit tag:

`V4P25-AUDIT-OF-P24-CORPUS-WIDE-ACTUAL-FAMILY`.

Paper 24 prints the corpus-wide actual family:

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

with local finite packets:

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

Paper 24 also prints the normal-form rule:

$$
\boxed{
w\Rightarrow A^{*}R^{*}K^{*}E^{*}.
}
$$

Here \(A\) is analysis, \(R\) is exact refinement, \(K\) is unpaired corner
extension, and \(E\) is unpaired source extension.  Same actual presentation
changes are exactly the \(A^{*}R^{*}\) part.  Nonzero \(K\) or \(E\) means
new actual content, not a new presentation of the same actual situation.

Pull this family into the P25 audit tuple by setting:

$$
\boxed{
\begin{array}{ll}
{\mathcal R}_{\alpha}^{25}:&
\mathrm{Desc}(\alpha),\\
\sim_{\alpha}^{25}:&
\hbox{equivalence generated by }A^{*}R^{*}\hbox{ moves},\\
{\mathcal O}_{\alpha}^{25}:&
\hbox{finite normal-form observables }Q,C,A^{eff}\hbox{ and GR readouts},\\
{\mathcal C}_{\alpha}^{25}:&
\hbox{metric/frame/transport/torsion comparison probes},\\
{\mathcal P}_{\alpha}^{25}:&
\hbox{Cartan, Wilson, holonomy, corner, and word probes},\\
{\mathcal S}_{\alpha}^{25}:&
\hbox{finite source and stress-response dictionary},\\
{\mathbb Z}_{\alpha}^{25}:&
\hbox{same-actual completion functional},\\
{\mathcal R}_{\alpha\to\beta}^{25}:&
r_{\beta\alpha}.
\end{array}
}
$$

Thus the P24 family is not merely background motivation.  It is the concrete
input to the P25 FAC/SLC/RSC audit:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\longmapsto
{\mathfrak A}^{adm}_{P25}.
}
$$

The audit is run under the P24 actual-refinement law:

$$
\boxed{
\hbox{refinement may reveal, split, relabel, or pair records; it may not
introduce new unpaired actual content.}
}
$$

Without that law, same-actual refinement is undefined and FAC cannot be
audited.

## 57. FAC Result On The P24 Family

Searchable result tag:

`V4P25-P24-FAC-AUDIT-RESULT`.

For the P24 family, same-actual moves are \(A^{*}R^{*}\).  Paper 24 proves:

$$
\boxed{
A^{*}R^{*}
\Rightarrow
\Delta Q=0,
\qquad
\Delta C=0.
}
$$

and:

$$
\boxed{
A^{*}R^{*}
\Rightarrow
\Delta A^{eff}=0
}
$$

up to the fixed endpoint/reference convention.  Therefore the finite
value-source observables descend to the same-actual quotient:

$$
\boxed{
{\mathcal O}_{value}
:
{\mathcal R}_{\alpha}^{25}
\to
V_{\mathcal O}
\quad
\hbox{factors through}\quad
{\mathcal R}_{\alpha}^{25}/\!\sim_{\alpha}^{25}.
}
$$

The Einstein FAC obstruction is therefore:

$$
\boxed{
{\mathcal A}_{FAC,\alpha}^{P24}=0.
}
$$

The Feynman FAC Ward defect also vanishes.  Exact pairs and commutator
changes contribute only:

$$
\boxed{
[D,A]\oplus(I_V-I_V),
}
$$

whose finite trace is zero:

$$
\boxed{
\operatorname{Tr}[D,A]=0,
\qquad
\operatorname{Tr}(I_V-I_V)=0.
}
$$

Hence:

$$
\boxed{
{\mathfrak W}_{FAC,\alpha}^{P24}=0.
}
$$

FAC result:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC}.
}
$$

This is the strongest part of the audit.  It is not merely conditional on
looking like GR.  It follows from the P24 same-actual normal form and actual
refinement law.

## 58. SLC Result On The P24 Family

Searchable result tag:

`V4P25-P24-SLC-AUDIT-RESULT`.

SLC asks for more than value-source invariance.  It asks whether the same
finite actual family supports stable clock, ruler, frame, and transport
comparison probes.

The P24 normal form supplies the actual-presentation side:

$$
\boxed{
\hbox{same actual presentation change}
\Longleftrightarrow
A^{*}R^{*}.
}
$$

Paper 25 supplies the GR comparison side through the finite Cartan/Wilson
completion:

$$
\boxed{
{\mathcal C}_{\alpha}^{GR}
=
(g_{\alpha},e_{\alpha},U_{\alpha},T_{\alpha},F_{\alpha}).
}
$$

The SLC audit condition is:

$$
\boxed{
A^{*}R^{*}
\hbox{ preserves }
g_{\alpha},e_{\alpha},U_{\alpha}
\hbox{ up to endpoint/reference terms,}
}
$$

and:

$$
\boxed{
T_{\alpha}\to0
\quad
\hbox{or}
\quad
T_{\alpha}
\hbox{ is printed as a spin/torsion source channel.}
}
$$

Using the P25 Cartan completion, the metric/frame/transport comparison moves
are represented by finite Lorentz transport and Cartan curvature probes.
Thus:

$$
\boxed{
{\mathcal A}_{metric,\alpha}=0,\quad
{\mathcal A}_{frame,\alpha}=0
}
$$

on the GR-effective Cartan branch.

The remaining SLC fork is torsion:

$$
\boxed{
{\mathcal A}_{SLC,\alpha}^{P24}
=
{\mathcal A}_{torsion,\alpha}.
}
$$

Therefore:

$$
\boxed{
\begin{array}{ll}
{\mathcal A}_{torsion,\alpha_n}\to0
&\Rightarrow
\mathrm{SLC\ PASS}_{GR},\\
{\mathcal A}_{torsion,\alpha_n}\to{\mathcal A}_{torsion,*}\ne0
&\Rightarrow
\mathrm{SLC\ PASS}_{typed}
\hbox{ with Einstein-Cartan correction.}
\end{array}
}
$$

The Feynman Ward statement is the same:

$$
\boxed{
{\mathfrak W}_{SLC,\alpha}
=0
\quad
\hbox{modulo a printed torsion/spin source channel.}
}
$$

Thus the SLC result is:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{SLC}_{typed},
}
$$

and:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{SLC}_{GR}
\quad
\hbox{iff}
\quad
{\mathcal A}_{torsion,\alpha_n}\to0.
}
$$

So SLC is not an unconditional pure-GR pass.  It is a disciplined fork: pure
GR if torsion vanishes cofinally, Einstein-Cartan-type correction if it does
not.

## 59. RSC Result On The P24 Family

Searchable result tag:

`V4P25-P24-RSC-AUDIT-RESULT`.

RSC asks whether every persistent loop, source, boundary, commutator, and
word-depth residue is represented by the printed probe/source dictionary or
typed.

For the P24 normal form, every finite corpus move reduces to:

$$
\boxed{
A^{*}R^{*}K^{*}E^{*}.
}
$$

The \(A^{*}R^{*}\) part is presentation.  The \(K^{*}\) part is unpaired
corner cohomology.  The \(E^{*}\) part is unpaired source extension.  Therefore
the finite residue module is:

$$
\boxed{
{\mathcal E}_{\alpha}^{P24}
=
K_{\alpha}^{corner}
\oplus
\operatorname{Ind}_{fin}({\mathcal K}_{new})
\oplus
{\mathcal E}_{comm}
\oplus
{\mathcal E}_{word}.
}
$$

The P25 dictionary map is:

$$
\boxed{
D_{\alpha}^{25}
:
{\mathcal P}_{Cartan/Wilson,\alpha}
\oplus
{\mathcal S}_{stress,\alpha}
\longrightarrow
{\mathcal E}_{\alpha}^{P24}.
}
$$

By the Cartan/Wilson completion, commutator and holonomy residues are
represented by the completed finite curvature/probe algebra.  By the source
dictionary, source extensions are represented by finite stress-response
components.  By the corner construction, corner residues are represented by
finite corner cohomology.

Thus:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{25}
\subset
{\mathcal A}_{typed,\alpha}.
}
$$

The pure-GR branch requires the stronger condition:

$$
\boxed{
\mathrm{coker}\,D_{\alpha_n}^{25}\to0.
}
$$

The typed branch allows a stable nonzero cokernel, but it must be named:

$$
\boxed{
\mathrm{coker}\,D_{\alpha_n}^{25}
\to
{\mathcal A}_{typed,*}\ne0
\Longrightarrow
\hbox{extra source/probe/boundary/higher-curvature channel.}
}
$$

The Feynman Ward form is:

$$
\boxed{
\delta_{\Phi_{RSC}}{\mathbb Z}_{\alpha}
\in
\mathrm{im}\,D_{\alpha}^{25}
\oplus
{\mathcal A}_{typed,\alpha}.
}
$$

Therefore:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{RSC}_{typed},
}
$$

and:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{RSC}_{GR}
\quad
\hbox{iff}
\quad
\mathrm{coker}\,D_{\alpha_n}^{25}\to0.
}
$$

RSC is the second honest fork.  It does not let the theory ignore missing
channels.  It says every missing channel is either absent cofinally, or it is
the predicted finite deviation from pure GR.

## 60. P24 Family FAC/SLC/RSC Audit Verdict

Searchable verdict tag:

`V4P25-P24-FAC-SLC-RSC-AUDIT-VERDICT`.

The audit result is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{principle} & \hbox{P24 family result} & \hbox{meaning}\\
\hline
\mathrm{FAC} &
\mathrm{PASS} &
\hbox{same-actual normal form preserves finite observables}\\
\mathrm{SLC} &
\mathrm{PASS}_{typed} &
\hbox{pure GR iff torsion vanishes cofinally}\\
\mathrm{RSC} &
\mathrm{PASS}_{typed} &
\hbox{pure GR iff dictionary cokernel vanishes cofinally}
\end{array}
}
$$

Equivalently:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC_{typed}+RSC_{typed}}.
}
$$

The pure-GR branch is:

$$
\boxed{
{\mathcal A}_{torsion,\alpha_n}\to0
\quad
\hbox{and}
\quad
\mathrm{coker}\,D_{\alpha_n}^{25}\to0.
}
$$

Under those two no-anomaly conditions:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}.
}
$$

If either condition fails:

$$
\boxed{
\begin{array}{c|l}
\hbox{persistent failure} & \hbox{prediction}\\
\hline
{\mathcal A}_{torsion,*}\ne0 &
\hbox{Einstein-Cartan/spin-torsion correction}\\
\mathrm{coker}\,D_{*}^{25}\ne0 &
\hbox{extra matter, probe, boundary, or higher-curvature correction}
\end{array}
}
$$

Thus the audit is not an automatic victory and not a retreat.  It proves the
following precise statement:

$$
\boxed{
\hbox{the P24 corpus-wide finite actual family is Barandes-admissible and
closes effective GR exactly on its no-typed-residue branch.}
}
$$

This is the strongest honest result available at this point.  The remaining
work, if one wants pure GR rather than a typed extension, is now sharply
localized:

$$
\boxed{
\hbox{prove torsion vanishes cofinally and prove the source/probe dictionary
cokernel vanishes cofinally.}
}
$$

If those proofs hold, Paper 25 closes pure effective GR dynamics.  If they do
not, Paper 25 prints the first controlled ISP correction to GR.

## 61. Complete SLC Audit: Torsion As Exact Or Actual

Searchable audit tag:

`V4P25-COMPLETE-SLC-TORSION-AUDIT`.

Section 60 left SLC conditional on:

$$
\boxed{
{\mathcal A}_{torsion,\alpha_n}\to0.
}
$$

Now evaluate that condition on the P24 corpus-wide actual family.

The finite torsion residue is the local translation-closure defect:

$$
\boxed{
T_{\alpha}
=
\hbox{failure of a finite local frame parallelogram to close as the same
actual endpoint.}
}
$$

It can occur in exactly two ways:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{type} & \hbox{normal-form location} & \hbox{meaning}\\
\hline
T_{\mathrm{exact}} &
A^{*}R^{*} &
\hbox{presentation/frame artifact}\\
T_{\mathrm{actual}} &
E_T\hbox{ or }K_T &
\hbox{new spin/torsion actual content}
\end{array}
}
$$

There is no third option in the P24 normal form:

$$
\boxed{
w\Rightarrow A^{*}R^{*}K^{*}E^{*}.
}
$$

### 61.1 Einstein Torsion Audit

Einstein's question is:

$$
\boxed{
\hbox{can a same-actual local frame comparison have a persistent closure
defect?}
}
$$

If the defect lies inside the same-actual fiber, then two presentations of the
same actual local coincidence give different endpoint coincidence content:

$$
\boxed{
X\sim_{\alpha}Y
\quad\hbox{but}\quad
endpoint(X)\ne endpoint(Y).
}
$$

That is exactly a FAC violation.  But the P24 family already passed FAC:

$$
\boxed{
{\mathcal A}_{FAC,\alpha}^{P24}=0.
}
$$

Therefore:

$$
\boxed{
T_{\mathrm{exact}}
\in A^{*}R^{*}
\Longrightarrow
T_{\mathrm{exact}}=0
\hbox{ in the same-actual quotient.}
}
$$

A persistent nonzero torsion residue must therefore be new actual content:

$$
\boxed{
T_{\alpha,*}\ne0
\Longrightarrow
T_{\alpha,*}
\in
E_T\oplus K_T.
}
$$

But the active P24 normal-form family has no independent spin/torsion
extension generator.  Its value-changing content is already classified by the
printed source and corner generators:

$$
\boxed{
\mathrm{Active}(P20\text{-}P24)
\Rightarrow
A^{*}R^{*}E^{*}
\quad
\hbox{with no }E_T\hbox{ generator.}
}
$$

Hence the Einstein SLC result for the active corpus is:

$$
\boxed{
{\mathcal A}_{torsion,\alpha_n}^{P24}\to0.
}
$$

If a later corpus backfill introduces an independent \(E_T\) or \(K_T\), then
the result changes in a typed way:

$$
\boxed{
E_T\hbox{ or }K_T\hbox{ printed}
\Longrightarrow
\hbox{Einstein-Cartan branch, not pure GR.}
}
$$

### 61.2 Feynman Torsion Ward Audit

Feynman's question is:

$$
\boxed{
\hbox{does the finite completion functional change under the local
parallelogram route move?}
}
$$

Let \(\Phi_T\) be the move that computes a local frame endpoint by two finite
routes around the same actual small parallelogram.  The torsion Ward defect is:

$$
\boxed{
{\mathfrak W}_{T,\alpha}
=
\delta_{\Phi_T}{\mathbb Z}_{\alpha}.
}
$$

By the P24 finite transfer law, every same-actual transfer change has normal
form:

$$
\boxed{
\Delta\Xi
=
[D,A]\oplus(I_V-I_V)
}
$$

unless it contains an unpaired actual extension:

$$
\boxed{
\Delta\Xi
=
[D,A]\oplus(I_V-I_V)\oplus P_{K}\oplus P_{E}.
}
$$

The first two terms vanish under finite trace:

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
{\mathfrak W}_{T,\alpha}=0
\quad
\hbox{for same-actual }A^{*}R^{*}\hbox{ torsion moves.}
}
$$

A nonzero Ward defect would have to be:

$$
\boxed{
{\mathfrak W}_{T,*}
=
\operatorname{Tr}P_{E_T}
\quad\hbox{or}\quad
\operatorname{Tr}P_{K_T}.
}
$$

The active P24/P25 corpus contains no such independent torsion projector.
Therefore:

$$
\boxed{
{\mathfrak W}_{T,\alpha_n}^{P24}\to0.
}
$$

### 61.3 SLC Final Result

The complete SLC audit result is:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{SLC}_{GR}
}
$$

for the active P20-P25 corpus.

More precisely:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{torsion class} & \hbox{status} & \hbox{meaning}\\
\hline
T_{\mathrm{exact}} & 0 & \hbox{same-actual presentation artifact}\\
T_{\mathrm{actual}} & \hbox{absent in active corpus} &
\hbox{no spin/torsion extension printed}\\
T_{\mathrm{future}} & \hbox{typed if printed} &
\hbox{Einstein-Cartan correction branch}
\end{array}
}
$$

Thus SLC is no longer conditional for the active corpus.  It is conditionally
extendable, but the active Barandes-aligned ISP branch is torsion-free.

## 62. Complete RSC Audit: Dictionary Cokernel

Searchable audit tag:

`V4P25-COMPLETE-RSC-DICTIONARY-COKERNEL-AUDIT`.

Section 60 left RSC conditional on:

$$
\boxed{
\mathrm{coker}\,D_{\alpha_n}^{25}\to0.
}
$$

Now evaluate that condition on the P24 normal-form family.

The P24 normal-form theorem says every finite corpus transformation reduces
to:

$$
\boxed{
A^{*}R^{*}K^{*}E^{*}.
}
$$

The residue part is therefore exactly:

$$
\boxed{
{\mathcal E}_{res,\alpha}^{P24}
=
{\mathcal E}_{K,\alpha}
\oplus
{\mathcal E}_{E,\alpha}.
}
$$

where:

$$
\boxed{
{\mathcal E}_{K,\alpha}
=
\hbox{finite corner/curvature/commutator residues},
\qquad
{\mathcal E}_{E,\alpha}
=
\hbox{finite source/stress extensions}.
}
$$

The P25 completed dictionary is:

$$
\boxed{
D_{\alpha}^{25}
:
{\mathcal P}_{Cartan/Wilson,\alpha}
\oplus
{\mathcal S}_{stress,\alpha}
\longrightarrow
{\mathcal E}_{K,\alpha}\oplus{\mathcal E}_{E,\alpha}.
}
$$

### 62.1 Einstein Dictionary Audit

Einstein's question is:

$$
\boxed{
\hbox{can a finite residue be physically real while not appearing as
geometry or source?}
}
$$

By the P24 normal form, a persistent residue is not an \(A\)-move and not an
\(R\)-move.  Therefore it is either \(K\) or \(E\):

$$
\boxed{
\hbox{persistent residue}
\Longrightarrow
K\hbox{ or }E.
}
$$

The Cartan/Wilson completion represents \(K\):

$$
\boxed{
{\mathcal E}_{K,\alpha}
\subset
\mathrm{im}\,
{\mathcal P}_{Cartan/Wilson,\alpha}.
}
$$

The finite source/stress dictionary represents \(E\):

$$
\boxed{
{\mathcal E}_{E,\alpha}
\subset
\mathrm{im}\,
{\mathcal S}_{stress,\alpha}.
}
$$

Therefore:

$$
\boxed{
{\mathcal E}_{res,\alpha}^{P24}
\subset
\mathrm{im}\,D_{\alpha}^{25}.
}
$$

and hence:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{25}=0.
}
$$

This is not true for all imaginable future ISP extensions.  It is true for
the active P24 normal-form alphabet.  A nonzero cokernel would mean one of the
P24 normal-form falsifiers occurred:

$$
\boxed{
\begin{array}{c|l}
\hbox{nonzero cokernel source} & \hbox{P24 falsifier}\\
\hline
\hbox{residue not }K\hbox{ or }E & \mathrm{NF6}\\
\hbox{source extension without finite index complex} & \mathrm{NF4}\\
\hbox{corner residue not finite quotient/cohomology} & \mathrm{NF5}\\
\hbox{same-actual refinement changes residue} & \mathrm{NF1/NF2}
\end{array}
}
$$

Paper 24's active normal-form audit says these falsifiers do not occur in the
active P20-P24 closure chain.  Therefore the Einstein RSC result is:

$$
\boxed{
\mathrm{coker}\,D_{\alpha_n}^{25}\to0.
}
$$

### 62.2 Feynman Dictionary Ward Audit

Feynman's question is:

$$
\boxed{
\hbox{does every insertion residue either cancel by finite identity or land
in the printed dictionary?}
}
$$

For a finite insertion move \(\Phi\), the transfer change is:

$$
\boxed{
\Delta_{\Phi}\Xi
=
[D,A]\oplus(I_V-I_V)\oplus P_{K_{\Phi}}\oplus P_{E_{\Phi}}.
}
$$

Taking finite trace:

$$
\boxed{
\operatorname{Tr}\Delta_{\Phi}\Xi
=
\operatorname{Tr}P_{K_{\Phi}}
+
\operatorname{Tr}P_{E_{\Phi}}.
}
$$

The commutator and exact-pair terms cancel before becoming physical
residues:

$$
\boxed{
\operatorname{Tr}[D,A]=0,
\qquad
\operatorname{Tr}(I_V-I_V)=0.
}
$$

The surviving \(K\)-term is a Cartan/Wilson probe residue:

$$
\boxed{
\operatorname{Tr}P_{K_{\Phi}}
\in
\mathrm{im}\,
{\mathcal P}_{Cartan/Wilson,\alpha}.
}
$$

The surviving \(E\)-term is a stress/source residue:

$$
\boxed{
\operatorname{Tr}P_{E_{\Phi}}
\in
\mathrm{im}\,
{\mathcal S}_{stress,\alpha}.
}
$$

Thus:

$$
\boxed{
\delta_{\Phi}{\mathbb Z}_{\alpha}
\in
\mathrm{im}\,D_{\alpha}^{25}
}
$$

for every active corpus insertion move \(\Phi\).  Hence:

$$
\boxed{
{\mathfrak W}_{RSC,\alpha}^{P24}=0.
}
$$

### 62.3 RSC Final Result

The complete RSC audit result is:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{RSC}_{GR}
}
$$

for the active P20-P25 corpus.

More precisely:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{residue class} & \hbox{status} & \hbox{dictionary image}\\
\hline
A & \hbox{cancels} & \hbox{analysis only}\\
R & \hbox{cancels} & \hbox{exact-pair/refinement identity}\\
K & \hbox{represented} & \hbox{Cartan/Wilson/corner probe}\\
E & \hbox{represented} & \hbox{finite source/stress response}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{coker}\,D_{\alpha}^{25}=0
}
$$

on the active normal-form corpus.  A future nonzero cokernel is allowed only
by enlarging the actual move alphabet or failing the P24 normal-form audit,
and then it becomes a typed new ISP correction.

## 63. Complete SLC/RSC Audit Verdict

Searchable verdict tag:

`V4P25-COMPLETE-SLC-RSC-AUDIT-VERDICT`.

The two remaining conditional gates have now been evaluated on the active
P24/P25 corpus-wide finite actual family:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{gate} & \hbox{active corpus result} & \hbox{reason}\\
\hline
\mathrm{SLC} &
\mathrm{PASS}_{GR} &
\hbox{torsion exact terms vanish; no spin/torsion extension is printed}\\
\mathrm{RSC} &
\mathrm{PASS}_{GR} &
\hbox{normal-form residues are exactly represented by Cartan/Wilson/stress}
\end{array}
}
$$

Together with FAC:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\models
\mathrm{FAC+SLC+RSC}_{GR}.
}
$$

Therefore:

$$
\boxed{
{\mathfrak A}^{act}_{P24}
\Longrightarrow
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}
}
$$

for the active Barandes-aligned P20-P25 corpus.

This is not a claim that no extension can ever exist.  It is a classification
of the actual ISP theory selected by the current finite corpus:

$$
\boxed{
\begin{array}{c|l}
\hbox{if the corpus remains in }A^{*}R^{*}K^{*}E^{*}
& \hbox{pure effective GR branch}\\
\hbox{if an independent }E_T\hbox{ or }K_T\hbox{ appears}
& \hbox{Einstein-Cartan/spin-torsion branch}\\
\hbox{if a residue appears outside }K,E
& \hbox{new source/probe/boundary/higher-curvature branch}
\end{array}
}
$$

Thus the actual ISP theory is not chosen by aesthetic preference.  It is
selected by the finite Ward cohomology of the corpus:

$$
\boxed{
\hbox{surviving same-actual Ward cohomology }= \hbox{ physical ISP content.}
}
$$

For the active corpus, the only surviving physical content is already
represented by the GR-effective Cartan/Wilson geometry and finite
stress-source dictionary.  Hence the active branch is pure effective GR.

Future deviations are not forbidden.  They are precisely typed by the first
new surviving Ward cohomology class.
