# Relativistic ISP v7 Paper XLI: Eight-Target Closure Campaign

**Status:** analytic campaign note, not peer reviewed, version 2026-06-30.

Paper XL became large because it followed several openings at once.  This
paper restarts from the clean frontier.  The goal is to name the missing
theorems, order them by dependency, and push each target until the remaining
obstruction is explicit.

The current candidate click law is:

$$
\boxed{
h_B(H)
=
\exp[-\mathcal A_B^{hist}(H)]
}
$$

where:

- `B` is a bounded record diamond;
- `H` is a compatible bounded record history inside `B`;
- `h_B(H)` is a positive compatibility weight, not a primitive probability;
- probabilities appear only after projecting the compatible histories onto the
  finite panel actually observed.

The action is:

$$
\boxed{
\mathcal A_B^{hist}
=
\Psi_B^{center}
+
\Lambda_B^{coalgebra}
+
X_B^{typed}
+
P_B^{projective}
+
N_B^{nonlookup}
+
C_B^{commit}.
}
$$

The eight missing targets are:

1. **Center-ledger extraction.**  Derive the center channels, committed masses,
   and scales from record diamonds.
2. **Intrinsic gap.**  Prove positive anchored Hessian/conductance gap for
   physical bounded diamonds.
3. **Subraw closure growth.**  Prove no-silent closure stays below raw
   reconstruction complexity.
4. **Projective compatibility.**  Prove depth changes commute with deletion,
   insertion, and projection.
5. **Projective sufficiency.**  Prove the least panel predicts target clicks
   up to tolerance.
6. **Full action convexity/coercivity.**  Prove the positive history weight is
   selected stably, modulo same-actual quotient and harmless gauges.
7. **Typed source and entanglement residues.**  Derive when long shared
   record structure is bounded, printed, or forces boundary expansion.
8. **Finite spacetime packet licensing.**  Define and stabilize a finite
   record-intrinsic spacetime readout without deriving Newton's constant or
   assuming manifoldlikeness.

These targets are not independent.  The campaign order is:

$$
\boxed{
1\to2\to3\to4\to5\to6\to7\to8.
}
$$

The reason is simple: without the ledger there is no Hessian; without the gap
there is no tail; without the tail there is no nonlookup/sufficiency; without
projectivity the same experiment has different laws at different depths;
without convexity there is no stable `h_B`; without typed residues long
entanglement is either hidden or mishandled; without packet licensing the
spacetime claim overreaches.

## 1. Target 1: Center-Ledger Extraction

### 1.1 Object To Derive

The center ledger is:

$$
\boxed{
\mathscr L_B
=
(\mathfrak C_B,\mu_B,\omega_B).
}
$$

Here:

- `\mathfrak C_B` is the finite set of no-silent center channels;
- `\mu_B(\alpha)=\mu_\alpha` is the committed mass in channel `\alpha`;
- `\omega_B(\alpha)=\omega_\alpha` is the scale or precision assigned to that
  channel.

The center-work term is:

$$
\boxed{
\Psi_B^{center}(h)
=
\sum_{\alpha\in\mathfrak C_B}
\omega_\alpha
\left[
\mu_\alpha\log\frac{\mu_\alpha}{\widehat\mu_\alpha(h)}
-
\mu_\alpha
+
\widehat\mu_\alpha(h)
\right]
+
\kappa U_B(h).
}
$$

The risk is that `\mathfrak C_B`, `\mu_B`, and `\omega_B` are chosen by hand.
The law needs them from the diamond itself.

### 1.2 Diamond Interfaces

Let a bounded record diamond be:

$$
\boxed{
D_B=(R_B,\le_B,\partial^-B,\partial^+B,\mathcal I_B,\mathcal U_B).
}
$$

where:

- `R_B` is the finite record set;
- `\le_B` is the causal/order relation;
- `\partial^-B,\partial^+B` are lower and upper boundary records;
- `\mathcal I_B` maps boundary pairs to interval interiors;
- `\mathcal U_B` records deletion, insertion, refinement, and overlap
  updates.

The primitive interfaces are:

$$
\boxed{
\partial,\quad I,\quad U,\quad O.
}
$$

They mean boundary membership, interval incidence, update response, and overlap
identification.

### 1.3 Extraction Rule

For each elementary update `e` and compatible history `H`, define the response
vector:

$$
\boxed{
\delta(H,e)
=
\left(
\delta_\partial(H,e),
\delta_I(H,e),
\delta_U(H,e),
\delta_O(H,e)
\right).
}
$$

Two pairs `(H,e)` and `(H',e')` define the same center channel when their
response vectors agree after same-actual quotienting:

$$
\boxed{
(H,e)\sim_B(H',e')
\quad\Longleftrightarrow\quad
\delta(H,e)=\delta(H',e')
\text{ modulo same-actual zero residue.}
}
$$

Then:

$$
\boxed{
\mathfrak C_B
=
\{[(H,e)]_B:\delta(H,e)\ne0\}.
}
$$

The committed mass is:

$$
\boxed{
\mu_\alpha
=
\sum_{(H,e)\in\alpha}
a(H,e)m(H,e),
}
$$

where `a(H,e)` is the admissibility indicator and `m(H,e)` is the elementary
record mass/cost assigned by the update calculus.

The scale is:

$$
\boxed{
\omega_\alpha
=
\epsilon_\alpha^{-2},
}
$$

where `\epsilon_\alpha` is the smallest tolerated response uncertainty for
channel `\alpha`.

### 1.4 Theorem 1: Ledger Extraction

If bounded record diamonds have exactly the primitive interfaces
`(\partial,I,U,O)`, and if same-actual zero residue is the only quotient, then
the construction above gives the minimal no-silent center ledger.

**Proof Sketch.**

Every finite record-intrinsic query of `D_B` factors through boundary,
interval, update, or overlap data.  A nonzero response at any of these
interfaces must be printed, otherwise a perturbation can change the bounded
history without changing the ledger.  Quotienting same-actual zero residue
removes presentation artifacts but not physical response.  The equivalence
classes of nonzero response vectors are therefore exactly the minimal
no-silent channels. `\square`

### 1.5 Hostile Review and Follow-Up

**Objection:** the primitive-interface claim may hide a fifth interface.

**Follow-up.**  A fifth interface must be one of:

1. a new observable on records;
2. a new observable on order relations;
3. a new observable on updates;
4. a new observable on overlaps;
5. a hidden presentation field.

The first four refine `\partial,I,U,O`.  The fifth is inadmissible.  Therefore
the only honest opening is to prove a representation theorem for the chosen
record language.  That theorem is now part of Target 1.

## 2. Target 2: Intrinsic Gap

### 2.1 Object To Prove

The intrinsic gap is:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

Here `\lambda` is the tolerance scale defining which response is relevant to
the experiment.  The gap says every unresolved nonzero response leaks to the
printed boundary/source panel with positive cost.

### 2.2 Hessian Form

Let:

$$
\boxed{
\widehat\mu(h)=Ah
}
$$

where `A_{\alpha H}` is the center-channel incidence of history `H` in channel
`\alpha`.

The Hessian of center work is:

$$
\boxed{
\mathcal H_B(h)
=
A^\ast D_B(h)A+\kappa\mathcal H_{U,B}(h)
}
$$

with:

$$
\boxed{
D_B(h)_{\alpha\alpha}
=
\omega_\alpha
\frac{\mu_\alpha}{\widehat\mu_\alpha(h)^2}.
}
$$

The intrinsic gap is:

$$
\boxed{
\gamma_{B,\lambda}
=
\lambda_{\min}^+(\mathcal H_B)
}
$$

after same-actual quotienting and boundary/source anchoring.

### 2.3 Conductance Form

Equivalently, define the no-silent dependency hypergraph:

$$
\boxed{
\mathcal D_{B,\lambda}
=
(\mathcal A_{B,\lambda},\mathcal E_{B,\lambda})
}
$$

with interface atoms `\mathcal A` and dependency hyperedges `\mathcal E`.

For any unresolved atom set `S`, define:

$$
\boxed{
\Phi(S)
=
\frac{
c(\partial_{\mathcal D}S)+q(S\cap\mathcal P_{B,\lambda})
}{
m(S)
}.
}
$$

Here:

- `c(\partial_{\mathcal D}S)` is the coupling mass crossing from `S` to its
  complement;
- `q(S\cap\mathcal P)` is the anchoring mass touching printed atoms;
- `m(S)` is committed response mass in `S`.

The anchored conductance is:

$$
\boxed{
\Phi_{B,\lambda}
=
\inf_{S\ne\emptyset}\Phi(S).
}
$$

### 2.4 Theorem 2: Intrinsic Gap Equivalence

Assume finite degree and bounded hyperedge size.  Then:

$$
\boxed{
\Phi_{B,\lambda}>0
\quad\Longrightarrow\quad
\gamma_{B,\lambda}>0
\quad\Longrightarrow\quad
\theta_{B,\lambda}<1.
}
$$

The final term `\theta_{B,\lambda}<1` means unresolved response contracts
under no-silent closure.

**Proof Sketch.**

The finite Cheeger bound gives:

$$
\gamma_{B,\lambda}
\ge
\frac{\Phi_{B,\lambda}^2}{2\Delta}.
$$

The Hessian gap then contracts the closure relaxation:

$$
\theta_{B,\lambda}
\le
1-\tau\gamma_{B,\lambda}.
$$

Since `\tau>0`, positive conductance implies positive gap and positive gap
implies contraction. `\square`

### 2.5 Hostile Review and Follow-Up

**Objection:** this proves a condition, not the physical gap.

**Follow-up.**  Correct.  The physical theorem is now:

$$
\boxed{
\text{physical bounded diamonds have }\Phi_{B,\lambda}>0
\text{ after the correct source boundary is printed.}
}
$$

If `\Phi` vanishes, the boundary missed a hidden island.  The law then expands
`B` until the island is either printed as a typed source sector or the regime
is declared unclosed at tolerance `\lambda`.

## 3. Target 3: Subraw Closure Growth

### 3.1 Object To Prove

No-silent closure must not reconstruct the raw hidden history.

Let:

$$
\boxed{
C(\mathfrak O^\dagger_{B,\lambda})
}
$$

be the complexity of the least no-silent panel, and let:

$$
\boxed{
C_{\rm raw}(B)
}
$$

be the cost of raw history/order reconstruction.

The target is:

$$
\boxed{
C(\mathfrak O^\dagger_{B,\lambda})
=
o(C_{\rm raw}(B)).
}
$$

### 3.2 Tail Radius

If unresolved response contracts with `\theta<1`, then the radius needed for
tolerance `\epsilon` is:

$$
\boxed{
R_{B,\lambda}(\epsilon)
\le
\left\lceil
\frac{\log(C_{B,\lambda}/\epsilon)}
-\log\theta_{B,\lambda}}
\right\rceil.
}
$$

Suppose boundary-growth obeys:

$$
\boxed{
|\{a:d_{\mathcal D}(a,\mathcal S)\le r\}|
\le
C_0|\partial_\lambda B|(1+r)^d e^{\sigma r}.
}
$$

Then:

$$
\boxed{
C(\mathfrak O^\dagger_{B,\lambda})
\le
C_0|\partial_\lambda B|(1+R)^d e^{\sigma R}.
}
$$

### 3.3 Theorem 3: Subraw Closure

If:

$$
\boxed{
|\partial_\lambda B|
(\log |B|)^d
|B|^{c\sigma}
=
o(C_{\rm raw}(B)),
}
$$

then the least no-silent panel is nonreconstructive.

**Proof Sketch.**

Use `R=O(\log |B|)` from contraction and substitute into the boundary-growth
envelope.  The displayed inequality is exactly the subraw condition. `\square`

### 3.4 Hostile Review and Follow-Up

**Objection:** near black holes, dense matter, or long entanglement, the
boundary may grow too fast.

**Follow-up.**  That is a feature.  The law is tolerance-relative:

$$
\boxed{
B_{\lambda,\epsilon}
=
\min\{B':\Phi_{B',\lambda}\ge\phi_0,\ 
C(\mathfrak O^\dagger_{B',\lambda})<C_{\rm raw}(B')\}.
}
$$

The bounded region is not a metric ball.  It is the smallest record diamond
that closes response below tolerance before becoming reconstructive.

## 4. Target 4: Projective Compatibility

### 4.1 Object To Prove

Let `k` be history depth.  Let:

$$
\boxed{
\pi_{k+1\to k}:H_{B,k+1}\to H_{B,k}
}
$$

forget the oldest layer of a compatible bounded history.

Projective compatibility requires:

$$
\boxed{
(\pi_{k+1\to k})_\# h_{B,k+1}
\propto
h_{B,k}.
}
$$

This says the shorter-depth law is the projection of the longer-depth law.

### 4.2 Coalgebra Ward Identity

The deletion/insertion flux is:

$$
\boxed{
\mathcal W_{B,k}
=
\mu_{B,k}
-
(\pi_{k+1\to k})_\#\mu_{B,k+1}.
}
$$

The projective penalty is:

$$
\boxed{
P_B^{projective}
=
\sum_k
\|\mathcal W_{B,k}\|_{\omega,k}^2.
}
$$

### 4.3 Theorem 4: Ward-Projectivity Equivalence

Assume center ledgers are extracted functorially under deletion and insertion.
Then:

$$
\boxed{
\mathcal W_{B,k}=0\ \forall k
\quad\Longleftrightarrow\quad
(\pi_{k+1\to k})_\# h_{B,k+1}\propto h_{B,k}.
}
$$

**Proof Sketch.**

The center ledger is a linear image of the history weight.  If pushed-forward
ledgers agree at every depth and the no-silent response class separates
nonzero projected residues, then pushed-forward weights agree on the
admissible quotient.  Conversely, projected weights imply projected ledgers.
`\square`

### 4.4 Hostile Review and Follow-Up

**Objection:** anomalies or typed source sectors can break exact projectivity.

**Follow-up.**  Then exact projectivity is replaced by typed projectivity:

$$
\boxed{
\mathcal W_{B,k}
=
\mathcal S^{typed}_{B,k}
+
\mathcal R^{untyped}_{B,k},
\qquad
\mathcal R^{untyped}_{B,k}=0.
}
$$

Licensed source flux may remain, but untyped projective residue is forbidden.

## 5. Target 5: Projective Sufficiency

### 5.1 Object To Prove

For a target click/readout `Y`, define the panel:

$$
\boxed{
\mathcal P_{B,k,\lambda}
=
\sigma(\mathfrak O^\dagger_{B,\lambda}\text{ on }H_{B,k}).
}
$$

For a panel cell `p`, define:

$$
\boxed{
\operatorname{diam}_Y(p)
=
\sup_{H,H'\in p}
d_Y(Y(H),Y(H')).
}
$$

The sufficiency target is:

$$
\boxed{
\sup_{p\in\mathcal P_{B,k,\lambda}}
\operatorname{diam}_Y(p)
\le
\epsilon_Y.
}
$$

This is deterministic.  Probability comes later.

### 5.2 Tail Bound

If all unprinted changes telescope through unresolved response, then:

$$
\boxed{
d_Y(Y(H),Y(H'))
\le
L_Y\sum_{r\ge R}\|v_r(H,H')\|.
}
$$

Using contraction:

$$
\boxed{
\operatorname{diam}_Y(\mathcal P_{B,k,\lambda})
\le
\frac{L_YC_{B,\lambda}\theta^R}{1-\theta}.
}
$$

### 5.3 Theorem 5: Tail Sufficiency

If the no-silent response tail contracts and `Y` is Lipschitz in that tail,
then a finite closure radius gives projective sufficiency.

**Proof Sketch.**

Two histories in the same panel agree on printed response through radius `R`.
Their difference is therefore entirely in the unresolved tail.  The Lipschitz
bound and geometric tail estimate give the displayed diameter bound.
`\square`

### 5.4 Hostile Review and Follow-Up

**Objection:** sufficiency is target-dependent.

**Follow-up.**  Correct.  The law should not claim one panel predicts every
possible future statement.  It predicts an admissible family:

$$
\boxed{
\mathcal Y_B
=
\{Y:\ L_Y<\infty\text{ on the no-silent response norm}\}.
}
$$

For targets outside `\mathcal Y_B`, either expand the panel or do not claim a
prediction.

## 6. Target 6: Full Action Convexity and Coercivity

### 6.1 Object To Prove

The action must select stable positive weights:

$$
\boxed{
h_B
=
\operatorname*{argmin}_{h>0,\ \sum h=1}
\mathcal F_B(h).
}
$$

where:

$$
\boxed{
\mathcal F_B
=
\Psi_B^{center}
+
\Lambda_B^{coalgebra}
+
X_B^{typed}
+
P_B^{projective}
+
N_B^{nonlookup}
+
C_B^{commit}.
}
$$

### 6.2 Convex Core

The RN/KL center work is convex in `Ah`.  The coalgebra and projective terms
are quadratic in pushed-forward ledgers.  The commitment term is a barrier:

$$
\boxed{
C_B^{commit}(h)
=
-\tau\sum_H\log h(H)
}
$$

on the admissible finite quotient.

### 6.3 Theorem 6: Stable Positive Weight

If:

1. the center incidence map separates no-silent quotient directions;
2. typed source terms are convex after source labels are printed;
3. the nonlookup penalty excludes raw-reconstructive panels;
4. same-actual zero modes are quotiented;
5. the barrier is finite only for positive weights;

then `\mathcal F_B` is coercive and strictly convex on the admissible quotient,
and `h_B` exists uniquely modulo harmless gauge normalization.

**Proof Sketch.**

Finite-dimensional lower semicontinuity and the barrier give existence in the
positive simplex.  Strict convexity on separated no-silent directions gives
uniqueness on the quotient.  Coercivity follows because escape to a silent or
raw direction is either quotiented, penalized, or hits the barrier. `\square`

### 6.4 Hostile Review and Follow-Up

**Objection:** typed source residues may be nonconvex or multi-sector.

**Follow-up.**  Then the correct object is not necessarily one minimizer but a
projectively stable minimizer face:

$$
\boxed{
\mathcal M_B^{min}
=
\operatorname*{Argmin}\mathcal F_B.
}
$$

The prediction is still unique if the projected diameter of this face is
small:

$$
\boxed{
\operatorname{diam}_Y(\mathcal M_B^{min})
\le
\epsilon_Y.
}
$$

Thus uniqueness of `h_B` is sufficient, not always necessary.

## 7. Target 7: Typed Source and Entanglement Residue Law

### 7.1 Object To Derive

Long-range entanglement and source structure must not be hidden outside the
records.  It enters as typed response:

$$
\boxed{
X_B^{typed}
=
\sum_{\tau\in\mathcal T_B}
\xi_\tau\|R_\tau(H)\|^2.
}
$$

Here:

- `\mathcal T_B` is the finite set of licensed source/entanglement types;
- `R_\tau(H)` is the typed response residue;
- `\xi_\tau` is the cost scale for that type.

### 7.2 Source Printing Rule

A source sector is admissible if:

$$
\boxed{
m_\tau(B)<\infty,
\qquad
\theta_\tau(B)<1,
\qquad
C_\tau(B)<C_{\rm raw}(B).
}
$$

That means finite mass, contracting unresolved response, and nonraw panel
complexity.

If any fail, the boundary must expand or the regime is not closed.

### 7.3 Theorem 7: Typed Residue Admission

An entanglement/source sector is admissible exactly when it can be printed as a
finite no-silent source label whose residual response contracts below
tolerance without raw reconstruction.

**Proof Sketch.**

If the sector is printed and the residual contracts, it becomes part of the
bounded panel and contributes a finite typed cost.  If it is not printed, it is
an untyped no-silent residue and violates sufficiency.  If printing it is raw,
the boundary is not an admissible local law. `\square`

### 7.4 Hostile Review and Follow-Up

**Objection:** this makes locality non-spatial.

**Follow-up.**  Yes.  Locality here is record-boundedness, not metric
nearness.  Two spatially distant records can share a typed source sector if
the diamond prints the shared information needed for prediction.  Emergent
spacetime locality is a later readout, not the primitive boundary rule.

## 8. Target 8: Finite Spacetime Packet Licensing

### 8.1 Not Newton's Constant

To avoid the overloaded symbol `G`, this paper writes the finite spacetime
packet as:

$$
\boxed{
\mathcal G_B(H).
}
$$

This is not Newton's constant and not a full continuum metric.  It is a finite
record-intrinsic readout.

### 8.2 Packet Definition

Let:

$$
\boxed{
\mathcal G_B(H)
=
\left(
d_B,V_B,\ell_B,\mathcal R_B,\mathcal B_B,\mathcal T_B,\mathcal M_B
\right).
}
$$

where:

- `d_B` is dimension/profile readout;
- `V_B` is volume/count profile;
- `\ell_B` is causal distance proxy;
- `\mathcal R_B` is curvature/work residue;
- `\mathcal B_B` is Ward/Bianchi residue;
- `\mathcal T_B` is typed source residue;
- `\mathcal M_B` is manifoldlikeness/atlas defect.

The packet is licensed only if denominators and profile masses have a
regularity floor:

$$
\boxed{
\rho_B\ge\rho_0(\lambda)>0.
}
$$

### 8.3 Stability Criterion

The finite spacetime error is:

$$
\boxed{
\mathcal E_B^{ST}
=
\operatorname{diam}_{ST}(\mathcal P_{B,k,\lambda})
+
\mathcal M_B+\mathcal B_B+\mathcal R_B.
}
$$

The regime is spacetime-like when:

$$
\boxed{
\mathcal E_B^{ST}\le\epsilon_{ST}.
}
$$

### 8.4 Theorem 8: Packet Licensing

If the bounded click panel is sufficient, the spacetime packet is built from
finite center-ledger functionals and regularized ratios, and
`\mathcal E_B^{ST}\le\epsilon_{ST}`, then the same bounded history law licenses
a stable finite spacetime readout.

If click sufficiency holds but `\mathcal E_B^{ST}` fails, the regime is
pre-spacetime click-predictive.

**Proof Sketch.**

The packet components are finite functions of printed ledgers and typed
residues.  The regularity floor gives Lipschitz stability.  The same tail
bound that controls click predictions controls packet diameter.  The defect
terms determine whether the packet is spacetime-like. `\square`

### 8.5 Hostile Review and Follow-Up

**Objection:** older no-go theorems said records cannot derive `G`.

**Follow-up.**  The no-go remains.  This packet does not derive Newton's
constant, absolute length, or a full continuum metric.  It computes a finite
readout and licenses a spacetime-like interpretation only when its defects are
small and calibration gates pass.

## 9. Integrated Conditional Theorem

#### Theorem 9: Eight-Target Conditional Click Law

Assume Targets 1--8 hold for a bounded diamond `B` at tolerance `\lambda`.
Then:

1. there is a least no-silent nonraw response panel
   `\mathcal P_{B,k,\lambda}`;
2. there is a positive bounded-history weight:

   $$
   \boxed{
   h_B(H)=\exp[-\mathcal A_B^{hist}(H)];
   }
   $$

3. projected probabilities are:

   $$
   \boxed{
   \Pr_B(Y=y\mid p)
   =
   \frac{\sum_{H\in p,\ Y(H)=y}h_B(H)}
   {\sum_{H\in p}h_B(H)};
   }
   $$

4. the prediction is deterministic up to tolerance before it is probabilistic:

   $$
   \boxed{
   \operatorname{diam}_Y(p)\le\epsilon_Y;
   }
   $$

5. finite spacetime appears only if the same panel also satisfies:

   $$
   \boxed{
   \mathcal E_B^{ST}\le\epsilon_{ST}.
   }
   $$

**Proof Sketch.**

Target 1 supplies the ledger.  Target 2 supplies contraction.  Target 3 keeps
the panel nonreconstructive.  Target 4 makes the law projective in history
depth.  Target 5 gives deterministic sufficiency.  Target 6 selects stable
positive weights.  Target 7 handles nonlocal shared source sectors without
hiding them.  Target 8 licenses finite spacetime only as an output.  Combining
these gives the displayed probability by projection. `\square`

## 10. Final Hostile Review

### Review A: "This still has many assumptions."

Accepted.

The point of Paper XLI is not to pretend the law is proven.  It converts the
frontier into eight named finite theorem targets with dependencies.

### Review B: "The intrinsic gap is still the hardest."

Accepted.

It remains the key physical theorem.  But it is now tied to the Hessian and
conductance of the extracted center ledger, not to a vague stochastic
mixing assumption.

### Review C: "Projective compatibility may fail in anomalous sectors."

Accepted.

Then anomalous flux must be typed.  Untyped projective residue is forbidden;
typed projective residue is a source sector.

### Review D: "The packet licensing may sneak manifoldlikeness back in."

Rejected in construction, accepted in calibration.

The panel and packet can be computed without assuming manifoldlikeness.
Calling the packet spacetime-like requires the manifold/Ward/curvature defects
to be small.

### Review E: "Probability is still not fundamental here."

Accepted.

The fundamental statement is the compatibility of bounded histories.  The
probability is the normalized projection after the panel discards unresolved
history.

## 11. Campaign Result

The eight-target frontier has a clean spine:

$$
\boxed{
\mathscr L_B
\Rightarrow
\gamma_{B,\lambda}>0
\Rightarrow
\text{subraw closure}
\Rightarrow
\text{projective panel}
\Rightarrow
\text{sufficient predictions}
\Rightarrow
h_B
\Rightarrow
\text{typed source handling}
\Rightarrow
\mathcal G_B\text{ licensing}.
}
$$

The most compressed current rule is:

$$
\boxed{
\text{the click law is the positive boundary-work history weight on the least
projectively compatible, no-silent, subraw diamond panel sufficient for the
requested target.}
}
$$

The next mathematical attack should not be another broad campaign.  The rest
of this paper now executes the first dependency chain:

$$
\boxed{
\text{ledger extraction}
\Rightarrow
\text{positive anchored conductance}
\Rightarrow
\text{subraw closure}
}
$$

because every downstream theorem needs that spine.

## 12. First Dependency Chain Campaign

The first dependency chain is:

$$
\boxed{
\mathscr L_B
\Rightarrow
\Phi_{B,\lambda}>0
\Rightarrow
\gamma_{B,\lambda}>0
\Rightarrow
\theta_{B,\lambda}<1
\Rightarrow
\text{subraw closure}.
}
$$

Target 1 gives `\mathscr L_B`.  Target 2 needs positive conductance.  Target 3
needs the resulting contraction to stay below raw reconstruction.

The enemy is a hidden zero-conductance island: a set of unresolved response
atoms that can change without leaking to the printed panel.

### 12.1 Zero-Conductance Set

Let `S\subset\mathcal A_{B,\lambda}` be unresolved.  It is silent if:

$$
\boxed{
c(\partial_{\mathcal D}S)=0
\quad\text{and}\quad
q(S\cap\mathcal P_{B,\lambda})=0.
}
$$

Equivalently:

$$
\boxed{
\Phi(S)=0.
}
$$

Such an `S` kills the intrinsic gap.

### 12.2 Zero-Conductance Dichotomy

The ledger extraction theorem implies every zero-conductance set must be one
of two types:

1. **Same-actual null island.**  The apparent variation is presentation-only
   and should be quotiented.
2. **Unprinted source island.**  The variation is physical but the boundary did
   not print the records that carry it.

There is no third admissible possibility.  A physical variation that is neither
quotiented nor printed violates no-silentness.

#### Theorem 10: Zero-Conductance Dichotomy

Assume the primitive-interface representation theorem and minimal no-silent
ledger extraction.  If `S` is unresolved and `\Phi(S)=0`, then either:

$$
\boxed{
S\subset\ker(\sim_{\rm same\ actual})
}
$$

or `S` defines an unprinted typed source sector.

**Proof Sketch.**

If `S` is not same-actual null, it contains a nonzero response at boundary,
interval, update, or overlap interface.  Minimal no-silent extraction would
create a center channel for that response.  If the channel has no boundary
leak and no anchor, then the source records needed to print it were excluded
from `B`.  Thus it is an unprinted source sector. `\square`

### 12.3 Boundary-Source Completion

Define a completion operator:

$$
\boxed{
\mathcal C_\lambda(B)
=
B
\cup
\{\text{minimal records needed to print every non-null }S
\text{ with }\Phi(S)=0\}.
}
$$

Iterate:

$$
\boxed{
B^{(n+1)}
=
\mathcal C_\lambda(B^{(n)}).
}
$$

The completed boundary is:

$$
\boxed{
B^\star_{\lambda}
=
\operatorname{lfp}(\mathcal C_\lambda;B).
}
$$

If the fixed point exists and is subraw, then all zero-conductance physical
islands have been printed.

### 12.4 Theorem 11: Completed Boundary Conductance

Assume:

1. zero-conductance dichotomy holds;
2. same-actual null islands are quotiented;
3. boundary-source completion reaches a fixed point `B^\star_\lambda`;
4. completion does not cross raw reconstruction:

   $$
   \boxed{
   C(\mathfrak O^\dagger_{B^\star,\lambda})
   =
   o(C_{\rm raw}(B^\star)).
   }
   $$

Then:

$$
\boxed{
\Phi_{B^\star,\lambda}>0.
}
$$

**Proof Sketch.**

If conductance were zero after completion, Theorem 10 says the zero set is
same-actual null or an unprinted source island.  Same-actual null sets have
been quotiented.  Unprinted source islands are exactly what completion adds.
Contradiction. `\square`

### 12.5 Consequence

The intrinsic gap is proven for completed subraw boundaries:

$$
\boxed{
B^\star_\lambda\text{ exists and is subraw}
\quad\Longrightarrow\quad
\gamma_{B^\star,\lambda}>0.
}
$$

This is not a universal proof for every proposed boundary.  It is a constructive
criterion for when a boundary is physically closed.

## 13. Subraw Completion Campaign

The remaining opening is whether completion stays subraw.

### 13.1 Completion Growth

Let:

$$
\boxed{
b_n=|\partial_\lambda B^{(n)}|,
\qquad
s_n=\text{number of newly printed source sectors at step }n.
}
$$

Assume:

$$
\boxed{
b_{n+1}
\le
b_n+A s_n b_n^\alpha,
\qquad
s_{n+1}
\le
\rho s_n,
\qquad
0\le\rho<1.
}
$$

The second inequality says source islands have a contracting hierarchy after
being printed.  This is the source-sector analogue of the unresolved-response
tail.

Then:

$$
\boxed{
\sum_{n\ge0}s_n
\le
\frac{s_0}{1-\rho}.
}
$$

If `\alpha\le1` and `s_0` grows subraw, completion remains subraw.

### 13.2 Theorem 12: Subraw Boundary Completion

Assume:

1. source-sector discovery contracts: `s_{n+1}\le\rho s_n` with `\rho<1`;
2. each source sector adds at most polynomial boundary mass:

   $$
   \boxed{
   b_{n+1}\le b_n+A s_n b_n^\alpha,\quad \alpha\le1;
   }
   $$

3. the initial source defect is subraw:

   $$
   \boxed{
   s_0 b_0^\alpha=o(C_{\rm raw}(B)).
   }
   $$

Then boundary-source completion reaches a subraw fixed point.

**Proof Sketch.**

The source count has a summable geometric tail.  Boundary growth is bounded by
the accumulated source additions times at most linear boundary amplification.
Under the displayed subraw condition, total completion complexity remains
below raw reconstruction. `\square`

### 13.3 Hostile Review and Follow-Up

**Objection:** the source-sector contraction is another gap assumption.

**Follow-up.**  Correct.  It is the same kind of statement as the main
intrinsic gap, but now restricted to typed source islands after they are
printed.  Therefore the physical closure theorem must prove two conductance
conditions:

$$
\boxed{
\Phi^{local}_{B,\lambda}>0,
\qquad
\Phi^{source}_{B,\lambda}>0.
}
$$

The first handles ordinary boundary response.  The second handles long shared
record structure.

## 14. First Chain Result

The first dependency chain is now conditionally proved in the following form:

#### Theorem 13: Completed-Subraw Boundary Gives Intrinsic Gap

If:

1. the center ledger is extracted by primitive-interface no-silent response;
2. zero-conductance sets obey the same-actual/source dichotomy;
3. source completion terminates before raw reconstruction;
4. local and printed-source conductance are positive after completion;

then:

$$
\boxed{
\Phi_{B^\star,\lambda}>0,
\qquad
\gamma_{B^\star,\lambda}>0,
\qquad
\theta_{B^\star,\lambda}<1,
}
$$

and the least no-silent closure is subraw.

This proves the first dependency chain for completed physical boundaries.

### 14.1 What Would Falsify It?

The chain fails if there exists a bounded record diamond with a physical
zero-conductance response island that is:

1. not same-actual null;
2. not printable as a typed source sector;
3. not removable by boundary expansion below raw reconstruction.

Such an object would be a genuine counterexample to the bounded click-law
program at that tolerance.

### 14.2 Next Chain

The next dependency chain is no longer "find the gap."  It is:

$$
\boxed{
\text{completed-subraw gap}
\Rightarrow
\text{projective Ward compatibility}
\Rightarrow
\text{target sufficiency}.
}
$$

The next sections execute that chain.

## 15. Projective Ward Compatibility Campaign

Completed-subraw closure gives a bounded panel at one depth.  A law also needs
the same panel to behave coherently under history-depth changes.

### 15.1 Depth Tower

Let:

$$
\boxed{
H_{B,k}
}
$$

be the compatible bounded histories visible from depth `k`, and let:

$$
\boxed{
\pi_{k+1\to k}:H_{B,k+1}\to H_{B,k}
}
$$

forget the oldest layer.

The center ledger at depth `k` is:

$$
\boxed{
\mathscr L_{B,k}
=(\mathfrak C_{B,k},\mu_{B,k},\omega_{B,k}).
}
$$

The deletion/projection flux is:

$$
\boxed{
\mathcal W_{B,k}
=
\mu_{B,k}
-
(\pi_{k+1\to k})_\#\mu_{B,k+1}.
}
$$

### 15.2 Typed Ward Decomposition

After completed-source printing, flux decomposes as:

$$
\boxed{
\mathcal W_{B,k}
=
\mathcal S^{typed}_{B,k}
+
\mathcal R^{silent}_{B,k}
+
\mathcal R^{untyped}_{B,k}.
}
$$

Admissibility requires:

$$
\boxed{
\mathcal R^{silent}_{B,k}=0
\quad\text{mod same-actual quotient},
\qquad
\mathcal R^{untyped}_{B,k}=0.
}
$$

Typed source flux may remain, but it must be printed in `X_B^{typed}`.

### 15.3 Theorem 14: Completed Ward Projectivity

Assume:

1. the completed boundary has subraw no-silent closure;
2. all zero-conductance physical islands are printed as typed source sectors;
3. untyped Ward flux vanishes at every depth;
4. same-actual silent flux is quotiented.

Then:

$$
\boxed{
(\pi_{k+1\to k})_\# h_{B,k+1}
\propto
h_{B,k}
}
$$

on the admissible quotient.

**Proof Sketch.**

The history weight is determined by center work, typed source work, and
projective penalties.  If pushed ledgers agree after typed flux and same-actual
quotienting, then every no-silent response channel has the same pushed mass at
depth `k`.  Since the response class separates admissible quotient directions,
the pushed weight agrees up to normalization. `\square`

### 15.4 Hostile Review and Follow-Up

**Objection:** exact vanishing of untyped Ward flux may be too strict.

**Follow-up.**  For finite experiments, exact vanishing can be tolerance
vanishing:

$$
\boxed{
\|\mathcal R^{untyped}_{B,k}\|_{\omega}
\le
\epsilon_{proj}.
}
$$

Then projectivity holds up to controlled total-variation error:

$$
\boxed{
d_{TV}\left((\pi_{k+1\to k})_\#\bar h_{B,k+1},\bar h_{B,k}\right)
\le
C_{proj}\epsilon_{proj}.
}
$$

Here `\bar h` is normalized `h`.  Exact projectivity is the zero-tolerance
limit.

## 16. Target Sufficiency After Projectivity

Projectivity controls consistency between depths.  Sufficiency controls whether
the panel predicts the target.

### 16.1 Projective Diameter

For target `Y`, define the worst projected panel diameter:

$$
\boxed{
D_Y(B,k,\lambda)
=
\sup_{j\ge k}
\sup_{p\in\mathcal P_{B,k,\lambda}}
\operatorname{diam}_Y
\left(
\pi_{j\to k}^{-1}(p)
\right).
}
$$

This includes older compatible histories, not only histories exactly at depth
`k`.

### 16.2 Sufficiency From Tail Plus Projectivity

If:

$$
\boxed{
\sum_{r\ge R}\|v_r\|
\le
\frac{C\theta^R}{1-\theta}
}
$$

and projective drift contributes at most:

$$
\boxed{
\sum_{j\ge k}\epsilon_{proj,j}
\le
E_{proj,k},
}
$$

then:

$$
\boxed{
D_Y(B,k,\lambda)
\le
L_Y\frac{C\theta^R}{1-\theta}
+
C_YE_{proj,k}.
}
$$

### 16.3 Theorem 15: Projective Sufficiency

If completed-subraw closure contracts, target `Y` is Lipschitz in unresolved
response, and projective Ward residue has summable tail, then:

$$
\boxed{
D_Y(B,k,\lambda)\le\epsilon_Y
}
$$

for large enough depth `k` and closure radius `R`.

**Proof Sketch.**

Any two full histories compatible with the same panel cell differ by an
unresolved response tail plus accumulated projection drift.  Contraction
controls the first; Ward projectivity controls the second. `\square`

### 16.4 Hostile Review and Follow-Up

**Objection:** a target can be too ambitious.

**Follow-up.**  The admissible target class is:

$$
\boxed{
\mathcal Y_{B,\lambda}
=
\left\{
Y:
L_Y<\infty,\ 
\sum_{j\ge k}\epsilon_{proj,j}<\infty
\right\}.
}
$$

The law predicts targets in `\mathcal Y_{B,\lambda}`.  It does not promise
stable predictions for arbitrary questions.

## 17. Weight Selection After Sufficiency

Once the panel is projective and sufficient, the remaining issue is whether
`h_B` is selected rather than hand-fit.

### 17.1 Quotient Action

Let `\mathcal Q_B` be the finite admissible quotient generated by completed
no-silent closure.  The action descends to:

$$
\boxed{
\mathcal F_B:\Delta(\mathcal Q_B)\to\mathbb R\cup\{\infty\}.
}
$$

The positive weight is:

$$
\boxed{
\bar h_B
=
\operatorname*{argmin}_{q\in\Delta(\mathcal Q_B)}
\mathcal F_B(q).
}
$$

### 17.2 Theorem 16: Weight Is Determined by the Completed Panel

Assume:

1. the completed panel is subraw, projective, and sufficient;
2. `\Psi_B^{center}` is strictly convex on no-silent quotient directions;
3. typed sectors are either convex after printing or have projected diameter
   below tolerance;
4. `C_B^{commit}` prevents zero-weight escape;
5. `N_B^{nonlookup}` excludes raw refinements.

Then the projected predictions are determined by the completed panel.  If the
minimizer is unique, predictions use that minimizer.  If there is a minimizer
face, predictions are unique whenever the target diameter across the face is
below tolerance.

**Proof Sketch.**

The action is finite-dimensional on `\mathcal Q_B`.  Convexity and the
commitment barrier give a stable positive minimizer or minimizer face.
Sufficiency ensures that all histories in a panel cell give the same target
up to tolerance, so residual variation becomes effective probability rather
than hidden dynamics. `\square`

### 17.3 Second Chain Result

The second dependency chain is conditionally proved:

$$
\boxed{
\text{completed-subraw gap}
\Rightarrow
\text{projective Ward compatibility}
\Rightarrow
\text{target sufficiency}
\Rightarrow
\text{stable projected weight}.
}
$$

The remaining unresolved part is not stochastic.  It is the finite positive
weight on the residual histories compatible with the panel.

## 18. Interim Paper XLI Status

Paper XLI has now followed both live chains:

1. ledger extraction to intrinsic gap to subraw closure;
2. subraw closure to projective compatibility to sufficiency to weight
   selection.

The only targets not expanded into full subchains here are:

- typed source sector classification beyond the admission criterion;
- finite spacetime packet calibration beyond packet licensing.

These are downstream of the two chains above.  They do not change the click
law's core structure; they determine which nonlocal source sectors and which
spacetime readouts the core law licenses.

The compact final statement is:

$$
\boxed{
\text{a physical bounded click law exists when the completed no-silent diamond
panel is subraw, projective, sufficient for the target, and selected by convex
boundary work.}
}
$$

The exact remaining proof obligation is:

$$
\boxed{
\text{prove physical bounded diamonds satisfy the zero-conductance dichotomy
and subraw source-completion bounds.}
}
$$

## 19. Why the Theorem Is False for Arbitrary Diamonds

Before proving the physical version, remove a possible confusion.  The theorem
is false for arbitrary finite ordered sets.

### 19.1 Counterexample: A Silent Detached Island

Take a bounded diamond `B` and add a disjoint finite subdiamond `Z` with no
boundary, interval, update, or overlap response crossing from `Z` to `B`.
Let:

$$
\boxed{
D'=D_B\sqcup Z.
}
$$

In the dependency hypergraph, the atoms of `Z` form a set:

$$
\boxed{
S_Z\subset\mathcal A_{D',\lambda}
}
$$

with:

$$
\boxed{
c(\partial_{\mathcal D}S_Z)=0,
\qquad
q(S_Z\cap\mathcal P_{D',\lambda})=0.
}
$$

Thus:

$$
\boxed{
\Phi(S_Z)=0.
}
$$

If `Z` is not same-actual null and is not declared a typed source sector, the
zero-conductance dichotomy fails.

### 19.2 Consequence

No purely order-theoretic theorem can say every finite diamond has positive
conductance.  Physical bounded diamonds need an extra admissibility condition:
no physical response island may remain detached from the printed boundary.

So the target is not:

$$
\boxed{
\text{all finite diamonds have the dichotomy.}
}
$$

The target is:

$$
\boxed{
\text{diamonds admitted by the record law have the dichotomy, because every
non-null detached island must be printable as a source sector or excluded.}
}
$$

## 20. Physical Bounded Diamond Definition

A bounded diamond is **physical at tolerance** `\lambda` for target class
`\mathcal Y` if it satisfies the following finite record-intrinsic conditions.

### 20.1 P1: Primitive-Interface Completeness

Every admissible finite response query factors through:

$$
\boxed{
\partial,\quad I,\quad U,\quad O.
}
$$

These are boundary, interval, update, and overlap interfaces.

### 20.2 P2: No-Silent Source Carrier

For every non-same-actual perturbation with zero boundary conductance, there is
a minimal finite carrier:

$$
\boxed{
\operatorname{car}(S)
\subset R_{B'}
}
$$

in some boundary extension `B'\supseteq B`, such that printing
`\operatorname{car}(S)` turns the perturbation into a typed source response.

In symbols:

$$
\boxed{
\Phi_B(S)=0,\quad S\not\subset\ker(\sim_{\rm same\ actual})
\quad\Longrightarrow\quad
\exists\tau:\ S\mapsto R_\tau
\text{ after finite carrier completion.}
}
$$

### 20.3 P3: Finite Carrier Cost

Every source carrier has finite cost:

$$
\boxed{
0<c(\operatorname{car}(S))<\infty.
}
$$

### 20.4 P4: Subcritical Source Reproduction

Let `M_\lambda` be the nonnegative carrier-reproduction matrix:

$$
\boxed{
(M_\lambda)_{\tau\sigma}
=
\text{maximal normalized amount of new type }\sigma
\text{ exposed by printing type }\tau.
}
$$

Physical boundedness requires:

$$
\boxed{
\rho(M_\lambda)<1.
}
$$

This is not probability.  It is a finite domination statement: source
completion has a contracting dependency tree.

### 20.5 P5: Boundary Cost Is Subraw

Let `r_0` be the initial vector of unprinted source residues and `c` the vector
of carrier costs.  The total completion cost must obey:

$$
\boxed{
\mathbf 1^\top (I-M_\lambda)^{-1}\operatorname{diag}(c)r_0
=
o(C_{\rm raw}(B)).
}
$$

This prevents "completion" from becoming raw reconstruction.

### 20.6 P6: Target Regularity

The requested targets have finite response Lipschitz constants:

$$
\boxed{
Y\in\mathcal Y_{B,\lambda}.
}
$$

Targets outside this class require a larger panel or no prediction claim.

## 21. Zero-Conductance Dichotomy for Physical Diamonds

### 21.1 Theorem 17: Physical Zero-Conductance Dichotomy

If `B` is physical at tolerance `\lambda`, then every zero-conductance
unresolved response set `S` satisfies exactly one of:

1. `S` is same-actual null;
2. `S` is a printable typed source sector.

Equivalently:

$$
\boxed{
\Phi_B(S)=0
\quad\Longrightarrow\quad
S\subset\ker(\sim_{\rm same\ actual})
\ \text{or}\
S\in\mathcal T_B^{source}.
}
$$

**Proof.**

Let `S` be a zero-conductance unresolved response set.

If `S` is same-actual null, it falls under case 1.

If not, P2 applies: every non-same-actual zero-conductance perturbation has a
finite source carrier in a boundary extension.  Printing that carrier turns
the perturbation into a typed source response.  Therefore `S` is a printable
typed source sector, case 2. `\square`

### 21.2 Why This Is Not Circular

The theorem does not define physicality by "positive conductance."  It defines
physicality by the weaker carrier condition:

$$
\boxed{
\text{detached physical response must have a finite printable carrier.}
}
$$

Positive conductance appears only after those carriers are printed or null
islands are quotiented.

## 22. Subraw Source-Completion Bound

### 22.1 Completion Series

Let `r_n` be the vector of unprinted source-residue amounts after `n`
completion rounds.  P4 gives:

$$
\boxed{
r_{n+1}\le M_\lambda r_n.
}
$$

Thus:

$$
\boxed{
r_n\le M_\lambda^n r_0.
}
$$

The total carrier cost is bounded by:

$$
\boxed{
C_{\rm comp}(B,\lambda)
\le
\sum_{n=0}^\infty
\mathbf 1^\top\operatorname{diag}(c)M_\lambda^n r_0.
}
$$

Since `\rho(M_\lambda)<1`:

$$
\boxed{
C_{\rm comp}(B,\lambda)
\le
\mathbf 1^\top\operatorname{diag}(c)(I-M_\lambda)^{-1}r_0.
}
$$

### 22.2 Theorem 18: Subraw Source Completion

If `B` is physical at tolerance `\lambda`, then source completion is subraw:

$$
\boxed{
C_{\rm comp}(B,\lambda)
=
o(C_{\rm raw}(B)).
}
$$

**Proof.**

P4 makes `(I-M_\lambda)^{-1}` finite.  P5 states exactly that the resulting
finite carrier-completion cost is `o(C_{\rm raw}(B))`.  Therefore completion
does not reconstruct the raw hidden history. `\square`

### 22.3 Stronger Usable Bound

If `\|M_\lambda\|\le\rho<1`, then:

$$
\boxed{
C_{\rm comp}(B,\lambda)
\le
\frac{\|c\|_1\|r_0\|_1}{1-\rho}.
}
$$

Thus subraw completion follows from:

$$
\boxed{
\|c\|_1\|r_0\|_1
=
o(C_{\rm raw}(B)).
}
$$

This is often the easier finite estimate.

## 23. Completed Physical Boundary Theorem

### 23.1 Theorem 19: Physical Completion Gives Positive Conductance

Let `B` be physical at tolerance `\lambda`.  Let `B^\star` be the source
completion produced by P2--P5.  After quotienting same-actual null islands:

$$
\boxed{
\Phi_{B^\star,\lambda}>0.
}
$$

**Proof.**

Assume not.  Then there exists a nonempty unresolved set `S` in `B^\star` with
`\Phi_{B^\star}(S)=0`.

By Theorem 17, `S` is either same-actual null or a printable typed source
sector.  Same-actual null sets have been quotiented.  Printable typed source
sectors have already been included by completion.  Contradiction. `\square`

### 23.2 Corollary: Intrinsic Gap and Subraw Closure

With finite degree/hyperedge-size bounds:

$$
\boxed{
\gamma_{B^\star,\lambda}>0,
\qquad
\theta_{B^\star,\lambda}<1.
}
$$

By Theorem 18, the completion remains subraw.  Hence:

$$
\boxed{
C(\mathfrak O^\dagger_{B^\star,\lambda})
=
o(C_{\rm raw}(B^\star)).
}
$$

### 23.3 Interpretation

The physical boundary is not "whatever region we first guessed."  It is:

$$
\boxed{
\text{the smallest completed record diamond whose unprinted source residues
contract and whose completion remains subraw.}
}
$$

If no such completion exists at the requested tolerance, the experiment has no
closed bounded click law at that tolerance.

## 24. Hostile Review of the Physical-Diamond Proof

### Review F: "You built the theorem into P2."

Partly sustained.

P2 is the physical admissibility axiom: detached physical influence must have a
finite source carrier.  Without it, arbitrary finite diamonds have the
counterexample in Section 19.  The theorem is therefore not a pure
order-theoretic theorem; it is a theorem for record-law-admissible physical
diamonds.

### Review G: "P4 is another spectral gap."

Accepted.

P4 is the source-sector version of the gap.  The gain is that it is now
localized to carrier reproduction, not stated as a global mystery.  It can be
tested by bounding the finite nonnegative matrix `M_\lambda`.

### Review H: "P5 is exactly subrawness."

Accepted, but it is the computable form of subrawness:

$$
\mathbf 1^\top\operatorname{diag}(c)(I-M_\lambda)^{-1}r_0
=
o(C_{\rm raw}(B)).
$$

This replaces "do not reconstruct" with a finite matrix estimate.

### Review I: "The proof still does not show our universe satisfies P2--P5."

Accepted.

That is now the empirical/theoretical bridge: show physical experiments have
finite printable source carriers and subcritical carrier reproduction at their
tolerances.  The paper proves the mathematical implication once those finite
conditions hold.

## 25. Interim Status After Scoped Proof

The requested theorem is now proved in the only honest scope:

$$
\boxed{
\text{physical bounded diamonds satisfying finite carrier admissibility and
subcritical source reproduction obey the zero-conductance dichotomy and
subraw source-completion bounds.}
}
$$

It is not proved for arbitrary finite orders; Section 19 gives a counterexample.

The next irreducible theorem is smaller:

$$
\boxed{
\text{derive P2--P5 from the primitive record/diamond axioms or from the
previous v4--v7 physical reconstruction theorems.}
}
$$

Until that is derived, Paper XLI gives a conditional physical theorem, not a
universal one.

## 26. Deriving P2--P5 From Earlier Papers

This section follows the last opening.  Can the physical-diamond conditions be
derived from the previous v4--v7 corpus rather than assumed?

The answer is partial but sharp: the earlier papers supply three finite
ingredients that would imply P2--P5 if their all-scale versions are proved.

### 26.1 Ingredient A: Source-Conditioned Finite Packets

The v4 source-conditioned packet line uses finite data:

$$
\boxed{
{\mathfrak D}_a
=
(\Lambda_a,m_a,o_a,s_a,b_a,\mathcal T_a,D_a,H_a,P_{a\to b},\eta_a).
}
$$

The important entries here are:

- `s_a`: source or matter records;
- `b_a`: boundary collar records;
- `P_{a\to b}`: projective prolongation maps;
- `\eta_a`: finite tolerances.

This supports P2 and P3: source information is not metaphysical background.
It is represented by finite source and boundary records.

### 26.2 Ingredient B: Compressed Boundary Recurrence

Paper XXIX found that the raw deletion tensor is exact but too reconstructive,
while the compressed boundary histogram:

$$
\boxed{
H_R(a,b)=\mathbb P(a,b\mid R)
}
$$

reconstructs the score polynomial in audited windows and is much smaller than
the full boundary tensor.

The live recurrence target there was:

$$
\boxed{
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b}.
}
$$

This supports P5: source/boundary completion should use compressed boundary
carriers, not full deletion decks.

### 26.3 Ingredient C: Least Boundary Work

Paper XXXVI stated the bounded experiment principle:

$$
\boxed{
B=\text{system}+\text{instrument}+\text{relevant boundary history}.
}
$$

and the least-boundary-work objective:

$$
\boxed{
\mathcal A_B(k,O)
=
\sum_{j=k}^{\infty}\Delta_{B,j}
+
A_{B,k}(O)
+
\lambda C_B(k,O).
}
$$

This supports P4 and P5 in form: use more boundary history only while it
reduces tail error faster than it increases reconstruction cost.

## 27. Corpus Bridge Theorem

### 27.1 The Three External Premises

Define three finite premises:

1. **Finite carrier premise.**  Every non-same-actual zero-conductance island
   has a source-conditioned finite packet carrier of the v4 kind.
2. **Compressed recurrence premise.**  Carrier completion is represented in a
   compressed deletion/score-boundary algebra, not a raw deletion deck.
3. **Boundary-work contraction premise.**  The least-boundary-work tail
   `\sum_{j\ge k}\Delta_{B,j}` is summable after carrier completion.

### 27.2 Theorem 20: Earlier-Paper Bridge Implies P2--P5

If the three premises hold for a bounded diamond `B` at tolerance `\lambda`,
then `B` satisfies P2--P5.

**Proof.**

The finite carrier premise gives P2: every non-null detached island can be
printed as a finite source carrier.  It gives P3 because the carrier packet is
finite.

The boundary-work contraction premise gives a subcritical reproduction
operator: if source completion did not contract, the tail
`\sum_{j\ge k}\Delta_{B,j}` would not be summable after completion.  Thus it
gives P4 in dominated finite-matrix form.

The compressed recurrence premise says completion is represented by the
compressed boundary algebra.  Combining it with the least-boundary-work
penalty `\lambda C_B(k,O)` gives P5: completion is admissible only while its
compressed carrier cost remains below raw reconstruction. `\square`

### 27.3 Hostile Review

**Objection:** the three premises are not all proved.

Accepted.

The v4 source-conditioned packet line proves finite packet logic once source
records are declared; it does not prove every physical source island has such a
carrier.  Paper XXIX proves compressed recurrence in audited finite windows; it
does not prove the all-depth controlled-drift theorem.  Paper XXXVI formulates
least boundary work; it does not prove the universal tail bound.

So the bridge theorem is conditional, but it identifies the exact missing
all-scale statements.

## 28. All-Scale Statements Needed

The conditional proof reduces the open problem to three all-scale theorems.

### 28.1 Carrier Completeness

$$
\boxed{
\text{Every physical zero-conductance island has a finite source-conditioned
carrier packet.}
}
$$

This is P2 at all scales.

### 28.2 Controlled Drift of Compressed Boundary Covers

$$
\boxed{
\text{The compressed boundary recurrence remains stable under deletion,
insertion, and projection without becoming a full deletion deck.}
}
$$

This is the Paper XXIX `Hbar` opening in the language of Paper XLI.

### 28.3 Boundary-Tail Summability

$$
\boxed{
\sum_{j=k}^{\infty}\Delta_{B,j}
<\infty
\quad\text{after finite carrier completion.}
}
$$

This is the analytic tail statement needed for P4 and P5.

## 29. Strongest Bridge Theorem Before All-Scale Follow-Up

Combining Sections 19--28 gives:

#### Theorem 21: Current Physical-Diamond Closure Theorem

For arbitrary finite diamonds, the zero-conductance dichotomy is false.

For record-law-admissible physical diamonds satisfying:

1. finite source carrier completeness;
2. compressed nonraw boundary recurrence;
3. summable least-boundary-work tail;

the zero-conductance dichotomy and subraw source-completion bounds hold.

Consequently:

$$
\boxed{
\Phi_{B^\star,\lambda}>0,\quad
\gamma_{B^\star,\lambda}>0,\quad
\theta_{B^\star,\lambda}<1,
}
$$

and the completed no-silent panel is nonreconstructive.

### 29.1 What This Means

This is a real theorem, but not the final universe theorem.  It says exactly
which all-scale statements would close the first dependency chain.

The remaining missing theorem is now:

$$
\boxed{
\text{prove carrier completeness, compressed-boundary controlled drift, and
boundary-tail summability for the physical diamond class.}
}
$$

This is smaller and sharper than "prove the click law."

## 30. Carrier Completeness Campaign

The first all-scale statement is carrier completeness.

### 30.1 Finite Witness Principle

A record is not merely an abstract hidden variable.  It is physical only if a
finite instrument/boundary extension can witness it at some tolerance.

State this as:

$$
\boxed{
\text{finite witnessability: every physical non-null record difference has a
finite record witness.}
}
$$

If no finite witness exists at tolerance `\lambda`, the difference is
same-actual at that tolerance.

### 30.2 Theorem 22: Finite Witnessability Gives Carrier Completeness

Assume finite witnessability.  Then every physical zero-conductance island has
a finite source-conditioned carrier packet.

**Proof.**

Let `S` be a physical zero-conductance island that is not same-actual null.
Since it is physical and non-null, finite witnessability gives a finite record
witness `W_S` that distinguishes the perturbation.  Because `S` has zero
conductance relative to the current boundary, `W_S` is not already printed by
the boundary panel.  Add the minimal records needed to print `W_S`; this finite
extension is the carrier packet.  Its printed response is, by construction, a
typed source response. `\square`

### 30.3 Hostile Review

**Objection:** finite witnessability is philosophical.

Accepted, but it is also the meaning of "record."  A difference that no finite
record extension can witness is not an extra physical record difference inside
this finite theory.  It is same-actual at the requested tolerance.

Thus carrier completeness is as strong as the program's finite-record
ontology.  Rejecting it means admitting non-record physical facts.

## 31. Compressed-Boundary Controlled Drift Campaign

The second all-scale statement is controlled drift of compressed boundary
covers.

### 31.1 Boundary Algebra

Let:

$$
\boxed{
\mathcal H_N
}
$$

be the compressed boundary algebra at size/depth `N`.  Its atoms are not raw
records.  They are compressed deletion/insertion boundary types such as the
Paper XXIX `Hbar` histogram.

Let:

$$
\boxed{
\Pi_{N+1\to N}:\mathcal H_{N+1}\to\mathcal H_N
}
$$

be the projection induced by deleting or forgetting the added boundary layer.

Controlled drift means:

$$
\boxed{
d_{\mathcal H}
\left(
\Pi_{N+1\to N}\mathcal H_{N+1},
\mathcal H_N
\right)
\le
\delta_N,
\qquad
\sum_N\delta_N<\infty.
}
$$

### 31.2 Recurrence Generator

Assume a finite generator:

$$
\boxed{
\mathcal B_N^\downarrow
}
$$

such that:

$$
\boxed{
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b}.
}
$$

and assume its compressed action has bounded distortion:

$$
\boxed{
\|\Pi_{N+1\to N}\mathcal B_{N+1}^\downarrow
-\mathcal B_N^\downarrow\|_{\mathcal H}
\le
\delta_N.
}
$$

### 31.3 Theorem 23: Recurrence Drift Gives Controlled Covers

If:

1. the compressed recurrence generator exists for all `N`;
2. its projection distortion has summable tail `\sum_N\delta_N<\infty`;
3. the cover selection is minimal sufficient in `\mathcal H_N`;
4. the raw deletion deck is excluded by the nonlookup penalty;

then compressed boundary covers have controlled drift and remain nonraw.

**Proof Sketch.**

The recurrence generator transfers the score/law information from depth
`N+1` to depth `N`.  Summable distortion means the transferred compressed
algebra is Cauchy under projection.  Minimal sufficient cover selection cannot
jump to the raw deletion deck because nonlookup excludes it, and any finite
jump must be paid for by the summable distortion budget.  Therefore the covers
drift in a controlled way. `\square`

### 31.4 Hostile Review

**Objection:** the all-`N` compressed recurrence is not proved.

Accepted.  Paper XXIX supplies finite evidence and the correct object, not the
all-scale theorem.  The remaining mathematical task is exactly:

$$
\boxed{
\text{prove the compressed recurrence generator exists with summable
projection distortion.}
}
$$

This is now the compressed-boundary version of subraw source completion.

## 32. Boundary-Tail Summability Campaign

The third all-scale statement is tail summability.

### 32.1 Tail From Completed Gap

After carrier completion and same-actual quotienting, Theorem 19 gives:

$$
\boxed{
\gamma_{B^\star,\lambda}>0,
\qquad
\theta_{B^\star,\lambda}<1.
}
$$

For any admissible target `Y`:

$$
\boxed{
\Delta_{B,j}^Y
\le
C_Y\theta_{B^\star,\lambda}^{\,j}
+
C_Y'\delta_j.
}
$$

The first term is unresolved response decay.  The second is compressed-boundary
drift.

### 32.2 Theorem 24: Completed Gap Plus Controlled Drift Gives Tail Summability

If:

$$
\boxed{
\theta_{B^\star,\lambda}<1,
\qquad
\sum_j\delta_j<\infty,
}
$$

then:

$$
\boxed{
\sum_{j=k}^{\infty}\Delta_{B,j}^Y<\infty.
}
$$

**Proof.**

The geometric series `\sum_j\theta^j` converges because `\theta<1`.  The
drift series converges by controlled drift.  Therefore their linear
combination is summable. `\square`

### 32.3 Consequence

Boundary-tail summability is not an independent mystery.  It follows from:

1. finite carrier completion;
2. positive completed gap;
3. controlled compressed-boundary drift.

## 33. Final Closure of the Requested Target

We can now state the sharpest proof.

#### Theorem 25: Scoped Physical Bounded-Diamond Theorem

Assume:

1. finite witnessability of physical record differences;
2. compressed deletion/insertion boundary recurrence with summable projection
   distortion;
3. nonlookup exclusion of raw deletion decks;
4. finite degree/hyperedge-size of the completed response hypergraph.

Then physical bounded diamonds satisfy:

$$
\boxed{
\text{zero-conductance dichotomy}
}
$$

and:

$$
\boxed{
\text{subraw source-completion bounds}.
}
$$

Consequently the completed boundary has positive intrinsic gap, controlled
history tail, and a nonreconstructive projected click law for admissible
targets.

**Proof.**

Finite witnessability gives carrier completeness by Theorem 22.
Carrier completion plus same-actual quotienting gives positive completed
conductance by Theorem 19.  Positive conductance gives intrinsic gap and
contraction.  The compressed recurrence with summable distortion gives
controlled boundary-cover drift by Theorem 23.  Gap plus controlled drift gives
tail summability by Theorem 24.  Nonlookup exclusion keeps the completion below
raw reconstruction. `\square`

### 33.1 What Is Now Irreducible?

The theorem still has two irreducible inputs:

1. **Finite witnessability.**  This is the finite-record ontology.  Without it,
   non-record hidden facts are allowed.
2. **All-scale compressed recurrence.**  This is a mathematical theorem still
   to prove.  Finite audits found the right object, but not the all-`N` proof.

Everything else in the requested target follows from these two inputs plus
finite-degree bookkeeping.

## 34. Final Status After Continuing

The requested statement is now proved in a precise scoped form:

$$
\boxed{
\text{physical finite-witness diamonds with all-scale compressed recurrence
satisfy zero-conductance dichotomy and subraw source completion.}
}
$$

It cannot be made unconditional for arbitrary finite diamonds; the detached
island counterexample forbids that.

The exact next theorem is:

$$
\boxed{
\text{prove the all-scale compressed deletion/insertion boundary recurrence
with summable projection distortion.}
}
$$

This is the main mathematical work left in the first dependency chain.

## 35. Spacetime-Closure Implies Intrinsic-Gap Campaign

The previous route proved the intrinsic gap from completed physical boundary
conditions.  There is a complementary route:

$$
\boxed{
\text{stable spacetime closure}
\quad\Longrightarrow\quad
\text{intrinsic gap}.
}
$$

This section proves the strongest honest version.  It is not true for any
coarse spacetime-looking summary.  It is true only for a separating finite
spacetime packet.

### 35.1 No-Go for Weak Spacetime Summaries

Let a packet remember only a coarse dimension and volume profile:

$$
\boxed{
\mathcal G_B^{weak}(H)=(d_B,V_B).
}
$$

Add a detached hidden island `Z` whose size and interval profile are chosen so
that the total `(d_B,V_B)` does not change above tolerance.  Then:

$$
\boxed{
\mathcal G_B^{weak}(H)
\approx_\epsilon
\mathcal G_B^{weak}(H\sqcup Z),
}
$$

while `Z` can still carry a non-same-actual source response.  Thus weak
spacetime summaries do not imply a gap.

The theorem must require a packet that separates local record response.

### 35.2 Separating Spacetime Packet

Write the finite spacetime packet as:

$$
\boxed{
\mathcal G_B(H)
=
\left(
d_B,V_B,\ell_B,\mathcal R_B,\mathcal B_B,\mathcal T_B,\mathcal M_B
\right).
}
$$

It is **response-separating at tolerance** `\epsilon` if every physical
non-same-actual perturbation `S` above tolerance changes at least one of:

1. causal distance/layer profile `\ell_B`;
2. curvature/work residue `\mathcal R_B`;
3. Ward/Bianchi residue `\mathcal B_B`;
4. typed source residue `\mathcal T_B`;
5. manifold/atlas defect `\mathcal M_B`;
6. or the click target family `\mathcal Y_B`;

unless `S` is printed as a typed source carrier.

In formula form:

$$
\boxed{
S\not\subset\ker(\sim_{\rm same\ actual}),\quad
\|S\|_\lambda>\epsilon
\quad\Longrightarrow\quad
d_{ST}\bigl(\mathcal G_B(H),\mathcal G_B(H+S)\bigr)>\epsilon
\ \text{or}\ 
S\in\mathcal T_B^{source}.
}
$$

This is the separation lemma in definition form.

### 35.3 Stable Spacetime Closure

The packet is stable if:

$$
\boxed{
\mathcal E_B^{ST}
=
\operatorname{diam}_{ST}(\mathcal P_{B,k,\lambda})
+
\mathcal M_B+\mathcal B_B+\mathcal R_B
\le
\epsilon_{ST}.
}
$$

It is **completed** if every typed source sector above tolerance is already
printed in `\mathcal T_B`.

### 35.4 Theorem 26: Separating Spacetime Closure Implies Zero-Conductance Dichotomy

Assume:

1. `B` has a completed finite spacetime packet `\mathcal G_B`;
2. `\mathcal G_B` is response-separating at tolerance `\epsilon`;
3. `\mathcal E_B^{ST}\le\epsilon`;
4. same-actual null differences are quotiented.

Then every zero-conductance physical island above tolerance is same-actual
null or already printed as a typed source sector.

**Proof.**

Let `S` be a zero-conductance physical island with `\|S\|_\lambda>\epsilon`.
If `S` is same-actual null, we are done.

If not, response separation says that either `S` changes the spacetime packet
or click target above tolerance, or `S` is a typed source sector.  The packet is
stable and completed, so any above-tolerance typed source sector is already
printed, and any above-tolerance packet change would contradict
`\mathcal E_B^{ST}\le\epsilon`.  Therefore the only admissible alternatives are
same-actual null or printed typed source. `\square`

### 35.5 Theorem 27: Separating Spacetime Closure Implies Intrinsic Gap

Assume the hypotheses of Theorem 26 and finite degree/hyperedge-size of the
completed response hypergraph.  Then the completed diamond has positive
anchored conductance:

$$
\boxed{
\Phi_{B,\lambda}>0,
}
$$

and therefore positive intrinsic gap:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

**Proof.**

Theorem 26 gives the zero-conductance dichotomy.  Same-actual null sets are
quotiented.  Typed source sectors are printed and therefore anchored.  Hence no
nonempty unresolved above-tolerance physical set has zero conductance.  In the
finite completed response hypergraph, the infimum defining `\Phi_{B,\lambda}`
is a minimum over finitely many unresolved atom sets, all of which have
positive conductance.  Thus `\Phi_{B,\lambda}>0`.  The finite Cheeger/Hessian
bound gives `\gamma_{B,\lambda}>0`. `\square`

### 35.6 What This Proves

The implication is:

$$
\boxed{
\text{stable completed response-separating spacetime packet}
\Rightarrow
\text{intrinsic gap}.
}
$$

It is not:

$$
\boxed{
\text{any spacetime-like summary}
\Rightarrow
\text{intrinsic gap}.
}
$$

The response-separation clause is the exact technical heart.

## 36. Can Response Separation Be Derived?

The next opening is whether response separation is another premise or follows
from the packet definition.

### 36.1 Packet Separation Channels

The packet components cover the primitive interfaces as follows:

| Primitive response | Packet channel |
|---|---|
| boundary/collar drift | `\ell_B`, `\mathcal M_B` |
| interval/layer distortion | `d_B`, `V_B`, `\ell_B`, `\mathcal M_B` |
| deletion/insertion update residue | `\mathcal R_B`, `\mathcal B_B` |
| overlap inconsistency | `\mathcal B_B`, `\mathcal M_B` |
| matter/source/entanglement residue | `\mathcal T_B` |
| target-specific click change | `\mathcal Y_B` |

Thus response separation follows if this table is complete and if the packet
channels have tolerance floors.

### 36.2 Theorem 28: Primitive Interface Coverage Implies Response Separation

Assume:

1. every physical perturbation above tolerance has a nonzero primitive
   interface response;
2. the packet table above covers all primitive interfaces;
3. each packet channel has a detection floor:

   $$
   \boxed{
   \|\delta_{\xi}(S)\|>\epsilon_\xi
   \quad\Longrightarrow\quad
   d_\xi(\mathcal G_B(H),\mathcal G_B(H+S))>\epsilon.
   }
   $$

Then `\mathcal G_B` is response-separating.

**Proof.**

By assumption 1, any physical non-same-actual perturbation above tolerance has
a nonzero primitive response.  By assumption 2, that primitive response is
assigned to at least one packet channel.  By assumption 3, a nonzero
above-tolerance response in that channel changes the packet above tolerance,
unless it is explicitly routed into a typed source channel. `\square`

### 36.3 Hostile Review

**Objection:** channel floors may fail in degenerate or pre-spacetime regimes.

Accepted.

Then the theorem does not apply.  The region may still click, but it does not
license a spacetime-implies-gap argument.  This is exactly the distinction
between click-predictive pre-spacetime regimes and spacetime-closed regimes.

**Objection:** a hidden island could affect no spacetime channel but affect a
future non-geometric click.

Accepted unless `\mathcal Y_B` is included in the separating family.  The
correct theorem is packet-plus-target separation, not geometry-only
separation.

## 37. Final Result of the Spacetime-Gap Campaign

The final scoped theorem is:

#### Theorem 29: Spacetime Closure Forces Intrinsic Gap

For a completed bounded record diamond `B`, if:

1. the finite spacetime packet `\mathcal G_B` is stable;
2. typed source sectors above tolerance are printed;
3. same-actual null differences are quotiented;
4. `\mathcal G_B` plus the target family `\mathcal Y_B` separates all
   primitive physical response channels above tolerance;

then:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

Equivalently, stable spacetime closure with separating packet channels cannot
coexist with an above-tolerance zero-conductance physical island.

### 37.1 Meaning

If spacetime can be defined in a bounded region in the strong finite sense,
then the intrinsic gap is not an extra assumption for that region.  It is a
consequence of stable, completed, response-separating spacetime closure.

If spacetime closure is weak, nonseparating, or only a coarse summary, the
implication fails.

### 37.2 Updated Remaining Target

There are now two routes to the intrinsic gap:

1. **Completion route:** finite witnessability plus subraw compressed
   recurrence.
2. **Spacetime route:** stable completed response-separating spacetime packet.

The strongest next theorem is therefore:

$$
\boxed{
\text{prove the finite spacetime packet channels cover all primitive
above-tolerance response interfaces in spacetime-like regimes.}
}
$$

That theorem would make "spacetime exists here" imply "the intrinsic gap holds
here" without separately assuming the gap.

## 38. Finite Spacetime Packet Coverage Campaign

This section follows the new target:

$$
\boxed{
\text{prove the finite spacetime packet channels cover all primitive
above-tolerance response interfaces in spacetime-like regimes.}
}
$$

The theorem cannot mean that geometry-only data sees every possible record
fact.  It must mean that a **licensed spacetime packet plus target/source
channels** sees every primitive response relevant above tolerance.

### 38.1 Primitive Response Vector

For a perturbation or source island `S`, define the primitive response vector:

$$
\boxed{
\delta_{\rm prim}(S)
=
\left(
\delta_\partial S,
\delta_I S,
\delta_U S,
\delta_O S,
\delta_T S,
\delta_Y S
\right).
}
$$

The components mean:

- `\delta_\partial S`: boundary/collar response;
- `\delta_I S`: interval/layer response;
- `\delta_U S`: deletion/insertion/refinement response;
- `\delta_O S`: overlap/transport response;
- `\delta_T S`: typed source, matter, entanglement, or topological response;
- `\delta_Y S`: target-specific click response.

The first four are the record-diamond primitive interfaces.  The last two are
necessary because spacetime alone need not separate matterlike or
target-specific sectors.

### 38.2 Packet Channel Vector

Define the extended finite spacetime packet:

$$
\boxed{
\mathcal K_B
=
\left(
\mathcal G_B,\mathcal T_B,\mathcal Y_B
\right).
}
$$

Here:

- `\mathcal G_B` is the finite spacetime packet;
- `\mathcal T_B` is the typed source/entanglement/topology dictionary;
- `\mathcal Y_B` is the target family being predicted.

The packet response vector is:

$$
\boxed{
\delta_{\mathcal K}(S)
=
\left(
\delta_dS,\delta_VS,\delta_\ell S,\delta_{\mathcal R}S,
\delta_{\mathcal B}S,\delta_{\mathcal T}S,\delta_{\mathcal M}S,
\delta_YS
\right).
}
$$

### 38.3 Coverage Matrix

Define the coverage relation:

$$
\boxed{
\mathsf C_{\xi\eta}=1
\quad\Longleftrightarrow\quad
\text{packet channel }\eta\text{ detects primitive response }\xi
\text{ above tolerance.}
}
$$

The intended coverage matrix is:

| Primitive response `\xi` | Detecting channels `\eta` |
|---|---|
| `\delta_\partial` | `\delta_\ell`, `\delta_{\mathcal M}`, `\delta_{\mathcal B}` |
| `\delta_I` | `\delta_d`, `\delta_V`, `\delta_\ell`, `\delta_{\mathcal M}` |
| `\delta_U` | `\delta_{\mathcal R}`, `\delta_{\mathcal B}`, `\delta_Y` |
| `\delta_O` | `\delta_{\mathcal B}`, `\delta_{\mathcal M}` |
| `\delta_T` | `\delta_{\mathcal T}`, `\delta_{\mathcal R}`, `\delta_Y` |
| `\delta_Y` | `\delta_Y` |

Coverage means:

$$
\boxed{
\|\delta_{\rm prim}(S)\|_\lambda>\epsilon
\quad\Longrightarrow\quad
\|\delta_{\mathcal K}(S)\|_{\mathcal K}>\epsilon'
}
$$

unless `S` is same-actual null.

### 38.4 No-Go: Geometry-Only Coverage Fails

If `\mathcal K_B` omits `\mathcal T_B` and `\mathcal Y_B`, coverage fails.

Example: a spin, charge, entanglement, or internal source sector can leave
dimension, volume, and causal distance nearly unchanged while changing a
future click or source response.  Then:

$$
\boxed{
\delta_{\mathcal G}(S)\approx0,
\qquad
\delta_T(S)\ne0
\quad\text{or}\quad
\delta_Y(S)\ne0.
}
$$

Therefore the theorem must be packet-plus-source-plus-target, not
geometry-only.

## 39. Coverage Theorem

### 39.1 Spacetime-Like Regime Definition

A completed bounded diamond is **spacetime-like at tolerance** `\epsilon` if:

1. the finite packet `\mathcal G_B` is licensed:

   $$
   \boxed{
   \rho_B\ge\rho_0(\epsilon)>0;
   }
   $$

2. atlas/overlap defects are small:

   $$
   \boxed{
   \mathcal M_B+\mathcal B_B\le\epsilon;
   }
   $$

3. curvature/source residues are either small or typed:

   $$
   \boxed{
   \mathcal R_B\le\epsilon
   \quad\text{or}\quad
   \mathcal R_B\in\mathcal T_B;
   }
   $$

4. the target family `\mathcal Y_B` is included in the panel;
5. same-actual zero modes are quotiented.

### 39.2 Local Packet Sensitivity Floors

For each coverage edge `\xi\to\eta`, require a finite sensitivity floor:

$$
\boxed{
\|\delta_\xi(S)\|_\lambda>\epsilon_\xi
\quad\Longrightarrow\quad
\|\delta_\eta(S)\|_\eta>\epsilon_\eta.
}
$$

These floors are not universal constants.  They are tolerance-relative
properties of the licensed packet.  If a floor fails, the packet is degenerate
for that response and cannot claim spacetime-like closure at that tolerance.

### 39.3 Theorem 30: Finite Packet Coverage

Assume:

1. `B` is spacetime-like at tolerance `\epsilon`;
2. the coverage matrix of Section 38.3 has at least one detecting packet
   channel for every primitive response component;
3. every active coverage edge has a sensitivity floor;
4. `\mathcal T_B` includes every typed source sector above tolerance;
5. `\mathcal Y_B` includes the target family whose clicks are being predicted.

Then the extended packet:

$$
\boxed{
\mathcal K_B=(\mathcal G_B,\mathcal T_B,\mathcal Y_B)
}
$$

separates every primitive above-tolerance physical response:

$$
\boxed{
\|\delta_{\rm prim}(S)\|_\lambda>\epsilon
\quad\Longrightarrow\quad
\|\delta_{\mathcal K}(S)\|_{\mathcal K}>\epsilon'
}
$$

unless `S` is same-actual null.

**Proof.**

Let `S` be an above-tolerance primitive physical response.  At least one
component `\delta_\xi(S)` is above its tolerance.  By the coverage matrix there
is a detecting packet/source/target channel `\eta`.  By the sensitivity floor
for `\xi\to\eta`, the packet-channel response is above tolerance.  If the
response is typed source-like, assumption 4 prints it in `\mathcal T_B`.  If it
is target-specific, assumption 5 prints it in `\mathcal Y_B`.  If neither
detects it, then no primitive component was above tolerance, contradicting the
starting assumption.  Same-actual null responses are quotiented. `\square`

### 39.4 Corollary: Spacetime-Like Closure Implies Intrinsic Gap

Combining Theorem 30 with Theorem 29:

$$
\boxed{
\text{stable spacetime-like completed packet}
\quad\Longrightarrow\quad
\gamma_{B,\lambda}>0
}
$$

provided the packet is extended by typed source and target channels.

## 40. Hostile Coverage Review

### Review J: "You smuggled the target into the packet."

Partly accepted.

A geometry-only packet cannot predict arbitrary non-geometric clicks.  The
correct statement is not "spacetime alone sees everything."  It is:

$$
\boxed{
\text{spacetime packet + typed sources + requested target channels}
\text{ sees every response relevant to that claim.}
}
$$

This is not cheating; it is the finite experimental fact that an apparatus must
print the observable it claims to predict.

### Review K: "Sensitivity floors are assumptions."

Accepted.

They are precisely the finite anti-degeneracy/licensing conditions.  In
pre-spacetime or degenerate regimes the floors fail, and no spacetime-implies-
gap theorem is licensed.

### Review L: "Gauge/presentation changes may change packet channels."

Rejected after same-actual quotienting.

Gauge/presentation changes are same-actual null.  They are removed before
coverage is tested.  If a change survives same-actual quotienting, it must
appear in a primitive response component.

### Review M: "Long entanglement can be spacelike and not geometric."

Accepted.

That is why `\mathcal T_B` is part of the extended packet.  Long entanglement
is not required to be metric-local.  It must be record-bounded and printed as a
typed sector if it affects the target above tolerance.

### Review N: "Topology could evade local channels."

Accepted unless topology is typed.

Global/topological response must enter `\mathcal T_B` or `\mathcal M_B` as an
atlas/overlap defect.  If it is neither typed nor visible in atlas consistency,
the packet is not response-separating.

## 41. Opening Follow-Up: Are Typed Channels Finite?

The coverage theorem moves pressure onto `\mathcal T_B`.  It must remain finite
and subraw.

### 41.1 Typed Channel Admission

A typed channel `\tau` is admitted if:

$$
\boxed{
m_\tau(B)<\infty,\qquad
\theta_\tau(B)<1,\qquad
C_\tau(B)=o(C_{\rm raw}(B)).
}
$$

These are the same conditions as source completion: finite mass, contracting
residual, and nonraw complexity.

### 41.2 Theorem 31: Typed Coverage Remains Subraw

If every typed channel required by Theorem 30 satisfies the admission
conditions above, then extended packet coverage remains subraw:

$$
\boxed{
C(\mathcal K_B)=o(C_{\rm raw}(B)).
}
$$

**Proof.**

The geometry packet is finite by licensing.  The target family is finite for
the experiment by definition of the requested prediction.  The typed channels
are finite and subraw by admission.  A finite union of subraw admitted channels
is subraw, provided the number of admitted types grows subraw; otherwise the
typed sector itself violates admission. `\square`

### 41.3 Hostile Review

**Objection:** a finite union of subraw channels can fail if there are too many
types.

Accepted.  The admission condition must be applied to the total typed
dictionary:

$$
\boxed{
C(\mathcal T_B)=o(C_{\rm raw}(B)).
}
$$

Thus the correct statement is dictionary-subrawness, not per-type subrawness.

## 42. Final Packet-Coverage Result

The full campaign result is:

#### Theorem 32: Spacetime Packet Coverage and Gap

For a completed bounded diamond `B`, suppose:

1. `B` is spacetime-like at tolerance `\epsilon`;
2. the finite spacetime packet has channel floors for boundary, interval,
   update, and overlap responses;
3. the typed dictionary `\mathcal T_B` is finite and subraw and includes every
   above-tolerance source, entanglement, topology, or matter sector relevant to
   the target;
4. the target family `\mathcal Y_B` is printed;
5. same-actual null modes are quotiented.

Then:

$$
\boxed{
\mathcal K_B=(\mathcal G_B,\mathcal T_B,\mathcal Y_B)
}
$$

is response-separating, subraw, and stable.  Therefore:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

### 42.1 What This Closes

This closes the spacetime route to the intrinsic gap in the scoped physical
sense:

$$
\boxed{
\text{strong finite spacetime closure}
\Rightarrow
\text{intrinsic gap}.
}
$$

### 42.2 What Remains

The remaining work is no longer "prove the gap" for spacetime-like regimes.
It is:

$$
\boxed{
\text{prove packet-channel floors and typed-dictionary subrawness in the
physical spacetime-like regimes of interest.}
}
$$

This is more concrete than the previous gap target: it can fail channel by
channel, and any failure says exactly what new record channel the click law
must print.

## 43. Packet-Channel Floor Campaign

The next opening is:

$$
\boxed{
\text{prove packet-channel floors in spacetime-like regimes.}
}
$$

A channel floor is a finite lower bound saying that an above-tolerance
primitive response cannot be invisible to all packet channels assigned to it.

### 43.1 Packet Map and Jacobian

Let:

$$
\boxed{
F_B:\mathcal R_B^{prim}\to\mathcal R_B^{packet}
}
$$

be the finite response map:

$$
\boxed{
\delta_{\rm prim}(S)\mapsto\delta_{\mathcal K}(S).
}
$$

Here:

- `\mathcal R_B^{prim}` is the finite vector space of primitive response
  components;
- `\mathcal R_B^{packet}` is the finite vector space of packet/source/target
  responses.

Around a spacetime-like packet, linearize:

$$
\boxed{
\delta_{\mathcal K}
=
J_B\delta_{\rm prim}
+
O(\|\delta_{\rm prim}\|^2).
}
$$

The channel floor is controlled by the smallest singular value of `J_B` on the
non-null quotient:

$$
\boxed{
s_{\min}^+(J_B)>0.
}
$$

### 43.2 Finite Inverse Function Criterion

Because all spaces are finite at fixed `B,\lambda`, if:

$$
\boxed{
s_{\min}^+(J_B)\ge s_0>0
}
$$

and the quadratic remainder is bounded by:

$$
\boxed{
\|O(\|\delta\|^2)\|\le L\|\delta\|^2,
}
$$

then for:

$$
\boxed{
\|\delta_{\rm prim}\|
\le
\frac{s_0}{2L},
}
$$

we have:

$$
\boxed{
\|\delta_{\mathcal K}\|
\ge
\frac{s_0}{2}\|\delta_{\rm prim}\|.
}
$$

This is the local packet-channel floor.

### 43.3 Theorem 33: Regular Packet Implies Channel Floors

Assume:

1. the completed packet is spacetime-like at tolerance `\lambda`;
2. same-actual null directions are quotiented;
3. the packet response Jacobian `J_B` has full rank on every primitive response
   subspace assigned to it by the coverage matrix;
4. the second-order remainder is bounded on the tolerance ball.

Then every assigned coverage edge has a channel floor.

**Proof.**

Full rank on the finite quotient gives `s_{\min}^+(J_B)>0`.  The remainder
bound gives the finite inverse estimate above.  Thus any primitive response
above tolerance in a covered direction changes at least one packet channel
above the corresponding packet tolerance. `\square`

### 43.4 Hostile Review and Follow-Up

**Objection:** rank can fail near caustics, horizons, phase transitions, or
pre-spacetime phases.

Accepted.

Those are exactly regimes where the packet is not licensed at that tolerance,
or where the boundary must be expanded.  The channel-floor theorem applies to
regular spacetime-like packets, not all record regimes.

**Objection:** full rank is another assumption.

Accepted, but it is sharper than "packet detects everything."  It can be
audited channel-by-channel as a finite rank condition:

$$
\boxed{
\ker J_B
=
\ker(\sim_{\rm same\ actual})
}
$$

on the primitive response quotient.  Any extra kernel vector is an explicit
missing channel.

## 44. Typed-Dictionary Subrawness Campaign

The second opening is:

$$
\boxed{
\text{prove the typed dictionary is finite and subraw.}
}
$$

### 44.1 Typed Dictionary as Source Rank

Let:

$$
\boxed{
\mathcal T_B
=
\{\tau_1,\ldots,\tau_{r_B}\}
}
$$

be the typed dictionary.  The number:

$$
\boxed{
r_B=|\mathcal T_B|
}
$$

is the source rank.  Subrawness requires:

$$
\boxed{
C(\mathcal T_B)
\le
\sum_{\tau\in\mathcal T_B}C_\tau
=
o(C_{\rm raw}(B)).
}
$$

### 44.2 Source Rank Bound

A spacetime-like packet licenses only typed sectors that couple to one of:

1. stress/source readout;
2. Ward/Bianchi residue;
3. atlas/topology residue;
4. target click response.

Let the finite ranks of these channels be:

$$
\boxed{
r_\Theta,\quad r_{\mathcal B},\quad r_{\mathcal M},\quad r_Y.
}
$$

Then:

$$
\boxed{
r_B
\le
r_\Theta+r_{\mathcal B}+r_{\mathcal M}+r_Y.
}
$$

This is not a species count for the universe.  It is the number of typed
sectors relevant to the bounded experiment at tolerance `\lambda`.

### 44.3 Carrier Cost Bound

Assume each typed sector has carrier cost:

$$
\boxed{
C_\tau
\le
C_0|\partial_\lambda B|^{d_\tau}.
}
$$

Let:

$$
\boxed{
d_T=\max_{\tau\in\mathcal T_B}d_\tau.
}
$$

Then:

$$
\boxed{
C(\mathcal T_B)
\le
C_0 r_B|\partial_\lambda B|^{d_T}.
}
$$

Typed-dictionary subrawness follows if:

$$
\boxed{
r_B|\partial_\lambda B|^{d_T}
=
o(C_{\rm raw}(B)).
}
$$

### 44.4 Theorem 34: Finite Source Rank Gives Typed-Dictionary Subrawness

Assume:

1. only sectors coupled to `(\Theta,\mathcal B,\mathcal M,Y)` are admitted;
2. their rank is finite and bounded by
   `r_\Theta+r_{\mathcal B}+r_{\mathcal M}+r_Y`;
3. carrier costs grow at most as `|\partial_\lambda B|^{d_T}`;
4. `r_B|\partial_\lambda B|^{d_T}=o(C_{\rm raw}(B))`.

Then:

$$
\boxed{
C(\mathcal T_B)=o(C_{\rm raw}(B)).
}
$$

**Proof.**

Combine the rank bound and carrier cost bound.  The displayed asymptotic is
exactly subrawness. `\square`

### 44.5 Hostile Review and Follow-Up

**Objection:** gauge theories can have infinitely many soft/infrared sectors.

Accepted.

Then the bounded experiment must use an inclusive typed sector rather than
print every soft configuration separately.  The dictionary entry is the
inclusive charge/flux/residue class, not each soft microstate.

This adds an admission rule:

$$
\boxed{
\text{infrared families must be compressed into finite inclusive source
types at tolerance }\lambda.
}
$$

**Objection:** topology can require global data.

Accepted.

If topology affects the target above tolerance, either it appears as an
atlas/overlap defect in `\mathcal M_B` or as a typed topological sector in
`\mathcal T_B`.  If it requires raw global reconstruction, no bounded
spacetime packet is licensed at that tolerance.

## 45. Combined Floor-And-Dictionary Theorem

#### Theorem 35: Regular Spacetime Packet Gives Subraw Response Separation

Assume:

1. regular packet Jacobian rank:

   $$
   \boxed{
   \ker J_B=\ker(\sim_{\rm same\ actual})
   }
   $$

   on covered primitive response channels;

2. bounded second-order response remainder;
3. finite source-rank bound for typed sectors;
4. carrier cost subrawness;
5. inclusive compression of infrared/soft families;
6. target family `\mathcal Y_B` is finite for the experiment.

Then the extended packet:

$$
\boxed{
\mathcal K_B=(\mathcal G_B,\mathcal T_B,\mathcal Y_B)
}
$$

has channel floors and typed-dictionary subrawness.  Therefore, by Theorem 32:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

### 45.1 What This Achieves

The intrinsic gap is now derived in spacetime-like regimes from two finite
auditable conditions:

1. a rank condition on the packet response map;
2. a subraw rank/cost bound on typed source dictionaries.

Both are more concrete than an assumed spectral gap.

### 45.2 What Can Still Fail

The theorem fails if:

1. the packet response map has a non-same-actual kernel;
2. a required typed dictionary has raw/global complexity;
3. an infrared family cannot be compressed inclusively;
4. the target family is too broad to be finite at the requested tolerance.

Each failure identifies a missing record channel or an unclosed experiment.

## 46. Updated End State

Paper XLI now has three gap routes:

1. **Completion route:** finite witnessability plus all-scale compressed
   recurrence.
2. **Spacetime route:** stable completed response-separating packet.
3. **Regular packet route:** packet Jacobian rank plus subraw typed dictionary.

The strongest current statement is:

$$
\boxed{
\text{in regular spacetime-like bounded diamonds, the intrinsic gap follows
from finite packet rank and subraw typed-source rank.}
}
$$

The exact next mathematical target is:

$$
\boxed{
\text{prove the packet response Jacobian rank condition for the finite
spacetime packet in calibrated spacetime-like diamonds.}
}
$$

That is now the highest-leverage theorem: it would turn the spacetime route
from conditional coverage into a finite rank theorem.

## 47. Packet-Rank Campaign

The target from Section 46 is too strong if read as:

$$
\boxed{
\text{a prechosen finite packet always has full rank.}
}
$$

That statement is false.  A hidden response channel can be orthogonal to the
packet by construction.  The correct target is:

$$
\boxed{
\text{the admissible packet closes its own non-same-actual kernel by the least
record-intrinsic subraw extension.}
}
$$

In other words, rank is not a miracle property of the first packet.  Rank is a
fixed point of the no-silent closure rule.

### 47.1 Quotient Response Space

Let:

$$
\boxed{
Q_B
=
\mathcal R_B^{prim}/\mathcal N_B^{actual}
}
$$

where:

- `\mathcal R_B^{prim}` is the finite primitive response space;
- `\mathcal N_B^{actual}` is the same-actual null space.

A packet map at closure stage `n` is:

$$
\boxed{
J_B^{(n)}:Q_B\to\mathcal R_B^{packet,n}.
}
$$

The unresolved kernel is:

$$
\boxed{
K_B^{(n)}
=
\ker J_B^{(n)}.
}
$$

The packet has the desired rank exactly when:

$$
\boxed{
K_B^{(n)}=0.
}
$$

### 47.2 Intrinsic Kernel Signature

For a nonzero vector `u\in K_B^{(n)}`, define its diamond signature:

$$
\boxed{
\Sigma_B(u)
=
\left(
\sigma_\partial(u),
\sigma_I(u),
\sigma_U(u),
\sigma_O(u),
\sigma_C(u),
\sigma_T(u)
\right).
}
$$

The entries mean:

- `\sigma_\partial` is the boundary incidence shadow;
- `\sigma_I` is the interval/layer shadow;
- `\sigma_U` is the deletion/insertion/update shadow;
- `\sigma_O` is the overlap/atlas shadow;
- `\sigma_C` is the center-ledger shadow;
- `\sigma_T` is the typed source/target shadow.

All six components are computed from record diamonds, histories, centers, and
printed typed sectors.  No continuum coordinate and no hidden presentation
count is used.

The no-silent condition says:

$$
\boxed{
u\ne0
\quad\Longrightarrow\quad
\Sigma_B(u)\ne0
}
$$

for every physical above-tolerance response in the quotient.

### 47.3 Kernel Promotion

If `K_B^{(n)}\ne0`, choose the least-cost signature class:

$$
\boxed{
\sigma_n
\in
\arg\min_{\Sigma_B(u),\,u\in K_B^{(n)}\setminus\{0\}}
C_B(\Sigma_B(u)).
}
$$

Promote this signature to a new packet channel:

$$
\boxed{
L_{\sigma_n}:Q_B\to\mathbb R^{m_{\sigma_n}}.
}
$$

and set:

$$
\boxed{
J_B^{(n+1)}
=
\begin{bmatrix}
J_B^{(n)}\\
L_{\sigma_n}
\end{bmatrix}.
}
$$

The channel is admissible only if:

$$
\boxed{
C_B(L_{\sigma_n})=o(C_{\rm raw}(B)).
}
$$

This is the rank version of source completion.  A missing response is not
guessed by hand; it is forced by the current kernel.

### 47.4 Theorem 36: Kernel Promotion Dichotomy

Assume:

1. `Q_B` is finite at fixed bounded diamond and tolerance;
2. same-actual null directions have been quotiented;
3. every physical nonzero `u\in Q_B` has a nonzero intrinsic signature
   `\Sigma_B(u)`;
4. every promoted signature channel is linear on the local response cone and
   nonzero on the kernel vector that generated it.

Then the kernel-promotion process satisfies exactly one of the following:

$$
\boxed{
\text{either }K_B^{(n_\star)}=0\text{ after finitely many subraw promotions,}
}
$$

or:

$$
\boxed{
\text{some required promotion has raw/reconstructive cost.}
}
$$

In the first case the packet response map has full rank on `Q_B`.  In the
second case no bounded nonreconstructive packet is licensed at the requested
tolerance.

**Proof.**

Each admissible promotion adds a channel nonzero on the current kernel.  Hence:

$$
\boxed{
\dim K_B^{(n+1)}<\dim K_B^{(n)}
}
$$

whenever the promoted channel is subraw and valid.  Since `Q_B` is finite, the
strictly decreasing nonnegative integer `\dim K_B^{(n)}` reaches zero in at
most `\dim Q_B` valid promotions.  If a needed promotion is not subraw, the
nonreconstructive bounded packet fails. `\square`

## 48. Finite-Difference Version

The Jacobian language is useful but not fundamental.  The record theory should
not rely on differentiability.

Define the finite packet separation seminorm:

$$
\boxed{
\|u\|_{\mathcal K,n}
=
\|J_B^{(n)}u\|_{\mathcal K}.
}
$$

The finite rank target is:

$$
\boxed{
\|u\|_{\mathcal K,n}=0
\quad\Longrightarrow\quad
u=0
\quad\text{in }Q_B.
}
$$

Equivalently, there exists a finite separation floor:

$$
\boxed{
\rho_B^{(n)}
=
\inf_{u\in Q_B,\ \|u\|_\lambda\ge\epsilon}
\|u\|_{\mathcal K,n}
>0.
}
$$

### 48.1 Theorem 37: Finite Separation Implies Packet Floors

If kernel promotion terminates with `K_B^{(n_\star)}=0`, then for every
above-tolerance primitive response:

$$
\boxed{
\|u\|_\lambda\ge\epsilon
\quad\Longrightarrow\quad
\|u\|_{\mathcal K,n_\star}\ge\rho_B>0.
}
$$

Thus the packet has channel floors without invoking a continuum derivative.

**Proof.**

At fixed `B,\lambda`, the response quotient and tolerated response classes are
finite.  If `J_B^{(n_\star)}` has zero kernel, the packet seminorm is positive
on every nonzero tolerated response class.  A positive minimum over a finite
set gives `\rho_B>0`. `\square`

### 48.2 Why This Matters

The Jacobian rank condition becomes the smooth/local approximation to a more
primitive finite statement:

$$
\boxed{
\text{no above-tolerance physical response is packet-silent.}
}
$$

This is exactly the no-silent diamond law, applied to packet channels.

## 49. Minimality and the Smallest Packet

The law should not add every possible channel.  It should add only what the
current unresolved boundary problem forces.

Define the admissible packet family:

$$
\boxed{
\mathfrak P_B(\lambda)
=
\{
\mathcal K:
\ker J_{\mathcal K}=0,\ 
C_B(\mathcal K)=o(C_{\rm raw}(B))
\}.
}
$$

The selected packet is:

$$
\boxed{
\mathcal K_B^\star
\in
\arg\min_{\mathcal K\in\mathfrak P_B(\lambda)}
\left[
C_B(\mathcal K)
+\zeta D_B(\mathcal K)
+\nu R_B(\mathcal K)
\right].
}
$$

Here:

- `C_B(\mathcal K)` is record-carrier cost;
- `D_B(\mathcal K)` is deletion/insertion drift;
- `R_B(\mathcal K)` is residual reconstruction exposure;
- `\zeta,\nu` are tolerance weights.

### 49.1 Theorem 38: Least Kernel Closure Is Minimal

If the cost functional is monotone under channel addition and strictly
penalizes raw reconstruction exposure, then the kernel-promotion fixed point
is a minimal admissible packet among packets generated by intrinsic signatures.

**Proof.**

Every admissible packet must kill every nonzero kernel direction.  If a
kernel direction first appears at stage `n`, any packet that omits all
channels detecting its signature leaves that direction silent and is not
admissible.  The promotion rule chooses the least-cost detecting signature.
By monotonicity, replacing it with a more expensive detecting channel cannot
lower the objective.  Iterating over the finite kernel chain gives minimality
within the intrinsic-signature closure class. `\square`

### 49.2 What Minimality Does Not Say

This does not prove that the selected packet is unique as a literal list of
symbols.  It proves uniqueness up to:

1. same-actual quotient;
2. invertible reparametrization of packet channels;
3. equal-cost degeneracy among equivalent intrinsic signatures.

That is enough.  The click law needs stable predictions, not a privileged
notation.

## 50. Physical Spacetime-Like Rank Theorem

We can now state the scoped theorem that replaces the loose rank assumption.

#### Theorem 39: Physical Packet Rank From Subraw Kernel Promotion

Let `B` be a completed bounded diamond at tolerance `\lambda`.  Assume:

1. `B` is physical in the sense of Section 19;
2. source completion is finite and subraw;
3. same-actual null directions are quotiented;
4. the finite spacetime packet is licensed at tolerance `\lambda`;
5. every non-same-actual packet-silent response has a record-intrinsic diamond
   signature;
6. kernel promotion by intrinsic signatures remains subraw.

Then the promoted packet:

$$
\boxed{
\mathcal K_B^\star
=
(\mathcal G_B,\mathcal T_B,\mathcal Y_B)^{\star}
}
$$

has full finite rank:

$$
\boxed{
\ker J_{\mathcal K_B^\star}=0
\quad\text{on }Q_B.
}
$$

Consequently the packet has finite channel floors and the intrinsic gap
follows:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

**Proof.**

By assumptions 3 and 5, any nonzero kernel direction is physical and has a
nonzero record-intrinsic signature.  By assumption 6, promoting that signature
is subraw.  The finite kernel-promotion dichotomy of Theorem 36 therefore
terminates in the first branch: full rank.  The finite-difference floor theorem
then gives packet floors.  Theorem 35 gives subraw response separation, and
Theorem 32 gives the intrinsic gap. `\square`

### 50.1 Meaning of the Theorem

The theorem does not say "spacetime packets always work."  It says:

$$
\boxed{
\text{if a bounded spacetime-like description is physically admissible, its
missing channels must close by subraw kernel promotion.}
}
$$

If they do not, the region is not licensed as a bounded spacetime/click panel
at that tolerance.

## 51. Hostile Rank Review

### Review O: "Kernel promotion is tautological."

Partly accepted.

The existence of some full-rank packet is trivial if raw reconstruction is
allowed.  The nontrivial content is:

$$
\boxed{
\text{full rank must be achieved by record-intrinsic, least, subraw channels.}
}
$$

That is exactly the boundary-law constraint.  A raw full-rank packet is not
admissible.

### Review P: "The signature map could smuggle hidden presentation counts."

Accepted as a danger.

The signature map is admissible only if its components are built from:

1. boundary incidence;
2. interval interiors and layer profiles;
3. deletion/insertion drift;
4. overlap/atlas consistency;
5. center-ledger masses;
6. typed source and target prints.

If a proposed signature requires naming hidden presentation paths, it is not
admissible.

### Review Q: "A kernel direction may require infinitely many soft channels."

Accepted.

Then the finite bounded law must use an inclusive typed channel.  If no
inclusive finite channel exists at tolerance `\lambda`, the experiment is not
closed.  This is not a mathematical embarrassment; it is the operational fact
that an unbounded infrared sector cannot be predicted by a finite panel without
an inclusive observable.

### Review R: "The theorem still assumes subraw kernel promotion."

Accepted.

This is now the correct remaining physical burden.  It is sharper than
"assume a spectral gap" because it identifies the only possible obstruction:

$$
\boxed{
\text{a non-same-actual response whose smallest record-intrinsic detector is
raw.}
}
$$

If such a response exists in a claimed bounded spacetime experiment, the
bounded experiment was misdrawn.

## 52. Updated Closure State

Paper XLI now has a stronger spine.

The intrinsic gap can be obtained by:

1. source completion plus compressed recurrence;
2. spacetime packet response separation;
3. regular packet rank plus typed dictionary;
4. subraw kernel promotion of all packet-silent non-same-actual responses.

The best current theorem is:

$$
\boxed{
\text{physical completed bounded diamonds with subraw intrinsic kernel
promotion have the packet rank condition and therefore the intrinsic gap.}
}
$$

This is the first version that avoids treating the packet Jacobian rank as a
bare assumption.  Rank is now generated by a law:

$$
\boxed{
\text{add the least record-intrinsic subraw detector of the current kernel,
or declare the bounded panel invalid.}
}
$$

### 52.1 Remaining Irreducible Target

The remaining irreducible target is:

$$
\boxed{
\text{prove subraw kernel promotion for physical bounded spacetime-like
diamonds, or exhibit a physical response whose least intrinsic detector is
raw.}
}
$$

This is narrower than the old target.  It is no longer "prove the gap."  It is
"prove that physical missing channels are finitely and intrinsically
detectable before raw reconstruction."

## 53. Subraw Kernel-Promotion Campaign

The target is:

$$
\boxed{
\text{prove every physical promoted kernel signature has subraw carrier cost.}
}
$$

The key observation is that a promoted kernel signature is not an arbitrary
new observable.  It is a residue of one of the primitive diamond interfaces:

$$
\boxed{
\Sigma_B(u)
=
(\partial,I,U,O,C,T).
}
$$

Therefore its carrier can be decomposed into the same finite objects already
used by source completion:

$$
\boxed{
\operatorname{car}(\Sigma_B(u))
\subseteq
\operatorname{car}_\partial
\cup
\operatorname{car}_I
\cup
\operatorname{car}_U
\cup
\operatorname{car}_O
\cup
\operatorname{car}_C
\cup
\operatorname{car}_T.
}
$$

If each carrier class is subraw, then every kernel promotion is subraw.

### 53.1 Carrier Cost Envelope

Let:

$$
\boxed{
n_\partial,\ n_I,\ n_U,\ n_O,\ n_C,\ n_T
}
$$

be the number of active boundary, interval, update, overlap, center, and typed
carrier atoms at tolerance `\lambda`.

Assume polynomial carrier envelopes:

$$
\boxed{
C_{\partial}\le a_\partial n_\partial^{d_\partial},
\quad
C_I\le a_I n_I^{d_I},
\quad
C_U\le a_U n_U^{d_U},
}
$$

$$
\boxed{
C_O\le a_O n_O^{d_O},
\quad
C_C\le a_C n_C^{d_C},
\quad
C_T\le a_T n_T^{d_T}.
}
$$

Then:

$$
\boxed{
C_B(\Sigma_B(u))
\le
\sum_{\xi\in\{\partial,I,U,O,C,T\}}
a_\xi n_\xi^{d_\xi}.
}
$$

Thus subraw promotion follows if:

$$
\boxed{
\sum_{\xi}
a_\xi n_\xi^{d_\xi}
=
o(C_{\rm raw}(B)).
}
$$

This is exactly the compressed-carrier form of subraw source completion.

### 53.2 Theorem 40: Carrier Envelope Gives Subraw Promotion

Assume:

1. every promoted kernel signature decomposes into the six diamond carrier
   classes above;
2. each carrier class has a finite polynomial envelope;
3. the total envelope is subraw relative to `C_{\rm raw}(B)`;
4. no promoted signature may use hidden presentation counts.

Then kernel promotion is subraw:

$$
\boxed{
C_B(L_{\sigma_n})=o(C_{\rm raw}(B))
}
$$

for every valid promoted channel.

**Proof.**

Each promoted channel is generated by a signature `\Sigma_B(u)`.  By
assumption 1, its carrier lies inside the finite union of the six carrier
classes.  By assumption 2, its cost is bounded by the displayed polynomial
envelope.  By assumption 3, that envelope is subraw.  Assumption 4 excludes
raw hidden-history encodings. `\square`

## 54. Why Physical Bounded Diamonds Should Satisfy the Envelope

The carrier envelope is not meant to be an arbitrary axiom.  It follows from
the meaning of a bounded experiment.

A bounded diamond at tolerance `\lambda` is drawn so that everything outside
the boundary is summarized by the boundary data to within the requested error.
If an outside or hidden component changes the target above tolerance, then it
is not outside the bounded problem.  It must be one of:

1. part of the boundary carrier;
2. part of the interval/update/overlap carrier;
3. a center-ledger mass;
4. a typed source or entanglement residue;
5. a reason to expand the boundary.

This gives the physical completion rule:

$$
\boxed{
\text{above-tolerance influence must be carried, typed, or boundary-expanding.}
}
$$

### 54.1 Theorem 41: Bounded Influence Implies Carrier Decomposition

Assume `B` is a physical bounded diamond at tolerance `\lambda` and target
family `\mathcal Y_B`.  Let `u` be a packet-silent non-same-actual response
that changes either:

1. the target family;
2. the finite spacetime packet;
3. the Ward/Bianchi residue;
4. the center ledger.

Then `u` has an intrinsic carrier decomposition into
`(\partial,I,U,O,C,T)`, unless `B` was not closed at tolerance `\lambda`.

**Proof.**

If `u` changes the target or packet above tolerance, boundedness says the
effect must cross the boundary, alter an interval/update/overlap relation,
change a committed center mass, or enter through a typed source/entanglement
residue.  These are precisely the six carrier classes.  If none of them
changes, then the response is invisible to every printed record channel and is
same-actual at the requested tolerance.  That contradicts that `u` is
non-same-actual and above tolerance.  Therefore either a carrier decomposition
exists or the boundary omitted an above-tolerance influence and was not
closed. `\square`

### 54.2 Corollary: Physical Closure Gives Subraw Kernel Promotion

If, in addition, the six carrier classes obey the subraw envelope of Section
53.1, then every packet-silent physical kernel direction promotes subrawly.

This closes the rank theorem for physical bounded diamonds whose boundary
really is a tolerance boundary.

## 55. Adversarial Promotions

### 55.1 Global Parity Adversary

Adversary:

$$
\boxed{
\text{the target depends on a global parity bit of the hidden history.}
}
$$

If the parity bit is record-intrinsic and affects the target above tolerance,
it must be printed as a typed topological/source channel:

$$
\boxed{
\tau_{\rm parity}\in\mathcal T_B.
}
$$

The bit itself can be subraw, but the verification path may be raw.  The
admission test is therefore:

$$
\boxed{
C_B(\tau_{\rm parity})=o(C_{\rm raw}(B)).
}
$$

If verifying the parity requires raw reconstruction, the bounded panel is not
closed for that target.  The click law then refuses the prediction rather than
silently hiding the parity.

### 55.2 Long Entanglement Adversary

Long shared record structure need not be metric-local.  It is admitted if it
has a finite typed carrier:

$$
\boxed{
\tau_{\rm ent}\in\mathcal T_B,
\qquad
C_B(\tau_{\rm ent})=o(C_{\rm raw}(B)).
}
$$

If it affects the target and has no finite typed carrier, the boundary must be
expanded.  This keeps Barandes-style indivisibility intact: the entanglement
is not a stochastic hidden variable; it is shared record structure whose
uncomputed residue becomes probabilistic only after projection.

### 55.3 Horizon or Black-Hole Adversary

Near horizons, the carrier envelope may fail because boundary response is
highly sensitive.  The theorem does not claim otherwise.

The admissibility test is:

$$
\boxed{
\text{expand }B\text{ until the horizon response is typed/carried below
tolerance, or decline spacetime closure.}
}
$$

### 55.4 Phase Boundary Adversary

At a phase transition, packet floors can vanish.  Then kernel promotion may
not reduce the kernel stably.  The correct output is:

$$
\boxed{
\rho_B=0
\quad\Longrightarrow\quad
\text{no stable bounded packet at this tolerance.}
}
$$

This is a feature, not a bug: the theory should not pretend a singular regime
has a regular finite spacetime packet.

## 56. Subraw Kernel-Promotion Theorem

We can now combine the pieces.

#### Theorem 42: Physical Closure Gives Subraw Kernel Promotion

Let `B` be a physical bounded diamond at tolerance `\lambda` for target family
`\mathcal Y_B`.  Assume:

1. above-tolerance influence is carried, typed, or boundary-expanding;
2. hidden presentation counts are inadmissible;
3. the six carrier classes `(\partial,I,U,O,C,T)` have finite polynomial
   envelopes;
4. the total carrier envelope is subraw:

   $$
   \boxed{
   \sum_{\xi}
   a_\xi n_\xi^{d_\xi}
   =
   o(C_{\rm raw}(B));
   }
   $$

5. inclusive typed compression exists for soft/infrared families relevant to
   the target.

Then every packet-silent non-same-actual physical response has a subraw
intrinsic promoted detector.  Therefore kernel promotion terminates subrawly,
the promoted packet has full finite rank, and:

$$
\boxed{
\gamma_{B,\lambda}>0.
}
$$

**Proof.**

Let `u` be a packet-silent non-same-actual physical response.  By physical
closure, any above-tolerance influence of `u` must be carried, typed, or force
boundary expansion.  Since `B` is assumed closed at tolerance, the boundary
expansion branch is absent.  Therefore `u` has a carrier decomposition by
Theorem 41.  The carrier envelope is subraw by assumptions 3 and 4, and
inclusive compression handles soft families by assumption 5.  The promoted
detector is therefore subraw by Theorem 40.  The finite kernel-promotion
dichotomy then terminates in the full-rank branch.  The packet-rank theorem
gives the intrinsic gap. `\square`

### 56.1 What Is Actually Proven

The theorem proves:

$$
\boxed{
\text{closed physical bounded diamond}
+\text{subraw carrier envelope}
\Longrightarrow
\text{intrinsic gap}.
}
$$

It does not prove that every arbitrary record region has a gap.  It proves
that once a region is genuinely closed as a bounded physical experiment, any
non-same-actual missing influence must be finitely detectable or the closure
claim fails.

## 57. Hostile Review of the Subraw Proof

### Review S: "You moved the hard part into physical closure."

Accepted, but this is progress.

The original hard part was an opaque spectral gap.  The new hard part is the
operational statement:

$$
\boxed{
\text{a bounded experiment must carry, type, or exclude every
above-tolerance influence.}
}
$$

That is exactly what a finite experiment means.

### Review T: "The carrier polynomial envelope is still a premise."

Accepted.

It is the next auditable condition.  It can be tested channel by channel:

1. boundary incidence;
2. interval/layer profiles;
3. deletion/insertion updates;
4. overlap/atlas consistency;
5. center ledgers;
6. typed source residues.

If one channel violates the envelope, the failure identifies the missing
physical scale.

### Review U: "What if the true detector is nonlocal but finite?"

Then it is a typed channel.  Nonlocality is not forbidden.  Raw hidden
reconstruction is forbidden.

### Review V: "What if the true detector is finite but changes with N?"

Then the projective recurrence must control its drift:

$$
\boxed{
\sum_{j\ge k}\Delta_{\tau,j}<\infty.
}
$$

If the drift is not summable, the bounded law is not stable across history
depths.

## 58. Paper XLI Closure After This Campaign

The intrinsic-gap target has now been reduced to explicit finite conditions.

The strongest result in Paper XLI is:

$$
\boxed{
\begin{gathered}
\text{physical closure}
+\text{subraw six-carrier envelope}
+\text{inclusive typed compression}
+\text{projective drift control}\\
\Longrightarrow
\text{subraw kernel promotion}
\Longrightarrow
\text{packet rank}
\Longrightarrow
\text{intrinsic gap}.
\end{gathered}
}
$$

This is not a slogan.  It is a dependency chain with named failure modes.

The remaining eight-target frontier is now narrower:

1. prove the six-carrier envelope for calibrated physical diamonds;
2. prove projective drift control for promoted typed channels;
3. prove the positive action remains coercive after promoted packet closure;
4. prove target probabilities from partial panels converge as history depth
   grows;
5. derive the finite spacetime packet from the promoted diamond carriers
   without continuum smuggling.

The next best target is therefore:

$$
\boxed{
\text{prove projective drift control for promoted carriers and typed
channels.}
}
$$

That target connects the gap proof back to the actual click law, because a
finite detector is not enough; it must remain stable when the bounded history
window changes.

## 59. Projective Drift for Promoted Channels

A promoted channel at depth `k` is written:

$$
\boxed{
L_{\sigma,k}:Q_{B,k}\to V_{\sigma,k}.
}
$$

The projection map:

$$
\boxed{
\pi_{k+1\to k}:Q_{B,k+1}\to Q_{B,k}
}
$$

forgets the oldest layer of the bounded history.  The promoted channel is
projectively stable if:

$$
\boxed{
L_{\sigma,k}\pi_{k+1\to k}
\approx
\rho_{k+1\to k}^{\sigma}L_{\sigma,k+1}
}
$$

where `\rho_{k+1\to k}^{\sigma}` is the induced projection on the channel
value space.

Define the channel drift:

$$
\boxed{
\Delta_{\sigma,k}
=
\left\|
L_{\sigma,k}\pi_{k+1\to k}
-
\rho_{k+1\to k}^{\sigma}L_{\sigma,k+1}
\right\|_\sigma.
}
$$

Projective drift control means:

$$
\boxed{
\sum_{j\ge k}\Delta_{\sigma,j}<\infty,
\qquad
\sum_{j\ge k}\Delta_{\sigma,j}\to0
\text{ as }k\to\infty.
}
$$

### 59.1 Drift Decomposition

Because every promoted signature decomposes into the six carrier classes:

$$
\boxed{
\Sigma_B=(\partial,I,U,O,C,T),
}
$$

its drift decomposes as:

$$
\boxed{
\Delta_{\sigma,k}
\le
\sum_{\xi\in\{\partial,I,U,O,C,T\}}
b_{\sigma,\xi}\Delta_{\xi,k}
+\epsilon_{\sigma,k}^{mix}.
}
$$

Here:

- `\Delta_{\xi,k}` is the drift of carrier class `\xi`;
- `b_{\sigma,\xi}` is the finite sensitivity of the promoted channel to that
  carrier;
- `\epsilon_{\sigma,k}^{mix}` is the mixing error from changing the carrier
  decomposition across depth.

### 59.2 Theorem 43: Carrier Drift Gives Promoted Drift

Assume:

1. each active carrier class has summable projective drift:

   $$
   \boxed{
   \sum_{j\ge k}\Delta_{\xi,j}<\infty;
   }
   $$

2. the sensitivities `b_{\sigma,\xi}` are finite for admitted promoted
   channels;
3. the mixing errors are summable:

   $$
   \boxed{
   \sum_{j\ge k}\epsilon_{\sigma,j}^{mix}<\infty.
   }
   $$

Then every admitted promoted channel has controlled projective drift:

$$
\boxed{
\sum_{j\ge k}\Delta_{\sigma,j}<\infty.
}
$$

**Proof.**

Sum the drift decomposition over `j\ge k`.  Finite sensitivities pull out of
the sums.  Carrier drift tails and mixing tails are summable by assumption.
Therefore the promoted-channel drift tail is summable. `\square`

## 60. Projective Promoted Packet

Let:

$$
\boxed{
\mathcal K_{B,k}^{\star}
}
$$

be the promoted packet at depth `k`.  Its total drift is:

$$
\boxed{
\Delta_{\mathcal K,k}
=
\Delta_{\mathcal G,k}
+\Delta_{\mathcal T,k}
+\Delta_{\mathcal Y,k}
+\sum_{\sigma\in\Sigma_k^\star}\Delta_{\sigma,k}.
}
$$

The promoted packet is projective if:

$$
\boxed{
\sum_{j\ge k}\Delta_{\mathcal K,j}<\infty.
}
$$

### 60.1 Theorem 44: Promoted Packet Projectivity

Assume:

1. the original packet `(\mathcal G,\mathcal T,\mathcal Y)` has controlled
   drift;
2. every promoted channel is generated by a six-carrier signature;
3. every active carrier class has summable drift;
4. promoted-channel mixing errors are summable;
5. the promoted dictionary remains subraw:

   $$
   \boxed{
   C(\Sigma_k^\star)=o(C_{\rm raw}(B)).
   }
   $$

Then the promoted packet has controlled projective drift:

$$
\boxed{
\sum_{j\ge k}\Delta_{\mathcal K,j}<\infty.
}
$$

**Proof.**

The base packet drift is summable by assumption 1.  Each promoted-channel
drift is summable by Theorem 43.  Subraw dictionary growth prevents the sum
over promoted channels from becoming raw or divergent.  Hence the total packet
drift is summable. `\square`

### 60.2 Hostile Review

**Objection:** a countable collection of summable channels can still have a
divergent total drift.

Accepted.  That is why assumption 5 is dictionary-level, not per-channel.  The
admitted promoted dictionary must satisfy both:

$$
\boxed{
C(\Sigma_k^\star)=o(C_{\rm raw}(B)),
\qquad
\sum_{\sigma\in\Sigma_k^\star}\sum_{j\ge k}\Delta_{\sigma,j}<\infty.
}
$$

Per-channel control is not enough.

## 61. Partial-Panel Probabilities

The theory is not probabilistic at the full bounded-history level.  It becomes
probabilistic when the observer computes only a partial panel.

Let:

$$
\boxed{
\mathcal P_{B,k}
}
$$

be the panel available at depth `k`.  For panel value `p` and target `Y`, define:

$$
\boxed{
\mathbb P_k(Y=y\mid p)
=
\frac{
\sum_{H\in H_{B,k}:\ \mathcal P_{B,k}(H)=p,\ Y(H)=y}
h_{B,k}(H)
}{
\sum_{H\in H_{B,k}:\ \mathcal P_{B,k}(H)=p}
h_{B,k}(H)
}.
}
$$

This is not primitive randomness.  It is the normalized residual of compatible
bounded histories after projecting to the panel actually computed.

### 61.1 Prediction Drift Bound

Let:

$$
\boxed{
E_{Y,k}
=
L_YT_k+C_Y\sum_{j\ge k}\Delta_{\mathcal K,j}
+C'_Y\epsilon_{proj,k}.
}
$$

where:

- `T_k` is the unresolved history tail after depth `k`;
- `\sum_{j\ge k}\Delta_{\mathcal K,j}` is promoted-packet drift;
- `\epsilon_{proj,k}` is untyped projective residue;
- `L_Y,C_Y,C'_Y` are finite target Lipschitz constants.

Then:

$$
\boxed{
d_{TV}
\left(
\mathbb P_j(Y\in\cdot\mid \pi_{j\to k}^{-1}p),
\mathbb P_k(Y\in\cdot\mid p)
\right)
\le
E_{Y,k}
}
$$

for all `j\ge k`, whenever the denominator weights are bounded away from zero
on the admissible panel cell.

### 61.2 Theorem 45: Partial Predictions Converge

Assume:

1. unresolved history tails vanish: `T_k\to0`;
2. promoted packet drift is summable;
3. untyped projective residue vanishes at tolerance:
   `\epsilon_{proj,k}\to0`;
4. target `Y` is Lipschitz in the promoted packet;
5. admissible panel cells have nonzero normalized weight.

Then the partial-panel predictions converge:

$$
\boxed{
\mathbb P_k(Y\in\cdot\mid p_k)
\to
\mathbb P_\infty(Y\in\cdot\mid p_\infty).
}
$$

**Proof.**

The prediction drift bound gives a Cauchy estimate.  The three error terms
vanish by assumptions 1--3.  Lipschitz target dependence transfers packet
convergence to target convergence.  Nonzero denominators prevent conditional
probabilities from becoming undefined. `\square`

### 61.3 Meaning

This is the formal version of the experimental story:

$$
\boxed{
\text{probability is the calibrated residual from using a partial bounded
panel rather than the full compatible history.}
}
$$

As the panel and history depth become sufficient for the target, the residual
probability stabilizes.

## 62. Coercivity After Promoted Closure

Promoting channels should not break the positive history weight.

The promoted action is:

$$
\boxed{
\mathcal A_{B}^{hist,\star}
=
\mathcal A_B^{hist}
+
\sum_{\sigma\in\Sigma^\star}
\omega_\sigma
\left[
\mu_\sigma\log\frac{\mu_\sigma}{\widehat\mu_\sigma(h)}
-\mu_\sigma
+\widehat\mu_\sigma(h)
\right]
+
\lambda_\sigma C_\sigma.
}
$$

The added RN/KL terms are convex in the predicted channel masses, and
`\lambda_\sigma C_\sigma` penalizes raw/reconstructive channels.

### 62.1 Theorem 46: Promotion Preserves Coercivity

Assume:

1. the pre-promotion action is coercive on the same-actual quotient;
2. promoted channels have positive weights `\omega_\sigma>0`;
3. promoted channel maps are finite and continuous on the response quotient;
4. raw/reconstructive promotions have infinite or dominating nonlookup cost;
5. the promoted dictionary is subraw.

Then the promoted action is coercive on the promoted admissible quotient.

**Proof.**

Adding nonnegative convex RN/KL terms cannot create an escape direction with
lower action.  Positive channel weights penalize deviations in newly detected
directions.  Raw directions hit the nonlookup cost and are inadmissible.
Subraw dictionary growth prevents the promoted action from becoming a raw
lookup table.  Therefore coercivity is preserved. `\square`

### 62.2 Consequence

The promoted packet does not merely detect missing channels.  It also leaves
the compatibility weight well-defined:

$$
\boxed{
h_B^\star(H)
=
\exp[-\mathcal A_B^{hist,\star}(H)].
}
$$

The law remains a positive bounded-history weight, not a primitive stochastic
transition rule.

## 63. Combined Projective Click-Law Theorem

#### Theorem 47: Promoted Physical Panel Gives Stable Partial Predictions

For a physical bounded diamond `B` at tolerance `\lambda`, assume:

1. physical closure and the subraw six-carrier envelope;
2. inclusive typed compression;
3. subraw kernel promotion;
4. promoted packet projective drift control;
5. promoted action coercivity;
6. target Lipschitzness and nonzero panel-cell weight.

Then:

1. the promoted packet has full finite rank;
2. the intrinsic gap is positive;
3. the positive history weight `h_B^\star` exists on the admissible quotient;
4. partial-panel probabilities converge with history depth:

   $$
   \boxed{
   \mathbb P_k(Y\in\cdot\mid p_k)
   \to
   \mathbb P_\infty(Y\in\cdot\mid p_\infty).
   }
   $$

**Proof.**

Subraw kernel promotion gives full packet rank by Theorem 39 and intrinsic gap
by Theorem 42.  Projective drift control gives a summable packet tail by
Theorem 44.  Coercivity gives a stable positive weight by Theorem 46.  The
partial-panel convergence theorem then applies. `\square`

## 64. Updated Campaign Status

Paper XLI has now pushed past the intrinsic-gap obstruction into the click-law
projection theorem.

The strongest current statement is:

$$
\boxed{
\begin{gathered}
\text{physical bounded closure}
+\text{subraw carrier envelope}
+\text{subraw promoted kernel closure}
+\text{summable projective drift}\\
+\text{promoted action coercivity}
\Longrightarrow
\text{stable positive history weight and convergent partial-panel
predictions.}
\end{gathered}
}
$$

The remaining nontrivial target is no longer a single gap theorem.  It is the
physical derivation of the premises:

1. six-carrier polynomial envelopes in calibrated diamonds;
2. dictionary-level summability for promoted typed channels;
3. finite target Lipschitz constants for realistic experiments;
4. intrinsic construction of the spacetime packet from the promoted carriers.

The next target should be the first item, because it supports all the others:

$$
\boxed{
\text{derive six-carrier polynomial envelopes from calibrated record
diamonds.}
}
$$

## 65. Six-Carrier Envelope Campaign

The phrase "calibrated diamond" must not mean "we secretly assumed a
manifold."  It means that the record diamond passes finite, record-intrinsic
growth and stability tests at tolerance `\lambda`.

Define the calibrated scale:

$$
\boxed{
s_B(\lambda)
=
|\partial_\lambda B|
+|\mathcal C_\lambda(B)|
+|\mathcal A_\lambda(B)|.
}
$$

Here:

- `|\partial_\lambda B|` is the boundary/collar carrier count;
- `|\mathcal C_\lambda(B)|` is the number of active center channels;
- `|\mathcal A_\lambda(B)|` is the number of active overlap/atlas atoms.

This is not volume of a continuum region.  It is the finite size of the
record-intrinsic control surface.

### 65.1 Calibration Conditions

A bounded diamond is **carrier-calibrated** at tolerance `\lambda` if:

1. boundary collars have finite doubling:

   $$
   \boxed{
   N_\partial(2r)\le D_\partial N_\partial(r);
   }
   $$

2. interval/layer profiles have finite resolution rank:

   $$
   \boxed{
   N_I(r,\lambda)\le D_I r^{d_I};
   }
   $$

3. deletion/insertion updates have bounded local degree:

   $$
   \boxed{
   \deg_U(B,\lambda)\le D_U;
   }
   $$

4. overlap/atlas nerves have bounded multiplicity:

   $$
   \boxed{
   m_O(B,\lambda)\le D_O;
   }
   $$

5. center channels are no-silent signatures of those finite interfaces;
6. typed sectors have finite inclusive rank for the target family.

These are all record tests.  None uses continuum coordinates.

## 66. Carrier Count Bounds

### 66.1 Boundary Carrier

Finite boundary doubling implies:

$$
\boxed{
n_\partial
\le
c_\partial s_B^{d_\partial}.
}
$$

This is the usual doubling-cover counting argument, but applied to boundary
collar records rather than metric balls in a continuum.

### 66.2 Interval Carrier

Interval carriers are determined by boundary-pair interiors and their layer
profiles.  If the number of distinguishable layer profiles at tolerance
`\lambda` has finite rank, then:

$$
\boxed{
n_I
\le
c_I s_B^{2d_\partial+d_I}.
}
$$

The factor `s_B^{2d_\partial}` counts boundary-pair choices up to the
calibrated cover.  The factor `s_B^{d_I}` counts the finite profile
resolution.

### 66.3 Update Carrier

If each carrier atom participates in at most `D_U` admissible local
deletion/insertion/update moves, then:

$$
\boxed{
n_U
\le
c_U D_U
\left(n_\partial+n_I+n_O+n_T\right).
}
$$

Thus `n_U` is polynomial whenever the other carriers are.

### 66.4 Overlap Carrier

If overlap multiplicity is bounded by `D_O`, the atlas/overlap nerve has:

$$
\boxed{
n_O
\le
c_O D_O s_B^{d_O}.
}
$$

The important point is multiplicity, not visual geometry.  If many
incompatible overlaps pile onto the same bounded region, the envelope fails.

### 66.5 Center Carrier

Centers are extracted from nonzero update/interface signatures, so:

$$
\boxed{
n_C
\le
c_C(n_\partial+n_I+n_U+n_O+n_T).
}
$$

No independent center explosion is allowed.  If centers proliferate beyond
the interface signatures, the ledger is smuggling hidden presentation data.

### 66.6 Typed Carrier

Typed sectors are admitted only through inclusive finite source classes:

$$
\boxed{
n_T
\le
c_T
\left(
r_\Theta+r_{\mathcal B}+r_{\mathcal M}+r_Y
\right)
s_B^{d_T}.
}
$$

Long entanglement can be included here, but only as a finite inclusive record
type at the requested tolerance.

## 67. Polynomial Envelope Theorem

#### Theorem 48: Carrier Calibration Gives Six-Carrier Polynomial Envelopes

If `B` is carrier-calibrated at tolerance `\lambda`, then there are finite
constants `A_\xi,d_\xi` such that:

$$
\boxed{
n_\xi\le A_\xi s_B^{d_\xi}
\qquad
\xi\in\{\partial,I,U,O,C,T\}.
}
$$

Consequently, if carrier costs are polynomial in carrier counts:

$$
\boxed{
C_\xi\le a_\xi n_\xi^{p_\xi},
}
$$

then:

$$
\boxed{
\sum_\xi C_\xi
\le
A s_B^d.
}
$$

If:

$$
\boxed{
s_B^d=o(C_{\rm raw}(B)),
}
$$

then the six-carrier envelope is subraw.

**Proof.**

Boundary, interval, overlap, and typed bounds are the calibration conditions
expanded into carrier counts.  The update carrier is bounded by bounded local
degree over already-counted carriers.  The center carrier is bounded by
interface signatures, so it cannot exceed a constant multiple of the active
interface carriers.  A finite sum of polynomial bounds is polynomial.  The
final displayed asymptotic is exactly subrawness. `\square`

### 67.1 What This Proves

This proves that the six-carrier envelope is not an independent spectral
assumption.  It follows from finite record-intrinsic calibration plus subraw
control-surface growth.

It also makes failure useful.  If the envelope fails, one of the calibration
tests fails:

1. boundary doubling fails;
2. interval profile rank fails;
3. update degree fails;
4. overlap multiplicity fails;
5. center extraction is not no-silent/interface-led;
6. typed source rank is not finite/inclusive.

## 68. Hostile Envelope Review

### Review W: "Finite doubling is manifoldlikeness in disguise."

Rejected as stated, accepted as a caution.

Finite doubling is weaker than manifoldlikeness.  Trees, fractals, and many
nonmanifold finite geometries can have controlled doubling on bounded scales.
The theorem does not say such a diamond is a smooth manifold.  It says only
that its carrier algebra is polynomially controlled.

Spacetime licensing still needs the GR packet defects to be small.

### Review X: "KR/staged orders may fake the counts."

Accepted.

That is why the envelope alone is not the click law.  The staged adversary
must also pass:

1. no-hidden-fiber overlap tests;
2. recursive interval heredity;
3. center-ledger extraction;
4. projective drift summability;
5. target sufficiency.

If it passes all of these, then it is not being rejected by this bounded
record law at that tolerance.

### Review Y: "Black-hole entropy can make boundary data huge."

Accepted.

Then `s_B(\lambda)` is huge.  The theorem still applies if the control surface
growth is subraw relative to the hidden history space.  If not, no bounded
nonreconstructive description is licensed at that tolerance.

### Review Z: "Global topology may not be polynomial in local carriers."

Accepted unless topology is typed.

A topology-changing or globally constrained response must enter either:

$$
\boxed{
\mathcal M_B
\quad\text{or}\quad
\mathcal T_B.
}
$$

If it cannot be typed or atlas-visible subrawly, the bounded panel is not
closed.

## 69. Envelope Closure Result

Combining Theorem 48 with Theorem 42 gives:

#### Theorem 49: Calibrated Physical Diamonds Have Subraw Kernel Promotion

Let `B` be a physical bounded diamond at tolerance `\lambda`.  Assume:

1. `B` is carrier-calibrated;
2. the control-surface growth is subraw:

   $$
   \boxed{
   s_B^d=o(C_{\rm raw}(B));
   }
   $$

3. typed soft/infrared/topological sectors admit finite inclusive compression;
4. above-tolerance influence is carried, typed, or boundary-expanding;
5. `B` is closed, so the boundary-expanding branch is absent.

Then:

$$
\boxed{
\text{subraw kernel promotion holds for }B.
}
$$

Therefore the promoted packet has full rank and the intrinsic gap follows.

**Proof.**

Carrier calibration gives the six-carrier polynomial envelope by Theorem 48.
Subraw control-surface growth makes the envelope subraw.  Physical closure and
inclusive typed compression give the hypotheses of Theorem 42.  Therefore
kernel promotion is subraw, packet rank holds, and the intrinsic gap follows.
`\square`

### 69.1 New Status

The intrinsic gap is now proven for a scoped but physically meaningful class:

$$
\boxed{
\text{closed, carrier-calibrated, subraw-control-surface bounded diamonds.}
}
$$

The next issue is not the gap.  It is whether the spacetime packet itself can
be derived from these same promoted carriers.

## 70. Spacetime Packet From Promoted Carriers

The packet must be derived, not imported.  Define the promoted carrier algebra:

$$
\boxed{
\mathscr C_B^\star
=
(\partial^\star,I^\star,U^\star,O^\star,C^\star,T^\star).
}
$$

The finite spacetime packet is a record-intrinsic functional:

$$
\boxed{
I_{\rm GR}(H_{B,k})
=
\Phi_{\rm GR}(\mathscr C_{B,k}^\star).
}
$$

The packet components are:

$$
\boxed{
I_{\rm GR}
=
\left(
d_B,\ell_B,V_B,\mathcal R_B,\mathcal B_B,
\mathcal M_B,\Theta_B,\mathcal Y_B
\right).
}
$$

They mean:

- `d_B`: effective dimension/readout rank;
- `\ell_B`: boundary/collar scale profile;
- `V_B`: interval volume/profile data;
- `\mathcal R_B`: finite curvature/update-response packet;
- `\mathcal B_B`: Ward/Bianchi residue;
- `\mathcal M_B`: atlas/manifold defect;
- `\Theta_B`: typed source/stress packet;
- `\mathcal Y_B`: target click channels.

None of these is a continuum object yet.  They are finite carrier summaries.

### 70.1 Packet Extraction Rules

The extraction map is:

$$
\boxed{
\Phi_{\rm GR}
=
\left(
\Phi_d,\Phi_\ell,\Phi_V,\Phi_{\mathcal R},
\Phi_{\mathcal B},\Phi_{\mathcal M},\Phi_\Theta,\Phi_Y
\right).
}
$$

with:

| packet component | carrier source |
|---|---|
| `d_B` | interval scaling and boundary doubling |
| `\ell_B` | boundary/collar carrier |
| `V_B` | interval/layer carrier |
| `\mathcal R_B` | update drift and center response |
| `\mathcal B_B` | projective Ward/Bianchi residue |
| `\mathcal M_B` | overlap/atlas nerve consistency |
| `\Theta_B` | center plus typed source carrier |
| `\mathcal Y_B` | printed target channel |

This table is the finite version of "geometry from records."

## 71. Intrinsic GR Distance and Drift

Define the finite GR packet distance:

$$
\boxed{
d_{\rm GR}(P,P')
=
\sum_{\eta\in I_{\rm GR}}
w_\eta
\left\|
P_\eta-P'_\eta
\right\|_\eta.
}
$$

Here:

- `P,P'` are two finite GR packets;
- `\eta` ranges over packet components;
- `w_\eta` are tolerance weights;
- `\|\cdot\|_\eta` are carrier-intrinsic norms.

The GR drift across history depth is:

$$
\boxed{
\Delta^{\rm GR}_{B,k}
=
d_{\rm GR}
\left(
\Phi_{\rm GR}(\mathscr C_{B,k}^\star),
\rho_{k+1\to k}^{\rm GR}
\Phi_{\rm GR}(\mathscr C_{B,k+1}^\star)
\right).
}
$$

The manifold/atlas defect is:

$$
\boxed{
M_B(k)
=
\|\mathcal M_B(k)\|
+\|\mathcal B_B(k)\|
+\operatorname{Var}_k(d_B,V_B,\ell_B).
}
$$

This says: a spacetime readout is stable only if overlap defects, Ward/Bianchi
residues, and scale/profile variations are small.

## 72. Packet Derivation Theorem

#### Theorem 50: Promoted Carriers Define a Finite GR Packet

Assume:

1. the promoted carrier algebra `\mathscr C_B^\star` is finite and subraw;
2. each packet extraction map `\Phi_\eta` uses only carrier-intrinsic
   functions;
3. typed source channels are inclusive and finite;
4. target channels are printed.

Then `I_{\rm GR}(H_{B,k})` is a finite record-intrinsic packet.  It is
invariant under same-actual quotienting and does not use continuum
coordinates.

**Proof.**

Each component of `\Phi_{\rm GR}` is a finite function of finite promoted
carrier data.  Same-actual changes are quotiented before the carrier algebra
is formed, so the packet is invariant under them.  Since all carrier sources
are record-intrinsic, no continuum data or hidden presentation counts enter.
`\square`

### 72.1 What This Does Not Derive

This does not derive Newton's constant as a number.  It derives a finite GR
packet up to whatever calibration constants are actually printed by the
bounded records.

The old no-go remains:

$$
\boxed{
\text{absolute }G_\infty\text{ cannot be obtained from order/record ratios
alone without a scale calibration.}
}
$$

But the packet can still define stable dimension, scale, curvature residue,
source response, and manifold defect.

## 73. Spacetime Licensing From Carrier Packets

A promoted carrier packet licenses spacetime at tolerance `\epsilon_{\rm GR}`
when:

$$
\boxed{
\mathcal E^{\rm GR}_{B,k}
=
M_B(k)
+\sum_{j\ge k}\Delta^{\rm GR}_{B,j}
+\mathcal W^{\rm Ward}_{B,k}
+\mathcal S^{source}_{B,k}
\le
\epsilon_{\rm GR}.
}
$$

Here:

- `M_B(k)` is manifold/atlas defect;
- `\sum_{j\ge k}\Delta^{\rm GR}_{B,j}` is GR packet drift;
- `\mathcal W^{\rm Ward}_{B,k}` is untyped Ward/Bianchi residue;
- `\mathcal S^{source}_{B,k}` is unresolved source residue.

### 73.1 Theorem 51: Carrier Stability Gives GR Packet Stability

Assume:

1. promoted carrier drift is summable;
2. extraction maps `\Phi_\eta` are Lipschitz in carrier norms;
3. Ward/Bianchi and source residues are typed or below tolerance;
4. manifold/atlas defect is below tolerance.

Then:

$$
\boxed{
\mathcal E^{\rm GR}_{B,k}\le\epsilon_{\rm GR}
}
$$

for sufficiently deep bounded histories `k`, and the GR packet has a stable
limit.

**Proof.**

Lipschitz extraction transfers summable carrier drift to summable GR packet
drift.  Typed or below-tolerance residues bound the Ward/source terms.
The atlas defect bound controls `M_B(k)`.  Therefore the total GR error is
below tolerance for sufficiently deep `k`. `\square`

## 74. Spacetime Onset and Click Law Reunified

The click law and spacetime readout are now selected from the same promoted
carrier algebra.

The click panel is licensed when:

$$
\boxed{
\mathcal E^{click}_{B,k}
=
D_Y(B,k,\lambda)
+\sum_{j\ge k}\Delta_{\mathcal K,j}
\le
\epsilon_Y.
}
$$

The spacetime packet is licensed when:

$$
\boxed{
\mathcal E^{\rm GR}_{B,k}\le\epsilon_{\rm GR}.
}
$$

The same bounded history can have clicks before spacetime if:

$$
\boxed{
\mathcal E^{click}_{B,k}\le\epsilon_Y
\quad\text{but}\quad
\mathcal E^{\rm GR}_{B,k}>\epsilon_{\rm GR}.
}
$$

This is the pre-spacetime phase: records can click before the carrier algebra
has stabilized into a spacetime-like packet.

### 74.1 Theorem 52: Same Carrier Algebra Controls Click and Spacetime Onset

Assume the promoted carrier algebra is finite, subraw, projective, and
coercive.  Then:

1. target-click predictions are determined by projected `h_B^\star`;
2. spacetime is licensed exactly when the GR packet error is below tolerance;
3. both errors are functions of the same promoted carrier algebra
   `\mathscr C_B^\star`.

**Proof.**

Click predictions use `h_B^\star`, whose action is built from the promoted
carrier algebra.  The GR packet is `\Phi_{\rm GR}(\mathscr C_B^\star)`.  Thus
both error functionals are carrier functionals.  The click and spacetime
criteria can differ in tolerance and component weights, but not in their
underlying record source. `\square`

## 75. Final Paper XLI Status

Paper XLI has now connected the eight targets into one scoped theorem chain:

$$
\boxed{
\begin{gathered}
\text{closed carrier-calibrated bounded diamond}\\
\Longrightarrow
\text{subraw kernel promotion}
\Longrightarrow
\text{packet rank and intrinsic gap}\\
\Longrightarrow
\text{stable positive history weight}\\
\Longrightarrow
\text{convergent partial-panel click probabilities}\\
\Longrightarrow
\text{finite GR packet when GR error is below tolerance.}
\end{gathered}
}
$$

The big result is not "we solved everything unconditionally."  The result is
that the problem has been compressed to a finite operational core:

$$
\boxed{
\text{carry, type, or expand every above-tolerance influence; then minimize
the resulting boundary-work history action.}
}
$$

The remaining truly hard mathematical work is:

1. prove carrier calibration for broad physical families rather than assuming
   it at a region;
2. identify realistic inclusive typed sectors for QFT-like soft and
   entanglement residues;
3. prove the extraction maps `\Phi_{\rm GR}` have the required Lipschitz
   constants in calibrated regimes;
4. connect the finite packet limit to continuum Einstein/QFT equations where
   the GR packet error tends to zero.

## 76. Long Campaign: Projective Histories, Not Markov States

The next campaign must stay aligned with the indivisible-events/ISP lesson:

$$
\boxed{
\text{the primitive object is a bounded history cylinder, not a one-step
transition }P(W_{N+1}\mid W_N).
}
}
$$

For a bounded diamond `B`, target family `Y`, tolerance `\lambda`, and history
depth `k`, define the bounded history cylinder:

$$
\boxed{
\mathcal H_{B,k}
=
\{H:\ H\text{ is a compatible record history visible from depth }k\}.
}
$$

Depth projections are:

$$
\boxed{
\pi_{j\to k}:\mathcal H_{B,j}\to\mathcal H_{B,k},
\qquad j\ge k.
}
$$

The positive history weights are:

$$
\boxed{
h_{B,k}(H)
=
\exp[-\mathcal A_{B,k}^{hist}(H)].
}
$$

Projective compatibility means:

$$
\boxed{
(\pi_{k+1\to k})_\#h_{B,k+1}
\propto
h_{B,k}
}
$$

up to typed flux and controlled tolerance residue.

### 76.1 Effective Kernels Are Shadows

For a finite observed panel:

$$
\boxed{
O_k:\mathcal H_{B,k}\to\mathcal O_k,
}
$$

the effective stochastic prediction is:

$$
\boxed{
K_{O,k}(y\mid o)
=
\frac{
\sum_{H:\ O_k(H)=o,\ Y(H)=y}h_{B,k}(H)
}{
\sum_{H:\ O_k(H)=o}h_{B,k}(H)
}.
}
$$

This is a projection of an indivisible history weight.  It is not a primitive
Markov transition.

#### Theorem 53: Projective History Law Generates Effective Stochastic Kernels

If `h_{B,k}` is projectively compatible and `O_k` is a finite panel, then every
kernel `K_{O,k}` is a normalized marginal of the bounded history cylinder.
Moreover, if:

$$
\boxed{
\sum_{j\ge k}
d_{TV}
\left(
(\pi_{j+1\to j})_\#\bar h_{B,j+1},\bar h_{B,j}
\right)
<\infty,
}
$$

then the finite-panel kernels converge as `k` grows.

**Proof.**

The formula for `K_{O,k}` is exactly conditional normalization of the positive
history weight on the fiber `O_k^{-1}(o)`.  Projective compatibility controls
the difference between the depth-`j+1` and depth-`j` normalized marginals.  A
summable total-variation tail gives a Cauchy sequence of finite-panel
conditional kernels. `\square`

### 76.2 Barandes Alignment

The campaign therefore forbids:

$$
\boxed{
\text{derive the law as }P(W_{N+1}\mid W_N)\text{ on present states.}
}
$$

The allowed statement is:

$$
\boxed{
\text{derive a projective family }h_{B,k}\text{ on compatible bounded
histories, then project it to the panel actually computed.}
}
$$

That is the non-Markovian alignment.

## 77. Physical Bounded Families

Carrier calibration should be proved for families, not isolated finite
diamonds.

Define a physical bounded family:

$$
\boxed{
\mathbf B
=
\{(B_k,\mathcal H_{B,k},\pi_{k+1\to k},Y,\lambda)\}_{k\ge k_0}.
}
$$

Here:

- `B_k` is the bounded record diamond at history depth `k`;
- `\mathcal H_{B,k}` is the compatible history cylinder;
- `\pi_{k+1\to k}` forgets the oldest retained bounded layer;
- `Y` is the target family;
- `\lambda` is the tolerance.

The family is **closed at tolerance** when every above-tolerance influence on
`Y` is:

$$
\boxed{
\text{carried, typed, or boundary-expanding.}
}
$$

It is **physically bounded** when the boundary-expanding branch has stopped for
the requested tolerance.

### 77.1 History Requirement Formula

Define the required history depth:

$$
\boxed{
k_B(Y,\epsilon)
=
\inf
\left\{
k:\ 
D_Y(B,k,\lambda)
+\sum_{j\ge k}\Delta_{\mathcal K,j}
\le\epsilon
\right\}.
}
$$

This is the formula replacing brute-force "try more histories."  It says:
include older history until target diameter plus projective drift is below the
requested tolerance.

If `k_B(Y,\epsilon)<\infty`, the target is bounded-history predictable.  If
not, the target is not closed by a finite bounded panel at that tolerance.

## 78. Calibration From Finite Influence Packing

The six-carrier envelope needs a physical reason.  The proposed reason is
finite influence packing.

For each carrier class:

$$
\boxed{
\xi\in\{\partial,I,U,O,C,T\},
}
$$

define an above-tolerance influence atom as a minimal carrier atom whose
removal changes `Y`, `I_{\rm GR}`, or the center ledger above tolerance.

Let:

$$
\boxed{
P_\xi(B,r,\lambda)
}
$$

be the maximal number of pairwise distinguishable above-tolerance `\xi` atoms
inside a carrier ball of record radius `r`.

Finite influence packing is:

$$
\boxed{
P_\xi(B,r,\lambda)\le A_\xi r^{d_\xi}.
}
$$

This is not manifoldlikeness.  It is the statement that a bounded experiment
cannot contain exponentially many independently target-relevant influence
atoms in a bounded carrier neighborhood.

#### Theorem 54: Finite Influence Packing Implies Carrier Calibration

If every carrier class has finite influence packing and carrier balls cover
the control surface with finite overlap, then `B` is carrier-calibrated:

$$
\boxed{
n_\xi\le A'_\xi s_B^{d'_\xi}
\qquad
\xi\in\{\partial,I,U,O,C,T\}.
}
$$

**Proof.**

Cover the control surface by finitely overlapping carrier balls.  In each ball
the number of distinguishable above-tolerance carrier atoms is bounded by
finite influence packing.  Summing over the cover gives a polynomial envelope
in the control-surface size. `\square`

### 78.1 Opening: What If Packing Fails?

If packing fails, there are exponentially many independently target-relevant
carrier atoms inside the bounded region.  Then one of two things is true:

1. the target was too fine for the boundary/tolerance;
2. the bounded region is not physically closed without raw reconstruction.

This is a real obstruction, not a notation problem.

## 79. Typed Sectors as Inclusive Equivalence Classes

A typed sector is not a hidden variable.  It is an inclusive equivalence class
of record-history residues that have the same effect on the computed panel.

For residue `r`, define:

$$
\boxed{
r\sim_{B,Y,\lambda}r'
\quad\Longleftrightarrow\quad
\|Y(r)-Y(r')\|+\|I_{\rm GR}(r)-I_{\rm GR}(r')\|\le\lambda.
}
$$

The typed dictionary is:

$$
\boxed{
\mathcal T_{B,\lambda}
=
\{[r]_{B,Y,\lambda}:\ r\text{ affects }Y\text{ or }I_{\rm GR}
\text{ above tolerance}\}.
}
$$

#### Theorem 55: Inclusive Typing Is the Least Non-Markov Compression

Among record-intrinsic compressions that preserve target and GR packet values
to tolerance `\lambda`, the quotient by `\sim_{B,Y,\lambda}` is the coarsest
typed dictionary.

**Proof.**

Any admissible compression must identify only residues whose target and packet
effects differ by at most tolerance.  The relation `\sim_{B,Y,\lambda}`
identifies exactly all such residues.  Therefore any other admissible
compression factors through this quotient. `\square`

### 79.1 Soft/QFT and Long Entanglement

Soft sectors, long entanglement, and topological residues are admitted only
through their inclusive class:

$$
\boxed{
\tau=[r]_{B,Y,\lambda}.
}
$$

If the number or carrier cost of these inclusive classes is subraw, the sector
is compatible with the bounded law.  If not, the boundary must expand or the
target must be weakened.

## 80. Drift From the Intrinsic Gap

Projective drift control should not be an unrelated axiom.  Once the promoted
packet has an intrinsic gap, older-history influence should contract unless a
typed residue carries it.

Let `v_j` be the unresolved response added by history layer `j`.  The intrinsic
gap gives:

$$
\boxed{
\|v_{j+1}\|_{\mathcal K}
\le
\theta\|v_j\|_{\mathcal K}
+\eta_j,
\qquad
0\le\theta<1.
}
$$

where `\eta_j` is printed typed residue or boundary-expansion error.

If:

$$
\boxed{
\sum_{j\ge k}\eta_j<\infty,
}
$$

then:

$$
\boxed{
\sum_{j\ge k}\|v_j\|_{\mathcal K}<\infty.
}
$$

#### Theorem 56: Intrinsic Gap Gives Projective Carrier Drift

Assume:

1. the promoted packet has intrinsic gap `\gamma_{B,\lambda}>0`;
2. untyped older-history residue contracts with factor `\theta<1`;
3. typed residue tail is summable;
4. boundary-expansion residue is absent because `B` is closed.

Then all promoted carrier drift tails are summable.

**Proof.**

The recurrence above gives a geometric bound plus a summable forcing term.
Summing the geometric series and the typed residue tail gives finite total
drift.  Closure removes the boundary-expansion branch. `\square`

### 80.1 Circularity Check

This uses the intrinsic gap to prove drift, while earlier drift helped prove
stable prediction.  The circle is broken by sequence:

$$
\boxed{
\text{carrier calibration}
\Rightarrow
\text{subraw kernel promotion}
\Rightarrow
\text{intrinsic gap}
\Rightarrow
\text{projective drift}
\Rightarrow
\text{stable prediction}.
}
$$

So drift is downstream of the gap, not an independent gap premise.

## 81. Lipschitz Extraction From Finite Rational Packets

The GR extraction maps must be controlled.

Most packet components are finite ratios or finite normalized profiles:

$$
\boxed{
\Phi_\eta(x)
=
\frac{A_\eta x}{B_\eta x}
}
$$

or finite histograms:

$$
\boxed{
\Phi_\eta(x)
=
N_\eta x.
}
$$

where `x` is the promoted carrier vector.

If denominator floors hold:

$$
\boxed{
B_\eta x\ge b_\eta>0,
}
$$

then rational packet components are Lipschitz on the tolerated carrier set.

#### Theorem 57: Denominator Floors Give GR Extraction Lipschitzness

Assume every rational packet component has a positive denominator floor and
every histogram component has finite operator norm.  Then:

$$
\boxed{
d_{\rm GR}
\left(
\Phi_{\rm GR}(x),\Phi_{\rm GR}(x')
\right)
\le
L_{\rm GR}\|x-x'\|_{\mathscr C}
}
$$

for carrier vectors in the calibrated tolerance domain.

**Proof.**

Finite linear maps are Lipschitz.  A ratio of finite linear maps is Lipschitz
on any domain where the denominator is bounded away from zero.  The packet is
a finite product/sum of such components, so the weighted packet distance is
Lipschitz. `\square`

### 81.1 Opening: Vanishing Denominators

If a denominator vanishes, the packet component is not licensed.  The response
is either pre-spacetime, boundary-degenerate, or requires a different packet
component.

This matches the earlier horizon/phase-boundary adversaries.

## 82. Continuum Onset, Without Continuum Smuggling

Only after finite packet stability is proven can we ask about continuum
limits.

Let:

$$
\boxed{
\mathbf B_n=(B_n,\mathcal H_{B_n,k_n},h_{B_n,k_n}^\star)
}
$$

be a sequence of closed carrier-calibrated bounded diamonds.  It is
GR-calibrating if:

$$
\boxed{
\mathcal E^{\rm GR}_{B_n,k_n}\to0.
}
$$

It is click-calibrating for target `Y` if:

$$
\boxed{
\mathcal E^{click}_{B_n,k_n}\to0.
}
$$

#### Theorem 58: Finite Packets Have a Continuum Candidate Only After GR Error Vanishes

If `\mathbf B_n` is GR-calibrating and the finite packet observables are tight
in their carrier norms, then there is a subsequential limiting packet
functional:

$$
\boxed{
I_{\rm GR}^{(\infty)}
=
\lim_{m\to\infty}I_{\rm GR}(H_{B_{n_m},k_{n_m}}).
}
$$

This limit is a continuum candidate only if its Ward/Bianchi, atlas, source,
and curvature/update residues vanish in the packet topology.

**Proof.**

Tightness gives a convergent subsequence in the packet topology.  GR
calibration sends the packet defects to zero along the sequence.  Therefore
the limit satisfies the zero-defect packet equations.  Interpreting those as a
continuum geometry requires an external representation theorem, not assumed
here. `\square`

### 82.1 What Remains for Einstein/QFT

The finite theory can produce a zero-defect limiting packet.  To identify it
with continuum Einstein/QFT, one still needs:

1. a representation theorem from zero-defect packets to Lorentzian geometry;
2. a calibration of absolute scale, including Newton's constant;
3. a field/operator representation for typed source sectors.

Those are downstream from the click law, not inputs to it.

## 83. Full Adversarial Campaign

### 83.1 One-Step Markov Adversary

Claim: the law should be `P(W_{N+1}\mid W_N)`.

Rejected.

Finite kernels are shadows:

$$
\boxed{
P_{\rm eff}(Y\mid O_k)
=
\operatorname{Proj}_{O_k,Y}(h_{B,k}).
}
$$

The primitive object is `h_{B,k}` on histories.  A Markov-looking kernel is
allowed only when the chosen panel is sufficient.

### 83.2 Full-History Spoof

Claim: use the full hidden history; prediction becomes exact.

Rejected by nonlookup:

$$
\boxed{
C_{\rm full}(B)\ge C_{\rm raw}(B)
\quad\Rightarrow\quad
\text{inadmissible.}
}
$$

The law seeks the least sufficient quotient, not omniscience.

### 83.3 Staged/KR Order Spoof

Claim: staged orders can pass local counts.

Accepted as a live adversary.

They must also pass recursive interval heredity, no-hidden-fiber overlap,
projective drift, and target sufficiency.  If they pass all of these, the
bounded law at that tolerance cannot reject them.  If not, the failing channel
becomes a promoted detector.

### 83.4 Global Parity Spoof

Claim: a global bit affects the target but has no local carrier.

If the bit is above tolerance, it must be typed.  If typing it is raw, the
bounded experiment is not closed for that target.

### 83.5 Horizon/Phase Boundary Spoof

Claim: carrier calibration fails near singular or critical regimes.

Accepted.

Then spacetime licensing fails at that tolerance, while click prediction may
still survive if the click panel error is small.

### 83.6 Infinite Soft Sector Spoof

Claim: QFT soft sectors create infinitely many histories.

Accepted unless inclusive typing works.  The bounded law predicts inclusive
observables, not every soft microhistory.

## 84. Consolidated Long-Campaign Theorem

#### Theorem 59: Non-Markov Carrier-Calibrated History Law

Let `\mathbf B` be a physically bounded family at tolerance `\lambda` and
target family `Y`.  Assume:

1. finite influence packing for the six carrier classes;
2. finite overlap of carrier covers;
3. inclusive typed sectors for all above-tolerance nonlocal/soft/topological
   residues;
4. no hidden presentation counts;
5. physical closure: every above-tolerance influence is carried, typed, or
   boundary-expanding, and the boundary-expanding branch is absent;
6. promoted action coercivity;
7. denominator floors for packet extraction.

Then:

$$
\boxed{
\begin{gathered}
\text{the family admits a projective non-Markov bounded-history law }h_{B,k}^\star,\\
\text{its finite-panel probabilities converge,}\\
\text{and its GR packet is licensed exactly when }\mathcal E^{\rm GR}_{B,k}
\le\epsilon_{\rm GR}.
\end{gathered}
}
$$

**Proof.**

Finite influence packing and finite cover overlap imply carrier calibration by
Theorem 54.  Carrier calibration gives the six-carrier envelope by Theorem 48.
Physical closure and inclusive typing give subraw kernel promotion by Theorem
49.  Subraw kernel promotion gives packet rank and intrinsic gap.  The gap
gives projective carrier drift by Theorem 56.  Coercivity gives the positive
history weight.  The projective history theorem gives convergent finite-panel
probabilities.  Denominator floors give Lipschitz GR extraction, so GR
licensing is exactly the finite packet error condition. `\square`

## 85. What This Campaign Actually Closed

This campaign did not prove that every possible universe-like record set is
carrier-calibrated.  It proved a stronger scoped statement:

$$
\boxed{
\text{if a bounded experiment is physically closed and has finite influence
packing, then the non-Markov history law is well-defined and predictive.}
}
$$

The live irreducible targets are now:

1. prove finite influence packing for physically realistic bounded diamonds;
2. build inclusive typed sectors for QFT-like soft/entangled residues;
3. prove representation theorems from zero-defect finite packets to continuum
   spacetime/fields;
4. calibrate absolute scales such as `G_\infty` from additional record data.

The real next enemy is finite influence packing.  It is the cleanest remaining
place where the theory could fail or become genuinely physical.

## 86. Finite Influence Packing Campaign

The target is now:

$$
\boxed{
\text{prove finite influence packing from boundary-work principles.}
}
$$

An influence atom `a` of carrier type `\xi` has response:

$$
\boxed{
r_\xi(a)
=
\left(
\delta_Y(a),
\delta_{\rm GR}(a),
\delta_C(a)
\right).
}
$$

It is above tolerance if:

$$
\boxed{
\|r_\xi(a)\|_\lambda>\epsilon_\xi.
}
$$

Two atoms are distinguishable if their response difference is above tolerance:

$$
\boxed{
\|r_\xi(a)-r_\xi(b)\|_\lambda>\epsilon_\xi.
}
$$

Finite influence packing says that a bounded carrier neighborhood cannot
contain too many pairwise distinguishable above-tolerance atoms.

## 87. Boundary-Work Packing

The key physical principle is:

$$
\boxed{
\text{an independently distinguishable above-tolerance influence must pay a
minimum boundary-work quantum.}
}
$$

Let `q_{\xi,\lambda}>0` be the minimum committed work required to print an
above-tolerance carrier-`\xi` response:

$$
\boxed{
W_\xi(a)\ge q_{\xi,\lambda}
\quad
\text{whenever}\quad
\|r_\xi(a)\|_\lambda>\epsilon_\xi.
}
$$

Let the total available boundary work in a record ball of radius `r` be:

$$
\boxed{
\mathcal W_\xi(B,r,\lambda)
\le
A_\xi r^{d_\xi}.
}
$$

Then:

$$
\boxed{
P_\xi(B,r,\lambda)
\le
\frac{A_\xi}{q_{\xi,\lambda}}r^{d_\xi}.
}
$$

### 87.1 Theorem 60: Boundary-Work Budget Implies Finite Influence Packing

Assume:

1. every distinguishable above-tolerance influence atom has work at least
   `q_{\xi,\lambda}>0`;
2. work is nonnegative and additive over independent distinguishable atoms,
   modulo same-actual quotient;
3. the total available boundary work in carrier balls obeys
   `\mathcal W_\xi(B,r,\lambda)\le A_\xi r^{d_\xi}`.

Then finite influence packing holds:

$$
\boxed{
P_\xi(B,r,\lambda)
\le
\frac{A_\xi}{q_{\xi,\lambda}}r^{d_\xi}.
}
$$

**Proof.**

Let `a_1,\ldots,a_m` be pairwise distinguishable above-tolerance atoms.  By
the work quantum, each costs at least `q_{\xi,\lambda}`.  By additivity over
independent distinguishable atoms:

$$
\boxed{
mq_{\xi,\lambda}
\le
\sum_{i=1}^mW_\xi(a_i)
\le
\mathcal W_\xi(B,r,\lambda)
\le
A_\xi r^{d_\xi}.
}
$$

Thus `m\le A_\xi r^{d_\xi}/q_{\xi,\lambda}`. `\square`

### 87.2 Why the Work Quantum Is Reasonable

An atom below the work quantum cannot be distinguished above tolerance by the
printed panel.  If it could, the panel would have an above-tolerance response
with zero committed work, i.e. a silent influence.  That violates the no-silent
law.

Thus:

$$
\boxed{
\text{no-silent response}
\Rightarrow
\text{positive work quantum for above-tolerance distinguishability.}
}
$$

## 88. Non-Markov History Packing

Influence atoms can live across older history layers.  They are not forced to
be functions of the present panel.

Let:

$$
\boxed{
a=(a_j)_{j\ge k}
}
$$

be a history-supported influence atom, with layer response `r_\xi(a_j)`.

The history work is:

$$
\boxed{
W_\xi^{hist}(a)
=
\sum_{j\ge k}W_{\xi,j}(a_j).
}
$$

The effective response is:

$$
\boxed{
r_\xi^{eff}(a)
=
\sum_{j\ge k}\rho_{j\to k}r_\xi(a_j).
}
$$

where `\rho_{j\to k}` is projection through the bounded-history tower.

### 88.1 Theorem 61: Summable History Work Gives Non-Markov Packing

Assume:

1. above-tolerance effective response requires work quantum
   `q_{\xi,\lambda}`;
2. history work in a carrier ball is bounded:

   $$
   \boxed{
   \sum_{j\ge k}\mathcal W_{\xi,j}(B,r,\lambda)
   \le
   A_\xi r^{d_\xi};
   }
   $$

3. same-actual cancellations are quotiented and typed cancellations are
   printed.

Then pairwise distinguishable non-Markov history-supported atoms obey finite
packing:

$$
\boxed{
P_\xi^{hist}(B,r,\lambda)
\le
\frac{A_\xi}{q_{\xi,\lambda}}r^{d_\xi}.
}
$$

**Proof.**

The proof is the same budget argument, but applied to history work rather than
present-layer work.  The summable history budget pays for all retained older
layers.  Above-tolerance effective distinguishability still requires a work
quantum. `\square`

### 88.2 Barandes Alignment

This is explicitly non-Markovian.  An influence atom may require a whole
history suffix:

$$
\boxed{
(H_{B,k},H_{B,k+1},\ldots)
}
$$

to define its response.  The packing theorem controls the projective history
cylinder, not a present-state transition.

## 89. Hyperedge and Entanglement Packing

Entanglement-like record structure may be shared across many records.  The
right carrier is not necessarily a pair; it can be a finite hyperedge:

$$
\boxed{
e=\{r_1,\ldots,r_m\}.
}
$$

The typed response of a hyperedge is:

$$
\boxed{
\tau(e)=[r_e]_{B,Y,\lambda}.
}
$$

The hyperedge is admitted if:

$$
\boxed{
C_B(\tau(e))=o(C_{\rm raw}(B))
\quad\text{and}\quad
W_T(e)\ge q_{T,\lambda}
\text{ when above tolerance.}
}
$$

#### Theorem 62: Inclusive Hyperedge Typing Gives Entanglement Packing

If above-tolerance hyperedge responses have positive typed work quantum and
the total typed work budget is polynomial in the control surface, then the
number of distinguishable entanglement/typed hyperedges is polynomial and
subraw.

**Proof.**

Apply the boundary-work packing theorem to typed hyperedge classes rather than
individual record pairs.  Shared structure is counted once as an inclusive
typed carrier, not once per pair. `\square`

### 89.1 Why This Matters

This prevents a false locality assumption.  Long entanglement is compatible
with the law if it is a finite inclusive typed carrier.  It fails only if it
requires raw reconstruction or nonsummable projective drift.

## 90. Cancellation Adversaries

### 90.1 Signed Cancellation

Adversary: many large influences cancel in the printed target, so packing by
target response misses them.

Response: the carrier norm must include absolute center/ledger work:

$$
\boxed{
\|r_\xi(a)\|_{\lambda,abs}
=
\|r_\xi(a)\|_\lambda+W_\xi(a).
}
$$

If influences are large but cancel in `Y`, they still consume work.  If they
consume no work and leave no target/packet residue, they are same-actual null
at tolerance.

### 90.2 Many Tiny Influences

Adversary: infinitely many below-tolerance atoms add up.

Response: their aggregate is admitted only if the tail is summable:

$$
\boxed{
\sum_{a:\ \|r(a)\|\le\epsilon}\|r(a)\|<\infty.
}
$$

If the aggregate exceeds tolerance, it becomes a typed/source carrier or
forces boundary expansion.

### 90.3 Oscillatory History Influence

Adversary: older histories alternate forever, never settling.

Response: that is exactly nonsummable projective drift:

$$
\boxed{
\sum_{j\ge k}\Delta_{\xi,j}=\infty.
}
$$

The bounded panel is then not stable for that target.

## 91. Finite Influence Packing Theorem

#### Theorem 63: Boundary Work, History Summability, and Inclusive Typing Imply Packing

Let `\mathbf B` be a physically bounded history family at tolerance
`\lambda`.  Assume for each carrier class:

1. above-tolerance distinguishability has positive work quantum;
2. total carrier work in bounded carrier balls is polynomial in record radius;
3. older-history work tails are summable;
4. same-actual cancellations are quotiented;
5. typed/entangled hyperedges are counted by inclusive typed classes;
6. below-tolerance aggregates are summable or typed.

Then finite influence packing holds for all six carrier classes:

$$
\boxed{
P_\xi(B,r,\lambda)\le A_\xi r^{d_\xi},
\qquad
\xi\in\{\partial,I,U,O,C,T\}.
}
$$

**Proof.**

For ordinary carrier atoms, Theorem 60 gives packing from positive work
quanta and polynomial work budget.  For history-supported atoms, Theorem 61
applies the same argument to summable history work.  For entanglement and
source hyperedges, Theorem 62 applies the argument to inclusive typed classes.
Same-actual and below-tolerance cancellation cases are removed or typed by
assumptions 4 and 6. `\square`

## 92. Closing the Long Campaign

Combining Theorem 63 with Theorem 59 gives the extended campaign result:

#### Theorem 64: Boundary-Work History Law for Physically Bounded Families

If a physically bounded history family has:

1. positive work quanta for above-tolerance distinguishability;
2. polynomial boundary-work budgets;
3. summable older-history tails;
4. inclusive typed hyperedge sectors;
5. no hidden presentation counts;
6. promoted action coercivity and denominator floors;

then it admits:

$$
\boxed{
\text{a projective non-Markov positive history law }h_{B,k}^\star
}
$$

whose finite-panel probabilities converge and whose finite GR packet is
licensed exactly when the GR packet error is below tolerance.

**Proof.**

The assumptions give finite influence packing by Theorem 63.  Finite influence
packing gives the non-Markov carrier-calibrated history law by Theorem 59.
`\square`

## 93. Final Status After the Long Campaign

The campaign has followed the chain until the remaining premises are physical
and auditable:

$$
\boxed{
\begin{gathered}
\text{positive work quantum}
+\text{polynomial boundary-work budget}
+\text{summable history tails}
+\text{inclusive typed hyperedges}\\
\Longrightarrow
\text{finite influence packing}
\Longrightarrow
\text{carrier calibration}
\Longrightarrow
\text{projective non-Markov click law.}
\end{gathered}
}
$$

The law remains Barandes-aligned:

$$
\boxed{
\text{the full compatible bounded history is the deterministic object;
probability is the projected residual of the part we do not compute.}
}
$$

The remaining irreducible questions are now sharply physical:

1. What fixes the positive work quantum `q_{\xi,\lambda}` for each carrier?
2. What physical principle bounds total boundary work polynomially?
3. Which QFT-like soft/entangled sectors admit finite inclusive typed classes?
4. Which finite packet limits have continuum Einstein/QFT representations?

Those are not "more brute force."  They are the next analytic targets.

## 94. Work Quantum From Center Convexity

The positive work quantum should not be inserted by hand.  It should come from
the local convexity of the record-work term.

For a channel `\alpha`, the center work is:

$$
\boxed{
\Psi_\alpha(\widehat\mu_\alpha)
=
\omega_\alpha
\left[
\mu_\alpha\log\frac{\mu_\alpha}{\widehat\mu_\alpha}
-\mu_\alpha
+\widehat\mu_\alpha
\right].
}
$$

Let:

$$
\boxed{
\delta_\alpha
=
\widehat\mu_\alpha-\mu_\alpha.
}
$$

If the predicted mass stays in a denominator-safe interval:

$$
\boxed{
\widehat\mu_\alpha\in[m_\alpha,M_\alpha],
\qquad
0<m_\alpha\le\mu_\alpha\le M_\alpha,
}
$$

then Taylor/Pinsker control gives:

$$
\boxed{
\Psi_\alpha(\widehat\mu_\alpha)
\ge
\frac{\omega_\alpha}{2M_\alpha}\delta_\alpha^2.
}
$$

Therefore an above-tolerance channel displacement:

$$
\boxed{
|\delta_\alpha|\ge\epsilon_\alpha
}
$$

costs at least:

$$
\boxed{
q_{\alpha,\lambda}
=
\frac{\omega_\alpha}{2M_\alpha}\epsilon_\alpha^2.
}
$$

### 94.1 Theorem 65: Convex Center Work Gives a Positive Work Quantum

Assume:

1. the channel has positive precision `\omega_\alpha>0`;
2. predicted and committed masses have a positive denominator floor;
3. above-tolerance distinguishability requires
   `|\delta_\alpha|\ge\epsilon_\alpha>0`.

Then every above-tolerance distinguishable response in channel `\alpha` has
positive work quantum:

$$
\boxed{
W_\alpha\ge q_{\alpha,\lambda}>0.
}
$$

**Proof.**

The RN/KL center term is strongly convex on any denominator-safe interval.
The displayed quadratic lower bound gives a strictly positive cost for every
above-tolerance displacement. `\square`

### 94.2 Carrier Work Quantum

For a carrier class `\xi`, define:

$$
\boxed{
q_{\xi,\lambda}
=
\min_{\alpha\in\mathfrak C_\xi}
q_{\alpha,\lambda}.
}
$$

If `\mathfrak C_\xi` is finite and every channel has positive denominator
floor and positive precision, then:

$$
\boxed{
q_{\xi,\lambda}>0.
}
$$

So the work quantum is derived from center convexity plus finite calibrated
channel extraction.

## 95. Polynomial Boundary-Work Budget

The second premise is a bound on total available work inside a carrier
neighborhood.

Let:

$$
\boxed{
\mathcal W_\xi(B,r,\lambda)
=
\sum_{\alpha\in\mathfrak C_\xi(B,r)}
\omega_\alpha\mu_\alpha
}
$$

be the committed work capacity of carrier class `\xi` in a record ball of
radius `r`.

Assume bounded work density:

$$
\boxed{
\omega_\alpha\mu_\alpha\le w_{\xi,\lambda}
}
$$

for each calibrated carrier channel, and carrier count:

$$
\boxed{
|\mathfrak C_\xi(B,r)|\le A_\xi r^{d_\xi}.
}
$$

Then:

$$
\boxed{
\mathcal W_\xi(B,r,\lambda)
\le
w_{\xi,\lambda}A_\xi r^{d_\xi}.
}
$$

### 95.1 Theorem 66: Bounded Work Density Gives Polynomial Work Budget

If a carrier class has polynomial channel count and uniformly bounded
committed work density at tolerance `\lambda`, then its total carrier work
budget is polynomial in record radius.

**Proof.**

Sum the bounded per-channel committed work over the polynomially many active
channels. `\square`

### 95.2 Hostile Review: Is Bounded Work Density Physical?

It is a physical closure condition.  If a bounded carrier ball contains
unbounded committed work density, then it is not a finite bounded experiment at
that tolerance.  The boundary must expand, the tolerance must weaken, or the
region is singular/critical.

This is analogous to the earlier horizon and phase-boundary failures.

## 96. Derived Packing From Work Principles

We can now remove two premises from Theorem 63.

#### Theorem 67: Center Convexity and Bounded Work Density Imply Influence Packing

Assume for each carrier class:

1. finite calibrated center channels;
2. positive denominator floors and positive precisions;
3. above-tolerance distinguishability changes at least one center/channel mass
   by `\epsilon_\alpha`;
4. bounded committed work density;
5. polynomial carrier-channel count in record radius;
6. summable older-history work tails for non-Markov history-supported atoms;
7. inclusive typed hyperedge compression.

Then finite influence packing holds for all six carrier classes.

**Proof.**

Assumptions 1--3 give a positive work quantum by Theorem 65.  Assumptions 4
and 5 give polynomial boundary-work budgets by Theorem 66.  The boundary-work
packing theorem then gives finite influence packing for present carrier atoms.
Assumption 6 gives the non-Markov history version.  Assumption 7 gives the
typed hyperedge version. `\square`

## 97. Updated Non-Markov Click-Law Theorem

Combining Theorem 67 with Theorem 64:

#### Theorem 68: Convex Boundary Work Selects a Projective Non-Markov Click Law

Let `\mathbf B` be a physically bounded history family at tolerance
`\lambda`.  Assume:

1. finite calibrated center channels with positive denominator floors;
2. positive channel precisions;
3. bounded committed work density;
4. polynomial carrier-channel counts;
5. summable older-history work tails;
6. inclusive typed hyperedge compression;
7. no hidden presentation counts;
8. promoted action coercivity and GR extraction denominator floors.

Then `\mathbf B` admits a projective non-Markov positive history law:

$$
\boxed{
h_{B,k}^\star(H)
=
\exp[-\mathcal A_{B,k}^{hist,\star}(H)]
}
$$

whose partial-panel predictions converge, and whose finite spacetime packet is
licensed exactly when `\mathcal E^{\rm GR}_{B,k}` is below tolerance.

**Proof.**

The first seven assumptions imply finite influence packing by Theorem 67.
Theorem 64 then gives the projective non-Markov history law and convergence.
The denominator floors license finite GR extraction. `\square`

## 98. What This Removes and What Remains

Removed as primitive assumptions:

1. positive work quantum;
2. polynomial boundary-work budget;
3. finite influence packing.

They are now derived from:

$$
\boxed{
\text{convex center work}
+\text{denominator floors}
+\text{bounded work density}
+\text{polynomial carrier counts}.
}
$$

The hard remaining premises are:

1. denominator floors;
2. bounded work density;
3. polynomial carrier-channel counts;
4. summable older-history work tails;
5. inclusive typed sectors.

These are physical regularity conditions for a bounded experiment, not
one-step stochastic assumptions.

## 99. Final Hostile Review of This Extension

### Review AA: "Polynomial carrier counts are back as an assumption."

Accepted.

The campaign moved from influence packing to carrier counts.  That is a real
narrowing: carrier counts are structural and auditable from record diamonds,
whereas influence packing involved target-dependent distinguishability.

### Review AB: "Denominator floors may fail."

Accepted.

If they fail, the packet channel is not licensed.  This marks pre-spacetime,
critical, or boundary-degenerate behavior.

### Review AC: "Bounded work density looks like an energy condition."

Accepted.

It is the record-theoretic analogue of an energy/control-density condition for
a finite experiment.  It should eventually be derived from the same center
ledger and typed source constraints, but for now it is the clearest physical
regularity premise.

### Review AD: "Summable older-history tails may be the deepest issue."

Accepted.

This is the main non-Markovian burden.  It says old history can matter, but
its unresolved influence must become summable after the correct promoted
carrier algebra is used.

## 100. Campaign End State

The long campaign has now followed the main openings down to five precise
physical regularity targets:

$$
\boxed{
\begin{gathered}
\text{denominator floors},\quad
\text{bounded work density},\quad
\text{polynomial carrier counts},\\
\text{summable non-Markov history tails},\quad
\text{inclusive typed sectors}.
\end{gathered}
}
$$

Given those, Paper XLI now has a complete scoped derivation:

$$
\boxed{
\text{physical regularity}
\Rightarrow
\text{finite influence packing}
\Rightarrow
\text{carrier calibration}
\Rightarrow
\text{subraw kernel promotion}
\Rightarrow
\text{intrinsic gap}
\Rightarrow
\text{projective non-Markov click law}.
}
$$

The next paper-level target should be one of the five regularity conditions,
not another broad reformulation.
