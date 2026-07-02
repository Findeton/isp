# Relativistic ISP v7 Paper XLVI: Geometry-Irreducible Carrier Phase

**Status:** analytic campaign note, not peer reviewed, version 2026-06-30.

## 0. Question

Paper XLV changed the problem.

The click law is no longer:

$$
\boxed{
\text{geometry must be the universal minimizer.}
}
$$

The click law is:

$$
\boxed{
\text{bounded histories select minimal admissible carriers.}
}
$$

The new question is:

$$
\boxed{
\text{when does the selected carrier deserve to be called spacetime?}
}
$$

This paper develops the answer:

$$
\boxed{
\text{spacetime is the geometry-irreducible carrier phase.}
}
$$

## 1. Executive Result

The campaign proves a finite soundness/completeness theorem for the
spacetime phase criterion.

Let:

$$
\boxed{
K_B^\star(H;\mathcal Y_B,\epsilon)
}
$$

be Paper XLV's minimal admissible bounded-history carrier selector.  Define a
record-intrinsic defect:

$$
\boxed{
\mathcal E^{GI}_B(K)
}
$$

whose components test:

1. multiscale interval dimension;
2. nonlookup atlas overlap;
3. finite no-silent response tail;
4. presentation-covariant anisotropy;
5. density regularity;
6. Ward/source stability;
7. robustness under no-silent target closure;
8. bounded-history drift stability.

The main finite theorem is:

$$
\boxed{
\mathcal E^{GI}_B(K_B^\star)\le\epsilon_{GI}
\quad\Longleftrightarrow_{\rm finite}
\quad
\text{the selected carrier licenses a stable finite spacetime packet.}
}
$$

The equivalence is finite and tolerance-resolved.  It does not assert smooth
continuum GR.  It says exactly when the selected record carrier has enough
intrinsic structure to support Paper 39's finite spacetime readout:

$$
\boxed{
I_{GR}^{cl},\quad d_{GR}^{cl},\quad \mathcal M_B^{cl},\quad
\Delta^{GR}.
}
$$

## 2. Inputs From Paper XLV

For a bounded problem `B`, target family `\mathcal Y_B`, and tolerance
`\epsilon`, Paper XLV defines:

$$
\boxed{
\operatorname{Adm}_B(\mathcal Y_B,\epsilon)
}
$$

as the finite same-actual quotient of carriers satisfying:

1. history-first action on `H_{B,k}`;
2. record-intrinsic dictionary;
3. no-silent completeness;
4. subraw/nonlookup complexity;
5. projective deletion/refinement compatibility;
6. finite channel floors;
7. deterministic target sufficiency.

The selector is:

$$
\boxed{
K_B^\star
=
\operatorname*{Argmin}_{K\in\operatorname{Adm}_B}
\mathcal A^{sel}_B(H,K;\mathcal Y_B).
}
$$

The effective click weight is:

$$
\boxed{
h_B(H;\mathcal Y_B)
=
\exp[-\mathcal A_B^{click}(H;\mathcal Y_B)].
}
$$

Probability appears only after projection:

$$
\boxed{
\Pr_B(Y=y\mid O=o)
=
\frac{
\sum_{H:\ O(H)=o,\ Y(H)=y}h_B(H;\mathcal Y_B)
}{
\sum_{H:\ O(H)=o}h_B(H;\mathcal Y_B)
}.
}
$$

This paper does not alter that click law.  It adds the spacetime-phase test.

## 3. Geometry-Irreducibility Defect

For an admissible carrier `K`, define:

$$
\boxed{
\mathcal E^{GI}_B(K)
=
w_DD_B(K)
+w_AA_B(K)
+w_TT_B(K)
+w_CC_B(K)
+w_\rho\rho_B(K)
+w_WW_B(K)
+w_NN_B(K)
+w_\Delta\Delta_B(K).
}
$$

All weights are nonnegative.  Each term is record-intrinsic.

The carrier is geometry-irreducible at tolerance `\epsilon_{GI}` when:

$$
\boxed{
\mathcal E^{GI}_B(K)\le\epsilon_{GI}.
}
$$

The selected history is in the spacetime phase when every least-work selected
carrier is geometry-irreducible up to same-actual equivalence:

$$
\boxed{
K_B^\star\subseteq
\{K:\mathcal E^{GI}_B(K)\le\epsilon_{GI}\}/\sim_{\rm same\ actual}.
}
$$

If some selected minimizer is non-geometric and not same-actual equivalent to
a geometry-irreducible carrier, the phase is mixed or non-spacetime.

## 4. Defect 1: Multiscale Interval Dimension `D_B`

For a carrier `K`, let:

$$
\boxed{
N_K(x,r)
}
$$

be the carrier-printed number of records in the intrinsic interval shell of
radius/depth `r` around record `x`.  The scale variable `r` is not a continuum
distance.  It is built from chain depth, interval nesting, or carrier shell
rank.

Define the local dimension slope:

$$
\boxed{
d_K(x;r,s)
=
\frac{\log N_K(x,s)-\log N_K(x,r)}
{\log s-\log r}.
}
$$

For a scale window `\mathcal R_B`, define:

$$
\boxed{
D_B(K)
=
\inf_{d\in\mathbb R_+}
\sup_{x,\ r<s\in\mathcal R_B}
|d_K(x;r,s)-d|.
}
$$

Small `D_B(K)` means interval growth is stably finite-dimensional across the
bounded history window.

### Theorem 1: Dimension Failure Blocks Stable Manifold Readout

If `D_B(K)` is above tolerance on every selected carrier, then no finite
spacetime packet can have stable volume/dimension component on `B`.

**Proof.**

Paper 39's packet includes interval volume and dimension summaries.  If no
single finite dimension controls interval-shell growth on the target scale
window, two histories in the same carrier phase can have incompatible volume
readouts.  The packet distance or manifold defect is therefore above
tolerance. `\square`

## 5. Defect 2: Nonlookup Atlas Overlap `A_B`

Let:

$$
\boxed{
\mathcal A_K=\{D_\alpha\}
}
$$

be the carrier's finite set of diamond neighborhoods.  Define an overlap graph:

$$
\boxed{
\alpha\sim\beta
\quad\Longleftrightarrow\quad
D_\alpha\cap D_\beta
\text{ has nonzero center-visible overlap.}
}
$$

For overlapping diamonds, the carrier prints a transport comparison:

$$
\boxed{
U_{\alpha\beta}.
}
$$

For overlap loops `\gamma=(\alpha_0,\ldots,\alpha_n=\alpha_0)`, define:

$$
\boxed{
F_K(\gamma)
=
U_{\alpha_0\alpha_1}
\cdots
U_{\alpha_{n-1}\alpha_n}
}
$$

where `+` denotes the carrier's finite composition law; if the transport is
group-like, read this as product/composition.

The atlas defect is:

$$
\boxed{
A_B(K)
=
C_{\rm raw}^{-1}C_{\rm atlas}(K)
+\operatorname{disc}(\mathcal A_K)
+\sup_{\gamma\in\Gamma_B}
\operatorname{loopdef}(F_K(\gamma)).
}
$$

Here:

- `C_{\rm atlas}/C_{\rm raw}` prevents raw atlas lookup;
- `\operatorname{disc}` charges disconnected or non-covering overlap graphs;
- `\operatorname{loopdef}` charges unaccounted transport inconsistency.

### Theorem 2: Atlas Failure Blocks Spacetime

If `A_B(K)` is above tolerance, `K` cannot license a finite spacetime packet
on `B`.

**Proof.**

A finite spacetime packet needs local frames and overlap comparisons.  If the
cover is raw, disconnected, or loop-inconsistent beyond the allowed curvature
residue, the carrier cannot distinguish coordinate/gauge change from physical
change.  Paper 39's `I_{GR}^{cl}` and `\mathcal M_B^{cl}` therefore fail.
`\square`

## 6. Defect 3: Finite Response Tail `T_B`

Let:

$$
\boxed{
v_r^K(H,H')
}
$$

be unresolved no-silent response mass at carrier distance/depth `r` between
two compatible histories that agree on the printed panel through radius `r`.

Define:

$$
\boxed{
T_B(K)
=
\inf_{C>0,\ 0<\theta<1}
\sup_{H,H'}\sup_{r\in\mathcal R_B}
\frac{\|v_r^K(H,H')\|}{C\theta^r}.
}
$$

Small `T_B(K)` means unresolved influence decays before the carrier becomes
raw lookup.

### Theorem 3: Tail Failure Blocks Bounded Spacetime

If the selected carrier has no finite response tail, then the bounded region
`B` is not a closed spacetime region at the requested tolerance.

**Proof.**

Without a finite response tail, histories that agree on the printed bounded
panel can differ by above-tolerance unprinted residue from outside the panel.
Then both click prediction and GR readout depend on unprinted history.  The
proper remedy is boundary/history expansion, not spacetime licensing. `\square`

## 7. Defect 4: Presentation-Covariant Anisotropy `C_B`

The earlier phrase "approximate isotropy" is too strong.  GR allows anisotropic
sources, curvature, gravitational waves, and cosmological anisotropy.

The correct finite test is:

$$
\boxed{
\text{no unprinted preferred presentation.}
}
$$

Let `\operatorname{Aut}_0(K)` be same-actual presentation changes of the
carrier dictionary.  Let `R_K` be the printed residue tensor/vector family.
Define:

$$
\boxed{
C_B(K)
=
\sup_{\sigma\in\operatorname{Aut}_0(K)}
d_{\rm res}\left(
R_K,\sigma_\ast R_K
\right)
-
d_{\rm phys}(R_K,\sigma_\ast R_K).
}
$$

Small `C_B` means anisotropy is either same-actual/gauge or printed as physical
source/curvature residue.  Large `C_B` means the carrier depends on arbitrary
generator labels or presentation artifacts.

### Theorem 4: Presentation Anisotropy Blocks Geometry

If `C_B(K)` is above tolerance, then `K` does not define a record-covariant
spacetime readout.

**Proof.**

Two same-actual presentations of the same carrier produce different unprinted
residue readings.  A spacetime packet must be record-covariant under such
presentation changes.  Therefore the packet distance or same-actual quotient
is ill-defined. `\square`

## 8. Defect 5: Density Regularity `\rho_B`

Let:

$$
\boxed{
\mu_K(D)
}
$$

be the carrier-printed record density of a diamond neighborhood `D`, normalized
by its interval/volume proxy.  For overlapping neighborhoods define:

$$
\boxed{
R_{\alpha\beta}
=
\frac{\mu_K(D_\alpha)}{\mu_K(D_\beta)}.
}
$$

The density defect is:

$$
\boxed{
\rho_B(K)
=
\sup_{\alpha\sim\beta}
\left|\log R_{\alpha\beta}\right|
+\operatorname{cluster}_B(K).
}
$$

The term `\operatorname{cluster}_B` charges hidden high-density clusters whose
effect is not printed as source/curvature.

### Theorem 5: Hidden Density Modulation Blocks Metric Stability

If density modulation changes interval counts but is not printed as a
source/curvature residue, then the same order panel admits incompatible
metric-volume readouts.

**Proof.**

Metric volume is inferred from record density and interval scaling.  Hidden
density modulation can mimic curvature or expansion without being a geometric
effect.  Unless it is printed as source/curvature, two histories with the same
geometric panel produce different volume metrics. `\square`

## 9. Defect 6: Ward/Source Stability `W_B`

Let:

$$
\boxed{
\Delta_K^{Ward},\qquad \Delta_K^{Bianchi}
}
$$

be the finite record residues for source conservation and loop/curvature
compatibility.

Define:

$$
\boxed{
W_B(K)
=
\|\Delta_K^{Ward}\|
+\|\Delta_K^{Bianchi}\|
+\operatorname{untypedSource}_B(K).
}
$$

Small `W_B` means the carrier's source/curvature information closes at the
finite packet level.

### Theorem 6: Ward Failure Blocks GR-Like Spacetime

If `W_B(K)` is above tolerance, then `K` may still define a geometric-looking
carrier, but not a GR-like finite spacetime packet.

**Proof.**

Paper 39's packet includes Ward/Bianchi/source residues.  If those fail,
curvature/source information cannot be transported consistently through the
atlas.  This blocks GR-like closure even if interval growth and overlaps look
manifoldlike. `\square`

## 10. Defect 7: No-Silent Robustness `N_B`

Let:

$$
\boxed{
\overline{\mathcal Y}_B
=
\operatorname{NoSilentClosure}(\mathcal Y_B).
}
$$

Define:

$$
\boxed{
N_B(K)
=
d_{\rm phase}
\left(
K_B^\star(\mathcal Y_B),
K_B^\star(\overline{\mathcal Y}_B)
\right).
}
$$

Small `N_B` means the geometric phase is not an artifact of omitting a nearby
target-changing residue.

### Theorem 7: Nonrobust Geometry Is Not Physical Spacetime

If a carrier is geometric only before no-silent closure, then spacetime onset
is not licensed.

**Proof.**

No-silent closure appends all above-tolerance target-changing residues.  A
phase that disappears after those residues are printed was selected by
omission, not by the physical bounded history. `\square`

## 11. Defect 8: Bounded-History Drift `\Delta_B`

The carrier must be stable across the history cylinder:

$$
\boxed{
\Delta_B(K)
=
\sum_{j=N-k}^{N-1}
d_K(K_{j+1},\rho_{j+1\to j}^{\ast}K_j).
}
$$

Small drift means the same carrier phase persists through the bounded
non-Markovian history window.

### Theorem 8: Drift Failure Blocks Stable Phase

If `\Delta_B(K)` is above tolerance, the carrier may describe one slice but
not a stable spacetime phase of the bounded history.

**Proof.**

Spacetime readout is a history-stable effective description.  If deletion or
refinement changes the carrier phase above tolerance, the readout is not
projectively stable and cannot license a bounded spacetime region. `\square`

## 12. Combined Geometry-Irreducibility Theorem

### Theorem 9: Soundness

If a selected carrier `K_B^\star` satisfies:

$$
\boxed{
\mathcal E^{GI}_B(K_B^\star)\le\epsilon_{GI},
}
$$

then it licenses a finite spacetime packet:

$$
\boxed{
I_{GR}^{cl}(K_B^\star)
=
(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r)
}
$$

with:

$$
\boxed{
d_{GR}^{cl}\le C\epsilon_{GI},
\qquad
\mathcal M_B^{cl}\le C\epsilon_{GI},
\qquad
\Delta^{GR}\le C\epsilon_{GI}.
}
$$

**Proof.**

`D_B` supplies finite interval/volume/dimension summaries.  `A_B` supplies a
nonlookup atlas with overlap transport and loop defects.  `T_B` supplies
bounded tail stability.  `C_B` guarantees record covariance under
presentation changes.  `\rho_B` prevents hidden density modulation from
spoofing geometry.  `W_B` supplies finite source/curvature compatibility.
`N_B` prevents omitted-residue artifacts.  `\Delta_B` gives projective
history stability.  These are exactly the components and stability controls
of Paper 39's finite packet, hence the packet defects are bounded by a
constant multiple of their weighted sum. `\square`

### Theorem 10: Finite Completeness

Suppose a selected carrier licenses a stable finite spacetime packet in the
Paper 39 sense:

$$
\boxed{
d_{GR}^{cl}\le\epsilon,\qquad
\mathcal M_B^{cl}\le\epsilon,\qquad
\Delta^{GR}\le\epsilon
}
$$

and the packet is subraw, no-silent closed, and record-covariant.  Then some
selected carrier equivalent to it satisfies:

$$
\boxed{
\mathcal E^{GI}_B(K)\le C'\epsilon.
}
$$

**Proof.**

A stable finite spacetime packet contains interval/dimension summaries, an
atlas/overlap system, loop/source residues, and refinement maps.  Its bounded
packet distance gives tail and drift controls.  Record covariance gives
presentation-covariant anisotropy.  No-silent closure and source typing give
`N_B` and `W_B`.  The packet's nonlookup and volume stability give density
regularity.  Reading these packet controls into the definitions of the eight
defects gives the bound. `\square`

### Corollary 11: Finite Spacetime Phase Criterion

At fixed bounded problem and tolerance:

$$
\boxed{
\text{selected carrier is spacetime-like}
\quad\Longleftrightarrow_{\epsilon}
\quad
\mathcal E^{GI}_B(K_B^\star)\le\epsilon_{GI}.
}
$$

This is the finite criterion needed after Paper XLV.

## 13. Test Campaign On Examples

### 13.1 Cayley Expander Residue Carrier

The Cayley-residue carrier from Paper XLV is admissible for clicks.  It fails
the spacetime phase gate because:

1. interval growth is graph/algebraic rather than stable manifoldlike across
   the selected scales;
2. overlap loops are relator identities, not local curvature defects;
3. presentation-covariant anisotropy fails unless the generator presentation
   is promoted into physical source data;
4. density and atlas overlap have no manifold calibration.

Result:

$$
\boxed{
K_{\rm Cayley}\in\text{algebraic click phase},
\qquad
K_{\rm Cayley}\notin\text{spacetime phase}.
}
$$

### 13.2 Finite Torus/Grid Carrier

For a carrier equivalent to a finite `d`-torus grid with nearest-neighbor
generators:

1. interval growth is polynomial on scales below wraparound;
2. local overlaps are translation-compatible;
3. relator loops are small plaquette defects;
4. presentation anisotropy is same-actual or printed as lattice anisotropy;
5. density is regular on the selected scale window.

Result:

$$
\boxed{
K_{\mathbb Z_n^d}\simeq K_{geo}
\quad
\text{on scales }1\ll r\ll n.
}
$$

This is not a contradiction.  Algebraic syntax can encode geometric content.

### 13.3 Chain Carrier

A chain has interval growth but no nontrivial overlap/loop atlas.  It fails
`A_B` for spacetime dimension greater than one and supports at most a
one-dimensional order-like phase.

### 13.4 Kleitman-Rothschild/Staged Carrier

A staged order can match layer profiles, but it fails local overlap transport
and no-hidden-staging tests.  Its apparent dimension is globally staged rather
than locally propagated.

### 13.5 Sprinkled Causal Diamond

A Poisson-like causal sprinkling carrier is expected to pass the gate at high
density and away from boundaries/singularities:

1. interval growth concentrates around dimension;
2. overlap transport concentrates;
3. density modulation is controlled by the sprinkling law;
4. Ward/source residues are small in vacuum or typed by matter/source sectors.

This is a calibration case, not a derivation of the universe.  It says the
gate agrees with the standard manifoldlike causal-set benchmark.

### 13.6 Density-Modulated Cluster

A clustered carrier can fake interval moments while failing density
regularity.  It is rejected unless the clustering is printed as source or
curvature residue.

### 13.7 Entanglement-Only Hypergraph

A pure hyperedge carrier may carry nonlocal click correlations.  It fails
spacetime unless interval/overlap/atlas residues also close.  Entanglement is
allowed inside records; it is not by itself a metric.

### 13.8 Strong Source Or Horizon-Like Region

The gate does not require flat spacetime.  It requires that sources and long
tails be printed inside the bounded panel.  Near strong source sectors the
tail defect may force boundary expansion:

$$
\boxed{
B\mapsto B'
\quad\text{until}\quad
T_{B'}(K)\le\epsilon_T.
}
$$

## 14. Hostile Review Round I

### Review 1: "The gate just restates spacetime."

Partly sustained, but not fatal.  The gate is not a continuum spacetime
definition.  It is a finite record-intrinsic checklist built from interval
counts, overlap transport, response tails, density, Ward/source residues, and
history drift.  It can be evaluated on non-spacetime carriers and rejects many
of them.

### Review 2: "Approximate isotropy is false in GR."

Accepted.  The gate was corrected to presentation-covariant anisotropy.
Physical anisotropy is allowed if printed as source/curvature.  Unprinted
generator preference is not.

### Review 3: "A clever algebraic carrier could pass the gate."

Accepted.  If it passes all record-intrinsic geometric tests, then it is not a
counterexample.  It is an algebraic representation of a geometric carrier
phase, like a finite torus grid.

### Review 4: "The thresholds are not derived."

Accepted.  Thresholds are calibration data for the bounded problem.  The
theorem is finite and tolerance-resolved.  Continuum or experimental
calibration remains downstream.

### Review 5: "The selected carrier may tie between geometric and
non-geometric phases."

Accepted.  That is a mixed phase, not spacetime-forcing.  Spacetime is forced
only if all selected minimizers are geometry-irreducible up to same-actual
equivalence.

## 15. Opening Follow-Up A: Mixed Phases

Define the selected phase set:

$$
\boxed{
\Phi_B^\star
=
\{\operatorname{phase}(K):K\in K_B^\star\}.
}
$$

Then:

$$
\boxed{
\text{forced spacetime on }B
\quad\Longleftrightarrow\quad
\Phi_B^\star=\{\text{geometric}\}.
}
$$

If:

$$
\boxed{
\text{geometric}\in\Phi_B^\star
\quad\text{and}\quad
|\Phi_B^\star|>1,
}
$$

the bounded problem is spacetime-allowing but not spacetime-forcing.

### Theorem 12: Tie Classification

Ties between geometric and non-geometric selected carriers imply branch
dependence of spacetime readout, not failure of the click law.

**Proof.**

The click law sums over selected histories/carriers through the bounded
history action.  If multiple same-cost carrier phases remain, the panel
prediction exists, but spacetime interpretation depends on which carrier phase
is conditioned on or selected by additional boundary data. `\square`

## 16. Opening Follow-Up B: Geometry-Irreducibility Versus Manifoldlikeness

Geometry-irreducibility is stronger than "some low-dimensional statistics
look manifoldlike" and weaker than "a smooth Lorentzian manifold has been
constructed."

It is stronger because it requires:

1. overlap transport;
2. response tails;
3. density regularity;
4. Ward/source closure;
5. projective history drift.

It is weaker because it produces only:

$$
\boxed{
\text{finite spacetime packet at tolerance}.
}
$$

not a differentiable continuum.

### Theorem 13: No Manifold Assumption

The defect `\mathcal E^{GI}_B` is computable on any selected carrier, including
non-geometric carriers.

**Proof.**

Each term is defined from record counts, carrier overlaps, response tails,
presentation changes, density ledgers, Ward/source residues, no-silent target
closure, and history drift.  None requires a continuum manifold as input.
`\square`

## 17. Opening Follow-Up C: Einstein Dynamics

The geometry-irreducibility gate licenses finite spacetime, not full Einstein
dynamics.

To approach Einstein equations, add a dynamical residual:

$$
\boxed{
E^{Ein}_B(K)
=
\|G^{finite}_B(K)-8\pi G_B T^{finite}_B(K)\|.
}
$$

This requires:

1. a scale anchor for `G_B`;
2. a typed source packet `T^{finite}_B`;
3. a finite Einstein tensor proxy from center/loop residues;
4. projective convergence of the residual.

### Theorem 14: Spacetime Gate Precedes Einstein Gate

Small `\mathcal E^{GI}_B` is necessary for a finite Einstein residual to be
interpretable as GR, but it is not sufficient to prove Einstein dynamics.

**Proof.**

Einstein dynamics compares curvature and source packets.  Without a stable
spacetime carrier, those packets are not defined.  But defining the packets
does not force their residual to vanish. `\square`

## 18. Opening Follow-Up D: QFT Gate

Paper XLII's QFT gate requires:

1. a stable spacetime carrier or explicitly pre-spacetime typed net;
2. finite local algebras;
3. microcausal or record-causal commutation structure;
4. state/update/amplitude rule;
5. source/entanglement sectors.

Geometry-irreducibility provides the spacetime background phase for QFT-like
local nets.  It does not by itself define QFT.

### Theorem 15: QFT Requires A Further Phase Layer

Passing the geometry-irreducibility gate is not enough to construct a QFT
sector.  It only supplies the finite spacetime packet on which a QFT gate can
be tested.

**Proof.**

QFT requires local observable algebras and state/amplitude rules.  The geometry
gate supplies atlas, interval, tail, density, and source stability, but not
the full operator algebra or dynamics of matter sectors. `\square`

## 19. Second Hostile Review

### Review 6: "This makes spacetime dependent on targets."

Yes.  Bounded physics is target- and tolerance-relative.  That is already true
for experiments: a lab region, instrument, and accuracy define what must be
closed.

### Review 7: "A carrier might pass locally but fail globally."

Accepted.  The theorem is bounded.  Global spacetime requires a projective
family of bounded carriers whose defects remain controlled on overlaps and
limits.

### Review 8: "A black-box carrier might pass the gate."

Only if its internal state is finite, record-intrinsic, subraw, projective,
and prints the eight geometry defects.  Then its black-box status has been
converted into a finite carrier dictionary.

### Review 9: "Near singularities the gate may fail."

Accepted.  That means spacetime is not licensed at that bounded tolerance.
This is a feature, not a bug: pre-geometric or critical regimes should not be
forced into a manifold description.

## 20. Final Campaign Result

Paper XLVI closes the immediate post-falsification problem.

The correct chain is:

$$
\boxed{
\text{bounded indivisible histories}
\to
\text{minimal admissible carrier}
\to
\text{click probabilities by projection}.
}
$$

Then:

$$
\boxed{
\text{selected carrier}
+\mathcal E^{GI}_B\le\epsilon_{GI}
\Longleftrightarrow_{\rm finite}
\text{stable finite spacetime packet}.
}
$$

Thus:

$$
\boxed{
\text{click law is broader than spacetime;}
\quad
\text{spacetime is a stable geometric phase of the click law.}
}
$$

The next paper should not ask whether geometry always wins.  That is false.
It should ask:

$$
\boxed{
\text{which cosmological/pre-geometric initial carrier classes flow into the
geometry-irreducible phase under the bounded-history selector?}
}
$$
