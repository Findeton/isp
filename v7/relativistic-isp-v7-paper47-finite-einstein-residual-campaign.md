# Relativistic ISP v7 Paper XLVII: Finite Einstein Residual From Geometry-Irreducible Carriers

**Status:** analytic campaign note, not peer reviewed, version 2026-06-30.

## 0. Question

Paper XLVI closed the finite spacetime-carrier question:

$$
\boxed{
\text{selected carrier}
+\mathcal E^{GI}_B\le\epsilon_{GI}
\Longleftrightarrow_{\rm finite}
\text{stable finite spacetime packet}.
}
$$

But a stable finite spacetime packet is not yet Einstein dynamics.

The next question is:

$$
\boxed{
\text{when does the finite spacetime packet obey an Einstein-like
curvature/source law?}
}
$$

This paper attacks that question.

## 1. Executive Result

The campaign defines a finite, record-intrinsic Einstein residual:

$$
\boxed{
\mathcal E^{Ein}_B(K)
}
$$

for a selected geometry-irreducible carrier `K`.  It compares:

1. a finite curvature/Einstein-tensor packet;
2. a finite typed source/stress packet;
3. a finite cosmological/integration-constant packet;
4. untyped Ward/Bianchi residue;
5. unresolved higher-curvature, torsion, boundary, and history-tail residue.

The main finite theorem is:

$$
\boxed{
\begin{gathered}
\text{geometry-irreducible selected carrier}\\
+\text{licensed scale anchors}\\
+\text{typed source/stress packet}\\
+\text{interior stationarity of boundary work}\\
+\text{separating carrier variations}\\
\Longrightarrow
\mathcal E^{Ein}_B(K)\le\epsilon_{Ein}.
\end{gathered}
}
$$

The theorem is deliberately finite.  It does not derive the numerical value of
Newton's constant from pure order.  It says when a bounded record-history
packet is allowed to claim an Einstein-like finite dynamics.

## 2. Inputs From Earlier Papers

From Paper XLV, the click law selects minimal admissible carriers:

$$
\boxed{
K_B^\star
=
\operatorname*{Argmin}_{K\in\operatorname{Adm}_B}
\mathcal A_B^{sel}(H,K;\mathcal Y_B).
}
$$

From Paper XLVI, a selected carrier is spacetime-like when:

$$
\boxed{
\mathcal E^{GI}_B(K_B^\star)\le\epsilon_{GI}.
}
$$

From Paper 39, the finite spacetime packet is:

$$
\boxed{
I_{GR}^{cl}
=
(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r).
}
$$

The pieces are:

- `\mathsf A`: finite same-actual atlas;
- `\mathsf Q`: interval, shell, volume, and dimension summaries;
- `\mathsf U`: overlap transport;
- `\mathsf F`: loop/curvature packet;
- `\mathsf W`: Ward/Bianchi packet;
- `\mathsf\Theta`: typed source/stress dictionary;
- `\mathsf r`: refinement/history-drift maps.

Paper XLVII assumes `I_{GR}^{cl}` is licensed.  It asks whether the licensed
packet obeys a finite Einstein residual.

## 3. Einstein-Ready Carrier

A selected carrier `K` is Einstein-ready at tolerance `\epsilon` if:

$$
\boxed{
K\in K_B^\star,
\qquad
\mathcal E^{GI}_B(K)\le\epsilon_{GI},
}
$$

and the following extra gates pass:

1. scale anchors license `G_B`;
2. source/stress residues are typed into `\Theta_B`;
3. curvature residues define a finite Einstein-tensor proxy;
4. Ward/Bianchi residues are either typed or below tolerance;
5. carrier variations separate physical residuals on the same-actual quotient;
6. the selected carrier is an interior minimizer, not a boundary/critical
   failure.

Write:

$$
\boxed{
K\in\operatorname{EinReady}_B(\epsilon).
}
$$

If this class is empty, the bounded region may still have a spacetime carrier,
but it does not yet support Einstein dynamics.

## 4. Scale Anchors And `G_B`

Pure record order fixes ratios, not absolute units.  Therefore a finite
gravitational scale needs anchors:

$$
\boxed{
\mathcal S_B=(s_\ell,s_t,s_m,s_\hbar).
}
$$

Here:

- `s_\ell`: length/volume anchor;
- `s_t`: clock/time anchor;
- `s_m`: mass/source normalization anchor;
- `s_\hbar`: action/phase normalization anchor.

The finite Newton coupling is:

$$
\boxed{
G_B
=
\Gamma_G(I_{GR}^{cl},\mathcal S_B).
}
$$

The gate is:

$$
\boxed{
\operatorname{Lic}_G(B)=1
\quad\Longleftrightarrow\quad
\mathcal S_B\text{ has enough independent anchors and denominator floors}.
}
$$

### Theorem 1: Scale No-Go And Scale Gate

Without source/mass and geometric/action anchors, the numerical `G_B` is a
unit gauge.  With finite anchors and denominator floors, `G_B` is a finite
packet functional.

**Proof.**

If anchors are absent, rescale source normalization and geometric units
together.  Dimensionless interval and curvature ratios are unchanged while
the numerical value assigned to `G_B` changes.  If anchors are printed and
denominators have floors, the rescaling freedom is fixed, and `G_B` is
computed by the finite regularized functional `\Gamma_G`. `\square`

### 4.1 Consequence

Einstein form can be record-intrinsic before the absolute numerical value of
Newton's constant is known.  Numerical `G_B` is licensed only after scale
anchors are printed.

## 5. Finite Curvature Packet

The curvature packet comes from loop/overlap transport in the finite atlas.
For a loop `\gamma` in the overlap graph:

$$
\boxed{
F_B(\gamma)
=
U_{\alpha_0\alpha_1}
\cdots
U_{\alpha_{n-1}\alpha_n}.
}
$$

The finite curvature vector/tensor proxy is a centered contraction of loop
defects:

$$
\boxed{
\mathcal R_B^{fin}
=
\operatorname{Curv}_B(\mathsf A,\mathsf U,\mathsf F,\mathsf Q).
}
$$

This is not assumed to be a smooth Riemann tensor.  It is the finite packet
that becomes a curvature tensor only after representation gates pass.

The finite Einstein-tensor proxy is:

$$
\boxed{
\mathcal G_B^{fin}
=
\operatorname{Ein}_B(\mathcal R_B^{fin},\mathsf Q,\mathsf W).
}
$$

where `\operatorname{Ein}_B` is the unique finite contraction available after
same-actual covariance, Ward/Bianchi balance, and the selected packet
normalizations are fixed.

### Theorem 2: Curvature Proxy Is Record-Covariant

If atlas, overlap transport, loop defects, and center-shell summaries are
record-covariant, then `\mathcal R_B^{fin}` and `\mathcal G_B^{fin}` are
record-covariant packet functionals.

**Proof.**

Record isomorphisms transport diamonds, overlaps, loops, and center summaries.
The construction of `\operatorname{Curv}_B` and `\operatorname{Ein}_B` uses
only those transported objects and same-actual quotienting.  Therefore the
result transports covariantly. `\square`

## 6. Typed Source/Stress Packet

The source packet is:

$$
\boxed{
\Theta_B^{fin}
=
\operatorname{Src}_B(\mathsf\Theta,\mathsf W,\mathcal S_B).
}
$$

It includes only source/stress residues that are:

1. typed by stable record sectors;
2. additive under gluing of bounded diamonds;
3. projectively stable under history refinement;
4. linked to Ward/Bianchi residue;
5. normalized by scale anchors when numerical coupling is claimed.

Untyped source residue is not hidden.  It enters:

$$
\boxed{
W_B^{untyped}.
}
$$

### Theorem 3: Untyped Source Cannot Imitate Einstein Matter

If a source residue affects curvature or click predictions above tolerance but
is not typed into `\Theta_B^{fin}`, then the finite Einstein residual is
above tolerance.

**Proof.**

No-silent accounting requires above-tolerance source residue to be printed.
If it is not typed into the source packet, it remains in `W_B^{untyped}`.
The Einstein residual includes the norm of that untyped residue. `\square`

## 7. Cosmological/Integration-Constant Packet

Finite Einstein form should allow a trace/constant term:

$$
\boxed{
\Lambda_B^{fin}\mathfrak g_B^{fin}.
}
$$

Here:

- `\mathfrak g_B^{fin}` is the finite metric/volume pairing extracted from
  `\mathsf Q`;
- `\Lambda_B^{fin}` is an integration-constant or vacuum-source packet
  component.

It is licensed only if it is stable under bounded-history refinement:

$$
\boxed{
\Delta_B(\Lambda)
=
\sum_j
\left|\Lambda_{B,j+1}^{fin}-\rho_{j+1\to j}^{\ast}\Lambda_{B,j}^{fin}\right|
\le\epsilon_\Lambda.
}
$$

### Theorem 4: Cosmological Term Is A Separate Packet Channel

The finite cosmological term cannot be silently absorbed into curvature or
source without a typed residue.

**Proof.**

Changing `\Lambda_B^{fin}` changes the trace/uniform source response while
leaving local loop curvature differences partly unchanged.  If this change is
above tolerance, no-silent accounting demands a printed channel.  Therefore it
is either a licensed cosmological packet or an untyped residue charged by the
Einstein residual. `\square`

## 8. Finite Einstein Residual

Define:

$$
\boxed{
\mathcal E_B^{Ein}(K)
=
\left\|
\mathcal G_B^{fin}
+\Lambda_B^{fin}\mathfrak g_B^{fin}
-8\pi G_B\Theta_B^{fin}
\right\|_{B}
+\|W_B^{untyped}\|
+\|R_B^{typed}\|
+\|R_B^{tail}\|.
}
$$

The pieces are:

- first term: finite curvature/source mismatch;
- `W_B^{untyped}`: untyped Ward/Bianchi/source residue;
- `R_B^{typed}`: typed higher-curvature, torsion, anomaly, or matter-sector
  residue not belonging to the Einstein sector;
- `R_B^{tail}`: unresolved bounded-history tail.

The Einstein phase is:

$$
\boxed{
\mathcal E_B^{Ein}(K_B^\star)\le\epsilon_{Ein}.
}
$$

Small Einstein residual means the selected spacetime carrier is not just an
arena.  Its curvature and source packets obey the finite Einstein relation at
the requested tolerance.

## 9. Variational Origin

Let `u` be an admissible carrier variation of the selected spacetime packet.
It changes atlas/metric/source components while respecting same-actual
quotienting and no-silent constraints.

The selected total action is:

$$
\boxed{
\mathcal A_B^{tot}(H,K)
=
\mathcal A_B^{sel}(H,K;\mathcal Y_B)
+\alpha_{GI}\mathcal E_B^{GI}(K)
+\alpha_{src}\operatorname{UntypedSrc}_B(K).
}
$$

At an interior minimizer:

$$
\boxed{
|\delta_u\mathcal A_B^{tot}|
\le
\epsilon_{var}\|u\|.
}
$$

The first variation splits as:

$$
\boxed{
\delta_u\mathcal A_B^{tot}
=
\left\langle
\mathcal G_B^{fin}
+\Lambda_B^{fin}\mathfrak g_B^{fin}
-8\pi G_B\Theta_B^{fin},
u
\right\rangle
+\langle W_B^{untyped}+R_B^{typed}+R_B^{tail},u\rangle
+O(\|u\|^2).
}
$$

### Theorem 5: Stationarity Gives Finite Einstein Residual

Assume:

1. `K` is Einstein-ready;
2. `K` is an interior minimizer of `\mathcal A_B^{tot}`;
3. admissible variations separate residuals on the same-actual quotient;
4. second variation is bounded on the selected packet;
5. `G_B` and `\Lambda_B^{fin}` are licensed;
6. untyped residues are charged.

Then:

$$
\boxed{
\mathcal E_B^{Ein}(K)
\le
C_B\epsilon_{var}+C'_B\|u\|^2.
}
$$

In the finite linearized tolerance regime:

$$
\boxed{
\mathcal E_B^{Ein}(K)\le\epsilon_{Ein}.
}
$$

**Proof.**

Interior stationarity bounds the first variation against every admissible
direction.  Separating variations imply that a nonzero residual has some
direction detecting it.  The first variation formula identifies the detected
linear functional with the Einstein residual plus charged typed/tail
residues.  The bounded second variation controls the remainder. `\square`

## 10. Boundary Minima And Critical Regimes

If the minimizer lies on the boundary of admissibility, stationarity does not
imply Einstein residual smallness.

Boundary cases include:

1. horizon-like incomplete boundary;
2. singular/critical geometry;
3. missing source records;
4. unlicensed scale anchors;
5. raw/nonlookup failure;
6. geometry-to-algebraic phase transition.

### Theorem 6: Boundary Minima Are Not Einstein Closure

If `K_B^\star` is a boundary minimizer of the admissible class, the finite
Einstein residual need not be small.

**Proof.**

At a boundary minimizer, the first-variation condition is replaced by a
one-sided variational inequality or a constraint multiplier.  The residual may
be balanced by missing directions or active constraints rather than vanish.
The correct conclusion is boundary expansion, constraint typing, or critical
phase classification. `\square`

## 11. Higher-Curvature And Typed Residues

The finite residual must not force all non-Einstein response into the Einstein
side.

Define typed residual channels:

$$
\boxed{
R_B^{typed}
=
R_B^{HC}
+R_B^{tors}
+R_B^{anom}
+R_B^{matter}
+R_B^{bdry}.
}
$$

These represent:

- higher-curvature finite response;
- torsion-like carrier asymmetry;
- anomaly/Ward failure;
- matter-sector corrections;
- boundary/collar terms.

### Theorem 7: Typed Residues Prevent False Einstein Closure

If a stable above-tolerance residual is not of Einstein curvature/source type,
it must be typed outside the Einstein sector or charged as untyped residue.

**Proof.**

No-silent accounting forbids hiding stable residuals.  If the residual cannot
be represented as `\mathcal G+\Lambda\mathfrak g-8\pi G\Theta`, placing it on
the Einstein side would produce false closure.  The typed channel records it
without pretending it is Einstein dynamics. `\square`

## 12. Projective Einstein Stability

Einstein residual smallness must persist through bounded-history refinement.

Define:

$$
\boxed{
\Delta_B^{Ein}(K)
=
\sum_j
d_{Ein}\left(
\mathcal E_{B,j+1}^{Ein},
\rho_{j+1\to j}^{\ast}\mathcal E_{B,j}^{Ein}
\right).
}
$$

The projective Einstein gate is:

$$
\boxed{
\mathcal E_B^{Ein}(K)\le\epsilon_{Ein},
\qquad
\Delta_B^{Ein}(K)\le\epsilon_\Delta.
}
$$

### Theorem 8: One-Slice Einstein Closure Is Insufficient

A carrier that has small Einstein residual on one slice but unstable
projective residual does not license Einstein dynamics for the bounded
history.

**Proof.**

The click law is history-first.  Dynamics cannot be read from one slice alone.
If refinement/deletion changes the residual above tolerance, the claimed
Einstein relation is not stable under the bounded history cylinder. `\square`

## 13. Finite Einstein Phase Criterion

Define the Einstein defect:

$$
\boxed{
\mathcal F_B^{Ein}(K)
=
\mathcal E_B^{GI}(K)
+\chi_G(1-\operatorname{Lic}_G(B))
+\mathcal E_B^{Ein}(K)
+\Delta_B^{Ein}(K)
+\operatorname{UntypedSrc}_B(K).
}
$$

The selected carrier is in the finite Einstein phase when:

$$
\boxed{
\mathcal F_B^{Ein}(K_B^\star)\le\epsilon_F.
}
$$

### Theorem 9: Finite Einstein Phase

For a selected bounded-history carrier, finite Einstein dynamics is licensed
exactly when:

1. it is geometry-irreducible;
2. scale anchors license `G_B`;
3. source/stress residues are typed;
4. Einstein residual is below tolerance;
5. Einstein residual is projectively stable.

Equivalently:

$$
\boxed{
\mathcal F_B^{Ein}(K_B^\star)\le\epsilon_F.
}
$$

**Proof.**

The five listed requirements are exactly the summands of
`\mathcal F_B^{Ein}`.  If any summand is above tolerance, either spacetime is
not licensed, scale is unlicensed, sources are hidden, curvature/source
mismatch is large, or the relation is not stable across the history.  If all
are below tolerance, the finite Einstein packet is licensed by definition and
by Theorem 5's variational origin when stationarity is available. `\square`

## 14. Adversarial Campaign

### 14.1 Stable Geometry With Wrong Source Response

Adversary: a carrier passes geometry-irreducibility but source residues do not
match curvature.

Result: `\mathcal E_B^{Ein}` is large.  Spacetime exists, Einstein dynamics
fails.

### 14.2 Source Packet Without Curvature Response

Adversary: typed matter/source residues are printed, but loop curvature
packet remains flat or unresponsive.

Result: finite source packet exists, but Einstein residual is large unless the
source is pure gauge/same-actual or balanced by typed non-Einstein channels.

### 14.3 Pure Topological Curvature

Adversary: loop defects are topological/global and do not couple to local
source/stress.

Result: type as `R_B^{typed}` or cosmological/topological channel.  Do not
claim Einstein closure.

### 14.4 Hidden Density Modulation

Adversary: density clusters mimic curvature or source.

Result: Paper XLVI's density regularity gate rejects hidden modulation unless
it is printed as source/curvature.  If printed, it contributes to
`\Theta_B^{fin}` or `R_B^{typed}`.

### 14.5 Scale-Anchor Spoofing

Adversary: choose anchors that force any desired `G_B`.

Result: anchors must be record-realized, projectively stable, and independent.
If changing anchor convention changes `G_B` without changing record physics,
`G_B` is unlicensed.

### 14.6 QFT-Like Source With No Stress Closure

Adversary: local excitation labels exist, but no conserved stress/source
packet closes.

Result: this may be a pre-QFT typed phase, not an Einstein source.  It remains
in `R_B^{typed}` or `W_B^{untyped}`.

### 14.7 Boundary/Horizon Region

Adversary: residual is large only because the bounded region excludes relevant
source/boundary records.

Result: boundary expansion is required.  The paper does not call this
Einstein failure of the universe; it calls it failure of the chosen bounded
problem.

### 14.8 Algebraic Carrier With Formal Curvature

Adversary: a Cayley-like algebraic carrier defines loop defects that look like
curvature.

Result: unless it first passes geometry-irreducibility, its loop defects are
not GR curvature.  They may be algebraic phase residues.

## 15. Hostile Review Round I

### Review 1: "This assumes a finite Einstein tensor proxy."

Accepted.  The proxy exists only after geometry-irreducibility supplies atlas,
overlap, loop, and Ward packets.  Before that, `\mathcal G_B^{fin}` is
unlicensed.

### Review 2: "Stationarity is stronger than the click law."

Accepted.  Click prediction requires positive bounded-history weights.
Einstein dynamics requires an interior stationary spacetime/source carrier.
This is an extra phase condition.

### Review 3: "You still do not derive Newton's constant."

Accepted.  Pure order/record ratios do not give an absolute `G`.  The paper
derives the finite scale gate and `G_B` functional once anchors are printed.
The continuum value requires calibrated convergence.

### Review 4: "A cosmological constant can absorb errors."

Partly.  A stable uniform trace channel can be typed as `\Lambda_B`.  It
cannot absorb nonuniform, source-dependent, or untyped residual without being
charged.

### Review 5: "Higher-curvature gravity might be the right dynamics."

Accepted as an allowed typed phase.  The Einstein phase is the low-residue
sector where higher-curvature/torsion/anomaly channels are below tolerance or
irrelevant at the selected scale.

### Review 6: "This is still finite, not continuum GR."

Correct.  Continuum GR requires a projective sequence with
`\mathcal F_B^{Ein}\to0`, scale convergence, and representation gates.

## 16. Opening Follow-Up A: Low-Energy Einstein Uniqueness

The finite residual should explain why the Einstein form is selected when it
is selected.

Assume a low-energy carrier variation class:

$$
\boxed{
\mathcal V_B^{low}
}
$$

with:

1. same-actual covariance;
2. finite second-order carrier response;
3. Ward/Bianchi divergence constraint;
4. no untyped higher-curvature residues above tolerance;
5. scale-licensed source coupling.

### Theorem 10: Finite Low-Energy Einstein Form

Within `\mathcal V_B^{low}`, the only untyped rank-two curvature/source
residual compatible with finite Ward/Bianchi balance is:

$$
\boxed{
\mathcal G_B^{fin}
+\Lambda_B^{fin}\mathfrak g_B^{fin}
-8\pi G_B\Theta_B^{fin}
}
$$

up to below-tolerance same-actual and typed residual channels.

**Proof.**

The finite Ward/Bianchi constraint removes non-divergence-free curvature
responses.  Same-actual covariance removes presentation artifacts.  The
low-energy gate excludes higher-curvature/torsion/anomaly channels from the
untyped sector.  The remaining rank-two response space is spanned by the
finite Einstein proxy, the metric/trace packet, and the typed source packet.
Scale anchors fix the coupling.  The theorem is finite and conditional on the
listed low-energy carrier variation class. `\square`

### 16.1 Hostile Review

This is the finite analog of a Lovelock/Noether-style uniqueness claim.  It is
not a full proof of the continuum theorem.  Its honest role is to identify the
finite gates under which the Einstein residual is the correct untyped
low-energy residual.

## 17. Opening Follow-Up B: Continuum Limit

For a projective sequence `B_n`, define:

$$
\boxed{
\mathcal F_{B_n}^{Ein}\to0,
\qquad
G_{B_n}\to G_\infty,
\qquad
\Lambda_{B_n}\to\Lambda_\infty.
}
$$

If representation gates also pass, the limiting candidate satisfies:

$$
\boxed{
G[g]+\Lambda_\infty g
=
8\pi G_\infty T
}
$$

in the represented continuum sense.

### Theorem 11: Finite-To-Continuum Einstein Gate

If a projective bounded-history sequence has vanishing finite Einstein defect,
convergent scale anchors, and a causal-measure-atlas-curvature representation
limit, then its limiting represented packet satisfies the Einstein equation in
that representation.

**Proof.**

The finite residual is the packet-level difference between curvature,
cosmological, and source sides plus typed/tail residue.  Vanishing residual
and representation convergence send each finite packet component to its
continuum representative.  The limit of zero residual is the represented
Einstein equation. `\square`

### 17.1 Hostile Review

The hard part is external representation convergence.  This theorem is a
handoff: it says exactly what finite quantities must converge, not that every
selected carrier sequence converges.

## 18. Opening Follow-Up C: QFT Handoff

Einstein readiness is still not QFT.  It supplies:

1. stable finite spacetime packet;
2. scale-licensed `G_B`;
3. typed source/stress residues;
4. Ward/Bianchi conservation channels.

QFT needs an additional typed local algebra and state/amplitude structure.

Define the QFT handoff data:

$$
\boxed{
\mathcal QFTGate_B
=
(I_{GR}^{cl},\Theta_B^{fin},\mathcal A_T(D),\omega_D,\mathfrak M_D).
}
$$

This is licensed only if finite Einstein residual is small or the theory is
explicitly in a pre-Einstein typed-source regime.

### Theorem 12: Einstein Gate Precedes Standard QFT On Spacetime

For ordinary QFT-on-spacetime interpretation, finite Einstein readiness is a
background/source consistency gate, but not a construction of QFT.

**Proof.**

QFT requires local algebras, states, amplitudes, and microcausal or
record-causal compatibility.  Einstein readiness supplies only the stable
spacetime/source background on which those objects may be defined. `\square`

## 19. Hostile Review Round II

### Review 7: "What if the real dynamics is not Einstein?"

Then the selected carrier may fail `\mathcal F_B^{Ein}` while passing a
different typed dynamics residual.  The framework classifies that as a
non-Einstein geometric phase, not as failure of the click law.

### Review 8: "What if `G_B` changes with scale?"

Then projective Einstein stability fails unless the running is printed as a
typed coupling-flow channel.  A running coupling can be physical, but not
silent.

### Review 9: "What if no source exists, vacuum only?"

Then `\Theta_B^{fin}=0` and the residual tests vacuum/cosmological Einstein
form:

$$
\boxed{
\mathcal G_B^{fin}+\Lambda_B^{fin}\mathfrak g_B^{fin}\approx0.
}
$$

### Review 10: "What if stress energy is quantum?"

Then the source packet must be expectation-like, inclusive, or typed by the
finite QFT sector.  Until that sector is licensed, the quantum source remains
typed residue rather than classical Einstein matter.

### Review 11: "Does this prove GR from Barandes-style histories?"

No.  It proves the finite gate: if the history-first carrier selector enters a
geometry-irreducible, scale-licensed, stationary source/curvature phase, then
the finite residual has Einstein form.  The histories are the substrate; GR is
a later stable phase condition.

## 20. Interim Result Before Five-Blocker Closure

Before the five-blocker campaign, Paper XLVII had established the next layer
after Paper XLVI:

$$
\boxed{
\text{click law}
\to
\text{geometry-irreducible carrier}
\to
\text{finite Einstein residual}.
}
$$

The finite Einstein phase is:

$$
\boxed{
\mathcal F_B^{Ein}(K_B^\star)\le\epsilon_F.
}
$$

Expanded:

$$
\boxed{
\begin{gathered}
\text{geometry-irreducible selected carrier}\\
+\text{licensed }G_B\\
+\text{typed source/stress packet}\\
+\text{small curvature/source residual}\\
+\text{projective residual stability}
\\
\Longleftrightarrow_{\rm finite}
\text{Einstein-ready spacetime phase}.
\end{gathered}
}
$$

This is not QFT.  It is the finite GR dynamics gate needed before ordinary
QFT-on-spacetime becomes well posed.

Before attacking QFT, the Einstein blockers must be closed more sharply.
Section 21 follows that opening immediately:

$$
\boxed{
\text{stationarity, scale anchors, source typing, typed residual separation,
and projective Einstein stability.}
}
$$

## 21. Five-Blocker Closure Campaign

The direct blockers for finite Einstein dynamics are:

1. interior stationarity of the selected carrier action;
2. scale anchors sufficient to license `G_B`;
3. typed source/stress packet extraction;
4. separation of Einstein residual from higher-curvature/anomaly/torsion
   residue;
5. projective stability of the Einstein residual across bounded histories.

This section works on all five.

The target is not continuum GR.  The target is the finite implication:

$$
\boxed{
\text{five blockers closed}
\Longrightarrow
\mathcal F_B^{Ein}(K_B^\star)\le\epsilon_F.
}
$$

## 22. Blocker 1: Interior Stationarity

Let:

$$
\boxed{
\mathcal V_B(K)
}
$$

be the finite cone of admissible carrier variations preserving:

1. same-actual quotienting;
2. no-silent completeness;
3. geometry-irreducibility gates already below tolerance;
4. the bounded history cylinder;
5. active source/scale typing.

Let `\partial\operatorname{Adm}_B` be the boundary of the admissible carrier
class.  Define the stationarity defect:

$$
\boxed{
\operatorname{Stat}_B(K)
=
\sup_{\substack{u\in\mathcal V_B(K)\\ \|u\|=1}}
\left|\delta_u\mathcal A_B^{tot}(H,K)\right|.
}
$$

Define the active-boundary obstruction:

$$
\boxed{
\operatorname{Act}_B(K)
=
\operatorname{dist}(K,\partial\operatorname{Adm}_B)^{-1}
}
$$

with the convention that it is large when `K` lies on the boundary.

### Theorem 13: Stationarity Dichotomy

Let `K\in K_B^\star` be a selected geometry-irreducible carrier.  Then exactly
one of the following finite alternatives holds:

1. `K` is an interior minimizer and `\operatorname{Stat}_B(K)\le\epsilon`;
2. `K` is a boundary minimizer and an active obstruction is printed:
   missing boundary, raw/nonlookup failure, scale unlicensed, source untyped,
   phase tie, or critical/singular response.

**Proof.**

The admissible carrier class is finite after same-actual/subraw quotienting,
but each selected carrier has a finite local variation cone.  If all small
admissible variations remain inside the carrier class, minimality gives
zero first variation up to tolerance.  If some required variation is blocked,
then the carrier lies on an active admissibility boundary.  No-silent
accounting requires the active constraint to be printed as one of the listed
obstructions. `\square`

### 22.1 Residual Consequence

If the variation pairing separates residuals:

$$
\boxed{
\|R\|_B
\le
C_{\rm sep}
\sup_{\|u\|=1}|\langle R,u\rangle|,
}
$$

then:

$$
\boxed{
\mathcal E_B^{Ein}(K)
\le
C_{\rm sep}\operatorname{Stat}_B(K)
+O(\|u\|^2)
+\text{typed/tail residue}.
}
$$

Thus the real stationarity theorem is not "every selected carrier is
stationary."  It is:

$$
\boxed{
\text{selected carrier is either stationary or visibly boundary-obstructed.}
}
$$

This closes the first blocker at finite tolerance.

### 22.2 Hostile Review

**Objection:** a selected carrier can be discrete, so derivatives may not
exist.

Accepted.  In that case replace `\delta_u` by finite differences over
admissible moves:

$$
\boxed{
\operatorname{Stat}^{disc}_B(K)
=
\sup_{K'\sim K}
\frac{|\mathcal A_B^{tot}(K')-\mathcal A_B^{tot}(K)|}
{d_K(K,K')}.
}
$$

The dichotomy becomes finite-difference stationarity versus active boundary
obstruction.

## 23. Blocker 2: Scale Anchor Rank

Scale anchors are not optional if a numerical `G_B` is claimed.

Let `\mathcal U_B` be the finite unit-rescaling group acting on:

$$
\boxed{
(\ell,t,m,\hbar,G,\Theta,\mathcal G).
}
$$

Let:

$$
\boxed{
\mathcal S_B=(s_1,\ldots,s_q)
}
$$

be printed anchor readings.  Define the anchor response matrix:

$$
\boxed{
\mathsf A^{scale}_{ij}
=
\frac{\partial\log s_i}{\partial\log u_j}
}
$$

where `u_j` ranges over independent unit-rescaling directions.

The scale-anchor defect is:

$$
\boxed{
\operatorname{ScaleDef}_B
=
\dim\ker\mathsf A^{scale}_{G}
}
$$

where the subscript `G` means the kernel directions that still change the
numerical value of `G_B`.

### Theorem 14: Anchor-Rank Criterion For `G_B`

`G_B` is licensed if and only if:

$$
\boxed{
\operatorname{ScaleDef}_B=0
}
$$

and all anchor denominators have finite floors.

If `\operatorname{ScaleDef}_B>0`, only the dimensionless Einstein form is
licensed.

**Proof.**

If a rescaling direction lies in the anchor kernel but changes `G_B`, then all
printed anchors are unchanged while the numerical coupling changes.  Therefore
`G_B` is gauge.  Conversely, if no such direction remains and denominators
have floors, the unit gauge is fixed by printed records and `G_B` is a finite
regularized packet functional. `\square`

### 23.1 Running Couplings

If `G_B` changes under history depth:

$$
\boxed{
G_{B,j+1}-\rho_{j+1\to j}^{\ast}G_{B,j}\ne0,
}
$$

then the running must be printed as a typed coupling-flow residue:

$$
\boxed{
R_B^{G{\rm -flow}}.
}
$$

Otherwise projective Einstein stability fails.

## 24. Blocker 3: Typed Source/Stress Packet

Let:

$$
\boxed{
\mathscr S_B
}
$$

be the finite vector space or module of source-sensitive no-silent residues.
Let:

$$
\boxed{
\partial_W:\mathscr S_B\to\mathscr W_B
}
$$

be the finite Ward/Bianchi boundary map.  A typed source dictionary is:

$$
\boxed{
\Theta_B=(\tau_i,\theta_i,\partial_W\theta_i)_{i\in I}.
}
$$

with:

1. stable type labels `\tau_i`;
2. additive source components `\theta_i`;
3. Ward/Bianchi images `\partial_W\theta_i`;
4. projective refinement maps.

Define source typing defect:

$$
\boxed{
\operatorname{SrcDef}_B
=
\inf_{\Theta}
\left(
\|s_B-\sum_i\theta_i\|
+\|\partial_Ws_B-\sum_i\partial_W\theta_i\|
+\Delta_B(\Theta)
+C_{\rm nonlookup}(\Theta)
\right).
}
$$

### Theorem 15: Source Typing Dichotomy

Every above-tolerance source-sensitive residue is in exactly one finite class:

1. typed source/stress packet `\Theta_B^{fin}`;
2. typed non-Einstein residue `R_B^{typed}`;
3. untyped residue charged in `W_B^{untyped}`;
4. boundary-incomplete residue requiring boundary/history expansion.

**Proof.**

No-silent accounting forbids omission.  If the residue has a stable additive
type and Ward-compatible refinement, it enters `\Theta_B^{fin}`.  If stable
but not Einstein-source-like, it enters `R_B^{typed}`.  If visible but
untyped, it is charged as `W_B^{untyped}`.  If it cannot be represented
without external records, the bounded problem is incomplete.  These cases are
exhaustive by no-silent closure. `\square`

### 24.1 Quantum Or Inclusive Sources

If the source is quantum/inclusive, the source component may be an
expectation-like or inclusive packet:

$$
\boxed{
\Theta_B^{fin}
=
\mathbb E_{\omega_B}[\Theta_B]
}
$$

but the state `\omega_B` must be printed by a finite typed sector.  Otherwise
the source remains typed residue, not classical Einstein matter.

## 25. Blocker 4: Einstein Versus Typed Residual Separation

Let:

$$
\boxed{
\mathscr R_B
}
$$

be the finite residual space after geometry-irreducibility and source typing.
It contains curvature/source residuals, higher-curvature responses, torsion,
anomalies, matter-sector residue, and boundary terms.

Define the Einstein subspace:

$$
\boxed{
\mathscr E_B
=
\operatorname{span}
\left\{
\mathcal G_B^{fin},
\mathfrak g_B^{fin},
\Theta_B^{fin}
\right\}.
}
$$

Let:

$$
\boxed{
P_E:\mathscr R_B\to\mathscr E_B
}
$$

be the finite projection induced by the packet norm, when the separation gap:

$$
\boxed{
\operatorname{gap}_E(B)
=
\inf_{\substack{r\in\mathscr E_B\\ c\in\mathscr E_B^\perp}}
\frac{\|r-c\|}{\|r\|+\|c\|}
}
$$

is positive.

### Theorem 16: Residual Separation Theorem

If `\operatorname{gap}_E(B)>0`, every finite residual has a unique stable
decomposition:

$$
\boxed{
R_B
=
R_B^{Ein}
+R_B^{typed}
+R_B^{tail}
}
$$

up to same-actual tolerance.  The Einstein residual is the component
`R_B^{Ein}=P_E(R_B)`.

If `\operatorname{gap}_E(B)=0`, Einstein and non-Einstein residuals are not
separable at this tolerance.

**Proof.**

A positive gap makes the finite projection onto `\mathscr E_B` stable under
small perturbations.  Thus the Einstein component and typed complement are
well-defined.  If the gap is zero, arbitrarily small perturbations can move
residue between the Einstein subspace and typed complement, so no stable
Einstein claim is licensed. `\square`

### 25.1 Consequence

Higher-curvature gravity is not falsely rejected.  It is represented by a
typed residual channel unless it is below tolerance in the selected
low-energy sector.

## 26. Blocker 5: Projective Einstein Stability

Let the finite Einstein residual at history depth `j` be:

$$
\boxed{
E_j
=
\mathcal G_{B,j}^{fin}
+\Lambda_{B,j}^{fin}\mathfrak g_{B,j}^{fin}
-8\pi G_{B,j}\Theta_{B,j}^{fin}.
}
$$

Let:

$$
\boxed{
\rho_{j+1\to j}^{Ein}
}
$$

be the projective map induced by record deletion/refinement.

Define:

$$
\boxed{
\Delta_B^{Ein}
=
\sum_{j=N-k}^{N-1}
\left\|
E_j-\rho_{j+1\to j}^{Ein}(E_{j+1})
\right\|.
}
$$

### Theorem 17: Projective Stability Criterion

If:

$$
\boxed{
\Delta_B^{Ein}\le\epsilon_\Delta,
}
$$

then the finite Einstein residual is a bounded-history property rather than a
one-slice coincidence.

If the sum diverges or remains above tolerance, Einstein dynamics is not
licensed on the bounded history.

**Proof.**

The bounded-history law is non-Markovian.  A dynamical relation must persist
under the projective maps connecting the history cylinder.  The displayed sum
is exactly the accumulated mismatch of the residual under those maps.  If it
is small, the relation is projectively stable; if not, the relation is not a
history-stable property. `\square`

### 26.1 Tail Bound Sufficient Condition

If:

$$
\boxed{
\left\|
E_j-\rho_{j+1\to j}^{Ein}(E_{j+1})
\right\|
\le
C\theta^j,\qquad 0<\theta<1,
}
$$

then:

$$
\boxed{
\Delta_B^{Ein}
\le
\frac{C\theta^{N-k}}{1-\theta}.
}
$$

Thus a finite response-tail theorem implies projective Einstein stability.

## 27. Combined Five-Blocker Theorem

Define the closed Einstein blocker defect:

$$
\boxed{
\mathcal B_B^{Ein}(K)
=
\operatorname{Stat}_B(K)
+\operatorname{ScaleDef}_B
+\operatorname{SrcDef}_B
+\operatorname{gap}_E(B)^{-1}_{bad}
+\Delta_B^{Ein}.
}
$$

Here `\operatorname{gap}_E^{-1}_{bad}` is zero when the separation gap is above
tolerance and large when the gap collapses.

### Theorem 18: Five-Blocker Closure

Let `K\in K_B^\star` be a selected geometry-irreducible carrier.  If:

$$
\boxed{
\mathcal B_B^{Ein}(K)\le\epsilon_B
}
$$

and untyped residues are charged by the finite Einstein residual, then:

$$
\boxed{
\mathcal F_B^{Ein}(K)\le C\epsilon_B+\epsilon_{\rm typed}.
}
$$

Conversely, if any of the five blocker defects is above tolerance, finite
Einstein dynamics is not licensed at `B` without boundary expansion, source
typing, scale anchoring, residual typing, or phase refinement.

**Proof.**

Stationarity plus separating variations controls the curvature/source
mismatch.  Scale-rank closure licenses the numerical coupling.  Source typing
places source-sensitive residue into `\Theta_B^{fin}` or a charged complement.
Residual separation prevents higher-curvature/anomaly/torsion channels from
being mistaken for Einstein residue.  Projective stability makes the residual
a bounded-history property.  These are exactly the components of
`\mathcal F_B^{Ein}`.  If any fails, the corresponding term of
`\mathcal F_B^{Ein}` is unlicensed or above tolerance. `\square`

## 28. Five-Blocker Adversarial Review

### Review 12: "Stationarity can fail because the selected carrier is a hard
minimum on a discrete class."

Accepted and handled.  Use finite-difference stationarity.  If even finite
move stationarity fails, the carrier is not an Einstein interior phase.

### Review 13: "Scale anchors may be conventional."

Accepted.  Conventional anchors do not license `G_B`.  The anchor-rank matrix
must remove unit gauge using record-realized, projectively stable anchors.

### Review 14: "Source typing may require QFT."

Sometimes.  If a quantum source cannot yet be represented as a finite typed
source/stress packet, it remains typed residue or untyped residue.  That
blocks classical Einstein readiness, but not the click law.

### Review 15: "Higher-curvature gravity could be fundamental."

Allowed.  It is a different typed dynamics phase.  The Einstein phase is the
sector in which those typed residuals are below tolerance or irrelevant at
the selected scale.

### Review 16: "Projective stability can fail near singularities or horizons."

Accepted.  Then the bounded region is not Einstein-ready at that tolerance.
The remedy is boundary expansion, a critical-phase label, or a non-Einstein
dynamics gate.

## 29. Final Paper XLVII Result

Paper XLVII now packages the finite Einstein blockers into one gate:

$$
\boxed{
\text{geometry-irreducible carrier}
+\mathcal B_B^{Ein}\le\epsilon_B
\Longrightarrow
\text{finite Einstein-ready phase}.
}
$$

Expanded:

$$
\boxed{
\begin{gathered}
\text{interior or finite-difference stationarity}\\
+\text{anchor-rank licensed }G_B\\
+\text{typed source/stress packet}\\
+\text{Einstein/non-Einstein residual separation}\\
+\text{projective residual stability}
\\
\Longrightarrow
\mathcal F_B^{Ein}(K_B^\star)\le\epsilon_F.
\end{gathered}
}
$$

The blockers are not philosophical anymore.  Each is now a finite defect with
a pass/fail consequence.

QFT remains downstream:

$$
\boxed{
\text{after Einstein-ready phase, construct finite typed local algebras and
state/amplitude structure.}
}
$$
