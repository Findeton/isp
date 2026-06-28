# The record click-law, XXV: calibrated interval brackets and the joint-field wall

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-25. Twenty-fifth paper of the v7 program. This paper follows Paper XXIV's projective fixed-point and bracket-wall audit. It calibrates a finite interval-observable covariance action and attacks it with the clustered adversaries opened in Papers XXIII-XXIV. Tags: **[PRINCIPLE]** = candidate formulation; **[STRESS TEST]** = finite diagnostic, not a theorem; **[COUNTEREXAMPLE]** = explicit obstruction or spoof; **[CONSTRAINED]** = narrowed but not unique; **[OPEN]** = disclosed residue. Numerical checks are in `v7/code/p25_interval_bracket_action.py`, all at mpmath `dps = 140`.

---

## Scope guards

1. **This paper does not derive the click law.** It builds and attacks the next finite approximation: an interval-compensator bracket action.

2. **The bracket action is calibrated, not fundamental.** It depends on a finite observable basis, finite bands, finite calibration samples, and a whitening convention.

3. **The result is adversarial, not triumphalist.** The calibrated interval bracket catches the previous mean-tuned cluster, then a new bracket-tuned cluster appears.

4. **Hidden labels are diagnostic only.** Hidden cluster multiplicity is reported to understand the adversary, not used in the proposed law.

5. **All tests are 1+1 finite-N stress tests.** No higher-dimensional uniqueness theorem or asymptotic classification is claimed.

---

## Abstract

Paper XXIV showed that mean interval fingerprints are not the click law. A clustered coordinate adversary could tune random-deletion and interval-mean signatures. The next proposed object was a calibrated interval martingale bracket:

$$
M_{f,B}(C)=
\sum_{x<y,\ |I(x,y)|\in B}
\left[
f\!\left(C|_{I(x,y)}\right)
-
\mathbb{E}_{\Pi_{|I(x,y)|}}f
\right],
$$

with not only mean-zero behavior but also the correct covariance/bracket.

This paper makes that finite. For each causal interval band

$$
B\in \{24\text{-}47,\ 48\text{-}95,\ 96\text{-}191\},
$$

the receipt calibrates the mean and covariance of a six-component observable vector on independent 1+1 sprinklings:

$$
f(J)=
\left(
r,\ 
\frac{H}{2\sqrt{|J|}},\
\Theta_2,\
\frac{P_{\log 2}}{\mathbb{E}_{\Pi_{|J|}}P_{\log 2}},\
E_{\max},\
T_{\mathrm{near}}
\right).
$$

Candidate interval residuals are whitened by the calibrated covariance. The finite bracket score is:

$$
A_B(C)=
\|\overline{Z}_B\|^2
+
\left\|
\overline{Z_B Z_B^{\mathsf T}}-I
\right\|_F^2.
$$

This is a real advance. A fixed sprinkling has calibrated bracket action

`4.7228296999511580264`.

The Paper XXIII regularity-aware cluster scores

`13.764332856045287563`,

and the Paper XXIV mean-tuned cluster scores

`5.9210952159554569934`.

So the calibrated bracket catches both previous enemies.

Then the campaign follows the opening. A bounded hostile search over clustered coordinate-jitter processes finds a new bracket-tuned adversary:

| statistic | bracket-tuned cluster |
|---|---:|
| jitter | `3/1` |
| seed | `16003` |
| interval bracket action | `3.1957397888444246959` |
| search-resolution fixed sprinkling bracket action | `4.4389592054740385182` |
| `d_MM` | `1.8498456042458308` |
| `H/(2 sqrt(N))` | `1.04613624431364898` |
| `P_log2` ratio | `0.991677802876592393` |
| hidden-pair fraction in `48-95` intervals | `0.029782026384376735634` |

Thus interval brackets alone are still not the law. The bracket-tuned winner pays elsewhere: a crude full-size whitened score gives

| object | full-size whitened score |
|---|---:|
| fixed sprinkling | `35.0096939669538094` |
| bracket-tuned cluster | `74.0372098762606927` |

The next target is therefore sharper:

> not an interval bracket action alone, but a **joint global-and-interval compensator field**, with calibrated covariance across full-order observables and interval observables.

---

## 1. From moments to brackets

Paper XXIII showed that finite moment profiles can be tuned. Paper XXIV showed that mean interval laws can also be tuned. The natural repair is not "add another scalar," but:

1. choose a family of interval observables `f`;
2. subtract the calibrated sprinkling expectation;
3. compare both the residual mean and residual covariance.

In martingale language, this asks for the bracket, not merely the drift.

For a finite interval band `B`, define residuals

$$
R_{f,B}(x,y)=
f\!\left(C|_{I(x,y)}\right)
-
\mathbb{E}_{\Pi_{|I(x,y)|}}f.
$$

The finite action approximates the law by asking:

$$
\mathbb{E}R_{f,B}=0,
\qquad
\mathbb{E}R_{f,B}R_{g,B'}
=
\operatorname{Cov}_{\Pi}(f,g;B,B').
$$

The receipt implements a finite, band-local version of this. It does not yet include cross-band covariance or full-order covariance.

---

## 2. Observable basis

For each interval interior `J`, the receipt computes:

| component | meaning |
|---|---|
| `r` | related-pair fraction |
| `H/(2 sqrt(|J|))` | finite 1+1 height scaling |
| `Theta_2` | first recursive relation fraction |
| `P_log2` ratio | interval-profile generating-function ratio |
| `E_max` | max endpoint load among small internal intervals |
| `T_near` | soft near-neighborhood fraction |

This basis is intentionally not final. It is the smallest useful basis for this receipt because it includes the quantities that previous adversaries learned to tune one by one.

For each band, independent sprinklings produce a mean vector and covariance matrix. Candidate residuals are whitened:

$$
Z_B=L_B^{-1}\left(f-\mu_B\right),
$$

where

$$
\Sigma_B=L_B L_B^{\mathsf T}.
$$

The score is:

$$
A_B(C)=
\|\overline{Z}_B\|^2
+
\frac{1}{d^2}
\sum_{i,j}
\left(
\overline{Z_iZ_j}-\delta_{ij}
\right)^2.
$$

The first term is the compensator drift. The second term is the bracket defect.

---

## 3. Calibration

The receipt calibrates on five independent `N=384` sprinklings, with ten sampled intervals per band from each calibration sprinkling. The calibrated band means are:

| band | `r` | height ratio | `Theta_2` | `P_log2` ratio | endpoint max | near fraction |
|---|---:|---:|---:|---:|---:|---:|
| `24-47` | `0.510816150111853961` | `0.773535532782275483` | `0.488165524568085178` | `1.0139218305783709` | `1.58380158597744332` | `0.023042598129202848` |
| `48-95` | `0.501283999400927269` | `0.818747081558626464` | `0.496174288483400803` | `1.01191142815665662` | `1.60432618660204875` | `0.00624048401271279612` |
| `96-191` | `0.508747586898827574` | `0.85241957219474649` | `0.500744909412359458` | `1.01317029682450169` | `1.63295918702075664` | `0.00180419308234984318` |

The calibration is deliberately modest. This keeps the receipt runnable and exposes finite-sample weaknesses rather than hiding them.

---

## 4. Bracket action against previous enemies

The full-size summaries are:

| object | `d_MM` | height ratio | `Theta_2` | `P_log2` ratio | near fraction |
|---|---:|---:|---:|---:|---:|
| fixed sprinkling | `1.91288268507861852` | `0.969589689851674664` | `0.517231127404706075` | `0.989551897094434276` | `0.00129188424717145344` |
| Paper XXIII cluster | `1.98901459389216855` | `0.995105208005666102` | `0.508102255538894192` | `0.988355340545194693` | `0.00135987815491731941` |
| Paper XXIV mean-tuned cluster | `1.99601610602633214` | `0.893043135389700348` | `0.498582223374968744` | `0.993303264595046776` | `0.00130548302872062663` |

The calibrated interval bracket score is:

| object | total | mean part | bracket part |
|---|---:|---:|---:|
| fixed sprinkling | `4.72282969995115803` | `3.81537906931422436` | `0.907450630636933662` |
| Paper XXIII cluster | `13.7643328560452876` | `10.1606262760155537` | `3.60370658002973383` |
| Paper XXIV mean-tuned cluster | `5.92109521595545699` | `5.41485431185277938` | `0.506240904102677613` |

This is the first good news:

> **[CONSTRAINED] The calibrated interval bracket is strictly stronger than the Paper XXIV mean interval score in this receipt.**

It catches the original density/regularity cluster and the mean-tuned cluster.

---

## 5. The bracket-tuned adversary

The campaign then attacks the bracket action directly. The bounded search varies the clustered coordinate-jitter family over:

$$
\mathrm{jitter}\in\{2,\dots,8\},\qquad
\mathrm{seed}\in\{16000,\dots,16009\}.
$$

The best bracket-tuned adversary is:

| statistic | value |
|---|---:|
| jitter | `3/1` |
| seed | `16003` |
| interval bracket action | `3.1957397888444246959` |
| mean part | `2.38627709951936915` |
| bracket part | `0.809462689325055545` |
| `d_MM` | `1.8498456042458308` |
| height ratio | `1.04613624431364898` |
| `P_log2` ratio | `0.991677802876592393` |
| near fraction | `0.00119669277632724108` |

At the same search resolution, the fixed sprinkling scores:

`4.4389592054740385182`.

So interval brackets alone can still be tuned.

The hidden diagnostic shows the adversary remains clustered:

| band | hidden-pair fraction |
|---|---:|
| `48-95` | `0.029782026384376735634` |

This hidden diagnostic is not part of the proposed law. Its role is to explain what the order-only bracket score missed.

---

## 6. The joint-field wall

The bracket-tuned winner pays in full-size global context. A separate full-order whitening calibration gives:

| object | full-size whitened score |
|---|---:|
| fixed sprinkling | `35.0096939669538094` |
| Paper XXIII cluster | `22.4939512701422974` |
| Paper XXIV mean-tuned cluster | `2.10248646170236844` |
| bracket-tuned cluster | `74.0372098762606927` |

This full-size calibration is crude and noisy; the fixed sprinkling score is itself large. So it is not a final action. But it shows independence: the interval bracket score and global score are not the same information.

Combining the search-resolution interval bracket with the full-size score gives:

| object | combined score |
|---|---:|
| fixed sprinkling | `39.448653172427848` |
| bracket-tuned cluster | `77.2329496651051174` |

This opens the next target:

> **[CONSTRAINED] The law should not be an interval bracket action alone. It should be a joint compensator field over full-order observables, interval observables, and their cross-covariances.**

In formula form, the target is closer to:

$$
\mathcal{A}(C)=
\left\|
\mathbb{E}Z_{\mathrm{global,interval}}
\right\|^2
+
\left\|
\mathbb{E}
\left[
Z_{\mathrm{global,interval}}
Z_{\mathrm{global,interval}}^{\mathsf T}
\right]
-I
\right\|^2,
$$

where `Z_global,interval` includes both full-order and interval-residual observables after covariance calibration.

This is no longer a scalar click law. It is a finite approximation to a martingale field.

---

## 7. What this implies for finding the click law

The campaign now has a more disciplined search loop:

1. Calibrate a covariance field on sprinklings.

2. Whiten candidate residuals.

3. Attack with clustered/fiber/staged adversaries.

4. If an adversary wins locally, add the missing joint context.

5. If a covariance field survives adversaries, try to compress it into a small compensator/action principle.

The best new idea is therefore:

> The click law may be the compressed form of a joint interval/global martingale bracket, not a direct formula for interval counts.

This connects back to the earlier scalar martingale:

$$
N_\chi-\kappa\chi.
$$

The scalar record martingale is only the first coordinate. Manifoldlikeness requires a field of record martingales over interval observables, with a calibrated bracket.

---

## 8. Precision receipt

The receipt `v7/code/p25_interval_bracket_action.py` uses integer bitset counts for finite posets and mpmath `dps=140` for non-integer arithmetic. No float64 arithmetic is used for asserted quantities. The command used in this workspace is:

`isp/code/.venv/bin/python isp/v7/code/p25_interval_bracket_action.py`

Executed checks:

- original clustered adversary is disfavored by the calibrated bracket action: pass;
- Paper XXIV mean-tuned adversary is still visible to the calibrated bracket action: pass;
- bounded bracket-tuned clustered adversary still exists at this receipt resolution: pass;
- bracket-tuned winner keeps hidden clustered multiplicity diagnostically: pass;
- global full-size context is independent of the interval bracket score: pass.

Final receipt line:

`CHECKS PASSED: 5/5`.

---

## 9. Claims and non-claims

**Claims.**

1. A finite interval-observable covariance/bracket action can be calibrated on sprinklings and evaluated order-only on candidate posets. **[STRESS TEST]**

2. This calibrated interval bracket action catches the Paper XXIII cluster and the Paper XXIV mean-tuned cluster in the receipt. **[STRESS TEST]**

3. A bounded bracket-tuned clustered adversary still beats the interval-only bracket score at search resolution. **[COUNTEREXAMPLE / CONSTRAINED]**

4. The bracket-tuned adversary pays in a separate full-size global whitening score, showing that interval brackets and global context carry independent information. **[STRESS TEST]**

5. The next candidate object is a joint global-and-interval compensator/bracket field. **[PRINCIPLE / OPEN]**

**Non-claims.**

1. No unique click law is derived.

2. No manifoldlikeness theorem is proved.

3. The finite scores are not universal constants.

4. The covariance calibration is not asymptotic and not high-statistics.

5. The hidden cluster diagnostic is not part of the law.

6. The bracket-tuned adversary is not claimed to be physically acceptable; it is a stress construction.

7. The joint-field action is not yet implemented at full strength; only a crude global add-on is tested.

---

## 10. Hostile review pass

**Review A: "The covariance calibration is small and noisy."**  
Accepted. The calibration uses five sprinklings and finite interval samples to keep the receipt runnable. The paper treats it as a stress test, not a final action.

**Review B: "The bracket action only catches yesterday's adversary."**  
Accepted and followed. The receipt attacks the bracket action directly and finds a new bracket-tuned cluster.

**Review C: "If the bracket-tuned cluster beats the interval score, the bracket failed."**  
It failed as a standalone law, but it succeeded as a narrowing move. It catches the Paper XXIV mean-tuned cluster, then exposes the need for joint global-and-interval covariance.

**Review D: "The global full-size score is itself noisy; fixed sprinkling has score 35."**  
Accepted. The full-size score is not a finished calibration. The only claim is independence: the best interval-bracket adversary pays in global context, so the next action must include cross-covariance rather than isolated interval bands.

**Review E: "Hidden labels are doing the explanatory work."**  
Only in the hostile diagnosis. The actual bracket score uses only order observables. Hidden labels show that the low interval-bracket score can still come from clustered construction.

**Review F: "This is becoming an infinite feature-learning problem."**  
Correct unless a compression is found. The next mathematical problem is to discover whether the successful joint covariance field has a compact expression: maximum entropy, independent-increment compensator, BDG-like action, or renormalization fixed point.

Status after this pass: **accepted as a narrowing paper, rejected as a final click law. The target has moved from interval brackets to a joint global-and-interval martingale bracket field.**

---

## References

**Companion program.**

- *The record click-law, XXI* (v7) -- scalar record martingale principle.
- *The record click-law, XXIII* (v7) -- recursive interval laws, no-hidden-staging, hidden-fiber adversaries, and density/regularity wall.
- *The record click-law, XXIV* (v7) -- projective fixed-point search and the bracket wall.
- `v7/code/p25_interval_bracket_action.py` -- high-precision receipt for this paper.

**External orientation.**

- L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, *Space-time as a causal set*, Phys. Rev. Lett. 59, 521 (1987) -- order plus number as geometry.
- D. J. Daley and D. Vere-Jones, *An Introduction to the Theory of Point Processes* -- compensators, Palm ideas, and count fluctuations.
- S. Janson, *Poset limits and exchangeable random posets* -- finite-dimensional distributions as poset-limit data.
