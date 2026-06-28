# The record click-law, XXVII: unlabeled second moment and the linear-window washout fork

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-27. Twenty-seventh paper of the v7 program. This paper follows Paper XXVI's quadratic record-action campaign and returns to the decisive obstruction from Paper XXIII: whether the linear-jitter hidden-cluster adversary is genuinely contiguous to 1+1 sprinkling on the full unlabeled order sigma-field. Tags: **[PRINCIPLE]** = candidate formulation; **[STRESS TEST]** = finite diagnostic, not a theorem; **[COUNTEREXAMPLE]** = explicit obstruction or spoof; **[CONSTRAINED]** = narrowed but not unique; **[OPEN]** = disclosed residue. Numerical checks are in `v7/code/p27_unlabeled_second_moment_contiguity.py`, `v7/code/p27_linear_window_theorem_fork.py`, `v7/code/p27_sqrt_global_witness_attack.py`, `v7/code/p23_selected_rare_class_n10_n12_audit.py`, `v7/code/p27_n12_adaptive_invariant_screen.py`, `v7/code/p27_quotient_washout_proof_skeleton.py`, `v7/code/p27_lemma_m_one_pair_projection.py`, `v7/code/p27_density_matched_rank_kernel_projection.py`, `v7/code/p27_rank_copula_bound_scaling.py`, `v7/code/p27_nonshared_cycle_neutrality.py`, `v7/code/p27_higher_cycle_residue_scaling.py`, `v7/code/p27_cluster_expansion_bound_audit.py`, `v7/code/p27_matching_free_energy_separator.py`, `v7/code/p27_physical_pressure_asymptotic_adversary.py`, `v7/code/p27_fourier_wave_boundary.py`, `v7/code/p27_sectoral_pressure_marks.py`, `v7/code/p27_mark_anti_laundering.py`, `v7/code/p27_projective_mark_field_law.py`, `v7/code/p27_local_mark_coupling_gate.py`, `v7/code/p27_intrinsic_local_response_gate.py`, `v7/code/p27_shell_projection_bound.py`, `v7/code/p27_coherent_shell_cancellation.py`, `v7/code/p27_integrated_click_law_matrix.py`, `v7/code/p27_linear_window_polymer_budget.py`, and `v7/code/p27_continuous_copula_envelope.py`, at mpmath `dps = 140`.

---

## Scope guards

1. **This paper does not prove asymptotic contiguity.** It computes the exact-denominator finite object at `N=8` and uses split samples to reduce one-sample square bias.

2. **The adversary is frozen.** The clustered law is not changed after seeing diagnostics. It is the width-2 law `Q_N(2,c)`: replace each base sprinkling point by two records, jitter them by a coordinate window proportional to `cN`, then forget hidden pair labels.

3. **The denominator is exact only at `N=8`.** No sparse empirical estimate of `P_N(o)` is used as a substitute for the null denominator.

4. **The receipt is order-only.** Hidden pair labels are used only to generate `Q_N`; all measured outcomes are unlabeled transitive-order codes.

5. **The conclusion is adversarial.** Sharp and quarter-scale clustering are visible. Linear half/one/two schedules are not visible in this exact-`P_8` split audit. That is evidence for washout, not a triumph.

---

## Abstract

Papers XXIII-XXVI repeatedly narrowed the record-law problem to a single fork. Let `P_N` be the unlabeled law of a fixed-`N` 1+1 sprinkling, and let `Q_N` be a hidden clustered law projected to unlabeled orders. The decisive object is not another scalar feature. It is the likelihood second moment:

$$
S_N
=
\mathbb{E}_{P_N}
\left[
\left(
\frac{dQ_N}{dP_N}
\right)^2
\right]
=
\sum_o \frac{q_N(o)^2}{p_N(o)}.
$$

If `S_N` remains bounded in the linear-window clustered family, then the hidden cluster is likely washed out on the unlabeled order sigma-field. If `S_N` diverges, then some rare unlabeled order classes must carry the residue:

$$
\frac{q_N(o)^2}{p_N(o)}
\gg
p_N(o).
$$

This paper freezes the adversary and computes the exact finite denominator at `N=8`. To avoid one-sample square bias, the receipt estimates

$$
\widehat{S}_8
=
\sum_o
\frac{\widehat{q}_{A}(o)\widehat{q}_{B}(o)}{p_8(o)}
$$

from two independent `Q_8` samples, and calibrates the same estimator on independent sprinkling samples.

The exact zero-jitter hidden-pair law has

`S_8 = 1362.66666666666667`.

The quarter schedule is also visible:

`mean excess = 0.0707762718200683594`,

against a hostile split-null excess guard

`0.0305699586719211126`.

But the linear half/one/two schedules stay inside the null guard:

| schedule | mean second moment | mean excess | verdict |
|---|---:|---:|---|
| `linear_half` | `0.996932888031005859` | `-0.00306711196899414062` | inside |
| `linear_one` | `1.00674262046813965` | `0.00674262046813964844` | inside |
| `linear_two` | `0.999636268615722656` | `-0.00036373138427734375` | inside |

The rare-class opening is followed in the same receipt. The largest accumulated positive contribution above the half scale is only

`0.00478171696739`,

far below the deliberately loose `0.25` alarm threshold.

Therefore the clean finite conclusion is:

> **[CONSTRAINED] The exact `P_8` second-moment ladder sees sharp and quarter-scale clustering, but gives no evidence of a stable rare-order residue for the width-2 linear half/one/two schedules. The next honest theorem is bounded-width linear-window contiguity/washout, unless a larger exact-denominator computation finds a residue.**

The theorem path is then followed. It splits into a useful negative and a useful positive. The negative result is that direct coupling of the **marked coordinate-rank process** to iid ranks is too strong: for finite linear mixing ratio `c`, two hidden siblings retain a positive Palm bracket

$$
B(c)
=
\operatorname{Var}
\left(
\mathbb{E}[F_c(S+E)\mid S]
\right).
$$

For example,

`B(1)=0.0150545634920634921`.

The positive result is local washout: hidden sibling mass is sparse in unrooted order data. A uniformly sampled `k`-record induced suborder sees a same-hidden-cluster collision with probability at most

$$
\binom{k}{2}\frac{w-1}{N-1}.
$$

Thus every `k_N=o(\sqrt N)` unrooted induced-suborder test is asymptotically blind, conditional on the no-collision rank-kernel convergence. The first possible accumulation scale is `k \sim a\sqrt N`, where the limiting expected hidden-collision count is

$$
\frac{a^2(w-1)}{2}.
$$

So the proof target has sharpened: full contiguity cannot be proved by marked-rank iid coupling, and any remaining order-only witness must be sqrt-scale, global, or exact-likelihood/selected-class.

---

## 1. The frozen adversary

Start with a base 1+1 sprinkling of `N/2` records in permutation form. Replace each base record by two records. For each hidden pair, assign local coordinates

$$
u = U_i + \delta_u,
\qquad
v = V_i + \delta_v,
$$

with local ordering inside the pair used only to break ties. The jitter variables are sampled from a window of rank size proportional to `cN`. After generating the coordinate order, hidden pair labels are discarded.

This defines an unlabeled order law:

$$
Q_N(2,c).
$$

The schedules tested at `N=8` are:

| schedule | jitter window |
|---|---:|
| `linear_quarter` | `N/4` |
| `linear_5_16` | `5N/16` |
| `linear_3_8` | `3N/8` |
| `linear_half` | `N/2` |
| `linear_one` | `N` |
| `linear_two` | `2N` |

The point of freezing the adversary is to stop chasing moving counterexamples. The question is now a clean likelihood question: is this family distinguishable from sprinkling after forgetting labels?

---

## 2. Exact denominator at `N=8`

At `N=8`, the receipt enumerates all coordinate permutations:

$$
8! = 40320.
$$

Each induced transitive order is canonicalized under record relabeling. The exact unlabeled support size is

`14794`.

This gives exact probabilities:

$$
p_8(o)
=
\mathbb{P}_{P_8}(O=o).
$$

The receipt checks relabel invariance of the canonical code. The check passes.

The zero-jitter clustered law is also exact at `N=8`. Its hidden pair outcomes have:

| quantity | value |
|---|---:|
| outcomes | `9216` |
| support | `16` |
| second moment | `1362.66666666666667` |
| excess | `1361.66666666666667` |
| TV proxy | `0.999231150793650794` |

This confirms that the likelihood object sees real hidden clustering when it is present.

---

## 3. Split estimator

The receipt does not estimate

$$
\sum_o
\frac{\widehat{q}(o)^2}{p(o)}
$$

from one sample, because that has a positive self-collision bias. Instead it uses independent samples:

$$
\widehat{S}_8
=
\sum_o
\frac{\widehat{q}_{A}(o)\widehat{q}_{B}(o)}{p_8(o)}.
$$

The same split estimator is calibrated under `P_8`, using independent sprinkling samples. With `sample_count = 8192` and `10` null repetitions:

| null statistic | value |
|---|---:|
| mean excess | `-0.00271818637847900391` |
| std excess | `0.0110960483501333722` |
| max excess | `0.0135436058044433594` |
| hostile excess guard | `0.0305699586719211126` |
| TV guard | `0.545873829675099206` |

The TV number is large because both empirical samples are sparse on a support of `14794`. It is used only as a hostile finite guard, not as a physical claim about total variation.

---

## 4. The finite ladder

The exact-`P_8` split ladder gives:

| schedule | mean second | mean excess | excess/guard | verdict |
|---|---:|---:|---:|---|
| `linear_quarter` | `1.07077627182006836` | `0.0707762718200683594` | `2.31522301288150729` | visible |
| `linear_5_16` | `1.02673807144165039` | `0.0267380714416503906` | `0.874651867495314672` | inside |
| `linear_3_8` | `1.0118255615234375` | `0.0118255615234375` | `0.386836032405219619` | inside |
| `linear_half` | `0.996932888031005859` | `-0.00306711196899414062` | `-0.100330916436969905` | inside |
| `linear_one` | `1.00674262046813965` | `0.00674262046813964844` | `0.220563610847561572` | inside |
| `linear_two` | `0.999636268615722656` | `-0.00036373138427734375` | `-0.011898327641883126` | inside |

This is the sharpest finite picture so far:

$$
\text{sharp clustering visible}
\quad\longrightarrow\quad
\text{quarter visible}
\quad\longrightarrow\quad
\text{linear half/one/two washed into null guard}.
$$

The finite boundary between `1/4` and `5/16` at `N=8` should not be overinterpreted. The robust statement is only that the tested linear half/one/two schedules do not show a second-moment signal at this scale.

---

## 5. Rare-order opening

A bounded second moment can still hide a rare-class problem if the sampling is too small. Therefore the receipt follows the obvious opening: accumulate the largest positive class contributions across split repetitions.

For an order class `o`, the positive contribution is:

$$
\max
\left(
\frac{\widehat{q}_{A}(o)\widehat{q}_{B}(o)}{p_8(o)}
-p_8(o),
0
\right).
$$

The largest accumulated positive contributions above the half scale are:

| schedule | largest accumulated positive contribution |
|---|---:|
| `linear_half` | `0.00478171696739` |
| `linear_one` | `0.00365588627164` |
| `linear_two` | `0.00265406351241` |

The largest of these is:

`0.00478171696739`.

This is far below the alarm threshold:

`0.25`.

The classes also do not recur as stable cross-repetition survivors; they mostly appear as one-hit empirical spikes. This does not prove absence of a rare class, but it gives no finite evidence for one.

---

## 6. The theorem target

The natural asymptotic statement is now:

> **Bounded-width linear-window washout conjecture.** Fix width `w`. Let `Q_N(w,c)` be the clustered 1+1 coordinate law with jitter window `cN`, projected to unlabeled orders. For sufficiently large `c>0`, the unlabeled laws `Q_N(w,c)` and `P_N` are mutually contiguous, and possibly
>
> $$
> \mathbb{E}_{P_N}
> \left[
> \left(
> \frac{dQ_N(w,c)}{dP_N}
> \right)^2
> \right]
> =
> O(1).
> $$

A stronger version would prove:

$$
S_N(w,c)
\to
1
$$

as `c` grows at fixed width, after projection to unlabeled orders.

The opposite theorem would be equally useful:

> **Rare-class residue theorem.** There exists a stable order class family `A_N` such that
>
> $$
> \frac{Q_N(A_N)^2}{P_N(A_N)}
> $$
>
> contributes a non-vanishing or divergent amount to `S_N`.

The receipt supports the first direction at finite `N=8`, but does not prove it.

---

## 7. The theorem fork

The first theorem pass tries the most tempting proof route:

$$
\text{linear-window clustered coordinate ranks}
\approx
\text{iid coordinate ranks}.
$$

That route fails if the ranks are **marked** by hidden sibling identity. Let

$$
X=S+E,
$$

where

$$
S\sim\operatorname{Uniform}[0,1],
\qquad
E\sim\operatorname{Uniform}[-c,c],
$$

and let `F_c` be the marginal CDF of `X`. The rank-uniform coordinate is

$$
R=F_c(S+E).
$$

For two hidden siblings sharing the same parent `S`,

$$
B(c)
=
\operatorname{Cov}(R_1,R_2)
=
\operatorname{Var}
\left(
\mathbb{E}[R\mid S]
\right).
$$

The receipt computes:

| `c` | `B(c)` | `NVar`, width 2 | `NVar`, width 4 |
|---|---:|---:|---:|
| `0.25` | `0.0676587301587301587` | `0.150992063492063492` | `0.28630952380952381` |
| `0.5` | `0.0408730158730158730` | `0.124206349206349206` | `0.205952380952380952` |
| `1` | `0.0150545634920634921` | `0.0983878968253968254` | `0.12849702380952381` |
| `2` | `0.00445653521825396825` | `0.0877898685515873016` | `0.0967029389880952381` |
| `4` | `0.00120626782614087302` | `0.0845396011594742063` | `0.0869521368117559524` |
| `8` | `0.000313428848508804563` | `0.0836467621818421379` | `0.0842736198788597470` |
| `16` | `0.0000798615198286752852` | `0.0834131948531620086` | `0.0835729178928193592` |

The iid value is:

$$
\frac{1}{12}
=
0.0833333333333333333\ldots
$$

So finite `c` leaves a positive marked coordinate Palm bracket. Direct marked-rank total-variation coupling to iid ranks is therefore too strong as a proof of order washout.

The positive theorem is local and unrooted. In a width-`w` clustered law, the fraction of hidden sibling pairs among all record pairs is:

$$
\frac{w-1}{N-1}.
$$

For a uniformly sampled `k`-record induced suborder, the sibling-collision probability is bounded by:

$$
\mathbb{P}(\text{sibling collision})
\le
\binom{k}{2}
\frac{w-1}{N-1}.
$$

Consequently, if

$$
k_N=o(\sqrt N),
$$

then hidden sibling collisions vanish. Conditional on no hidden sibling collision, the sampled records come from distinct parents; in the linear-window regime their two coordinate rankings converge to the same finite-rank kernel as ordinary 1+1 sprinkling. Hence:

> **[CONSTRAINED] Every uniformly sampled `k_N=o(\sqrt N)` unrooted induced-suborder test is asymptotically blind to bounded-width linear-window hidden clustering.**

The receipt checks the collision bound for width `2`:

| `beta` in `k=N^beta` | bound at `N=10^8` |
|---|---:|
| `0.25` | `0.000049500000495000005` |
| `0.40` | `0.0125373601253736013` |
| `0.49` | `0.345820863458208635` |
| `0.50` | `0.49995000499950005` |
| `0.60` | `19.9045798490457985` |

The `beta=0.49` convergence is slow, but the exponent is in the right regime. At the square-root scale, hidden collisions accumulate:

$$
k=a\sqrt N
\quad\Longrightarrow\quad
\mathbb{E}[\text{sibling collisions}]
\to
\frac{a^2(w-1)}{2}.
$$

For `a=1`, this gives:

| width | limiting mean sibling collisions |
|---|---:|
| `2` | `0.5` |
| `4` | `1.5` |
| `8` | `3.5` |

This gives the clean theorem fork:

1. **Marked coordinate rank coupling fails.** Finite linear mixing has a positive hidden-sibling Palm bracket.

2. **Sub-sqrt unrooted order probes wash out.** They miss hidden siblings with high probability.

3. **The remaining witness, if any, must be sqrt-scale or global.** It must live in the exact unlabeled likelihood, a selected rare-order class, or a genuinely global Palm/Mecke/bracket statistic.

This is not full contiguity. It is a real theorem-shaped narrowing of where a full contiguity proof or counterexample can live.

---

## 8. Square-root/global witness attack

The theorem fork says that any remaining unrooted order-only witness must live at square-root scale or above. The next receipt therefore samples:

$$
k=\lfloor 2\sqrt N\rfloor
$$

record induced suborders and measures only order-visible pair-neighborhood similarity statistics:

| feature | meaning |
|---|---|
| relation density | induced relation fraction |
| degree variance | variance of internal past-plus-future degree |
| max pair similarity | largest pairwise external-neighborhood agreement |
| p99 pair similarity | upper-tail pair similarity |
| top5 pair similarity | mean of five most similar pairs |
| tail similarity `>=0.90` | fraction of highly similar pairs |

Hidden labels are used only for a diagnostic: the receipt checks that the sampled suborders actually contain the predicted number of hidden sibling collisions. The expected collision count is:

$$
\binom{k}{2}\frac{w-1}{N-1}.
$$

At `N=512`, `k=45`, this is:

`1.93737769080234834`.

At `N=1024`, `k=64`, this is:

`1.97067448680351906`.

The diagnostic collision ratios across all tested clustered schedules are:

`0.99545455, 0.93323864, 0.95628157, 0.94245581, 0.97241162, 1.0161932, 0.98769664, 0.96277769, 0.97410449`.

So the square-root hidden-collision field is present at the expected scale.

The order-only witness result is weaker. The first `N=512` calibration block flags `linear_two`:

| block | held-out max | `linear_half` | `linear_one` | `linear_two` |
|---|---:|---:|---:|---:|
| `N=512`, seed block 0 | `6.42926239539225852` | `5.87946742227091496` | `6.30451336832819351` | `11.2204280707224468` |

But the independent `N=512` block does not reproduce it:

| block | held-out max | `linear_half` | `linear_one` | `linear_two` |
|---|---:|---:|---:|---:|
| `N=512`, seed block 7000000 | `28.9506457570731643` | `9.76238531020261125` | `8.54461296418084388` | `9.50488194806799965` |

And `N=1024` does not reproduce it:

| block | held-out max | `linear_half` | `linear_one` | `linear_two` |
|---|---:|---:|---:|---:|
| `N=1024`, seed block 0 | `19.2072193077163446` | `8.42041331867761915` | `13.7255886191288589` | `14.1750824105624322` |

The receipt therefore demotes the candidate:

> **[STRESS TEST] The square-root hidden-collision field is real and appears at the predicted rate, but the tested order-only pair-similarity witness does not robustly separate the linear-window clustered schedules. The one visible `N=512` signal is finite calibration leakage unless a stronger repeatable statistic is found.**

This is stronger washout evidence than the sub-sqrt theorem, but still not full contiguity.

---

## 9. Selected-denominator attack beyond `N=8`

The second attack follows the exact likelihood route. The full denominator

$$
P_N(C)
$$

is not enumerated at `N=10` or `N=12`. Instead, the selected-class formula is used for candidate classes repeated by split `Q_N` samples:

$$
P_N(C)
=
\frac{r(C)}{|\operatorname{Aut}(C)|\,N!},
$$

where `r(C)` is the number of realizer first-orders compatible with the selected order class.

At `N=10`, the selected-denominator receipt samples repeated candidate classes and resolves exact denominators for `18` candidates. For the linear half/one schedules, the largest resolved contribution is:

`0.0540733337402`.

The important resolved half/one rows are:

| schedule | candidate | exact `P_N(C)` | contribution |
|---|---:|---:|---:|
| `linear_half` | `0` | `2.20458553792e-6` | `0.0135183334351` |
| `linear_half` | `1` | `1.10229276896e-6` | `0.0135183334351` |
| `linear_half` | `2` | `3.30687830688e-6` | `0.00450611114502` |
| `linear_one` | `0` | `5.5114638448e-7` | `0.0540733337402` |
| `linear_one` | `1` | `1.10229276896e-6` | `0.0135183334351` |
| `linear_one` | `2` | `5.5114638448e-7` | `0.0270366668701` |

This is not a large selected contribution. The receipt uses a loose alarm threshold of `0.25`, and the maximum half/one contribution stays below it.

At `N=12`, the first receipt does not substitute a sparse empirical null denominator. It reports the initial wall honestly: exact unlabeled canonicalization and realizer/aut counting must be improved before `N=12` can become a full selected-denominator attack.

The follow-up raises the `N=12` hard-schedule screen to `65536` samples per side for `linear_half`, `linear_one`, and `linear_two`, and adds a matched sprinkling-null split screen. It still does not use a sparse empirical denominator. Instead it groups by a cheap invariant, promotes split-overlap singleton keys to raw-degree exact isomorphism, and attempts selected denominators:

| schedule | split overlap keys | exact repeated | resolved selected denominators | unresolved selected | resolved aggregate | Q/null aggregate ratio |
|---|---:|---:|---:|---:|---:|---:|
| sprinkling null | `28` | `27` | `26` | `1` | `0.762096047401` | `1` |
| `linear_half` | `37` | `37` | `33` | `4` | `0.986697524786` | `1.29472` |
| `linear_one` | `37` | `36` | `31` | `5` | `1.14662926644` | `1.50457` |
| `linear_two` | `35` | `35` | `31` | `4` | `0.890661031008` | `1.1687` |

Across the raised `N=12` screen:

| statistic | value |
|---|---:|
| Q total split-overlap invariant keys | `109` |
| max overlap product | `1` |
| Q exact repeated classes | `108` |
| Q resolved selected denominators | `95` |
| Q unresolved selected counts | `13` |
| max selected contribution | `0.0557631254196` |
| Q aggregate resolved selected contribution | `3.02398782223` |
| sprinkling-null aggregate resolved selected contribution | `0.762096047401` |
| max per-schedule Q/null aggregate ratio | `1.50457317073` |

This moves the wall again. The easy "no overlap at `N=12`" story is gone, but the overlaps are singleton, exact selected denominators resolve for most of them, the largest individual contribution is not large, and the aggregate selected contribution is comparable to the sprinkling-null aggregate on a per-schedule basis.

So the selected-denominator result is:

> **[STRESS TEST] The exact selected-denominator attack beyond `N=8` finds no large half/one rare-class residue at `N=10`, and the raised `N=12` singleton-overlap screen resolves 95 Q selected denominators with max contribution `0.0557631254196`. The aggregate resolved selected contribution is order-one, but a matched sprinkling null is also order-one; the largest per-schedule Q/null aggregate ratio is `1.50457317073`. The remaining `N=12` barrier is repeated-mass growth, unresolved selected counts, and an asymptotic aggregate-null comparison.**

---

## 10. Why this matters for the click law

If the washout conjecture is true, then a pure order-only law cannot punish the linear-jitter hidden cluster by a small finite observable. The cluster has become an ordinary finite-density perturbation of the coordinate process after labels are forgotten.

Then the click-law search must change target. It cannot merely say:

$$
\text{detect hidden fibers.}
$$

It must say something like:

$$
\text{select the correct projective point-process density law.}
$$

That is a density/process regularity problem, not only a manifoldlikeness problem.

If the rare-class theorem is true instead, then the click law can remain order-only, but the missing statistic is not a low-order interval moment. It must be a selected likelihood, aggregate Palm bracket, or high-order rare-class action that sees the residue.

This is why Paper XXVI's quadratic-action idea has to be tied to the likelihood object. A quadratic action over hand-picked features is not enough. The real quadratic object is:

$$
A_N(Q\|P)
\sim
\log
\mathbb{E}_{P_N}
\left[
\left(
\frac{dQ_N}{dP_N}
\right)^2
\right].
$$

---

## 11. Hostile reviews

### Review 1: `N=8` is tiny

Correct. The paper does not claim asymptotic contiguity. Its value is that `N=8` is large enough for an exact unlabeled denominator and small enough to avoid fake empirical `P_N` substitution.

The repair is explicit: the next result must be a theorem or a larger exact-denominator computation.

### Review 2: The split estimator can miss very rare classes

Correct. That is why the receipt accumulates top positive contributions. It finds no stable class above the half scale, but this is not a proof. A rare class below the sampling resolution could still exist.

The next computational path is exact selected-denominator counting beyond `N=8`, not another sparse null denominator.

### Review 3: The TV guard is huge

Correct. The empirical support is sparse, so total variation is not interpreted physically. The important object is the cross second moment with exact `p_8(o)`.

### Review 4: The finite boundary at `1/4` versus `5/16` may be noise

Correct. The paper does not promote that boundary to a law. The robust finding is only the qualitative ladder: sharp and quarter visible; half/one/two inside.

### Review 5: If washout is true, this damages the order-only program

Yes. That is why this paper matters. If linear-window clustered processes are contiguous after projection to unlabeled orders, then the record law must include a density/process regularity principle or a projective construction that rules them out before they become order-indistinguishable.

### Review 6: If washout is false, the receipt has not found the residue

Correct. Then the next enemy is a stable rare-order class. The paper narrows the search: it must evade exact `P_8`, top-contribution accumulation, near-twin tails, rooted small-window tests, and the finite bracket projections already tried in Paper XXIII.

### Review 7: Marked rank residue means washout is false

Not by itself. The marked coordinate process retains hidden sibling information, but SHARD's record law cannot use hidden sibling labels or coordinate marks. The relevant question is whether that marked residue survives projection to the unlabeled causal order. The sub-sqrt theorem says many natural unrooted probes cannot see it.

### Review 8: Sub-sqrt washout is much weaker than full contiguity

Correct. It leaves square-root-scale, mesoscopic, and global witnesses alive. This is why the paper keeps the exact likelihood and selected-denominator paths open.

### Review 9: The sqrt attack found one visible signal

Accepted and followed. The signal appears only for `N=512`, `linear_two`, seed block 0. It does not reproduce in an independent `N=512` block and does not reproduce at `N=1024`. The paper demotes it to finite calibration leakage, not a residue.

### Review 10: The selected-denominator attack is still too small

Correct. It reaches exact selected denominators for `N=10` and a raised singleton-overlap selected screen at `N=12`, but not a full `S_N` computation. It is valuable because it does not fake the denominator with sparse empirical `P_N`; it also fails to find a large half/one/two residue in the resolved selected classes.

### Review 11: The quotient theorem is only conditional

Correct. Route 1 does not prove contiguity. It proves the algebraic shape of the theorem once Lemma M is available. The missing content is substantial: a projected local factor bound and nonshared-cycle neutrality on the unlabeled order sigma-field.

### Review 12: The `O(1/N)` random-pair bracket can still aggregate

Correct. The random unrooted pair bracket going to zero rules out a naive local bracket witness. It does not rule out an aggregate sparse-pair likelihood, selected rare denominator, or non-neutral cycle sum. Those are now the precise enemies.

### Review 13: The one-pair test can create its own density artifact

Correct. The first one-pair finite model jitters only the hidden pair while leaving the other records unjittered. Wide jitter then creates an order-visible density/outlier signal. The repair is the marginal-matched Palm model, where every record has the same one-record coordinate marginal and only the hidden pair shares a parent center.

### Review 14: Unlabeled projection may not erase the Palm residue

Correct. The rank-kernel receipt shows only mild contraction from labeled permutation likelihood to unlabeled canonical-order likelihood. At `N=8`, the largest tested projection ratio is `0.985176741102174549`. The useful smallness comes mainly from the density-matched rank copula becoming close to iid as `c` grows, not from the quotient map erasing the signal.

### Review 15: The rank-copula bound still needs an analytic proof

Correct. The scaling receipt proves an exact finite representation identity after numerical margin projection and tests boundedness of `A_N(c)` only up to `N=24`. The theorem still needs an analytic uniform bound on `A_N(c)` and then a nonshared-cycle neutrality proof.

### Review 16: Nonshared neutrality is not exact at all orders

Correct. Two disjoint pair factors have an exact closed form and are suppressed strongly. Three disjoint pair factors show a small signed cycle residue. The result is controlled neutrality, not zero neutrality. The remaining theorem must bound all higher cycle residues uniformly.

---

## 12. Claims and nonclaims

**Claim.** The exact `P_8` unlabeled second-moment object detects zero-jitter hidden clustering with `S_8 = 1362.66666666666667`.

**Claim.** The exact `P_8` split ladder detects the quarter schedule but not the tested half/one/two linear schedules.

**Claim.** The accumulated rare-class audit finds no stable large positive contribution above the half scale.

**Claim.** Direct marked-rank iid coupling is too strong because finite linear mixing has positive sibling bracket `B(c)`.

**Claim.** Uniformly sampled `k_N=o(\sqrt N)` induced-suborder tests wash out under bounded hidden width, modulo the no-collision rank-kernel convergence.

**Claim.** The square-root hidden-collision field is present at the predicted scale, but the tested order-only pair-similarity witness does not robustly separate the linear schedules.

**Claim.** The `N=10` selected-denominator attack resolves exact probabilities for selected candidates and finds no large half/one contribution.

**Claim.** The raised `N=12` adaptive selected screen resolves 95 singleton-overlap Q selected denominators, finds no large individual half/one/two contribution, and finds per-schedule aggregate contributions comparable to a matched sprinkling null.

**Claim.** The quotient-level proof path reduces to a precise missing lemma: a projected local factor bound together with nonshared-cycle neutrality.

**Claim.** The marked sibling bracket projects to a random unrooted pair bracket of order `O(1/N)`, so any surviving bracket residue must be aggregate, selected, or cycle-nonneutral.

**Claim.** The naive one-pair local model fails because it changes the one-record density, but the marginal-matched one-pair Palm model removes the visible wide-jitter obstruction at exact denominators `N=5..8`.

**Claim.** The exact rank-kernel projection receipt shows that unlabeled projection contracts the density-matched one-pair Palm residue only mildly; the smallness mechanism is rank-copula mixing in `c`.

**Claim.** After marginal projection, the density-matched one-pair labeled second moment has the exact finite form `A_N(c)^2/d_N`, with `d_N=N(N-3)/2`; hence a uniform bound on `A_N(c)` gives the desired one-pair `O(N^-1)` local `L^2` norm.

**Claim.** For two disjoint localized pair factors, zero-row neutrality gives the exact formula `rho_2 = 2A_N(c)/((N-2)(N-3))`; triple factors have a small nonzero cycle residue in the tested range.

**Claim.** Zero-row neutrality plus bounded one-pair energy is not enough for the full cluster theorem: a balanced block matrix passes the two-factor test but creates coherent high-order matching residue. The missing condition is closer to matching/free-energy regularity or the full finite-dimensional record law.

**Claim.** The matching-tail/free-energy profile separates tested macroscopic staged blocks from tested physical rank-copula kernels, while small staged admixtures can remain below the finite physical envelope. The candidate law is therefore a macroscopic staged/fiber regularity law, not an infinitesimal trace detector.

**Claim.** Raw matching tail is not the final diagnostic: a wide-jitter small-`N` physical corner and a tuned four-block defeat tail-only separation. The pressure density `N^-1 log Z_N(D;N)` is stronger in the current finite audit.

**Claim.** Fourier/coherent-wave kernels are a genuine boundary case: pure low-frequency modes can exceed the physical pressure envelope, while spectrally spread Fourier bands can fall below the staged-block floor. Pressure density should therefore be sectoral, not a naked ban on all coherent modes.

**Claim.** Explicit marks can rescue a pure Fourier wave, but naive mark projection is not enough: mixed physical-plus-wave residual pressure can increase after normalization, and smooth marks can partially launder block geometry.

**Claim.** Anti-laundering is not a cosmetic condition. Free post-hoc marks make block geometry admissible, exact block marks pay `O(N)` exact-step action, Fourier-band laundering pays growing bandwidth/action, and smooth steep marks can approximate blocks with bounded-in-`N` but large finite action. The law must therefore be a joint geometry-plus-mark action, not projection followed by forgiveness.

**Claim.** The anti-laundering gate has a plausible projective form: marks earn projection credit only when they belong to a pre-geometric tight-action field law. Exact hidden partition labels have refinement action growing linearly in `N`; fixed smooth profiles and low Fourier modes have bounded refinement action; approaching the exact block by steepening costs diverging action.

**Claim.** Projective admissibility is still not enough if the mark-to-geometry projection map is arbitrary. A block mark globally coupled as `f(i)f(j)` erases block geometry exactly, while local stress-type couplings project only `O(N^-2)` of the same global block. Mark projection credit must therefore be local/stress-type, or a nonlocal interaction sector must be explicitly introduced and charged.

**Claim.** The allowed local response family can be made order-intrinsic by using small interval shells, but shell locality must be coupled to shell-density/interval-profile regularity. On seeded sprinkling-like permutation orders, shell-local marked responses do not strongly project onto dense global block/cosine products as `N` grows; on a two-layer order, links are dense and shell-local stress launders the layer block exactly.

**Claim.** A deterministic shell-projection inequality now supplies the first small theorem: projection onto a shell-local marked span is bounded by the dense target's mass inside the shell supports, amplified by zero-row efficiency and Gram conditioning. For staged block targets the finite bound is tight and shrinks with shell density; for coherent cosine targets it is valid but loose.

**Claim.** Coherent-wave leakage is governed by a different deterministic bound: projection onto intrinsic shell-local stress tensors is controlled by normalized target-response correlations and Gram conditioning. In the finite receipt, the coherent projection falls from `0.099662119798697` at `N=32` to `0.01075222645749` at `N=192`, while the support-mass bound remains much looser.

**Claim.** The integrated candidate-law matrix is sectoral rather than scalar: macroscopic order pressure, shell regularity, projective mark admissibility, local/stress coupling, coherent correlation control, and the unlabeled second-moment fork play distinct roles. The matrix covers the current non-open adversaries and deliberately leaves the bounded-width linear hidden cluster open.

**Claim.** The linear-window polymer-budget receipt finds no growing low-order polymer residue in the tested rank-copula model. The truncated budget is at most `0.00396620845573223759`; the same-hidden-pair term dominates; the `r=2,3,4,5` disjoint-cycle tail decreases; and widening the mixing window suppresses the budget monotonically.

**Claim.** The continuous copula-envelope receipt identifies a concrete analytic lemma target: for `c >= 1/2`, the audited continuum and finite data are consistent with `A_N(c) <= K/c^2` using the loose guard `K=0.075`. The continuous quadrature gives `max c^2 A_infty(c) = 0.0726153470569359606` over `c=0.5,1,2,4`.

**Claim.** The next honest mathematical move is to prove the quotient local-factor/nonshared-neutrality lemma, or to disprove it by constructing a stable selected rare denominator or aggregate sparse-pair bracket.

**Nonclaim.** This paper does not prove contiguity.

**Nonclaim.** This paper does not prove that all hidden clusters wash out.

**Nonclaim.** This paper does not identify the final click law.

**Nonclaim.** This paper does not prove that every arbitrarily small staged admixture is detectable by order-only matching pressure.

**Nonclaim.** This paper does not yet decide whether Fourier/coherent-wave kernels are admissible matterlike structure or another non-manifold staging mode.

**Nonclaim.** This paper does not provide a matter-sector field-energy law; it only identifies where such a sector appears necessary.

**Nonclaim.** This paper does not license arbitrary marks as free explanatory variables; mark energy, residual amplitude, and independence from the geometry must still be controlled.

**Nonclaim.** This paper does not define the final admissible mark field law. It only shows that admissibility must be projective, charged by action/complexity, and fixed before geometry projection rather than chosen post hoc.

**Nonclaim.** This paper does not prove the full marked-sector continuum theorem. The projective tight-action criterion is a candidate gate supported by finite receipts and the standard one-dimensional compactness intuition.

**Nonclaim.** This paper does not derive the final mark-to-geometry coupling. It only rules out free global pair-product projection as too permissive.

**Nonclaim.** This paper does not prove that fixed small-shell tests characterize manifoldlikeness. The two-layer adversary shows the opposite: intrinsic local response requires a separate manifoldlike shell-density law.

**Nonclaim.** The shell-projection bound is not the final coherent-wave/matter theorem. It is a support-mass theorem; coherent fields require additional cancellation, spectral, or field-law structure.

**Nonclaim.** The coherent cancellation receipt is finite and one-dimensional. It identifies the right inequality and obstruction, but does not prove the full asymptotic spectral cancellation theorem for all admissible fields or higher-dimensional shells.

**Nonclaim.** The integrated matrix is not a proof of uniqueness, minimality, or final correctness of the record click-law. It is an adversary coverage ledger.

**Nonclaim.** The polymer-budget receipt is truncated and labeled-rank-level. It is not the unlabeled second moment `S_N`, and it does not control all polymer orders.

**Nonclaim.** The continuous copula envelope is a theorem target, not a proof. The finite-dimensional inequality `A_N(c) <= K/c^2` and its passage through unlabeled quotienting remain to be proved.

**Nonclaim.** This paper does not justify using sparse empirical `P_N` denominators at larger `N`.

---

## 13. Receipt ledger

Command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_unlabeled_second_moment_contiguity.py
```

Receipt summary:

| check | result |
|---|---|
| exact `P_8` law is computed and canonical code is relabel invariant | PASS |
| exact zero-jitter clustered law has huge direct unlabeled second moment | PASS |
| split null guard is finite and calibrated | PASS |
| sublinear/quarter schedule is visible at exact `P_8` | PASS |
| linear half/one/two schedules stay inside the hostile split-null guard | PASS |
| no stable large rare-order contribution survives above the half scale | PASS |

Final receipt line:

`CHECKS PASSED: 6/6`

Second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_linear_window_theorem_fork.py
```

Second receipt summary:

| check | result |
|---|---|
| finite linear mixing has positive marked coordinate Palm bracket | PASS |
| strong mixing reduces but does not erase finite-`c` marked residue | PASS |
| direct marked-rank iid coupling is too strong as a proof of order washout | PASS |
| unrooted hidden sibling pair mass is `O(1/N)` | PASS |
| sub-sqrt induced-suborder collision bounds decrease across tested `N` | PASS |
| critical and supercritical windows are not covered by the local washout bound | PASS |
| square-root samples have nonzero limiting hidden-collision mass | PASS |

Second final receipt line:

`CHECKS PASSED: 7/7`

Third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_sqrt_global_witness_attack.py
```

Third receipt summary:

| check | result |
|---|---|
| sqrt sampled suborders have the predicted nonzero hidden-collision scale | PASS |
| order-only sqrt witness schedules are classified against held-out sprinklings | PASS |
| no sqrt order-only witness is robust across independent calibration blocks | PASS |
| the receipt follows the sqrt-scale opening rather than a sub-sqrt checklist | PASS |

Third final receipt line:

`CHECKS PASSED: 4/4`

Fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p23_selected_rare_class_n10_n12_audit.py
```

Fourth receipt summary:

| check | result |
|---|---|
| candidate classes are collected for `N=10` and the `N=12` feasibility scan completes | PASS |
| at least one `N=10` candidate receives an exact selected denominator | PASS |
| the audit handles `N=12` without sparse empirical `P` | PASS |
| resolved half/one candidates do not show a large selected contribution | PASS |
| unresolved selected denominators are reported rather than replaced by empirical `P` | PASS |

Fourth final receipt line:

`CHECKS PASSED: 5/5`

Fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_n12_adaptive_invariant_screen.py
```

Fifth receipt summary:

| check | result |
|---|---|
| adaptive `N=12` invariant screen completes at raised sample size | PASS |
| sprinkling null split screen is computed for aggregate calibration | PASS |
| raised screen finds only singleton split-overlap invariant keys | PASS |
| singleton overlap keys receive exact isomorphism attempts | PASS |
| within-side invariant collisions remain sparse at `N=12` | PASS |
| resolved `N=12` selected contributions are not large when present | PASS |
| aggregate resolved selected contribution is explicitly reported | PASS |
| per-schedule aggregate contribution is comparable to sprinkling null | PASS |
| no sparse empirical `P_N` denominator is used | PASS |

Fifth final receipt line:

`CHECKS PASSED: 9/9`

Sixth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_quotient_washout_proof_skeleton.py
```

Sixth receipt summary:

| check | result |
|---|---|
| marked bracket is real but belongs to a marked refinement | PASS |
| random unrooted pair projection of the marked bracket decays as `O(1/N)` | PASS |
| conditional local-factor theorem would force diagonal residue to vanish | PASS |
| if the local factor is only `K/sqrt(N)`, cross terms can diverge | PASS |
| finite rare-order receipts do not currently show a large individual selected residue | PASS |
| finite aggregate selected ratio is order-one, not a divergence certificate | PASS |
| sub-sqrt bracket tests remain asymptotically blind by collision counting | PASS |
| square-root scale remains the first live bracket scale | PASS |

Sixth final receipt line:

`CHECKS PASSED: 8/8`

Seventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_lemma_m_one_pair_projection.py
```

Seventh receipt summary:

| check | result |
|---|---|
| exact denominators are used for every tested `N` | PASS |
| one-pair projected support remains inside the 1+1 sprinkling support | PASS |
| naive one-pair model exposes a density/outlier obstruction | PASS |
| marginal matching weakens the wide-jitter local obstruction | PASS |
| finite data still do not certify Lemma M | PASS |

Seventh final receipt line:

`CHECKS PASSED: 5/5`

Eighth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_density_matched_rank_kernel_projection.py
```

Eighth receipt summary:

| check | result |
|---|---|
| axis rank kernels are normalized | PASS |
| node-doubling convergence is adequate for the finite receipt | PASS |
| labeled Palm residue is positive before quotienting | PASS |
| unlabeled projection is an `L^2` contraction of the labeled likelihood | PASS |
| at `N=8` unlabeled projection contracts but does not erase the residue | PASS |
| density-matched rank residue shrinks rapidly with mixing `c` | PASS |
| finite rank-kernel data do not prove the `O(N^-1)` norm bound | PASS |

Eighth final receipt line:

`CHECKS PASSED: 7/7`

Ninth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_rank_copula_bound_scaling.py
```

Ninth receipt summary:

| check | result |
|---|---|
| margin projection enforces zero row sums | PASS |
| margin correction is controlled and explicitly reported | PASS |
| node-doubling convergence is adequate for scaling receipt | PASS |
| representation formula matches exact permutation second moment at `N<=8` | PASS |
| axis copula excess is bounded over tested `N` for each `c` | PASS |
| axis copula excess falls rapidly as `c` grows | PASS |
| formula bound gives `O(N^-2)` one-pair labeled excess when `A_N` is bounded | PASS |

Ninth final receipt line:

`CHECKS PASSED: 7/7`

Tenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_nonshared_cycle_neutrality.py
```

Tenth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| disjoint two-factor moment matches the closed form | PASS |
| disjoint two-factor aggregate is tiny over tested width-2 matchings | PASS |
| nonshared two-factor moment is small compared with same-edge variance | PASS |
| two-factor aggregate falls rapidly as `c` grows | PASS |
| disjoint three-factor aggregate is small but not zero | PASS |

Tenth final receipt line:

`CHECKS PASSED: 6/6`

Eleventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_higher_cycle_residue_scaling.py
```

Eleventh receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| higher-cycle aggregate residues remain small in tested range | PASS |
| hardest aggregate by `r` decreases after the two-factor term | PASS |
| cycle aggregates fall rapidly with mixing `c` | PASS |
| no tested higher cycle beats the two-factor aggregate | PASS |

Eleventh final receipt line:

`CHECKS PASSED: 5/5`

Twelfth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_cluster_expansion_bound_audit.py
```

Twelfth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced after `A`-normalization | PASS |
| two-factor formula holds for every hostile matrix | PASS |
| zero-row-only cluster bound is false in hostile search | PASS |
| balanced block creates coherent high-order matching residue | PASS |
| physical rank-copula remains far below hostile block aggregate | PASS |
| block obstruction has collapsed stable rank | PASS |
| random projected controls have larger stable rank | PASS |
| stable rank alone is not the final separator | PASS |
| two-factor neutrality misses the high-order obstruction | PASS |

Twelfth final receipt line:

`CHECKS PASSED: 9/9`

Thirteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_matching_free_energy_separator.py
```

Thirteenth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| universal two-factor coefficient is reproduced | PASS |
| matching tail separates staged blocks from physical kernels in this audit | PASS |
| balanced two-block has large matching-tail amplification | PASS |
| physical kernels remain subcritical by tail ratio | PASS |
| physical kernels remain below hostile pressure at `z=N` | PASS |
| random projected matrices are not automatically rejected like staged blocks | PASS |
| physical-plus-block tail increases with block contamination at `N=12` | PASS |
| small staged admixture can remain below the finite physical envelope | PASS |

Thirteenth final receipt line:

`CHECKS PASSED: 9/9`

Fourteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_physical_pressure_asymptotic_adversary.py
```

Fourteenth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| universal `q_2` coefficient is reproduced | PASS |
| physical `c=0.5` tail decreases over tested `N` | PASS |
| physical wide-jitter corner is the only tested tail above one | PASS |
| all physical pressure densities stay below `0.7` | PASS |
| tail alone fails against tuned fixed blocks | PASS |
| pressure density separates fixed macroscopic staged adversaries | PASS |
| structured Fourier adversaries can violate both pressure diagnostics | PASS |
| pressure density detects `N=12` contamination at finite threshold | PASS |

Fourteenth final receipt line:

`CHECKS PASSED: 9/9`

Fifteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_fourier_wave_boundary.py
```

Fifteenth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| universal `q_2` coefficient is reproduced | PASS |
| pure Fourier modes can exceed the physical pressure envelope | PASS |
| Fourier bands can fall back below the block pressure floor | PASS |
| spectral spreading increases effective rank | PASS |
| `cos1` pressure is not a finite `N=8` accident | PASS |
| random Fourier spectra straddle the staged-block pressure floor | PASS |

Fifteenth final receipt line:

`CHECKS PASSED: 7/7`

Sixteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_sectoral_pressure_marks.py
```

Sixteenth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| universal `q_2` coefficient is reproduced when residual is nonzero | PASS |
| correct Fourier marks erase pure `cos1` geometry pressure | PASS |
| wrong Fourier marks do not erase `cos2` pressure | PASS |
| correct Fourier marks remove mixed wave amplitude but not always pressure shape | PASS |
| block can be marked away only with growing mark energy | PASS |
| low-frequency Fourier mark energy stays bounded while block energy grows | PASS |
| smooth marks can partially but not uniformly launder block geometry | PASS |

Sixteenth final receipt line:

`CHECKS PASSED: 8/8`

Seventeenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_mark_anti_laundering.py
```

Seventeenth receipt summary:

| check | result |
|---|---|
| exact block labels can erase block geometry only with growing exact-step action | PASS |
| low Fourier field marks have bounded action over tested `N` | PASS |
| smooth steep marks strongly align with block but pay large finite action | PASS |
| spectral tail detects nontrivial blocklike content in steep marks | PASS |
| Fourier bands launder the block only by increasing bandwidth and action | PASS |
| exact small-`N` pair projections show the same laundering ladder | PASS |
| a single smooth steep mark partially launders pair geometry but does not make projection free | PASS |
| free post-hoc marks would make block geometry admissible, so admissibility is essential | PASS |

Seventeenth final receipt line:

`CHECKS PASSED: 8/8`

Eighteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_projective_mark_field_law.py
```

Eighteenth receipt summary:

| check | result |
|---|---|
| low Fourier mode has projectively bounded action | PASS |
| exact block label has linearly growing refinement action | PASS |
| fixed smooth steep field is projectively tight but not exact block | PASS |
| approaching exact block by steepening costs increasing action | PASS |
| finite-action steepening shows a nonzero action-defect tradeoff | PASS |
| Fourier approximation of a block requires growing bandwidth action | PASS |
| growth exponents separate smooth fields from hidden partition labels | PASS |

Eighteenth final receipt line:

`CHECKS PASSED: 7/7`

Nineteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_local_mark_coupling_gate.py
```

Nineteenth receipt summary:

| check | result |
|---|---|
| global pair-product mark projection erases block geometry exactly | PASS |
| endpoint-additive local stress has zero zero-row geometry projection | PASS |
| local wall-stress product projection decays like `O(N^-2)` | PASS |
| global Fourier product erases coherent cosine geometry exactly | PASS |
| local cosine stress does not launder global coherent pair geometry | PASS |
| local coupling separates admissible marks from nonlocal projection credit | PASS |

Nineteenth final receipt line:

`CHECKS PASSED: 6/6`

Twentieth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_intrinsic_local_response_gate.py
```

Twentieth receipt summary:

| check | result |
|---|---|
| sprinkling-like small interval shells are sparse and become sparser over the tested range | PASS |
| intrinsic shell-local mark stress has decreasing projection on global block products | PASS |
| intrinsic shell-local mark stress also weakens on coherent cosine products | PASS |
| genuinely shell-local marked responses remain in the intrinsic local span | PASS |
| two-layer orders make intrinsic local shells dense | PASS |
| dense shell locality can launder staging and must be rejected by shell regularity | PASS |

Twentieth final receipt line:

`CHECKS PASSED: 6/6`

Twenty-first command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_shell_projection_bound.py
```

Twenty-first receipt summary:

| check | result |
|---|---|
| deterministic projection bound dominates every tested actual projection | PASS |
| sprinkling-like shell support fraction decreases over tested range | PASS |
| block projection and bound both shrink with sprinkling-like shells | PASS |
| cosine actual projection shrinks but the support-mass bound is loose | PASS |
| two-layer dense shell adversary saturates projection and fails shell gate | PASS |

Twenty-first final receipt line:

`CHECKS PASSED: 5/5`

Twenty-second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_coherent_shell_cancellation.py
```

Twenty-second receipt summary:

| check | result |
|---|---|
| correlation bound dominates every tested coherent projection | PASS |
| coherent projection decays across the tested sprinkling-like shell range | PASS |
| normalized shell correlations broadly decay and explain the coherent projection | PASS |
| Gram conditioning is finite-`N` rough but stabilizes after `N=32` | PASS |
| support-mass bound is valid but much looser than correlation bound | PASS |

Twenty-second final receipt line:

`CHECKS PASSED: 5/5`

Twenty-third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_integrated_click_law_matrix.py
```

Twenty-third receipt summary:

| check | result |
|---|---|
| candidate action includes every currently needed gate | PASS |
| every non-open adversary has at least one assigned gate | PASS |
| exactly one adversary remains intentionally open | PASS |
| two-layer order is rejected by shell regularity before mark rescue | PASS |
| global mark products are not accepted as free projection credit | PASS |
| exact block labels pay linearly growing admissibility action | PASS |
| coherent waves are routed through correlation/field-sector control | PASS |
| linear-window cluster is not falsely declared solved by finite `P_8` data | PASS |

Twenty-third final receipt line:

`CHECKS PASSED: 8/8`

Twenty-fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_linear_window_polymer_budget.py
```

Twenty-fourth receipt summary:

| check | result |
|---|---|
| zero-row projection is enforced | PASS |
| truncated polymer budget is small in the tested linear window | PASS |
| same-pair term dominates the tested budget | PASS |
| cycle tail decreases after `r=2` in the tested range | PASS |
| mixing window `c` suppresses the budget monotonically | PASS |
| hardest tested case is the least-mixed `c=0.5` corner | PASS |

Twenty-fourth final receipt line:

`CHECKS PASSED: 6/6`

Twenty-fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p27_continuous_copula_envelope.py
```

Twenty-fifth receipt summary:

| check | result |
|---|---|
| continuous quadrature refinement is stable enough for envelope audit | PASS |
| scaled continuous energies are nearly `c^-2` | PASS |
| loose `K=0.075` guard bounds continuous `c^2 A_infty` | PASS |
| loose `K=0.075` guard bounds audited finite `A_N` values | PASS |
| `K/c^2` envelope makes same-pair budget decay like `O(1/N)` | PASS |

Twenty-fifth final receipt line:

`CHECKS PASSED: 5/5`

---

## 14. The 1-2-3 quotient campaign

The requested order of attack was:

1. prove quotient-level washout;
2. if that fails, find a stable rare-order residue;
3. if that fails, find a subtler unlabeled bracket identity.

Route 1 does not complete as an unconditional theorem. It completes as a sharp conditional theorem and exposes the exact missing lemma.

Let

$$
L_N(O)
=
\frac{dQ_N^O}{dP_N^O}(O)
$$

be the likelihood ratio after projecting to the unlabeled order sigma-field. Suppose the projected quotient can be expanded into centered hidden-pair factors `h_{e,N}` with `M_N` hidden sibling pairs, where

$$
M_N
=
\frac{N(w-1)}{2}.
$$

The desired local factor inequality is:

$$
\|h_{e,N}\|_{L^2(P_N^O)}
\le
\frac{K}{N}.
$$

The desired nonshared-cycle neutrality is that distinct non-interacting hidden-pair factors do not accumulate coherently after conditioning only on the unlabeled order:

$$
\sum_{e\ne f}
\mathbb{E}_{P_N^O}[h_{e,N}h_{f,N}]
=
O(1)
\quad
\text{or ideally } o(1).
$$

Then the diagonal part is forced down:

$$
\sum_e
\|h_{e,N}\|_2^2
\le
\frac{N(w-1)}{2}
\frac{K^2}{N^2}
=
\frac{K^2(w-1)}{2N}.
$$

The receipt checks this scaling at high precision. With `w=2`, `K=4`, and `N=10^12`, the diagonal term is

`8.0e-12`.

But the same receipt also shows why this is not yet a proof. If the local factor were only of size `K/sqrt(N)`, non-neutral cross terms could grow like

`3999999999992.0`

at `N=10^12`. Therefore the theorem is blocked exactly at:

> **[OPEN] Lemma M.** Prove that the projected hidden-pair quotient factor has `L^2` size `O(1/N)`, and that nonshared factors are neutral after conditioning only on the unlabeled order.

Route 2 is the rare-order fallback. The current finite facts remain:

| receipt | strongest resolved residue |
|---|---:|
| exact `P_8` largest positive linear contribution | `0.00478171696739` |
| `N=10` max half/one selected contribution | `0.0540733337402` |
| `N=12` max selected contribution | `0.0557631254196` |
| `N=12` max per-schedule Q/null aggregate ratio | `1.50457317073` |

These are not divergence certificates. They leave open the uniform selected-class theorem:

$$
\sup_N
\sum_{C\in\mathcal{S}_N}
\frac{q_N(C)^2}{p_N(C)}
<
\infty,
$$

or its negation by a stable selected family.

Route 3 is the bracket fallback. The marked bracket remains real:

$$
B(1)
=
0.0150545634920634921.
$$

But a random unrooted pair sees that bracket only with hidden-sibling probability

$$
\frac{w-1}{N-1}.
$$

So the random-pair projected bracket is

$$
\frac{w-1}{N-1}B(c)
=
O(N^{-1}).
$$

For `w=2`, `c=1`, and `N=10^12`, the receipt gives

`1.50545634920785466e-14`.

Thus the ordinary local bracket does not survive as a single-pair invariant. Any surviving unlabeled bracket must be an aggregate sparse-pair likelihood, a selected rare denominator, or a non-neutral cycle sum. This is narrower than "find a better feature"; it is the exact remaining mathematical enemy.

The preferred theorem path is therefore **not** marked coordinate-rank TV coupling; the marked bracket receipt rules that out at finite `c`. The theorem path is quotient-level: prove Lemma M, then bound the induced-order likelihood ratio. The preferred computational path is to make exact selected-denominator counting faster:

$$
P_N(C)
=
\frac{r(C)}{|\mathrm{Aut}(C)|\,N!},
$$

where `r(C)` is the number of realizer first-orders compatible with the selected class.

Until one of those is done, the honest status is:

> **The linear-window adversary looks washed out in the strongest finite exact-denominator receipts currently available, including the raised `N=12` singleton-overlap screen. Route 1 reduces the asymptotic theorem to Lemma M; routes 2 and 3 find no current residue except the same precise enemy: selected rare denominators or aggregate sparse-pair non-neutrality.**

---

## 15. Lemma M local-factor attack

The next pass attacks Lemma M directly at the smallest finite scale. Define `H_N^O` as a one-hidden-pair perturbation projected to unlabeled orders, and measure

$$
S_N(H\|P)-1
=
\mathbb{E}_{P_N^O}
\left[
\left(
\frac{dH_N^O}{dP_N^O}
\right)^2
\right]
-1.
$$

If the local factor has norm `O(1/N)`, this excess should behave like `O(N^{-2})`, modulo finite sampling noise.

The naive model is:

1. generate one hidden sibling pair from a shared parent;
2. jitter only that pair;
3. leave the other `N-2` records as unjittered ordinary records;
4. forget hidden labels and coordinates.

This model fails, and the failure is useful. At `N=8`, exact denominator, it gives:

| model | schedule | excess | guard ratio |
|---|---|---:|---:|
| naive one-pair | `linear_half` | `0.00477941036224365234` | `0.182949545463987185` |
| naive one-pair | `linear_one` | `0.129979622364044189` | `4.97544906772127638` |
| naive one-pair | `linear_two` | `0.723589074611663818` | `27.698038517196133` |

So the raw one-pair factor is not the right object. It changes the one-record density: only the hidden pair receives the wide jitter, so the order can see boundary/outlier structure. This is not the hidden-pair quotient after the density law has been matched.

The receipt therefore follows the opening immediately. In the marginal-matched Palm model:

1. every record has the same one-record coordinate marginal;
2. every record is jittered through the same window;
3. the only special feature of the hidden pair is shared parent center;
4. hidden labels and coordinates are forgotten.

At `N=8`, exact denominator, the same schedules become:

| model | schedule | excess | guard ratio |
|---|---|---:|---:|
| marginal-matched Palm | `linear_half` | `-0.00126832723617553711` | `-0.0485498992074370745` |
| marginal-matched Palm | `linear_one` | `-0.00499438047409057617` | `-0.191178318737239807` |
| marginal-matched Palm | `linear_two` | `0.00250573158264160156` | `0.0959161108492546014` |

The wide-jitter obstruction is reduced from

`0.723589074611663818`

to

`0.00250573158264160156`.

This does not prove Lemma M. It does something more precise: it says Lemma M must be stated **after marginal/density projection**. The raw hidden-pair factor is not small, because it includes an artificial density defect. The density-matched Palm factor is the right local object, and the finite exact-denominator receipt finds no visible obstruction for `N=5..8`.

The sharpened Lemma M is therefore:

> **[OPEN] Density-matched Lemma M.** Let `H_N^O` be the one-pair Palm perturbation with the same one-record coordinate marginal as `P_N`, projected to unlabeled orders. Prove
>
> $$
> \left\|
> \frac{dH_N^O}{dP_N^O}
> -1
> \right\|_{L^2(P_N^O)}
> =
> O(N^{-1}),
> $$
>
> then prove nonshared-cycle neutrality for many such density-matched factors.

If this refined lemma holds, the quotient washout theorem becomes plausible. If it fails, the failure should now be a real selected-class or Palm residue rather than a density artifact.

---

## 16. Rank-kernel projection

The next pass derives the density-matched one-pair Palm law directly on rank data. For one coordinate axis, let

$$
R
=
F_c(S+E),
\qquad
S\sim \mathrm{Uniform}[0,1],
\qquad
E\sim \mathrm{Uniform}[-c,c],
$$

where `F_c` is the marginal CDF of `S+E`. Then each single record has uniform rank marginal. Two hidden siblings share `S` but have independent jitter variables.

Let

$$
q_{\mathrm{axis}}(a,b)
$$

be the probability that the two ordered siblings have coordinate ranks `a,b` among `N` records. For a U-order permutation `pi`, the density-matched one-pair Palm law is:

$$
q(\pi)
=
\frac{1}{(N-2)!}
\sum_{a\ne b}
q_{\mathrm{axis}}(a,b)
q_{\mathrm{axis}}(\pi(a),\pi(b)).
$$

This is exact over the `N!` permutation support once the one-axis kernel is computed. The receipt computes `q_axis` by high-precision deterministic Gauss-Legendre quadrature, then enumerates all permutations for `N=5..8`.

The result corrects the previous intuition. Projection to unlabeled canonical orders is an `L^2` contraction, but it is not the main source of smallness. At `N=8`:

| `c` | labeled excess | unlabeled excess | projection ratio |
|---:|---:|---:|---:|
| `0.5` | `0.000886973248233214344` | `0.000873825414139208206` | `0.985176741102174549` |
| `1` | `0.0000183665034012862923` | `0.0000179909873062797365` | `0.979554295839443416` |
| `2` | `2.27189708239058282e-7` | `2.16336924919713937e-7` | `0.952230303901246248` |

So quotienting only mildly contracts the density-matched one-pair residue. The real smallness is the rank-copula falloff in `c`:

$$
8^2
\left(S_8^{O}(c=2)-1\right)
=
0.0000138455631948616919
$$

using the unlabeled excess above.

The refined theorem target is now:

1. prove a density-matched rank-copula bound for one hidden pair;
2. prove that the bound is strong enough in the linear-window regime;
3. prove nonshared-cycle neutrality when summing many such pair factors.

The important correction is:

> **[CONSTRAINED] Lemma M should not rely on the unlabeled quotient map erasing the one-pair Palm signal. It should prove that the density-matched rank copula is already small enough, and then prove that many small pair factors do not add coherently through nonshared cycles.**

---

## 17. Rank-copula bound

The next pass isolates the exact representation-theoretic mechanism behind the one-pair suppression.

Write the one-axis density-matched sibling rank kernel as

$$
q_{\mathrm{axis}}
=
u+\delta,
\qquad
u(a,b)
=
\frac{1}{N(N-1)}
\quad(a\ne b).
$$

The finite quadrature kernel is symmetrized and projected onto the exact zero-row space:

$$
\sum_{b\ne a}\delta(a,b)
=
0,
\qquad
\delta(a,b)
=
\delta(b,a),
\qquad
\delta(a,a)
=
0.
$$

Define the one-axis copula excess

$$
A_N(c)
=
N(N-1)
\sum_{a\ne b}
\delta(a,b)^2.
$$

After the zero-row projection, `delta` lies in the symmetric ordered-pair irreducible representation of dimension

$$
d_N
=
\frac{N(N-3)}{2}.
$$

Schur orthogonality then gives the finite target identity:

$$
S_N^{\mathrm{label}}(c)-1
=
\frac{A_N(c)^2}{d_N}.
$$

The receipt checks this identity by explicit enumeration of all permutations for `N<=8`. The maximum difference between the exact enumeration and `A_N(c)^2/d_N` is

`9.28633409537920361e-140`.

The tested scaling table is:

| `c` | max tested `A_N(c)`, `N<=24` | max tested `N^2(A_N(c)^2/d_N)` |
|---:|---:|---:|
| `0.5` | `0.214847062122` | `0.105506880234` |
| `1` | `0.0415842637487` | `0.00395257369491` |
| `2` | `0.0071521796807` | `0.000116922683852` |
| `4` | `0.0013733488712` | `4.31105627893e-6` |

This is the strongest progress in the Lemma M campaign so far. The quotient map is not the main suppressor. The main suppressor is:

$$
\text{bounded one-axis copula energy}
\quad+\quad
\text{representation dimension } d_N\sim \frac{N^2}{2}.
$$

Therefore:

> **[CONSTRAINED] A proof of a uniform analytic bound `A_N(c) <= C(c)`, preferably with decay in `c`, proves the one-pair local `L^2` factor bound. What remains after that is the many-pair problem: prove nonshared-cycle neutrality, or find the cycle family where many small pair factors add coherently.**

---

## 18. Nonshared-cycle neutrality

The next pass attacks the many-pair side directly in the labeled permutation model.

Let `delta` be the symmetric zero-row one-axis rank-copula residue, and define a localized one-axis factor for a fixed ordered domain edge `e=(a,b)`:

$$
g_e(\pi)
=
N(N-1)\delta(\pi(a),\pi(b)).
$$

For two disjoint domain edges `e,f`, the receipt computes

$$
\rho_2
=
\mathbb{E}[g_e g_f].
$$

Zero-row neutrality gives the exact finite formula

$$
\rho_2
=
\frac{2A_N(c)}{(N-2)(N-3)}.
$$

The receipt checks this formula numerically across all tested cases with maximum error

`5.86850596860070543e-142`.

For width `2`, there are `M=N/2` hidden pairs. The tested aggregate two-factor residue is

$$
\binom{M}{2}\rho_2^2.
$$

The worst tested value is

`0.00046336571365220063`

at `c=0.5`, `N=8`; it decreases with `N` and falls rapidly with `c`. The maxima by `c` are:

| `c` | max tested aggregate two-factor residue |
|---:|---:|
| `0.5` | `0.000463365713652` |
| `1` | `9.50914218922e-6` |
| `2` | `1.09420560536e-7` |
| `4` | `4.31257071717e-9` |

The receipt then measures the first nontrivial cycle-residue audit:

$$
\rho_3
=
\mathbb{E}[g_e g_f g_h],
$$

for three disjoint domain edges. This is not zero. The largest tested aggregate

$$
\binom{M}{3}\rho_3^2
$$

is

`0.0000300427813969838513`.

So the right conclusion is not exact cancellation. It is controlled cycle residue:

> **[CONSTRAINED] Nonshared two-factor terms are explicitly neutralized by the zero-row condition and have the closed form above. Three-factor terms reveal a small signed cycle residue. The remaining theorem is to bound all higher cycle residues uniformly and then transfer the labeled result through the unlabeled quotient or selected-class denominator.**

---

## 19. Higher-cycle residue scaling

The next follow-up asks whether the three-factor residue is the first sign of coherent growth. In the same labeled permutation model, the receipt computes disjoint `r`-factor moments

$$
\rho_r
=
\mathbb{E}
\left[
\prod_{i=1}^r g_{e_i}
\right]
$$

for `r=2,3,4,5`, using exact subset dynamic programming over disjoint ordered image pairs. The width-`2` aggregate is

$$
\binom{M}{r}\rho_r^2,
\qquad
M=N/2.
$$

For the hardest tested mixing value, `c=0.5`, the maxima over tested `N` are:

| `r` | max tested aggregate |
|---:|---:|
| `2` | `0.000462934624051` |
| `3` | `3.00612135294e-5` |
| `4` | `1.20293777188e-6` |
| `5` | `2.29770982292e-8` |

Across mixing values, the worst tested aggregate is:

| `c` | max tested aggregate |
|---:|---:|
| `0.5` | `0.000462934624051` |
| `1` | `9.49762298761e-6` |
| `2` | `1.10287964612e-7` |
| `4` | `2.02275645158e-9` |

The hostile reading is important. This does not prove that all higher cycles are harmless. It only says the tested higher cycles do not become a rare coherent order class. The residues are nonzero, but the finite evidence points to a summable cluster expansion rather than divergence.

The proof target is now:

$$
\sum_{r \geq 2}
\binom{M}{r}\rho_r^2
\leq
C(c)
$$

with decay in `c` if possible, and then the same quotient transfer required above.

> **[CONSTRAINED] Higher cycles survive the zero-row projection, but the tested physical aggregate residues decrease rapidly after the two-factor term. The next theorem cannot use zero-row neutrality alone; it must control the full matching/free-energy generating function or derive that control from the finite-dimensional record law.**

---

## 20. Zero-row-only cluster bound fails

The next hostile pass asks whether the apparent cluster expansion is a universal consequence of zero-row neutrality. It is not.

Let `D` be a symmetric zero-row ordered-pair matrix, normalized by

$$
\frac{1}{N(N-1)}
\sum_{i\neq j}D_{ij}^2
=
1.
$$

For disjoint image endpoints, define

$$
\rho_r(D)
=
\frac{1}{(N)_{2r}}
\sum_{\text{all endpoints distinct}}
\prod_{k=1}^r D_{a_k b_k}.
$$

The naive theorem would assert that `N^r |rho_r(D)|` stays uniformly controlled for fixed `r`, and therefore that the width-`2` aggregate

$$
\binom{N/2}{r}\rho_r(D)^2
$$

decays like `N^-r`.

The receipt tests the physical rank-copula against balanced block, Fourier, sparse signed-cycle, and projected random zero-row matrices. The balanced block defeats the zero-row-only theorem:

| diagnostic | value |
|---|---:|
| worst scaled residue `N^r |rho_r|` | `97332.8446777408458` |
| worst scaled aggregate `N^r binom(N/2,r)rho_r^2` | `94736.8265306122449` |
| worst family | balanced block, `N=10`, `r=5` |
| max scaled physical aggregate in the same audit | `35.9408634632` |

The important point is not that the block is physically plausible. It is that it passes the exact two-factor test. The receipt reports:

$$
\rho_2(D)
=
\frac{2}{(N-2)(N-3)}
$$

for every normalized hostile matrix, with maximum numerical formula error

`1.23007985368049721e-141`.

So two-factor neutrality can miss a high-order staged/fiber obstruction.

The spectral follow-up is also instructive but not final. The block obstruction has collapsed stable rank:

| matrix family | stable-rank diagnostic |
|---|---:|
| max block stable rank | `1.16666666666666667` |
| min projected-random stable rank | `2.30290346640011778` |
| max physical rank-copula stable rank | `1.3363795851915249` |

Thus spectral concentration is a symptom, not the final separator. The physical rank-copula can also have low stable rank without the same high-order matching explosion. The sharper object is the signed matching/free-energy generating function itself:

$$
\mathcal{Z}_N(D;z)
=
\sum_{r=0}^{N/2}
\binom{N/2}{r}
\rho_r(D)^2 z^r,
$$

or an equivalent finite-dimensional record law that controls all these coefficients at once.

> **[COUNTEREXAMPLE] Zero-row neutrality and bounded one-pair energy do not imply the cluster expansion. A balanced staged block is invisible to the two-factor formula but visible at high matching order. The click law therefore needs a full matching/free-energy regularity projection, or a projective finite-dimensional law strong enough to exclude macroscopic staged/fiber blocks.**

---

## 21. Matching/free-energy separator

The preceding counterexample makes the next object nearly forced. Under the `A(D)=1` normalization, the two-factor coefficient is universal. It cannot be the law.

Define

$$
q_r(D)
=
\binom{N/2}{r}\rho_r(D)^2
$$

and the normalized matching tail

$$
T_N(D)
=
\frac{\sum_{r\geq 3}q_r(D)}{q_2(D)}.
$$

The receipt tests physical rank-copula kernels, staged blocks, multiblocks, hierarchical blocks, Fourier kernels, sparse blocks, projected random kernels, and physical-plus-block mixtures. The finite separator is:

| diagnostic | value |
|---|---:|
| max physical `T_N` | `0.646530121406787645` |
| min staged-hostile `T_N` | `1.51120843688793914` |
| max balanced two-block `T_N` | `136.128075249853028` |
| max projected-random `T_N` | `0.330748636205892324` |
| max physical `log Z_N(D;N)` | `4.72408692993038315` |
| min staged-hostile `log Z_N(D;N)` | `6.61163097687816908` |

The full pressure used in the receipt is

$$
Z_N(D;z)
=
1+\sum_{r\geq 2}q_r(D)z^r.
$$

This is the first diagnostic in the campaign that has the right shape:

1. `q_2` is universal and therefore too weak.
2. stable rank notices the block but is not a sufficient separator.
3. the matching tail sees high-order staged coherence.
4. random projected matrices are not automatically rejected like staged blocks.

The tuned-mixture scan at `N=12` adds the necessary hostile nuance. Mixing physical `c=0.5` with a normalized balanced block gives:

| block admixture `lambda` | `T_N` | `log Z_N(D;N)` |
|---:|---:|---:|
| `0` | `0.363401136241543661` | `4.72408692993038315` |
| `0.05` | `0.437766917217452852` | `6.25635496966915188` |
| `0.10` | `0.558188112429318495` | `7.45185370680351518` |
| `0.125` | `0.644540158106801461` | `7.94193848420931503` |
| `0.15` | `0.753556121413068294` | `8.37639053847073873` |
| `0.20` | `1.05551044298534026` | `9.11386053861675075` |
| `0.25` | `1.49430873064617951` | `9.71791311329429086` |
| `0.50` | `6.38451075754274464` | `11.6194631377227498` |

The first tested admixture above the global physical `T_N` envelope is `lambda=0.15`. Therefore this is not an infinitesimal contamination detector. It is a macroscopic staged/fiber regularity diagnostic.

The candidate record-law statement should now be something like:

> A density-matched local record kernel is admissible only if its finite matching pressure remains subcritical across projective scales.

Equivalently, the projective finite-dimensional record law must imply a bound on all matching coefficients, not merely on `A(D)` or on the two-factor projection.

> **[CONSTRAINED] The strongest current finite candidate for the missing regularity projection is matching/free-energy subcriticality. It rejects tested macroscopic staged blocks and keeps tested physical rank-copula kernels, but it deliberately does not claim to detect arbitrarily small staged admixtures.**

---

## 22. Pressure-density scaling and tuned adversaries

The next pass tries to turn the finite separator into a theorem target. It also tries to break it.

The raw matching tail

$$
T_N(D)
=
\frac{\sum_{r\geq 3}q_r(D)}{q_2(D)}
$$

is useful, but it is not the final law. The stronger finite diagnostic is the pressure density

$$
p_N(D)
=
\frac{1}{N}\log Z_N(D;N),
\qquad
Z_N(D;z)
=
1+\sum_{r\geq 2}q_r(D)z^r.
$$

The receipt extends the physical rank-copula computation to `N=8,10,12,14` and `c=0.5,1,2,4`. For `c=0.5`, the matching tail decreases over the tested `N` values:

| `N` | `T_N` | `p_N` |
|---:|---:|---:|
| `8` | `0.649991484542364941` | `0.407344434269233292` |
| `10` | `0.481323269700065294` | `0.38872495950443513` |
| `12` | `0.364233481190487501` | `0.393770778440038473` |
| `14` | `0.285048114137706177` | `0.409301776101656529` |

Across the full tested physical grid:

| diagnostic | value |
|---|---:|
| max physical `T_N` | `2.21597735974522257` |
| max physical `T_N` excluding `N=8,c=4` | `0.649991484542364941` |
| max physical `p_N` | `0.67492564369670709` |

The high tail at `N=8,c=4` is the warning: tail alone can over-penalize a finite wide-jitter physical corner.

The tuned adversary audit then tests fixed blocks, hierarchical blocks, and Fourier kernels. Tail alone fails:

| diagnostic | value |
|---|---:|
| stealthiest fixed-block tail | `0.270705179246934039` |
| physical max tail | `2.21597735974522257` |

The stealthy case is `N=14`, four blocks. Its tail is low, but its pressure density is not:

| diagnostic | value |
|---|---:|
| least fixed-block `p_N` | `0.74507778509175585` |
| max physical `p_N` | `0.67492564369670709` |

So the current separator is not `T_N`. It is `p_N`.

The contamination thresholds support the same conclusion. Mixing physical `c=0.5` with a normalized two-block adversary, the first tested block admixture whose pressure density exceeds the physical envelope is:

| `N` | first pressure-density crossing |
|---:|---:|
| `8` | `0.25` |
| `10` | `0.20` |
| `12` | `0.15` |
| `14` | `0.125` |

This finite trend suggests, but does not prove, that any fixed macroscopic staged component may eventually become pressure-visible as `N` grows.

One new ambiguity remains. Fourier/coherent-wave kernels can violate both pressure diagnostics:

| diagnostic | value |
|---|---:|
| max structured Fourier tail | `7.8246` |
| max structured Fourier `p_N` | `0.838063123922422355` |

This is not automatically bad. It may mean coherent wave structure is a legitimate matterlike excitation rather than a non-manifold staged block. Or it may mean pressure density still needs a locality/mark/field-context qualifier.

The sharpened theorem target is therefore:

> Prove that the physical continuum rank-copula kernel has uniformly subcritical pressure density, while fixed macroscopic staged/fiber decompositions have pressure density bounded away above the physical envelope.

The open fork is:

> Decide whether Fourier/coherent-wave kernels are admissible records carrying field structure, or forbidden non-manifold staging.

> **[CONSTRAINED] Matching tail found the right family of diagnostics, but pressure density is the stronger current candidate. Tail-only separation is false in the finite hostile audit. Pressure-density subcriticality survives the tested physical kernels and fixed staged adversaries, but coherent Fourier kernels remain an unresolved boundary case.**

---

## 23. Fourier/coherent-wave boundary

The next receipt follows the unresolved boundary case rather than leaving it as a footnote.

It tests physical density-matched rank-copula kernels, fixed staged blocks, pure Fourier difference kernels, Fourier bands, and deterministic random Fourier spectra. The matching coefficients are computed by a symmetric matching-polynomial recursion:

$$
\rho_r
=
\frac{r!2^rS_r}{(N)_{2r}},
$$

where `S_r` is the weighted undirected matching sum of size `r`.

The finite pressure comparison is:

| diagnostic | value |
|---|---:|
| max physical `p_N`, `c=0.5`, `N<=14` | `0.409301776101656529` |
| max pure-Fourier `p_N`, `N<=16` | `0.838063123922422355` |
| min Fourier-band `p_N`, `N<=16` | `0.212272862006224522` |
| min staged-block `p_N`, `N<=16` | `0.74507778509175585` |
| max random-Fourier-band `p_N`, `N<=16` | `0.940755884474008723` |
| min random-Fourier-band `p_N`, `N<=16` | `0.439988226963201067` |

The first conclusion is that pure coherent modes are not a finite `N=8` artifact. The `cos1` pressure sequence is:

| `N` | `p_N(cos1)` |
|---:|---:|
| `8` | `0.4899696342` |
| `10` | `0.517823610185` |
| `12` | `0.553097774688` |
| `14` | `0.589384576435` |
| `16` | `0.624767593028` |

The second conclusion is that not all Fourier structure behaves like staging. A three-mode Fourier band has:

| `N` | `p_N(band3)` |
|---:|---:|
| `8` | `1.03222175102` |
| `10` | `0.458110747701` |
| `12` | `0.381913110359` |
| `14` | `0.212272862006` |
| `16` | `0.384746644626` |

Spectral spreading is visible:

| diagnostic | value |
|---|---:|
| min pure-Fourier effective rank | `3.80149827293340821` |
| max Fourier-band effective rank | `13.8316186722259165` |
| max random-Fourier-band effective rank | `8.53736805052884476` |

But spectral spreading is not sufficient. Random Fourier spectra straddle the staged-block pressure floor: some fall below it, while others exceed it. Therefore the candidate law should not say either:

1. all coherent wave kernels are forbidden;
2. all coherent wave kernels are admissible.

The better interpretation is sectoral:

> Geometry kernels must remain pressure-subcritical. Coherent wave structure can be admissible only when carried by an explicit matter/mark sector with its own field-energy or spectral-spread bookkeeping.

This clarifies the click-law search. The record law probably needs at least two coupled pieces:

1. a geometry pressure law suppressing hidden staged/fiber order;
2. a marked matter law allowing coherent excitations without letting them masquerade as geometry.

> **[OPEN] Fourier/coherent modes cannot be classified by pressure density alone. Pure modes look too pressure-heavy to be geometry, but spread Fourier bands can be low-pressure, and random spectra straddle the staged-block floor. The next law must separate geometry pressure from matter/mark field energy.**

---

## 24. Sectoral pressure with marks

The next receipt tests the obvious sectoral repair:

> apply geometry pressure only to the residual after projecting out structure carried by explicit matter marks.

Given a symmetric zero-row kernel `D` and node marks `F`, the receipt forms the mark-generated pair-kernel span

$$
f_a(i)f_b(j)+f_b(i)f_a(j),
$$

projects `D` onto that span in off-diagonal Frobenius inner product, and evaluates geometry pressure on

$$
D_{\mathrm{geom}}
=
D-\Pi_FD.
$$

The first result is positive. A pure `cos1` geometry-only kernel is pressure-heavy, but explicit `cos1/sin1` marks erase its geometry residual:

| `N` | raw `p_N(cos1)` | residual `p_N` with correct marks |
|---:|---:|---:|
| `8` | `0.4899696342` | `0` |
| `10` | `0.517823610185` | `0` |
| `12` | `0.553097774688` | `0` |
| `14` | `0.589384576435` | `0` |
| `16` | `0.624767593028` | `0` |

Wrong marks do not erase the wrong frequency:

| `N` | residual `p_N(cos2)` with `cos1/sin1` marks |
|---:|---:|
| `8` | `0.77982162025` |
| `10` | `0.53050603326` |
| `12` | `0.726833283656` |
| `14` | `0.592942000814` |
| `16` | `0.75219588773` |

So explicit marks can distinguish “wave carried by a field” from “wave hidden in geometry.”

But the hostile checks expose two constraints.

First, mixed physical-plus-wave kernels lose mark-carried amplitude, but their normalized residual pressure shape need not decrease:

| `N` | raw mixed `p_N` | residual `p_N` | raw `A` | residual `A` |
|---:|---:|---:|---:|---:|
| `8` | `0.38701543369` | `0.583903861476` | `2.82559938863` | `0.534899740879` |
| `10` | `0.397614558913` | `0.512681473182` | `2.83583736388` | `0.613449269522` |
| `12` | `0.422427223598` | `0.123796527869` | `2.83929827264` | `0.653338280655` |
| `14` | `0.452250926804` | `0.444957791367` | `2.83977297921` | `0.677510991172` |

The projection removes amplitude, but pressure after `A=1` normalization can rise. Therefore the sectoral law must track both residual pressure shape and residual amplitude.

Second, smooth marks can partially launder block geometry because a step function has low-frequency components:

| `N` | block residual `p_N` after `cos1/sin1` marks |
|---:|---:|
| `8` | `0.679454745657` |
| `10` | `0.33355067279` |
| `12` | `0.841603896572` |
| `14` | `0.857332184975` |
| `16` | `0.828309809045` |

This does not mean blocks are safe. A block can be marked away exactly only by a block mark, whose scaled field energy grows:

| `N` | low-frequency Fourier mark energy | block mark energy |
|---:|---:|---:|
| `8` | `74.9806640162` | `64.0` |
| `10` | `76.39320225` | `80.0` |
| `12` | `77.1693674202` | `96.0` |
| `14` | `77.6404075645` | `112.0` |
| `16` | `77.9473587084` | `128.0` |

The lesson is sharper than “add marks.” The law needs a coupled budget:

$$
\text{geometry residual pressure}
\quad+\quad
\text{geometry residual amplitude}
\quad+\quad
\text{mark field energy}
\quad+\quad
\text{anti-laundering condition}.
$$

The anti-laundering condition is the new unresolved piece: marks cannot be arbitrary labels that define the geometry after the fact.

> **[CONSTRAINED] Explicit matter marks can rescue genuine Fourier waves, but naive mark projection is insufficient. The sectoral click law must charge mark energy, retain residual amplitude, and prevent marks from silently becoming hidden geometry labels.**

---

## 25. Anti-laundering mark admissibility

The previous section leaves a precise enemy:

> marks that are chosen after seeing the geometry and then used to explain away the geometry.

The next receipt tests whether this can be reduced to a finite action/complexity condition.

For a centered, orthonormalized mark family `F`, define the scaled rank-circle Dirichlet action

$$
\mathcal E_N(F)
=
\sum_a
N^2
\sum_i
\left(
\tilde f_a(i+1)-\tilde f_a(i)
\right)^2.
$$

This is not proposed as the final field action. It is a hostile proxy for the minimal principle:

> projection credit must not be free; the mark sector must pay its own action/complexity.

The receipt also tracks the block-label Fourier tail and the pair-kernel projection fraction

$$
\mathcal P_N(D,F)
=
\frac{\lVert \Pi_FD\rVert^2}{\lVert D\rVert^2}.
$$

The first table compares a cheap low-frequency field, an exact block label, and a smooth steep blocklike field

$$
f_i
=
\tanh
\left(
8\sin \frac{2\pi i}{N}
\right).
$$

| `N` | `E(cos1,sin1)` | `E(exact block)` | `E(soft beta=8)` | `align(soft,block)` | `tail4(block)` | `tail4(soft)` |
|---:|---:|---:|---:|---:|---:|---:|
| `16` | `77.947358708442` | `128.0` | `72.688072686005` | `0.87499659005154` | `0.077688400689633` | `0.016972251227288` |
| `32` | `78.703491468368` | `256.0` | `118.01425697886` | `0.93672050925561` | `0.094108086369249` | `0.040217867143492` |
| `64` | `78.893438202726` | `512.0` | `139.55878320672` | `0.96130057185249` | `0.09806202584692` | `0.043117582397552` |
| `128` | `78.940982137822` | `1024.0` | `143.86933230986` | `0.96776086222628` | `0.099041539433934` | `0.043130754804676` |

This is the important hostile opening. Exact block labels pay `O(N)` exact-step action, but smooth steep marks can align strongly with a block while paying a large finite action. Therefore the law cannot say merely:

> reject all marks aligned with staged geometry.

That would wrongly reject possible domain-wall-like matter fields. But the law also cannot say:

> any marked projection is allowed.

That would make the geometry test vacuous.

The Fourier-band laundering ladder at `N=64` shows the same tradeoff:

| `K` | linear block fraction | pair-kernel lower proxy | mark energy | remaining Fourier tail |
|---:|---:|---:|---:|---:|
| `1` | `0.81122082467168` | `0.65807922638101` | `78.893438202726` | `0.18877917532832` |
| `2` | `0.81122082467168` | `0.65807922638101` | `393.7074040762` | `0.18877917532832` |
| `4` | `0.90193797415308` | `0.81349210921936` | `2346.3546827748` | `0.09806202584692` |
| `8` | `0.95222865613155` | `0.90673941355809` | `15559.917788871` | `0.047771343868452` |
| `16` | `0.98013741254797` | `0.96066934747624` | `103584.0092161` | `0.019862587452025` |

Fourier modes can approximate a block. But high projection requires growing bandwidth/action. This turns the danger into a cost, not a binary permission.

The exact small-`N` pair-kernel projection confirms that this is not only a one-point mark-alignment artifact:

| `N` | marks | projected block-pair fraction | mark energy |
|---:|---|---:|---:|
| `16` | `fourier K=1` | `0.68129571344567` | `77.947358708442` |
| `16` | `fourier K=4` | `0.86116455110631` | `2034.0021800316` |
| `16` | `fourier K=6` | `0.95382999624647` | `5197.9473587084` |
| `16` | `soft beta=8` | `0.75836559202295` | `72.688072686005` |
| `16` | `exact block` | `1.0` | `128.0` |
| `24` | `fourier K=1` | `0.66757128850739` | `78.506896229987` |
| `24` | `fourier K=4` | `0.83177357173347` | `2214.0103420568` |
| `24` | `fourier K=8` | `0.94591219888766` | `12582.010342057` |
| `24` | `soft beta=8` | `0.83673156305711` | `99.510336293707` |
| `24` | `exact block` | `1.0` | `192.0` |

This gives the next form of the law:

$$
\mathcal A_N(D,F)
=
\Phi_{\mathrm{geom}}
\left(
D-\Pi_FD
\right)
+
\lambda\mathcal E_N(F)
+
\mu\mathcal C_N(F)
+
\mathcal I_{\mathrm{adm}}(F).
$$

Here:

1. `D` is the geometry kernel or interval-bracket residue.
2. `F` is the explicit mark/matter sector.
3. `Phi_geom` contains residual pressure and residual amplitude.
4. `E_N` charges field action.
5. `C_N` charges spectral/description complexity not captured by a simple Dirichlet term.
6. `I_adm` is the anti-laundering term: marks must be generated by a projective field law before geometry projection, not fitted afterward to define hidden fibers.

The hard part has moved. It is no longer enough to find an order statistic that rejects every hidden block. The record law must specify a joint measure over geometry and marks such that:

$$
\text{genuine fields are paid-for excitations,}
\qquad
\text{post-hoc hidden labels are not admissible explanations.}
$$

The exact block mark demonstrates why `I_adm` is necessary:

$$
\mathcal P_N(D_{\mathrm{block}},F_{\mathrm{block}})
=
1.
$$

If arbitrary marks are allowed after the fact, any staged geometry can carry its own label and become admissible. That is not a field sector; it is hidden geometry renamed as matter.

The smooth steep mark demonstrates the opposite danger. Some high-alignment marks may be legitimate physical fields. They should not be banned by alignment alone; they should be charged by the same projective finite-dimensional mark law that generated them.

> **[CONSTRAINED] The anti-laundering condition must be a joint projective field-law condition, not a scalar penalty. Marks may rescue coherent matterlike structure only when they are present as paid-for records before projection. Free post-hoc marks trivialize the geometry law.**

---

## 26. Projective tight-action field gate

The previous section identified the correct qualitative obstruction. The next receipt tests the simplest projective version:

> admissible marks are finite-action projective field records, not arbitrary finite-`N` labels.

For a centered mark `f` on the rank circle, define the scale-invariant Rayleigh action

$$
R_N(f)
=
\frac{
N^2
\sum_i
\left(
f_{i+1}-f_i
\right)^2
}{
\sum_i f_i^2
}.
$$

This is the one-feature version of the mark action used above. Its purpose is not to assert the final matter action. Its purpose is to test the right admissibility shape:

$$
\sup_N R_N(f_N)<\infty
$$

for a projectively compatible family of marks.

The finite refinement ladder is:

| `N` | `R(cos1)` | `R(exact block)` | `R(soft beta=8)` | `align(soft8, block)` |
|---:|---:|---:|---:|---:|
| `16` | `38.973679354221` | `128.0` | `72.688072686005` | `0.87499659005154` |
| `32` | `39.351745734184` | `256.0` | `118.01425697886` | `0.93672050925561` |
| `64` | `39.446719101363` | `512.0` | `139.55878320672` | `0.96130057185249` |
| `128` | `39.470491068911` | `1024.0` | `143.86933230986` | `0.96776086222628` |
| `256` | `39.47643585112` | `2048.0` | `144.97278203537` | `0.96934543190676` |
| `512` | `39.477922158587` | `4096.0` | `145.25246720385` | `0.9697397839118` |

Three regimes separate.

First, `cos1` tends to `4 pi^2`, as a genuine low-frequency field should.

Second, the exact block label has

$$
R_N(F_{\mathrm{block}})
=
8N
$$

in this normalization. It is therefore not a projective finite-action field.

Third, the smooth steep profile

$$
f_i
=
\tanh
\left(
8\sin\frac{2\pi i}{N}
\right)
$$

has bounded action and high but incomplete block alignment. This is exactly the nuance needed: smooth domain-wall-like fields should not be banned, but they also cannot erase a sharp hidden partition for free.

At fixed `N=512`, increasing steepness gives the tradeoff:

| `beta` | `R(soft beta)` | alignment with block | defect | `R * defect` |
|---:|---:|---:|---:|---:|
| `1` | `40.911696010547` | `0.84522417532964` | `0.15477582467036` | `6.3321414886953` |
| `2` | `49.742427989507` | `0.89342500042875` | `0.10657499957125` | `5.3012992416547` |
| `4` | `79.3546914054` | `0.94117165553758` | `0.058828344462424` | `4.6683051207062` |
| `8` | `145.25246720385` | `0.9697397839118` | `0.0302602160882` | `4.3953710449326` |
| `16` | `278.31891999267` | `0.98452043000191` | `0.015479569998092` | `4.3082572038198` |
| `32` | `541.42376348103` | `0.99183504176123` | `0.0081649582387725` | `4.4207024183016` |
| `64` | `1040.0643744003` | `0.9951183009625` | `0.0048816990375042` | `5.0772812554526` |

The trend is the key point: to approach exact block alignment, the mark spends increasing action. Bounded action keeps a nonzero defect.

The Fourier approximation ladder at `N=128` gives the same message in spectral form:

| `K` | block projection fraction | remaining tail | total mark action |
|---:|---:|---:|---:|
| `1` | `0.81073224916639` | `0.18926775083361` | `78.940982137822` |
| `2` | `0.81073224916639` | `0.18926775083361` | `394.51473494873` |
| `4` | `0.90095846056607` | `0.099041539433934` | `2363.0988413907` |
| `8` | `0.95025045100038` | `0.049749548999623` | `15968.687890993` |
| `16` | `0.97601812265389` | `0.023981877346111` | `114313.01408188` |
| `32` | `0.99005680520076` | `0.0099431947992428` | `795099.66447957` |

Thus Fourier approximation can launder a block only by increasing bandwidth and action.

The theorem target is now clear. Let `F_N` be a compatible family of centered marks on rank circles, and suppose

$$
\sup_N R_N(F_N)<\infty.
$$

Then a subsequential continuum limit exists in the finite-action field class. In one spatial rank dimension, the standard compactness intuition is:

> bounded `H^1` action prevents convergence to a discontinuous step.

Therefore a sharp hidden block partition cannot be represented by a projective finite-action mark family. To launder the block, either the mark action diverges or the mark law must explicitly contain a domain-wall sector with its own finite surface action and prior weight. In both cases the mark is paid for; it is not a free hidden label.

This turns the anti-laundering term into a candidate gate:

$$
\mathcal I_{\mathrm{adm}}(F)
=
\begin{cases}
0,
&
F \text{ belongs to a pre-geometric projective tight-action mark law},
\\
+\infty,
&
F \text{ is chosen post hoc or has divergent refinement action}.
\end{cases}
$$

The full action candidate becomes:

$$
\mathcal A_N(D,F)
=
\Phi_{\mathrm{geom}}
\left(
D-\Pi_FD
\right)
+
\lambda R_N(F)
+
\mu\mathcal C_N(F)
+
\mathcal I_{\mathrm{adm}}(F),
$$

with `C_N` reserved for bandwidth, description length, or domain-wall-sector bookkeeping not captured by the simple Rayleigh action.

> **[CONSTRAINED] The mark sector now has a plausible mathematical spine: projection credit is legal only for projectively admissible finite-action marks. This rejects exact hidden partition labels by refinement divergence while allowing genuine smooth/coherent fields as paid-for excitations. The remaining hard problem is to specify the actual projective mark law and couple it to the order law without post-hoc fitting.**

---

## 27. Local mark-to-geometry coupling gate

The projective finite-action gate is necessary, but the next hostile review finds that it is not sufficient.

Suppose a legitimate mark `f` is allowed to subtract the global pair product

$$
f(i)f(j)
$$

from the geometry kernel. Then a blocklike mark can erase a blocklike geometry kernel, even if the mark itself is treated as a domain-wall field. That is too permissive. Physical marks should not automatically receive arbitrary global pair-product projection credit. Their geometric coupling should be local or separately paid for as an explicitly nonlocal interaction.

The receipt tests this using the same zero-row pair-kernel geometry space. For a field `f`, define a local stress proxy

$$
s_i
=
N^2
\left(
f_{i+1}-f_i
\right)^2.
$$

Then compare:

1. the forbidden global product `f(i)f(j)`;
2. endpoint-additive stress `s_i+s_j`;
3. local wall-stress products built from thickened stress support.

The finite results are:

| `N` | block global product | block additive stress | max local wall-stress product | `N^2 local` | cos global | cos local stress | `N^2 cos local` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `32` | `1.0` | `0.0` | `0.002020474137931` | `2.0689655172414` | `1.0` | `0.0023391356893628` | `2.3952749459075` |
| `64` | `1.0` | `0.0` | `0.00049628586065574` | `2.0327868852459` | `1.0` | `0.00053319000268745` | `2.1839462510078` |
| `128` | `1.0` | `0.0` | `0.000123046875` | `2.016` | `1.0` | `0.00012749407114625` | `2.0888628616601` |
| `256` | `1.0` | `0.0` | `0.000030638200963439` | `2.0079051383399` | `1.0` | `0.000031184219827142` | `2.0436890305916` |

This table is the cleanest mark-sector correction so far.

The global product projection erases the block exactly. But endpoint-additive local stress has no zero-row geometry projection at all, and local wall-stress pair products capture only

$$
O(N^{-2})
$$

of the global block geometry.

The wall-stress radius ladder confirms that this is not a radius artifact:

| `N` | radius | projection fraction |
|---:|---:|---:|
| `32` | `0` | `0.00202047413793103448` |
| `32` | `1` | `0.00121875` |
| `32` | `2` | `0.00113673941798941799` |
| `32` | `4` | `0.00111354638009049774` |
| `64` | `0` | `0.000496285860655737705` |
| `64` | `1` | `0.000298108552631578947` |
| `64` | `2` | `0.00027638561320754717` |
| `64` | `4` | `0.000264246323529411765` |
| `64` | `8` | `0.000260212578369905956` |
| `128` | `0` | `0.000123046875` |
| `128` | `1` | `0.0000738474948347107438` |
| `128` | `2` | `0.0000683964713912630579` |
| `128` | `4` | `0.0000652183536832164058` |
| `128` | `8` | `0.0000635608860785272076` |
| `128` | `16` | `0.0000629901284678436318` |
| `256` | `0` | `0.0000306382009634387352` |
| `256` | `1` | `0.0000183840832078313253` |
| `256` | `2` | `0.0000170234109268707483` |
| `256` | `4` | `0.0000162245352056962025` |
| `256` | `8` | `0.0000157923131555944056` |
| `256` | `16` | `0.0000155755160637973138` |

So the correct marked-sector statement is now two-gated:

$$
\text{mark projection credit}
\quad\Longrightarrow\quad
\begin{cases}
\text{projective mark admissibility},\\
\text{local/stress-type coupling admissibility}.
\end{cases}
$$

The previous global projection formula

$$
D-\Pi_FD
$$

was too generous when `Pi_F` meant the full span of all products `f_a(i)f_b(j)`. The corrected version is:

$$
D_{\mathrm{geom}}
=
D-\Pi_{\mathcal L(F)}D,
$$

where `L(F)` is not the whole algebra of mark pair products. It is the explicitly allowed local response family of the mark law. If a theory wants a nonlocal mark-mediated pair interaction, that interaction must be named as a separate sector and assigned its own projective action.

The action candidate becomes:

$$
\mathcal A_N(D,F)
=
\Phi_{\mathrm{geom}}
\left(
D-\Pi_{\mathcal L(F)}D
\right)
+
\lambda R_N(F)
+
\mu\mathcal C_N(F)
+
\nu\mathcal N_N(F,D)
+
\mathcal I_{\mathrm{adm}}(F,\mathcal L).
$$

Here `N_N(F,D)` is the charge for explicitly nonlocal mark-geometry couplings. The default local field sector has `N_N=0` but also has too little projection power to launder a global block.

This resolves the domain-wall loophole in the finite model:

1. a domain wall mark may be a legitimate field;
2. its local stress does not erase global staged geometry;
3. erasing global staged geometry requires a nonlocal product coupling;
4. that nonlocal coupling is no longer free.

> **[CONSTRAINED] The marked sector needs two gates: projective finite-action marks and local coupling. This preserves legitimate fields while blocking the move "choose a mark, take all pair products, subtract the bad geometry." The next target is to define the allowed local response family `L(F)` intrinsically for records, not from external rank coordinates.**

---

## 28. Order-intrinsic shell-local response

The previous local-coupling test still used an external rank circle to define neighbor stress. That is not acceptable as the final record law. The next receipt replaces it with an order-intrinsic local response family.

For records `x<y`, let

$$
I(x,y)
=
\{z:x<z<y\}.
$$

A pair is shell-local at shell `k` when

$$
|I(x,y)|=k.
$$

For a mark `f`, the tested local response basis is

$$
\mathbf 1_{\{x<y,\ |I(x,y)|=k\}}
\left(
f(x)-f(y)
\right)^2,
\qquad
k=0,\ldots,4,
$$

zero-row projected into the same pair-kernel geometry space. This candidate `L(F)` uses only:

1. the order relation;
2. interval cardinalities;
3. mark values.

It does not use external rank adjacency.

The first test uses seeded 1+1 sprinkling-like permutation orders. The table reports the mean over three seeded orders at each `N`:

| `N` | mean local shell count | local shell fraction | comparable fraction | block projection mean | block projection max | cos projection mean | local self min |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `32` | `162.0` | `0.32661290322581` | `0.42002688172043` | `0.15819647525228` | `0.18329749510107` | `0.11960460565215` | `1.0` |
| `64` | `546.66666666667` | `0.27116402116402` | `0.51041666666667` | `0.10823834150824` | `0.11209358076806` | `0.08601368524996` | `1.0` |
| `96` | `939.33333333333` | `0.20599415204678` | `0.43808479532164` | `0.063012102107648` | `0.064368334513713` | `0.054029150310253` | `1.0` |
| `128` | `1444.6666666667` | `0.17773950131234` | `0.50844816272966` | `0.050665092739786` | `0.053934243941375` | `0.038779869786534` | `1.0` |
| `160` | `1953.3333333333` | `0.15356394129979` | `0.49344863731656` | `0.039121491735102` | `0.040513088583765` | `0.030084682034009` | `1.0` |
| `192` | `2564.6666666667` | `0.13987056428156` | `0.50730802792321` | `0.034654674325865` | `0.035151730506251` | `0.025460854418404` | `1.0` |

This is a useful finite result:

1. shell-local marked responses project to themselves;
2. projection of dense global block products decreases over the tested range;
3. projection of coherent cosine products also decreases;
4. the construction is order-intrinsic.

But the hostile review finds the exact extra condition needed. In a complete two-layer order, every cross-layer pair is a link:

$$
|I(x,y)|=0.
$$

So shell-locality becomes globally dense. The two-layer audit gives:

| `N` | local shell count | local shell fraction | comparable fraction | block projection |
|---:|---:|---:|---:|---:|
| `32` | `256` | `0.51612903225806` | `0.51612903225806` | `1.0` |
| `64` | `1024` | `0.50793650793651` | `0.50793650793651` | `1.0` |
| `128` | `4096` | `0.50393700787402` | `0.50393700787402` | `1.0` |
| `192` | `9216` | `0.50261780104712` | `0.50261780104712` | `1.0` |

This is not a failure of order-intrinsic locality. It is the missing companion law:

> shell-local response is admissible only on orders whose shell-density and interval-profile are manifoldlike.

Otherwise a non-manifold order can make “local” mean half of all pairs.

The corrected definition of the allowed mark-response family is therefore:

$$
\mathcal L(F;O)
=
\operatorname{span}
\left\{
\mathbf 1_{\{x<y,\ |I(x,y)|=k\}}
\Psi_k(F;x,y)
:
k\le k_{\max}
\right\},
$$

subject to a shell-density gate

$$
\mathcal S_{k_{\max}}(O)
=
\frac{
\#\{x<y: |I(x,y)|\le k_{\max}\}
}{
\binom{N}{2}
}
$$

matching the calibrated sprinkling envelope. The two-layer order fails this gate immediately.

This folds back into the geometry law. The record action cannot be merely:

$$
\Phi_{\mathrm{geom}}
\left(
D-\Pi_{\mathcal L(F;O)}D
\right).
$$

It must include the intrinsic locality regularizer:

$$
\mathcal A_N(D,F,O)
=
\Phi_{\mathrm{geom}}
\left(
D-\Pi_{\mathcal L(F;O)}D
\right)
+
\lambda R_N(F)
+
\eta\Phi_{\mathrm{shell}}
(O)
+
\mathcal I_{\mathrm{adm}}(F,\mathcal L,O).
$$

Here `Phi_shell` is not optional. It prevents layered/KR-like orders from turning link-locality into a dense global coupling.

The present section also clarifies why the earlier interval-profile work and the mark-sector work are not separate tracks. They are now coupled:

1. interval shells define intrinsic local mark response;
2. interval shell density decides whether that locality is physically local or globally staged;
3. marks cannot rescue geometry unless both tests pass.

> **[CONSTRAINED] The allowed local response family can be made order-intrinsic by interval shells, but only together with a calibrated shell-density/interval-profile law. This closes the rank-coordinate loophole and exposes the next theorem target: prove that sprinkling-like shell profiles make `Pi_{L(F;O)}` too sparse to launder dense staged geometry, while dense-layer orders fail `Phi_shell` before marks are considered.**

---

## 29. Shell-local projection bound

The previous section gives an order-intrinsic candidate for `L(F;O)`. This section proves the first small deterministic lemma behind it.

Let `H_N` be the zero-row pair-kernel space with inner product

$$
\langle A,B\rangle
=
2\sum_{i<j}A_{ij}B_{ij}.
$$

Let `P_0` be zero-row projection. Let `B in H_N` be a geometry residue, and let `h_a` be raw shell-local marked response vectors. Define

$$
v_a
=
P_0h_a,
\qquad
L
=
\operatorname{span}\{v_a\}.
$$

For each nonzero `h_a`, define the zero-row efficiency

$$
\epsilon_a
=
\frac{\lVert P_0h_a\rVert^2}{\lVert h_a\rVert^2},
$$

and the target mass inside the raw support

$$
m_a(B)
=
\frac{
\lVert B\mathbf 1_{\operatorname{supp}h_a}\rVert^2
}{
\lVert B\rVert^2
}.
$$

Let `C` be the normalized Gram matrix of the nonzero `v_a`:

$$
C_{ab}
=
\frac{\langle v_a,v_b\rangle}
{\lVert v_a\rVert \lVert v_b\rVert}.
$$

Then:

$$
\frac{\lVert \Pi_LB\rVert^2}{\lVert B\rVert^2}
\le
\lambda_{\min}(C)^{-1}
\sum_a
\frac{m_a(B)}{\epsilon_a}.
$$

This is the promised small theorem. The proof is short. Since `B` is zero-row,

$$
\langle B,v_a\rangle
=
\langle B,P_0h_a\rangle
=
\langle B,h_a\rangle.
$$

By Cauchy-Schwarz on the raw support:

$$
\frac{
|\langle B,v_a\rangle|^2
}{
\lVert B\rVert^2\lVert v_a\rVert^2
}
\le
\frac{m_a(B)}{\epsilon_a}.
$$

The passage from one coordinate to the full span costs the inverse smallest eigenvalue of the normalized Gram matrix. This gives the displayed bound.

The receipt tests the bound with shell responses `k=0,\ldots,4`. On seeded 1+1 sprinkling-like permutation orders:

| `N` | shell fraction | block actual | block bound | cos actual | cos bound | min `lambda` | min efficiency |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `32` | `0.35685483870968` | `0.17529061825976` | `0.17561643067145` | `0.11513499542422` | `0.42949214313013` | `0.83137971888198` | `0.87458455522972` |
| `64` | `0.26016865079365` | `0.092294794608194` | `0.092353491434182` | `0.07924966215941` | `0.28830995791162` | `0.8985623789803` | `0.92479957328743` |
| `96` | `0.21041666666667` | `0.06736086184106` | `0.067386171303929` | `0.054463397485556` | `0.24846750556917` | `0.92395962214536` | `0.94381945042639` |
| `128` | `0.1742125984252` | `0.047638821964884` | `0.04764408693243` | `0.038386819787238` | `0.1991876659187` | `0.94668586662437` | `0.96799165536407` |
| `160` | `0.15522798742138` | `0.042483173890717` | `0.042485646022961` | `0.033937594611015` | `0.17828874399749` | `0.94297426020284` | `0.96972165306986` |
| `192` | `0.13688917975567` | `0.03286249834395` | `0.032867030145471` | `0.0270439308271` | `0.15836631944548` | `0.95846291021659` | `0.97580600716451` |

For the staged block target, the theorem is almost tight: the actual projection and bound agree to receipt precision. This is the desired theorem spine:

> shell-local marks cannot erase a dense staged block unless the block has significant mass inside the small-shell support, or the shell response has poor zero-row efficiency or bad Gram conditioning.

For coherent cosine structure, the same bound is valid but loose. The actual projection shrinks, but the support-mass bound remains larger because the cosine target has mass on shell-supported pairs even when the local shell span is not well aligned with it. This is not a problem for the block-laundering theorem; it is a warning that coherent fields need their own spectral/field-law argument.

The two-layer adversary shows why shell-density regularity is essential:

| `N` | shell fraction | actual | bound | `lambda_min` | min efficiency |
|---:|---:|---:|---:|---:|---:|
| `32` | `0.51612903225806` | `1.0` | `1.0` | `1.0` | `0.48387096774194` |
| `64` | `0.50793650793651` | `1.0` | `1.0` | `1.0` | `0.49206349206349` |
| `128` | `0.50393700787402` | `1.0` | `1.0` | `1.0` | `0.49606299212598` |
| `192` | `0.50261780104712` | `1.0` | `1.0` | `1.0` | `0.49738219895288` |

Here the bound correctly allows full laundering because the shell is dense. Therefore the two-layer order must fail `Phi_shell`; it cannot be rescued by mark-sector language.

The candidate theorem for the record law is now:

> If an order has calibrated small-shell density, nondegenerate shell-response zero-row efficiency, and controlled shell-response Gram conditioning, then intrinsic shell-local mark responses cannot project away a dense staged/block geometry residue except in proportion to the residue's mass on small shells.

This is not the final click law, but it is the first clean structural lemma connecting the interval-profile work with the mark-sector work.

> **[CONSTRAINED] A deterministic shell-projection bound now explains why intrinsic local marks cannot freely launder staged block geometry under sprinkling-like shell regularity. The bound is tight for staged blocks, valid but loose for coherent waves, and it correctly fails to save dense two-layer orders because their shell density is already non-manifoldlike.**

---

## 30. Coherent shell-cancellation bound

The previous theorem is a support-mass theorem. It is tight for staged block residues because block mass is organized by the same local shell supports that can launder it. But it is loose for coherent waves. A coherent wave has nonzero mass on almost every kind of pair, including small-shell pairs, even when the shell-local response span is poorly aligned with it.

The next deterministic inequality uses correlation rather than support.

Let `B` be a zero-row coherent target. In the receipt,

$$
B_{ij}
=
\cos
\left(
\frac{2\pi(i-j)}{N}
\right),
$$

zero-row projected. Let `v_a=P_0h_a` be the zero-row projections of the intrinsic shell-local stress-tensor responses

$$
\mathbf 1_{\{|I(i,j)|=k\}}
(\Delta c)^2,
\qquad
\mathbf 1_{\{|I(i,j)|=k\}}
(\Delta s)^2,
\qquad
\mathbf 1_{\{|I(i,j)|=k\}}
(\Delta c)(\Delta s),
$$

for `k=0,\ldots,4`, where

$$
c_i=\cos\frac{2\pi i}{N},
\qquad
s_i=\sin\frac{2\pi i}{N}.
$$

Define the normalized correlations

$$
z_a
=
\frac{
\langle B,v_a\rangle
}{
\lVert B\rVert\lVert v_a\rVert
}.
$$

If `C` is the normalized Gram matrix of the `v_a`, then

$$
\frac{\lVert \Pi_LB\rVert^2}{\lVert B\rVert^2}
\le
z^\top C^{-1}z
\le
\lambda_{\min}(C)^{-1}
\sum_a z_a^2.
$$

This is the coherent-wave counterpart to the support-mass bound. It says:

> coherent leakage is small when each shell-local stress response has small normalized correlation with the coherent target and the shell-response Gram matrix is not degenerate.

The finite receipt gives:

| `N` | shell fraction | actual projection | correlation bound | support bound | max correlation | min `lambda` | dim |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `32` | `0.32862903225806` | `0.099662119798697` | `0.31905758771245` | `3.2856888825802` | `0.16029990694806` | `0.27242870165074` | `15` |
| `64` | `0.27281746031746` | `0.041457594774258` | `0.08602792983846` | `1.5816452758157` | `0.08832656870979` | `0.58310930540309` | `15` |
| `96` | `0.2172149122807` | `0.026933847363225` | `0.057103500798841` | `1.3662946044659` | `0.069906555955459` | `0.56577655392781` | `15` |
| `128` | `0.17784202755906` | `0.014914179438295` | `0.030893824969542` | `1.124477305402` | `0.055231991455429` | `0.59977388282486` | `15` |
| `160` | `0.15459905660377` | `0.012750658630249` | `0.02561090433189` | `0.95753407632478` | `0.056395888277583` | `0.61613855828622` | `15` |
| `192` | `0.13961605584642` | `0.01075222645749` | `0.021711255547288` | `0.88425475678249` | `0.04423515587894` | `0.61508881298965` | `15` |

The receipt preserves the finite caveats:

1. `N=32` has rough Gram conditioning.
2. The actual projection is not zero; it falls by about a factor of `9.27` over the tested range.
3. The support-mass bound is valid but much too loose, remaining about `40.7` times larger than the correlation bound at `N=192`.

This is the missing distinction:

$$
\text{staged block}
\quad\Rightarrow\quad
\text{support-mass bound},
$$

while

$$
\text{coherent wave}
\quad\Rightarrow\quad
\text{correlation / spectral cancellation bound}.
$$

The marked click-law skeleton should therefore not treat coherent waves as merely “blocks with a different sign pattern.” They require a field-sector law that controls spectral correlations of shell-local responses.

The next theorem target is:

> For sprinkling-like shell profiles and projectively admissible smooth/coherent marks, the normalized correlations `z_a` between shell-local stress responses and nonlocal coherent pair kernels vanish in the large-`N` limit, with controlled Gram conditioning.

If true, coherent marked fields cannot launder geometry through shell-local coupling. They must either remain in the marked field sector or pay for an explicitly nonlocal interaction.

> **[CONSTRAINED] The coherent-wave exception now has its own bound. Shell support alone is too crude; normalized shell-response correlations supply the right finite control. The emerging record law separates staged-block suppression from coherent-field admissibility instead of forcing both through one statistic.**

---

## 31. Integrated candidate law and adversary matrix

The results above now force a cleaner picture. The click law should not be a single scalar such as matching pressure, shell density, mark action, or second moment. Each scalar alone has already been defeated by some adversary.

The candidate object is a sectoral record action:

$$
\mathcal A_N(O,F,L)
=
\Phi_{\rm geom}
\left(
D-\Pi_{L(F;O)}D
\right)
+
\Phi_{\rm shell}(O)
+
\Phi_{\rm mark}(F)
+
\Phi_{\rm coupling}(F,O,L)
+
I_{\rm adm}(F,O,L)
+
\Phi_{\rm 2nd}(O).
$$

Here:

| term | role |
|---|---|
| `Phi_geom` | penalizes macroscopic staged/fiber order pressure, or is replaced by the full calibrated finite-dimensional order law |
| `Phi_shell` | enforces calibrated interval-shell density and shell regularity |
| `Phi_mark` | gives an independent projective finite-action law for marks |
| `Pi_L` | gives projection credit only through admissible order-intrinsic local/stress responses |
| `Phi_coupling` | charges nonlocal mark-to-geometry interactions |
| `I_adm` | forbids post-hoc marks and post-hoc projection families |
| `Phi_2nd` | represents the remaining unlabeled second-moment/local-factor theorem fork |

The new receipt is not a proof of this law. It is an adversary coverage matrix. It asks whether the current pieces each do necessary work:

| adversary | status | gate | audited witness |
|---|---|---|---|
| macroscopic staged/fiber pressure | covered | `Phi_geom` | hostile matching tail / physical tail margin `2.3374138139143374562858432305309` |
| two-layer dense-shell order | covered | `Phi_shell` | shell ratio `3.6717131474104065296233393127409`, with exact shell laundering projection `1` |
| post-hoc exact block marks | covered | `Phi_mark + I_adm` | exact block action grows as `8N`; `E_16=128`, `E_128=1024` |
| free global product mark projection | covered | `Phi_coupling + I_adm + Pi_L` | global product projection `1`, local/stress projection at `N=256` only `0.0000306382009634387352` |
| coherent-wave false positive | rerouted | `Phi_mark + Phi_coupling + Pi_L` | coherent projection falls by `9.2689751460054467283303174855293`; support bound is `40.72794200485306243457493204821` times looser than correlation bound |
| bounded-width linear hidden cluster | open | `Phi_2nd` | finite `P_8` linear excess remains below the split-null guard; the quotient local-factor theorem is still missing |

This is the important architectural point:

$$
\text{manifoldlike record law}
\ne
\text{one magic regularizer}.
$$

The law has to behave like a small constitution. It must say which sector is allowed to explain which residue.

1. A non-manifold order cannot hide behind marks if its shell profile is wrong.
2. A staged block cannot be erased by marks unless those marks existed independently and pay projective action.
3. A legitimate coherent field should not be rejected merely because it has a large global pair kernel.
4. A coherent field also cannot get free nonlocal geometry projection; its coupling must be local/stress-type or explicitly charged.
5. A bounded-width linear hidden cluster is not solved by the current sectoral law. It still requires the unlabeled second-moment theorem, or a stable rare-order counterexample.

The current smallest live enemy is therefore not the old broad family of staged blocks. It is narrower:

> a bounded-width linear hidden-cluster law, projected to unlabeled orders, whose small induced suborders wash out, whose shell profile is sprinkling-like, whose marks are projectively admissible or absent, and whose residue, if any, survives only as an aggregate likelihood/local-factor effect.

That is exactly the place where the second-moment object

$$
S_N
=
\mathbb E_{P_N}
\left[
\left(
\frac{dQ_N}{dP_N}
\right)^2
\right]
$$

remains decisive.

The theorem target is now crisp:

> prove boundedness of `S_N` for bounded-width linear-window hidden clusters on the unlabeled order sigma-field, under the local-factor/nonshared-neutrality hypotheses; or construct a stable rare-order class that makes `S_N` diverge.

### Hostile review 31

**Objection.** The integrated action is too flexible. With enough sectors, anything can be saved.

**Reply.** Correct risk. That is why the receipt is framed as an adversary ledger, not a final theory. Every sector must earn its place by blocking an explicit failure mode:

| sector | removed failure if absent |
|---|---|
| no `Phi_shell` | two-layer shell-local laundering passes |
| no `Phi_mark` / `I_adm` | exact hidden block labels are free |
| no `Phi_coupling` | global `f(i)f(j)` marks erase staged geometry |
| no coherent correlation/field sector | matterlike Fourier modes are mistaken for staging |
| no `Phi_2nd` | linear hidden clusters remain invisible to local finite tests |

The dangerous next step is not to add another sector. The dangerous next step is to prove one of the existing forks:

$$
\text{unlabeled second-moment boundedness}
\quad
\text{or}
\quad
\text{stable rare-order divergence}.
$$

> **[CONSTRAINED] The campaign has consolidated into a sectoral candidate law. The old adversaries are no longer one amorphous problem: staged pressure, bad shell density, post-hoc marks, free nonlocal coupling, coherent fields, and linear hidden clusters each demand a different gate. The only live mathematical obstruction left in this paper is the unlabeled second-moment/local-factor fork.**

---

## 32. Linear-window polymer budget

The remaining fork is now attacked directly. The hidden-cluster law is not allowed to change. The question is whether the ordinary local polymer terms already show growth, or whether any residue must be more global/unlabeled.

Let `A_N(c)` be the density-matched one-axis copula excess after zero-row projection. From the earlier rank-copula receipt, the same-hidden-pair two-axis excess has the finite form

$$
\frac{A_N(c)^2}{d_N},
\qquad
d_N=\frac{N(N-3)}{2}.
$$

For width two, there are `M=N/2` hidden pairs. The same-pair contribution is therefore

$$
M\frac{A_N(c)^2}{d_N}.
$$

Let `rho_r(c)` be the disjoint `r`-factor residue of the zero-row one-axis factor. The truncated polymer budget is

$$
B_N^{(R)}(c)
=
M\frac{A_N(c)^2}{d_N}
+
\sum_{r=2}^{R}
\binom{M}{r}
\rho_r(c)^2.
$$

This is not the unlabeled second moment. It is a finite diagnostic for the most likely washout mechanism.

The receipt computes `R=5` at `N=8,10,12` and `c=0.5,1,2,4`. The hardest corner is `c=0.5`, `N=8`:

| `c` | max truncated budget | hardest `N` |
|---:|---:|---:|
| `0.5` | `0.00396620845573223759` | `8` |
| `1.0` | `0.0000890653297483220058` | `12` |
| `2.0` | `0.00000154375093108296672` | `12` |
| `4.0` | `0.0000000323641731110805198` | `12` |

For the hardest case, the decomposition is:

| term | value |
|---|---:|
| same-hidden-pair budget | `0.00347200968038025786` |
| `r=2` disjoint cycle | `0.000462934624050701048` |
| `r=3` disjoint cycle | `0.0000300612135294026321` |
| `r=4` disjoint cycle | `0.00000120293777187605244` |
| total | `0.00396620845573223759` |

Across all tested cases, the largest cycle share is only

$$
0.124602320041380989.
$$

The message is sharp:

> The first polymer terms do not expose a growing residue. If the bounded-width linear hidden cluster fails to wash out, the failure is probably not one of the first few labeled local polymer factors. It is more likely an all-orders effect, an unlabeled quotient effect, or a selected rare-order denominator.

### Hostile review 32

**Objection.** A truncated budget can miss the theorem-breaking term.

**Reply.** Correct. This receipt does not prove boundedness. It merely changes the target. Since `r=2,3,4,5` are small and decreasing in the tested range, the next proof should not spend more energy on isolated low-order factors. It should prove an all-orders polymer bound or find a selected rare class.

> **[CONSTRAINED] The ordinary low-order polymer expansion supports the washout side. The same-hidden-pair term dominates, disjoint cycles decrease after `r=2`, and wider linear jitter suppresses the budget. The remaining obstruction has moved to the analytic bound on `A_N(c)`, the all-orders tail, and the unlabeled quotient.**

---

## 33. Continuous copula envelope for `A_N(c)`

The polymer budget reveals that the same-hidden-pair term is the first thing to control. That term is governed by `A_N(c)`. So the next attack is to find a clean envelope for `A_N(c)`.

Let

$$
X=S+E,
\qquad
S\sim {\rm Unif}[0,1],
\qquad
E\sim {\rm Unif}[-c,c].
$$

Let `f_c` and `F_c` be the density and distribution function of `X`. If

$$
r=F_c(x),
\qquad
s=F_c(y),
$$

then the continuous sibling copula density is

$$
h_c(F_c(x),F_c(y))
=
\frac{
\left|
[0,1]\cap[x-c,x+c]\cap[y-c,y+c]
\right|
}{
4c^2f_c(x)f_c(y)
}.
$$

The continuous copula energy is

$$
A_\infty(c)
=
\iint
\left(
h_c(F_c(x),F_c(y))-1
\right)^2
f_c(x)f_c(y)\,dx\,dy.
$$

The receipt computes this by deterministic Gauss-Legendre quadrature. The striking pattern is:

| `c` | `A_infty` at 160 nodes | `c^2 A_infty` |
|---:|---:|---:|
| `0.5` | `0.289972464365796934229493` | `0.0724931160914492335573731` |
| `1.0` | `0.0725055893837703749771042` | `0.0725055893837703749771042` |
| `2.0` | `0.0181364728687117373973927` | `0.0725458914748469495895707` |
| `4.0` | `0.00453845919105849753594623` | `0.0726153470569359605751397` |

The scaled spread is only

$$
0.000122230965486727018.
$$

Thus the theorem-shaped conjecture is:

$$
A_N(c)
\le
\frac{K}{c^2},
\qquad
c\ge\frac12,
$$

with a safe audited guard

$$
K=0.075.
$$

This guard bounds the finite audited values too. The largest finite ratio is:

$$
\max_{N,c}
\frac{A_N(c)}{0.075/c^2}
=
0.562245211516599987.
$$

If this inequality is proved, then the same-hidden-pair contribution obeys

$$
M\frac{A_N(c)^2}{d_N}
\le
\frac{K^2}{c^4(N-3)},
$$

for width two. That is the first real `O(1/N)` mechanism for the linear-window washout theorem.

### Hostile review 33

**Objection.** The continuous envelope may not imply the finite rank envelope.

**Reply.** Correct. It gives a proof target, not a proof. The missing step is a finite-rank approximation theorem that controls the discretized rank kernel uniformly in `N`.

**Objection.** Even if `A_N(c)` is bounded, all-orders polymer interactions may accumulate.

**Reply.** Correct. The next lemma must combine the `K/c^2` envelope with a summable all-orders cycle-tail bound. The low-order budget says this is plausible; it does not prove it.

**Objection.** The unlabeled quotient can still amplify a rare denominator.

**Reply.** Correct. That is the remaining counterexample path. If the washout proof fails, it should now fail through a selected rare unlabeled order, not through the first few labeled polymer terms.

> **[CONSTRAINED] The campaign has found a concrete analytic spine: prove `A_N(c) <= K/c^2`, prove a summable all-orders cycle-tail bound, then prove that quotienting to unlabeled orders does not create a rare-denominator explosion. This is now the shortest honest path to bounded `S_N`; the rival path is an explicit stable rare-order class.**
