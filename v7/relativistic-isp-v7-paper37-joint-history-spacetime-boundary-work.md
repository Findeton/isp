# Relativistic ISP v7 Paper XXXVII: Joint History-Spacetime Boundary Work

**Status:** campaign note, not peer reviewed, version 2026-06-29.

Paper XXXVI reached the sharper target:

$$
\boxed{
\text{the click law and the emergence of spacetime should be related by one
bounded-history principle, but spacetime need not exist at the first records.}
}
$$

This paper investigates that target directly.

Receipts:

```text
isp/v7/code/p37_joint_history_spacetime_boundary_work.py
isp/v7/code/p37_spacetime_onset_campaign.py
```

The receipts passed:

```text
CHECKS PASSED: 9/9
CHECKS PASSED: 11/11
```

All finite probabilities in the receipts are exact `Fraction` calculations. The
receipts are not physical derivations. They are finite algebra audits of the
claim that a joint boundary-work functional can select the coarsest panel
sufficient for both future-click prediction and finite spacetime readout while
rejecting click-only, geometry-only, and full-reconstructive panels.

## 1. Executive Result

The next target is confirmed, but scoped.

The correct theorem is not:

$$
\boxed{
\text{derive a click law first, then add spacetime later.}
}
$$

The correct theorem is:

$$
\boxed{
\text{derive a record-intrinsic bounded-history panel whose projected
likelihood also carries a stable finite GR readout.}
}
$$

In symbols, for a bounded record diamond `B`, the target is:

$$
\boxed{
(k_B^*,O_B^*)
=
\arg\min_{k,O\ \mathrm{admissible}}
\mathcal A^{total}_B(k,O),
}
$$

with:

$$
\boxed{
\mathcal A^{total}_B(k,O)
=
\mathcal A^{click}_B(k,O)
+
\mu\,\mathcal A^{GR}_B(k,O)
+
\nu\,\mathcal M_B(k)
+
\eta\,C_B(k,O).
}
$$

The terms mean:

- `\mathcal A^{click}` is the forward-click residual;
- `\mathcal A^{GR}` is the finite spacetime-packet residual;
- `\mathcal M_B` is the manifoldlikeness and Ward/Bianchi stability residue;
- `C_B` is the reconstruction/lookup penalty;
- `k` is the history depth;
- `O` is the partial record panel actually used.

The paper's main conclusion is:

$$
\boxed{
\text{the finite projection theorem is easy;}
\quad
\text{the intrinsic diamond construction and the spacetime-onset threshold are
the hard parts.}
}
$$

That is progress. It says exactly where the missing theorem lives.

Important scope correction:

$$
\boxed{
\text{the click law is primary;}
\quad
\text{spacetime is a stable phase/readout of the click-history law.}
}
$$

Thus the total click-plus-GR functional is not required to be small at the
earliest record counts.  Before spacetime onset, the record law may have stable
click predictions while `I_GR` is undefined, unstable, or non-manifoldlike.

## 2. Imports

The campaign imports five previous results.

### 2.1 Diamond Center and Positive Shadow

Papers XXXII-XXXIV reduced the click-law skeleton to:

$$
\boxed{
\text{click law}
=
\text{positive h-transform shadow of a minimal no-silent diamond center}.
}
$$

The center is:

$$
\mathcal C_N.
$$

It is the minimal licensed boundary/collar structure required to remove
no-silent seam residue.

The selected positive shadow is:

$$
\mathcal P_N\preceq \mathcal C_N.
$$

It is the coarser record-intrinsic quotient allowed to enter the forward law.

### 2.2 Scalar-Work Quotient

Paper XXXV found a proper coarser quotient:

$$
\boxed{
\mathcal W_N
=
\left(
M,
|A|,
\operatorname{DelScal}(A),
\operatorname{InsScal}(A)
\right),
}
$$

where:

- `A` is an atom of the selected positive shadow;
- `M` is the selected odd quadratic metric channel;
- `|A|` is atom size;
- `\operatorname{DelScal}` is the scalar deletion-work profile;
- `\operatorname{InsScal}` is the scalar insertion-work profile.

At `N=6,7`, this quotient carries the exact h-transform weights.

### 2.3 History Cylinder

Paper XXXVI proved that one-step prediction is insufficient:

$$
\Pr(S_{N+1}\mid W_N)
\ne
\Pr(S_{N+1}\mid W_{N-1},W_N).
$$

The finite audited law is history-cylinder based:

$$
\boxed{
\Pr(S_B=s\mid O)
=
\sum_H
\Pr(S_B=s\mid H)\Pr(H\mid O).
}
$$

Here:

- `H` is a bounded compatible record history;
- `O` is the observed panel;
- the probability comes from projecting full compatible histories onto a
  partial panel.

### 2.4 Einstein Reconstruction

The v4 GR papers supply a finite GR packet:

$$
\boxed{
I_{GR}(H)
=
(R/{\sim},g,e,U,F,\nabla F,\Theta,D_{\rm src},r).
}
$$

The entries are:

- `R/~`: same-actual quotient;
- `g`: finite metric readout;
- `e`: local frame/clock/ruler readout;
- `U`: finite frame transport;
- `F`: closed-loop curvature/holonomy;
- `\nabla F`: finite curvature-difference data;
- `\Theta`: source/stress readout;
- `D_src`: typed source dictionary;
- `r`: refinement map.

Einstein form appears only after the finite packet passes same-actual,
Ward/Bianchi, low-energy, and cofinal gates.

### 2.5 Order Plus Number Gate

The v6/v7 causal-set line says:

$$
\boxed{
\text{order}+\text{number}
=
\text{geometry up to scale, given manifoldlikeness}.
}
$$

Thus a spacetime readout cannot be a bare metric label. It must be a
record-intrinsic stability statement about order, count, intervals, deletion
drift, and Ward/Bianchi residues.

## 3. Finite Projection Theorem

First isolate the part that is actually easy.

Let `\Omega_B` be the finite set of full compatible histories for a bounded
diamond `B`.

Let:

$$
S:\Omega_B\to\mathcal S
$$

be the next-click map, and let:

$$
\mathcal G:\Omega_B\to\mathfrak G
$$

be the finite GR-packet map.

An observation panel `O` is a finite partition or sigma-field on `\Omega_B`.

Define:

$$
\mathcal A^{click}(O)
=
\mathbb E\,
TV\!\left(
\delta_{S(H)},
\operatorname{Law}(S\mid O(H))
\right),
$$

and:

$$
\mathcal A^{GR}(O)
=
\mathbb E\,
d_{GR}\!\left(
\mathcal G(H),
\operatorname{Law}(\mathcal G\mid O(H))
\right).
$$

In the purely finite exact case, if `d_GR` is the total-variation distance on
GR-packet labels, then:

$$
\mathcal A^{click}(O)=0
\quad\Longleftrightarrow\quad
S\text{ is }O\text{-measurable},
$$

and:

$$
\mathcal A^{GR}(O)=0
\quad\Longleftrightarrow\quad
\mathcal G\text{ is }O\text{-measurable}.
$$

Therefore:

$$
\boxed{
\mathcal A^{click}(O)+\mu\mathcal A^{GR}(O)=0
\quad\Longleftrightarrow\quad
(S,\mathcal G)\text{ is }O\text{-measurable}.
}
$$

If `C(O)` is monotone under refinement and positive on strictly finer panels,
then the lexicographic or small-`\eta` minimizer of:

$$
\mathcal A^{click}(O)+\mu\mathcal A^{GR}(O)+\eta C(O)
$$

is the coarsest panel sufficient for both click and GR prediction.

This is the finite algebraic core of the unification.

### 3.1 Exact Receipt

The receipt tests the theorem pattern with sixteen full histories carrying
four hidden bits:

$$
H=(a,b,c,d).
$$

The future click is:

$$
S=a\oplus b.
$$

The GR packet is:

$$
G=(a,c).
$$

The bit `d` is pure reconstruction noise. It appears in the full history but is
not needed for either click or spacetime readout.

The exact output is:

```text
best click-only panel:     ('a', 'b')
best geometry-only panel:  ('a', 'c')
best joint panel:          ('a', 'b', 'c')
full reconstructive panel: ('a', 'b', 'c', 'd')
```

Exact residuals:

```text
click    fields=('a', 'b')          click=0     geom=1/2   total=201/400
geometry fields=('a', 'c')          click=1/2   geom=0     total=201/400
joint    fields=('a', 'b', 'c')     click=0     geom=0     total=1/200
full     fields=('a', 'b', 'c','d') click=0     geom=0     total=1/100
```

The joint panel wins because it keeps exactly the history information needed
for both targets and drops the irrelevant reconstructive bit.

This demonstrates the formal principle:

$$
\boxed{
\text{joint least boundary work selects common sufficiency, not full
reconstruction.}
}
$$

Again: this is not a physical proof. It is a finite algebra guardrail.

## 4. Intrinsic Diamond Construction of `I_GR`

The real theorem must define:

$$
I_{GR}(H_{B,k})
$$

from record diamonds alone.

The proposed construction is a functor:

$$
\boxed{
\mathfrak D_B^{hist}
\longrightarrow
\mathfrak G_B^{fin},
}
$$

from bounded record-history diamonds to finite GR packets.

Here:

- `\mathfrak D_B^{hist}` is the category of bounded histories of sealed record
  diamonds, with deletion, insertion, refinement, and same-actual maps;
- `\mathfrak G_B^{fin}` is the category of finite GR packets with metric,
  frame, transport, curvature, source, and refinement data.

The functor should be built in five intrinsic stages.

### 4.1 Stage 1: Boundary/Center Extraction

For every candidate history diamond:

$$
D\subset H_{B,k},
$$

extract:

$$
(\partial^-D,\partial^+D,\operatorname{Collar}(D),\mathcal C(D)).
$$

These are:

- lower boundary;
- upper boundary;
- collar neighborhood;
- minimal no-silent center.

The center is not a label. It is generated by residual boundary transport:

$$
T_D(i,j)
=
I(Y_i;Y_j\mid Y_{\partial D\setminus\{i,j\}}),
$$

or its non-probabilistic RN/KL record equivalent when the eventless seam is
audited.

### 4.2 Stage 2: Interval and Volume Readout

For related records `x<y`, define the interval object:

$$
I(x,y)=\{z:x<z<y\}.
$$

The metric-facing packet is not a coordinate distance. It is the collection:

$$
\mathsf q(x,y)
=
\left(
|I(x,y)|,
h(x,y),
\ell(x,y),
\operatorname{Layer}_{x,y},
\operatorname{Center}_{x,y}
\right).
$$

Here:

- `|I(x,y)|` is interval volume in record-count units;
- `h(x,y)` is longest-chain height;
- `\ell(x,y)` is the link/cover profile near the interval boundary;
- `\operatorname{Layer}` is the internal layer histogram;
- `\operatorname{Center}` is the no-silent residual center of the interval
  diamond.

This is the record-intrinsic replacement for a metric interval.

### 4.3 Stage 3: Frame and Transport Readout

A finite frame is a local family of overlapping diamonds:

$$
\mathfrak F_D=\{D_0,D_1,\ldots,D_m\}
$$

whose interval packets and centers have minimal boundary-work disagreement.

Transport between overlapping frames is:

$$
U_{D\to D'}
=
\operatorname*{argmin}_{U}
\operatorname{BW}\!\left(
U\mathcal C(D),
\mathcal C(D')
\right).
$$

The transport is not a continuum connection. It is a minimum-boundary-work
identification between overlapping record centers.

### 4.4 Stage 4: Curvature and Ward Residue

Curvature is the defect around a finite loop of overlapping diamonds:

$$
F(D_0D_1\cdots D_m)
=
U_{D_m\to D_0}
\cdots
U_{D_1\to D_2}
U_{D_0\to D_1}
-\operatorname{id}.
$$

The exact multiplication/addition form depends on whether the transport is
encoded as matrices, permutations, or RN kernels. The invariant is the same:

$$
\boxed{
\text{curvature is closed-loop transport defect.}
}
$$

Ward/Bianchi residue is the defect of defects over a closed two-surface of
diamond loops:

$$
\mathsf W(D)
=
\partial F(D).
$$

If `\mathsf W(D)` is nonzero, it must either be:

- a typed source/stress residue;
- a boundary term;
- a higher-curvature/torsion residue;
- or a failure of the candidate spacetime readout.

It cannot be hidden.

### 4.5 Stage 5: Source Dictionary

The source packet is the typed part of the Ward/Bianchi failure:

$$
\Theta_D
=
D_{\rm src}\bigl(\mathsf W(D)\bigr).
$$

This is the finite analogue of stress-energy. It is not postulated matter in a
background spacetime. It is the typed residue left by trying to close finite
record transport.

Thus:

$$
\boxed{
I_{GR}(H_{B,k})
=
(R/{\sim},g,e,U,F,\nabla F,\Theta,D_{\rm src},r)
}
$$

becomes a record-diamond construction.

## 5. Intrinsic `d_GR`

The distance `d_GR` must not compare coordinates. It compares finite readout
packets.

Define:

$$
d_{GR}(\mathcal G,\mathcal G')
=
w_q d_q
+
w_U d_U
+
w_F d_F
+
w_W d_W
+
w_\Theta d_\Theta
+
w_r d_r.
$$

The terms are:

- `d_q`: distance between interval/count/height/layer/center histograms;
- `d_U`: mismatch of overlapping boundary-work transports;
- `d_F`: closed-loop curvature-defect mismatch;
- `d_W`: Ward/Bianchi residue mismatch;
- `d_\Theta`: typed source-dictionary mismatch;
- `d_r`: refinement/cofinal drift.

Each term is record-intrinsic if computed from:

$$
\text{order},\quad
\text{counts},\quad
\text{diamond centers},\quad
\text{deletion/insertion maps},\quad
\text{boundary-work transport}.
$$

The simplest exact finite version is total variation over packet labels. The
physical version should be a weighted RN/KL or earthmover distance over the
same finite packet components.

## 6. Intrinsic `\Delta^{GR}` and `\mathcal M_B`

The history-drift quantity is:

$$
\Delta^{GR}_{B,j}
=
\mathbb E\,
d_{GR}\!\left(
I_{GR}(H_{B,j+1}),
I_{GR}(H_{B,j})
\right).
$$

This is exactly parallel to the click-history drift in Paper XXXVI.

The manifoldlikeness score should be:

$$
\mathcal M_B(k)
=
M_{\rm dim}
+
M_{\rm height}
+
M_{\rm interval}
+
M_{\rm shell}
+
M_{\rm deletion}
+
M_{\rm Ward}.
$$

The terms are:

- `M_dim`: disagreement between order-only dimension estimators;
- `M_height`: longest-chain/height failure against the dimension estimate;
- `M_interval`: failure of interval interiors to look recursively like smaller
  diamonds of the same class;
- `M_shell`: shell-density and local-response failure;
- `M_deletion`: uncontrolled deletion/insertion drift;
- `M_Ward`: finite Ward/Bianchi failure not typed as source.

This is intentionally not a single scalar imported from continuum geometry.
It is a record-intrinsic adversary suite against:

- Kleitman-Rothschild staged orders;
- density-modulated sprinklings;
- hidden clusters/fibers;
- coherent-wave marks that launder geometry;
- stable-click but unstable-spacetime panels.

## 7. The Joint Theorem Target

The theorem should read:

### Theorem Target: Joint Bounded-History Sufficiency

For the spacetime-admissible phase of the physical class of bounded record
diamonds, suppose:

1. `I_GR(H_{B,k})` is generated by the intrinsic diamond-center/transport
   construction above.
2. `d_GR` is a record-intrinsic packet distance.
3. `\mathcal M_B(k)` is the intrinsic manifoldlikeness/Ward suite.
4. `O` ranges only over admissible non-reconstructive panels generated by
   bounded diamond operators.
5. Residues obey no-silent promotion: unresolved boundary residue either
   washes out or becomes a licensed record sector.

Then:

$$
\boxed{
\inf_{k,O}\mathcal A^{total}_B(k,O)
\text{ is small}
}
$$

if and only if the bounded history admits a panel that is simultaneously:

- forward-click sufficient;
- finite-GR-readout sufficient;
- manifoldlike/stable under deletion and insertion;
- non-reconstructive.

Equivalently:

$$
\boxed{
\text{the same bounded history that predicts records is the bounded history
that licenses spacetime.}
}
$$

This theorem would turn the click-law problem and the spacetime-emergence
problem into one problem after spacetime onset. Section 8 separates this from
the earlier pre-spacetime record phase, where click prediction is meaningful
but `I_GR` need not yet be stable or defined.

## 8. Pre-Spacetime Scope Correction

The Big Bang objection is correct: the first records should not be expected to
already carry a spacetime.

The record law should therefore have two layers.

### 8.1 The Pre-Spacetime Click Layer

The click layer applies whenever there are records:

$$
\boxed{
\mathcal A^{pre}_B(k,O)
=
\mathcal A^{click}_B(k,O)
+
\eta C_B(k,O).
}
$$

The selected pre-geometric panel is:

$$
\boxed{
(k_B^{pre},O_B^{pre})
=
\arg\min_{k,O\ \mathrm{admissible}}
\mathcal A^{pre}_B(k,O).
}
$$

This is the bounded-history click law before spacetime is licensed.  It does
not require:

$$
I_{GR}(H_{B,k})
$$

to exist as a stable object.

In plain language:

> records can click before spacetime exists.

### 8.2 The Spacetime-Onset Defect

Define the GR-readout defect:

$$
\boxed{
\mathcal E^{GR}_B(k,O)
=
\mathcal A^{GR}_B(k,O)
+
\mathcal M_B(k)
+
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}.
}
$$

The terms mean:

- `\mathcal A^{GR}_B(k,O)` is uncertainty in the finite spacetime packet after
  seeing panel `O`;
- `\mathcal M_B(k)` is manifoldlikeness, interval-heredity, and Ward/Bianchi
  failure;
- `\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}` is the older-history tail affecting
  the spacetime packet.

Spacetime is licensed only when:

$$
\boxed{
\mathcal E^{GR}_B(k,O)\le \epsilon_{GR}.
}
$$

Thus the joint functional is not a demand placed on all histories.  It is a
phase/onset condition for histories that already support a stable metric
readout.

### 8.3 Spacetime Onset Number

For a growing record history, define:

$$
\boxed{
N_{GR}(\epsilon)
=
\min\left\{
N:
\exists(k,O)
\text{ with }
\mathcal A^{pre}_B(k,O)\le\epsilon_{click}
\text{ and }
\mathcal E^{GR}_B(k,O)\le\epsilon
\right\}.
}
$$

Here:

- `N` is the number of committed records in the bounded history;
- `N_GR(epsilon)` is the first size at which a spacetime description is
  licensed at tolerance `epsilon`;
- `epsilon_click` is the tolerated click-prediction residual;
- `epsilon` is the tolerated GR-readout defect.

Before `N_GR`, there may be a real record process but no stable spacetime.
After `N_GR`, the same history law admits a manifoldlike GR packet.

This reframes the early-universe picture:

$$
\boxed{
\text{Big Bang}
\ne
\text{first spacetime slice;}
\qquad
\text{Big Bang}
=
\text{pre-geometric record boundary/onset regime.}
}
$$

### 8.4 Corrected Unified Law

The corrected law has a fork:

1. **Pre-spacetime phase.**

   $$
   (k,O)=\arg\min\mathcal A^{pre}_B(k,O).
   $$

   Only click prediction and non-reconstructive sufficiency are required.

2. **Spacetime phase.**

   If some admissible `(k,O)` also satisfies:

   $$
   \mathcal E^{GR}_B(k,O)\le\epsilon_{GR},
   $$

   then select among such panels by the total action:

   $$
   \mathcal A^{total}_B
   =
   \mathcal A^{click}_B
   +
   \mu\mathcal A^{GR}_B
   +
   \nu\mathcal M_B
   +
   \eta C_B.
   $$

So the correct slogan is:

$$
\boxed{
\text{the click law always applies;}
\quad
\text{spacetime appears when the click-history law reaches a stable
manifoldlike readout phase.}
}
$$

## 9. Six Campaign Attacks

### Attack 1: "Can scalar work alone be `I_GR`?"

No.

The scalar-work quotient:

$$
\mathcal W_N
=
(M,|A|,\operatorname{DelScal},\operatorname{InsScal})
$$

is a strong carrier of h-weight in the audited window, but it is too small to
be the whole GR packet. It does not by itself carry:

- loop transport;
- curvature defect;
- Ward/Bianchi residue;
- typed source dictionary;
- interval-recursive manifoldlikeness.

So `\mathcal W_N` should be read as the click-facing control panel of the
diamond center, not the full spacetime readout.

The repair is:

$$
\boxed{
\mathcal W_N
\subset
I_{GR}(H)
\subset
\mathcal C_N
}
$$

as quotients of the same no-silent diamond center.

### Attack 2: "Does `d_GR` smuggle in a continuum metric?"

It would, if defined by coordinates.

The admissible `d_GR` must compare only record-intrinsic packet components:

$$
|I(x,y)|,\quad
h(x,y),\quad
\text{layer profiles},\quad
\text{centers},\quad
\text{transport defects},\quad
\text{Ward residues}.
$$

The metric appears only after these stabilize and pass the GR gates. Thus the
metric is a late readout, not an input.

### Attack 3: "Can click-stable histories be non-manifoldlike?"

Yes. This is the main adversary.

A panel may predict `S_{N+1}` while still allowing:

- staged KR order;
- fiber clustering;
- density modulation;
- shell-local laundering;
- hidden long-range blocks.

Therefore `\mathcal A^{click}` alone cannot define spacetime.

This is exactly why `\mathcal M_B` must be in the same total action once a
spacetime readout is being licensed.

### Attack 4: "Can spacetime-stable panels fail to predict clicks?"

Yes.

A coarse order/count packet may stabilize conformal geometry while missing
matterlike, marklike, or center-shadow data needed for the next record. Thus
`\mathcal A^{GR}` alone cannot define the click law.

This is why the total action must include both.

### Attack 5: "Does the minimizer choose full hidden history?"

Not if `C_B(k,O)` is real.

The full history is always sufficient in a finite brute-force sense. But it is
reconstructive. The physical panel must be the coarsest non-silent sufficient
quotient, not the whole hidden cylinder.

The receipt demonstrates the pattern exactly: `(a,b,c,d)` is sufficient, but
`(a,b,c)` wins because `d` is reconstructive noise.

### Attack 6: "Does this fix `G`?"

No.

The theorem can define relative/conformal spacetime, manifoldlike stability,
and Einstein form. It cannot fix the absolute length/area scale. The v6 scale
no-go remains:

$$
\boxed{
\text{records carry weight-zero invariants; }G\text{ is an external absolute
scale calibration.}
}
$$

This is not a failure of the joint theorem. It is a boundary condition on what
the theorem is allowed to claim.

## 10. Candidate Unified Law

The best current formulation must now be phase-scoped.

The pre-spacetime click law is:

> The click law is the projective h-transform of the coarsest admissible
> no-silent diamond-history quotient whose projected likelihood is stable under
> bounded history extension and whose reconstruction cost is controlled.

The spacetime-phase law is:

> The click law is the projective h-transform of the coarsest admissible
> no-silent diamond-history quotient whose projected likelihood and finite GR
> readout are both stable under bounded history extension, deletion/insertion
> drift, and manifoldlikeness/Ward tests.

In formulas:

Pre-spacetime:

$$
\mathcal Q_B^{pre}
=
\operatorname*{argmin}_{\mathcal Q\preceq\mathcal C_B^{hist}}
\left[
\mathcal A^{click}(\mathcal Q)
+
\eta C(\mathcal Q)
\right].
$$

Spacetime phase:

$$
\mathcal Q_B^*
=
\operatorname*{argmin}_{\mathcal Q\preceq\mathcal C_B^{hist}}
\left[
\mathcal A^{click}(\mathcal Q)
+
\mu\mathcal A^{GR}(\mathcal Q)
+
\nu\mathcal M(\mathcal Q)
+
\eta C(\mathcal Q)
\right],
$$

provided:

$$
\mathcal E^{GR}_B(\mathcal Q)\le\epsilon_{GR}.
$$

Then:

$$
\Pr(P\mid C)
=
\frac{D(P,C)h_{\mathcal Q_B^*}(P)}
{\sum_{P'}D(P',C)h_{\mathcal Q_B^*}(P')}.
$$

Here:

- `\mathcal C_B^{hist}` is the bounded history diamond center;
- `\mathcal Q_B^{pre}` is the selected pre-spacetime click quotient;
- `\mathcal Q_B^*` is the selected joint quotient;
- `h_{\mathcal Q_B^*}` is the positive h-weight derived from the
  boundary-work potential on that quotient;
- `D(P,C)` is deletion multiplicity from possible parent `P` to current
  committed record `C`.

The law is not "probability is primitive." It is:

$$
\boxed{
\text{full compatible histories carry the deterministic record structure;}
\quad
\text{probability is the projected residual on the selected quotient.}
}
$$

## 11. Hostile Reviews

### Review 1: "This still does not derive `\psi`."

Sustained.

The paper says where the boundary-work potential must live:

$$
\psi_{\mathcal Q_B^*}.
$$

It does not derive the physical RN/KL potential from the diamond center.

### Review 2: "`I_GR` is only a proposal."

Sustained.

The paper gives a record-intrinsic construction scheme for `I_GR`; it does not
prove that this construction has the correct continuum limit. The old GR
papers supply conditional gates, not a free pass.

### Review 3: "The finite receipt is toy algebra."

Sustained.

The receipt proves only the finite projection logic:

$$
\text{joint residual}+\text{complexity}
\Rightarrow
\text{coarsest common sufficient panel}.
$$

It does not identify the physical panel.

### Review 4: "Manifoldlikeness is still open."

Sustained.

The proposed `\mathcal M_B` is an adversary suite, not a theorem that the law
selects manifoldlike orders. The causal-set dominance problem remains.

### Review 5: "This may over-couple clicks and geometry."

Partly sustained.

Some click sectors may be matterlike excitations on an already stable
spacetime. Some geometry sectors may be stable while matter clicks remain
uncertain. The theorem should not force equality of the click and GR panels.
It should force a common bounded history quotient that contains both as
projections:

$$
\mathcal W_B^{click}
\preceq
\mathcal Q_B^*,
\qquad
\mathcal W_B^{GR}
\preceq
\mathcal Q_B^*.
$$

So the unified object is not a single scalar. It is a joint quotient with
click-facing and geometry-facing projections.

### Review 6: "The theorem could choose huge panels forever."

Sustained unless `C_B` is intrinsic and strong.

The reconstruction penalty must be derived from no-hidden-presentation/no-
lookup discipline, not added by taste. Otherwise the full history always wins.

### Review 7: "The theorem assumes spacetime at the Big Bang."

Sustained in the earlier wording; repaired here.

The corrected statement is not that every record history has a spacetime. The
corrected statement is that every record history has a click-law problem, while
only some sufficiently stable histories have a GR-readout problem.

The onset quantity is:

$$
N_{GR}(\epsilon).
$$

If `N<N_GR`, the total click-plus-GR action is not the right law. The
pre-spacetime action `\mathcal A^{pre}` is.

## 12. Bottom Line

This campaign does not close the click law.

It closes two conceptual forks.

First, the next theorem is not merely:

$$
\text{derive } \Pr(S_{N+1}\mid H).
$$

It is:

$$
\boxed{
\text{derive the coarsest admissible bounded history quotient that is jointly
sufficient for click prediction and finite spacetime readout.}
}
$$

Second, that joint theorem is not a demand on the first records.  The more
primitive theorem is:

$$
\boxed{
\text{derive the coarsest admissible bounded history quotient sufficient for
click prediction before spacetime is licensed.}
}
$$

Spacetime onset is the extra condition:

$$
\boxed{
\mathcal E^{GR}_B(k,O)\le\epsilon_{GR}.
}
$$

The finite projection theorem shows that, once the intrinsic objects exist, the
joint minimization principle is mathematically natural. The hard unresolved
work is exactly:

$$
\boxed{
\text{derive }I_{GR},\ d_{GR},\ \Delta^{GR},\ \mathcal M_B,\ C_B,
\text{ and }\psi
\text{ from the no-silent diamond center.}
}
$$

If that succeeds, the slogan becomes literal:

$$
\boxed{
\text{the rule that tells records how to click also tells when spacetime is
allowed to appear.}
}
$$

## 13. Next Exact Targets

The next campaign should not start with continuum GR. It should start with
record diamonds.

1. Define the pre-spacetime click action:

   $$
   \mathcal A^{pre}=\mathcal A^{click}+\eta C.
   $$

2. Define `I_GR` on the audited `N=6,7,8` shadow/center data using interval
   profiles, center drift, and deletion/insertion transport.
3. Test whether the scalar-work quotient embeds into a larger GR-facing
   quotient without forcing full reconstruction.
4. Build exact finite `d_GR` from packet labels and measure
   `\Delta^{GR}` on the Paper XXXVI deletion cylinders.
5. Add a first intrinsic `\mathcal M_B` adversary suite: dimension agreement,
   height, interval heredity, shell density, and Ward residue.
6. Measure the onset defect:

   $$
   \mathcal E^{GR}
   =
   \mathcal A^{GR}
   +
   \mathcal M
   +
   \sum_j\Delta^{GR}_j.
   $$

7. Estimate the first finite onset:

   $$
   N_{GR}(\epsilon).
   $$

8. Run the joint minimization only where `\mathcal E^{GR}` is small:

   $$
   \mathcal A^{total}
   =
   \mathcal A^{click}
   +
   \mu\mathcal A^{GR}
   +
   \nu\mathcal M
   +
   \eta C.
   $$

9. Attack it with four adversaries:
   pre-spacetime click-stable/no-GR,
   click-stable/non-manifold,
   geometry-stable/click-unstable,
   and full-history reconstructive spoof.

Passing those tests would not prove the universal law, but it would make the
joint click-spacetime theorem a finite object rather than a slogan.

## 14. Long Campaign: First Spacetime-Onset Finite Audit

Receipt:

```text
isp/v7/code/p37_spacetime_onset_campaign.py
```

The receipt passed:

```text
CHECKS PASSED: 11/11
```

All weights and residuals in this receipt are exact rational calculations.  The
receipt uses the audited permutation-order deletion cylinders and compares four
panels:

- `W`: scalar-work history;
- `G`: the first intrinsic GR-facing packet;
- `WG`: the joint scalar-work plus GR-facing packet;
- `R`: raw deletion-history reconstruction.

The first GR-facing packet is built only from record-intrinsic data:

$$
G_N
=
\left(
\#\mathrm{relations},
h,
w,
\mathrm{interval\ profile},
\mathrm{degree\ moments},
\mathrm{matching\ profile},
\mathrm{layer\ profile}
\right).
$$

Here:

- `N` is the number of records in the finite order;
- `h` is height, the longest-chain length;
- `w` is width, the largest antichain size;
- the interval profile counts sizes of internal diamonds;
- the degree moments summarize local comparability degrees;
- the matching profile counts disjoint comparable-pair matchings;
- the layer profile counts records by longest-chain rank.

This is not claimed to be the physical `I_GR`. It is the first hostile test of
whether scalar click-work already carries a spacetime-facing packet.

### 14.1 Exact `N=8` Result

The exact `N=8` campaign used four deletion-history depths for `W`, `G`, `WG`,
and `R`.  All path weights matched:

```text
total path weight W  = 67737600
total path weight G  = 67737600
total path weight WG = 67737600
total path weight R  = 67737600
expected path weight = 67737600
```

The key exact residuals were:

```text
W4_geom  = 0.966274417753212396069539...
WG4_geom = 0.937821180555555555555556...
R1_geom  = 0.937748015873015873015873...
```

So scalar-work history is not enough for the first GR-facing packet:

$$
\mathcal A^{GR}(W_4)
>
\mathcal A^{GR}(WG_4).
$$

But raw current order still wins the joint score at `N=8`:

```text
click+geom winner: R1
```

This is the important hostile result. The first `G` packet improves the
spacetime-facing residual, but it is too close to raw reconstruction.  The
final law cannot simply say "add all order/count/layer data."  It needs a
coarser, diamond-derived GR quotient.

### 14.2 Exact `N=9` Current-Panel Result

The full four-step `N=9` campaign is too large for this brute-force route, so
the receipt follows the theorem-critical opening and computes the exact
one-step current-panel comparison for `W1` and `G1`.

All path weights matched:

```text
total path weight W  = 3265920
total path weight G  = 3265920
expected path weight = 3265920
```

The exact residuals were:

```text
W1_click = 0.965103554281795023...
W1_geom  = 0.980341527042915932...
W1_total = 1.948778414658044288...

G1_click = 0.951217727317264354...
G1_geom  = 0.952362274642367235...
G1_total = 1.913580001959631589...
```

Thus, at `N=9`, the first GR-facing packet beats scalar work even for the click
residual:

$$
\mathcal A^{click}(G_1)
<
\mathcal A^{click}(W_1),
$$

and also for the GR residual:

$$
\mathcal A^{GR}(G_1)
<
\mathcal A^{GR}(W_1).
$$

But the packet census is a warning:

```text
N=9 records      = 131526
N=9 shadow cells = 65521
N=9 geom cells   = 125774
```

The `G` packet has nearly raw cardinality. It is useful, but not yet the
lawful non-reconstructive spacetime quotient.

### 14.3 Campaign Verdict

The campaign establishes the following finite facts.

1. Scalar click-work is not enough to carry even the first GR-facing packet.
2. Adding GR-facing intrinsic order data lowers residuals at `N=8` and `N=9`.
3. The naive first `G` packet is too fine and drifts toward raw reconstruction.
4. Therefore the next theorem is not "use `G`." It is:

   $$
   \boxed{
   \text{derive a coarser diamond-center quotient }
   G_N^{coarse}
   \text{ with }
   W_N\preceq G_N^{coarse}\prec R_N.
   }
   $$

The quotient must lower the GR readout defect while staying under an intrinsic
no-hidden-presentation complexity bound.

### 14.4 Block-History Clarification

The whole-history idea is close to the block-universe idea, but not identical.

The ordinary block universe starts with a four-dimensional spacetime already in
place.  This paper does not.  The primitive object is a compatible
record-history block:

$$
H_{B,k}.
$$

Here:

- `B` is the bounded record diamond being predicted from;
- `k` is the amount of bounded past/history included;
- `H_{B,k}` is the compatible finite record-history cylinder.

The full history may determine the next click, but it need not already be a
spacetime. Spacetime is a readout licensed only if:

$$
\mathcal E^{GR}_B(k,O)\le\epsilon_{GR}.
$$

So the correct phrase is:

$$
\boxed{
\text{pre-geometric block record history, not pre-given spacetime block.}
}
$$

Probability appears when the full history is projected onto the bounded panel
actually computed:

$$
\Pr(S_B=s\mid O)
=
\sum_H
\Pr(S_B=s\mid H)\Pr(H\mid O).
$$

If the full compatible history were known, the click would be deterministic
inside this finite model.  Because only `O` is known, the residual over
compatible histories is represented probabilistically.

### 14.5 Updated Long Target

The next long campaign should not brute-force larger and larger `N`.  It should
derive the missing coarser quotient.

The target is:

$$
\boxed{
\text{derive }G_N^{coarse}\text{ intrinsically from diamonds and centers,}
}
$$

such that:

$$
W_N
\preceq
G_N^{coarse}
\prec
R_N,
$$

and:

$$
\mathcal A^{GR}(G_N^{coarse})
\ll
\mathcal A^{GR}(W_N),
\qquad
C(G_N^{coarse})
\ll
C(R_N).
$$

The necessary attacks are:

1. remove raw-like entries from `G_N` and keep only diamond-center-stable
   components;
2. test whether interval profiles can be replaced by centered boundary
   histograms;
3. require deletion/insertion drift control rather than exact packet identity;
4. add a no-hidden-presentation penalty based on atom count, not hand-tuned
   taste;
5. retest against `N=8` raw-current-order victory;
6. extend the exact current-panel test to `N=9` and then prove a recurrence
   rather than brute-force `N=10`.

The living theorem is therefore sharper:

$$
\boxed{
\text{spacetime onset requires a coarser diamond-center GR quotient, not the
raw order and not scalar click-work alone.}
}
$$
