# The record click-law, XXVI: quadratic record action and finite-action selection

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-26. Twenty-sixth paper of the v7 program. This paper follows Paper XXIII's collapsed recursive-interval, no-hidden-staging, projective fixed-point, interval-bracket, and unlabeled-likelihood campaigns. It asks what can actually be imported from the quadratic-gravity direction associated with Stelle, Salvio, Lehners, Boyle, and Turok into the SHARD record-law search. Tags: **[PRINCIPLE]** = candidate formulation; **[STRESS TEST]** = finite diagnostic, not a theorem; **[COUNTEREXAMPLE]** = explicit obstruction or spoof; **[CONSTRAINED]** = narrowed but not unique; **[OPEN]** = disclosed residue. Numerical checks are in `v7/code/p26_quadratic_record_action_audit.py`, at mpmath `dps = 140`.

---

## Scope guards

1. **This paper does not derive quadratic gravity from SHARD.** It imports a structural lesson: finite quadratic action can suppress histories that linear or finitely sampled moment constraints miss.

2. **No continuum metric is assumed.** Any imported idea must be translated into order-only, record-only quantities. A metric curvature tensor cannot be placed into the fundamental law by hand.

3. **The result is not the click law.** The finite receipt catches gross non-manifold and staged adversaries, and catches signed-defect cancellation. It does not solve the linear-jitter clustered adversary from Paper XXIII.

4. **Turok-specific and quadratic-gravity-specific ideas are separated.** The Turok/Boyle program emphasizes fixed points, cancellation of vacuum/Weyl contributions, finite stress-tensor correlators, CPT-symmetric boundary conditions, and gravitational entropy. The Lehners-Stelle result emphasizes finite-action selection in quadratic gravity. The usable SHARD ideas sit at their intersection: finite actions, cancellation conditions, and high-order correlator/bracket constraints.

5. **The ghost problem is not imported.** SHARD has no fundamental metric Hilbert space in this paper, so it should not inherit the perturbative massive spin-2 ghost ontology. Conversely, SHARD cannot claim the ghost is solved merely because the analogy is useful.

6. **The finite action is calibrated, not fundamental.** The receipt uses a small order-observable basis at fixed `N=72`. It is a projection used to find adversaries, not a final probability law.

---

## Abstract

Quadratic gravity replaces a purely linear Einstein-Hilbert action by an action containing curvature-squared terms. The classic reward is improved ultraviolet behavior; the classic cost is the higher-derivative ghost problem. A nearby finite-action lesson is especially relevant to the SHARD record-law search: when the action is quadratic in the right defects, signed cancellations become expensive, and anisotropic or inhomogeneous histories can be selected against by finiteness rather than by a long list of moment constraints.

The SHARD translation is not:

$$
S[g] =
\int d^4x\,\sqrt{-g}
\cdots
$$

because SHARD does not begin with a continuum metric. The translation is:

$$
A_Q^{(N)}(C)
=
\sum_{a,b}
Z_a(C)\,\Gamma^{-1}_{ab}\,Z_b(C),
$$

where `C` is a finite record order, the `Z_a` are calibrated order-only defect fields, and `Gamma` is the calibrated null bracket/covariance. In martingale language, the click law should not merely say that each drift defect averages to zero; it should also fix the bracket of the record defects.

The receipt builds a first finite quadratic action from seven order-visible features:

$$
\rho,\quad
\frac{H}{2\sqrt{N}},\quad
P_{0.25},\quad
P_1,\quad
P_4,\quad
W_{\mathrm{int}},\quad
T_{\le 4}.
$$

Here `rho` is relation density, `H` is height, `P_alpha` are interval Laplace samples, `W_int` is an interval-shape anisotropy proxy, and `T_{\le 4}` is a near-external-twin tail.

At `N=72`, calibrated on 48 independent 1+1 sprinklings and tested on 12 held-out sprinklings, the held-out action has mean

`5.80440374154784871`

and maximum

`15.6482067326610085`.

Gross non-manifold orders are strongly penalized:

| order | quadratic action |
|---|---:|
| chain | `6630.51480133194129` |
| antichain | `172085.417867891179` |
| three-layer KR | `40471.4044296160514` |
| six staged blocks | `7109.08292815807317` |

The receipt also constructs a linear cancellation of relation density between a chain and an antichain. The relation-density defect cancels to

`1.04966814180735762e-140`,

but the quadratic mixture still has action

`91192.0386821151512`.

This is the genuinely useful import from quadratic gravity: **the record law should likely be cancellation-resistant and bracket-level, not a finite list of signed scalar constraints.**

The hostile review then follows the opening. Linear-jitter clustered schedules from Paper XXIII are not solved by this finite action:

| order | quadratic action |
|---|---:|
| linear-half jitter cluster | `3.69368084500711318` |
| linear-one jitter cluster | `8.7534874433810947` |

Those lie inside the held-out sprinkling range. Therefore the quadratic-action idea is compatible with SHARD and useful, but it is not enough. The next object remains the full calibrated finite-dimensional record law or an asymptotic selected-likelihood theorem on the unlabeled order sigma-field.

---

## 1. What quadratic gravity really offers

The relevant continuum action family has the schematic form

$$
S =
\int d^4x\,\sqrt{-g}
\left[
\frac{1}{16\pi G}(R-2\Lambda)
+\alpha R^2
+\beta R_{\mu\nu}R^{\mu\nu}
+\gamma C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}
\right].
$$

The detailed physics is not imported. The record-law search can only import structural ideas:

1. **Quadratic suppression.** A defect and its negative should not be allowed to cancel if both represent non-manifold structure.

2. **Finite action as selection.** The law can reject histories by divergence or large action rather than by explicitly naming every forbidden pathology.

3. **Fixed-point thinking.** The correct law should be stable under coarse-graining/projective restriction, not merely tuned at one `N`.

4. **Correlator finiteness.** A law of means is too weak; the whole bracket/covariance hierarchy matters.

5. **Conformal/Weyl caution.** Weyl-like anisotropy is a useful target, but SHARD cannot assume a Weyl tensor before manifoldness has emerged.

In SHARD language, the continuum curvature-squared impulse becomes:

$$
\text{linear defect control}
\quad\longrightarrow\quad
\text{quadratic bracket control}.
$$

That is the clean import. The rest has to earn its way into order theory.

---

## 2. Compatibility matrix

| imported idea | SHARD status | reason |
|---|---|---|
| finite action selection | compatible | SHARD already needs a law that suppresses non-manifold orders without coordinates |
| squared order-only defects | compatible | prevents signed moment cancellation and matches martingale-bracket thinking |
| UV fixed point / projective stability | compatible | maps naturally to deletion/coarse-graining consistency |
| finite stress-tensor correlators | compatible as analogy | maps to finite record-defect cumulants/brackets, not to a metric stress tensor |
| Weyl/anomaly cancellation | conditional | only order-visible anisotropy/cumulant proxies may be used |
| CPT-symmetric boundary conditions | conditional | must not conflict with the record martingale arrow or with causal-order covariance |
| gravitational entropy selecting smooth initial data | conditional | usable only as an order-counting entropy/action principle |
| metric curvature-squared action as fundamental | incompatible | assumes the manifold structure the click law is trying to explain |
| hidden coordinate labels | incompatible | violates the record-only law and was repeatedly defeated in Paper XXIII |
| finite-neighbor local graph dynamics | incompatible | conflicts with the Lorentzian finite-neighbor obstruction used throughout v7 |
| perturbative ghost ontology | not imported | belongs to metric higher-derivative quantization, not to the present order-only projection |

The compatibility line is sharp: finite-action and bracket ideas are welcome; continuum metric objects are not fundamental.

---

## 3. The order-only quadratic record action

Let `Pi_N` be the calibrated 1+1 sprinkling null at record count `N`. For each order-only observable `F_a`, define

$$
Z_a(C)
=
F_a(C)
-
\mathbb{E}_{\Pi_N}F_a.
$$

The simplest diagonal calibrated action is

$$
A_{\mathrm{diag}}^{(N)}(C)
=
\sum_a
\left(
\frac{Z_a(C)}{\sigma_a}
\right)^2.
$$

The more honest bracket form is

$$
A_Q^{(N)}(C)
=
Z(C)^{\mathsf T}\Gamma_N^{-1}Z(C),
$$

where

$$
\Gamma_{ab}^{(N)}
=
\operatorname{Cov}_{\Pi_N}(F_a,F_b).
$$

Paper XXIII already moved toward the second form with interval brackets and aggregate Palm brackets. Paper XXVI tests the simpler diagonal form because it is transparent enough for hostile failure.

The receipt uses:

| feature | order-only meaning |
|---|---|
| relation density | first MM-dimension proxy |
| height ratio | longest-chain scale |
| `P_0.25`, `P_1`, `P_4` | interval-size Laplace probes |
| interval Weyl proxy | mean squared deviation of internal interval relation density from `1/2` |
| near-twin tail | density of nearly duplicate causal neighborhoods |

The interval Weyl proxy is:

$$
W_{\mathrm{int}}(C)
=
\frac{1}{|\mathcal{I}_{\ge 4}|}
\sum_{(x,y)\in\mathcal{I}_{\ge 4}}
\left(
\rho(I(x,y))-\frac{1}{2}
\right)^2,
$$

where `I(x,y)` is the open interval and `rho(I(x,y))` is the relation density inside that interval.

This is not the Weyl tensor. It is only the first order-visible analogue of local interval anisotropy in 1+1.

---

## 4. Receipt

The command was:

```bash
isp/code/.venv/bin/python isp/v7/code/p26_quadratic_record_action_audit.py
```

The receipt uses `mpmath` with:

`mp.dps = 140`

Calibration:

| feature | mean | std |
|---|---:|---:|
| relation density | `0.488914971309337507` | `0.0460579905960370657` |
| height ratio | `0.826185527323865423` | `0.0968547809933037601` |
| `P_alpha_0.25` | `7.17924538306131959` | `0.279181187067462402` |
| `P_alpha_1` | `3.92854823097450722` | `0.182927696332088901` |
| `P_alpha_4` | `2.94088203899083681` | `0.179193051358033812` |
| interval Weyl proxy | `0.0215463398372471278` | `0.00361262611556048931` |
| near-twin tail | `0.0116881846635367762` | `0.00239361336651006606` |

Held-out sprinkling score:

| statistic | value |
|---|---:|
| mean action | `5.80440374154784871` |
| max action | `15.6482067326610085` |

Adversarial scores:

| adversary | action | leading z-defects |
|---|---:|---|
| chain | `6630.51480133194129` | interval Weyl, height, near twins |
| antichain | `172085.417867891179` | near twins, `P_0.25`, `P_1` |
| three-layer KR | `40471.4044296160514` | near twins, `P_4`, `P_1` |
| six staged blocks | `7109.08292815807317` | near twins, `P_4`, `P_1` |
| fixed clustered schedule | `8.96459005649688549` | interval Weyl, `P_4`, near twins |
| linear-half jitter cluster | `3.69368084500711318` | height, near twins, interval Weyl |
| linear-one jitter cluster | `8.7534874433810947` | height, `P_1`, `P_4` |

Checklist:

| check | result |
|---|---|
| held-out sprinklings have finite calibrated quadratic action | PASS |
| gross non-manifold adversaries are strongly penalized | PASS |
| linear relation-density cancellation leaves large quadratic action | PASS |
| linear-jitter clustered schedules are not falsely promoted as solved | PASS |
| interval Weyl proxy participates in at least one gross rejection | PASS |

Final receipt line:

`CHECKS PASSED: 5/5`

---

## 5. What is actually new here

The new content is not "SHARD becomes quadratic gravity." It does not.

The new content is the corrected record-law heuristic:

> **[CONSTRAINED] The click law should not be a list of first moments. It should be a finite-action or martingale-bracket principle over recursively calibrated order defects.**

This is stronger than saying:

$$
\mathbb{E}Z_a=0.
$$

It says the law should control:

$$
\mathbb{E}Z_aZ_b,
\qquad
\mathbb{E}Z_aZ_bZ_c,
\qquad
\ldots
$$

or equivalently the finite-dimensional record law generated by those defects. That is exactly where the Paper XXIII campaign had already been forced by the linear-jitter adversary. Quadratic gravity gives a useful physical precedent for taking that move seriously.

The finite receipt also gives a practical rule:

> **Never accept a signed scalar match unless the corresponding squared/bracket defect is also calibrated.**

The chain/antichain cancellation makes this vivid. A linear mixture can cancel the relation-density defect to `1e-140`, while the quadratic action remains enormous. This is the mathematical shadow of why curvature-squared actions can matter: they see variance, not just signed mean.

---

## 6. Hostile reviews

### Review 1: This is feature engineering

Correct. The finite receipt is feature engineering. The repair is not to pretend otherwise. The paper labels the action as a projection:

$$
A_{\mathrm{diag}}^{(N)}(C)
=
\sum_a z_a(C)^2.
$$

The target law must be invariantly generated, probably as a projective fixed point, a martingale compensator/bracket law, or an unlabeled likelihood principle. The receipt is a measuring instrument, not the final physics.

### Review 2: Quadratic gravity assumes a metric

Correct. Therefore no metric curvature tensor appears in the fundamental SHARD proposal. The only permitted translation is through order-visible interval statistics, bracket fields, Palm kernels, and selected likelihoods.

### Review 3: The interval Weyl proxy is not Weyl curvature

Correct. It is only a placeholder for local anisotropy of interval interiors:

$$
\left(
\rho(I)-\frac{1}{2}
\right)^2.
$$

In 1+1, continuum Weyl curvature vanishes identically, so calling this a Weyl tensor would be wrong. Its role is narrower: it detects interval-shape defects in finite orders.

### Review 4: The finite action fails on the best adversary

Correct, and this is the most important negative result. The linear-jitter clustered schedules land inside the held-out sprinkling action range. This confirms Paper XXIII's wall: once hidden clusters are washed through a linear coordinate window, small unrooted finite projections can become blind.

The quadratic-action idea helps, but the next enemy is still:

$$
\mathbb{E}_{P_N}
\left[
\left(
\frac{dQ_N}{dP_N}
\right)^2
\right]
$$

on the unlabeled order sigma-field, or an order-only statistic that recovers the marked Palm residue without hidden labels.

### Review 5: Finite action could reject real physical fluctuations

Correct. A quadratic action must be calibrated by the null law and by scale. A raw penalty on large deviations would over-smooth the record world. The law must distinguish physical sprinkling fluctuations from non-manifold concentration.

This points back to the bracket:

$$
\Gamma_{ab}^{(N)}
=
\operatorname{Cov}_{\Pi_N}(F_a,F_b).
$$

The right action penalizes deviations from the calibrated bracket, not deviations from zero variability.

### Review 6: Fixed-point cancellation is not the same as record-law uniqueness

Correct. Turok/Boyle fixed-point-style cancellations suggest that special field content may make stress-tensor correlators finite. The SHARD analogue would be that a special record law makes all order-defect brackets finite and projectively stable. That analogy does not prove uniqueness. It gives a search strategy.

---

## 7. Consequences for the click law

The click law should probably not be stated as:

$$
\text{match these finitely many scalar diagnostics.}
$$

It should be closer to:

$$
\text{the compensated record-defect field has the calibrated projective bracket law.}
$$

One possible finite projection is:

$$
d\mathcal{W}_N(C)
\propto
\exp\!\left[-A_Q^{(N)}(C)\right]
d\mu_N(C),
$$

where `mu_N` is an order-invariant base measure. But this is only a scaffolding unless the family is projectively consistent:

$$
\mathrm{Del}_{N\to M}\,\mathcal{W}_N
\approx
\mathcal{W}_M.
$$

In martingale form, the better target is:

$$
M_f(\chi)
=
F_f(C_\chi)
-
\int_0^\chi a_f(C_s)\,ds,
$$

with bracket:

$$
\langle M_f,M_g\rangle_\chi
=
\int_0^\chi \Gamma_{fg}(C_s)\,ds.
$$

This is the record-law version of "finite correlators": not just the mean drift, but the whole bracket hierarchy must be correct.

---

## 8. The useful ideas to import

The imported ideas that look genuinely useful are:

1. **Finite-action selection.** The law may be best found by asking which record histories have finite renormalized action under recursive coarse-graining.

2. **Quadratic penalties on defects.** Replace signed moment matching by squared, covariance-whitened defect fields.

3. **Fixed-point constraints.** Demand that the action form survives deletion/projective restriction.

4. **Correlator hierarchy.** Replace single-observable calibration with a hierarchy of cumulants or martingale brackets.

5. **Anisotropy/inhomogeneity suppression.** Translate this into interval-shape and density-regularity penalties, not into continuum curvature before emergence.

6. **Anomaly-cancellation thinking.** Look for special algebraic cancellations in record-defect beta functions. This may be the best lateral idea: the law might be singled out by the vanishing of projective drift for a whole basis of interval observables.

The incompatible imports are:

1. **Putting a metric into the fundamental law.**

2. **Using coordinate labels or hidden cluster labels.**

3. **Assuming a finite-neighbor cellular automaton as the microscopic law.**

4. **Treating the perturbative spin-2 ghost problem as a SHARD object without a metric Hilbert space.**

5. **Using a finite list of diagnostics as if it were a uniqueness theorem.**

---

## 9. Next campaign opened by this paper

The quadratic-gravity analogy does not open a brand-new final law by itself. It clarifies the next real move:

> **[OPEN] Build the projective quadratic/bracket action on the same object as the Paper XXIII likelihood wall, not on a small feature list.**

That means:

1. Compute or bound the actual unlabeled second moment:

$$
S_N
=
\mathbb{E}_{P_N}
\left[
\left(
\frac{dQ_N}{dP_N}
\right)^2
\right].
$$

2. Identify whether the linear-jitter clustered family is contiguous to sprinkling on the full unlabeled order sigma-field.

3. If it is contiguous, stop looking for an order-only detector of that adversary and move the record law to density/process regularity.

4. If it is not contiguous, find the stable rare-order class or aggregate Palm bracket that carries the divergence.

5. Only then attempt a quadratic projective action:

$$
A_*^{(N)}
=
\sum_{\ell\ge 1}
\lambda_\ell
\left\|
\mathcal{K}_{\ell,N}
-
\mathcal{K}_{\ell,N}^{\mathrm{spr}}
\right\|_{\Gamma_{\ell,N}^{-1}}^2,
$$

where `K_{\ell,N}` are order-only rooted, interval, and aggregate Palm kernels.

This is where the Turok/Boyle fixed-point analogy becomes operational: the correct law would be the one for which these defect beta functions vanish under deletion/coarse-graining.

---

## 10. Claims and nonclaims

**Claim.** A calibrated quadratic record action is compatible with SHARD when built from order-only record defects.

**Claim.** The finite receipt shows that quadratic penalties catch gross non-manifold orders and prevent simple signed-defect cancellation.

**Claim.** The same receipt shows that this finite quadratic projection does not solve the linear-jitter adversary.

**Claim.** The most valuable import from quadratic gravity is not the metric action itself; it is the finite-action, fixed-point, correlator/bracket mindset.

**Nonclaim.** This paper does not prove manifoldlikeness.

**Nonclaim.** This paper does not prove a unique record law.

**Nonclaim.** This paper does not establish compatibility between SHARD and every version of quadratic gravity.

**Nonclaim.** This paper does not solve the ghost problem, nor does it need to, because the ghost belongs to a continuum metric quantization not assumed here.

---

## References

1. K. S. Stelle, "Renormalization of Higher Derivative Quantum Gravity," *Phys. Rev. D* 16, 953 (1977). DOI: `10.1103/PhysRevD.16.953`.

2. Alberto Salvio, "Quadratic Gravity," *Frontiers in Physics* 6, 77 (2018), arXiv:1804.09944.

3. Jean-Luc Lehners and K. S. Stelle, "A Safe Beginning for the Universe?", *Phys. Rev. D* 100, 083540 (2019), arXiv:1909.01169.

4. Latham Boyle and Neil Turok, "Cancelling the vacuum energy and Weyl anomaly in the standard model with dimension-zero scalar fields," arXiv:2110.06258.

5. Neil Turok and Latham Boyle, "Gravitational entropy and the flatness, homogeneity and isotropy puzzles," arXiv:2201.07279.

6. Latham Boyle, Neil Turok, and Vatsalya Vaibhav, "Fixed points of classical gravity coupled with a Standard-Model-like theory," arXiv:2509.09346.

7. D. M. T. Benincasa and F. Dowker, "The Scalar Curvature of a Causal Set," *Phys. Rev. Lett.* 104, 181301 (2010), arXiv:1001.2725.

8. F. Dowker and L. Glaser, "Causal set d'Alembertians for various dimensions," arXiv:1305.2588.

9. Ludovico Machet and Jinzhao Wang, "On the continuum limit of Benincasa-Dowker-Glaser causal set action," arXiv:2007.13192.
