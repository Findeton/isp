# Relativistic ISP v7 - Paper XLVIII

# Selector Coefficient Calibration From Bounded-History Closure

## 0. Purpose

Paper XLIV ended with eight still-open physical derivation issues:

1. calibrate the selector coefficients, not just the selector form;
2. prove actual physical seeds flow into geometry;
3. derive record-realized scale anchors and the limit `G_\infty`;
4. construct the typed source/stress packet;
5. prove continuum convergence for large finite packets;
6. prove selected physical histories make the Einstein residual small;
7. build the finite QFT typed net and amplitude/state rule;
8. derive the initial-history projection weight that charges onset.

This paper began by attacking the first issue.  It was then extended through
the remaining seven issues, keeping the same standard: each slogan must become
a finite constrained theorem, a no-go boundary, or an explicitly named
physical-sector problem.  By the end of the paper, all eight issues have
finite operational closures; the remaining work is physical identification of
which large record panels satisfy the gates and what continuum/QFT constants
their limits realize.

The starting selector from Paper XLIV was:

$$
\boxed{
\mathcal A_B^{sel}(K)
=
L_B(K)
+\lambda_DD_B(K)
+\lambda_SS_B(K)
+\lambda_RR_B(K)
+\lambda_HH_B(K).
}
$$

Here:

- `K` is a finite carrier dictionary for the bounded history problem;
- `L_B(K)` is description length;
- `D_B(K)` is projective deletion/refinement drift;
- `S_B(K)` is no-silent unresolved residue;
- `R_B(K)` is raw/reconstructive dependence;
- `H_B(K)` is hidden-history dependence not printed in the bounded panel;
- the `\lambda` coefficients were left uncalibrated.

The goal is to remove the arbitrary status of the coefficients.

## 1. Executive Result

The coefficients are not new physical constants.

They are finite dual/barrier quantities induced by the bounded experiment:

$$
\boxed{
\text{selector coefficients}
=
\text{tolerance gates}
+\text{finite defect floors}
+\text{description-length range}.
}
$$

The calibrated selector is therefore not primarily a soft weighted sum.  It is
the scalar representation of a constrained finite problem:

$$
\boxed{
\min L_B(K)
\quad
\text{subject to}
\quad
D_B\le\epsilon_D,\ 
S_B\le\epsilon_S,\ 
R_B\le\epsilon_R,\ 
H_B\le\epsilon_H.
}
$$

The `\lambda` values are any finite penalties large enough to make a
constraint violation more expensive than every possible description-length
saving.  Because the admissible bounded carrier class is finite after the
same-actual/subraw quotient, such penalties are computable from the bounded
problem itself.

Thus the first open issue closes in this form:

$$
\boxed{
\text{the calibrated selector is a constrained finite closure law;}
\quad
\lambda\text{s are derived enforcement multipliers, not tunable dynamics.}
}
$$

The remaining open part is not coefficient calibration.  It is the physical
calibration of the tolerances `\epsilon_D,\epsilon_S,\epsilon_R,\epsilon_H`
from the experiment, boundary, and target family.

## 2. Bounded Carrier Class

Let:

$$
\boxed{
\mathfrak K_B
=
\operatorname{Adm}(H_{B,k},\mathcal T_B)
}
$$

be the finite admissible carrier class for bounded history cylinder `H_{B,k}`
and target family `\mathcal T_B`.

The class is already quotienting:

1. same-actual presentation-null directions;
2. raw reconstruction lookups disallowed by subraw closure;
3. hidden fibers that do not print bounded target effects;
4. carrier dictionaries equivalent below tolerance.

This finiteness is essential.  It lets the selector be calibrated without a
continuum variational assumption.

Define the hard defect vector:

$$
\boxed{
\mathbf d_B(K)
=
\left(
D_B(K),S_B(K),R_B(K),H_B(K)
\right).
}
$$

Define the tolerance vector:

$$
\boxed{
\boldsymbol\epsilon_B
=
\left(
\epsilon_D,\epsilon_S,\epsilon_R,\epsilon_H
\right).
}
$$

The feasible carrier class is:

$$
\boxed{
\mathfrak K_B^{feas}
=
\{K\in\mathfrak K_B:\mathbf d_B(K)\le\boldsymbol\epsilon_B\}.
}
$$

The calibrated selector is:

$$
\boxed{
\mathcal K_B^\star
=
\arg\min_{K\in\mathfrak K_B^{feas}} L_B(K).
}
$$

If `\mathfrak K_B^{feas}` is empty, the bounded problem is not closed at the
requested tolerance.  The boundary, history depth, target family, or tolerance
must be changed.

## 3. Why Linear Weights Were Suspicious

A soft linear action appears to allow tradeoffs such as:

$$
\boxed{
\text{slightly more silent residue}
\quad
\text{in exchange for}
\quad
\text{shorter description length}.
}
$$

That is physically wrong once the residue affects the target above tolerance.
No-silent control is not a preference; it is an admissibility condition.

The same holds for raw reconstruction.  A carrier cannot become physically
acceptable merely because it is short if it hides the answer in raw
presentation counts.

Thus the correct selector hierarchy is:

$$
\boxed{
\text{first pass hard closure gates;}
\quad
\text{then minimize description length;}
\quad
\text{then use stability reserves to break ties.}
}
$$

## 4. Normalized Violations

For each defect type `X\in\{D,S,R,H\}`, define the normalized violation:

$$
\boxed{
v_X(K)
=
\left[
\frac{X_B(K)-\epsilon_X}{\delta_X}
\right]_+.
}
$$

Here:

- `[z]_+=\max(z,0)`;
- `\epsilon_X` is the permitted tolerance;
- `\delta_X` is the finite resolution floor for defect `X`.

The floor `\delta_X` is the smallest target-distinguishable positive violation:

$$
\boxed{
\delta_X
=
\min\{
|X_B(K)-\epsilon_X|:
K\in\mathfrak K_B,\ 
X_B(K)>\epsilon_X
\}.
}
$$

If no carrier violates the `X` gate, set `\delta_X=1` and `v_X=0`.

The total normalized violation is:

$$
\boxed{
V_B(K)
=
v_D(K)+v_S(K)+v_R(K)+v_H(K).
}
$$

Then:

$$
\boxed{
V_B(K)=0
\quad\Longleftrightarrow\quad
K\in\mathfrak K_B^{feas}.
}
$$

## 5. Description-Length Range

Let:

$$
\boxed{
\Delta L_B
=
\max_{K,K'\in\mathfrak K_B}
|L_B(K)-L_B(K')|.
}
$$

This is finite because `\mathfrak K_B` is finite.

Choose:

$$
\boxed{
M_B>\Delta L_B.
}
$$

Define the calibrated scalar action:

$$
\boxed{
\mathcal A_B^{cal}(K)
=
L_B(K)+M_BV_B(K).
}
$$

This is the canonical replacement for arbitrary `\lambda` coefficients.

Equivalently:

$$
\boxed{
\lambda_X^{cal}
=
\frac{M_B}{\delta_X}
}
$$

on the violating side of the tolerance gate, with zero penalty below the gate.

## 6. Theorem 1: Barrier Calibration Equivalence

The minimizers of `\mathcal A_B^{cal}` are exactly the feasible carriers of
minimum description length:

$$
\boxed{
\arg\min_{K\in\mathfrak K_B}\mathcal A_B^{cal}(K)
=
\arg\min_{K\in\mathfrak K_B^{feas}}L_B(K),
}
$$

provided `\mathfrak K_B^{feas}` is nonempty.

**Proof.**

If `K` is feasible, `V_B(K)=0`, so:

$$
\mathcal A_B^{cal}(K)=L_B(K).
$$

If `K` is infeasible, at least one normalized violation is positive.  By the
definition of `\delta_X`, every positive violation contributes at least one
unit to `V_B`.  Hence:

$$
\mathcal A_B^{cal}(K)\ge L_B(K)+M_B.
$$

Because `M_B>\Delta L_B`, no infeasible carrier can beat any feasible carrier
by saving description length.  Therefore the minimizer must be feasible, and
among feasible carriers the action reduces to `L_B`. `\square`

## 7. Consequence: Coefficients Are Not Tuned

The old soft weights:

$$
\lambda_D,\lambda_S,\lambda_R,\lambda_H
$$

become calibrated gate-enforcement multipliers:

$$
\boxed{
\lambda_X^{cal}
=
\frac{M_B}{\delta_X},
\qquad
M_B>\Delta L_B.
}
$$

They depend on:

1. the bounded carrier class;
2. the target tolerance;
3. the defect resolution floor;
4. the description-length range.

They do not encode new physics.  They encode the rule:

$$
\boxed{
\text{do not buy description-length savings by violating bounded closure.}
}
$$

## 8. Tie-Breaking Among Feasible Carriers

Feasible carriers can tie in description length.  Some ties are physically
real; others are near-null presentation choices.

Define the reserve vector:

$$
\boxed{
\rho_B(K)
=
\boldsymbol\epsilon_B-\mathbf d_B(K).
}
$$

Positive reserve means the carrier is safely inside tolerance.  Define:

$$
\boxed{
\operatorname{Res}_B(K)
=
\sum_X
\frac{\rho_X(K)}{\epsilon_X}.
}
$$

The stable tie-breaker is:

$$
\boxed{
\mathcal A_B^{tie}(K)
=
\left(
\mathcal A_B^{cal}(K),
L_B(K),
-\operatorname{Res}_B(K),
\operatorname{PhaseLabel}_B(K)
\right)
}
$$

ordered lexicographically.

This says:

1. first satisfy gates;
2. then minimize description length;
3. then prefer larger stability reserve;
4. then keep irreducible phase labels rather than forcing a false tie.

## 9. Theorem 2: Tie Handling Is Record-Covariant

If deletion/refinement maps preserve defect values below tolerance and
description length up to same-actual null shifts, then the tie-breaking rule
commutes with bounded-history projection.

**Proof.**

The first coordinate of the lexicographic action depends only on normalized
gate violations.  The second depends on quotient description length.  The
third depends on margins from the same gates.  The fourth is an explicit phase
label preserved unless the projection collapses a physically real phase
difference below tolerance.  Each coordinate is record-intrinsic and
projectively defined. `\square`

## 10. Lagrange Dual Reading

The constrained selector may also be written as a finite Lagrange problem:

$$
\boxed{
\mathcal L_B(K,\boldsymbol\lambda)
=
L_B(K)
+\sum_X\lambda_X(X_B(K)-\epsilon_X).
}
$$

The calibrated multipliers are not found by aesthetic choice.  They are any
dual vector satisfying:

$$
\boxed{
\lambda_X\ge\frac{\Delta L_B}{\delta_X}
}
$$

for every active hard gate.

Complementarity has the finite form:

$$
\boxed{
\lambda_X\,[X_B(K^\star)-\epsilon_X]_+=0
}
$$

for feasible minimizers, because gate violations vanish at the minimizer.

The barrier version is preferable because it avoids pretending that a finite
discrete carrier class has a smooth KKT geometry.  But the dual reading helps
interpret the old `\lambda` symbols.

## 11. Theorem 3: Calibration Is Unique Up To Selector-Null Scaling

Let two calibrated scalarizations use penalties `M_B` and `M'_B`, both larger
than `\Delta L_B`.  Then they select the same feasible minimum-description
carrier set.

**Proof.**

By Theorem 1, any `M_B>\Delta L_B` excludes infeasible carriers and reduces to
description length on feasible carriers.  Therefore all such choices produce
the same minimizer set before tie-breaking. `\square`

This is important: the exact large number is not physical.  The selected
carrier is invariant once the barrier clears the finite dominance threshold.

## 12. Calibration Of Tolerances

The coefficients are now calibrated by tolerances and finite floors.  The next
question is where tolerances come from.

For a bounded experiment, define:

$$
\boxed{
\epsilon_X
=
\epsilon_X(\mathcal T_B,\mathcal I_B,\partial B,k)
}
$$

where:

- `\mathcal T_B` is the target family;
- `\mathcal I_B` is the instrument/control panel;
- `\partial B` is the boundary relation to the unresolved outside;
- `k` is history depth.

A tolerance is admissible only if:

$$
\boxed{
\epsilon_X
\ge
\epsilon_X^{inst}
+\epsilon_X^{boundary}
+\epsilon_X^{history}
}
$$

The three terms are:

1. instrument resolution;
2. permitted outside-boundary influence;
3. residual history truncation error.

This does not make tolerance arbitrary.  It makes tolerance a part of the
bounded physical question.

## 13. Theorem 4: Tolerance Monotonicity

If the boundary expands, the instrument is refined, or the history depth
increases, the admissible tolerance vector can only stay the same or decrease:

$$
\boxed{
B'\supset B,\quad
\mathcal I_{B'}\succeq\mathcal I_B,\quad
k'\ge k
\Longrightarrow
\boldsymbol\epsilon_{B'}\le\boldsymbol\epsilon_B
}
$$

provided the target family is not weakened.

**Proof.**

Expanding the boundary reduces unresolved outside influence.  Refining the
instrument reduces measurement/control-panel uncertainty.  Increasing history
depth reduces truncation residue.  None of these operations can require a
larger tolerance for the same target; they can only preserve or sharpen it.
`\square`

## 14. Hostile Review I: "You Hid The Coefficients In The Tolerances"

Accepted in part, but that is the right place for them.

The `\lambda` coefficients should not encode physics.  The physical inputs are:

1. what question is being asked;
2. what boundary is being controlled;
3. what history depth is being used;
4. what error the instrument can distinguish.

Those are tolerances, not selector preferences.

The calibrated selector says:

$$
\boxed{
\text{once a target and tolerance are fixed, coefficient freedom disappears.}
}
$$

## 15. Hostile Review II: "Hard Gates Are Too Harsh"

The gates are hard only relative to the stated target.

If the target allows error `\epsilon_S`, then no-silent residue below
`\epsilon_S` is allowed.  If it exceeds `\epsilon_S`, the target is no longer
being answered.

Thus the hard gate is not metaphysical.  It is ordinary experimental honesty:

$$
\boxed{
\text{do not claim a prediction at tolerance }\epsilon
\text{ while hiding residue larger than }\epsilon.
}
$$

## 16. Hostile Review III: "What If All Feasible Carriers Are Huge?"

Then the bounded problem is expensive but still closed.

If feasible carriers exist but are near-raw, the selector may choose one only
if it remains subraw and non-reconstructive.  If every feasible carrier is raw,
then:

$$
\boxed{
\mathfrak K_B^{feas}=\emptyset
\quad\text{inside the subraw admissible class.}
}
$$

The correct response is boundary expansion, history deepening, target
weakening, or declaring that the bounded panel cannot close the prediction.

## 17. Hostile Review IV: "Can A Carrier Game The Floors?"

The finite floor `\delta_X` must be computed after quotienting same-actual
nulls but before minimizing.  If a carrier splits one violation into many
tiny presentation fragments, the projected defect `X_B(K)` is measured on the
bounded target, not on the presentation fragments.

Thus gaming is blocked by:

$$
\boxed{
\text{defects are target-projected, not presentation-counted.}
}
$$

## 18. Hostile Review V: "Does This Preserve Barandes Alignment?"

Yes.

The calibrated selector never introduces a Markov transition:

$$
\boxed{
\Pr(W_{N+1}\mid W_N)
\quad\text{is not primitive.}
}
$$

Instead:

$$
\boxed{
H_{B,k}
\to
\mathfrak K_B^{feas}
\to
\mathcal K_B^\star
\to
\text{projected probabilities}.
}
$$

The full bounded history remains primitive.  Probability appears only after
projection onto the computable carrier panel.

## 19. Full Closure Theorem For Issue 1

### Theorem 5: Coefficient Calibration Closure

For every finite bounded-history prediction problem with:

1. finite admissible carrier quotient `\mathfrak K_B`;
2. target tolerance vector `\boldsymbol\epsilon_B`;
3. positive finite resolution floors `\delta_X`;
4. finite description-length range `\Delta L_B`;

the selector coefficients are calibrated by:

$$
\boxed{
\lambda_X^{cal}
=
\frac{M_B}{\delta_X},
\qquad
M_B>\Delta L_B.
}
$$

The resulting scalar selector is equivalent to the constrained law:

$$
\boxed{
\min L_B(K)
\quad
\text{subject to}
\quad
D_B\le\epsilon_D,\ 
S_B\le\epsilon_S,\ 
R_B\le\epsilon_R,\ 
H_B\le\epsilon_H.
}
$$

This closes the coefficient-calibration problem up to tolerance calibration.

**Proof.**

Theorem 1 proves barrier equivalence.  Theorem 2 proves projective tie
compatibility.  Theorem 3 proves invariance under selector-null rescaling.
Theorem 4 locates tolerance sharpening under boundary/history refinement.
Thus the old free coefficients are replaced by finite enforcement multipliers
computed from the bounded carrier class and tolerance floors. `\square`

## 20. What Is Actually Closed

Closed:

$$
\boxed{
\text{the selector coefficients are no longer arbitrary.}
}
$$

More precisely:

$$
\boxed{
\text{for a fixed bounded target and tolerance, the coefficients are
barrier/dual enforcement terms.}
}
$$

Not closed:

$$
\boxed{
\text{the physical derivation of the tolerance vector itself.}
}
$$

That tolerance problem belongs partly to:

1. instrument/control-panel modeling;
2. boundary influence bounds;
3. history truncation estimates;
4. source/QFT sector resolution;
5. continuum representation error.

## 21. Updated List Of Open Issues

After this paper, the eight issues become:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level; tolerance calibration remains as part of bounded experimental
   definition;
2. **physical seed flow into geometry:** open;
3. **record-realized scale anchors and `G_\infty`:** open;
4. **typed source/stress construction:** open;
5. **continuum convergence:** open;
6. **small Einstein residual on physical histories:** open;
7. **finite QFT typed net and amplitude/state rule:** open;
8. **initial-history projection weight charging onset:** open.

The next issue should be attacked with the same standard:

$$
\boxed{
\text{turn the slogan into a finite constrained theorem, a no-go, or a
remaining physical derivation.}
}
$$

## 22. Final Result

Paper XLVIII closes the first remaining issue in the only non-arbitrary way:

$$
\boxed{
\lambda\text{s are not tunable physical weights;}
\quad
\lambda\text{s are calibrated barriers enforcing bounded-history closure.}
}
$$

The calibrated click selector is:

$$
\boxed{
\mathcal K_B^\star
=
\arg\min_{K\in\mathfrak K_B}
\left[
L_B(K)+M_B
\sum_{X\in\{D,S,R,H\}}
\left[
\frac{X_B(K)-\epsilon_X}{\delta_X}
\right]_+
\right],
\qquad
M_B>\Delta L_B.
}
$$

Equivalently:

$$
\boxed{
\mathcal K_B^\star
=
\arg\min_{K\in\mathfrak K_B^{feas}}L_B(K).
}
$$

This preserves the whole point of the program:

$$
\boxed{
\text{history first;}
\quad
\text{bounded closure second;}
\quad
\text{probability only after projection.}
}
$$

## 23. Issue 2 Campaign: Physical Seed Flow Into Geometry

Issue 2 asks whether physical pre-geometric seeds flow into the
geometry-irreducible phase.

This cannot mean:

$$
\boxed{
\text{every physically admissible seed becomes spacetime.}
}
$$

Paper XLV falsified that by giving physically admissible recurrent algebraic
carrier phases.  The correct target is:

$$
\boxed{
\text{characterize exactly when calibrated selection forces a seed into the
geometry-irreducible basin.}
}
$$

The campaign must therefore produce:

1. a positive flow theorem;
2. a no-go boundary;
3. hostile tests against algebraic, entanglement-heavy, symmetric, and
   click-only seeds;
4. a remaining physical obstruction if actual cosmological seeds cannot yet
   be proven to satisfy the hypotheses.

## 24. Calibrated Extension Graph

Let `S_0` be a pre-geometric record seed.  Let:

$$
\boxed{
\mathcal H(S_0)
}
$$

be the finite tree of bounded history extensions reachable from `S_0` by
admissible record additions, deletions, and refinements up to the working
depth.

At each node `h\in\mathcal H(S_0)`, define:

$$
\boxed{
\mathfrak K_h^{feas}
}
$$

using the calibrated feasibility gates of Sections 2-6.

The selected carrier set at node `h` is:

$$
\boxed{
\mathcal K_h^\star
=
\arg\min_{K\in\mathfrak K_h^{feas}}L_h(K).
}
$$

Let:

$$
\boxed{
\Phi_h^{GI}(K)
}
$$

be the geometry-irreducibility defect of carrier `K`: interval dimension,
atlas overlap, finite response tail, anisotropy, density regularity,
Ward/source stability, no-silent robustness, and bounded-history drift.

A selected branch is a sequence:

$$
\boxed{
(h_0,K_0),(h_1,K_1),\ldots
}
$$

where `K_j\in\mathcal K_{h_j}^\star` and `h_{j+1}` is an admissible extension
of `h_j`.

The branch enters spacetime when:

$$
\boxed{
\Phi_{h_j}^{GI}(K_j)\le\epsilon_{GI}.
}
$$

## 25. Flow Cannot Be A One-Step Law

The flow question is not:

$$
\boxed{
\Pr(K_{j+1}\mid K_j).
}
$$

That would violate the history-first alignment.

The correct object is the selected extension cylinder:

$$
\boxed{
\mathcal C_{S_0,k}
=
\{(h_j,K_j)_{j=0}^{k}:
K_j\in\mathcal K_{h_j}^\star\}.
}
$$

Probabilities, if used, are projections over compatible selected branches:

$$
\boxed{
\mu_{B,k}(E)
=
\frac{\sum_{\gamma\in E\cap\mathcal C_{S_0,k}}w(\gamma)}
{\sum_{\gamma\in\mathcal C_{S_0,k}}w(\gamma)}.
}
$$

The flow theorem must be deterministic at the selected-branch level and only
probabilistic after projection.

## 26. Geometric Reuse Pressure

Geometry wins only when it reuses multiple recurrent residues through the same
carrier.

Let the target-relevant recurrent residue channels be:

$$
\boxed{
\mathcal R_h
=
\mathcal R_h^{int}
\cup\mathcal R_h^{ov}
\cup\mathcal R_h^{loop}
\cup\mathcal R_h^{dens}
\cup\mathcal R_h^{Ward}
\cup\mathcal R_h^{drift}.
}
$$

These are, respectively:

1. interval-size/profile residue;
2. overlap/atlas residue;
3. loop/curvature-like residue;
4. density regularity residue;
5. Ward/source-balance residue;
6. deletion/refinement drift residue.

For a carrier `K`, define its reuse score:

$$
\boxed{
\operatorname{Reuse}_h(K)
=
\sum_{c\in\mathcal D_K}
\left(
\#\{\tau:c\text{ carries a residue of type }\tau\}-1
\right)_+.
}
$$

A geometric carrier has positive reusable overlap when one local atlas/center
carrier explains several residue types at once.

Define the geometry advantage margin:

$$
\boxed{
\Gamma_h
=
\min_{K\in\mathfrak K_h^{NG}}L_h(K)
-
\min_{K\in\mathfrak K_h^{GI-ready}}L_h(K).
}
$$

Here:

- `\mathfrak K_h^{NG}` are feasible non-geometric carriers;
- `\mathfrak K_h^{GI-ready}` are feasible carriers whose next selected
  refinements reduce `\Phi^{GI}` rather than increase it.

Positive `\Gamma_h` means geometry is cheaper at node `h`.

## 27. Theorem 6: Geometry Basin Entry

If along every selected branch outside the geometry-irreducible phase there is
a finite window `m` and a margin `\eta>0` such that:

$$
\boxed{
\sum_{i=j}^{j+m-1}\Gamma_{h_i}\ge\eta
}
$$

and the selected extensions satisfy the response-tail bound:

$$
\boxed{
\sum_{i=j}^{j+m-1}
\left|
\Phi_{h_{i+1}}^{GI}(K_{i+1})
-\Phi_{h_i}^{GI}(K_i)
+c\,\Gamma_{h_i}
\right|
\le
\eta/2
}
$$

for some `c>0`, then every selected branch enters the
geometry-irreducible phase after finitely many windows.

**Proof.**

The first condition says the calibrated selector repeatedly gives geometry a
positive description-length advantage over feasible non-geometric carriers.
The second says the geometry defect responds to that advantage with controlled
tail error.  Therefore over each window:

$$
\Phi_{h_{j+m}}^{GI}(K_{j+m})
\le
\Phi_{h_j}^{GI}(K_j)-c\eta+\eta/2.
$$

Thus `\Phi^{GI}` decreases by a fixed positive amount until it reaches
`\epsilon_{GI}`.  Since the defect is nonnegative, finite entry follows.
`\square`

## 28. Theorem 7: Stable Non-Geometric Counter-Basin

If there exists an infinite selected branch such that:

$$
\boxed{
\Gamma_{h_j}\le0
}
$$

for all sufficiently large `j`, and the selected non-geometric carriers have
bounded projective drift, then geometry is not forced from `S_0`.

**Proof.**

When `\Gamma\le0`, feasible non-geometric carriers are at least as cheap as
the geometric-ready carriers.  The calibrated selector cannot be forced to
choose geometry.  Bounded projective drift prevents the non-geometric branch
from being disqualified by history instability.  Therefore a selected
non-geometric branch persists. `\square`

This is the formal version of the Cayley lesson:

$$
\boxed{
\text{physical admissibility alone does not imply spacetime.}
}
$$

## 29. Theorem 8: Basin Trichotomy

For any finite pre-geometric seed `S_0`, exactly one of the following holds at
the chosen target/tolerance:

1. **forced geometry basin:** all selected branches enter
   `\Phi^{GI}\le\epsilon_{GI}`;
2. **stable non-geometric basin:** at least one selected branch remains
   non-geometric with bounded drift;
3. **critical mixed basin:** branch selection has persistent ties or unclosed
   boundary defects requiring boundary expansion, history deepening, or phase
   refinement.

**Proof.**

The calibrated selector gives a finite selected extension graph at each
bounded depth.  If every selected branch satisfies the positive-window
advantage of Theorem 6, case 1 holds.  If some selected branch satisfies the
non-geometric persistence of Theorem 7, case 2 holds.  Otherwise the only
remaining possibilities are persistent ties, empty feasible classes, or
unresolved boundary/projective defects.  These are exactly case 3. `\square`

## 30. Opening Investigation A: Can Reuse Pressure Be Derived?

We now investigate whether `\Gamma_h>0` can be derived from finite residue
structure rather than assumed.

Let the residue channels form a co-support hypergraph:

$$
\boxed{
\mathcal C_h=(V_h,E_h).
}
$$

Vertices are local record centers or diamond interfaces.  A hyperedge
`e\in E_h` records that the same bounded carrier support participates in
several residue types:

$$
\boxed{
\tau(e)\subset
\{int,ov,loop,dens,Ward,drift\}.
}
$$

Define the multichannel co-support surplus:

$$
\boxed{
\operatorname{CoSup}_h
=
\sum_{e\in E_h}(|\tau(e)|-1)_+.
}
$$

Define the split-code overhead:

$$
\boxed{
\operatorname{SplitCost}_h
=
\min_{K\in\mathfrak K_h^{NG}}
\left[
L_h(K)-L_h(K_{split})
\right],
}
$$

where `K_{split}` is the carrier that treats each residue type separately.

The geometric atlas carrier saves description length only when co-support
surplus is real and cannot be captured by a non-geometric shared code.

### Theorem 9: Co-Support Sufficient Condition

If:

$$
\boxed{
a\,\operatorname{CoSup}_h
-
\operatorname{AltShare}_h
-
\operatorname{AtlasOverhead}_h
\ge
\eta>0,
}
$$

then `\Gamma_h\ge\eta`.

Here:

- `a` is the minimum per-co-support saving after quotienting null
  presentation changes;
- `\operatorname{AltShare}_h` is the best saving of non-geometric shared
  carriers;
- `\operatorname{AtlasOverhead}_h` is the dictionary cost of the geometric
  atlas/overlap carrier.

**Proof.**

A geometric carrier reuses every multichannel co-support through one
atlas/center dictionary entry.  The maximum competing saving is explicitly
subtracted as `\operatorname{AltShare}`.  If the remaining saving exceeds the
geometric overhead by `\eta`, the geometric-ready description length is lower
by at least `\eta`. `\square`

### Result

Reuse pressure can be derived for a narrower class:

$$
\boxed{
\text{multichannel co-support}
\quad
+\quad
\text{bounded alternative sharing}
\quad
\Rightarrow
\quad
\text{positive geometry margin.}
}
$$

It cannot be derived from recurrence alone.

## 31. Opening Investigation B: Cayley And Algebraic Carriers

The Cayley counterexample from Paper XLV has high alternative sharing:

$$
\boxed{
\operatorname{AltShare}_h
\approx
a\,\operatorname{CoSup}_h.
}
$$

Therefore the sufficient condition of Theorem 9 fails.

This is not a flaw.  It classifies the seed as algebraic:

$$
\boxed{
\Gamma_h\le0
\quad\Rightarrow\quad
\text{non-geometric click phase is allowed.}
}
$$

### Theorem 10: Algebraic Reuse Blocks Forced Geometry

If a non-geometric carrier represents all target-relevant co-support with
description length no greater than the geometric-ready carrier and has bounded
projective drift, then the seed is not in the forced geometry basin.

**Proof.**

This is Theorem 7 applied with the co-support estimate of Theorem 9 failing by
non-geometric alternative sharing. `\square`

## 32. Opening Investigation C: Entanglement-Heavy Seeds

An entanglement-heavy seed may carry many shared hyperedges without local
overlap structure.

Let:

$$
\boxed{
\operatorname{EntShare}_h
}
$$

be the sharing saving of typed nonlocal correlation carriers.

Geometry is forced only if:

$$
\boxed{
a\,\operatorname{CoSup}_h
>
\operatorname{EntShare}_h
+\operatorname{AtlasOverhead}_h.
}
$$

### Theorem 11: Entanglement Does Not Decide The Basin

Entanglement-heavy seeds enter the geometry basin only when their nonlocal
shared carriers either:

1. are typed source/correlation residues compatible with a geometric carrier;
   or
2. fail to compress the multichannel geometry targets as cheaply as atlas
   carriers.

Otherwise they define a non-geometric or mixed carrier phase.

**Proof.**

Entanglement carriers are admissible typed carriers.  They are not spacetime
carriers unless they also print interval, overlap, density, Ward, and drift
defects in a geometry-irreducible way.  If they do, they are compatible with
geometry; if they beat geometry, forced geometry fails; if they tie, the phase
is mixed. `\square`

## 33. Opening Investigation D: Symmetric Zero-Floor Seeds

Highly symmetric seeds can have zero channel floors.  Then defects may be
undistinguished:

$$
\boxed{
\delta_X=0
}
$$

for one or more geometry-relevant channels.

But calibrated selection requires positive finite floors.  If the floor is
zero, the branch is critical:

$$
\boxed{
\text{zero floor}
\quad\Rightarrow\quad
\text{no forced basin decision at that tolerance.}
}
$$

### Theorem 12: Symmetry Breaking Is Required For Flow

A symmetric seed with zero geometry-channel floors enters the forced geometry
basin only after a record-intrinsic perturbation or refinement creates
positive floors while preserving multichannel co-support.

**Proof.**

With zero floors, the calibrated barriers cannot distinguish violations of
the corresponding geometry-relevant channels.  The selector cannot force a
unique geometry basin.  Once floors become positive, Theorems 6 and 9 can
apply. `\square`

## 34. Opening Investigation E: Click-Only Targets

If the target family contains only click predictions and no spacetime,
boundary, density, Ward, or drift closure, geometry need not be selected.

Let:

$$
\boxed{
\mathcal T_B=\mathcal T_B^{click}
}
$$

and suppose a small non-geometric carrier predicts the click panel within
tolerance.  Then:

$$
\boxed{
\Gamma_h\le0
}
$$

is possible even for seeds that could support geometry under richer targets.

### Theorem 13: Rich Targets Are Necessary For Forced Geometry

Geometry can be forced only for target families that include the
geometry-relevant closure channels.  Click-only targets license click phases,
not spacetime phases.

**Proof.**

The selector minimizes the carrier needed for the stated target.  If the
target does not ask for geometry-sensitive residue, geometry has no mandatory
reuse advantage. `\square`

## 35. Opening Investigation F: Actual Physical Seeds

The phrase "physical seed" must not mean "seed we want."

Define the physical-onset seed class:

$$
\boxed{
\mathsf P_{geom}
}
$$

as seeds satisfying:

1. finite calibrated feasibility;
2. positive geometry-channel floors;
3. multichannel co-support across interval, overlap, density, Ward, and drift;
4. bounded alternative non-geometric sharing;
5. projective response-tail control;
6. rich target closure including spacetime-readout channels.

### Theorem 14: Physical-Onset Seed Theorem

Every seed in `\mathsf P_{geom}` flows into the geometry-irreducible phase
under the calibrated bounded-history selector.

**Proof.**

Conditions 2-4 imply positive geometry margin by Theorem 9.  Condition 5 gives
the response-tail bound of Theorem 6.  Condition 6 ensures the target family
actually charges geometry-relevant residue.  Therefore Theorem 6 applies to
every selected branch. `\square`

### What This Does Not Prove

It does not prove:

$$
\boxed{
\text{the actual universe began in }\mathsf P_{geom}.
}
$$

That belongs to the cosmological/onset prior, issue 8.

## 36. Independent Hostile Review Round For Issue 2

### Review 1: "You still assumed geometry margin."

Partly accepted.  The campaign derives a sufficient margin from multichannel
co-support minus alternative sharing.  It does not derive that actual seeds
have bounded alternative sharing.

### Review 2: "The Cayley counterexample still lives."

Accepted.  It must live.  It is classified as a stable non-geometric basin
when its alternative sharing beats or ties geometry.

### Review 3: "Entanglement-heavy histories may avoid geometry."

Accepted.  If they satisfy the click target more cheaply and do not need
geometry-sensitive closure, they are non-geometric phases.  If the target
requires spacetime closure, they must either cooperate with geometry or lose.

### Review 4: "The theorem is target-dependent."

Accepted.  Bounded physics is target-dependent.  The claim is not that the
universe computes a manifold for every question; it is that spacetime appears
when the bounded target forces geometry-irreducible carriers.

### Review 5: "This does not prove actual cosmology."

Accepted.  It proves the basin criterion.  Actual cosmology requires the
initial-history projection weight of issue 8.

### Review 6: "The response-tail bound may fail near singular regimes."

Accepted.  Then the branch is critical or non-spacetime at that tolerance.
This matches the pre-geometric/onset picture.

## 37. Issue 2 Final Theorem

### Theorem 15: Calibrated Geometry-Flow Classification

For calibrated bounded-history selection, every pre-geometric seed belongs to
one of three classes:

$$
\boxed{
\mathsf P_{geom}
\quad\cup\quad
\mathsf P_{nongeom}
\quad\cup\quad
\mathsf P_{crit}.
}
$$

Here:

1. `\mathsf P_{geom}` seeds have positive multichannel geometric reuse margin
   and controlled response tail, so all selected branches enter the
   geometry-irreducible phase;
2. `\mathsf P_{nongeom}` seeds have stable cheaper or tied non-geometric
   carriers, so geometry is not forced;
3. `\mathsf P_{crit}` seeds have zero floors, persistent ties, empty feasible
   classes, or boundary/projective defects requiring refinement.

**Proof.**

The calibrated selector is finite at every bounded depth.  Theorems 6 and 14
define the geometry basin.  Theorems 7, 10, and 11 define stable non-geometric
basins.  The remaining cases are precisely zero-floor, tie, empty-feasible,
or boundary/projective failures, hence critical. `\square`

## 38. Updated Status After Issue 2

Issue 2 is closed at the same level as issue 1:

$$
\boxed{
\text{we have a finite calibrated classification of geometry flow.}
}
$$

It is not closed as an empirical/cosmological fact:

$$
\boxed{
\text{we have not proven the actual universe's initial history lies in }
\mathsf P_{geom}.
}
$$

That remaining statement belongs to issue 8.

The open list is now:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification; actual cosmological support remains issue 8;
3. **record-realized scale anchors and `G_\infty`:** open;
4. **typed source/stress construction:** open;
5. **continuum convergence:** open;
6. **small Einstein residual on physical histories:** open;
7. **finite QFT typed net and amplitude/state rule:** open;
8. **initial-history projection weight charging onset:** open.

The next natural issue is `G_B` anchoring, because without scale anchors the
geometry phase can be dimensionless but cannot yet supply Newton's constant or
fully calibrated Einstein dynamics.

## 39. Issue 3 Campaign: Record-Realized Scale Anchors And `G_\infty`

Issue 3 asks whether the finite spacetime carrier can define a gravitational
scale:

$$
\boxed{
G_B
\quad\text{and}\quad
G_B\to G_\infty.
}
$$

The first point is conceptual.  A geometry-irreducible carrier gives stable
finite spacetime structure, but that structure can still be dimensionless.
It can say:

$$
\boxed{
\text{this record region has stable interval/overlap/curvature-like
relations.}
}
$$

It cannot by itself say:

$$
\boxed{
\text{this much curvature equals this much source in SI-like units.}
}
$$

For that, the bounded history must print anchors.

The campaign target is:

$$
\boxed{
\text{derive the finite conditions under which }G_B\text{ is record-realized,
and under which }G_B\to G_\infty.
}
$$

## 40. Unit Rescaling Group

Let `K_B^\star` be a selected geometry-irreducible carrier.  Let:

$$
\boxed{
\mathcal U_B
}
$$

be the finite unit-rescaling groupoid acting on the packet variables:

$$
\boxed{
\ell,\ t,\ m,\ a
}
$$

where:

- `\ell` is length/volume scale;
- `t` is clock/time scale;
- `m` is mass/source normalization;
- `a` is action/phase normalization.

The rescaling groupoid acts on finite curvature/source expressions such as:

$$
\boxed{
\mathcal G_B^{fin}
+\Lambda_B^{fin}\mathfrak g_B^{fin}
-8\pi G_B\Theta_B^{fin}.
}
$$

If a rescaling changes `G_B` while preserving all printed record predictions,
then `G_B` is not yet physical.  It is a coordinate in unit gauge.

## 41. Record-Realized Anchors

A scale anchor is not a convention.  It is a stable record subsystem whose
readout changes under a unit rescaling.

Define the anchor packet:

$$
\boxed{
\mathcal S_B
=
\{s_1,\ldots,s_q\}.
}
$$

Each `s_i` is a finite record carrier satisfying:

1. **printed:** it is part of the bounded carrier panel;
2. **stable:** it has bounded projective drift;
3. **non-null:** it changes under at least one unit-rescaling direction;
4. **same-actual invariant:** presentation changes do not alter its readout;
5. **floor-positive:** its denominator/readout has a finite lower bound.

Examples of possible anchors are:

1. clock-like recurrence periods;
2. rod/volume-like interval-density standards;
3. source/mass normalization carriers;
4. action/phase/interference normalization carriers;
5. dimensionless ratios that jointly remove residual unit gauge.

This is deliberately broad.  It does not assume atoms, photons, or QFT yet.
Those are later candidates for physical anchors.

## 42. Anchor Response Matrix

For each anchor `s_i`, define its logarithmic response to unit-rescaling
direction `u_j`:

$$
\boxed{
\mathsf A^{scale}_{ij}
=
\Delta_{u_j}\log s_i.
}
$$

The finite anchor matrix is:

$$
\boxed{
\mathsf A_B^{scale}
=
\left(\mathsf A^{scale}_{ij}\right).
}
$$

Let `\mathcal U_B^G` be the subspace of unit-rescaling directions that change
the numerical value assigned to `G_B`.  Define:

$$
\boxed{
\operatorname{ScaleDef}_B
=
\dim\left(
\ker\mathsf A_B^{scale}
\cap
\mathcal U_B^G
\right).
}
$$

Thus:

$$
\boxed{
\operatorname{ScaleDef}_B=0
}
$$

means no unit-rescaling direction can change `G_B` while leaving all anchors
unchanged.

## 43. Theorem 16: Pure Geometry Cannot Determine `G_B`

If the selected carrier contains only dimensionless geometry-irreducible
relations and no record-realized anchor packet with nonzero response to
source/action/time/length rescalings, then `G_B` is unlicensed.

**Proof.**

Dimensionless geometry fixes incidence, overlap, ratios, and curvature-like
shape relations.  It is invariant under at least one joint rescaling of source
normalization and geometric units.  Under that rescaling, the numerical value
assigned to `G_B` changes while the printed dimensionless geometry does not.
Therefore `G_B` is gauge-like rather than physical. `\square`

This theorem is the finite version of:

$$
\boxed{
\text{spacetime onset can precede Newton-scale gravitational calibration.}
}
$$

## 44. Theorem 17: Anchor-Rank Licensing Of `G_B`

`G_B` is licensed at bounded region `B` if and only if:

$$
\boxed{
\operatorname{ScaleDef}_B=0
}
$$

and all anchor readouts used in `\mathsf A_B^{scale}` have finite
denominator floors.

**Proof.**

If `\operatorname{ScaleDef}_B>0`, then there exists a unit-rescaling direction
that leaves every printed anchor unchanged while changing `G_B`.  Hence the
numerical value of `G_B` is not determined by records.

Conversely, if the kernel intersection is zero and denominators have floors,
then every `G_B`-changing rescaling changes at least one printed anchor above
finite resolution.  The unit gauge relevant to `G_B` is therefore fixed by
record data. `\square`

## 45. Constructing The Finite Coupling

Once anchor-rank closure holds, define the finite coupling by an anchor
functional:

$$
\boxed{
G_B
=
\Gamma_G
\left(
I_{GR}^{cl}(H_{B,k}),
\Theta_B^{fin},
\mathcal S_B
\right).
}
$$

Here:

- `I_{GR}^{cl}(H_{B,k})` is the finite GR packet;
- `\Theta_B^{fin}` is the typed source/stress packet, if present;
- `\mathcal S_B` is the anchor packet;
- `\Gamma_G` is the record-intrinsic ratio functional that compares
  curvature response to source response after unit gauge is fixed.

If `\Theta_B^{fin}` is absent, the region can license vacuum or
dimensionless geometry, but not a nontrivial numerical matter coupling.

## 46. Theorem 18: Source Coupling Requirement

A non-vacuum `G_B` requires a typed source/stress packet or an equivalent
source-normalizing anchor.  Geometry anchors alone can license lengths,
volumes, and clock ratios, but not the source side of Newton's coupling.

**Proof.**

The Einstein-form coupling compares curvature units to source/stress units.
If the source normalization is absent, a source rescaling can be compensated
by changing `G_B` while preserving the geometric packet.  Therefore the
source side must be anchored or typed. `\square`

This couples issue 3 to issue 4:

$$
\boxed{
G_B\text{ anchoring is not fully separable from source typing.}
}
$$

## 47. Projective Scale Drift

Let:

$$
\boxed{
\rho_{B'\to B}^{scale}
}
$$

be the projective map carrying anchors and scale packets from a refined or
larger bounded region `B'` to `B`.

Define the scale drift:

$$
\boxed{
\Delta_B^G
=
\left|
G_B-\rho_{B'\to B}^{scale}(G_{B'})
\right|.
}
$$

For a nested history/boundary sequence:

$$
\boxed{
B_1\subset B_2\subset\cdots,
}
$$

define:

$$
\boxed{
\operatorname{Drift}_G(n,m)
=
\left|
G_{B_n}
-\rho_{B_m\to B_n}^{scale}(G_{B_m})
\right|.
}
$$

## 48. Theorem 19: Projective Cauchy Criterion For `G_\infty`

If:

1. `G_{B_n}` is licensed for all sufficiently large `n`;
2. the projective scale maps are coherent;
3. for every `\epsilon>0` there exists `N` such that for all `m>n>N`:

$$
\boxed{
\operatorname{Drift}_G(n,m)<\epsilon,
}
$$

then there exists a projective limit:

$$
\boxed{
G_B\to G_\infty.
}
$$

If the Cauchy condition fails, `G_B` is a scale-running or boundary-dependent
finite coupling rather than a settled Newton constant.

**Proof.**

The sequence is Cauchy in the projective scale metric.  Coherent maps ensure
that comparisons are made in the same anchor gauge.  Therefore the finite
couplings converge to a projective limit.  Failure of Cauchy convergence means
the assigned coupling depends on boundary/history scale. `\square`

## 49. Theorem 20: Newton Interpretation Gate

`G_\infty` may be identified with Newton's gravitational constant only if:

$$
\boxed{
\begin{gathered}
G_B\to G_\infty,\\
\text{anchors converge to the physical clock/rod/source/action sector,}\\
\text{the finite Einstein residual converges in the same anchor gauge,}\\
\text{the continuum representation gate is passed.}
\end{gathered}
}
$$

Otherwise `G_\infty`, if it exists, is only the limiting coupling of the
selected finite record sector.

**Proof.**

Newton's constant is an empirical continuum-scale coupling.  A finite limit
can be compared to it only after the finite units, source normalization,
Einstein residual, and continuum representation all converge to the physical
sector. `\square`

## 50. Opening Investigation A: Clock-Like Anchors

Clock anchors require stable recurrence.

Define a clock-like carrier `c` by:

$$
\boxed{
c=(P_c,\Delta_c,\sigma_c)
}
$$

where:

- `P_c` is a repeated record pattern;
- `\Delta_c` is its recurrence count in bounded history;
- `\sigma_c` is its drift under deletion/refinement.

The clock defect is:

$$
\boxed{
\operatorname{ClockDef}_B(c)
=
\sigma_c+\operatorname{Var}(\Delta_c).
}
$$

### Theorem 21: Clock Anchor Gate

A record subsystem can serve as a time anchor only if:

$$
\boxed{
\operatorname{ClockDef}_B(c)\le\epsilon_t
}
$$

and it has nonzero response to time rescaling.

**Proof.**

If recurrence is unstable, the subsystem cannot define a reproducible time
unit.  If it has no time-rescaling response, it does not anchor time. `\square`

## 51. Opening Investigation B: Rod/Volume Anchors

Rod-like anchors require stable interval-density or volume profiles.

Let:

$$
\boxed{
r=(V_r,\partial V_r,\nu_r)
}
$$

where `V_r` is a bounded record subregion, `\partial V_r` its boundary, and
`\nu_r` its interval-density profile.

Define:

$$
\boxed{
\operatorname{RodDef}_B(r)
=
\operatorname{DimDrift}(r)
+\operatorname{DensDrift}(r)
+\operatorname{BoundaryLeak}(r).
}
$$

### Theorem 22: Rod Anchor Gate

A record subsystem can serve as a length/volume anchor only if
`\operatorname{RodDef}_B(r)\le\epsilon_\ell` and its profile responds
nontrivially to length/volume rescaling.

**Proof.**

Length/volume calibration requires stable scale-dependent interval structure.
Dimension drift, density drift, or boundary leakage above tolerance makes the
anchor unstable. `\square`

## 52. Opening Investigation C: Source/Mass Anchors

Mass/source anchoring is harder because it is not pure geometry.

Let:

$$
\boxed{
m=(\theta_m,\partial_W\theta_m,\chi_m)
}
$$

where `\theta_m` is a typed source residue, `\partial_W\theta_m` is its
Ward/Bianchi boundary response, and `\chi_m` is its coupling to curvature or
clock/rod response.

Define:

$$
\boxed{
\operatorname{MassDef}_B(m)
=
\|\partial_W\theta_m\|
+\operatorname{TypeDrift}(\theta_m)
+\operatorname{CouplingDrift}(\chi_m).
}
$$

### Theorem 23: Mass Anchor Requires Source Typing

A mass/source anchor exists only when there is a typed source residue with
small Ward drift and stable coupling response:

$$
\boxed{
\operatorname{MassDef}_B(m)\le\epsilon_m.
}
$$

**Proof.**

Without typed source residue, the supposed mass anchor is merely an untyped
effect on records.  If Ward drift or coupling drift is large, the source
normalization is not stable enough to anchor `G_B`. `\square`

## 53. Opening Investigation D: Action/Phase Anchors

Action/phase anchors may be needed if the finite source sector is quantum-like
or interference-bearing.

Let:

$$
\boxed{
a=(\varphi_a,\mathcal I_a,\omega_a)
}
$$

where `\varphi_a` is a phase/interference residue, `\mathcal I_a` is the
interference carrier, and `\omega_a` is the projected state functional if it
exists.

Define:

$$
\boxed{
\operatorname{ActionDef}_B(a)
=
\operatorname{InterfDrift}(\varphi_a)
+\operatorname{StateDrift}(\omega_a)
+\operatorname{GaugeLeak}(a).
}
$$

### Theorem 24: Action Anchor Is QFT-Gated

An action/phase anchor is licensed only after the finite typed-net or
interference branch supplies stable phase/state residue.

**Proof.**

Action normalization cannot be read from pure order or pure dimensionless
geometry.  It requires either a stable interference residue or a typed
state/amplitude structure. `\square`

This couples issue 3 to issue 7.

## 54. Opening Investigation E: Vacuum Regions

Vacuum regions may have stable spacetime and even Einstein-like vacuum
residuals:

$$
\boxed{
\mathcal G_B^{fin}
+\Lambda_B^{fin}\mathfrak g_B^{fin}
\approx0.
}
$$

But a vacuum-only region cannot determine nonzero matter coupling `G_B`
without source or inherited boundary anchors.

### Theorem 25: Vacuum Scale Limitation

A bounded vacuum packet can inherit `G_B` from boundary/projective anchors, but
cannot generate a nontrivial source coupling from vacuum geometry alone.

**Proof.**

The coupling `G_B` multiplies source/stress.  If no source/stress response is
present in the bounded panel and no boundary/projective anchor imports it, the
source normalization remains free. `\square`

## 55. Opening Investigation F: Running Coupling

It may be that `G_B` does not converge immediately.  It may run with scale:

$$
\boxed{
G_B=G(\mu_B)
}
$$

where `\mu_B` is a finite record scale determined by the anchor packet.

This is not failure unless the target demands a scale-independent Newton
constant.  The correct classification is:

1. **unlicensed:** `\operatorname{ScaleDef}_B>0`;
2. **licensed running:** `\operatorname{ScaleDef}_B=0` but Cauchy convergence
   fails while scale dependence is typed;
3. **Newton-limit:** licensed and projectively Cauchy.

### Theorem 26: Running Coupling Classification

Every scale-anchored bounded region falls into exactly one of the three
classes above.

**Proof.**

If the anchor-rank gate fails, the coupling is unlicensed.  If it passes, the
finite coupling is licensed.  The projective Cauchy criterion then either
holds, giving a limit, or fails.  If it fails but the drift is typed by scale,
the coupling is running.  If untyped, the boundary/history panel is incomplete.
`\square`

## 56. Independent Hostile Review Round For Issue 3

### Review 1: "You still have not calculated Newton's number."

Accepted.  The campaign derives the finite licensing and limit criteria.  The
numerical value requires physical anchors and empirical calibration.

### Review 2: "Pure geometry should determine gravity."

Rejected at the finite scale level.  Pure dimensionless geometry can determine
shape and curvature-like ratios, not source normalization.  A source/action
anchor is needed for a numerical `G_B`.

### Review 3: "This makes issue 3 depend on issue 4 and issue 7."

Accepted.  That is a discovery, not a failure.  Scale anchoring has a
geometric side and a matter/source/action side.

### Review 4: "Clock and rod anchors sound like continuum smuggling."

Rejected if they are defined as record subsystems with recurrence and
interval-density stability.  Accepted if one imports external seconds/meters.
This campaign forbids the latter.

### Review 5: "A conventional unit choice could fake `G_B`."

Handled by anchor-rank closure.  If changing units changes `G_B` without
changing printed records, `G_B` is unlicensed.

### Review 6: "Near onset, anchors may not exist."

Accepted.  Then finite spacetime can be dimensionless and pre-Newtonian.
Scale-licensed gravity may onset later.

## 57. Issue 3 Final Theorem

### Theorem 27: Scale Anchor Closure

For a selected geometry-irreducible bounded-history carrier:

1. pure dimensionless geometry does not license a numerical `G_B`;
2. `G_B` is licensed exactly when record-realized anchors remove every
   `G_B`-changing unit-rescaling null direction;
3. a non-vacuum `G_B` requires source normalization through typed source
   residue or equivalent boundary/projective anchors;
4. `G_B\to G_\infty` exists exactly when licensed finite couplings are
   projectively Cauchy;
5. `G_\infty` may be identified with Newton's constant only after physical
   clock/rod/source/action anchors, Einstein residual convergence, and
   continuum representation all pass.

**Proof.**

Items 1 and 2 are Theorems 16 and 17.  Item 3 is Theorem 18 and the mass/source
anchor gate.  Item 4 is Theorem 19.  Item 5 is Theorem 20. `\square`

## 58. Updated Status After Issue 3

Issue 3 is closed as a finite licensing and limit theorem:

$$
\boxed{
\text{we know exactly when }G_B\text{ is meaningful and when }G_B\to G_\infty.
}
$$

It is not closed as a numerical derivation of Newton's constant:

$$
\boxed{
\text{we still need the physical source/action/clock anchor sectors.}
}
$$

That remaining work belongs mainly to issue 4 and issue 7.

The open list is now:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification; actual cosmological support remains issue 8;
3. **record-realized scale anchors and `G_\infty`:** closed as finite
   licensing/limit theorem; physical anchor construction remains coupled to
   issues 4 and 7;
4. **typed source/stress construction:** open;
5. **continuum convergence:** open;
6. **small Einstein residual on physical histories:** open;
7. **finite QFT typed net and amplitude/state rule:** open;
8. **initial-history projection weight charging onset:** open.

The next issue should be typed source/stress construction, because it supplies
the source normalization needed for non-vacuum `G_B` and for Einstein dynamics.

## 59. Issue 4 Campaign: Typed Source/Stress Construction

Issue 4 asks for a finite record-intrinsic construction of:

$$
\boxed{
\Theta_B^{fin}
}
$$

the typed source/stress packet used in:

$$
\boxed{
\mathcal G_B^{fin}
+\Lambda_B^{fin}\mathfrak g_B^{fin}
-8\pi G_B\Theta_B^{fin}.
}
$$

The danger is obvious.  We must not import continuum stress-energy, matter
fields, or QFT by name.  The packet must be built from record residues:

1. source-sensitive no-silent effects;
2. Ward/Bianchi boundary failures;
3. additive gluing behavior across bounded diamonds;
4. projective stability under history refinement;
5. scale-anchor compatibility when a numerical `G_B` is claimed.

The campaign target is:

$$
\boxed{
\text{derive the least finite typed source packet, and charge everything it
cannot type.}
}
$$

## 60. Source-Sensitive Residue Module

Let:

$$
\boxed{
\mathscr S_B
}
$$

be the finite module of source-sensitive residues.  An element:

$$
\boxed{
s\in\mathscr S_B
}
$$

is included when changing `s` changes at least one of the following above
tolerance:

1. loop/curvature-like response;
2. density/volume response;
3. clock/rod/source anchor response;
4. click target prediction;
5. Ward/Bianchi balance;
6. boundary work.

The finite Ward/Bianchi boundary map is:

$$
\boxed{
\partial_W:\mathscr S_B\to\mathscr W_B.
}
$$

Here `\mathscr W_B` is the finite Ward/Bianchi residue module: it records the
failure of source/curvature information to glue consistently across bounded
diamond boundaries.

## 61. Typed Source Dictionary

A typed source dictionary is:

$$
\boxed{
\Theta
=
\{(\tau_i,\theta_i,\partial_W\theta_i,\alpha_i)\}_{i\in I}.
}
$$

where:

- `\tau_i` is a stable type label;
- `\theta_i\in\mathscr S_B` is an additive source component;
- `\partial_W\theta_i` is its Ward/Bianchi boundary image;
- `\alpha_i` is its scale-anchor normalization data, if numerical coupling is
  claimed.

The dictionary is admissible when:

1. **typed stability:** `\tau_i` is preserved by same-actual quotienting;
2. **additivity:** components glue over disjoint or overlapping diamonds with
   controlled boundary correction;
3. **Ward compatibility:** `\partial_W` of the total component matches the
   printed Ward residue;
4. **projective stability:** deletion/refinement transports the dictionary;
5. **nonlookup:** the type is not a raw presentation tag;
6. **scale compatibility:** source normalization is tied to anchors when
   `G_B` is numerical.

## 62. Source Typing Defect

Let `s_B^{vis}` be the total visible source-sensitive residue in
`\mathscr S_B`.

For a typed dictionary `\Theta`, define:

$$
\boxed{
\operatorname{Approx}_B(\Theta)
=
\left\|
s_B^{vis}-\sum_i\theta_i
\right\|.
}
$$

Define Ward mismatch:

$$
\boxed{
\operatorname{WardDef}_B(\Theta)
=
\left\|
\partial_W s_B^{vis}
-\sum_i\partial_W\theta_i
\right\|.
}
$$

Define projective drift:

$$
\boxed{
\operatorname{ProjDef}_B(\Theta)
=
\sum_j
\left\|
\Theta_j-\rho_{j+1\to j}^{src}(\Theta_{j+1})
\right\|.
}
$$

Define nonlookup/type cost:

$$
\boxed{
\operatorname{TypeCost}_B(\Theta)
}
$$

as the finite description length of the typed dictionary after same-actual
quotienting, with raw presentation tags disallowed.

The total source typing defect is:

$$
\boxed{
\operatorname{SrcDef}_B
=
\inf_{\Theta}
\left[
\operatorname{Approx}_B(\Theta)
+\operatorname{WardDef}_B(\Theta)
+\operatorname{ProjDef}_B(\Theta)
+\chi_{raw}\operatorname{TypeCost}_B(\Theta)
\right].
}
$$

The least typed packet is:

$$
\boxed{
\Theta_B^\star
=
\arg\min_{\Theta}
\left[
\operatorname{Approx}_B(\Theta)
+\operatorname{WardDef}_B(\Theta)
+\operatorname{ProjDef}_B(\Theta)
+\chi_{raw}\operatorname{TypeCost}_B(\Theta)
\right].
}
$$

When `\operatorname{SrcDef}_B\le\epsilon_{src}`, define:

$$
\boxed{
\Theta_B^{fin}:=\Theta_B^\star.
}
$$

## 63. Theorem 28: Least Typed Source Packet Exists

If the bounded source-sensitive residue module `\mathscr S_B` is finite after
same-actual quotienting and raw presentation tags are excluded, then the least
typed packet `\Theta_B^\star` exists.

**Proof.**

The admissible typed dictionaries form a finite class once the bounded residue
module is finite, type labels are quotient-stable, and raw tags are excluded.
The displayed finite defect functional therefore attains a minimum. `\square`

## 64. Theorem 29: Source Typing Dichotomy

Every above-tolerance source-sensitive residue belongs to exactly one of:

1. typed Einstein source/stress packet `\Theta_B^{fin}`;
2. typed non-Einstein residual channel `R_B^{typed}`;
3. untyped charged residue `W_B^{untyped}`;
4. boundary-incomplete residue requiring boundary/history expansion;
5. anomalous Ward residue requiring an anomaly/topological channel.

**Proof.**

No-silent closure forbids omission.  If the residue is additively typed,
Ward-compatible, and scale-compatible, it enters the finite source packet.  If
it is stable but not Einstein-source-like, it is typed non-Einstein residue.
If visible but untyped, it remains charged.  If typing requires records
outside `B`, the boundary is incomplete.  If its Ward image is stable but
nonzero in a way that cannot be absorbed into ordinary source conservation, it
is anomalous/topological.  The cases are disjoint by their defining defects
and exhaustive by no-silent accounting. `\square`

## 65. Additivity And Gluing

A source packet must be additive under bounded-region gluing.  If:

$$
\boxed{
B=B_1\cup B_2
}
$$

with overlap `O=B_1\cap B_2`, define the gluing defect:

$$
\boxed{
\operatorname{GlueDef}_B(\Theta)
=
\left\|
\Theta_B-\Theta_{B_1}-\Theta_{B_2}+\Theta_O
\right\|.
}
$$

The stress packet is admissible only if:

$$
\boxed{
\operatorname{GlueDef}_B(\Theta)\le\epsilon_{glue}.
}
$$

### Theorem 30: Additivity Is Required For Stress Interpretation

If a typed residue is not additive under bounded diamond gluing up to boundary
correction, it cannot be interpreted as Einstein stress at that tolerance.

**Proof.**

Stress/source acts as a local density or flux-like packet.  If the same source
depends on how the bounded region is decomposed, it is not a local stress
packet; it is a boundary artifact, nonlocal typed residue, or incomplete
history effect. `\square`

## 66. Ward/Bianchi Compatibility

Einstein-like source must satisfy finite conservation compatibility.  Define:

$$
\boxed{
\operatorname{ConsDef}_B(\Theta)
=
\|\partial_W\Theta_B+\partial_W^{geom}\mathcal G_B^{fin}\|.
}
$$

Here `\partial_W^{geom}` is the Ward/Bianchi boundary map applied to the
finite curvature packet.

The conservation gate is:

$$
\boxed{
\operatorname{ConsDef}_B(\Theta)\le\epsilon_{cons}.
}
$$

### Theorem 31: Ward Compatibility Gate

Typed source residue enters `\Theta_B^{fin}` for Einstein dynamics only if its
Ward/Bianchi mismatch with the finite curvature packet is below tolerance.

**Proof.**

The finite Einstein equation cannot be projectively stable if curvature and
source boundary residues fail to match.  The mismatch would appear as
unbalanced no-silent residue under deletion/refinement or gluing. `\square`

## 67. Scale Compatibility

When `G_B` is numerical, source units must be anchored.  Define:

$$
\boxed{
\operatorname{ScaleSrcDef}_B(\Theta)
=
\dim\left(
\ker\mathsf A_B^{scale}
\cap
\mathcal U_B^{source}
\right).
}
$$

where `\mathcal U_B^{source}` is the source-normalization rescaling subspace
that changes `G_B\Theta_B^{fin}` while preserving dimensionless geometry.

The gate is:

$$
\boxed{
\operatorname{ScaleSrcDef}_B(\Theta)=0.
}
$$

### Theorem 32: Numerical Stress Requires Source Anchoring

If `\operatorname{ScaleSrcDef}_B>0`, the packet may be a dimensionless typed
source pattern, but it cannot supply numerical Einstein stress.

**Proof.**

A source rescaling null direction changes the numerical source normalization
without changing printed records.  Then `G_B\Theta_B^{fin}` is not record
fixed. `\square`

## 68. Classical Source Sector

A typed packet is classical at bounded tolerance when:

$$
\boxed{
\operatorname{ClassDef}_B(\Theta)
=
\operatorname{Var}_{proj}(\Theta)
+\operatorname{InterfResid}_B(\Theta)
+\operatorname{NoncommDef}_B(\Theta)
\le\epsilon_{cl}.
}
$$

Here:

- `\operatorname{Var}_{proj}` measures projected fluctuation over compatible
  histories;
- `\operatorname{InterfResid}` measures unresolved interference-like residue;
- `\operatorname{NoncommDef}` measures failure of source components to commute
  as committed records.

### Theorem 33: Classical Stress Gate

The packet `\Theta_B^{fin}` can be used as classical Einstein stress only if
`\operatorname{ClassDef}_B(\Theta_B^{fin})\le\epsilon_{cl}`.

If this fails but the residue is typed and state-compatible, the source is
quantum/inclusive and belongs to the QFT gate rather than the classical
Einstein gate.

**Proof.**

Classical stress is a committed finite packet.  Large projection variance,
interference residue, or noncommuting source components mean the source is not
a single classical record packet at the requested tolerance. `\square`

## 69. Quantum Or Inclusive Source Packet

When the source is not classical but is still typed, define:

$$
\boxed{
\Theta_B^{incl}
=
\omega_B(\widehat\Theta_B)
}
$$

where:

- `\widehat\Theta_B` is a finite typed source observable;
- `\omega_B` is a finite state/projection functional supplied by a typed net;
- `\Theta_B^{incl}` is the inclusive source response visible to the
  spacetime packet.

### Theorem 34: Inclusive Source Requires Typed State

An inclusive or expectation-like source packet is licensed only if
`\omega_B` is itself printed by a finite typed sector with projective state
compatibility.

**Proof.**

Otherwise the expectation value is hidden machinery.  Record-intrinsic source
typing requires the state/projection rule to be part of the bounded carrier
panel. `\square`

This couples issue 4 to issue 7:

$$
\boxed{
\text{classical sources can close before full QFT;}
\quad
\text{quantum/inclusive sources require finite typed-net state structure.}
}
$$

## 70. Source Packet And `G_B`

Issue 3 showed that non-vacuum `G_B` needs source normalization.  With
`\Theta_B^{fin}` constructed, define:

$$
\boxed{
\operatorname{MassAnchor}_B
=
\operatorname{Anchor}(\Theta_B^{fin},\mathcal S_B).
}
$$

The mass/source anchor is licensed when:

$$
\boxed{
\operatorname{SrcDef}_B
+\operatorname{ScaleSrcDef}_B
+\operatorname{ConsDef}_B
\le\epsilon_{mass}.
}
$$

### Theorem 35: Typed Source Supplies The Non-Vacuum Scale Anchor

If the source packet is typed, Ward-compatible, and scale-compatible, then it
supplies the source-normalization anchor required for non-vacuum `G_B`.

**Proof.**

The source packet fixes the record-visible unit of source response.  Ward
compatibility links it to curvature response.  Scale compatibility removes
source-rescaling null directions.  Therefore it is exactly the missing
non-vacuum anchor. `\square`

## 71. Boundary-Incomplete Sources

Some source effects are not local to `B`.  Define:

$$
\boxed{
\operatorname{BdySrcDef}_B(s)
}
$$

as the minimum residual source effect that changes predictions in `B` but is
not represented by records inside `B`.

If:

$$
\boxed{
\operatorname{BdySrcDef}_B(s)>\epsilon_{src},
}
$$

then `B` is not source-closed.

### Theorem 36: Boundary Source Expansion Rule

Above-tolerance boundary-incomplete source residue cannot be typed inside
`B`.  The boundary must expand, or the residue remains charged.

**Proof.**

Typing inside `B` would assign a local source carrier to an effect whose
distinguishing records lie outside `B`.  That is hidden reconstruction or
false locality. `\square`

## 72. Anomalies And Non-Einstein Typed Residues

A stable Ward residue may be real but not Einstein stress.  Define:

$$
\boxed{
\mathcal A_B^{anom}
=
\operatorname{Proj}_{anom}(\partial_Ws_B^{vis}).
}
$$

If:

$$
\boxed{
\|\mathcal A_B^{anom}\|>\epsilon_{anom},
}
$$

then the source sector is not ordinary conserved Einstein matter.  It is a
typed anomaly/topological/non-Einstein channel.

### Theorem 37: Anomalies Are Typed, Not Hidden

Stable above-tolerance Ward anomalies must be represented as typed residual
channels, not absorbed into `\Theta_B^{fin}`.

**Proof.**

Absorbing an anomalous Ward residue into conserved Einstein stress would make
the finite Bianchi/Ward gate falsely pass.  No-silent closure requires a
visible typed channel. `\square`

## 73. Full Source-Closure Defect

Define:

$$
\boxed{
\mathcal SDef_B
=
\operatorname{SrcDef}_B
+\operatorname{GlueDef}_B
+\operatorname{ConsDef}_B
+\operatorname{ScaleSrcDef}_B
+\operatorname{ClassDef}_B
+\operatorname{BdySrcDef}_B
+\|\mathcal A_B^{anom}\|.
}
$$

For classical Einstein source closure, require:

$$
\boxed{
\mathcal SDef_B\le\epsilon_{\Theta}.
}
$$

For inclusive/QFT-source closure, replace `\operatorname{ClassDef}` with the
finite typed-state defect from issue 7.

## 74. Theorem 38: Typed Source/Stress Closure

If:

$$
\boxed{
\mathcal SDef_B\le\epsilon_{\Theta},
}
$$

then the bounded record region has a finite typed classical source/stress
packet `\Theta_B^{fin}` suitable for the finite Einstein residual.

If all terms except `\operatorname{ClassDef}` are small, and a finite typed
state `\omega_B` exists with projective compatibility, then the region has an
inclusive source packet `\Theta_B^{incl}` suitable for a semiclassical or
QFT-gated Einstein residual.

If any source defect is above tolerance, the source is not closed at `B`.

**Proof.**

The terms of `\mathcal SDef_B` are exactly the obstructions to source/stress
interpretation: approximation, additivity, Ward compatibility, scale
normalization, classicality, boundary closure, and anomaly separation.  If
they are small, the least typed dictionary defines a stable source packet.  If
classicality alone fails but a typed state exists, the inclusive packet is
licensed.  If any obstruction remains, no-silent closure prevents using it as
Einstein matter. `\square`

## 75. Opening Investigation A: Can Source Typing Be Derived From Ward Data?

The strongest possible source theorem would derive type labels from Ward
residue alone.

Let:

$$
\boxed{
\mathcal Q_B^{Ward}
=
\operatorname{im}\partial_W
}
$$

be the finite Ward image.  Two source residues are Ward-equivalent when:

$$
\boxed{
s\sim_Ws'
\quad\Longleftrightarrow\quad
\partial_Ws=\partial_Ws'
\text{ up to same-actual nulls.}
}
$$

### Theorem 39: Ward Data Gives Charge Classes, Not Full Stress

Ward equivalence can define finite charge/source-conservation classes, but it
does not by itself determine the full stress packet unless the kernel of
`\partial_W` is typed or below tolerance.

**Proof.**

Ward data records boundary conservation behavior.  Stress also includes
interior pressure/energy/flux-like response.  Kernel components invisible to
`\partial_W` may still affect curvature or clicks.  They must be typed
separately or charged. `\square`

## 76. Opening Investigation B: Can Geometry Type The Source?

Maybe curvature response alone can classify sources.

Let:

$$
\boxed{
\mathcal C_B^{src}(s)
}
$$

be the curvature-response signature of source residue `s`.

### Theorem 40: Curvature Response Is Insufficient Without Degeneracy Control

Curvature response types source residue only if the map:

$$
\boxed{
s\mapsto\mathcal C_B^{src}(s)
}
$$

has a finite separated inverse on the source-sensitive quotient.

If two inequivalent source residues have the same curvature response but
different click, Ward, clock, or boundary effects, geometry alone cannot type
the source.

**Proof.**

A non-injective curvature response loses source information.  The missing
components are physically visible in other target channels, so they cannot be
silently identified. `\square`

## 77. Opening Investigation C: Can Classical Source Close Before QFT?

Yes, when source residues are committed records.

### Theorem 41: Committed Source Shortcut

If a bounded source sector has small `ClassDef`, stable additivity, Ward
compatibility, and scale-source anchoring, then classical `\Theta_B^{fin}` is
licensed without constructing the full QFT typed net.

**Proof.**

The source behaves as a committed finite record packet at the requested
tolerance.  QFT structure is unnecessary for that coarse-grained source
claim. `\square`

This is how ordinary macroscopic stress-energy can be a valid effective
source before microscopic QFT is reconstructed.

## 78. Opening Investigation D: Quantum Source Fork

If `ClassDef` is large but all typed-source and Ward defects are controlled,
there are two possibilities:

1. source is inclusive and requires `\omega_B`;
2. source cannot be closed at the requested boundary.

### Theorem 42: Quantum Source Fork

A nonclassical typed source is admissible for Einstein coupling only through a
finite typed state/projection functional.  Without it, the source remains
typed residue, not Einstein matter.

**Proof.**

The finite Einstein residual needs a definite source packet.  Nonclassical
typed residue does not supply one until a state/projection rule maps it to the
visible bounded source response. `\square`

## 79. Independent Hostile Review Round For Issue 4

### Review 1: "You smuggled in stress-energy."

Rejected.  The packet is defined from source-sensitive residues, gluing,
Ward/Bianchi maps, and scale anchors.  Continuum stress-energy is not assumed.

### Review 2: "The type labels are arbitrary."

Rejected if labels are required to be same-actual invariant, projectively
stable, additive, and nonlookup.  Accepted if labels are raw tags; those are
explicitly disallowed.

### Review 3: "Quantum matter cannot be classical stress."

Accepted.  The campaign separates classical committed source packets from
inclusive/QFT-gated source packets.

### Review 4: "Ward identities do not determine stress."

Accepted and handled by Theorem 39.  Ward data gives charge/conservation
classes, not full stress unless the kernel is controlled.

### Review 5: "Boundary sources can fake local matter."

Handled by the boundary source expansion rule.  Above-tolerance external
source residue cannot be localized inside `B`.

### Review 6: "Anomalies break Einstein closure."

Accepted.  Stable anomalies are typed residual channels.  They block ordinary
Einstein-source closure unless represented in the correct dynamics phase.

### Review 7: "This still depends on QFT."

Partly.  Classical committed sources can close before QFT.  Nonclassical or
inclusive sources require issue 7.

## 80. Issue 4 Final Theorem

### Theorem 43: Typed Source/Stress Packet Closure

For a selected geometry-irreducible bounded-history carrier:

1. the least typed source dictionary exists whenever the source-sensitive
   residue quotient is finite and raw labels are disallowed;
2. every visible source-sensitive residue is typed Einstein source, typed
   non-Einstein residue, untyped charged residue, boundary-incomplete residue,
   or anomaly/topological residue;
3. classical Einstein stress is licensed exactly when the full source-closure
   defect `\mathcal SDef_B` is below tolerance;
4. nonclassical inclusive source is licensed only with a finite typed
   state/projection functional;
5. untyped, boundary-incomplete, or anomalous residue cannot be silently used
   as Einstein matter.

**Proof.**

Item 1 is Theorem 28.  Item 2 is Theorem 29.  Additivity, Ward compatibility,
scale compatibility, classicality, boundary closure, and anomaly separation
are Theorems 30-37.  Inclusive source licensing is Theorems 34 and 42.
Together they give the stated closure. `\square`

## 81. Updated Status After Issue 4

Issue 4 is closed as a finite typed-source construction and obstruction
theorem:

$$
\boxed{
\text{we can construct the least typed source packet or classify why it fails.}
}
$$

It is not closed as a full microscopic matter/QFT derivation:

$$
\boxed{
\text{nonclassical source states and amplitudes remain issue 7.}
}
$$

The open list is now:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification; actual cosmological support remains issue 8;
3. **record-realized scale anchors and `G_\infty`:** closed as finite
   licensing/limit theorem; physical anchor construction partly supplied by
   issue 4 and partly by issue 7;
4. **typed source/stress construction:** closed as least typed-packet theorem;
   nonclassical states remain issue 7;
5. **continuum convergence:** open;
6. **small Einstein residual on physical histories:** open;
7. **finite QFT typed net and amplitude/state rule:** open;
8. **initial-history projection weight charging onset:** open.

The next natural issue is continuum convergence, because after spacetime,
scale, and source gates, we still need to show finite packets converge to a
smooth Lorentzian representation at the relevant tolerance.

## 82. Issue 5 Campaign: Continuum Convergence

Issue 5 asks when a sequence of finite spacetime packets deserves a continuum
readout:

$$
\boxed{
I_{GR}^{cl}(H_{B_n,k_n})
\longrightarrow
(M,g,\Theta)
}
$$

where:

- `I_{GR}^{cl}` is the finite GR/spacetime packet;
- `M` is a candidate manifold or manifold-like represented region;
- `g` is a Lorentzian metric-like field;
- `\Theta` is the represented source/stress packet when available.

The campaign must not confuse three different claims:

1. **finite spacetime:** geometry-irreducible carrier at tolerance;
2. **continuum-ready:** finite packets form a Cauchy/precompact represented
   family;
3. **smooth Lorentzian continuum:** the limiting readout has stable
   differentiable/manifold structure at the requested scale.

The target is:

$$
\boxed{
\text{derive finite defects whose summability is sufficient for continuum
representation, and classify failures.}
}
$$

## 83. Finite Packet Sequence

Let:

$$
\boxed{
\mathcal P_n
=
I_{GR}^{cl}(H_{B_n,k_n})
}
$$

be a projective sequence of finite spacetime packets with:

$$
\boxed{
B_1\subset B_2\subset\cdots,
\qquad
k_1\le k_2\le\cdots.
}
$$

Each packet contains:

1. interval/volume profile;
2. local center/diamond atlas;
3. overlap and transport data;
4. loop/curvature-like residues;
5. density/measure profile;
6. causal/order profile;
7. source/stress packet if typed;
8. deletion/refinement maps.

Let:

$$
\boxed{
\rho_{m\to n}^{cont}:\mathcal P_m\to\mathcal P_n
}
$$

be the projective comparison map for `m>n`.

## 84. Representation Candidates

A representation candidate for `\mathcal P_n` is:

$$
\boxed{
\Gamma_n(\mathcal P_n)
=
(M_n,g_n,\mu_n,\Theta_n,\mathcal A_n)
}
$$

where:

- `M_n` is a finite atlas/manifold patch candidate;
- `g_n` is a Lorentzian metric-like assignment on the patch;
- `\mu_n` is a measure/volume readout;
- `\Theta_n` is the represented source packet if available;
- `\mathcal A_n` is the atlas/transition system.

This is a readout, not an input.  It is licensed only if constructed from
record packet data.

Define a representation distance:

$$
\boxed{
d_{cont}(\Gamma_m,\Gamma_n)
}
$$

as a finite comparison of dimension, measure, atlas overlap, causal cones,
curvature/source residues, and projective transport.  No continuum metric is
assumed before the representation is licensed.

## 85. Continuum Defect Vector

Define the continuum defect vector:

$$
\boxed{
\mathcal CDef_n
=
\left(
D_n^{dim},
D_n^{dbl},
D_n^{atl},
D_n^{caus},
D_n^{sig},
D_n^{meas},
D_n^{curv},
D_n^{src},
D_n^{tail},
D_n^{proj}
\right).
}
$$

The components are:

1. `D^{dim}`: dimension drift across scales;
2. `D^{dbl}`: failure of finite doubling/volume regularity;
3. `D^{atl}`: atlas and overlap gluing error;
4. `D^{caus}`: causal/order-cone inconsistency;
5. `D^{sig}`: failure of stable Lorentzian signature readout;
6. `D^{meas}`: measure/density instability;
7. `D^{curv}`: curvature/loop-response instability;
8. `D^{src}`: source/stress representation instability;
9. `D^{tail}`: unresolved response tail;
10. `D^{proj}`: projective mismatch under refinement/deletion.

The scalar continuum defect is:

$$
\boxed{
\operatorname{ContDef}_n
=
\|\mathcal CDef_n\|_1.
}
$$

## 86. Theorem 44: Finite Continuum Cauchy Gate

If:

$$
\boxed{
\sum_{n=1}^{\infty}\operatorname{ContDef}_n<\infty,
}
$$

and the representation comparison maps are coherent:

$$
\boxed{
\rho_{m\to n}^{cont}\rho_{\ell\to m}^{cont}
=
\rho_{\ell\to n}^{cont}
\quad
\text{up to same-actual nulls,}
}
$$

then the represented packet sequence is Cauchy in `d_{cont}` and has a stable
continuum readout at the chosen tolerance.

**Proof.**

Each defect term bounds one source of representation drift between successive
packets.  Summability makes the total drift over the tail finite and
vanishing.  Coherent projective maps ensure all comparisons are made in the
same record-derived representation gauge.  Therefore the represented sequence
is Cauchy. `\square`

## 87. Dimension And Doubling Gates

For a finite packet, define the interval ball around center `x` at record
radius `r`:

$$
\boxed{
B_r(x)=\{y:d_{rec}(x,y)\le r\}.
}
$$

The finite dimension slope is:

$$
\boxed{
d_n(x,r)
=
\frac{\log |B_{2r}(x)|-\log |B_r(x)|}{\log 2}.
}
$$

Define:

$$
\boxed{
D_n^{dim}
=
\operatorname{Var}_{x,r\in\mathcal R_n}d_n(x,r).
}
$$

and:

$$
\boxed{
D_n^{dbl}
=
\sup_{x,r\in\mathcal R_n}
\left[
\frac{|B_{2r}(x)|}{|B_r(x)|}-C_{dbl}
\right]_+.
}
$$

### Theorem 45: Dimension-Doubling Necessity

If `D_n^{dim}` or `D_n^{dbl}` stays above tolerance along a projective tail,
then no stable finite-dimensional manifold representation is licensed on that
tail.

**Proof.**

A finite-dimensional manifoldlike region has stable local volume scaling and
finite doubling on bounded scales.  Persistent drift or unbounded doubling
means the finite packet cannot be represented by one stable local dimension at
that tolerance. `\square`

## 88. Atlas And Overlap Gate

Let `\mathcal A_n` be the record-derived finite atlas:

$$
\boxed{
\mathcal A_n=\{U_{\alpha},\psi_{\alpha},T_{\alpha\beta}\}.
}
$$

Here:

- `U_{\alpha}` are local diamond neighborhoods;
- `\psi_{\alpha}` are finite coordinate/readout labels constructed from
  record summaries;
- `T_{\alpha\beta}` are overlap transport maps.

The overlap cocycle defect is:

$$
\boxed{
D_n^{atl}
=
\sum_{\alpha,\beta,\gamma}
\|T_{\alpha\gamma}-T_{\beta\gamma}T_{\alpha\beta}\|.
}
$$

### Theorem 46: Nonlookup Atlas Gate

A continuum representation requires:

$$
\boxed{
D_n^{atl}\to0
}
$$

or summable `D_n^{atl}` along the projective tail.  Raw atlas lookup does not
count as a representation.

**Proof.**

Manifold representation requires compatible overlaps.  If the cocycle defect
persists, local patches do not glue.  If the gluing is supplied only by raw
lookup, the representation is reconstructive rather than record-intrinsic.
`\square`

## 89. Causal And Signature Gate

The finite causal/order packet must distinguish timelike, spacelike, and null
directions at tolerance.

Let:

$$
\boxed{
C_n(x)
}
$$

be the finite cone profile around center `x`, extracted from interval order,
boundary growth, and overlap transport.

Define the cone-stability defect:

$$
\boxed{
D_n^{caus}
=
\operatorname{Var}_{x,\alpha}
d_{cone}(C_n(x),T_{\alpha\beta}C_n(x)).
}
$$

Define the signature defect:

$$
\boxed{
D_n^{sig}
=
\operatorname{dist}
\left(
\operatorname{Inertia}(g_n^{fin}),
(1,d-1)
\right).
}
$$

### Theorem 47: Lorentzian Signature Gate

A smooth Lorentzian representation is licensed only if:

$$
\boxed{
D_n^{caus}+D_n^{sig}\to0
}
$$

or the corresponding defects are summable on the projective tail.

**Proof.**

Stable Lorentzian geometry is not just manifoldlike volume growth.  It needs a
stable causal cone and one-time-direction signature.  Persistent cone or
signature ambiguity means the packet may be geometric but not Lorentzian at
that tolerance. `\square`

## 90. Measure And Density Gate

Let `\mu_n` be the finite measure readout:

$$
\boxed{
\mu_n(U_{\alpha})=|U_{\alpha}|\cdot w_{\alpha}
}
$$

where `w_{\alpha}` is the record-derived density normalization.

Define:

$$
\boxed{
D_n^{meas}
=
\sum_{\alpha,\beta}
\left|
\mu_n(U_{\alpha}\cap U_{\beta})
-\mu_n(U_{\alpha})\cap_{\mu}\mu_n(U_{\beta})
\right|.
}
$$

### Theorem 48: Measure Compatibility Gate

If finite density/measure assignments are not compatible across overlaps, the
packet cannot license a single continuum volume element.

**Proof.**

A continuum volume element gives consistent measures on overlaps.  Persistent
overlap measure mismatch means the finite packet carries density modulation,
boundary incompleteness, or nonmanifold structure. `\square`

## 91. Curvature And Source Convergence Gate

Let:

$$
\boxed{
\mathcal R_n^{curv}
}
$$

be the finite loop/curvature response packet, and let:

$$
\boxed{
\Theta_n^{fin}
}
$$

be the typed source/stress packet when closed.

Define:

$$
\boxed{
D_n^{curv}
=
\|\mathcal R_{n+1}^{curv}
-\rho_{n+1\to n}^{curv}\mathcal R_n^{curv}\|.
}
$$

and:

$$
\boxed{
D_n^{src}
=
\|\Theta_{n+1}^{fin}
-\rho_{n+1\to n}^{src}\Theta_n^{fin}\|.
}
$$

### Theorem 49: Curvature/Source Representation Gate

Continuum GR representation requires curvature and typed-source packets to be
projectively Cauchy in the same atlas/anchor gauge.  If either packet has
unsummable drift, finite spacetime may exist but continuum Einstein
representation is not licensed.

**Proof.**

A continuum Einstein readout compares curvature and source fields over the
same represented region.  If either side fails projective convergence, no
stable field readout exists. `\square`

## 92. Response Tail And Boundary Gate

The finite packet may omit outside influence.  Define:

$$
\boxed{
D_n^{tail}
=
\sup_{\text{target }Y}
\left|
Y(H_{B_{\infty}})-Y(H_{B_n,k_n})
\right|_{proj}.
}
$$

This is not directly computable from an actual infinity, so the finite gate
uses boundary certificates:

$$
\boxed{
D_n^{tail}\le T_n^{cert}.
}
$$

where `T_n^{cert}` is the record-intrinsic tail certificate from boundary
work, source completion, and deletion drift.

### Theorem 50: Tail Certificate Gate

If:

$$
\boxed{
\sum_n T_n^{cert}<\infty,
}
$$

then unresolved boundary/history influence does not obstruct continuum
convergence.  If no certificate exists, continuum convergence is unlicensed.

**Proof.**

The certificate bounds the unmodeled contribution to each represented packet.
Summability prevents hidden outside influence from accumulating into a finite
representation mismatch. `\square`

## 93. Compactness Theorem For Representation Candidates

Define a representation family to be precompact when:

$$
\boxed{
\operatorname{PreComp}_n
=
D_n^{dim}+D_n^{dbl}+D_n^{atl}+D_n^{caus}
+D_n^{sig}+D_n^{meas}
\le\epsilon_{pc}
}
$$

uniformly on the projective tail.

### Theorem 51: Finite Precompactness Gate

Uniform precompactness plus summable projective defects gives a convergent
subsequence of continuum readouts.  If the projective limit is unique up to
same-actual nulls, the full sequence converges.

**Proof.**

The finite precompactness defects bound dimension, doubling, gluing, causal
signature, and measure behavior.  Therefore the representation candidates
cannot wander through infinitely many incompatible local structure types.
Summable projective defects make all tail subsequences mutually same-actual.
Uniqueness promotes subsequential convergence to full convergence. `\square`

## 94. Smoothness Level

Continuum convergence does not automatically mean smooth `C^\infty` geometry.
Define:

$$
\boxed{
\operatorname{Reg}_n^{(q)}
}
$$

as the finite regularity defect controlling derivatives or difference
operators up to order `q`.

The smoothness gate is:

$$
\boxed{
\sum_n\operatorname{Reg}_n^{(q)}<\infty
}
$$

for each required finite order `q`.

### Theorem 52: Smoothness Is Layered

Finite packets may license:

1. topological/manifoldlike representation;
2. continuous metric representation;
3. finite differentiability `C^q`;
4. smooth `C^\infty` only as a family of all finite-order regularity gates.

**Proof.**

Each regularity level requires its own finite difference controls.  Lower
levels do not imply higher levels. `\square`

## 95. Failure Classification

If continuum convergence fails, classify the failure:

1. **dimension failure:** `D^{dim}` or `D^{dbl}` persists;
2. **atlas failure:** `D^{atl}` persists or is raw/reconstructive;
3. **causal/signature failure:** `D^{caus}` or `D^{sig}` persists;
4. **measure failure:** `D^{meas}` persists;
5. **curvature/source failure:** `D^{curv}` or `D^{src}` is unsummable;
6. **tail failure:** no summable boundary/history certificate;
7. **regularity failure:** only lower-smoothness representation is licensed;
8. **topology-change/critical failure:** no unique projective representation
   type stabilizes.

### Theorem 53: Continuum Failure Is Typed

Every failure of continuum convergence is one of the listed typed failures,
provided the finite packet defects are no-silent complete.

**Proof.**

The continuum defect vector includes each finite obstruction needed for
representation: dimension, atlas, causality/signature, measure,
curvature/source, tail, regularity, and projective type.  If no-silent
completion holds, any above-tolerance obstruction appears in one of these
channels. `\square`

## 96. Opening Investigation A: Fractal Or Scale-Changing Limits

A packet may be stable but nonmanifoldlike, for example with scale-dependent
dimension.

### Theorem 54: Fractal Scale Drift Blocks Smooth Manifold Readout

If `d_n(x,r)` has no stable finite-dimensional plateau on the target scale
window, the sequence cannot license a smooth finite-dimensional manifold on
that window.

**Proof.**

A smooth finite-dimensional manifold has local dimension stability on
sufficiently small but represented scales.  Persistent scale drift contradicts
that requirement. `\square`

## 97. Opening Investigation B: Graph-Like Or Algebraic Limits

Cayley-like or expander-like packets can be stable without being manifoldlike.

### Theorem 55: Algebraic Stability Is Not Continuum Geometry

Projective stability of a non-geometric algebraic carrier does not license a
continuum manifold unless the continuum defect vector is summable.

**Proof.**

Stability only says the carrier persists.  Continuum representation requires
the specific dimension, atlas, causal, measure, and tail gates. `\square`

## 98. Opening Investigation C: Topology Change

A sequence may pass local tests but change global patching type.

Define:

$$
\boxed{
D_n^{top}
=
d_{top}(\mathcal A_{n+1},\rho_{n+1\to n}\mathcal A_n).
}
$$

### Theorem 56: Topology Change Requires Critical Label Or Boundary Expansion

If `D_n^{top}` is above tolerance infinitely often, the sequence does not
license a single continuum topology.  It must be represented as a critical
topology-changing phase or with expanded boundary/history data.

**Proof.**

A single continuum patch has stable overlap topology.  Persistent topological
drift means the represented object changes type. `\square`

## 99. Opening Investigation D: Singular Or Horizon Regimes

Near singular/horizon-like regimes, tail, causal, or curvature defects may not
be summable.

### Theorem 57: Critical Regions Are Not Failures Of The Click Law

If continuum defects fail only in a bounded critical region, the click law can
remain valid while smooth continuum representation is suspended or weakened
there.

**Proof.**

The click law selects finite carriers.  Smooth continuum representation is a
later gate.  Failure of the later gate classifies the region as critical; it
does not invalidate the history-first carrier law. `\square`

## 100. Opening Investigation E: FLRW-Like Cosmology

For an FLRW-like readout, the finite packet sequence must have stable
homogeneous/isotropic large-scale profiles.

Define:

$$
\boxed{
D_n^{FLRW}
=
D_n^{hom}+D_n^{iso}+D_n^{scale-factor}+D_n^{source-fluid}.
}
$$

### Theorem 58: FLRW Representation Gate

An FLRW-like continuum readout is licensed only if the ordinary continuum
defects are controlled and:

$$
\boxed{
\sum_nD_n^{FLRW}<\infty
}
$$

where `D_n^{FLRW}` denotes the displayed FLRW defect.

**Proof.**

FLRW is not just any continuum representation; it requires stable homogeneous,
isotropic, scale-factor, and source-fluid readouts.  These are additional
finite defects. `\square`

## 101. Independent Hostile Review Round For Issue 5

### Review 1: "You smuggled in manifolds via `M_n`."

Rejected.  `M_n` is a candidate readout constructed from finite packet data.
It is licensed only after finite defects pass.  It is not input ontology.

### Review 2: "Cauchy readout may converge to a non-smooth object."

Accepted.  Smoothness is layered by finite regularity defects.  Continuum
readout can be topological, continuous, `C^q`, or smooth depending on gates.

### Review 3: "Summability is strong."

Accepted.  It is a sufficient condition.  Weaker compactness-plus-subsequence
conditions can license subsequential readouts, but full stable physical
representation needs uniqueness or projective Cauchy control.

### Review 4: "Lorentzian signature may fail near onset."

Accepted.  Then the region is finite spacetime-like or pre-Lorentzian, not
smooth Lorentzian spacetime at that tolerance.

### Review 5: "Physical large-scale packets might not satisfy the gates."

Accepted.  The campaign gives the gate and failure classification.  Proving
actual large-scale physical packets pass it is tied to issue 8 and empirical
cosmological support.

### Review 6: "Continuum convergence should come before Einstein dynamics."

Mostly accepted.  Einstein-ready finite packets can be studied first, but
continuum Einstein equations require continuum representation convergence.

## 102. Issue 5 Final Theorem

### Theorem 59: Continuum Convergence Closure

For a projective sequence of selected geometry-irreducible finite packets:

1. summable continuum defects give a Cauchy continuum readout;
2. uniform finite precompactness gives convergent subsequences;
3. uniqueness up to same-actual nulls gives full sequence convergence;
4. Lorentzian representation requires causal/signature gates;
5. smoothness requires finite regularity gates at the desired orders;
6. failures are typed as dimension, atlas, causal/signature, measure,
   curvature/source, tail, regularity, topology-change, or critical defects.

**Proof.**

Items 1-3 are Theorems 44 and 51.  Item 4 is Theorem 47.  Item 5 is Theorem
52.  Item 6 is Theorem 53 and the opening investigations. `\square`

## 103. Updated Status After Issue 5

Issue 5 is closed as a finite continuum-convergence gate and failure
classification:

$$
\boxed{
\text{we know when finite packets license continuum/Lorentzian/smooth
readouts, and what kind of failure occurs otherwise.}
}
$$

It is not closed as proof that the actual universe's large-scale packets pass
the gate:

$$
\boxed{
\text{physical large-scale convergence remains a cosmological/empirical
support problem.}
}
$$

The open list is now:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification; actual cosmological support remains issue 8;
3. **record-realized scale anchors and `G_\infty`:** closed as finite
   licensing/limit theorem; physical anchor construction partly supplied by
   issues 4 and 7;
4. **typed source/stress construction:** closed as least typed-packet theorem;
   nonclassical states remain issue 7;
5. **continuum convergence:** closed as finite convergence/readout gate;
   actual physical satisfaction remains issue 8 and empirical support;
6. **small Einstein residual on physical histories:** open;
7. **finite QFT typed net and amplitude/state rule:** open;
8. **initial-history projection weight charging onset:** open.

The next natural issue is the small Einstein residual on physical histories:
after spacetime, scale, source, and continuum gates, the question becomes why
the selected histories make the finite Einstein residual small rather than
merely definable.

## 104. Issue 6 Campaign: Small Einstein Residual On Physical Histories

Issue 6 asks why selected physical histories should satisfy:

$$
\boxed{
\mathcal E_B^{Ein}(K_B^\star)\le\epsilon_{Ein}.
}
$$

The previous issues made this expression meaningful:

1. issue 1 calibrated the selector;
2. issue 2 classified geometry flow;
3. issue 3 licensed `G_B`;
4. issue 4 constructed typed source packets;
5. issue 5 licensed continuum/Lorentzian readouts.

But meaningful is not the same as true.  Issue 6 is the dynamics question.

The campaign target is:

$$
\boxed{
\text{derive small Einstein residual from finite stationarity of selected
bounded histories, or classify the obstruction.}
}
$$

## 105. Finite Einstein Residual

For an Einstein-ready bounded carrier `K`, define:

$$
\boxed{
E_B^{Ein}(K)
=
\mathcal G_B^{fin}(K)
+\Lambda_B^{fin}\mathfrak g_B^{fin}(K)
-8\pi G_B\Theta_B^{fin}(K).
}
$$

The full finite Einstein residual is:

$$
\boxed{
\mathcal E_B^{Ein}(K)
=
\|E_B^{Ein}(K)\|_B
+\|W_B^{untyped}\|
+\|R_B^{typed}\|
+\|R_B^{tail}\|.
}
$$

Here:

- `W_B^{untyped}` is untyped Ward/source residue;
- `R_B^{typed}` is typed non-Einstein residue, such as higher curvature,
  torsion, anomaly, or nonclassical source response;
- `R_B^{tail}` is unresolved boundary/history tail.

Small residual means:

$$
\boxed{
\text{curvature, source, scale, tail, and typed-residual channels close as an
Einstein phase.}
}
$$

## 106. Boundary-Work Action

Define the total finite boundary-work action:

$$
\boxed{
\mathcal A_B^{BW}(H,K)
=
\mathcal A_B^{cal}(H,K)
+\alpha_{GI}\Phi_B^{GI}(K)
+\alpha_{\Theta}\mathcal SDef_B(K)
+\alpha_C\operatorname{ContDef}_B(K)
+\alpha_E\mathcal E_B^{Ein}(K).
}
$$

This is not an imported Hilbert action.  It is a finite record action whose
terms are the already-defined closure defects.

The Einstein residual is small only if the selected carrier is not merely a
minimum of description length, but an interior stationary point of the total
boundary-work problem after the geometry/source/scale/continuum gates are
active.

## 107. Admissible Variation Cone

Let:

$$
\boxed{
\mathcal V_B^{Ein}(K)
}
$$

be the finite cone of admissible variations preserving:

1. same-actual quotienting;
2. calibrated feasibility gates;
3. geometry-irreducibility below tolerance;
4. source typing below tolerance;
5. scale-anchor rank closure;
6. continuum readout gauge;
7. bounded history cylinder.

A variation:

$$
\boxed{
u\in\mathcal V_B^{Ein}(K)
}
$$

changes finite metric/atlas/source/curvature components while staying inside
the Einstein-ready phase.

Define stationarity defect:

$$
\boxed{
\operatorname{Stat}_B^{Ein}(K)
=
\sup_{\substack{u\in\mathcal V_B^{Ein}(K)\\\|u\|=1}}
|\delta_u\mathcal A_B^{BW}(H,K)|.
}
$$

For discrete carrier moves, replace `\delta_u` by finite differences.

## 108. Residual-Separating Variations

The variation cone must see the residual.  Define the separation constant:

$$
\boxed{
C_B^{sep}
=
\inf\left\{
C:
\|R\|_B
\le
C\sup_{\|u\|=1}|\langle R,u\rangle|
\right\}.
}
$$

The infimum ranges over residuals in the Einstein residual subspace after
same-actual null quotienting.

If `C_B^{sep}` is infinite, the finite variations do not detect all residual
directions.  Then stationarity cannot imply small Einstein residual.

## 109. First Variation Identity

For an Einstein-ready interior carrier, the first variation has the finite
form:

$$
\boxed{
\delta_u\mathcal A_B^{BW}
=
\left\langle
E_B^{Ein}(K),u
\right\rangle
+\left\langle
W_B^{untyped}+R_B^{typed}+R_B^{tail},u
\right\rangle
+\operatorname{Rem}_B(u).
}
$$

The remainder satisfies:

$$
\boxed{
|\operatorname{Rem}_B(u)|
\le
C_B^{(2)}\|u\|^2
}
$$

inside the finite linearized tolerance window.

## 110. Theorem 60: Interior Stationarity Gives Small Einstein Residual

Assume:

1. `K_B^\star` is geometry-irreducible;
2. `G_B` is licensed;
3. `\Theta_B^{fin}` is typed or inclusive with a licensed state;
4. continuum representation is licensed at the requested level;
5. `K_B^\star` is an interior stationary point of `\mathcal A_B^{BW}`;
6. `C_B^{sep}<\infty`;
7. typed/tail residues are either below tolerance or charged outside the
   Einstein sector;
8. the second variation remainder is bounded.

Then:

$$
\boxed{
\mathcal E_B^{Ein}(K_B^\star)
\le
C_B^{sep}\operatorname{Stat}_B^{Ein}(K_B^\star)
+C_B^{(2)}\|u\|^2
+\epsilon_{typed/tail}.
}
$$

In the finite linearized tolerance window, the selected history is
Einstein-obeying:

$$
\boxed{
\mathcal E_B^{Ein}(K_B^\star)\le\epsilon_{Ein}.
}
$$

**Proof.**

Interior stationarity bounds the first variation for every admissible
Einstein-phase variation.  The first variation identity identifies that
linear functional with the Einstein residual plus charged non-Einstein
channels and second-order remainder.  Residual separation converts small
pairing against all variations into small residual norm. `\square`

## 111. Theorem 61: Boundary Obstruction Dichotomy

If `K_B^\star` is selected but not an interior stationary point, then exactly
one of the following obstructions is printed:

1. boundary/history incompleteness;
2. source untyped or nonclassical without state;
3. scale anchors unlicensed;
4. continuum representation not licensed;
5. non-Einstein typed residual dominates;
6. phase tie or topology/critical transition;
7. variation cone fails to separate residuals.

In any of these cases, small Einstein residual is not forced.

**Proof.**

If a variation needed for stationarity is blocked, no-silent closure requires
the blocking reason to appear in the finite defect ledger.  The listed
obstructions are exactly the active gates from issues 3-5 and the residual
separation gate. `\square`

## 112. Theorem 62: Higher-Curvature Phase Separation

If a typed residual channel `R_B^{typed}` is stable and above tolerance, then
the selected history is not in the Einstein phase unless that channel is
irrelevant at the selected scale or absorbed into an explicitly licensed
Einstein-sector redefinition.

**Proof.**

Typed non-Einstein residue is visible record data.  Absorbing it silently into
the Einstein residual would make the finite equation pass by hiding a real
channel.  Therefore it either becomes a typed non-Einstein dynamics phase or
is shown below tolerance. `\square`

## 113. Theorem 63: Vacuum Einstein Phase

If the typed source packet is absent or zero, `G_B` need not be non-vacuum
licensed.  A vacuum Einstein phase is licensed when:

$$
\boxed{
\|\mathcal G_B^{fin}+\Lambda_B^{fin}\mathfrak g_B^{fin}\|_B
+\|R_B^{typed}\|+\|R_B^{tail}\|
\le\epsilon_{vac}.
}
$$

**Proof.**

In vacuum, the source term is absent.  The finite equation is a curvature plus
cosmological/integration-constant packet.  Non-vacuum source normalization is
not needed, but curvature scale and continuum representation still must be
record-licensed for numerical claims. `\square`

## 114. Theorem 64: Semiclassical Source Fork

If the source packet is inclusive:

$$
\boxed{
\Theta_B^{incl}=\omega_B(\widehat\Theta_B),
}
$$

then small Einstein residual is licensed only if:

1. `\omega_B` is projectively stable;
2. the inclusive source has small Ward/source defect;
3. source fluctuations not represented in `\Theta_B^{incl}` are below
   tolerance or typed as noise/backreaction residue.

Otherwise the region is QFT-source incomplete rather than Einstein-obeying.

**Proof.**

An inclusive source is not a committed classical record packet.  It becomes an
Einstein source only through a stable projection/state functional and
controlled residual fluctuations. `\square`

## 115. Theorem 65: Projective Einstein Stability

Let:

$$
\boxed{
\Delta_B^{Ein}
=
\sum_j
\|E_{B,j}^{Ein}
-\rho_{j+1\to j}^{Ein}E_{B,j+1}^{Ein}\|.
}
$$

If:

$$
\boxed{
\mathcal E_{B,j}^{Ein}\le\epsilon_j
\quad\text{and}\quad
\sum_j\epsilon_j+\Delta_B^{Ein}<\infty,
}
$$

then Einstein residual smallness is a bounded-history property rather than a
one-slice coincidence.

**Proof.**

The residual is small at each depth and coherent under history projection.
Summability prevents accumulated drift from producing a different limiting
dynamics. `\square`

## 116. Opening Investigation A: Can Selector Minimality Alone Prove Einstein?

No.

### Theorem 66: Selector Minimality Alone Is Insufficient

Calibrated carrier minimality does not imply small Einstein residual unless
the selector action includes the Einstein boundary-work channel and the
selected carrier is interior stationary with separating variations.

**Proof.**

A carrier may be the shortest feasible predictor for click/spacetime targets
while having stable non-Einstein typed curvature/source residue.  Minimality
of description length alone does not set the Einstein residual to zero.
`\square`

## 117. Opening Investigation B: Can Continuum GR Be Used To Prove The Gate?

No, not as an input.

### Theorem 67: Continuum Einstein Equations Cannot Be Imported

If small finite Einstein residual is justified by assuming continuum Einstein
equations on the represented manifold, the derivation is circular.

**Proof.**

Issue 6 is the bridge from finite record histories to Einstein dynamics.  Using
continuum Einstein dynamics as a premise assumes the target conclusion.
`\square`

Continuum GR can be used later as a comparison after the finite residual is
shown small.

## 118. Opening Investigation C: Does Least Boundary Work Select Einstein
Over Higher Curvature?

Only in a low-energy/low-response sector.

Define:

$$
\boxed{
\operatorname{HCDef}_B
=
\|R_B^{higher-curv}\|.
}
$$

### Theorem 68: Low-Energy Einstein Sector

If higher-curvature/torsion/anomaly typed residues are below tolerance in the
selected scale window, and the interior stationarity theorem applies, then the
least boundary-work dynamics reduces to the Einstein residual.

If `\operatorname{HCDef}_B` is above tolerance, the selected dynamics is
non-Einstein or mixed.

**Proof.**

The finite variation identity separates Einstein and typed non-Einstein
channels.  When non-Einstein channels are below tolerance, the remaining
stationary residual is Einstein.  Otherwise those channels remain visible.
`\square`

## 119. Opening Investigation D: Boundary Or Horizon Regimes

Boundary/horizon-like regions often fail interior stationarity.

### Theorem 69: Horizon/Critical Obstruction

If the residual variation cone is one-sided because the selected carrier lies
on an active causal, boundary, or topology-change constraint, small Einstein
residual is not forced by stationarity.

**Proof.**

One-sided constrained minima satisfy inequalities with active multipliers, not
zero residual equations.  The active multiplier is a physical boundary or
critical residue. `\square`

## 120. Opening Investigation E: Cosmological Constant Channel

The cosmological term is not a fudge factor.  It is licensed only if the trace
or vacuum-source residue is stable and projective.

Define:

$$
\boxed{
\Lambda_B^{fin}
=
\Gamma_{\Lambda}(R_B^{trace},\mathfrak g_B^{fin})
}
$$

when the trace/vacuum residue is typed and anchor-compatible.

### Theorem 70: Cosmological Packet Gate

`\Lambda_B^{fin}` may enter the Einstein residual only when the uniform
trace/vacuum source channel is typed, projectively stable, and separated from
ordinary matter source residue.

**Proof.**

Otherwise an arbitrary trace term could absorb untyped source, higher-curvature
residue, or boundary error.  No-silent closure forbids that. `\square`

## 121. Opening Investigation F: Actual Physical Histories

Define the Einstein-obeying physical class:

$$
\boxed{
\mathsf P_{Ein}
}
$$

as selected bounded histories satisfying:

1. geometry-irreducibility;
2. scale anchoring or vacuum-appropriate scale licensing;
3. typed source closure;
4. continuum/Lorentzian readout gate;
5. interior boundary-work stationarity;
6. residual-separating variation cone;
7. sub-tolerance typed non-Einstein and tail residues;
8. projective Einstein stability.

### Theorem 71: Physical Einstein Class

Every selected history in `\mathsf P_{Ein}` is Einstein-obeying at tolerance.

**Proof.**

The assumptions are exactly the hypotheses of Theorems 60, 62, 64, and 65,
with the obstruction gates excluded. `\square`

This does not prove:

$$
\boxed{
\text{the actual universe always lies in }\mathsf P_{Ein}.
}
$$

It proves the finite class for which Einstein dynamics follows.

## 122. Independent Hostile Review Round For Issue 6

### Review 1: "You only proved Einstein under many conditions."

Accepted.  Those conditions are precisely the finite gates needed to make the
claim non-circular.  Outside them, the correct answer is not Einstein.

### Review 2: "This does not prove the actual residual is small everywhere."

Accepted.  It proves the Einstein-obeying class and obstruction taxonomy.
Global or cosmological prevalence remains issue 8.

### Review 3: "Boundary-work action was chosen to include Einstein residual."

Partly accepted.  The action includes all finite closure channels.  The
Einstein residual channel is not arbitrary; it is the already-licensed
curvature/source mismatch after issues 3-5.  But a deeper derivation of the
relative importance of dynamics channels belongs to the physical history
weight/prior.

### Review 4: "Higher-curvature gravity could be fundamental."

Accepted.  Then the selected history is in a typed non-Einstein dynamics
phase, not a failed click law.

### Review 5: "QFT sources are unresolved."

Accepted.  Nonclassical source closure requires issue 7.  Until then,
semiclassical Einstein residuals are licensed only for inclusive typed-state
packets that pass Theorem 64.

### Review 6: "Singularities break the theorem."

Accepted.  They are boundary/critical phases where interior stationarity is
not available.

## 123. Issue 6 Final Theorem

### Theorem 72: Einstein Residual Closure

For selected bounded histories, small finite Einstein residual is derived
exactly in the interior Einstein-obeying class `\mathsf P_{Ein}`.  Outside
that class, the failure is typed as:

1. boundary/history incompleteness;
2. source untyped or QFT-state incomplete;
3. scale unlicensed;
4. continuum representation failure;
5. higher-curvature/torsion/anomaly dynamics;
6. cosmological/trace channel untyped;
7. residual-separation failure;
8. projective Einstein instability;
9. critical/horizon/topology-change regime.

**Proof.**

Inside `\mathsf P_{Ein}`, Theorem 60 gives small residual and Theorem 65 makes
it history-stable.  The remaining theorems classify every obstruction:
boundary obstruction, non-Einstein typed residue, vacuum/semiclassical forks,
higher-curvature sectors, cosmological packet failure, and critical regimes.
`\square`

## 124. Updated Status After Issue 6

Issue 6 is closed as a finite Einstein-dynamics theorem:

$$
\boxed{
\text{selected histories make the Einstein residual small exactly in the
interior Einstein-obeying class.}
}
$$

It is not closed as a claim that all physical histories are Einstein-obeying:

$$
\boxed{
\text{actual prevalence of }\mathsf P_{Ein}\text{ remains issue 8, and
nonclassical sources remain issue 7.}
}
$$

The open list is now:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification; actual cosmological support remains issue 8;
3. **record-realized scale anchors and `G_\infty`:** closed as finite
   licensing/limit theorem; physical anchor construction partly supplied by
   issues 4 and 7;
4. **typed source/stress construction:** closed as least typed-packet theorem;
   nonclassical states remain issue 7;
5. **continuum convergence:** closed as finite convergence/readout gate;
   actual physical satisfaction remains issue 8 and empirical support;
6. **small Einstein residual on physical histories:** closed as finite
   interior-stationarity theorem; actual prevalence remains issue 8 and QFT
   source completion remains issue 7;
7. **finite QFT typed net and amplitude/state rule:** open;
8. **initial-history projection weight charging onset:** open.

The next natural issue is the finite QFT typed net and amplitude/state rule,
because it is now the main remaining obstruction to nonclassical source
closure and microscopic matter dynamics.

## 125. Issue 7 Campaign: Finite QFT Typed Net And Amplitude/State Rule

Issue 7 asks for the finite nonclassical matter layer.

The previous issues allow:

$$
\boxed{
\text{spacetime carrier}
+\text{scale anchors}
+\text{classical source packet}
+\text{continuum readout}
+\text{Einstein residual gate}.
}
$$

But nonclassical matter still requires:

1. typed local algebras;
2. finite state/projection rules;
3. locality or typed entanglement discipline;
4. Ward/source compatibility;
5. exchange/occupation sectors;
6. gauge-null directions;
7. dynamics or Schwinger-Dyson/Ward stationarity;
8. an amplitude/decoherence rule if committed positive histories cannot carry
   stable interference residue.

The issue-7 target is:

$$
\boxed{
\text{construct the least finite QFT-ready typed net, or classify exactly why
it is not licensed.}
}
$$

## 126. Local Diamond Net

Let:

$$
\boxed{
\mathcal D_B
}
$$

be the finite family of bounded diamonds inside the selected spacetime carrier
`K_B^\star`.

For each diamond `D\in\mathcal D_B`, define the local typed generator set:

$$
\boxed{
\mathcal T_D
=
\{\tau:\tau\text{ is a stable typed residue supported in }D\}.
}
$$

The local typed algebra is:

$$
\boxed{
\mathfrak A_D
=
\operatorname{Alg}(\mathcal T_D).
}
$$

This algebra is finite.  Its generators are not continuum fields; they are
typed record residues: source charges, exchange labels, interference sectors,
soft/inclusive carriers, gauge-null moves, and local detector/source
responses.

## 127. Net Conditions

A finite typed net is:

$$
\boxed{
\mathfrak A_B
=
\{(\mathfrak A_D,\iota_{D_1D_2},\omega_D):D\in\mathcal D_B\}.
}
$$

Here:

- `\iota_{D_1D_2}:\mathfrak A_{D_1}\to\mathfrak A_{D_2}` is the inclusion map
  for `D_1\subset D_2`;
- `\omega_D` is the finite state/projection functional on `\mathfrak A_D`.

The net defects are:

$$
\boxed{
\begin{aligned}
N_B^{iso}&=\text{isotony/inclusion failure},\\
N_B^{state}&=\text{projective state incompatibility},\\
N_B^{loc}&=\text{locality or typed-entanglement failure},\\
N_B^{Ward}&=\text{Ward/source mismatch},\\
N_B^{dyn}&=\text{finite dynamics/Ward-SD failure},\\
N_B^{gauge}&=\text{non-null gauge-like motion},\\
N_B^{occ}&=\text{unstable occupation/exchange sector},\\
N_B^{amp}&=\text{unresolved interference/amplitude residue}.
\end{aligned}
}
$$

The total QFT-readiness defect is:

$$
\boxed{
\mathcal QDef_B
=
N_B^{iso}
+N_B^{state}
+N_B^{loc}
+N_B^{Ward}
+N_B^{dyn}
+N_B^{gauge}
+N_B^{occ}
+N_B^{amp}.
}
$$

## 128. Finite State From Projected Histories

For committed record histories, define:

$$
\boxed{
\omega_D(a)
=
\frac{\sum_{H\in\mathcal H_D}w_D(H)a(H)}
{\sum_{H\in\mathcal H_D}w_D(H)}.
}
$$

Here:

- `\mathcal H_D` is the bounded history cylinder restricted to `D`;
- `w_D(H)` is the calibrated projected history weight;
- `a\in\mathfrak A_D` is a typed observable on committed records.

This is a positive committed-history state.  It is not yet an amplitude.

Projective state compatibility is:

$$
\boxed{
|\omega_{D_2}(\iota_{D_1D_2}a)-\omega_{D_1}(a)|
\le\epsilon_{\omega}
}
$$

for all tested `a\in\mathfrak A_{D_1}`.

## 129. Theorem 73: Least Finite Typed Net Exists

If the finite typed residue quotient is finite after same-actual quotienting
and raw labels are disallowed, then a least finite typed net exists by
minimizing:

$$
\boxed{
\mathcal C_B^{QFT}
=
L(\mathfrak A_B)
+\chi_{iso}N_B^{iso}
+\chi_{state}N_B^{state}
+\chi_{loc}N_B^{loc}
+\chi_{Ward}N_B^{Ward}
+\chi_{dyn}N_B^{dyn}
+\chi_{gauge}N_B^{gauge}
+\chi_{occ}N_B^{occ}
+\chi_{amp}N_B^{amp}.
}
$$

**Proof.**

The admissible typed-net class is finite after quotienting and raw-label
exclusion.  The cost is finite on admissible nets and charges every
above-tolerance obstruction.  Therefore a minimizer exists. `\square`

## 130. Theorem 74: QFT-Readiness Gate

If:

$$
\boxed{
\mathcal QDef_B\le\epsilon_Q,
}
$$

then `B` supports a finite QFT-ready typed net over the selected spacetime
carrier.

If any summand is above tolerance, the finite QFT layer is not licensed until
the corresponding obstruction is typed, boundary-expanded, or moved to an
amplitude/decoherence layer.

**Proof.**

The eight defects are exactly the finite prerequisites of a QFT-ready net:
local algebras, compatible states, locality/entanglement discipline,
Ward/source compatibility, dynamics, gauge-null structure, occupation/exchange
stability, and interference handling. `\square`

## 131. Locality Versus Typed Entanglement

Locality should not erase entanglement.  Define the finite locality defect:

$$
\boxed{
N_B^{loc}
=
\sum_{D_1\perp D_2}
\|[a_{D_1},b_{D_2}]\|_{\omega}
-\operatorname{EntTyped}(D_1,D_2).
}
$$

Here:

- `D_1\perp D_2` means record-causally independent in the selected carrier;
- `\operatorname{EntTyped}` subtracts stable typed entanglement/shared-carrier
  channels already printed in the bounded panel.

### Theorem 75: Locality With Typed Entanglement

Record-causally separated sectors must commute up to tolerance after
conditioning on printed shared carriers.  Nonlocal correlations are allowed
only when typed as entanglement/shared-residue sectors.

**Proof.**

Unprinted nonlocal influence would violate no-silent closure.  Printed shared
carriers are part of the typed algebra, so they are not locality violations;
they are explicit nonclassical structure. `\square`

## 132. Ward/Charge Gate

Typed charges are generated by finite Ward/Bianchi residues.

Let:

$$
\boxed{
Q_{\tau}(D)
=
\int_D^{fin}\partial_W\tau.
}
$$

This is finite notation for the Ward/Bianchi residue carried by type `\tau`.

The Ward defect is:

$$
\boxed{
N_B^{Ward}
=
\sum_D
\left\|
\partial_W\Theta_D
-\sum_{\tau\in\mathcal T_D}Q_{\tau}(D)
\right\|.
}
$$

### Theorem 76: Ward Residues Generate Finite Charges

If a typed sector has stable additive Ward residue, then it defines a finite
charge/source component.  If Ward residue is untyped or nonadditive, the
sector is anomalous, boundary-incomplete, or not QFT-ready.

**Proof.**

Charge is the stable additive quantity transported through the Ward/Bianchi
map.  Without additivity and projective stability, there is no conserved
finite charge. `\square`

## 133. Dynamics Gate: Finite Ward/Schwinger-Dyson Residual

A typed net needs dynamics.  Define the finite typed variation:

$$
\boxed{
\delta_a\mathcal A_B^{QFT}
}
$$

for a local typed move `a\in\mathfrak A_D`.  The finite Ward/SD residual is:

$$
\boxed{
N_B^{dyn}
=
\sup_{\|a\|=1}
\left|
\omega_D(\delta_a\mathcal A_B^{QFT})
\right|.
}
$$

### Theorem 77: Least Typed-Net Stationarity Gives Finite Ward/SD Identities

If the least typed net is interior stationary under local typed variations,
then `N_B^{dyn}` is below tolerance.

**Proof.**

Interior stationarity means no local typed move reduces finite boundary work
above tolerance.  The expectation of local typed variation is exactly the
finite Ward/Schwinger-Dyson residual. `\square`

## 134. Gauge-Null Directions

A gauge-like move is not imported symmetry.  It is a record-null typed move:

$$
\boxed{
g\in\mathfrak G_D
\quad\Longleftrightarrow\quad
d_{pred}(\omega_D,\omega_D\circ g)
+d_{geom}(I_{GR},I_{GR}\circ g)
+d_{src}(\Theta,\Theta\circ g)
\le\epsilon_g.
}
$$

Define:

$$
\boxed{
N_B^{gauge}
=
\inf_{\mathfrak G}
\operatorname{dist}
\left(
\{\text{prediction-null typed moves}\},
\mathfrak G
\right).
}
$$

### Theorem 78: Gauge Is Record-Null Motion

Finite gauge structure is licensed exactly as the groupoid of typed moves that
do not change click predictions, spacetime readout, or source packets above
tolerance.

**Proof.**

If a move changes no record-visible readout, it is gauge-like at that
tolerance.  If it changes a readout, it is physical typed residue, not gauge.
`\square`

## 135. Occupation And Exchange Sectors

Repeated typed carriers can define occupation sectors.

Let:

$$
\boxed{
n_{\tau}(D)
=
\#\{\text{stable carriers of type }\tau\text{ in }D\}.
}
$$

The exchange defect is:

$$
\boxed{
N_B^{occ}
=
\sup_{\pi}
d_{\omega}
\left(
\omega_D(a_{\tau,1}\cdots a_{\tau,k}),
\omega_D(a_{\tau,\pi(1)}\cdots a_{\tau,\pi(k)})
\right).
}
$$

### Theorem 79: Occupation Sectors Are Stable Repeated Types

A finite occupation sector is licensed only when repeated typed carriers have
stable counts, projective correlators, and controlled exchange defect.

**Proof.**

Particle-like occupation is not primitive.  It is the stable repetition of
typed record carriers with exchange behavior.  If repetition or exchange
fails, no occupation sector is licensed. `\square`

## 136. Positive Committed Histories And Interference

Positive committed histories cannot hide interference between disjoint
committed alternatives.

For disjoint committed alternatives `E_1,E_2`, define the interference
witness:

$$
\boxed{
\mathcal I_D(E_1,E_2;Y)
=
Y(E_1\cup E_2)
-p_1Y(E_1)-p_2Y(E_2).
}
$$

where `p_i` are the projected committed-history weights.

### Theorem 80: No Silent Interference In Committed Positive Histories

If all target-relevant carriers are printed in the committed typed algebra,
then:

$$
\boxed{
\mathcal I_D(E_1,E_2;Y)=0
}
$$

for disjoint committed alternatives.

**Proof.**

The committed state is a positive mixture over disjoint alternatives.  The law
of total probability holds on the committed event algebra.  Any cross effect
must therefore be either a printed typed residue, a coarse-graining artifact,
or a pre-commitment effect. `\square`

## 137. Printed Interference Sector

If interference is itself printed as a stable record residue, define:

$$
\boxed{
\tau^I_{12}
}
$$

with gates:

$$
\boxed{
|\mathcal I_D(E_1,E_2;Y)|>\epsilon_I,
\qquad
\Delta^I_D\le\epsilon_I^{drift},
\qquad
C_{raw}(\tau^I_{12})=0.
}
$$

Then:

$$
\boxed{
\mathfrak A_D
\mapsto
\mathfrak A_D\vee\operatorname{Alg}(\tau^I_{12}).
}
$$

### Theorem 81: Printed Interference Is A Typed Sector

Stable subraw interference residue is admissible as a typed sector of the
finite net.  It does not force amplitudes.

**Proof.**

No-silent closure requires above-tolerance stable residue to be typed.  Once
typed, the cross effect is part of the committed algebra rather than a hidden
correction to a positive mixture. `\square`

## 138. Amplitude Necessity Fork

An amplitude/decoherence layer is forced only if committed typed residues
cannot carry stable interference.

Let `\Gamma` be a pre-commitment history space and:

$$
\boxed{
c:\Gamma\to H
}
$$

the commitment map to indivisible committed records.

A decoherence functional is:

$$
\boxed{
\mathfrak D_D(U,V)\in\mathbb C.
}
$$

The committed positive weight is the diagonal shadow:

$$
\boxed{
w_D(H)=\mathfrak D_D(c^{-1}H,c^{-1}H).
}
$$

Off-diagonal terms carry pre-commitment interference.

### Theorem 82: Amplitude Necessity Trichotomy

For every stable above-tolerance interference witness, exactly one of the
following holds:

1. it is typed as a printed committed residue;
2. it disappears under bounded history refinement;
3. it cannot be typed without raw reconstruction or projective instability,
   and a pre-commitment amplitude/decoherence layer is necessary.

**Proof.**

No-silent closure requires above-tolerance residue to be typed, refined away,
or represented by a licensed noncommitted layer.  If typing is impossible
without rawness or instability while the witness persists, the committed
positive algebra cannot carry it.  A pre-commitment off-diagonal structure is
therefore forced. `\square`

## 139. Decoherence Functional Gate

A finite decoherence functional is licensed only if:

1. hermiticity:

$$
\boxed{
\mathfrak D(U,V)=\overline{\mathfrak D(V,U)};
}
$$

2. positivity on diagonals:

$$
\boxed{
\mathfrak D(U,U)\ge0;
}
$$

3. finite additivity on disjoint unions;
4. projective compatibility under bounded history refinement;
5. diagonal shadow matches committed record weights;
6. off-diagonal blocks reproduce printed or required interference witnesses;
7. no off-diagonal effect changes record predictions without appearing in the
   typed control panel.

Define:

$$
\boxed{
N_B^{decoh}
}
$$

as the sum of violations of these gates.

### Theorem 83: Decoherence Gate

An amplitude/decoherence layer is admissible only if:

$$
\boxed{
N_B^{decoh}\le\epsilon_{decoh}.
}
$$

Otherwise it is hidden machinery and not part of the record law.

**Proof.**

Each condition is needed for the pre-commitment layer to project to a positive
committed record law while carrying stable interference.  If it fails, the
layer is not record-intrinsic. `\square`

## 140. Source Expectation Packet

Issue 4 required inclusive sources of the form:

$$
\boxed{
\Theta_D^{incl}=\omega_D(\widehat\Theta_D).
}
$$

or, in the amplitude branch:

$$
\boxed{
\Theta_D^{incl}
=
\frac{\mathfrak D_D(\widehat\Theta_D)}
{\mathfrak D_D(1)}.
}
$$

### Theorem 84: QFT Net Supplies Inclusive Source Closure

If the finite typed net has projectively compatible states or an admissible
decoherence functional, then nonclassical source packets from issue 4 are
licensed as inclusive source responses.

**Proof.**

The missing object in issue 4 was the state/projection functional.  The
QFT-ready net supplies `\omega_D` or an admissible diagonal shadow of
`\mathfrak D_D`.  Therefore `\Theta_D^{incl}` becomes record-intrinsic.
`\square`

## 141. Continuum-QFT Readiness

A sequence of finite QFT-ready nets:

$$
\boxed{
(\mathfrak A_{D_n},\omega_{D_n})
}
$$

is continuum-QFT-ready when:

1. the spacetime packets pass continuum/smoothness gates;
2. finite correlators converge on local typed tests;
3. typed locality defects vanish or converge to licensed shared sectors;
4. Ward/source anomalies vanish or become typed anomaly sectors;
5. occupation/exchange profiles stabilize;
6. gauge-null groupoids converge;
7. decoherence/amplitude layers, if present, have projective limits.

### Theorem 85: Finite-To-Continuum QFT Candidate

If the seven conditions hold, the finite typed-net sequence defines a
continuum QFT candidate over the represented spacetime packet.

**Proof.**

Continuum localization comes from issue 5.  Convergent correlators and states
supply the algebraic/state limit.  Locality, Ward, occupation, gauge, and
decoherence convergence supply the remaining QFT-readiness gates. `\square`

## 142. What This Does Not Derive

The finite QFT-ready gate does not yet derive:

1. the Standard Model gauge group;
2. exact particle spectrum;
3. renormalized continuum dynamics;
4. unique Hilbert-space representation;
5. numerical coupling constants;
6. full path-integral measure.

It derives the finite record-intrinsic condition under which those questions
become well-posed.

## 143. Opening Investigation A: Are Amplitudes Fundamental?

Not in this framework.

### Theorem 86: Amplitudes Are Licensed, Not Primitive

Amplitude/decoherence structure is introduced only when stable
above-tolerance interference cannot be carried by committed typed residues or
removed by history refinement.

**Proof.**

This is the amplitude necessity trichotomy.  The primitive object remains the
bounded indivisible record history; amplitudes are a pre-commitment carrier
licensed by projection requirements. `\square`

## 144. Opening Investigation B: Can Positive Histories Mimic Quantum Theory?

Sometimes, but not when stable interference witnesses persist.

### Theorem 87: Positive-History Limit

If all interference witnesses are below tolerance or printed as typed sectors,
positive committed histories suffice for finite predictions.  If not, they do
not.

**Proof.**

Below-tolerance witnesses are irrelevant to the bounded target.  Printed
witnesses are part of the algebra.  Remaining persistent unprinted witnesses
violate Theorem 80 and force Theorem 82 case 3. `\square`

## 145. Opening Investigation C: Gauge From Records

Gauge structure emerges from record-null typed moves, not from imposed
symmetry.

### Theorem 88: Gauge Groupoid Reconstruction

If record-null typed moves close under composition up to tolerance, they form
a finite gauge groupoid.  If they do not close, there is no licensed gauge
symmetry at that tolerance.

**Proof.**

Closure under composition is the finite groupoid condition.  Record-nullness
makes the moves gauge-like rather than physical. `\square`

## 146. Opening Investigation D: Matter Spectrum

The finite matter spectrum is the stable set of irreducible typed occupation
sectors.

### Theorem 89: Spectrum Is Stable Typed Decomposition

A particle/species label is licensed only when an irreducible typed sector has
stable occupation, exchange, Ward/source, and projective correlator profiles.

**Proof.**

Without stability under those tests, the label is a presentation artifact or
temporary residue, not a finite particle/species sector. `\square`

## 147. Opening Investigation E: Barandes Alignment

The construction remains Barandes-aligned if:

$$
\boxed{
\text{committed records are indivisible;}
\quad
\text{probability is projected history weight;}
\quad
\text{amplitudes, if any, are pre-commitment carriers whose diagonal projects
to committed records.}
}
$$

### Theorem 90: No Markov Replacement

The finite QFT-ready net does not replace the click law with a Markov
transition.

**Proof.**

Every state, typed net, or amplitude layer is defined over bounded histories
or pre-commitment histories with a commitment map.  No one-step transition
`\Pr(W_{N+1}\mid W_N)` is primitive. `\square`

## 148. Independent Hostile Review Round For Issue 7

### Review 1: "This is not full QFT."

Accepted.  It is QFT-ready finite structure.  Full continuum QFT requires
continuum limits, renormalization, and physical sector identification.

### Review 2: "Amplitudes are smuggled in."

Rejected if amplitudes are introduced only by the necessity fork and pass the
decoherence gate.  Accepted if amplitudes are assumed from taste.  This paper
forbids that.

### Review 3: "Positive history states cannot reproduce quantum theory."

Accepted in interference-bearing regimes.  That is exactly why the amplitude
necessity fork exists.

### Review 4: "Typed sectors could be arbitrary labels."

Rejected when type labels must be stable, subraw, projective, local/entangled
in a typed way, Ward-compatible, and nonlookup.

### Review 5: "Gauge groups are not derived."

Partly accepted.  The paper derives the finite condition for a gauge groupoid:
record-null typed moves that close.  It does not derive the Standard Model
group.

### Review 6: "Matter spectrum is not derived."

Accepted.  The paper derives the finite licensing condition for spectrum
labels, not the actual spectrum.

### Review 7: "This depends on spacetime."

For ordinary QFT-on-spacetime, yes.  A pre-spacetime typed net is possible in
principle, but this campaign is aimed at the post-spacetime QFT gate needed
for nonclassical sources and Einstein coupling.

## 149. Issue 7 Final Theorem

### Theorem 91: Finite QFT-Ready Typed Net Closure

For a selected bounded-history carrier that has passed the spacetime, scale,
source, continuum, and Einstein-readiness gates, issue 7 is closed in the
following finite sense:

1. the least finite typed net exists whenever the typed residue quotient is
   finite and raw labels are excluded;
2. QFT-readiness is exactly the smallness of `\mathcal QDef_B`;
3. classical committed positive histories suffice only when interference
   witnesses are below tolerance or printed as typed sectors;
4. persistent unprinted interference forces an admissible pre-commitment
   amplitude/decoherence layer;
5. inclusive source packets are licensed by finite states or decoherence
   shadows;
6. gauge, occupation, charge, and matter labels are licensed only as stable
   typed record sectors;
7. continuum QFT is a further limit of QFT-ready finite nets, not an input.

**Proof.**

Items 1 and 2 are Theorems 73 and 74.  Items 3 and 4 are Theorems 80-83.  Item
5 is Theorem 84.  Items 6 and 7 are Theorems 75-79 and 85-89. `\square`

## 150. Updated Status After Issue 7

Issue 7 is closed as a finite QFT-ready typed-net and amplitude-necessity
theorem:

$$
\boxed{
\text{we know when finite nonclassical matter/source structure is licensed,
and when amplitudes are forced.}
}
$$

It is not closed as a derivation of the full observed QFT:

$$
\boxed{
\text{Standard Model groups, spectra, renormalized continuum dynamics, and
numerical couplings remain later physical-sector work.}
}
$$

The open list is now:

1. **selector coefficient calibration:** closed at finite constrained-selector
   level;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification; actual cosmological support remains issue 8;
3. **record-realized scale anchors and `G_\infty`:** closed as finite
   licensing/limit theorem; physical anchor construction partly supplied by
   issues 4 and 7;
4. **typed source/stress construction:** closed as least typed-packet theorem;
   nonclassical states supplied by issue 7 when QFT-ready;
5. **continuum convergence:** closed as finite convergence/readout gate;
   actual physical satisfaction remains issue 8 and empirical support;
6. **small Einstein residual on physical histories:** closed as finite
   interior-stationarity theorem; nonclassical source completion supplied by
   issue 7 when QFT-ready;
7. **finite QFT typed net and amplitude/state rule:** closed as finite
   QFT-ready/amplitude-necessity theorem;
8. **initial-history projection weight charging onset:** open.

The last remaining issue is the initial-history projection weight: why the
actual bounded history branch charges the geometry, continuum, Einstein, and
QFT-ready classes rather than only allowing them abstractly.

## 151. Issue 8 Campaign: Initial-History Projection Weight

The eighth issue was previously stated as:

$$
\boxed{
\text{derive the initial-history projection weight that charges onset.}
}
$$

This wording hides a trap.  It sounds like we need a fundamental prior over
all possible beginnings.  That is not Barandes-aligned and it is not required
by the bounded record law.

The correct object is conditional and record-intrinsic:

$$
\boxed{
\text{project the current bounded record-history cylinder back onto the
compatible initial seeds.}
}
$$

The "prior" is therefore not primitive.  It is the shadow of the same positive
bounded-history weight already derived in Papers XL and XLI:

$$
\boxed{
h_B^\star(H)=\exp[-\mathcal A_B^{hist}(H)].
}
$$

Issue 8 closes only if the following can be proved:

$$
\boxed{
\text{if the current bounded panel licenses spacetime, then its compatible
initial-history projection charges onset seeds.}
}
$$

It does not need to prove an unconditional probability distribution over
possible universes.

## 152. Why An Unconditional Prior Would Be Wrong

Let `\Omega_0` be the class of all admissible pre-geometric initial seeds.
An unconditional measure:

$$
\boxed{
\mu_0(C)
=
\frac{\sum_{S\in C}w_0(S)}{\sum_{S\in\Omega_0}w_0(S)}
}
$$

would introduce a new primitive object `w_0`.

That would violate the current program unless `w_0` is itself derived as a
projection of bounded histories.  The law must not say:

$$
\boxed{
\text{first choose a random beginning, then evolve it.}
}
$$

It must say:

$$
\boxed{
\text{given a bounded record panel, unresolved compatible histories project
onto effective weights.}
}
$$

Therefore the issue-8 target is not an external cosmological prior.  It is a
support and concentration theorem for the projected history weight.

## 153. Current Panel, Histories, And Seed Map

Fix a bounded record panel `B` at tolerance `\epsilon`.

Let:

$$
\boxed{
\Gamma_B
}
$$

be the finite or compact same-actual quotient of compatible bounded histories
after the completed subraw boundary closure.

An element:

$$
\boxed{
H\in\Gamma_B
}
$$

is not a one-step transition.  It is a bounded compatible history cylinder:
enough past record structure to compute the requested current and forward
panel predictions.

Define the initial-seed projection:

$$
\boxed{
\sigma_0:\Gamma_B\to\Omega_0,
\qquad
\sigma_0(H)=S_0(H).
}
$$

Here `S_0(H)` is the earliest bounded pre-geometric seed retained by the
history depth used for the panel.  If the history begins after a still earlier
unresolved layer, then `S_0(H)` means the earliest admitted seed of the
bounded cylinder, not an absolute metaphysical beginning.

## 154. Onset Labels

For the target family of `B`, split initial seeds into:

$$
\boxed{
\Omega_0
=
\Omega_{\rm force}
\sqcup
\Omega_{\rm allow}
\sqcup
\Omega_{\rm block}
\sqcup
\Omega_{\rm trivial}.
}
$$

The labels mean:

- `\Omega_force`: every least admissible continuation reaches finite spacetime
  onset for the target;
- `\Omega_allow`: at least one least admissible continuation reaches finite
  spacetime onset and at least one does not;
- `\Omega_block`: no least admissible continuation reaches finite spacetime
  onset for the target;
- `\Omega_trivial`: no nontrivial bounded click/geometric channel appears.

Define:

$$
\boxed{
\Omega_{\rm on}
=
\Omega_{\rm force}\cup\Omega_{\rm allow}.
}
$$

These are the seeds that can support the spacetime branch of the bounded
panel.

## 155. Projected Initial Weight

The projected initial weight is the pushforward of the bounded-history weight:

$$
\boxed{
\mu_B(C)
=
\frac{
\sum_{H\in\Gamma_B:\ \sigma_0(H)\in C} h_B^\star(H)
}{
\sum_{H\in\Gamma_B} h_B^\star(H)
}.
}
$$

For a partial observed panel `p`, use the compatible cylinder:

$$
\boxed{
\Gamma_B(p)
=
\{H\in\Gamma_B: H\text{ projects to }p\}.
}
$$

and:

$$
\boxed{
\mu_B(C\mid p)
=
\frac{
\sum_{H\in\Gamma_B(p):\ \sigma_0(H)\in C} h_B^\star(H)
}{
\sum_{H\in\Gamma_B(p)} h_B^\star(H)
}.
}
$$

This is the only admissible "initial prior" in the bounded theory.

### Theorem 92: Initial Weight Is A Pushforward

The initial-history projection weight `\mu_B` is not an independent
probability law.  It is the pushforward:

$$
\boxed{
\mu_B=(\sigma_0)_\#\bar h_B^\star
}
$$

where `\bar h_B^\star` is the normalized bounded-history weight on
`\Gamma_B`.

**Proof.**

The displayed formula for `\mu_B` is exactly the definition of pushforward
measure under `\sigma_0`.  No additional probability space or Markov kernel is
introduced. `\square`

## 156. The Spacetime-Panel Support Principle

Suppose the current bounded panel licenses a finite spacetime packet:

$$
\boxed{
\operatorname{STDef}_B\le\epsilon_{\rm ST}.
}
$$

Here `\operatorname{STDef}_B` abbreviates the finite spacetime-readiness
defects: atlas/overlap closure, manifoldlike packet consistency,
center/boundary stability, and the finite GR packet gates developed in Papers
XXXVII--XLII.

Then any compatible history must either:

1. contain an onset route in its bounded past;
2. be same-actual equivalent to an onset route at tolerance;
3. smuggle the spacetime packet silently across the boundary;
4. fail compatibility with the current panel.

The third option is excluded by no-silent closure.  The fourth option is not
in `\Gamma_B(p)`.

## 157. Theorem 93: Spacetime Panels Charge Onset

Let `p` be a bounded observed panel whose record-intrinsic readout licenses a
finite spacetime packet at tolerance `\epsilon`.  Assume:

1. completed no-silent boundary closure holds for `B`;
2. same-actual null differences are quotiented;
3. `p` contains enough packet data to distinguish spacetime onset from
   non-onset above tolerance;
4. raw/reconstructive hidden presentation counts are inadmissible;
5. `h_B^\star` is the selected positive bounded-history weight.

Then:

$$
\boxed{
\mu_B(\Omega_{\rm on}\mid p)
\ge
1-\epsilon_{\rm leak}(B,p).
}
$$

If the panel is exact at the quotient level, then:

$$
\boxed{
\epsilon_{\rm leak}(B,p)=0
\quad\text{and}\quad
\mu_B(\Omega_{\rm on}\mid p)=1.
}
$$

**Proof.**

Take `H\in\Gamma_B(p)` with `\sigma_0(H)\notin\Omega_{\rm on}`.  Then
`\sigma_0(H)` is blocking or trivial for the target family.  By definition it
has no admitted finite-onset continuation producing the spacetime packet in
`p`.

Since `H` nevertheless projects to a spacetime panel, one of three things must
be true.

First, the spacetime packet is same-actual null relative to the panel.  Then
`H` is quotiented with an onset-compatible representative and does not
contribute to a distinct non-onset class.

Second, the spacetime packet enters through an unprinted boundary/source
channel.  Completed no-silent closure forbids this above tolerance; below
tolerance it contributes only to `\epsilon_{\rm leak}`.

Third, `H` reconstructs or looks up hidden presentation data sufficient to
mimic the packet without an onset route.  Raw/reconstructive carriers are
inadmissible by the calibrated selector.

Thus no above-tolerance non-onset history remains in the compatible quotient.
The only surviving mass outside `\Omega_{\rm on}` is below-tolerance leakage.
`\square`

## 158. Stronger Exact Support Version

The exact quotient theorem is:

$$
\boxed{
\Gamma_B(p)
\subseteq
\sigma_0^{-1}(\Omega_{\rm on})
\quad
\text{modulo same-actual null and below-tolerance leakage.}
}
$$

This is stronger than a large-deviation statement.  It says the support itself
is wrong if a non-onset history is admitted while the current panel already
contains a licensed spacetime packet.

## 159. Barrier Dominance For Spoof Histories

The support theorem handles exact compatibility.  Approximate panels require
a quantitative penalty.

Let:

$$
\boxed{
\Delta_{\rm spoof}(H)
}
$$

be the minimum calibrated selector penalty paid by a history whose seed is
blocking/trivial but whose current projection mimics a spacetime packet.

The penalty is a sum of already-calibrated barriers:

$$
\boxed{
\Delta_{\rm spoof}
\ge
\Delta_{\rm silent}
+\Delta_{\rm raw}
+\Delta_{\rm drift}
+\Delta_{\rm packet}.
}
$$

where the terms charge:

- silent boundary insertion;
- raw hidden reconstruction;
- deletion/insertion drift mismatch;
- packet/readout mismatch.

### Theorem 94: Spoof Leakage Bound

Let:

$$
\boxed{
M_{\rm bad}(B,p)
=
\#\{H\in\Gamma_B(p):\sigma_0(H)\notin\Omega_{\rm on}\}
}
$$

after same-actual quotienting, or the corresponding finite covering number in
the compact case.  If every bad compatible history pays
`\Delta_{\rm spoof}\ge\delta_B`, then:

$$
\boxed{
1-\mu_B(\Omega_{\rm on}\mid p)
\le
M_{\rm bad}(B,p)\,e^{-\delta_B}.
}
$$

**Proof.**

Normalize by the total positive weight.  Each bad history has weight at most
`e^{-\delta_B}` times the weight scale of a least compatible onset history.
Summing over at most `M_{\rm bad}` bad quotient classes gives the bound.
`\square`

### Consequence

The calibrated selector coefficients from issue 1 can make spoof leakage
smaller than any requested bounded tolerance, provided the bad covering number
is subraw relative to the calibrated penalty range.

## 160. Why This Is Not Circular

The theorem does not assume spacetime in the initial seed.

It conditions on a current bounded record panel that already contains stable
spacetime readout.  The question is then:

$$
\boxed{
\text{which compatible bounded histories can explain this panel without
silent/reconstructive cheating?}
}
$$

The answer is: only onset-compatible histories.

This is exactly the same logic used for ordinary bounded predictions.  We do
not know the whole actual history, so we project over compatible histories.
The difference is that the observable is now the initial-seed label.

## 161. Forced Seeds Versus Allowing Seeds

The projection need not distinguish forced from allowing seeds.

If:

$$
\sigma_0(H)\in\Omega_{\rm force},
$$

then every least continuation supports onset.

If:

$$
\sigma_0(H)\in\Omega_{\rm allow},
$$

then only some continuations support onset.  Conditioning on the current
spacetime panel selects the onset continuations:

$$
\boxed{
\mu_B(\Omega_{\rm force}\cup\Omega_{\rm allow}\mid p_{\rm ST})\approx1,
}
$$

but:

$$
\boxed{
\mu_B(\Omega_{\rm force}\mid p_{\rm ST})
}
$$

may be less than one.  That is not a failure.  It means the actual bounded
history projection may pass through a branch-dependent seed whose realized
branch is onset.

## 162. Defining `PriorDef_B`

The previous papers introduced a prior defect without a final formula.  The
record-intrinsic definition is:

$$
\boxed{
\operatorname{PriorDef}_B(p)
=
-\log \mu_B(\Omega_{\rm on}\mid p).
}
$$

When leakage is small:

$$
\boxed{
\operatorname{PriorDef}_B(p)
\le
-\log(1-\epsilon_{\rm leak})
\sim
\epsilon_{\rm leak}.
}
$$

Thus issue 8 is closed exactly when `\operatorname{PriorDef}_B` is small for
the bounded spacetime panels under consideration.

## 163. Theorem 95: Issue 8 Finite Closure

For a bounded panel `p` whose finite spacetime, continuum, Einstein, and
QFT-readiness gates have passed, the initial-history projection defect is
small:

$$
\boxed{
\operatorname{PriorDef}_B(p)\le\epsilon_{\rm prior}
}
$$

whenever:

1. completed no-silent closure holds;
2. the same-actual quotient has removed null alternatives;
3. non-onset spoof histories must use silent, raw, drift-unstable, or
   packet-incompatible carriers;
4. calibrated selector barriers dominate their quotient multiplicity.

In the exact closed quotient:

$$
\boxed{
\operatorname{PriorDef}_B(p)=0.
}
$$

**Proof.**

Theorem 93 gives support on onset classes modulo leakage.  Theorem 94 bounds
the leakage by calibrated barrier dominance.  Taking `-\log` gives the defect
bound. `\square`

## 164. What Has Actually Been Proven

The proof establishes:

$$
\boxed{
\text{spacetime-containing bounded records project backward onto
onset-compatible initial histories.}
}
$$

It does not establish:

$$
\boxed{
\text{an unconditional probability that an arbitrary possible universe begins
in an onset-forcing seed.}
}
$$

That second statement is not a bounded record prediction unless a current
panel is specified.

## 165. Barandes Alignment Check

The construction is Barandes-aligned in three ways.

First:

$$
\boxed{
\text{the primitive object is an indivisible compatible history, not a Markov
transition.}
}
$$

Second:

$$
\boxed{
\text{probability appears only after projecting unresolved histories onto a
bounded panel.}
}
$$

Third:

$$
\boxed{
\text{the initial seed is inferred as a history label, not sampled by an
external stochastic law.}
}
$$

The framework therefore removes probability from the full compatible history
description and reintroduces effective probabilities only for bounded partial
access.

## 166. Opening Investigation A: Is This Merely Anthropic?

Objection:

$$
\boxed{
\text{"You conditioned on spacetime, so of course you get onset."}
}
$$

Answer: yes, and that is the correct bounded law.

The program is not trying to assign God's-eye probabilities to unobserved
entire universes.  It is trying to compute what follows from records we have.
If the records contain a stable spacetime packet, then compatible histories
must explain that packet.  Non-onset histories are allowed only if they are
same-actual, below tolerance, or cheating by silent/raw reconstruction.

Thus the result is not a cosmological metaphysics theorem.  It is an
operational projection theorem.

## 167. Opening Investigation B: What About Non-Spacetime Branches?

Non-spacetime branches may exist in the global admissible class.

They simply do not lie in the compatible cylinder of a bounded panel whose
records license spacetime, except through below-tolerance or same-actual
equivalence.

Therefore:

$$
\boxed{
\mu_B(\Omega_{\rm block}\mid p_{\rm ST})\approx0
}
$$

does not imply:

$$
\boxed{
\mu_0(\Omega_{\rm block})=0
}
$$

for some nonexistent unconditional prior `\mu_0`.

## 168. Opening Investigation C: Boundary Conditions And External Influence

Suppose the experiment sits near a black hole, a massive body, or a strong
source sector.  Then the bounded panel must include enough boundary/source
carriers to make the influence below tolerance.

If it does not, no-silent closure fails:

$$
\boxed{
\mathsf{NoSilent}_B>\epsilon_{\rm ns}.
}
$$

Then `\operatorname{PriorDef}_B` is not licensed because the compatible
history cylinder is incomplete.  The remedy is not a different prior.  The
remedy is boundary expansion, source typing, or tolerance weakening.

## 169. Opening Investigation D: Does This Explain The Early Universe?

It explains the early universe only conditionally on present bounded records.

Given present spacetime records, the compatible histories must pass through
onset-compatible seeds.  That is a backward projection result.

It does not yet derive a unique absolute first seed.  The bounded theory says
instead:

$$
\boxed{
\text{the earliest retained seed of any compatible history for our spacetime
panel is onset-compatible.}
}
$$

If one demands a statement before any records are conditioned on, one has left
the bounded prediction framework.

## 170. Opening Investigation E: Could A Non-Geometric Code Fake Everything?

A non-geometric code can fake the spacetime panel only if it passes all of:

1. nonlookup/subraw carrier tests;
2. deletion/insertion projective drift tests;
3. center-ledger and boundary-work tests;
4. spacetime packet readout tests;
5. Einstein residual tests;
6. QFT-ready typed-source tests;
7. no-silent source completion.

If it passes all of those, it is not a bad spoof.  It is same-actual to the
effective spacetime packet for the bounded target.

If it fails one above tolerance, it is charged by the calibrated barriers.

### Theorem 96: Non-Geometric Successful Spoofs Are Same-Actual

Any non-geometric carrier that preserves all bounded click, spacetime,
Einstein, and QFT-ready readouts at tolerance is same-actual for that bounded
panel.

**Proof.**

Same-actual equivalence is precisely equality of all licensed bounded response
readouts at the requested tolerance.  If the non-geometric carrier preserves
all of them, it is not an operationally distinct counterexample. `\square`

## 171. Opening Investigation F: Does Issue 8 Depend On QFT?

Only if the panel asks for QFT-ready matter/source predictions.

For a purely classical spacetime panel:

$$
\boxed{
\Omega_{\rm on}^{GR}
}
$$

is enough.

For a panel with nonclassical matter/source readouts:

$$
\boxed{
\Omega_{\rm on}^{QFT}
}
$$

requires the issue-7 typed net/amplitude gate.  The initial projection theorem
then charges histories whose onset route also licenses the needed typed
matter/source packet.

## 172. The Eight-Issue Closure Functional Revisited

Paper XLIV defined:

$$
\boxed{
\mathcal X_B
=
\operatorname{SelDef}_B
+\Phi_B^{GI}
+\operatorname{ScaleDef}_B
+\operatorname{SrcDef}_B
+\operatorname{ContDef}_B
+\mathcal B_B^{Ein}
+\mathcal Q_B^{def}
+\operatorname{PriorDef}_B.
}
$$

Issue 8 supplies:

$$
\boxed{
\operatorname{PriorDef}_B(p)
=
-\log \mu_B(\Omega_{\rm on}\mid p).
}
$$

Therefore all eight summands now have finite record-intrinsic meanings.

### Theorem 97: Eight-Gate Operational Closure

For a bounded panel `p`, if:

$$
\boxed{
\mathcal X_B(p)\le\epsilon_X,
}
$$

then the panel licenses:

$$
\boxed{
\text{history-first click prediction}
\to
\text{spacetime packet}
\to
\text{continuum-ready readout}
\to
\text{Einstein-ready residual}
\to
\text{QFT-ready typed net}
}
$$

and its compatible initial histories charge onset-compatible seeds.

**Proof.**

The first seven summands license the layers developed in sections 1-150.
The eighth summand, now defined by projected initial onset mass, guarantees
that the compatible history cylinder projects to onset-compatible seeds.
`\square`

## 173. Independent Hostile Review Round For Issue 8

### Review 1: "This does not explain why there is a spacetime universe."

Accepted.

It explains what the bounded record law says once the current bounded panel
contains spacetime records.  An unconditioned explanation of existence is not
a finite record prediction.

### Review 2: "You are using the present to infer the past."

Accepted, deliberately.

The law is history-first, not Markov-forward.  Bounded predictions are made by
projecting compatible histories.  Retrodicting onset from current records is
the same operation as predicting a future click from a partial panel.

### Review 3: "A blocking seed might generate a fake spacetime by hidden
presentation data."

Rejected above tolerance.

That is raw/reconstructive or silent.  The calibrated selector excludes it or
charges it by Theorem 94.

### Review 4: "Maybe non-geometric physics is exactly equivalent to geometry."

Then it is same-actual for the bounded panel.  The finite law is not allowed
to distinguish unprinted metaphysical descriptions that make identical
bounded record predictions.

### Review 5: "The theorem depends on no-silent closure."

Accepted.  No-silent closure is one of the already closed prerequisites of
the bounded law.  Without it, no bounded prediction law is licensed.

### Review 6: "The result is local, not global."

Accepted.

The result is bounded-panel local.  It can be applied to larger and larger
panels, but it is never an unconditional all-universe prior.

### Review 7: "What if the present panel is partial and weak?"

Then `\epsilon_{\rm leak}` is larger and `\operatorname{PriorDef}_B` may not
be small.  This is correct: weak panels cannot strongly infer onset history.

### Review 8: "Does this prove geometry wins?"

It proves geometry wins for the compatible history projection of a
spacetime-containing panel, modulo tolerance.  It does not prove that every
possible seed in an unconditioned class must geometrize.

## 174. Issue 8 Final Theorem

### Theorem 98: Initial-History Projection Weight Charges Onset

Let `p` be a bounded record panel whose already-licensed readouts include the
requested spacetime, continuum, Einstein-ready, and QFT-ready structures at
tolerance.  Let `h_B^\star` be the selected positive bounded-history weight on
the completed no-silent same-actual quotient.  Let `\sigma_0` project each
compatible history to its earliest retained pre-geometric seed.

Then the induced initial-history projection:

$$
\boxed{
\mu_B(C\mid p)
=
\frac{
\sum_{H\in\Gamma_B(p):\sigma_0(H)\in C}h_B^\star(H)
}{
\sum_{H\in\Gamma_B(p)}h_B^\star(H)
}
}
$$

charges onset:

$$
\boxed{
\mu_B(\Omega_{\rm force}\cup\Omega_{\rm allow}\mid p)
\ge
1-\epsilon_{\rm leak}(B,p).
}
$$

In the exact completed quotient:

$$
\boxed{
\mu_B(\Omega_{\rm force}\cup\Omega_{\rm allow}\mid p)=1.
}
$$

The leakage term is bounded by calibrated spoof penalties:

$$
\boxed{
\epsilon_{\rm leak}(B,p)
\le
M_{\rm bad}(B,p)e^{-\delta_B}.
}
$$

Thus:

$$
\boxed{
\operatorname{PriorDef}_B(p)
=
-\log\mu_B(\Omega_{\rm force}\cup\Omega_{\rm allow}\mid p)
}
$$

is finite, record-intrinsic, and small whenever the bounded panel is closed.

**Proof.**

The formula for `\mu_B` is the pushforward of `h_B^\star` by the seed map.
The support theorem excludes above-tolerance blocking/trivial seeds from a
spacetime-containing compatible cylinder unless they are same-actual, silent,
raw/reconstructive, or packet-incompatible.  Same-actual alternatives are
quotiented.  Silent, raw, and packet-incompatible alternatives are excluded or
charged by calibrated barriers.  The remaining bad mass is exactly
`\epsilon_{\rm leak}`, bounded by Theorem 94. `\square`

## 175. Final Status After Issue 8

All eight issues now have finite operational closures.

The eighth issue is closed in the following precise sense:

$$
\boxed{
\text{there is no independent onset prior;}
\quad
\text{onset charge is the backward projection of the current bounded history
weight.}
}
$$

For a bounded panel with licensed spacetime readout:

$$
\boxed{
\text{compatible histories project to onset-compatible seeds.}
}
$$

What remains outside this finite closure is not issue 8 as stated, but a
larger metaphysical/cosmological question:

$$
\boxed{
\text{why is there an actual record history whose bounded panels contain
spacetime at all?}
}
$$

That question is not answered by a bounded record prediction law.  Within the
bounded law, the initial-history projection weight has been derived.

## 176. Updated Eight-Issue Ledger

1. **selector coefficient calibration:** closed as finite constrained-selector
   barrier/dual calibration;
2. **physical seed flow into geometry:** closed as calibrated basin
   classification and spacetime-panel support;
3. **record-realized scale anchors and `G_\infty`:** closed as finite
   licensing/limit theorem, conditional on anchor sectors;
4. **typed source/stress construction:** closed as least typed source packet,
   with QFT-ready extension;
5. **continuum convergence:** closed as finite convergence/readout gate;
6. **small Einstein residual on physical histories:** closed as finite
   interior-stationarity and residual gate;
7. **finite QFT typed net and amplitude/state rule:** closed as finite
   QFT-ready/amplitude-necessity theorem;
8. **initial-history projection weight charging onset:** closed as
   record-conditioned pushforward/support theorem.

The program after Paper XLVIII is therefore no longer missing the finite
operational architecture.

The next frontier is physical identification:

$$
\boxed{
\text{which actual large bounded record panels satisfy the gates, and what
continuum/QFT constants do their limits realize?}
}
$$
