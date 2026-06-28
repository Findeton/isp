# The record click-law, XXIV: projective fixed-point search and the bracket wall

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-24. Twenty-fourth paper of the v7 program. This paper follows Paper XXIII's recursive interval and no-hidden-staging campaign. It asks how the full calibrated finite-dimensional record law could be found rather than merely named. Tags: **[PRINCIPLE]** = candidate formulation; **[STRESS TEST]** = finite diagnostic, not a theorem; **[COUNTEREXAMPLE]** = explicit obstruction or spoof; **[CONSTRAINED]** = narrowed but not unique; **[OPEN]** = disclosed residue. Numerical checks are in `v7/code/p24_projective_fixed_point_law.py`, all at mpmath `dps = 140`.

---

## Scope guards

1. **This paper does not derive the click law.** It gives an inverse route toward it and records the first failures of that route.

2. **Mean fingerprints are not the full law.** The receipt repeatedly finds that averaged finite signatures can be tuned. The target must include fluctuation and bracket data.

3. **Hidden labels are diagnostic only.** The receipt tracks hidden cluster multiplicity to understand adversaries, but the proposed law must be order-only and relabeling-invariant.

4. **The tests are 1+1-dimensional.** They are fixed-N stress tests for the current shard/manifoldlikeness problem, not a higher-dimensional theorem.

5. **No finite checklist theorem is claimed.** The useful object is an approximating action or compensator sequence whose limit is the full finite-dimensional law.

---

## Abstract

Paper XXIII ended with the statement that the click law probably needs the full calibrated finite-dimensional record law, or an action/compensator principle that reproduces it. This paper asks how to find such a law.

The first attempt is deletion projectivity. For a sprinkling law `Pi_N`, a uniform induced `m`-record suborder should have law `Pi_m`:

$$
C_N\sim \Pi_N,\qquad U_m\subset C_N
\quad\Longrightarrow\quad
C_N|_{U_m}\sim \Pi_m.
$$

This is true for finite binomial sprinklings, but as a practical discriminator it is too geometry-blind. In the receipt, a fixed sprinkling has deletion mean-signature score

`0.76010926263835077177`,

while the Paper XXIII regularity-aware clustered candidate has score

`0.88550596841134269807`.

That is only a mild separation, and it is not the right next law.

The second attempt uses causal intervals instead of random subsets. For every interval `I(x,y)`, condition on its size and demand the induced interior law to be the calibrated sprinkling law at that size:

$$
\mathcal{L}\!\left(C|_{I(x,y)}\ \middle|\ |I(x,y)|=k\right)
\approx
\Pi_k.
$$

This is sharper. The fixed sprinkling's interval fixed-point score is

`1.0322493697127026835`,

while the original Paper XXIII clustered candidate scores

`1.5459842417147670765`.

So causal interval recursion is a real improvement over random deletion.

But the hostile follow-up then tunes the coordinate-jitter cluster. A bounded search finds a `jitter=6/1`, `seed=16002` candidate with interval-only score

`0.75264159079495597304`,

below the fixed-sprinkling calibration score. A mean combined global-plus-interval score is also too weak in this finite receipt:

| family | combined mean score |
|---|---:|
| fixed sprinkling | `1.8641413095870703811` |
| original cluster | `2.3103809956150651297` |
| best tuned cluster | `1.1553550541278504275` |

This does not mean the cluster is the right law. It means averaged signatures are the wrong target.

The third attempt adds fluctuation information. The receipt compares interval-signature moment scores:

| family | interval moment score |
|---|---:|
| fixed sprinkling | `7.6933830645315982293` |
| original cluster | `6.2702887881782761517` |
| best mean-tuned cluster | `5.2753504838166316761` |

This crude standard-deviation score is independent information, but it does **not** solve the adversary either. The lesson is sharper: the missing object is not "add variance" generically. It is the calibrated **record martingale bracket** for interval observables.

The proposed next target is therefore an interval-compensator law. For order observables `f`, interval bands `B`, and calibrated sprinkling expectations,

$$
M_{f,B}(C)=
\sum_{x<y,\ |I(x,y)|\in B}
\left[
f\!\left(C|_{I(x,y)}\right)
-
\mathbb{E}_{\Pi_{|I(x,y)|}} f
\right]
$$

should have the correct mean-zero behavior and the correct bracket/covariance structure. The click law is not found by guessing one scalar penalty. It is found by calibrating these compensators, attacking them with adversaries, and looking for a compressed action whose minimizers reproduce both the interval fixed point and its fluctuation law.

---

## 1. The inverse problem

The phrase "full finite-dimensional record law" sounds enormous because it is enormous. For every finite size, it means the distribution of induced order patterns, rooted interval patterns, endpoint profiles, overlap profiles, near-neighborhood profiles, and their joint fluctuations.

That does not make the problem hopeless. It turns it into an inverse problem:

> Find a compact order-only action, transition rule, or compensator whose low-action or typical records reproduce the calibrated finite-dimensional law of sprinklings.

This is like learning a physical law from all finite correlation functions. The full set of correlations is too large to write as the law, but it can reveal the small principle generating it.

Paper XXIII suggests three requirements:

1. **Heredity:** causal intervals should look like smaller worlds.

2. **Extensionality/no-hidden-fiber:** records should not secretly duplicate causal roles.

3. **Density regularity:** the order should behave like finite-density sprinkling, not a lumpy clustered point process.

Paper XXIV adds a fourth:

4. **Bracket law:** the fluctuations of interval observables must match, not only their averages.

---

## 2. Why random deletion is not enough

A genuine fixed-N sprinkling is deletion-projective. If `m` records are chosen uniformly from an `N`-record sprinkling, the induced order has the same distribution as an `m`-record sprinkling.

This gives a tempting action:

$$
A_{\mathrm{del}}(C)=
\sum_{m\in M} w_m\,
D\!\left(
\mathcal{L}(C|_{U_m}),\Pi_m
\right),
$$

where `U_m` is a uniform `m`-record subset and `D` is a finite discrepancy between distributions.

The receipt tests mean signatures at `m=48,96,192`. This is order-only and relabeling-invariant. But it does not use causal geometry. A random subset is not a local window. It can miss density modulation that only appears when the order itself chooses intervals.

The receipt result is therefore negative:

| object | deletion mean-signature score |
|---|---:|
| fixed sprinkling | `0.76010926263835077177` |
| Paper XXIII cluster | `0.88550596841134269807` |

The cluster is only mildly worse. Random deletion is a useful consistency check, not the click-law skeleton.

---

## 3. Causal intervals are the right microscope

A causal interval is the order's own local microscope. The natural fixed-point target is:

$$
\mathcal{L}\!\left(C|_{I(x,y)}\ \middle|\ |I(x,y)|=k\right)
=
\Pi_k
$$

up to finite-N calibration and dimension-dependent corrections.

The receipt samples interval interiors in three size bands:

| band |
|---|
| `24-47` |
| `48-95` |
| `96-191` |

It compares mean signatures of those interval interiors against fresh sprinklings of matching sizes. This catches the original regularity-aware cluster:

| object | interval fixed-point score |
|---|---:|
| fixed sprinkling | `1.0322493697127026835` |
| Paper XXIII cluster | `1.5459842417147670765` |

So the first real answer to "how do we find the law?" is:

> Build the law from recursively sampled causal intervals, not from arbitrary record subsets.

This is the right direction, but not enough.

---

## 4. Mean interval laws can be tuned

The hostile review then asks whether a cluster can tune the interval mean signatures too.

The bounded search varies the coordinate-jitter span and seed in the Paper XXIII clustered family. The best mean interval candidate is:

| statistic | best tuned cluster |
|---|---:|
| jitter | `6/1` |
| seed | `16002` |
| `d_MM` | `1.99601610602633214` |
| `H/(2 sqrt(N))` | `0.893043135389700348` |
| `P_log2` ratio | `0.993303264595046776` |
| interval-only score | `0.75264159079495597304` |
| combined mean score | `1.1553550541278504275` |
| hidden-pair fraction at `m=96` | `0.0087719298245614035088` |

The important point is not the hidden label. The hidden label is not allowed in the law. The important point is that the order-only mean signatures are not enough. A tuned clustered coordinate process can look better than a particular fixed sprinkling under this crude finite score.

This gives the second answer:

> The law cannot be a mean profile. It must control the distribution, including fluctuations and covariance.

---

## 5. The bracket wall

The next obvious move is to add variance. The receipt tries a crude interval-signature moment score: compare both means and standard deviations of interval signatures against matching fresh sprinklings.

This is new information:

`moment score - mean interval score = 4.5227088930216757031`

for the best mean-tuned cluster.

But the crude moment score still does not reject the cluster:

| object | interval moment score |
|---|---:|
| fixed sprinkling | `7.6933830645315982293` |
| Paper XXIII cluster | `6.2702887881782761517` |
| best mean-tuned cluster | `5.2753504838166316761` |

This failure is valuable. It says "add variance" is too vague. The click-law target should use the actual compensated fluctuation law of record observables.

For a family of interval observables `f`, define:

$$
M_{f,B}(C)=
\sum_{x<y,\ |I(x,y)|\in B}
\left[
f\!\left(C|_{I(x,y)}\right)
-
\mathbb{E}_{\Pi_{|I(x,y)|}} f
\right].
$$

The target is not merely:

$$
\mathbb{E}M_{f,B}=0.
$$

It is also the bracket:

$$
\left\langle M_{f,B},M_{g,B'}\right\rangle
$$

or finite-record covariance kernel, calibrated from sprinklings and stated in order-only form.

This is the bridge back to the martingale language of Paper XXI. The scalar slogan was:

$$
N_\chi-\kappa\chi
$$

is the record martingale. The manifoldlikeness version should be:

> interval observables minus their sprinkling compensators form a calibrated record martingale field, with the correct bracket.

That is a much smaller target than "all finite-dimensional distributions" but much richer than a checklist.

---

## 6. Candidate law object

The receipt suggests a practical finite action:

$$
A(C)=
\sum_{B,f} w_{B,f}\,
D_{\mathrm{mean}}\!\left(M_{f,B}(C),0\right)
+
\sum_{B,B',f,g} \lambda_{B,B',f,g}\,
D_{\mathrm{bracket}}\!\left(
\langle M_{f,B},M_{g,B'}\rangle,
\langle M_{f,B},M_{g,B'}\rangle_{\Pi}
\right).
$$

This is not proposed as the final law. It is the next search object.

The hoped-for compression is that many of these terms collapse to a small principle, for example:

- interval-local maximum entropy subject to the record martingale bracket;
- a causal-set analogue of independent Poisson increments, stated through interval compensators;
- a renormalization fixed point under "choose an interval, condition on size, forget the outside";
- a BDG-like action whose second variation supplies the bracket;
- an exchangeable-poset limit principle plus a finite-density fluctuation condition.

If no compression appears, the program remains an infinite calibration scheme. If a compression appears, that is the click-law skeleton.

---

## 7. What to do next

The next investigation should not add another scalar. It should do three concrete things.

1. Build a basis of small interval observables:

   `f = relation fraction, height, H_k bins, endpoint loads, near-neighborhood tails, overlap counts, induced pattern densities`.

2. Calibrate their compensators and covariance kernels on many independent sprinklings:

   $$
   \mathbb{E}_{\Pi_k}f,\qquad
   \operatorname{Cov}_{\Pi_k}(f,g).
   $$

3. Run adversarial optimization against the resulting bracket action, not just against means.

The pass/fail criterion should be brutal:

- if clustered/fiber/staged constructions can minimize the bracket action, the action is missing an observable or a structural term;
- if they cannot, try to compress the successful action into a closed law;
- if no compression is found, the result is a calibrated effective law, not a fundamental click law.

---

## 8. Precision receipt

The receipt `v7/code/p24_projective_fixed_point_law.py` uses integer bitset counts for finite posets and mpmath `dps=140` for non-integer arithmetic. No float64 arithmetic is used for asserted quantities. The command used in this workspace is:

`isp/code/.venv/bin/python isp/v7/code/p24_projective_fixed_point_law.py`

Executed checks:

- fixed sprinkling is deletion-projective within finite sampled calibration: pass;
- deletion-projective mean signatures are too weak to reject the clustered candidate: pass;
- causally selected interval recursion is sharper than random deletion: pass;
- interval-only recursion can be tuned below the fixed-sprinkling interval calibration: pass;
- mean combined global-plus-interval scoring is still too weak in the bounded search: pass;
- the original clustered candidate is disfavored by the combined mean action: pass;
- best bounded tuned candidate still retains hidden cluster multiplicity: pass;
- fluctuation/bracket data are independent information beyond mean interval signatures: pass.

Final receipt line:

`CHECKS PASSED: 8/8`.

---

## 9. Claims and non-claims

**Claims.**

1. Random deletion projectivity is a valid consistency property of sprinklings but too geometry-blind to serve as the next click-law target. **[STRESS TEST]**

2. Causally selected interval recursion is sharper and catches the original Paper XXIII clustered candidate in the finite receipt. **[STRESS TEST]**

3. Mean interval signatures, even when combined with global mean signatures, can be tuned by a coordinate-jitter clustered adversary in the bounded receipt. **[COUNTEREXAMPLE / CONSTRAINED]**

4. The next target must include fluctuation/bracket data, not only mean interval content. **[CONSTRAINED]**

5. A crude standard-deviation score is not the final bracket law; it demonstrates independence of fluctuation information but does not solve the adversary. **[STRESS TEST / OPEN]**

6. The most promising mathematical object is an interval-compensator martingale field with calibrated covariance/bracket. **[PRINCIPLE / OPEN]**

**Non-claims.**

1. No unique click law is derived.

2. No manifoldlikeness theorem is proved.

3. The finite discrepancy scores are not universal constants.

4. The hidden cluster labels are not part of the proposed law.

5. The best tuned cluster is not claimed to be physically acceptable; it is an adversary showing that mean profiles are insufficient.

6. The bracket formula is a target, not an established action.

7. The paper does not solve the higher-dimensional case.

---

## 10. Hostile review pass

**Review A: "Deletion projectivity is basically tautological and too weak."**  
Accepted. It is a valid property of sprinklings, but uniform subsets are not causal neighborhoods. The receipt keeps it only as a baseline and moves to interval-selected suborders.

**Review B: "The interval fixed point only catches the cluster you already knew about."**  
Accepted and followed. The receipt tunes the clustered family against the interval mean score and finds a stronger `jitter=6/1`, `seed=16002` adversary.

**Review C: "A mean action is not a law."**  
Accepted. The tuned adversary beats both interval-only and crude combined mean scores in the receipt. This is the main negative result of the paper.

**Review D: "Then add variance."**  
Tried, but not enough in this crude form. The interval moment score is independent information, yet it still scores the tuned cluster below the fixed sprinkling. The right object is not arbitrary variance; it is the calibrated martingale bracket/covariance kernel for interval observables.

**Review E: "You are using hidden labels."**  
Only diagnostically. The law proposals use intervals, induced orders, compensators, and covariance kernels. The hidden-pair fraction explains the adversary but is not a permitted observable.

**Review F: "This still sounds infinite."**  
Correct. The present object is an infinite calibration target. The research problem is to find a compression: a small action, compensator, or maximum-entropy principle that reproduces the calibrated interval means and brackets.

Status after this pass: **accepted as a narrowing paper, rejected as a final click law. The target has moved from full finite-dimensional means to interval compensators with calibrated brackets.**

---

## References

**Companion program.**

- *The record click-law, XXI* (v7) -- scalar record martingale principle.
- *The record click-law, XXII* (v7) -- marked compensators, interval-profile calibration, moment underdetermination, and transitivity tax.
- *The record click-law, XXIII* (v7) -- recursive interval laws, no-hidden-staging, hidden-fiber adversaries, and density/regularity wall.
- `v7/code/p24_projective_fixed_point_law.py` -- high-precision receipt for this paper.

**External orientation.**

- L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, *Space-time as a causal set*, Phys. Rev. Lett. 59, 521 (1987) -- order plus number as geometry.
- D. J. Daley and D. Vere-Jones, *An Introduction to the Theory of Point Processes* -- point-process compensators, Palm ideas, and count fluctuations.
- S. Janson, *Poset limits and exchangeable random posets* -- finite-dimensional distributions as poset-limit data.
