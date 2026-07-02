# Relativistic ISP v7 Paper XXXIX: Spacetime Closure Packet Campaign

**Status:** analytic campaign note, not peer reviewed, version 2026-06-30.

Paper XXXVIII reduced spacetime closure to four missing objects:

$$
\boxed{
I_{GR},\quad d_{GR},\quad \mathcal M_B,\quad \Delta^{GR}.
}
$$

This paper works on all four.

It does not use brute-force enumeration.  It builds a finite, record-intrinsic
spacetime-closure packet and then stress-tests it with hostile reviews.

The target is:

$$
\boxed{
\mathcal E^{GR}_B(k,O)
=
\mathcal A^{GR}_{B,k}(O)
+
\mathcal M_B(k)
+
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}
\le
\epsilon_{GR},
}
$$

where every term is defined from bounded record diamonds, centers, boundaries,
transport, and history drift, not from an assumed continuum metric.

## 1. Executive Result

The campaign produces a sharper finite spacetime-closure package:

$$
\boxed{
I_{GR}^{cl}(H_{B,k})
=
(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf \Theta,\mathsf r).
}
$$

The components are:

- `\mathsf A`: a same-actual diamond atlas;
- `\mathsf Q`: interval/volume/shell/center metric-measure summaries;
- `\mathsf U`: finite transport between overlapping diamond frames;
- `\mathsf F`: loop curvature/holonomy defects;
- `\mathsf W`: Ward/Bianchi boundary-of-curvature residues;
- `\mathsf \Theta`: typed source dictionary for non-hidden residues;
- `\mathsf r`: refinement/cofinal comparison maps.

It also defines:

$$
\boxed{
d_{GR}^{cl}
=
d_{\mathsf A}
+
d_{\mathsf Q}
+
d_{\mathsf U}
+
d_{\mathsf F}
+
d_{\mathsf W}
+
d_{\mathsf \Theta}
+
d_{\mathsf r}.
}
$$

with normalized weights supplied by tolerances rather than continuum units.

The manifold/Ward defect becomes:

$$
\boxed{
\mathcal M_B^{cl}(k)
=
M_{\rm dim}
+
M_{\rm interval}
+
M_{\rm shell}
+
M_{\rm drift}
+
M_{\rm Ward}
+
M_{\rm nonlookup}.
}
$$

The GR history increment is:

$$
\boxed{
\Delta^{GR}_{B,k}
=
\mathbb E_h\,
d_{GR}^{cl}\!\left(
I_{GR}^{cl}(H_{B,k+1}),
\rho_{k+1\to k}^*I_{GR}^{cl}(H_{B,k})
\right).
}
$$

Here:

- `\rho_{k+1\to k}` is the deletion/refinement comparison from the longer
  history window to the shorter one;
- `\rho^*` aligns packet labels before comparison.

The campaign does prove formal properties:

1. Minimal center-visible atlas sets exist in the finite resolved class and
   are stable as sets under controlled deletion/insertion drift; unique atlas
   choices are stable only with a positive minimizer gap.
2. `d_GR^{cl}` is a record-covariant pseudometric whenever the component
   distances are record-covariant pseudometrics.
3. `\Delta^{GR}` gives the same non-Markovian tail bound as the click law.
4. `\mathcal M_B^{cl}` does not assume manifoldlikeness; it scores failure of
   a spacetime interpretation.
5. A spacetime-like closure diamond is a joint click-plus-GR closure region.

The campaign does not prove that physical record histories make these defects
small.  That is the remaining dynamical theorem.

## 2. Inputs and Discipline

The construction imports four earlier lessons.

### 2.1 From Paper XXXIII-XXXV

The click carrier is not a raw order.  It is generated through:

$$
\mathcal C_N
\to
\mathcal P_N
\to
\mathcal W_N
\to
h.
$$

The lesson for spacetime is:

$$
\boxed{
\text{do not build }I_{GR}\text{ from raw lookup if a center-stable quotient
can carry the same closure work.}
}
$$

### 2.2 From Paper XXXVI

Spacetime is read from histories, not from one snapshot:

$$
H_{B,k}
=
(q_B(N-k),\ldots,q_B(N)).
$$

The older-history tail must be controlled:

$$
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}.
$$

### 2.3 From Paper XXXVII-XXXVIII

The click boundary and spacetime boundary should unify in a spacetime-like
region:

$$
\mathcal E^{click}_B\le\epsilon_{click},
\qquad
\mathcal E^{GR}_B\le\epsilon_{GR}.
$$

### 2.4 From the v4/v6 GR Line

The old GR line supplies gates, not a free metric:

- finite geometry records may enter the configuration law;
- same-actual covariance must quotient presentation artifacts;
- Ward/Bianchi residue must be printed or typed, not hidden;
- Einstein form is late: it appears only after the finite packet stabilizes and
  low-energy gates pass;
- the absolute scale `G` is not fixed by the record-intrinsic packet.

So this paper seeks finite closure, not a fundamental continuum metric.

## 3. Bounded Diamond Atlas

Let `B` be a bounded record diamond and `H_{B,k}` a compatible bounded history.

A candidate local diamond in the history is an interval/collar object:

$$
D=(x,y;\operatorname{Collar}_r(x,y))
$$

where:

- `x<y` are boundary records in the order;
- `I(x,y)=\{z:x<z<y\}` is the interval interior;
- `\operatorname{Collar}_r(x,y)` is the finite shell of records whose deletion
  or insertion changes the interval packet up to radius/depth `r`.

Define the diamond center:

$$
\mathcal C(D)
$$

as the minimal no-silent boundary/collar residue required to make transport
through `D` explicit.

Two diamonds are same-actual equivalent when their center-shell ledgers,
boundary maps, and transport residues agree up to the admissible zero-residue
relation:

$$
D\sim_{\rm act}D'
\quad\Longleftrightarrow\quad
d_{\rm center}(D,D')=0.
$$

The same-actual atlas is:

$$
\boxed{
\mathsf A(H_{B,k})
=
\{[D]_{\rm act}\}
}
$$

with overlap relation:

$$
[D]\leftrightarrow[D']
\quad\Longleftrightarrow\quad
\operatorname{Collar}(D)\cap\operatorname{Collar}(D')
\text{ has nonzero center-visible overlap.}
$$

This is the finite replacement for a coordinate atlas.

### 3.1 Atlas Theorem: Proof Attempt

The informal theorem target was:

$$
\boxed{
\text{minimal center-visible atlases exist and are stable.}
}
$$

This is too strong if "the atlas" means a unique chosen atlas.  A finite
history can have two equally good center-visible covers, and an arbitrarily
small deletion/insertion drift can swap which one is lexicographically chosen.

The provable target is therefore:

$$
\boxed{
\text{the set of minimal center-visible atlases exists, is record-covariant,
and is stable as a set; a unique atlas is stable only under a positive gap.}
}
$$

This is exactly the kind of stability already forced by the set-valued
transport repair in Section 5.

#### 3.1.1 Candidate Diamonds and Center Atoms

For a bounded history `H_{B,k}`, fix a finite resolution:

$$
\lambda=(r_{\max},s_{\max},\tau,\epsilon).
$$

Here:

- `r_max` is the largest collar depth allowed;
- `s_max` is the largest interval/center summary size allowed;
- `\tau` is the minimum visible center-residue threshold;
- `\epsilon` is the tolerated unresolved boundary residue.

Let:

$$
\mathfrak D_\lambda(H_{B,k})
$$

be the finite set of all candidate diamonds:

$$
D=(x,y;\operatorname{Collar}_r(x,y))
$$

with `r\le r_max` and summary size at most `s_max`.

Let:

$$
\Omega_\lambda(H_{B,k})
$$

be the finite set of center-visible atoms:

$$
\omega
=
\text{a no-silent boundary/collar residue channel with norm }\ge\tau.
$$

Each candidate diamond covers a subset:

$$
\operatorname{Cov}(D)\subseteq\Omega_\lambda(H_{B,k}).
$$

`D` covers `\omega` when `\omega` appears in the center ledger of `D` or in an
overlap transport residue involving `D`.

#### 3.1.2 Admissible Atlas Covers

A finite subset:

$$
\mathcal A\subseteq \mathfrak D_\lambda(H_{B,k})
$$

is a center-visible atlas cover when:

$$
\boxed{
\Omega_\lambda(H_{B,k})
\subseteq
\bigcup_{D\in\mathcal A}\operatorname{Cov}(D)
}
$$

up to tolerated unresolved residue `\epsilon`.

It is admissible when it also satisfies:

1. **Overlap support.**  Each connected component of the covered center atoms
   has a connected overlap graph.
2. **No-silent residue.**  Uncovered atoms are charged explicitly and cannot be
   ignored.
3. **Nonlookup budget.**

   $$
   C(\mathcal A)
   <
   \lambda_{\rm raw}\,C(R_B)
   $$

   unless raw lookup is forced by the target, in which case spacetime closure
   fails by `M_nonlookup`.
4. **Record covariance.**  The definition uses only order, centers, collars,
   residues, and same-actual classes.

Let:

$$
\operatorname{Adm}_\lambda(H_{B,k})
$$

be the set of all admissible atlas covers.

If this set is empty, the correct conclusion is not "choose the raw atlas."
The correct conclusion is:

$$
\boxed{
\text{no non-reconstructive spacetime atlas exists at this resolution.}
}
$$

That becomes a positive defect in `\mathcal M_B^{cl}`.

#### 3.1.3 Boundary-Work Atlas Functional

Define the atlas cost:

$$
\mathcal J_\lambda(\mathcal A;H)
=
\sum_{D\in\mathcal A} c(D)
+
\sum_{D\leftrightarrow E\in\mathcal A}
o(D,E)
+
u(\mathcal A)
+
n(\mathcal A).
$$

The terms are:

- `c(D)`: center-description and collar cost of using `D`;
- `o(D,E)`: boundary-work mismatch on overlaps;
- `u(A)`: charged unresolved center-visible residue;
- `n(A)`: nonlookup/reconstruction penalty.

All four are required to be record-covariant.

The minimal atlas set is:

$$
\boxed{
\operatorname{Atlas}_\lambda(H)
=
\operatorname*{Argmin}_{\mathcal A\in\operatorname{Adm}_\lambda(H)}
\mathcal J_\lambda(\mathcal A;H).
}
$$

#### Atlas Theorem 0: Finite Existence and Covariance

Assume:

1. `H_{B,k}` is bounded, hence `\mathfrak D_\lambda(H_{B,k})` and
   `\Omega_\lambda(H_{B,k})` are finite;
2. `\operatorname{Adm}_\lambda(H_{B,k})` is nonempty;
3. `\mathcal J_\lambda` is finite and record-covariant on admissible covers.

Then `\operatorname{Atlas}_\lambda(H_{B,k})` is nonempty and finite.
Moreover, record isomorphisms map minimal atlases to minimal atlases.

**Proof.**

Because `\mathfrak D_\lambda(H)` is finite, the power set of candidate
diamonds is finite.  Therefore the admissible subfamily is finite.  By
assumption it is nonempty, and `\mathcal J_\lambda` is finite on it, so a
minimum exists.  The set of minimizers is finite and nonempty.

If `\phi:H\to H'` is a record isomorphism, covariance maps candidate diamonds
to candidate diamonds, center atoms to center atoms, covers to covers, and
preserves `\mathcal J_\lambda`.  Hence an atlas cover minimizes for `H` iff
its transported cover minimizes for `H'`. `\square`

#### 3.1.4 Stability Under Deletion/Insertion

Let:

$$
\delta(H,H')
$$

be the boundary-work size of a bounded deletion/insertion/refinement move.

Assume a bi-admissible transported comparison between candidates of `H` and
`H'`: admissible covers in the compared domain can be pushed forward, and
minimizers in the target compared domain can be pulled back without leaving the
admissible class.  Assume further that:

$$
\left|
\mathcal J_\lambda(\mathcal A;H)
-
\mathcal J_\lambda(\rho\mathcal A;H')
\right|
\le
L_\lambda\delta(H,H')
$$

for every admissible atlas cover whose transport is defined, and likewise for
the pullback comparison.  This is the atlas-level Lipschitz hypothesis.  It is
the exact finite analogue of controlled deletion/insertion drift.

Define the `\gamma`-near-minimizer set:

$$
\operatorname{Atlas}_\lambda^\gamma(H)
=
\left\{
\mathcal A\in\operatorname{Adm}_\lambda(H):
\mathcal J_\lambda(\mathcal A;H)
\le
\inf\mathcal J_\lambda(\cdot;H)+\gamma
\right\}.
$$

#### Atlas Theorem A: Set-Valued Stability

Under the bi-admissible Lipschitz hypothesis:

$$
\boxed{
\rho\operatorname{Atlas}_\lambda(H)
\subseteq
\operatorname{Atlas}_\lambda^{2L_\lambda\delta(H,H')}(H')
}
$$

on the compared admissible domain.

**Proof.**

Let `\mathcal A` minimize `\mathcal J_\lambda(\cdot;H)` in the compared
domain.  Let `\mathcal B'` minimize `\mathcal J_\lambda(\cdot;H')` in the
compared target domain, and pull it back to an admissible cover `\mathcal B`
of `H`.  Since `\mathcal A` is minimal in `H`,

$$
\mathcal J_\lambda(\mathcal A;H)
\le
\mathcal J_\lambda(\mathcal B;H).
$$

Apply the Lipschitz comparison to both sides:

$$
\mathcal J_\lambda(\rho\mathcal A;H')
\le
\mathcal J_\lambda(\mathcal A;H)+L_\lambda\delta
\le
\mathcal J_\lambda(\mathcal B;H)+L_\lambda\delta
\le
\mathcal J_\lambda(\mathcal B';H')+2L_\lambda\delta.
$$

Thus `\rho\mathcal A` is a `2L_\lambda\delta`-near minimizer for `H'`.
`\square`

#### Atlas Theorem B: Unique Stability With a Gap

Suppose `H` has a unique minimizer `\mathcal A_*` and a positive gap:

$$
\Gamma_\lambda(H)
=
\min_{\mathcal A\ne\mathcal A_*}
\left[
\mathcal J_\lambda(\mathcal A;H)
-
\mathcal J_\lambda(\mathcal A_*;H)
\right]
>0.
$$

If:

$$
2L_\lambda\delta(H,H')<\Gamma_\lambda(H),
$$

then every compared minimizer for `H'` is transported from the same atlas
class `\mathcal A_*`, up to zero-distance/same-actual equivalence.

**Proof.**

Apply Atlas Theorem A in the reverse comparison direction to any compared
minimizer of `H'`.  Its pullback is a `2L_\lambda\delta`-near minimizer of
`H`.  If this tolerance is smaller than the gap, the near-minimizer set of `H`
contains only `\mathcal A_*` up to zero-distance equivalence.  Pushing forward
again gives the claim. `\square`

#### 3.1.5 What This Proves and What It Does Not

This proves the atlas theorem in the finite, tolerance-resolved sense:

$$
\boxed{
\text{minimal atlas sets exist; unique atlas choices need a margin.}
}
$$

It does not prove that a nonlookup admissible atlas exists for every bounded
history.  If the only cover is raw reconstruction, the atlas functional must
fail the nonlookup budget and charge `M_nonlookup`.

Thus the remaining atlas-adjacent problem is sharper:

$$
\boxed{
\text{prove that physical click-selected histories admit nonlookup
center-visible covers at useful tolerances.}
}
$$

## 4. Metric-Measure Packet `\mathsf Q`

For each same-actual diamond class `[D]`, define:

$$
\mathsf q(D)
=
\left(
V_D,
H_D,
L_D,
S_D,
C_D,
P_D
\right).
$$

The entries are:

- `V_D=|I(x,y)|`: interval volume in record count;
- `H_D`: height/longest-chain profile inside `D`;
- `L_D`: layer histogram relative to lower and upper boundary;
- `S_D`: shell profile, counting records by boundary response depth;
- `C_D`: center-shell residue histogram;
- `P_D`: rooted interval-pattern profile, compressed through the center.

The packet over the atlas is:

$$
\boxed{
\mathsf Q(H_{B,k})
=
\{\mathsf q(D):[D]\in\mathsf A(H_{B,k})\}.
}
$$

This is not a continuum metric.  It is the record-intrinsic data from which a
metric interpretation may be read after closure.

### 4.1 Why `\mathsf Q` Is Coarser Than Raw Order

The raw order remembers every relation.  `\mathsf Q` remembers only
center-stable interval, shell, and rooted-pattern summaries.

The admissibility condition is:

$$
\boxed{
\mathcal W_B
\preceq
\mathsf Q_B
\prec
R_B
}
$$

where:

- `\mathcal W_B` is the scalar-work click quotient;
- `R_B` is raw record-order lookup.

If `\mathsf Q_B=R_B`, the packet has failed non-reconstruction.

## 5. Transport Packet `\mathsf U`

For overlapping diamond classes `[D]` and `[E]`, define a transport candidate:

$$
U_{D\to E}
:
\mathcal C(D)|_{D\cap E}
\to
\mathcal C(E)|_{D\cap E}.
$$

It is selected by least boundary work:

$$
\boxed{
U_{D\to E}
\in
\operatorname*{argmin}_{U}
\operatorname{BW}_{D,E}(U).
}
$$

If the minimizer is not unique, keep the whole minimizing set:

$$
\mathsf U_{D,E}
=
\operatorname*{Argmin}_{U}\operatorname{BW}_{D,E}(U).
$$

This avoids a false uniqueness assumption.

The transport packet is:

$$
\boxed{
\mathsf U(H_{B,k})
=
\{\mathsf U_{D,E}:D\leftrightarrow E\}.
}
$$

### Theorem 1: Transport Covariance

If the center ledgers and boundary-work functional are record-covariant, then
`\mathsf U` is record-covariant as a set-valued transport.

**Proof.**

A record isomorphism maps diamonds to diamonds, centers to centers, overlaps
to overlaps, and preserves boundary-work values.  Therefore it maps minimizers
of `\operatorname{BW}_{D,E}` to minimizers of the transported problem. `\square`

## 6. Curvature Packet `\mathsf F`

For a loop in the overlap graph:

$$
\ell=(D_0,D_1,\ldots,D_m,D_0),
$$

choose transports:

$$
U_i\in\mathsf U_{D_i,D_{i+1}}.
$$

The loop defect is:

$$
F_\ell(U_0,\ldots,U_m)
=
U_m\cdots U_1U_0-\operatorname{id}
$$

when transports are represented linearly.  If transports are represented by
kernels, relations, or couplings, replace subtraction by the corresponding
record-intrinsic defect distance to the identity relation.

Because transports may be set-valued, define the curvature interval:

$$
\boxed{
\mathsf F_\ell
=
\left\{
F_\ell(U_0,\ldots,U_m):
U_i\in\mathsf U_{D_i,D_{i+1}}
\right\}.
}
$$

The curvature packet is:

$$
\boxed{
\mathsf F(H_{B,k})
=
\{\mathsf F_\ell:\ell\text{ a bounded loop in }\mathsf A\}.
}
$$

Nonzero loop defect is not automatically bad.  It is the finite curvature
candidate.  The bad object is hidden or non-typed curvature residue.

## 7. Ward/Bianchi Packet `\mathsf W`

The Ward/Bianchi packet measures closure of loop defects across closed
two-surfaces of the overlap graph.

Let `\Sigma` be a finite closed family of loops.  Define:

$$
\partial\mathsf F(\Sigma)
=
\sum_{\ell\in\partial\Sigma}
\operatorname{or}(\ell,\Sigma)\,\mathsf F_\ell
$$

where `\operatorname{or}` is the orientation sign.  In set-valued transport,
take the minimum possible boundary defect and the residual ambiguity:

$$
\mathsf W_\Sigma
=
\left(
\inf \|\partial\mathsf F(\Sigma)\|,
\operatorname{diam}\{\partial\mathsf F(\Sigma)\}
\right).
$$

The Ward/Bianchi packet is:

$$
\boxed{
\mathsf W(H_{B,k})
=
\{\mathsf W_\Sigma:\Sigma\text{ bounded closed loop-surface}\}.
}
$$

This is the finite record version of:

$$
\nabla\cdot G=0
$$

or Bianchi closure, but without assuming a differentiable manifold.

## 8. Source Dictionary `\mathsf \Theta`

A nonzero Ward/Bianchi residue is not allowed to vanish silently.

Define a typed source dictionary:

$$
\mathsf \Theta(H_{B,k})
=
D_{\rm src}(\mathsf W,\mathsf R_B).
$$

The dictionary assigns each persistent residue to one of:

1. boundary residue;
2. matter/source residue;
3. torsion/non-metricity-like residue;
4. higher-curvature residue;
5. unresolved failure.

The fifth class is charged:

$$
M_{\rm Ward}>0.
$$

Thus source terms are not assumed.  They are typed residues of finite transport
closure.

## 9. Refinement Packet `\mathsf r`

If `H_{B,k+1}` refines or extends `H_{B,k}`, there is a comparison:

$$
\rho_{k+1\to k}
:
H_{B,k+1}\to H_{B,k}.
$$

This induces packet maps:

$$
\mathsf r_{k+1\to k}
:
I_{GR}^{cl}(H_{B,k+1})
\to
I_{GR}^{cl}(H_{B,k}).
$$

The refinement packet is:

$$
\boxed{
\mathsf r(H_{B,k})
=
\{\mathsf r_{j+1\to j}:j\le k\}.
}
$$

It records whether the spacetime readout survives longer history, coarser
panels, and bounded refinement.

## 10. Definition of `I_GR^{cl}`

The closure packet is:

$$
\boxed{
I_{GR}^{cl}(H_{B,k})
=
(\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf \Theta,\mathsf r).
}
$$

It is defined only when:

1. the same-actual quotient is nonempty;
2. center-shell summaries are finite;
3. overlap transport exists on the chosen atlas;
4. Ward residues are typed or explicitly unresolved;
5. refinement maps are defined for the included history.

If these fail, the history does not yet carry a finite spacetime packet.

This is a construction target, not a theorem that every record history is
spacetime.

## 11. Packet Distance `d_GR^{cl}`

Define component distances:

$$
d_{\mathsf A},\quad
d_{\mathsf Q},\quad
d_{\mathsf U},\quad
d_{\mathsf F},\quad
d_{\mathsf W},\quad
d_{\mathsf \Theta},\quad
d_{\mathsf r}.
$$

Each is a record-covariant pseudometric:

- `d_A`: edit/bottleneck distance between same-actual overlap atlases;
- `d_Q`: earthmover/TV distance between center-shell metric-measure summaries;
- `d_U`: Hausdorff distance between transport-minimizer sets;
- `d_F`: loop-defect distance after matching bounded loops;
- `d_W`: Ward/Bianchi residue distance;
- `d_Theta`: typed source dictionary distance;
- `d_r`: refinement/cofinality drift distance.

The full distance is:

$$
\boxed{
d_{GR}^{cl}(X,Y)
=
\sum_{\xi}
w_\xi d_\xi(X,Y),
\qquad
\xi\in\{\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r\}.
}
$$

The weights are not continuum constants.  They are tolerance normalizations:

$$
w_\xi=\epsilon_\xi^{-1}
$$

or lexicographic gates when one component must pass before another matters.

### Theorem 2: Packet Distance Is a Pseudometric

If each component `d_\xi` is a record-covariant pseudometric and
`w_\xi\ge0`, then `d_GR^{cl}` is a record-covariant pseudometric.

If the zero-distance equivalence relation is quotiented, `d_GR^{cl}` becomes a
metric on packet equivalence classes.

**Proof.**

Nonnegativity, symmetry, and the triangle inequality are preserved under
nonnegative weighted sums.  Record covariance is preserved because each
component is covariant.  Quotienting by zero distance is the standard metric
quotient of a pseudometric space. `\square`

## 12. Conditional GR Residual

Given a panel:

$$
O_{B,k}=\Phi(H_{B,k}),
$$

define the conditional packet law:

$$
\mu^{GR}_{B,k,O}
=
\operatorname{Law}_h(I_{GR}^{cl}(H_{B,k})\mid O_{B,k}).
$$

The GR spread residual is:

$$
\boxed{
\mathcal A^{GR}_{B,k}(O)
=
\mathbb E_h
\left[
\inf_{G_O}
d_{GR}^{cl}(I_{GR}^{cl}(H_{B,k}),G_O)
\mid O_{B,k}
\right].
}
$$

Here `G_O` ranges over packet representatives for the observed cell.  In a
finite packet-label model, `G_O` can be the Fréchet median.  If the packet
space is discrete with `0/1` distance, this reduces to conditional
misclassification/spread.

This definition measures how much spacetime readout remains unresolved after
the actual panel is known.

## 13. Manifold/Ward Defect `\mathcal M_B^{cl}`

Define:

$$
\boxed{
\mathcal M_B^{cl}(k)
=
M_{\rm dim}
+
M_{\rm interval}
+
M_{\rm shell}
+
M_{\rm drift}
+
M_{\rm Ward}
+
M_{\rm nonlookup}.
}
$$

### 13.1 Dimension Consistency

Let `D_1,D_2,\ldots` be admissible dimension estimates from:

- relation fraction;
- height scaling;
- interval-size distribution;
- shell growth;
- center-shell response.

Then:

$$
M_{\rm dim}
=
\operatorname{Disp}(D_1,D_2,\ldots)
+
\operatorname{OutOfRange}(D_i).
$$

This does not assume a dimension.  It penalizes disagreement among intrinsic
dimension witnesses.

### 13.2 Recursive Interval Heredity

For bounded subdiamonds `D\subset B`, compare the packet of `D` with the
rescaled/restricted packet of `B`:

$$
M_{\rm interval}
=
\mathbb E_D
d_{GR}^{cl}\!\left(
I_{GR}^{cl}(D),
I_{GR}^{cl}(B)|_D
\right).
$$

This is the "diamonds inside diamonds look like the same kind of object" test.

### 13.3 Shell Regularity

For shells around boundary/center roots, define:

$$
M_{\rm shell}
=
\sum_r
\operatorname{Var}_{\rm roots}
\left(
\#\operatorname{Shell}_r
\right)
+
\operatorname{Anisotropy}_r.
$$

The exact normalization must be calibrated by the null law, but the invariant
is clear: staged or clustered orders tend to have abnormal shell load.

### 13.4 Deletion/Insertion Drift

Let `Del_i` delete a bounded admissible record set and `Ins_i` insert a
compatible bounded set.  Define:

$$
M_{\rm drift}
=
\mathbb E_i\,
d_{GR}^{cl}\!\left(
I_{GR}^{cl}(H),
I_{GR}^{cl}(\operatorname{Del}_iH)
\right)
+
\mathbb E_i\,
d_{GR}^{cl}\!\left(
I_{GR}^{cl}(H),
I_{GR}^{cl}(\operatorname{Ins}_iH)
\right).
$$

This tests whether the spacetime packet is stable under local record
perturbations.

### 13.5 Ward/Bianchi Residue

Let `\mathsf W_{\rm untyped}` be Ward/Bianchi residue not assigned to a
licensed source dictionary.  Define:

$$
M_{\rm Ward}
=
\|\mathsf W_{\rm untyped}\|
+
\operatorname{Ambiguity}(\mathsf \Theta).
$$

The rule is no-silent:

$$
\boxed{
\text{untyped conservation residue is charged, not hidden.}
}
$$

### 13.6 Nonlookup Defect

Let:

$$
C(I_{GR}^{cl})
$$

be the atom-count/operator-description complexity of the packet.  Let:

$$
C(R_B)
$$

be raw-order lookup complexity.  Define:

$$
M_{\rm nonlookup}
=
\left[
\frac{C(I_{GR}^{cl})}{C(R_B)}
-\lambda_{\rm max}
\right]_+.
$$

This prevents `I_GR` from quietly becoming raw reconstruction.

### Theorem 3: `\mathcal M_B^{cl}` Is Not a Manifold Assumption

`\mathcal M_B^{cl}` is a defect functional.  It can be evaluated on any bounded
record history for which the component packets exist.  Smallness of
`\mathcal M_B^{cl}` is the manifoldlike condition; it is not assumed.

**Proof.**

Each summand is defined as a discrepancy, dispersion, drift, residue, or
complexity excess.  None requires the history to be manifoldlike in order to
be computed.  Manifoldlikeness enters only as the small-defect regime. `\square`

## 14. GR History Increment `\Delta^{GR}`

A longer history and a shorter history do not have identical packet domains.
They must be aligned before comparison.

Let:

$$
\rho_{k+1\to k}:H_{B,k+1}\to H_{B,k}
$$

be the forgetful/refinement comparison.  It induces:

$$
\rho_{k+1\to k}^*I_{GR}^{cl}(H_{B,k})
$$

as the shorter packet lifted to the longer comparison domain.

Define:

$$
\boxed{
\Delta^{GR}_{B,k}
=
\mathbb E_h\,
d_{GR}^{cl}\!\left(
I_{GR}^{cl}(H_{B,k+1}),
\rho_{k+1\to k}^*I_{GR}^{cl}(H_{B,k})
\right).
}
$$

### Theorem 4: GR Tail Bound

For any `L>k`:

$$
\boxed{
\mathbb E_h\,
d_{GR}^{cl}\!\left(
I_{GR}^{cl}(H_{B,L}),
\rho_{L\to k}^*I_{GR}^{cl}(H_{B,k})
\right)
\le
\sum_{j=k}^{L-1}\Delta^{GR}_{B,j}.
}
$$

**Proof.**

Compare the packet chain:

$$
H_{B,k}
\to
H_{B,k+1}
\to
\cdots
\to
H_{B,L}.
$$

At each step align the shorter packet into the longer comparison domain.  The
triangle inequality for `d_GR^{cl}` gives a telescoping upper bound by the sum
of adjacent aligned distances.  Taking `h_B`-expectation yields the result.
`\square`

This is the GR analogue of the click-history tail theorem.

## 15. Spacetime Closure Condition

The closure error is:

$$
\boxed{
\mathcal E^{GR,cl}_B(k,O)
=
\mathcal A^{GR}_{B,k}(O)
+
\mathcal M_B^{cl}(k)
+
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}.
}
$$

The bounded region is spacetime-closed at tolerance `\epsilon_GR` if:

$$
\boxed{
\mathcal E^{GR,cl}_B(k,O)\le\epsilon_{GR}.
}
$$

The joint spacetime-like experimental boundary is:

$$
\boxed{
B^{ST}_\epsilon
=
\operatorname*{argmin}_{B,k,O}C_B(k,O)
}
$$

subject to:

$$
\boxed{
\mathcal E^{click}_B(k,O)\le\epsilon_{click},
\qquad
\mathcal E^{GR,cl}_B(k,O)\le\epsilon_{GR}.
}
$$

## 16. What Is Now Defined

The four missing objects from Paper XXXVIII now have analytic forms:

1. `I_GR` becomes:

   $$
   I_{GR}^{cl}
   =
   (\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r).
   $$

2. `d_GR` becomes:

   $$
   d_{GR}^{cl}
   =
   \sum_\xi w_\xi d_\xi.
   $$

3. `\mathcal M_B` becomes:

   $$
   \mathcal M_B^{cl}
   =
   M_{\rm dim}
   +
   M_{\rm interval}
   +
   M_{\rm shell}
   +
   M_{\rm drift}
   +
   M_{\rm Ward}
   +
   M_{\rm nonlookup}.
   $$

4. `\Delta^{GR}` becomes the aligned packet-history increment:

   $$
   \Delta^{GR}_{B,k}
   =
   \mathbb E_h\,
   d_{GR}^{cl}(
   I_{GR}^{cl}(H_{B,k+1}),
   \rho_{k+1\to k}^*I_{GR}^{cl}(H_{B,k})
   ).
   $$

These are definitions strong enough to run a proof program.  They are not yet
a proof that the physical click law makes spacetime closure typical.

### 16.1 Claim Boundary

This closes a definition gap, not the whole spacetime problem.

Before this paper, the statement "spacetime closure is small" depended on
symbols whose finite record meaning was still loose.  After this paper, those
symbols have a proposed record-intrinsic meaning:

$$
I_{GR}^{cl},\quad d_{GR}^{cl},\quad \mathcal M_B^{cl},\quad
\Delta^{GR}_{B,k}.
$$

The remaining question is dynamical:

$$
\boxed{
\text{do physical bounded histories selected by the click law make these
quantities small at useful tolerances?}
}
$$

That is the theorem still missing.

## 17. Full Campaign Attacks

### Attack 1: "`I_GR^{cl}` is just raw order in disguise."

Partly sustained.

The atlas and packet can become raw if every interval, shell, and rooted
pattern is retained with excessive resolution.

Repair:

1. compress through center-stable summaries;
2. charge `M_nonlookup`;
3. require:

   $$
   \mathcal W_B
   \preceq
   I_{GR}^{cl}
   \prec
   R_B.
   $$

Remaining theorem:

$$
\boxed{
\text{prove a nonlookup bound for the physical packet resolution.}
}
$$

### Attack 2: "Transport minimizers need not be unique."

Sustained and repaired.

The construction uses set-valued transports:

$$
\mathsf U_{D,E}
=
\operatorname{Argmin}\operatorname{BW}_{D,E}.
$$

Curvature and distance use Hausdorff/set distances.  Nonuniqueness becomes a
finite ambiguity defect, not a hidden choice.

### Attack 3: "Curvature assumes a vector bundle."

Rejected at the finite level.

The loop defect only requires composition of admissible transports and a
distance to identity.  Linear matrices are one representation, not the
definition.

Remaining theorem:

$$
\boxed{
\text{identify the physical transport category: kernels, couplings,
relations, or finite modules.}
}
$$

### Attack 4: "Ward/Bianchi residue is hand-typed."

Sustained.

The source dictionary `\mathsf\Theta` is a required construction, not a solved
law.

Opening followed: use no-silent rule.  Untyped residue is charged:

$$
M_{\rm Ward}>0.
$$

Remaining theorem:

$$
\boxed{
\text{derive }D_{\rm src}\text{ from stable residue sectors of the click law.}
}
$$

### Attack 5: "`d_GR` weights are arbitrary."

Sustained unless handled as tolerances.

The paper does not claim unique weights.  It uses either:

- tolerance normalization `w_\xi=\epsilon_\xi^{-1}`;
- or lexicographic gates.

The physical theorem should prove robustness: closure should not depend
sensitively on small changes of weights inside a tolerated class.

### Attack 6: "`\mathcal M_B` still assumes manifoldlikeness."

Rejected in definition, sustained in calibration.

The defect is computable without assuming manifoldlikeness.  But its null
calibration remains open.  A final theorem must prove which defect profiles are
typical of spacetime-like histories and which adversaries are rejected.

### Attack 7: "Shell regularity fails near black holes or matter."

Partly sustained.

The shell defect must be environment-aware.  Near massive or horizon-like
regions, shell growth may be distorted but still stable.  Therefore
`M_shell` should compare against the local packet's own transport/source
dictionary, not against flat sprinkling.

This creates a new subtarget:

$$
\boxed{
\text{derive environment-conditioned manifoldlikeness null laws.}
}
$$

### Attack 8: "The GR tail may never decay."

Accepted as a possible physical outcome.

If:

$$
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}
$$

does not become small, the bounded region is not spacetime-closed at that
tolerance.  The theory should allow this.

### Attack 9: "Einstein equations are still not derived."

Correct.

This paper defines closure packets.  Einstein form appears only after:

1. `I_GR^{cl}` is stable;
2. Ward/Bianchi residue is typed or vanishes;
3. low-energy/cofinal gates pass;
4. the v6 gravity scale no-go is respected.

The result is spacetime closure, not the full gravitational field equations.

## 18. Hostile Review Round 1

### Review 1: "This just renames old placeholders."

Rejected.

The placeholders have been expanded into explicit finite objects:

$$
\mathsf A,\mathsf Q,\mathsf U,\mathsf F,\mathsf W,\mathsf\Theta,\mathsf r.
$$

Each has a construction route and a failure mode.

### Review 2: "The atlas is coordinate-free but still arbitrary."

Partly resolved by Section 3.1.

The atlas is no longer selected by a human preference.  At finite resolution it
is the minimizer set of the record-covariant boundary-work functional
`\mathcal J_\lambda` over admissible center-visible covers.

The honest result is set-valued:

$$
\boxed{
\text{minimal atlas sets exist and are stable; unique atlases require a gap.}
}
$$

The remaining issue is not finite existence.  It is physical admissibility:
prove that click-selected histories have useful nonlookup center-visible
covers, rather than only raw/reconstructive ones.

### Review 3: "Same-actual equivalence may collapse real distinctions."

Sustained unless zero-residue equivalence is derived.

The same-actual relation must be generated by record isomorphism, center
transport, and zero boundary-work residue.  It cannot be declared by human
interpretation.

### Review 4: "The packet distance may be too weak."

Sustained.

If `d_GR^{cl}` misses an instability channel, closure is false-positive.  The
defense is the Ward/no-silent rule: any stable residual not represented in the
packet becomes a new component or a charged unresolved residue.

### Review 5: "The packet distance may be too strong."

Sustained.

If `d_GR^{cl}` distinguishes gauge/presentation artifacts, closure is
false-negative.  The defense is same-actual quotienting and zero-distance
metric quotienting.

## 19. Hostile Review Round 2: Openings Followed

### Opening A: Environment-Conditioned Null Laws

Flat-lab manifoldlikeness cannot be the only null.  Define a packet class:

$$
\mathcal K
=
\operatorname{Class}(I_{GR}^{cl})
$$

such as flat, massive-object, horizon-like, entangled, or pre-spacetime.

Then calibrate:

$$
\mathcal M_B^{cl,\mathcal K}
$$

against the local packet class.

This avoids punishing a curved but stable region for not looking flat.

### Opening B: Set-Valued Geometry

If transports or packets are ambiguous, closure should require small diameter:

$$
\operatorname{diam}_{d_{GR}^{cl}}
\operatorname{Law}(I_{GR}^{cl}\mid O)
\le
\epsilon.
$$

Thus classical spacetime appears when the compatible packet cloud is tight, not
when there is a single hidden packet by fiat.

### Opening C: Ward Typing From Click Sectors

Source dictionary entries should be tied to stable click sectors.  A residue is
typed as matter/source only if it correlates with a stable record-click sector
under bounded history projection.

Candidate rule:

$$
\Theta_\alpha
\text{ is licensed}
\quad\Longleftrightarrow\quad
I_h(\Theta_\alpha;S_B\mid O_B)
\text{ is stable under refinement}.
$$

This is not yet proved, but it links matter/source typing to the click law
instead of adding source labels by hand.

### Opening D: Closure Scaling

A true spacetime region needs a scaling theorem:

$$
C_B(k_\epsilon,O_\epsilon)
\le
F(\epsilon,\mathcal K).
$$

Paper XXXVIII named this `F_closure`.  Paper XXXIX refines the environment
classes `\mathcal K` using the packet itself.

## 20. Barandes/ISP Alignment Campaign

This section audits the three ways the construction could accidentally stop
being an ISP-style history law:

1. the panel might collapse back to one-step Markov prediction;
2. the atlas might smuggle in coordinates, labels, or raw lookup;
3. `h_B` might become primitive stochastic dynamics rather than a
   deterministic/projective bounded-history weight.

The campaign result is:

$$
\boxed{
\text{Paper XXXIX is Barandes-aligned only if all three gates pass.}
}
$$

The three gates are:

$$
\boxed{
\text{history sufficiency,}
\qquad
\text{record-intrinsic nonlookup atlas,}
\qquad
\text{projective deterministic }h_B.
}
$$

### 20.1 Gate I: Non-Markovian History Sufficiency

Let `Y_B` be any bounded target readout:

- the next click;
- a selected shadow sector;
- a finite GR packet label;
- or a joint click-plus-GR closure class.

Let:

$$
O_{B,k}=\Phi_k(H_{B,k})
$$

be the admissible panel extracted from the bounded history:

$$
H_{B,k}=(q_B(N-k),\ldots,q_B(N)).
$$

The projected prediction from depth `k` is:

$$
\boxed{
K^Y_{B,k}(y\mid o)
=
\frac{
\sum_{H:\ O_{B,k}(H)=o,\ Y_B(H)=y}h_B(H)
}{
\sum_{H:\ O_{B,k}(H)=o}h_B(H)
}.
}
$$

This is not a primitive transition probability.  It is the normalized
projection of the bounded history weight onto a partial panel.

Define the history-depth drift:

$$
\boxed{
\Delta^Y_{B,k}
=
\mathbb E_h\,
TV\!\left(
K^Y_{B,k+1}(\cdot\mid O_{B,k+1}),
K^Y_{B,k}(\cdot\mid O_{B,k})
\right).
}
$$

The comparison uses the natural forgetful map:

$$
H_{B,k+1}\mapsto H_{B,k}.
$$

#### Alignment Theorem 1: One-Step Markov Is Only an Approximation

For any `L>k`:

$$
\boxed{
\mathbb E_h\,
TV\!\left(
K^Y_{B,L},
K^Y_{B,k}
\right)
\le
\sum_{j=k}^{L-1}\Delta^Y_{B,j}.
}
$$

**Proof.**

Along each compatible bounded history chain:

$$
H_{B,k}\to H_{B,k+1}\to\cdots\to H_{B,L},
$$

the triangle inequality for total variation gives the telescoping bound.  Then
take the normalized `h_B` expectation.  No Markov assumption is used.
`\square`

The sufficient history depth for target `Y` is:

$$
\boxed{
m^Y_B(\epsilon)
=
\min\left\{
k:
\sum_{j=k}^{\infty}\Delta^Y_{B,j}
\le
\epsilon
\right\}.
}
$$

Interpretation:

- if `m^Y_B(\epsilon)=0`, the one-panel law is an effective approximation at
  tolerance `\epsilon`;
- if `0<m^Y_B(\epsilon)<\infty`, the law is genuinely non-Markovian but
  bounded;
- if no finite `k` works, the chosen boundary/panel does not close the target.

Thus:

$$
\boxed{
\Pr(Y_{N+1}\mid W_N)
\text{ is never fundamental; it is permitted only after the history tail
has washed out.}
}
$$

#### Hostile Attacks on Gate I

**Attack I.1: hidden periodic memory.**

Two histories share the same current panel but differ by an older parity,
phase, or staged block that changes `Y_B`.  Then `\Delta^Y_{B,k}` does not
decay until that older layer is included.  This does not falsify the framework;
it forces a larger `k`.

**Attack I.2: infinite tail.**

If:

$$
\sum_{j=k}^{\infty}\Delta^Y_{B,j}
$$

never becomes small, then the bounded panel fails.  The theory must say
"not closed," not invent a one-step stochastic kernel.

**Attack I.3: apparent Markov success.**

If `\Delta^Y_{B,0}` is small, one-step prediction is a good engineering
approximation.  But it remains derived from bounded histories, not primitive
ontology.

Gate I passes only for targets and tolerances with finite `m^Y_B(\epsilon)`.

### 20.2 Gate II: Record-Intrinsic Nonlookup Atlas

The atlas risk is that `I_{GR}^{cl}` might look finite and intrinsic while
quietly carrying raw-order lookup.

Section 3.1 already proves the finite atlas theorem once the admissible cover
class is nonempty.  Gate II turns that into a pass/fail score.

Define the atlas alignment error:

$$
\boxed{
\mathcal E^{atlas}_{B,\lambda}
=
U_\lambda
+
N_\lambda
+
D_\lambda
+
A_\lambda.
}
$$

The four terms are:

- `U_lambda`: charged uncovered center-visible residue;
- `N_lambda`: nonlookup excess;
- `D_lambda`: deletion/insertion atlas drift;
- `A_lambda`: ambiguity diameter of the minimal atlas set.

More explicitly:

$$
N_\lambda
=
\left[
\frac{C(\operatorname{Atlas}_\lambda)}
{C(R_B)}
-
\lambda_{\rm raw}
\right]_+.
$$

And:

$$
D_\lambda
=
\mathbb E_h\,
d_{\mathsf A}\!\left(
\operatorname{Atlas}_\lambda(H_{B,k+1}),
\rho^*\operatorname{Atlas}_\lambda(H_{B,k})
\right).
$$

The atlas is Barandes-compatible at tolerance `\epsilon_A` when:

$$
\boxed{
\mathcal E^{atlas}_{B,\lambda}\le\epsilon_A.
}
$$

#### Alignment Theorem 2: Atlas Compatibility

If:

1. the finite atlas theorem applies;
2. `\mathcal E^{atlas}_{B,\lambda}\le\epsilon_A`;
3. same-actual zero-distance quotienting is used;

then the atlas component of `I_{GR}^{cl}` is record-covariant,
non-reconstructive up to `\epsilon_A`, and stable under bounded
deletion/insertion drift up to `\epsilon_A`.

**Proof.**

Finite existence and covariance come from Atlas Theorem 0.  Set-valued
stability comes from Atlas Theorem A.  The nonlookup term `N_lambda` bounds
raw reconstruction.  The uncovered residue term `U_lambda` enforces no-silent
coverage.  The drift term `D_lambda` bounds history instability.  The ambiguity
diameter term `A_lambda` prevents large hidden set-valued freedom from being
called classical geometry. `\square`

#### Hostile Attacks on Gate II

**Attack II.1: relabeling.**

Rename every record.  The atlas must transport, not change.  Failure means the
construction used labels or coordinates.

**Attack II.2: raw lookup.**

Keep enough interval/rooted data that the atlas reconstructs `R_B`.  This is
not a success.  It is charged by `N_lambda` and by `M_nonlookup`.

**Attack II.3: tied atlases.**

Multiple minimal covers can exist.  The stable object is the minimizer set, not
a hand-picked representative.  A unique atlas requires a positive gap.

**Attack II.4: entangled outside sector.**

A distant sector is outside only if its effect is washed into the bounded
boundary residue.  If it changes a center-visible atom, it belongs inside the
record boundary for this prediction.

Gate II passes only if the atlas is smaller than raw lookup while still
covering all relevant center-visible residue.

### 20.3 Gate III: Projective Deterministic `h_B`

The final risk is more subtle.  We use probability notation in predictions,
but the intended primitive is not a stochastic transition.  The primitive is a
positive weight on compatible bounded histories:

$$
h_B:\Gamma_B\to\mathbb R_{>0}.
$$

At finite depth:

$$
h_{B,k}:\Gamma_{B,k}\to\mathbb R_{>0}.
$$

Let:

$$
\pi_{k+1\to k}:\Gamma_{B,k+1}\to\Gamma_{B,k}
$$

forget the oldest retained layer.

The projective consistency condition is:

$$
\boxed{
h_{B,k}(H)
=
\sum_{H':\pi_{k+1\to k}(H')=H}
h_{B,k+1}(H').
}
$$

Equivalently, for normalized finite measures:

$$
\boxed{
\bar h_{B,k}
=
(\pi_{k+1\to k})_\#\bar h_{B,k+1}.
}
$$

Define the projective defect:

$$
\boxed{
\Pi_{B,k}
=
TV\!\left(
\bar h_{B,k},
(\pi_{k+1\to k})_\#\bar h_{B,k+1}
\right).
}
$$

The exact Barandes-aligned case is:

$$
\Pi_{B,k}=0.
$$

The tolerated finite case requires:

$$
\sum_{j=k}^{\infty}\Pi_{B,j}\le\epsilon_h.
$$

#### Alignment Theorem 3: Probability Is Projection, Not Primitive Randomness

Assume:

1. the full bounded-history readout is deterministic:

   $$
   Y_B:\Gamma_B\to\mathcal Y;
   $$

2. `h_B` is projectively consistent;
3. `O_B` is an admissible partial panel.

Then:

$$
\boxed{
\Pr_B(Y_B=y\mid O_B=o)
=
\frac{
\sum_{H:\ O_B(H)=o,\ Y_B(H)=y}h_B(H)
}{
\sum_{H:\ O_B(H)=o}h_B(H)
}
}
$$

is a projected effective probability.  Given the full history:

$$
\Pr_B(Y_B=y\mid H)\in\{0,1\}.
$$

**Proof.**

The full history determines the readout by assumption.  A partial panel `O_B=o`
selects a fiber of compatible histories.  Normalizing the positive weights on
that fiber gives the displayed conditional projection.  Projective consistency
ensures that conditioning after a finer projection and then forgetting agrees
with conditioning directly on the coarser panel. `\square`

#### Hostile Attacks on Gate III

**Attack III.1: arbitrary stochastic kernels.**

One can always fit a kernel `Pr(Y|O)` by hand.  It is rejected unless it is the
projection of a projectively consistent `h_B`.

**Attack III.2: hidden whole universe.**

The cylinder `\Gamma_B` is not the whole universe.  It is the compatible
bounded-history object for the experiment/region.  If outside data changes the
prediction, it must appear as boundary residue or force a larger `B`.

**Attack III.3: projective defect.**

If `\Pi_{B,k}` does not decay, the family of finite weights is not a stable
bounded-history law.  Effective probabilities may still be fitted, but they do
not satisfy the ISP alignment gate.

**Attack III.4: complex or signed weights.**

The current closure packet uses positive `h_B` after commitment.  A future
amplitude-level theory may introduce phases, but it must project to positive
bounded-history weights for committed records.  Otherwise the present
probability formula is not licensed.

Gate III passes only when probability is demonstrably the normalized
projection of a deterministic bounded-history weight.

### 20.4 Combined Alignment Rule

For a target `Y_B`, define:

$$
\boxed{
\mathcal E^{ISP}_B(k,\lambda,O)
=
\sum_{j=k}^{\infty}\Delta^Y_{B,j}
+
\mathcal E^{atlas}_{B,\lambda}
+
\sum_{j=k}^{\infty}\Pi_{B,j}.
}
$$

The Barandes/ISP alignment criterion is:

$$
\boxed{
\mathcal E^{ISP}_B(k,\lambda,O)\le\epsilon_{ISP}.
}
$$

This says:

1. the panel has enough bounded history;
2. the atlas is record-intrinsic and non-reconstructive;
3. the effective probabilities come from projection of `h_B`, not from a
   primitive Markov transition.

The joint spacetime closure theorem should therefore use:

$$
\mathcal E^{click}_B
+
\mathcal E^{GR,cl}_B
+
\mathcal E^{ISP}_B
\le
\epsilon.
$$

All three closure families must pass their own tolerances; the displayed
single bound is only the compressed joint form.

### 20.5 Campaign Conclusion

The alignment campaign does not derive `h_B` or prove physical closure.

It does prove the correct test architecture:

$$
\boxed{
\text{no Markov shortcut, no raw atlas, no primitive stochastic kernel.}
}
$$

If one of the three gates fails, the correct conclusion is:

$$
\boxed{
\text{the chosen bounded panel does not close at this tolerance.}
}
$$

not:

$$
\boxed{
\text{invent a stochastic transition law.}
}
$$

## 21. Conditional Spacetime Closure Theorem

Assume:

1. the finite atlas theorem applies to the bounded candidate class, and the
   nonlookup admissible cover class is nonempty at the tolerance in question;
2. same-actual equivalence is generated by zero boundary-work residue;
3. transport minimizer sets are finite or compact in the packet topology;
4. source typing is generated by stable no-silent click sectors;
5. environment-conditioned null laws calibrate `\mathcal M_B^{cl}`;
6. closure scaling bounds hold for the environment class;
7. the Barandes/ISP alignment error `\mathcal E^{ISP}_B` is below tolerance for
   the target readout.

Then:

$$
\boxed{
\mathcal E^{GR,cl}_B(k,O)\le\epsilon_{GR}
}
$$

is a record-intrinsic, non-reconstructive spacetime closure condition.

Moreover, if the click closure condition also holds:

$$
\mathcal E^{click}_B(k,O)\le\epsilon_{click},
$$

then `B` is a spacetime-like experimental diamond at tolerances
`(\epsilon_click,\epsilon_GR)`.

**Proof.**

Under assumptions 1-4, `I_GR^{cl}` is record-intrinsic and non-silent.  Under
Theorem 2, `d_GR^{cl}` is a record-covariant packet pseudometric.  Under
Theorem 3, `\mathcal M_B^{cl}` is a defect functional rather than a manifold
assumption, and assumption 5 supplies its local null calibration.  Under
Theorem 4, the GR history tail is controlled by `\Delta^{GR}`.  The three
terms in `\mathcal E^{GR,cl}` therefore exactly bound packet spread,
manifold/Ward failure, and omitted-history instability.  Assumption 6 prevents
the tolerance-relative boundary from becoming arbitrary.  Assumption 7 ensures
the closure is non-Markovian, record-intrinsic, and projective rather than a
hand-fit stochastic kernel.  Combining with click closure gives the joint
closure definition. `\square`

## 22. Final Status

This paper advances Paper XXXVIII by replacing four placeholders with a
candidate finite closure calculus:

$$
\boxed{
I_{GR}^{cl},\quad
d_{GR}^{cl},\quad
\mathcal M_B^{cl},\quad
\Delta^{GR}.
}
$$

It proves formal covariance/pseudometric/tail-bound statements and makes the
manifoldlikeness assumption explicit as a defect smallness condition rather
than a starting axiom.

It also adds a Barandes/ISP alignment campaign.  The construction is acceptable
only if:

$$
\boxed{
\mathcal E^{ISP}_B
=
\text{history tail}
+
\text{atlas alignment error}
+
\text{projective }h_B\text{ defect}
}
$$

is small at the target tolerance.

It does not yet prove spacetime closure for the physical click law.

The remaining independent theorem targets are:

1. **Nonlookup atlas-cover theorem.**
   Physical click-selected histories admit center-visible atlas covers that
   are not raw reconstruction.  Finite existence and set-valued stability are
   proved in Section 3.1 once such a cover class is nonempty.

2. **Same-actual theorem.**
   Zero boundary-work equivalence is the correct same-actual quotient.

3. **Transport theorem.**
   Boundary-work transport minimizers form a stable finite/set-valued
   transport category.

4. **Source theorem.**
   Ward/Bianchi residues are typed by stable click sectors or charged as
   unresolved.

5. **Environment-null theorem.**
   `\mathcal M_B^{cl,\mathcal K}` has calibrated null laws for flat, curved,
   horizon-like, entangled, and pre-spacetime regimes.

6. **Closure-scaling theorem.**
   The smallest joint boundary grows according to a record-intrinsic scaling
   law:

   $$
   C_B(k_\epsilon,O_\epsilon)
   \le
   F(\epsilon,\mathcal K).
   $$

7. **Projective history-weight theorem.**
   The physical `h_B` is derived from the no-silent boundary-work potential and
   satisfies projective consistency on bounded histories.

These are now concrete.  Further brute-force enumeration is useful only as a
diagnostic for these seven theorems, not as a substitute for them.

## 23. Bottom Line

Spacetime closure is no longer a single undefined symbol.

The current best formulation is:

$$
\boxed{
\text{a bounded record diamond is spacetime-like when its center-visible
atlas, transport, curvature, Ward/source, and refinement packets are stable
under bounded history projection and jointly close with the click boundary.}
}
$$

In plain language:

> spacetime is not assumed; it is the stable, non-reconstructive packet carried
> by the same bounded record histories that make clicks predictable.

And the Barandes/ISP guardrail is:

> probability is allowed only as the projected residual of bounded histories;
> it is not the primitive law of the next click.
