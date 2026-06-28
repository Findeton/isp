# The record click-law, XXIII: recursive interval law, no-hidden-staging, and bracket-field stress tests

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-26. Twenty-third paper of the v7 program, now collapsed to include the former Paper XXIV-XXVI continuation campaigns. This paper follows Paper XXII's marked-compensator and interval-profile audit. It investigates whether manifoldlikeness can be constrained by hereditary interval laws, no-hidden-staging/fiber controls, density regularity, and ultimately a joint global-and-interval martingale bracket field. Tags: **[PRINCIPLE]** = candidate formulation; **[STRESS TEST]** = finite diagnostic, not a theorem; **[COUNTEREXAMPLE]** = explicit obstruction or spoof; **[CONSTRAINED]** = narrowed but not unique; **[OPEN]** = disclosed residue. Numerical checks are in `v7/code/p23_recursive_interval_law.py`, `v7/code/p24_projective_fixed_point_law.py`, `v7/code/p25_interval_bracket_action.py`, `v7/code/p23_joint_global_interval_bracket.py`, `v7/code/p23_multiscale_interval_pair_covariance.py`, `v7/code/p23_stability_adversarial_limit_audit.py`, `v7/code/p23_rooted_palm_bracket_audit.py`, `v7/code/p23_mecke_palm_poisson_audit.py`, `v7/code/p23_asymptotic_jittered_cluster_limit_audit.py`, `v7/code/p23_jitter_scaling_phase_diagram.py`, `v7/code/p23_jitter_scaling_exponent_audit.py`, `v7/code/p23_jitter_linear_washout_audit.py`, `v7/code/p23_washout_two_sample_distance_audit.py`, `v7/code/p23_washout_residue_dichotomy_bounds.py`, `v7/code/p23_linear_critical_kernel_audit.py`, `v7/code/p23_linear_window_interval_variance_audit.py`, `v7/code/p23_linear_window_load_bracket_audit.py`, `v7/code/p23_observable_label_information_audit.py`, `v7/code/p23_higher_order_label_residue_audit.py`, `v7/code/p23_observable_law_metric_campaign.py`, `v7/code/p23_degree_covariance_label_residue_audit.py`, `v7/code/p23_asymptotic_bracket_identity.py`, `v7/code/p23_order_visible_bracket_variance_audit.py`, `v7/code/p23_reconstructed_coordinate_palm_audit.py`, `v7/code/p23_growing_window_washout_bounds.py`, `v7/code/p23_sqrt_collision_poisson_law.py`, `v7/code/p23_hidden_partition_likelihood_audit.py`, `v7/code/p23_palm_kernel_projection_audit.py`, `v7/code/p23_exact_palm_kernel_integral.py`, `v7/code/p23_pair_palm_signature_audit.py`, `v7/code/p23_aggregate_pair_palm_bracket_audit.py`, `v7/code/p23_aggregate_pair_palm_source_audit.py`, `v7/code/p23_invariant_aggregate_pair_palm_bracket_audit.py`, `v7/code/p23_endpoint_symmetric_pair_flag_likelihood_audit.py`, `v7/code/p23_mesoscopic_rooted_flag_field_audit.py`, `v7/code/p23_small_unlabeled_likelihood_second_moment.py`, `v7/code/p23_unlabeled_second_moment_ladder.py`, `v7/code/p23_unlabeled_second_moment_n8_stability.py`, `v7/code/p23_unlabeled_rare_class_stability_audit.py`, `v7/code/p23_partition_overlap_poisson_bound.py`, `v7/code/p23_local_factor_inequality_audit.py`, `v7/code/p23_overlap_graph_cycle_tax.py`, `v7/code/p23_cycle_neutrality_signature_audit.py`, `v7/code/p23_overlap_graph_mgf_bound.py`, `v7/code/p23_transfer_operator_cycle_theorem.py`, `v7/code/p23_overlap_component_factorization_audit.py`, `v7/code/p23_diagonal_identity_rarity_bound.py`, `v7/code/p23_split_sample_diagonal_artifact_audit.py`, `v7/code/p23_direct_unlabeled_likelihood_ladder.py`, `v7/code/p23_selected_class_probability_formula.py`, `v7/code/p23_selected_rare_class_n10_n12_audit.py`, and `v7/code/p23_n12_invariant_screen_selected_count.py`, all at mpmath `dps = 140`.

---

## Scope guards

1. **This paper does not prove manifoldlikeness.** It gives a sharper target and finite adversarial stress tests. It does not show that SHARD records, causal sets, cellular automata, deterministic hidden machines, or any proposed substrate typically produce manifoldlike orders.

2. **A full interval-size histogram is still only first-order.** Paper XXII showed that five alpha samples are moment-underdetermined. This paper strengthens the object from finite alpha samples to the full interval-size distribution, then shows why even that is not enough.

3. **Recursive interval consistency is necessary, not sufficient.** In a 1+1 sprinkling, the interior of a causal interval is again a sprinkling of a smaller causal interval, conditional on its size. That suggests a hereditary law. The receipt only tests the first recursive relation statistic; it is not a complete recursive distribution law.

4. **Structural interval self-similarity, not dynamical locality.** The BHS finite-neighbor obstruction remains. Long-range quantum entanglement is not being forbidden. The proposed constraint is that causal intervals must not be globally staged by reusing the same hidden interior block across many nominally different intervals.

5. **No uniqueness theorem is claimed.** The useful result is a narrowing: the click law, if it is to carry manifoldlikeness, must control hereditary interval statistics, overlap/concentration, density regularity, and calibrated bracket/covariance structure, not just scalar counts, MM dimension, height, or first-order interval histograms.

6. **The collapsed continuation is adversarial.** Projective deletion, interval means, interval brackets, and a finite joint bracket field are all stress-tested and partially defeated. The paper records the failures because they define the next target.

---

## Abstract

Paper XXII reached the moment-problem wall. A finite profile

$$
P_\alpha = N^{-1}\sum_{x<y}\exp\!\left(-\alpha |I(x,y)|\right)
$$

can be matched by a positive interval-size measure while hiding most relation mass at large interval size. A naive complete-sandwich realization pays a large transitivity tax, but the open problem remained: maybe a more clever transitive order can spoof the interval profile.

This paper pushes the target one layer deeper. The first-order interval law counts only

$$
H_k(C)=\#\{x<y: |I(x,y)|=k\}.
$$

For fixed-N 1+1 binomial sprinklings, the receipt derives and checks the exact finite-N expectation

$$
\mathbb{E}\!\left[\frac{H_k}{N}\right]
=(N-1)\binom{N-2}{k}\sum_{j=0}^{N-2-k}
\frac{(-1)^j\binom{N-2-k}{j}}{(k+j+1)^2(k+j+2)^2}.
$$

The full histogram expectation sums to `(N-1)/4` and reproduces the generating-function expectation from Paper XXII to better than `1e-80`. A fixed sprinkling at `N=192` matches a coarse full-histogram binning with maximum log gap

`0.086522558527323288656`.

But the full interval-size law is still blind to what is inside the intervals. The natural next object is recursive interval consistency. For every interval `J(x,y)`, let `R(J)` be the number of relations among its interior elements. Define the first recursive statistic

$$
\Theta_2(C)=
\frac{\sum_{x<y,\ |J|\ge 2} R(J)}
{\sum_{x<y,\ |J|\ge 2}\binom{|J|}{2}}.
$$

For a 1+1 sprinkling, conditional on an interval interior having size `k`, the expected number of relations inside that interior is `binom(k,2)/2`. The finite pooled ratio still fluctuates, but it is centered on the 2D value in this first-moment sense. This is a 1+1 target; in dimension `d` the recursive target is `f(d)`, not universally `1/2`. The receipt finds:

- fixed sprinkling, `N=384`: `Theta_2=0.51723112740470607482`;
- chain, `N=256`: `Theta_2=1`;
- thin-middle-plus-chain, `N=1024`: `Theta_2=0.0097672403607577488086`.

So the recursive statistic catches the thin-middle adversary that Paper XXII used to spoof MM, height, and one calibrated alpha.

Then the hostile path opens. Construct a staged order with a single 31-record middle block `P` whose first-order relation fraction is close to 1+1, bottom layer `A`, top layer `B`, all relations `A<P<B`, and an isolated chain to supply the 1+1 longest-chain scale. At `N=512` the receipt uses

`|A|=218`, `|P|=31`, `|B|=218`, `|chain|=45`.

This order is violently non-manifold, and it passes the deliberately coarse scalar/recursive-mean tests:

- related-pair fraction `r=0.476042685909980431`;
- `d_MM=2.0652375054644658753`;
- height `H=45`, close to `2 sqrt(512)=45.254833995939041562`;
- recursive mean `Theta_2=0.52680255524312207184`.

It does **not** pass the full first-order interval histogram. It has a spike at interval size `31`:

`observed H_31/N = 92.845703125`, while the 1+1 expectation is `1.08469454780777819414953`, a ratio of `85.596173883832825458`.

So its role is narrow: it disproves a pooled recursive mean as a standalone law. A real target must be conjunctive: full first-order interval law, recursive content law, and overlap/concentration law.

It passes the recursive mean because many outer intervals have the same first-order good-looking interior `P`. The block `P` is not recursively good in the finite receipt: its own `Theta_2` is `0.653648509763617677`. A truly hereditary law would inspect that. This exposes the next missing ingredient: no hidden staging. The receipt measures this by the load of records inside interval interiors. For all intervals with `|I|>=8`, define `L_z` as the number of tested interiors containing record `z`, and define the effective support

$$
S_{\mathrm{eff}}=\frac{\left(\sum_z L_z\right)^2}{\sum_z L_z^2}.
$$

It also tracks the largest duplicate interior-set fraction. The fixed sprinkling has

`S_eff/N = 0.67745115206078147824`, `max duplicate fraction = 0.00019678583142013775008`.

The staged adversary has

`S_eff/N = 0.061548950771653563845`, `max duplicate fraction = 0.87488954344624447717`.

The load statistic is region-shape dependent, so the receipt adds a 1+1 continuum null calibration. Without a size threshold, the continuum mean-field load profile in the unit Alexandrov square is proportional to `uv(1-u)(1-v)`, giving

$$
\frac{S_{\mathrm{eff}}}{N}\to
\frac{\left(\int f\right)^2}{\int f^2}
=\frac{25}{36}
=0.69444444444444444444.
$$

The fixed sprinkling gives `0.68014416377691967134`; the staged order gives `0.061613974505719183211`.

The receipt also adds a soft-overlap check, because exact duplicate interiors are easy to game. On a deterministic sample of interval interiors, the fixed sprinkling has mean Jaccard overlap `0.096290193615272969517` and p95 `0.3850267379679144385`; the staged adversary has mean `0.85910029731534583575` and p95 `1.0`.

The receipt then attacks the next obvious evasions. Fiber blow-ups replace each sprinkling point by a hidden four-record cloud. Antichain fibers keep `d_MM=2.0046486296873872374` and `Theta_2=0.486756325219465709`, but their longest-chain ratio collapses to `H/(2 sqrt(N))=0.38273277230987157784`. Chain fibers keep `d_MM=1.9838377498285342214` and `Theta_2=0.548913580437378619`, but overshoot height with `H/(2 sqrt(N))=1.5309310892394863114`. Independent distributed staging lowers the exact duplicate fraction from `0.87488954344624447717` to `0.20466639377814162914`, but pays by leaving the 2D MM band with `d_MM=3.6176602504201855312` and still has elevated overlap.

Continuing that hostile path, the receipt tunes a two-fiber construction by mixing chain and antichain fibers. This is the first adversary in the paper that evades the old load/overlap alarm. It reaches `H/(2 sqrt(N))=0.99510520800566610239`, `d_MM=2.1131578539640458008`, `Theta_2=0.489854632712372087`, `S_eff/N=0.694386125691969685`, and sampled mean Jaccard `0.085077747538599827391`. It is exposed by two finer signatures: the log-2 interval profile is shifted to `0.90810627527125956341` of the 1+1 expectation, and the order has `196` exact external-twin pairs, compared with `1` accidental pair in the fixed sprinkling.

A cross-linked staged-reservoir search also repairs height, giving `H/(2 sqrt(N))=0.97227182413150284605`, but overpays elsewhere: `d_MM=1.6554287940645027748`, `Theta_2=0.84132595188654795616`, a module-middle histogram spike ratio `4.79827139704259842`, and `4555` exact external-twin pairs.

The campaign then follows the exact-twin opening. Single-tag and double-tag decorations do not close it. A twin-free local motif finally drives exact external twins to `0` and keeps `P_log2` close, with ratio `0.98308573963087372273`, while retaining good global statistics: `d_MM=1.9130886247586462703`, `H/(2 sqrt(N))=0.96958968985167466387`, `Theta_2=0.518896639942437559`, and `S_eff/N=0.688885691516175239`. This is the strongest purely quotient-fiber adversary so far. It is exposed by a **soft near-twin tail**: there are `674` pairs with external causal-neighborhood difference at most `8`, compared with `95` in the fixed sprinkling. A richer random local-motif search up to width `16` does not improve this tail in the tested broad band; its best candidate has `998` such pairs and pays with `P_log2` ratio `0.88291207260521286423`.

The follow-up branch lets a four-record hidden fiber borrow actual 1+1 coordinate jitter. With bounded jitter, the adversary becomes much stronger: `d_MM=1.9935222878608324494`, `H/(2 sqrt(N))=0.96958968985167466387`, `Theta_2=0.505849474807618903`, `S_eff/N=0.699811171178873987`, `P_log2` ratio `0.98839205290919710349`, and only `153` `diff<=8` near-twin pairs. This nearly closes the soft-tail alarm but still exceeds the sprinkling count `95`. If the jitter is increased further, the soft tail can be matched (`93` versus `95`) with good scalar profiles, but the hidden fiber has effectively washed out into a clustered 1+1 point process: same-hidden-cluster `diff<=8` pairs fall to `19`. The new boundary is therefore sharper: escaping the no-hidden-fiber tests seems to require abandoning a true hidden quotient and moving into a density/regularity problem.

The campaign then follows the density/regularity opening. Endpoint-load regularity, conditional endpoint residuals, and sampled induced size-4/5 pattern densities are added. A regularity-aware clustered adversary with jitter span `3.0` still matches the soft tail and scalar profiles: `diff<=8=100` versus sprinkling `95`, `P_log2` ratio `0.98835534054519469285`, `d_MM=1.9890145938921685549`, exact twins `1`, and p95 Jaccard `0.38333333333333333333`. Its conditional endpoint residual gap is `0.36261367215434820561`, below the independent sprinkling-vs-sprinkling calibration `0.70446455247920145541`. Its sampled induced pattern total-variation gap is `0.19580078125`, close to the independent sprinkling calibration `0.172119140625`. The top pattern-aware search keeps the same candidate.

So the next click-law target is not merely the full interval generating function, nor merely heredity plus a handful of density scalars. It is a full calibrated finite-dimensional record law: interval interiors must look recursively manifoldlike, must be distributed across the record set rather than globally staged through a reused hidden block, must not arise by duplicating records with nearly identical causal environments, and must match the finite-dimensional order statistics of sprinkling rather than a small checklist. The intended direction is law-first: a future click law should make manifoldlike orders the stable/typical phase of a specific recursive record law, while the finite diagnostics here are only projections used to find adversaries.

The collapsed continuation then tries to turn "full law" into a working object. Random deletion projectivity is too weak; causal interval fixed points are sharper but mean interval signatures can be tuned; calibrated interval brackets catch the previous mean-tuned cluster but admit a bracket-tuned cluster; a 47-dimensional joint global-and-interval bracket projection with train/held-out sprinkling calibration rejects density-modulated and staged families but still admits tuned jittered clusters inside the finite null; a multiscale interval-pair covariance projection rejects density-modulated and staged adversaries at `N=192` and `N=384`, but still admits tuned jittered clusters and exposes finite calibration instability. A compact stability audit reduces but does not eliminate finite calibration leakage, and the adversarial-limit audit finds a sharper obstruction: fixed-width hidden clusters have unrooted pair mass `O(1/N)` while rooted hidden multiplicity remains `O(1)`. A first rooted/Palm score is stable on fresh sprinklings but does not reject a jittered width sweep up to width `16`; the same hidden construction labels cease to be order-visible near twins as jitter diversifies their causal neighborhoods. A deletion-increment Mecke/Palm shadow catches a gross density-modulated/Cox-like process, but the jittered width sweep still remains inside the finite null at smaller scales. The asymptotic jitter audit then finds a stronger signal: high jitter sits inside the finite null at `N=192,384` but separates sharply at `N=768` under exact triple-pattern and rooted features. A finite phase diagram shows locked hidden fibers, finite camouflage, and later reappearance as distinct regimes, with no tested fixed-jitter schedule proving full washout. An exponent audit then shows that the phase boundary is not controlled by raw jitter alone: hidden width, effective rank-mixing radius, and `N` are independent knobs. Linear/superlinear washout audits split the target again: some large-mixing clustered generators become finite-law close to sprinkling and lose order-visible near-label signatures, while other large-mixing cases remain visible. A first theorem proves the two easy asymptotic regimes: rooted/Palm residue when `w_N J_N` is below microscopic sprinkling spacing, and full-record washout under an intentionally strong product-TV coupling when `J_N` dominates the coordinate center range. The linear critical-kernel theorem then proves that fixed unrooted finite patterns are blind throughout the bounded-width linear window. A follow-up interval-size audit shows that even mesoscopic size moments can wash out at `N=768`; adding an order-visible load/bracket field restores only a marginal partial signal. An observable-label information audit shows the conceptual split directly: low-jitter hidden labels are recoverable from order-only pair features, while linear-window hidden labels fall to pseudo-label separability in this projection. The higher-order label audit then checks same-label triples and finds the same boundary: square-root mixing remains visible, but all tested linear schedules are pseudo-label-like. A combined observable-law projection metric and a degree-covariance audit both fail to recover a linear-window residue. The asymptotic marked-coordinate bracket calculation then finds a real residue: finite mixing ratio contributes `(w-1)B(c)` to the empirical-rank bracket. But finite order-visible bracket, degree-reconstructed coordinate, and reconstructed-coordinate Palm audits still do not recover that residue in the tested linear schedules. A growing-window theorem proves order-only washout for uniformly sampled `k_N=o(\sqrt N)` induced suborders. The square-root collision law then proves that at `k_N=a\sqrt N` hidden sibling collisions become a Poisson field with mean `a^2(w-1)/2`. A simple full-order hidden-partition top-tail likelihood recovers fixed and square-root schedules but not the tested linear schedules. The local Palm-kernel projection shows the pair kernel is exactly null, while a sibling-plus-outsider triple kernel is visible at mixing ratio `c=0.5` and washes into the iid Monte Carlo control by `c=1,2,4`; the exact Palm integral then proves the finite-`c` triple residue is real for all tested finite `c`, with L1 gap `1/300` at `c=1`. A pair-rooted Palm-signature audit sees fixed and square-root schedules but still fails on the tested linear schedules. An oriented aggregate pair-Palm bracket appears to break the deadlock, but hostile relabeling review shows it used endpoint ordering tied to record indices; the endpoint-invariant repair does not recover the tested linear schedules. The final target is therefore corrected: the all-pair Palm-bracket idea remains promising, but every candidate must be endpoint-symmetric and relabeling-invariant before it counts as order-only.

---

## 1. Why Paper XXII did not finish the target

Paper XXII made three useful moves:

- it replaced grid-calibrated pair density by the correct fixed-N 1+1 sprinkling calibration;
- it upgraded a single alpha to a five-alpha generating-function profile;
- it showed that finitely many alpha samples are a moment problem, not a law.

The obstruction was not just numerical. The data

$$
P_\alpha=N^{-1}\sum_m H_m e^{-\alpha m}
$$

are Laplace samples of the interval-size histogram. A finite number of samples cannot determine the histogram. Even the full polynomial

$$
G_C(q)=N^{-1}\sum_m H_m q^m
$$

only determines the number of intervals of each size. It says nothing about the order type inside those intervals, and it says nothing about whether many intervals share the same interior records.

That is the main update:

> **[CONSTRAINED] The click law cannot stop at the full interval-size generating function. It must see recursive interval content, reuse/concentration of interiors, and hidden-fiber duplication of causal roles.**

This is the first point where the target starts to look less like "match a list of moments" and more like a hereditary law on the record order.

---

## 2. Literature boundary

The direction is adjacent to existing causal-set and combinatorics work, but the specific adversarial package tested here is not identical to any single diagnostic found in the literature check.

Glaser and Surya proposed locality tests based on the abundance of `m`-element order intervals in manifoldlike causal sets, deriving analytic expectations and arguing that evidence of local regions is necessary for manifoldlikeness. Recent configuration-space work by Eichhorn, Mack, Le, and Wagner reports that link degree distributions, Hasse-graph Laplacian spectra, and interval abundance distinguish many manifoldlike and non-manifoldlike classes. Carlip's overview emphasizes the same core obstacle: most causal sets are non-manifoldlike and KR-like orders dominate kinematically, while path-integral/action suppression is still not a complete continuum-emergence theorem.

Combinatorics supplies the right adversarial language. Janson developed poset limits by homomorphism-density convergence, Hladky--Mathe--Patel--Pikhurko showed poset limits can be represented over a totally ordered probability space, and Razborov's flag-algebra method is the natural template for proving finite-pattern density inequalities by semidefinite relaxation. Those tools suggest the right mathematical formulation:

> **Transitive moment problem:** characterize which hereditary interval statistics and overlap statistics are feasible for finite transitive orders that also match MM dimension, height, and first-order interval abundance.

This paper does not solve that problem. It gives a receipt-backed reason to pose it.

---

## 3. The full first-order interval histogram

Let

$$
H_k(C)=\#\{x<y\ \mathrm{in}\ C: |I(x,y)|=k\},
$$

where `I(x,y)` is the open order interval. For a fixed-N 1+1 binomial sprinkling in an Alexandrov interval, use lightcone coordinates. For two random points, the absolute coordinate gaps `U,V` have density `2(1-u)` and `2(1-v)`. The pair is comparable with probability `1/2`. Conditional on comparability and `U,V`, the number of interior records is

$$
K\sim \operatorname{Binomial}(N-2,UV).
$$

Expanding `(UV)^k(1-UV)^(N-2-k)` gives:

$$
\mathbb{E}\!\left[\frac{H_k}{N}\right]
=(N-1)\binom{N-2}{k}\sum_{j=0}^{N-2-k}
\frac{(-1)^j\binom{N-2-k}{j}}{(k+j+1)^2(k+j+2)^2}.
$$

The receipt checks this at `N=96`:

- `sum_k E[H_k/N] = 23.75`;
- `(N-1)/4 = 23.75`;
- `P_log2` from the full histogram is `5.113632599282471664023028323927346711851`;
- direct generating-function value is the same to the displayed precision;
- both checks pass with gaps below `1e-80`.

At `N=192`, a fixed sprinkling has the following coarse bin ratios:

| interval size bin | observed `H/N` | expected `H/N` | ratio |
|---|---:|---:|---:|
| `0` | `3.97916666666666667` | `3.86771561461910792` | `1.02881573082` |
| `1` | `2.97395833333333333` | `2.89811828619744526` | `1.02616872041` |
| `2-3` | `4.81770833333333333` | `4.54456264268545812` | `1.06010384544` |
| `4-7` | `6.625` | `6.63639782050144059` | `0.998282529045` |
| `8-15` | `8.796875` | `8.74446246410166116` | `1.00599379734` |
| `16-31` | `10.125` | `9.74765990114259064` | `1.03871083959` |
| `32+` | `12.3333333333333333` | `11.3110832707522963` | `1.09037596472` |

The maximum log gap is

`0.086522558527323288656`.

This is a useful calibration target, but it is still first-order.

---

## 4. Recursive interval consistency

For a 1+1 sprinkling, if an interval contains `k` interior records, then conditional on its endpoints and on `k`, those `k` records are distributed as a smaller 1+1 sprinkling inside the smaller Alexandrov interval. Therefore `E[R(J) | |J|=k] = binom(k,2)/2`. The pooled ratio `Theta_2` is not asserted to equal `1/2` in every finite realization; it is a finite stress statistic around that first-moment target. In higher dimension this target becomes `f(d)`, the Myrheim-Meyer related-pair fraction for the dimension.

Define, for every interval `J(x,y)={z:x<z<y}`,

$$
R(J)=\#\{u<v: u,v\in J\ \text{and}\ u<v\ \text{in}\ C\}.
$$

The first recursive relation statistic is

$$
\Theta_2(C)=
\frac{\sum_{x<y,\ |J|\ge 2} R(J)}
{\sum_{x<y,\ |J|\ge 2}\binom{|J|}{2}}.
$$

The receipt finds:

| family | N | r | dMM | H | `Theta_2` |
|---|---:|---:|---:|---:|---:|
| fixed sprinkling | 384 | `0.533588990426457789` | `1.9128826850786` | 38 | `0.517231127404706075` |
| chain | 256 | `1.0` | `1.0` | 256 | `1.0` |
| thin-middle plus chain | 1024 | `0.476274208822091887` | `2.0645936758881` | 32 | `0.00976724036075774881` |

This is the first genuinely new positive constraint in the campaign. The thin-middle order was designed to spoof the older scalar, height, and single-alpha diagnostics. It cannot hide from the recursive statistic, because its large intervals contain an antichain-like middle rather than a smaller 1+1 order.

So the candidate law improves:

> **[CONSTRAINED] A record law that controls manifoldlikeness should require intervals to be recursively manifoldlike, not merely to have the right size distribution.**

---

## 5. The opened hostile path: reuse one good interval

The next adversary is obvious once the recursive test is stated.

If large intervals fail because their interiors are antichains, replace the antichain by a small sprinkling-like poset. Construct:

- a bottom antichain `A`;
- a middle poset `P` whose first-order related-pair fraction is 1+1-like;
- a top antichain `B`;
- all relations `A<P<B`;
- an isolated chain to supply the 1+1 longest-chain scale.

This order is not manifoldlike. It is globally staged. But every `A<B` interval has the same interior `P`, and `P` can have a good internal ordering fraction. The receipt uses:

`N=512`, `|A|=218`, `|P|=31`, `|B|=218`, `|chain|=45`.

The result:

| statistic | value |
|---|---:|
| related pairs | `62274` |
| related-pair fraction | `0.476042685909980431` |
| Myrheim-Meyer dimension | `2.0652375054644658753` |
| height | `45` |
| `2 sqrt(N)` | `45.254833995939041562` |
| recursive interval mean `Theta_2` | `0.52680255524312207184` |

So a recursive mean alone is spoofable. The adversary passes by reusing the same first-order good-looking middle block across most tested outer intervals. It is not a hard physical imposter: disconnected-component checks, Hasse spectra, link-degree distributions, and the full interval histogram would reject it.

The full interval histogram rejection is immediate in the receipt:

`H_31/N = 92.845703125`, compared with the 1+1 expectation `1.08469454780777819414953`, a ratio of `85.596173883832825458`.

The reused block is also not recursively good on its own: its internal `Theta_2` is `0.653648509763617677`. This matters. The counterexample is not "one perfect mini-manifold fools everything." It is narrower and more useful: a pooled recursive mean can be gamed if it is not accompanied by first-order histogram and hereditary checks at smaller scales.

This is the important negative result:

> **[COUNTEREXAMPLE] Recursive interval relation consistency is stronger than first-order interval abundance, but a pooled recursive mean by itself is not enough. A staged order can reuse one first-order-good interior and pass the recursive mean while failing the full histogram and deeper heredity.**

---

## 6. No hidden staging: interval-load concentration

The staged adversary fails in a different way. Its interval interiors are not spread through the record set. They are repeated.

For a tested band of intervals, here `|I|>=8`, define the load of a record

$$
L_z=\#\{\text{tested intervals whose interior contains }z\}.
$$

Define the effective support

$$
S_{\mathrm{eff}}=\frac{\left(\sum_z L_z\right)^2}{\sum_z L_z^2}.
$$

This is the usual participation-ratio idea: if interval interior mass is spread across many records, `S_eff` is large; if it is concentrated on a small reused middle block, `S_eff` is small. Also define

$$
D_{\mathrm{dup}}=
\frac{\max_S \#\{\text{tested intervals with interior set }S\}}
{\#\{\text{tested intervals}\}}.
$$

The receipt finds:

| family | tested intervals | `S_eff/N` | max load / mean load | `D_dup` |
|---|---:|---:|---:|---:|
| fixed sprinkling, N=384 | `30490` | `0.67745115206078147824` | `2.4695520224997192563` | `0.00019678583142013775008` |
| staged adversary, N=512 | `54320` | `0.061548950771653563845` | `16.797946327231731377` | `0.87488954344624447717` |

The effective-support ratio separates them by a factor

`11.006705127665349942`.

Because `S_eff` is region-shape dependent, the receipt adds one analytic calibration. In a 1+1 unit Alexandrov interval, without a size threshold, the continuum load profile for a point `(u,v)` is proportional to

$$
f(u,v)=uv(1-u)(1-v).
$$

Therefore the mean-field participation ratio is

$$
\frac{\left(\int f\right)^2}{\int f^2}
=\frac{(1/36)^2}{1/900}
=\frac{25}{36}.
$$

The receipt compares this null with the all-interior finite examples:

| family | all-interior `S_eff/N` |
|---|---:|
| 1+1 continuum null | `0.69444444444444444444` |
| fixed sprinkling, N=384 | `0.68014416377691967134` |
| staged adversary, N=512 | `0.061613974505719183211` |

The receipt also adds a soft-overlap statistic. It samples interval interiors and computes pairwise Jaccard overlaps. This is still not a final law, but it is less brittle than exact duplicate counting:

| family | mean Jaccard | p95 Jaccard | max Jaccard |
|---|---:|---:|---:|
| fixed sprinkling | `0.096290193615272969517` | `0.3850267379679144385` | `0.96969696969696969697` |
| staged adversary | `0.85910029731534583575` | `1.0` | `1.0` |

The exact thresholds in the receipt are not proposed as the law. They are a finite warning: a hereditary interval law needs a calibrated non-reuse or concentration component, including soft overlap, not merely exact duplicate detection.

The name "no hidden staging" is meant literally. A non-manifold order can fake local-looking interiors by using a single good interior stage as a reusable prop. The tested manifoldlike sprinkling does not do that; interval interiors overlap, but not by making almost all large intervals share the same hidden block.

---

## 7. What this changes for the click law

The click law target after Paper XXII was:

> match the full interval generating function, or an equivalent layer/action object.

This paper says that is still too shallow. The revised target is:

> match the full interval law recursively, and control the calibrated concentration/overlap of interval interiors.

This should not be read as a proposed theorem of the form "any order passing a finite checklist is manifoldlike." That would be too blunt. The better target is a **specific recursive record law** whose low-dimensional projections are these diagnostics. In that reading, the tests are not the law. They are observable shadows of the law, used to discover which adversarial orders must be assigned negligible weight or large action.

The sharper law-first formulation is:

> A candidate click law must define compensators, transition weights, or an action for recursive interval kernels such that sprinkling-like orders are stable/typical and staged, fibered, or globally scripted orders are exponentially penalized.

That formulation leaves room for nuance: finite orders can fluctuate, different dimensions have different interval kernels, and matter/entanglement marks can be long-range. What is constrained is not ordinary correlation at distance; it is the hidden reuse of causal-order interiors as a global staging mechanism.

In martingale language, this is not merely an event-mark compensator. It is a law for pair/update and hereditary interval statistics:

1. Scalar projection:

   `N_chi - kappa chi` in the dense simple regime.

2. First-order interval abundance:

   `H_k(C_n)` or `G_C(q)` with the correct finite-N sprinkling calibration.

3. Recursive interval content:

   conditional laws for the order inside `I(x,y)` given `|I(x,y)|=k`, with dimension-dependent target `f(d)`.

4. Interior support/concentration:

   controls preventing many different outer intervals from reusing the same hidden interior block, calibrated against the continuum region shape.

5. Soft overlap, not just exact duplicate interiors:

   Jaccard/overlap profiles or stronger interval-intersection laws, because exact duplicate detection is easy to defeat with decorations or distributed staging.

6. Soft no-hidden-fiber / extensional tail:

   controls the calibrated finite-N tail of records with identical or near-identical causal environments. The tuned and twin-free fiber adversaries show why this is separate from load concentration: hidden fibers can be spread across the whole record set, close exact-twin alarms, and still leave too many very-near causal roles.

7. Density/regularity projection:

   controls whether the order looks like a finite-density sprinkling rather than a lumpy clustered point process. The coordinate-jitter branch shows why this is a separate issue: enough jitter can erase the hidden-fiber near-tail, but then the adversary is no longer a clean quotient-fiber order.

8. Covariance-compatible expression:

   everything must be stated as a relabeling-invariant order observable, and a future dynamics must also avoid dependence on unphysical birth labels or hidden growth histories.

This is still not unique. But it is a much narrower target than "penalize non-manifold orders."

---

## 8. Relation to entanglement and locality language

The phrase "locally spread" can be misleading. Entangled physical systems can be far apart in emergent space, and causal-set discreteness cannot be treated as a finite-valency nearest-neighbor graph without breaking Lorentz invariance.

The proposed structural test does not say "only nearby things may be correlated." It says:

- choose a causal interval using the order;
- condition on its size;
- ask whether its interior order looks like a smaller interval;
- ask whether the record mass appearing inside such intervals is broadly supported rather than a single globally reused stage.

This is compatible with long-range entanglement. It is a structural condition on causal-order intervals, not a ban on nonlocal quantum correlations and not a matter-field locality principle.

---

## 9. Additional adversaries: fibers and distributed staging

The hostile opening after no-hidden-staging is clear: avoid a single reused middle block.

Two simple families were added to the receipt.

First, a **fiber blow-up** starts with a 1+1 sprinkling quotient and replaces every quotient point by a four-record hidden fiber. If quotient point `i` precedes quotient point `j`, every record in fiber `i` precedes every record in fiber `j`. Internally, each fiber is either an antichain or a chain.

| family | N | `d_MM` | H | `H/(2 sqrt(N))` | `Theta_2` | `S_eff/N` | `D_dup` |
|---|---:|---:|---:|---:|---:|---:|---:|
| antichain fiber blow-up | 384 | `2.0046486296874` | 15 | `0.38273277230987157784` | `0.486756325219465709` | `0.652017600012019979` | `0.00733220530174844896` |
| chain fiber blow-up | 384 | `1.9838377498285` | 60 | `1.5309310892394863114` | `0.548913580437378619` | `0.677405684928747718` | `0.000440111043401719819` |

This is useful because it shows what is and is not dangerous. A hidden fiber can keep the quotient-looking MM scale and even a tolerable first recursive mean, but simple fibers immediately damage the 1+1 height law. Antichain fibers make chains too short; chain fibers make chains too long. So hidden thickness is not invisible once height is kept in the diagnostic set.

Second, a **distributed staging** adversary splits the reusable middle block into four independent staged reservoirs plus one chain. This lowers exact duplicate concentration:

| family | N | `d_MM` | H | `Theta_2` | `S_eff/N` | `D_dup` | mean Jaccard |
|---|---:|---:|---:|---:|---:|---:|---:|
| single reused block | 512 | `2.0652375054645` | 45 | `0.526802555243122072` | `0.0615489507716535638` | `0.874889543446244477` | `0.85910029731534583575` |
| four reservoirs | 512 | `3.6176602504202` | 45 | `0.571960393814342883` | `0.150674005619534784` | `0.204666393778141629` | `0.20066343078041194556` |

The duplicate fraction falls, as intended. But the order pays globally: most pairs in different reservoirs are incomparable, so the related-pair fraction falls to `0.137689579256360078` and the MM estimate leaves the 2D band. The overlap statistic also remains more than twice the sprinkling mean Jaccard.

The adversary lesson is sharper now:

> **[CONSTRAINED] The hard remaining adversary is not a plain fiber and not independent distributed staging. It must cross-link staged reservoirs enough to restore MM dimension and interval abundance while still hiding recursive non-manifold structure without producing load/overlap spikes.**

That is a much more specific enemy. Cross-linking is not free: adding enough relations to restore the 2D pair density changes interval sizes, creates new mixed interiors, and risks recreating the transitivity tax that Paper XXII exposed. This does not prove impossibility, but it says where the next attack has to live.

The next pass built that attack more directly.

### 9.1 Tuned mixed fibers

A plain antichain fiber makes chains too short; a plain chain fiber makes chains too long. The receipt therefore searched a bounded family of **mixed two-fiber blow-ups**: each point of a 1+1 sprinkling quotient is replaced by two records, and a deterministic selector makes some fibers chains and the rest antichains. The selector is integer-only; the winning finite candidate used `3/5`, giving an actual chain-fiber fraction `0.598958333333333333333333`.

This adversary is materially stronger than the previous ones:

| statistic | tuned mixed fiber |
|---|---:|
| N | `384` |
| related-pair fraction | `0.459081266318537859` |
| `d_MM` | `2.1131578539640458008` |
| height | `39` |
| `H/(2 sqrt(N))` | `0.99510520800566610239` |
| `Theta_2` | `0.489854632712372087` |
| `S_eff/N` | `0.694386125691969685` |
| `D_dup` | `0.000715279157560103318` |
| mean Jaccard | `0.085077747538599827391` |

This is the first adversary in the paper that makes the load/overlap tests look almost harmless. Its interval interiors are spread across the record set because every base point carries a small hidden duplicate. It is not globally staged through one reused block.

It is still visible in two ways.

First, the log-2 interval profile is shifted:

| quantity | value |
|---|---:|
| observed `H_0/N` | `3.87760416666666666666667` |
| expected `H_0/N` | `4.54616275582764753891311` |
| `H_0` ratio | `0.85294002325280432147` |
| `P_log2` ratio | `0.90810627527125956341` |

Second, it creates many records with the same causal environment. Define an **external twin pair** as a pair of records whose past and future agree after removing the two records themselves from the comparison. A fixed sprinkling at `N=384` had one accidental external-twin pair, with pair fraction `0.000013598781549173194082`. The tuned mixed fiber had `196` external-twin pairs, `191` nontrivial classes, and maximum class size `4`.

So the tuned fiber opens a new condition:

> **[CONSTRAINED] No-hidden-staging is not enough. The law also needs a no-hidden-fiber or extensionality condition: records should not come in duplicated causal roles, even when the duplicates are distributed throughout the order.**

This condition is not final. Exact twins can be broken by small decorations, so the real target is probably a soft version: near-twin causal neighborhoods, conditional fiber entropy, or an interval-kernel law that makes hidden multiplicity pay in the full recursive profile.

### 9.2 Cross-linked staged reservoirs

The receipt also tried the staged-reservoir attack directly. Each module is an `A<P<B` sandwich, but the modules are cross-linked by a 1+1 sprinkling quotient: if quotient module `i` precedes quotient module `j`, every record in module `i` precedes every record in module `j`.

A bounded grid search over module counts, middle sizes, and quotient seeds chose the best crude MM/height score. The best candidate used `9` modules, middle size `11`, and quotient seed `8108`:

| statistic | cross-linked staging |
|---|---:|
| N | `512` |
| related-pair fraction | `0.643965569960861057` |
| `d_MM` | `1.6554287940645027748` |
| height | `44` |
| `H/(2 sqrt(N))` | `0.97227182413150284605` |
| `Theta_2` | `0.84132595188654795616` |
| `S_eff/N` | `0.632271913626356651` |
| `D_dup` | `0.0208491635006332067` |
| mean Jaccard | `0.17035337750017187740` |
| module-middle histogram spike | `4.79827139704259842` |
| `P_log2` ratio | `1.5607723373551636673` |
| exact external-twin pairs | `4555` |

This candidate repairs the height scale but overshoots comparability, overorders interval interiors, keeps a visible module-middle spike, and has large twin classes. The result is not a theorem against all cross-linked staging; it is a finite no-free-lunch result for the most direct construction.

### 9.3 Decorated fibers: exact twins are brittle

Exact external twins are too brittle to be the final law. The receipt therefore follows the decoration path.

The first decorated adversary gives each quotient point two main records plus one local tag. It still reaches the broad global band:

| statistic | single-tag decorated fiber |
|---|---:|
| `d_MM` | `2.1149152711393543201` |
| `H/(2 sqrt(N))` | `0.96958968985167466387` |
| `Theta_2` | `0.466075369007271229` |
| `S_eff/N` | `0.645170377977697535` |
| mean Jaccard | `0.088203986016565514265` |
| exact external-twin pairs | `157` |
| `P_log2` ratio | `1.0880175569742347307` |

This does **not** close the exact-twin opening. It lowers exact twins only from `196` to `157`. Worse, the soft near-twin tail becomes large:

| threshold on external causal-neighborhood difference | sprinkling | single-tag decorated fiber |
|---|---:|---:|
| `<= 2` | `11` | `411` |
| `<= 4` | `35` | `417` |
| `<= 8` | `95` | `475` |
| `<= 16` | `316` | `664` |

A naive double-tag decoration also fails. It has strong global statistics, `d_MM=2.0134023329269241997` and `H/(2 sqrt(N))=1.0206207261596575409`, but adjacent local tag pairs are still external twins when the tested pair itself is removed. Exact external-twin pairs rise to `216`; the `diff<=8` near-twin count is `652`; and `P_log2` shifts to `0.89988142565079358865`.

This is an instructive failure: adding tags is not enough. The local fiber motif itself must be external-twin-free.

### 9.4 Twin-free motifs: scalar alarms can be closed

The next receipt pass uses a four-record local motif with no internal external-twin pair. It then searches seeds and selector fractions, choosing a candidate in the broad global height/MM band while minimizing exact twins.

This produces the strongest adversary in the paper:

| statistic | twin-free motif fiber |
|---|---:|
| N | `384` |
| related-pair fraction | `0.53350739773716275` |
| `d_MM` | `1.9130886247586462703` |
| height | `38` |
| `H/(2 sqrt(N))` | `0.96958968985167466387` |
| `Theta_2` | `0.518896639942437559` |
| `S_eff/N` | `0.688885691516175239` |
| `D_dup` | `0.000922722029988465975` |
| mean Jaccard | `0.10532514193840101349` |
| exact external-twin pairs | `0` |
| `P_log2` ratio | `0.98308573963087372273` |

This closes the two previous alarms: exact external twins vanish, and the log-2 scalar profile is close. But the hidden fiber is still visible in the soft near-twin tail:

| threshold on external causal-neighborhood difference | sprinkling | twin-free motif fiber | ratio |
|---|---:|---:|---:|
| `<= 2` | `11` | `578` | `48.25` |
| `<= 4` | `35` | `584` | `16.25` |
| `<= 8` | `95` | `674` | `7.03125` |
| `<= 16` | `316` | `929` | `2.9337539432176656151` |

So the best finite adversary has moved the target again:

> **[CONSTRAINED] Exact extensionality is not enough. The law needs a calibrated soft near-twin tail, or equivalently a finite-N law for the distribution of causal-neighborhood distances between records.**

### 9.5 Rich local motifs do not close the soft tail here

The next obvious move is to make each local fiber richer, so records inside the same hidden fiber differ by more than a few local relations. The receipt searches varied random local motifs of width `6`, `8`, `12`, and `16`, keeping candidates in a broad global height/MM band and selecting the one with the smallest `diff<=8` near-twin count.

The best candidate found has:

| statistic | rich random-motif fiber |
|---|---:|
| width | `6` |
| base size | `64` |
| `d_MM` | `2.0573252700396078959` |
| `H/(2 sqrt(N))` | `0.99510520800566610239` |
| `Theta_2` | `0.495559938591582113` |
| `S_eff/N` | `0.713509848696369569` |
| exact external-twin pairs | `64` |
| `diff<=8` near-twin count | `998` |
| `diff<=16` near-twin count | `1092` |
| `P_log2` ratio | `0.88291207260521286423` |

This does not beat the twin-free motif on the soft tail. It worsens `diff<=8` from `674` to `998`, still has excess `diff<=16` mass over sprinkling, and pays visible interval-profile drift. This is not an impossibility result for all rich fibers; it is the end of the finite branch tested here.

### 9.6 Coordinate jitter: the adversary starts becoming density

The next opening is more dangerous. Instead of adding more internal motif relations while keeping a complete quotient lift, let every hidden clone receive a small exact integer displacement in two 1+1 coordinates, then take the product order of the displaced points. This construction is still generated from hidden four-record clusters, but the records now have slightly different external causal neighborhoods.

With bounded jitter, no larger than one base spacing, the best broad-band candidate found is:

| statistic | bounded coordinate-jitter fiber |
|---|---:|
| N | `384` |
| jitter span/base spacing | `1.0` |
| `d_MM` | `1.9935222878608324494` |
| `H/(2 sqrt(N))` | `0.96958968985167466387` |
| `Theta_2` | `0.505849474807618903` |
| `S_eff/N` | `0.699811171178873987` |
| exact external-twin pairs | `4` |
| `P_log2` ratio | `0.98839205290919710349` |
| `diff<=8` near-twin count | `153` |
| same-hidden-cluster `diff<=8` count | `93` |

This is a real improvement over the twin-free motif: `diff<=8` drops from `674` to `153`, while scalar profiles remain strong. But it still has excess soft-tail mass over the fixed sprinkling, whose `diff<=8` count is `95`.

If the jitter is increased beyond one base spacing, the best washout candidate reaches the sprinkling soft tail:

| statistic | over-jitter washout |
|---|---:|
| jitter span/base spacing | `2.0` |
| `d_MM` | `1.8783511282397` |
| `H/(2 sqrt(N))` | `0.89304313538970034830` |
| `Theta_2` | `0.517499673022501908` |
| `S_eff/N` | `0.675113200981031486` |
| exact external-twin pairs | `0` |
| `P_log2` ratio | `1.0085069808868765099` |
| `diff<=8` near-twin count | `93` |
| same-hidden-cluster `diff<=8` count | `19` |

This is not a clean hidden-fiber victory. It matches the near-tail by letting cluster members spread far enough that they acquire ordinary coordinate individuality. The construction has started to look like a clustered, inhomogeneous 1+1 point process rather than a non-manifold quotient fiber.

This opens a follow-up branch rather than ending the campaign. The next question is whether order-only density/regularity projections can distinguish the clustered process.

### 9.7 Density regularity is not a small checklist

The receipt adds three increasingly strong density/regularity probes:

1. endpoint-load profiles for small intervals `|I(x,y)|<=0,2,8`;
2. conditional endpoint residuals after binning records by past-size and future-size quantiles;
3. sampled induced size-4 and size-5 unlabeled suborder pattern densities, calibrated against an independent sprinkling.

The first regularity-aware search optimizes the coordinate-jitter adversary against the soft tail, endpoint regularity, and global height/MM score. The best candidate remains a jittered four-record cluster construction, but now with jitter span `3.0`:

| statistic | regularity-aware cluster |
|---|---:|
| N | `384` |
| jitter span/base spacing | `3.0` |
| `d_MM` | `1.9890145938921685549` |
| height | `39` |
| `Theta_2` | `0.508102255538894192` |
| `S_eff/N` | `0.670549774522246092` |
| exact external-twin pairs | `1` |
| `P_log2` ratio | `0.98835534054519469285` |
| `diff<=8` near-twin count | `100` |
| same-hidden-cluster `diff<=8` count | `13` |
| mean Jaccard | `0.09988229213311691453` |
| p95 Jaccard | `0.38333333333333333333` |

Endpoint-load regularity does not reject it. For `k<=8`, the endpoint max/mean is `1.4951994879453808406`, while the fixed sprinkling has `1.3910121797564048719`; the whole endpoint-profile log gap is only `0.20994800275991994882`.

The conditional endpoint residual also does not reject it once finite-N variability is calibrated. The cluster's conditional residual gap is

`0.36261367215434820561`,

while an independent sprinkling-vs-sprinkling comparison gives

`0.70446455247920145541`.

Finally, sampled small induced-pattern densities are not decisive at this finite resolution:

| sampled induced pattern TV | sprinkling vs sprinkling | regularity-aware cluster |
|---|---:|---:|
| size `4` | `0.067626953125` | `0.0869140625` |
| size `5` | `0.1044921875` | `0.10888671875` |

A pattern-aware search over the top regularity candidates keeps the same candidate. This is the point where the campaign stops finding a useful next scalar diagnostic. The adversary is no longer a clean non-manifold quotient fiber; it has become an alternative finite 1+1 point process whose sampled order statistics are close to a sprinkling at the tested resolution.

So the remaining hard adversary has split again:

1. A true hidden-fiber adversary must now match the full recursive interval law and the finite-N causal-neighborhood distance distribution without smearing its fibers into coordinate individuality.
2. A clustered-coordinate adversary asks a different question: what record law distinguishes finite-density sprinkling from lumpy density modulation when endpoint loads, conditional residuals, and small induced patterns are already within finite sprinkling variability?

The honest target is no longer "add the next diagnostic." It is the full calibrated finite-dimensional law of record orders, or an action/compensator principle whose minimizers reproduce that law.

### 9.8 Projective fixed points are not enough

The collapsed continuation first asks how to find the "full law" rather than merely naming it.

The first attempt is deletion projectivity. For a fixed-N sprinkling law `Pi_N`, a uniform induced `m`-record suborder should have law `Pi_m`:

$$
C_N\sim \Pi_N,\qquad U_m\subset C_N
\quad\Longrightarrow\quad
C_N|_{U_m}\sim \Pi_m.
$$

This is true for sprinklings, but it is too geometry-blind as a finite discriminator. In the receipt, the deletion mean-signature scores are:

| object | deletion mean-signature score |
|---|---:|
| fixed sprinkling | `0.76010926263835077177` |
| regularity-aware cluster | `0.88550596841134269807` |

The separation is mild. Random subsets are not causal neighborhoods.

The sharper microscope is the causal interval:

$$
\mathcal{L}\!\left(C|_{I(x,y)}\ \middle|\ |I(x,y)|=k\right)
\approx
\Pi_k.
$$

This catches the original regularity-aware cluster:

| object | interval fixed-point score |
|---|---:|
| fixed sprinkling | `1.0322493697127026835` |
| regularity-aware cluster | `1.5459842417147670765` |

But the hostile follow-up tunes coordinate jitter. A `jitter=6/1`, `seed=16002` cluster reaches interval-only score

`0.75264159079495597304`,

below the fixed-sprinkling calibration. Mean interval profiles are therefore not the law.

Adding crude standard-deviation information gives independent information, but still does not solve the adversary:

| object | crude interval moment score |
|---|---:|
| fixed sprinkling | `7.6933830645315982293` |
| regularity-aware cluster | `6.2702887881782761517` |
| mean-tuned cluster | `5.2753504838166316761` |

The target moves from interval means to a compensated bracket law.

### 9.9 Calibrated interval brackets are stronger, but local

For a finite observable basis `f` and interval band `B`, define the compensated interval sum

$$
M_{f,B}(C)=
\sum_{x<y,\ |I(x,y)|\in B}
\left[
f\!\left(C|_{I(x,y)}\right)
-
\mathbb{E}_{\Pi_{|I(x,y)|}}f
\right].
$$

The bracket target is not only

$$
\mathbb{E}M_{f,B}=0,
$$

but also the covariance/bracket kernel

$$
\left\langle M_{f,B},M_{g,B'}\right\rangle.
$$

The interval-bracket receipt calibrates, for three interval bands, the mean and covariance of

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

Candidate interval residuals are whitened by the calibrated covariance and scored by

$$
A_B(C)=
\|\overline{Z}_B\|^2
+
\left\|
\overline{Z_BZ_B^{\mathsf T}}-I
\right\|_F^2.
$$

This is stronger than the mean tests:

| object | interval bracket action |
|---|---:|
| fixed sprinkling | `4.7228296999511580264` |
| regularity-aware cluster | `13.764332856045287563` |
| mean-tuned cluster | `5.9210952159554569934` |

Then the adversary moves again. A bracket-tuned clustered candidate with `jitter=3/1`, `seed=16003` scores

`3.1957397888444246959`,

below the search-resolution fixed sprinkling score

`4.4389592054740385182`.

It is not a clean victory for the cluster: it pays in a separate full-size whitening score. But it defeats the interval bracket as a standalone law. The next target is joint, not local.

### 9.10 Joint global-and-interval bracket calibration

The next collapsed continuation implements the five-step program: held-out null calibration, joint vector, current-enemy attack, broadened adversaries, and compression audit.

The joint observable vector contains:

- full-order observables;
- interval-band means;
- interval-band variances;
- selected interval-band covariances.

The receipt uses a 47-dimensional joint vector, trains on `56` independent sprinklings, and evaluates `16` held-out sprinklings. The held-out null scores are:

`16.0419725424`, `16.584088606`, `17.8473698121`, `17.8586633737`, `24.6363704544`, `26.0475802958`, `26.1297040769`, `26.138634025`, `28.7576344188`, `31.236422532`, `33.957155294`, `34.7463619595`, `39.554351487`, `44.2759290332`, `48.3384188466`, `86.3010074957`.

The current enemies score:

| object | joint score | held-out rank |
|---|---:|---:|
| fixed sprinkling | `39.2755586753145786` | `0.75` |
| regularity-aware cluster | `104.348497235692683` | `1.0` |
| mean-tuned cluster | `27.9731155988902569` | `0.5` |
| interval-bracket-tuned cluster | `62.249790749343648` | `0.9375` |

This is a genuine improvement over the unstable high-dimensional first pass: the original density/regularity cluster is outside the held-out maximum, while the fixed sprinkling is inside. But the tuned clusters are not eliminated. The bracket-tuned cluster is high-rank, but still inside the finite held-out support.

The broadened adversary menu adds variable-width jittered clusters, density-modulated coordinate processes, and staged sandwiches. Density-modulated and staged families are rejected very strongly:

| family | representative joint scores |
|---|---:|
| density-modulated | `820.178036436481494` to `1143.31425695252781` |
| staged sandwiches | about `52501` to `53564` |

But tuned jittered clusters remain inside the finite null. The best broadened adversary is:

| statistic | best broadened adversary |
|---|---:|
| family | `cluster_w4_j2_s16002` |
| joint score | `18.23981593188092237` |
| held-out rank | `0.25` |
| `d_MM` | `2.03576444242390146` |
| `H/(2 sqrt(N))` | `0.816496580927726033` |
| `Theta_2` | `0.484972758705003079` |
| `P_log2` ratio | `0.994593021367409348` |
| near fraction | `0.00149586597040905135` |
| hidden interval-pair fraction | `0.036179317079832039833` |

So the joint bracket field is the right **kind** of object, but this finite projection is not yet the law. It rejects some broad families and the original regularity-aware cluster; it does not reject every tuned clustered coordinate process.

The compression audit therefore does not find a closed click law. It finds the next honest target:

> **[OPEN] Calibrate a process-level joint martingale bracket field, or find a compact principle that implies it. The current finite vector is a useful projection, not the law itself.**

### 9.11 Multiscale interval-pair covariance

The next enemy after the 47-dimensional joint projection is narrower: a tuned clustered-coordinate process that matches global observables and individual interval brackets while hiding its structure in correlations between intervals. The follow-up receipt therefore tests pairs of causally selected intervals across two scales.

For each scale, the observable vector contains:

- full-order features;
- interval-band feature means;
- interval-band feature variances;
- selected covariances between interval features;
- pair topology for sampled intervals: disjoint, nested, overlapping, and shared-interior fractions.

The receipt calibrates this vector on independent 1+1 sprinklings, then scores held-out sprinklings and adversaries through the same whitened action. It uses a 59-dimensional vector at each tested scale.

For `N=192`, with bands `12-23`, `24-47`, and `48-95`, the held-out maximum is

`512.785800732762634`.

The key scores are:

| object | interval-pair score | held-out rank |
|---|---:|---:|
| fixed sprinkling | `149.853959000380944` | `0.0` |
| regularity-aware cluster | `328.815126833402873` | `0.625` |
| best joint-vector cluster | `915.005211792079009` | `1.0` |
| density-modulated process | `2092.85635649659188` | `1.0` |
| staged sandwich | `96783.1555340286799` | `1.0` |

For `N=384`, with bands `24-47`, `48-95`, and `96-191`, the held-out maximum is

`173.19016294453772`.

The key scores are:

| object | interval-pair score | held-out rank |
|---|---:|---:|
| fixed sprinkling | `213.450917598272535` | `1.0` |
| regularity-aware cluster | `235.837069764652973` | `1.0` |
| best joint-vector cluster | `94.4193077382641523` | `0.625` |
| density-modulated process | `3371.19757069306252` | `1.0` |
| staged sandwich | `66528.5013655265095` | `1.0` |

This is a real narrowing result, but not a law. Density-modulated processes and staged sandwiches are rejected strongly at both scales. The best tuned jitter cluster remains inside the held-out support at `N=384`, and the regularity-aware cluster remains inside at `N=192`. Even more importantly, the fixed fresh sprinkling at `N=384` lies above the small held-out maximum. That is not a physical failure of sprinklings; it is a finite calibration warning. The interval-pair projection is sensitive, but its finite held-out null is not stable enough to be promoted to a click law.

The target therefore sharpens again:

> **[OPEN] Replace finite multiscale interval-pair scores by an asymptotic/process-level independence and bracket principle whose finite projections include interval-pair covariance, while remaining stable on fresh sprinklings.**

### 9.12 Stability and adversarial-limit audit

The follow-up receipt separates two questions that had been mixed together:

1. Is the interval-pair projection itself calibrated stably on fresh sprinklings?
2. Can a fixed-width hidden clustered process disappear from global empirical laws as `N` grows?

The receipt first replaces the 59-dimensional interval-pair vector by a compact 32-dimensional projection:

- full-order features;
- interval-band feature means;
- interval-pair topology features.

It then trains on sprinklings, calibrates held-out sprinklings, and scores fresh probe sprinklings and the surviving jittered clusters.

| scale | held-out max | fresh probes outside max | fresh mean rank | jitter `j=2` rank | jitter `j=3` rank |
|---|---:|---:|---:|---:|---:|
| `N=192` | `56.9334818317871994` | `1/12` | `0.465277777777777778` | `0.583333333333333333` | `0.916666666666666667` |
| `N=384` | `38.0901181836020359` | `2/12` | `0.53125` | `0.791666666666666667` | `0.291666666666666667` |

The compact projection is better behaved than the previous 59-dimensional warning, but it is still not a stable null law. Fresh sprinklings leak above the held-out maximum, and jittered clusters remain inside the held-out support. The result is useful as a diagnostic, not as a completed click law.

The second part is more structural. Suppose each base record is replaced by a fixed hidden cluster of width `w`, with `N` divisible by `w`. The fraction of same-hidden-cluster pairs among all unordered pairs is

$$
\frac{(N/w)\binom{w}{2}}{\binom{N}{2}}
=
\frac{w-1}{N-1}.
$$

For `w=4`, the receipt finds:

| scale | same-cluster pair fraction | `N` times fraction | sprinkling near/root | jitter `j=2` near/root | jitter `j=2` same-near/root | hidden partners/root |
|---|---:|---:|---:|---:|---:|---:|
| `N=192` | `0.0157068062827225131` | `3.01570680628272251` | `0.395833333333333333` | `0.479166666666666667` | `0.09375` | `3.0` |
| `N=384` | `0.00783289817232375979` | `3.00783289817232376` | `0.458333333333333333` | `0.572916666666666667` | `0.213541666666666667` | `3.0` |

This is the most important negative lesson in the collapsed continuation. Any purely unrooted global pair statistic sees the fixed-width hidden cluster with mass `O(1/N)`. In the limit, that mass vanishes. But a rooted record still has `w-1` hidden partners. For `w=4`, each record has three hidden partners at every `N`.

Therefore a final law cannot be only an unrooted empirical law over record pairs or finite interval-pair averages. It needs a rooted/Palm component: what a typical record sees in its conditional causal neighborhood, not only what a random pair sees globally.

The target sharpens again:

> **[OPEN] The click law should imply a rooted/Palm process-level bracket law. Global finite-dimensional projections are necessary shadows, but fixed-width hidden multiplicity is asymptotically invisible to them.**

### 9.13 First rooted/Palm bracket audit

The next receipt tests the rooted idea directly. It samples a root record first, then computes order-only rooted features:

- past, future, and comparable fractions of the root;
- counts and soft sums of small external-neighborhood distances `Delta_C(root,y)`;
- relation fraction inside the near-root set;
- interval-through-root count, size, exponential-size weight, and recursive-content summaries.

The rooted vector has dimension `36`: four global features plus rooted feature means and variances over sampled roots. At `N=384`, the held-out sprinkling scores range from

`9.159269225560362`

to

`63.6954883587196324`.

Eight fresh probe sprinklings all stay inside the held-out maximum:

| probe result | value |
|---|---:|
| fresh probes outside held-out max | `0/8` |
| largest fresh-probe rank | `0.9375` |

So this rooted score is better calibrated than the previous interval-pair projections. But the hostile width sweep does not give the hoped-for rejection. With jitter `2/1`, all tested hidden widths remain inside the held-out support:

| hidden width | rooted score | held-out rank | score/max | global same-cluster pair mass | rooted hidden partners |
|---|---:|---:|---:|---:|---:|
| `2` | `32.6797712162481854` | `0.75` | `0.513062574105760323` | `0.00261096605744125326` | `1` |
| `4` | `25.2537516184405674` | `0.5625` | `0.39647630105631241` | `0.00783289817232375979` | `3` |
| `8` | `18.4099533393204091` | `0.375` | `0.289030727508350557` | `0.0182767624020887728` | `7` |
| `16` | `35.7207091432336475` | `0.8125` | `0.560804384481081373` | `0.039164490861618799` | `15` |

The receipt then follows the opening by measuring the hidden construction labels against the order-only near-twin relation. The result is decisive:

| hidden width | mean same-label `Delta/N` | same-label fraction with `Delta <= tau` |
|---|---:|---:|
| `2` | `0.0233832465277777778` | `0.489583333333333333` |
| `4` | `0.0966887297453703704` | `0.0711805555555555556` |
| `8` | `0.312786768353174603` | `0.00818452380952380952` |
| `16` | `0.527204499421296296` | `0.000347222222222222222` |

The label "same hidden cluster" is not the same thing as an order-visible near twin once jitter diversifies the causal neighborhoods. At width `16`, each root has fifteen hidden construction partners, but essentially none of those same-label pairs look near under the order-only `Delta <= tau` test.

That changes the interpretation. Rooted/Palm laws are still necessary because unrooted pair mass can vanish. But a finite rooted score cannot be expected to reject labels that have become invisible to the order. If the hidden label has washed out into an ordinary clustered coordinate process, then the remaining target is not "find the hidden label"; it is to distinguish the induced order distribution from the sprinkling order distribution by process-level density, interval, and rooted bracket laws.

The target sharpens again:

> **[OPEN] A rooted/Palm click law must be order-visible. It can penalize hidden multiplicity only when that multiplicity leaves a rooted causal signature. Otherwise the adversary has become a clustered point-process law, not a hidden-label law.**

### 9.14 Order-only Mecke/Palm compensator audit

The next receipt tests a closer order-only shadow of the Poisson Mecke/Slivnyak identity. Instead of only sampling a rooted neighborhood, it samples a root `x`, deletes it, and measures the add-one/delete-one increment of global and interval observables.

For an observable `F`, define the deletion increment

$$
D_xF(C)=F(C)-F(C\setminus\{x\}).
$$

The receipt builds a 32-dimensional vector from:

- full-order features of `C`;
- means over sampled roots of root degree, near-root tail, through-root interval features, and scaled `D_xF(C)`;
- variances of the same rooted deletion-increment features.

This is not a proof of the Mecke identity. It is a finite order-only projection of the kind of compensator a Poisson-like click law would have to imply.

At `N=192`, the held-out sprinkling scores range from

`1.167967153461788`

to

`5.7513943937404028`.

Fresh sprinklings have one leakage above the held-out maximum:

| probe result | value |
|---|---:|
| fresh probes outside held-out max | `1/8` |
| largest fresh-probe rank | `1.0` |

The adversarial scores are:

| process | Mecke score | held-out rank | score/max |
|---|---:|---:|---:|
| width `2`, jitter `2/1` | `2.55781381074199101` | `0.25` | `0.444729336163386311` |
| width `4`, jitter `2/1` | `3.23751590887159032` | `0.5` | `0.562909737575148478` |
| width `8`, jitter `2/1` | `3.12347962494818626` | `0.416666666666666667` | `0.543082148626020458` |
| width `16`, jitter `2/1` | `1.9434008336406129` | `0.166666666666666667` | `0.337900811628521924` |
| density-modulated/Cox-like | `33.7776737294004683` | `1.0` | `5.87295382945095778` |

This is informative in both directions. The deletion-increment score strongly rejects the gross density-modulated/Cox-like process. That is evidence that a Mecke/Palm compensator is the right kind of object. But it still does not reject the jittered width sweep. That is evidence that this finite deletion-increment projection is not the compensator itself.

The target sharpens again:

> **[OPEN] The click law should imply an asymptotic order-only Mecke/Palm compensator. A finite deletion-increment score is a useful shadow, but jittered clustered orders can still pass it.**

### 9.15 Asymptotic jittered-cluster limit audit

The next receipt stops asking which finite score catches the jittered cluster and asks the sharper question:

> Does the jittered clustered process converge to the same order law as 1+1 sprinkling, or does an order-visible asymptotic difference remain?

The receipt uses exact full three-record induced-pattern densities, not sampled pattern one-offs. For every audited finite order it exactly partitions all triples into:

$$
\{\text{antichain},\ \text{one relation},\ \vee,\ \wedge,\ \text{chain}\}.
$$

It combines those exact triple densities with global pair density, height ratio, log-2 interval-profile ratio, and rooted near-neighborhood features. It calibrates against finite sprinklings at `N=192`, `384`, and `768`, then tests width-4 clustered coordinate processes at jitter levels `0`, `1`, `2`, and `4`.

The score ratios below are candidate score divided by the largest held-out sprinkling score at the same `N`:

| scale | jitter `0` | jitter `1` | jitter `2` | jitter `4` |
|---|---:|---:|---:|---:|
| `N=192` | `64.5674432581865983` | `0.923716359177636794` | `0.649193115167048403` | `0.457950054716355159` |
| `N=384` | `132.470143298030305` | `0.638887377979625904` | `0.729212362577668174` | `0.631399885471121033` |
| `N=768` | `825.53304997401892` | `79.0368329859556805` | `59.6241746968675181` | `17.7158721626271524` |

The same-label near-twin visibility for the highest jitter is:

| scale | jitter `4`, same-label fraction with `Delta <= tau` |
|---|---:|
| `N=192` | `0.00347222222222222222` |
| `N=384` | `0.0121527777777777778` |
| `N=768` | `0.0477430555555555556` |

The leading separating components at `N=768`, jitter `4`, are rooted softness and exact triple densities:

| component | z-score |
|---|---:|
| `root_soft` | `10.1846` |
| `tri_antichain` | `8.94524` |
| `tri_chain` | `-8.87069` |

This is the first pass where the surviving jittered enemy stops looking merely finite-score evasive. Low jitter is strongly order-visible at every tested scale. Higher jitter can sit inside the finite null at `N=192` and `N=384`, but at `N=768` even jitter `4` separates by a factor `17.7158721626271524` over the held-out maximum.

The result is not yet a theorem. The calibration sample is small, the score is finite, and the jitter schedule is not an asymptotic classification. But the direction is important: the surviving adversary may not converge to the sprinkling order law. It may only look acceptable at small finite scale.

The target sharpens again:

> **[OPEN] Establish the phase boundary for clustered coordinate processes. Determine whether high-jitter clusters converge to the sprinkling poset limit or retain persistent exact-pattern/rooted signatures.**

### 9.16 Jitter scaling phase diagram

The next receipt makes the phase-boundary question explicit. It writes:

$$
P_N=\text{the 1+1 sprinkling order law at }N,
$$

and

$$
Q_N(w,j)=\text{the width-}w\text{ jittered clustered coordinate order law}.
$$

It fixes `w=4`, tests `N=192,384,768`, and varies the effective jitter scale. The audit again uses exact full three-record pattern densities, global interval-profile features, and rooted near-neighborhood features.

The tested phases are:

- **separated:** score/held-out max `>10`;
- **visible:** score/held-out max between `1` and `10`;
- **finite camouflage:** score/held-out max `<=1` and same-label near-twin visibility is low.

The phase table is:

| scale | locked `eff=0` | micro `eff=1` | unit `eff=4` | two `eff=8` | four `eff=16` | eight `eff=32` |
|---|---:|---:|---:|---:|---:|---:|
| `N=192` | `185.647284771408768` separated | `33.0371501903442091` separated | `2.78137579332244368` visible | `0.999542905842280286` finite camouflage | `2.41853099926250549` visible | `3.82501958706619368` visible |
| `N=384` | `67.5210000259177625` separated | `10.6421740975151475` separated | `0.568462699451713825` finite camouflage | `0.462444383365001546` finite camouflage | `0.953683644866992542` finite camouflage | `0.628482562333958312` finite camouflage |
| `N=768` | `147.785128252377258` separated | `37.5806990426462951` separated | `8.99013501344866665` visible | `3.56135548449755408` visible | `1.25395804452970841` visible | `0.812024119200680201` finite camouflage |

Same-label near-twin visibility decreases monotonically with jitter at each tested scale. For example:

| scale | locked | micro | unit | two | four | eight |
|---|---:|---:|---:|---:|---:|---:|
| `N=192` | `1.0` | `0.607638888888888889` | `0.0902777777777777778` | `0.0104166666666666667` | `0.0104166666666666667` | `0.0` |
| `N=384` | `1.0` | `0.960069444444444444` | `0.161458333333333333` | `0.0347222222222222222` | `0.00520833333333333333` | `0.00347222222222222222` |
| `N=768` | `1.0` | `1.0` | `0.421006944444444444` | `0.129340277777777778` | `0.0416666666666666667` | `0.0164930555555555556` |

This is the cleanest finite picture so far:

1. Locked hidden fibers are strongly order-visible at every tested scale.
2. Moderate/high jitter can produce finite camouflage at small or intermediate `N`.
3. The same fixed-jitter family can reappear at larger `N` as an exact-pattern/rooted defect.
4. No tested fixed-jitter schedule proves full washout across all scales.

The target sharpens again:

> **[OPEN] Prove a scaling theorem for `Q_N(w,j_N)` versus `P_N`: identify the critical jitter curve separating hidden-fiber, finite-camouflage, washout, and density-distortion/order-visible phases.**

### 9.17 Exponent audit: fixed, square-root, and weakly linear jitter

The phase diagram still left a major ambiguity. The phrase "jitter `4`" is not scale invariant. In this clustered coordinate construction the effective jitter is a rank-mixing radius: it says how many base ranks a hidden cloud can blur in each coordinate. The next receipt therefore varies not only raw jitter, but its scaling with `N`.

The receipt tests:

$$
j_N\in\{4,\ 16,\ \tfrac{1}{2}\sqrt{N},\ \sqrt{N},\ 2\sqrt{N},\ N/24\},
$$

rounded to integer effective rank-mixing radii, at:

$$
N\in\{192,384,768\},\qquad w\in\{2,4,8\}.
$$

It uses the same exact three-record pattern densities, global interval-profile features, and rooted external-neighborhood features as the preceding phase diagram.

At the largest tested scale `N=768`, the score ratios are:

| width | fixed `4` | fixed `16` | `sqrt(N)/2` | `sqrt(N)` | `2 sqrt(N)` | `N/24` |
|---|---:|---:|---:|---:|---:|---:|
| `w=2` | `2.0355009967482677` | `0.252834395832052002` | `1.02182879557802006` | `0.384596543937087152` | `1.35330798247621762` | `0.767776022941816446` |
| `w=4` | `2.35791476695236683` | `0.729504871166092471` | `1.10645612286559992` | `0.79270628828558056` | `0.699258088178154223` | `0.0867219071151043737` |
| `w=8` | `5.65777540835656975` | `0.342472083251988443` | `0.169803951680729394` | `0.230684165809339607` | `0.184645244483497477` | `0.180594912114668768` |

The main lesson is negative and useful:

1. Fixed small jitter is still order-visible at the largest tested scale for all tested widths.
2. Larger fixed or square-root-scale jitter can enter finite camouflage.
3. Wider hidden clouds do not simply make the defect easier to see; at high jitter, they can become more camouflaged in this finite projection.
4. No single raw jitter threshold or exponent threshold classifies the phase boundary.

The natural theorem target must therefore be formulated for:

$$
Q_N(w_N,j_N),
$$

not only fixed `w`, fixed `j`, or a fixed exponent family. The control variables should include hidden width, rank-mixing radius, density regularity, and the rooted/Palm order-visible neighborhood law.

> **[OPEN] Replace the finite phase diagram by a no-go or classification theorem for clustered coordinate limits `Q_N(w_N,j_N)`. The theorem must decide whether any scaling window has the same process-level order law as sprinkling, or whether every nontrivial hidden cluster leaves a rooted/Palm, Mecke, exact-pattern, density-regularity, or interval-bracket residue.**

### 9.18 Linear and superlinear washout

The next hostile opening is that a hidden clustered generator might become physically irrelevant if the induced record order has washed out to the ordinary sprinkling law. A click law over records should penalize order-visible clustering, not unobservable implementation history.

The washout receipt therefore tests rank-mixing radii:

$$
j_N\in\{4,\ 2\sqrt{N},\ N/24,\ N/12,\ N/6,\ N/3,\ N,\ 2N\},
$$

again for:

$$
N\in\{192,384,768\},\qquad w\in\{2,4,8\}.
$$

At the largest tested scale `N=768`, the single-sample score ratios are:

| width | fixed `4` | `2 sqrt(N)` | `N/24` | `N/12` | `N/6` | `N/3` | `N` | `2N` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `w=2` | `2.0355009967482677` | `1.35330798247621762` | `0.767776022941816446` | `0.712609250488918664` | `0.677615645656232304` | `0.968352474528171442` | `0.0957022725377258681` | `0.0889724684538083258` |
| `w=4` | `2.35791476695236683` | `0.699258088178154223` | `0.0867219071151043737` | `0.325184345380150157` | `0.388997667852217613` | `0.13255223398430263` | `0.211214411938198395` | `0.843394256644370274` |
| `w=8` | `5.65777540835656975` | `0.184645244483497477` | `0.180594912114668768` | `0.0458456632859939301` | `0.272037644393034647` | `0.150065767606287882` | `0.24129877130679627` | `0.178321288869572072` |

For `linear_1` and `super_2` at `N=768`, the mean same-label near-twin visibility is already negligible:

| width | `N` mixing | `2N` mixing |
|---|---:|---:|
| `w=2` | `0.0` | `0.0` |
| `w=4` | `0.0` | `0.000868055555555555556` |
| `w=8` | `0.000744047619047619048` | `0.000372023809523809524` |

The main interpretation is not "linear jitter always solves it." It is sharper:

1. Fixed small jitter remains order-visible at `N=768`.
2. Linear-scale mixing can erase same-label near twins and enter finite camouflage.
3. Increasing the mixing radius is not a monotone guarantee of better finite match.
4. If a hidden generator washes out so completely that only the sprinkling order law remains, then it is no longer an order-visible non-manifold adversary. The click law should be stated on the induced record law.

### 9.19 Two-sample washout distance

The preceding washout audit still used one candidate order at a time. The next receipt compares empirical laws. It calibrates the exact-pattern/rooted/global feature coordinates on repeated sprinklings and computes a finite law distance between two empirical clouds using both feature means and feature spreads.

For `N=768`, the two-sample law-distance ratios are:

| width | fixed `4` | `N` mixing | `2N` mixing |
|---|---:|---:|---:|
| `w=2` | `3.64619684033923609` | `0.976921613467883239` | `0.680853841587154671` |
| `w=4` | `5.30666394469903272` | `1.20755058169404669` | `1.58871759590512852` |
| `w=8` | `4.80166196533886906` | `0.962510703528528136` | `1.04709353166174651` |

This is the best finite split so far:

1. Fixed small jitter is robustly two-sample visible.
2. Some large-mixing clustered generators are inside the empirical sprinkling null under this finite law-distance projection.
3. Some large-mixing clustered generators remain visible.
4. The hidden label signal is gone in all large-mixing cases, so any remaining distinction must be a distinction of the induced order law itself.

The theorem target is now a classification rather than a pure rejection theorem:

$$
Q_N(w_N,j_N)\Rightarrow P
$$

only in windows where the induced order law converges to the sprinkling poset law `P`; otherwise the clustered process must leave an order-visible residue in rooted/Palm, Mecke, exact-pattern, density-regularity, interval-bracket, or higher finite-dimensional statistics.

> **[OPEN] Prove a dichotomy for clustered coordinate generators: either the hidden structure washes out and the induced record law converges to sprinkling, or an order-visible residue persists.**

### 9.20 Proved part of the washout/residue dichotomy

This section records the part of the dichotomy that can actually be proved cleanly from the clustered-coordinate model. It does not classify the linear window where the finite receipts live.

Let:

$$
N=m_N w_N
$$

and define the clustered coordinate generator `Q_N(w_N,J_N)` as follows. A base permutation `\pi` on `m_N` points is chosen. For each base point `b`, create `w_N` records:

$$
U_{b,a}=b+\xi_{b,a},\qquad
V_{b,a}=\pi(b)+\eta_{b,a},
$$

where the jitters are independent, continuous, and supported on an interval of rank radius `J_N`. The record order is:

$$
(b,a)\prec(c,d)
\quad\Longleftrightarrow\quad
U_{b,a}<U_{c,d}\ \text{and}\ V_{b,a}<V_{c,d}.
$$

Let `P_N` denote the ordinary `1+1` sprinkling order law, equivalently the law induced by two independent random coordinate orders.

For two records `x,y`, keep the external-neighborhood distance:

$$
\Delta_C(x,y)=
\left|(P_x\setminus\{y\})\triangle(P_y\setminus\{x\})\right|
+
\left|(F_x\setminus\{y\})\triangle(F_y\setminus\{x\})\right|.
$$

**Theorem 23.1, residue regime.**  
Assume `w_N\ge 2`, `w_N=O(1)`, and:

$$
w_NJ_N=o(\sqrt N).
$$

Then there is an order-only rooted/Palm threshold `\tau_N` such that:

$$
w_NJ_N\ll \tau_N\ll \sqrt N,
$$

and a typical record under `Q_N(w_N,J_N)` has a same-hidden-cluster partner `y` with:

$$
\Delta_C(x,y)\le \tau_N
$$

with probability tending to `1`, while a typical record under `P_N` has no such partner with probability tending to `1`. Therefore this regime leaves an order-visible rooted/Palm residue.

One explicit witness is:

$$
\tau_N=\sqrt{w_NJ_N\sqrt N}.
$$

The conditions give:

$$
\frac{w_NJ_N}{\tau_N}\to 0,
\qquad
\frac{\tau_N^2}{N}\to 0.
$$

**Proof.**  
Two records in the same hidden cluster have coordinate centers equal before jitter. Their coordinate separation is therefore `O(J_N)` in each rank coordinate. A third record can distinguish their past/future relation only if its `U` rank or `V` rank lies in one of the coordinate strips swept out by that separation. The expected number of such distinguishing records is `O(w_NJ_N)`, and standard binomial concentration gives:

$$
\Delta_C(x,y)=O_p(w_NJ_N).
$$

Thus `\Delta_C(x,y)\le\tau_N` with probability tending to `1`.

For an ordinary sprinkling, a record `y` satisfying `\Delta_C(x,y)\le\tau_N` must lie within a coordinate neighborhood of rank radius `O(\tau_N)` around `x`. The expected number of such records is:

$$
O\!\left(\frac{\tau_N^2}{N}\right),
$$

which tends to `0`. Markov's inequality then gives the claimed Palm separation. The unrooted same-cluster pair mass is only:

$$
\frac{\#\{\text{same-hidden-cluster pairs}\}}{\binom N2}
=
\frac{w_N-1}{N-1},
$$

so the residue is genuinely rooted/Palm rather than a macroscopic pair-density defect.

**Theorem 23.2, strong washout regime.**  
Assume `w_N=O(1)` and:

$$
J_N\gg N^2/w_N.
$$

Then the full finite record-order law of `Q_N(w_N,J_N)` converges in total variation to `P_N`.

**Proof.**  
Compare the jittered coordinates to a noise-only model in which:

$$
U'_{b,a}=\xi_{b,a},\qquad V'_{b,a}=\eta_{b,a}.
$$

The noise-only model has independent continuous `U'` and `V'` coordinates, so its induced order is exactly `P_N`. In `Q_N`, the `U` coordinate of any record is translated by at most `m_N`, and the `V` coordinate is also translated by at most `m_N`. For a uniform jitter interval of radius `J_N`, the one-coordinate total-variation cost of such a translation is `O(m_N/J_N)`. Tensorizing over `N` records and two coordinates gives:

$$
d_{\mathrm{TV}}\!\left(Q_N(w_N,J_N),P_N\right)
\le
C\,\frac{N m_N}{J_N}
=
C\,\frac{N^2}{w_NJ_N}.
$$

The right-hand side tends to zero under the displayed condition. Since the order is a measurable function of the coordinates, the same total-variation bound applies to the induced order law.

**Fixed-k washout.**  
The full-record total-variation condition is deliberately strong. For any fixed number `k` of sampled records, the weaker condition:

$$
\frac{m_N}{J_N}\to 0
$$

already makes the base centers negligible relative to the jitter. Thus the fixed-k induced order law converges to the `k`-record sprinkling law. This is why finite unrooted pattern densities are too weak: for bounded hidden width they can wash out even while rooted/Palm information remains.

**Critical window.**  
The theorem leaves a real middle window:

$$
w_NJ_N\not=o(\sqrt N),
\qquad
J_N\not\gg N^2/w_N.
$$

The finite audits live precisely in this window. In particular, linear mixing `J_N\asymp N` is not covered by the residue witness and is far from the sufficient full-record total-variation washout bound. This matches the receipts: some linear/superlinear families look washed out in finite empirical law distance; others remain visible.

So the proved statement is a partial dichotomy with an exposed critical window:

1. Below the microscopic Palm scale, hidden clusters leave a rooted/Palm residue.
2. Above the strong product-TV washout scale, the full record law is sprinkling.
3. The linear and near-linear regimes require a sharper theorem.

### 9.21 Linear critical-kernel theorem

The next theorem explains why the linear window cannot be solved by another fixed finite-pattern checklist.

Assume bounded hidden width:

$$
w_N=O(1),
$$

and linear rank mixing:

$$
\frac{J_N}{m_N}\to L\in(0,\infty).
$$

Equivalently, since `N=m_Nw_N`, this is:

$$
J_N\asymp N.
$$

**Theorem 23.3, fixed unrooted patterns wash out in the linear window.**  
For every fixed `k`, the unrooted `k`-record induced-order law of `Q_N(w_N,J_N)` converges to the `k`-record `1+1` sprinkling law.

**Proof.**  
The probability that a fixed `k`-sample contains two records from the same hidden cluster is at most:

$$
\binom{k}{2}\frac{w_N-1}{N-1},
$$

which tends to `0`. Conditional on no hidden-cluster collision, the sampled records have distinct base points. Their two base coordinate ranks are asymptotically independent random samples from a random permutation. Adding independent continuous jitter preserves independence between the `U` and `V` coordinate rankings and removes ties. Therefore the two coordinate rankings of the sampled records converge to two independent uniform permutations of `k` labels. That is exactly the `k`-record `1+1` sprinkling order law.

For example, the three-record law is:

$$
\Pr(\text{antichain})=\frac16,\qquad
\Pr(\text{one relation})=\frac13,\qquad
\Pr(\vee)=\Pr(\wedge)=\Pr(\text{chain})=\frac16.
$$

The pair relation probability is:

$$
\Pr(x\prec y)=\Pr(U_x<U_y)\Pr(V_x<V_y)=\frac12\cdot\frac12=\frac14.
$$

Thus no fixed unrooted finite-dimensional pattern law can distinguish the bounded-width linear critical window from sprinkling.

**Same-cluster labels are also not microscopic near twins.**  
When `L>0`, two records in the same hidden cluster have independent jitter differences of order `J_N`, hence coordinate-rank gaps of order one with positive probability. Consequently their external-neighborhood distance is typically order `N`, not `o(N)`. The microscopic rooted/Palm near-twin statistic that works in the low-jitter residue regime is no longer the right witness.

This is the important narrowing:

1. fixed unrooted finite patterns wash out;
2. microscopic rooted near-twins wash out;
3. hidden labels are not record observables unless they leave another order-visible trace;
4. any remaining distinction must be mesoscopic, full-law, boundary-sensitive, marked/compensated, or martingale-bracket based.

### 9.22 Critical-window mesoscopic interval and load-bracket audits

The next tempting move is to replace fixed finite patterns by mesoscopic interval statistics. The first receipt tests a sampled interval-size law. For sampled comparable endpoints `x<y`, it records:

$$
\frac{|I(x,y)|}{N},
$$

then compares relation density, moments, quantiles, and low/high interval-mass features against a repeated sprinkling null.

This helps at the smaller tested scale but does not survive as a classifier. At `N=384`, one tested linear-window family is visible:

$$
w=8,\qquad J_N=N,\qquad \mathrm{score/null}=1.46499376027173406.
$$

But at `N=768`, every tested interval-size projection is inside the finite null. The largest ratio is only:

$$
w=2,\qquad J_N=N/2,\qquad \mathrm{score/null}=0.958659265823868755.
$$

So the failure is not "we need a few more moments." The interval-size law, even with mesoscopic fluctuations, can wash out in the linear window.

The follow-up receipt adds an order-visible load/bracket field. For a sampled family of intervals `\mathcal S`, define the record load

$$
L_z=\#\{(x,y)\in\mathcal S: z\in I(x,y)\},
$$

and the band loads

$$
L_z^{(b)}=\#\{(x,y)\in\mathcal S_b: z\in I(x,y)\},
$$

where the bands are small, medium, and large interval interiors. The finite vector includes load variance, quantiles, maximum load, effective support, top-mass concentration, and sampled interval-overlap topology. This is still not a full bracket law, but it is closer to one because it asks how interval interiors fluctuate across records, not only how large they are.

The result is mixed and useful. At `N=768`, the 38-dimensional load/bracket projection recovers one marginal visible family:

$$
w=4,\qquad J_N=2N,\qquad \mathrm{score/null}=1.03424395062355414.
$$

The largest components are load-tail and small-band load fluctuations:

$$
\texttt{load\_max},\quad
\texttt{small\_load\_q90},\quad
\texttt{load\_q99},\quad
\texttt{small\_load\_var}.
$$

But many `N=768` linear-window families remain inside the finite null, for example:

$$
w=4,\qquad J_N=N,\qquad \mathrm{score/null}=0.540923137561183658,
$$

and

$$
w=8,\qquad J_N=N,\qquad \mathrm{score/null}=0.682372813722619811.
$$

This is the narrowest target so far:

1. fixed unrooted finite patterns provably wash out;
2. interval-size mesoscopic moments can wash out at the larger tested scale;
3. finite load/bracket fields recover only a weak partial signal;
4. the remaining question is whether the induced **process-level** order law has the same martingale/Palm/Mecke bracket as sprinkling.

If a clustered construction has the same process-level bracket law, then it is not a hidden-fiber counterexample at the record level; it has washed out into the same observable order process. If it does not, the witness is not likely to be a scalar or finite checklist. It should be a limiting bracket, Palm, or deletion-increment identity.

### 9.23 Observable hidden-label information audit

The previous section leaves a conceptual danger: maybe a hidden cluster should be rejected merely because a hidden construction label exists. That is too strong. A label that is not recoverable from the record order is not an observable defect of the record law.

The next receipt therefore asks a narrower question:

> Given only the transitive order, can one distinguish same-hidden-cluster pairs from different-cluster pairs?

It uses balanced samples of same-label and different-label pairs. For each pair `{x,y}`, it computes only order-visible features:

$$
\Delta_C(x,y)=
\left|(P_x\setminus\{y\})\triangle(P_y\setminus\{x\})\right|
+
\left|(F_x\setminus\{y\})\triangle(F_y\setminus\{x\})\right|,
$$

past and future Jaccard overlaps, causal-neighborhood agreement, comparability, and interval size if comparable. No black-box classifier is trained. For each single feature, the receipt computes the best orientation AUC against the hidden same-label/different-label split. The baseline is a true sprinkling with random pseudo-labels of the same width.

At `N=768`, `w=4`, the pseudo-label null gives:

$$
\mathrm{mean\ best\ separability}=0.524984931945800781,
\qquad
\mathrm{max}=0.555891036987304688.
$$

The receipt uses a conservative finite guard:

$$
0.555891036987304688+0.05
=0.605891036987304687.
$$

The hidden-label results are:

| schedule | mean best separability | interpretation |
|---|---:|---|
| locked `J=0` | `1.0` | visible residue |
| fixed `J=4` | `0.976752853393554687` | visible residue |
| square-root `J=floor(sqrt(N))` | `0.632798576354980469` | marginal visible residue |
| linear half `J=N/2` | `0.527651023864746094` | pseudo-label-like |
| linear one `J=N` | `0.520104789733886719` | pseudo-label-like |
| linear two `J=2N` | `0.521009635925292969` | pseudo-label-like |

The best low-jitter feature is external causal-neighborhood difference. In the linear schedules, the best feature changes from replicate to replicate and stays inside pseudo-label fluctuation.

So the receipt supports the lateral/information-theoretic version of the target:

1. a hidden implementation label is not automatically a record-law defect;
2. low-jitter hidden clusters leave order-visible label information and should be penalized;
3. in the tested linear schedules, the hidden label washes out in this pair-feature projection;
4. the remaining question is whether some higher order-visible process statistic still distinguishes the linear-window law from sprinkling.

In information-theory language, the desired theorem should not say "hidden variables are forbidden." It should say:

$$
\text{observable label information vanishes}
\quad\text{or}\quad
\text{an order-visible residue exists.}
$$

That is the right form of the washout/residue dichotomy.

### 9.24 Higher-order hidden-label residue audit

The next hostile opening is immediate: maybe same-hidden-label pairs are pseudo-label-like, but same-hidden-label triples still carry the hidden residue.

The higher-order receipt tests this at `N=768`, `w=4`. It compares all-same-label triples against all-distinct-label triples using only order-visible triple features:

- relation count and three-record height;
- mean, minimum, maximum, and variance of pairwise external-neighborhood differences;
- pairwise past/future Jaccard means;
- triple common-past and common-future Jaccard scores;
- interval-size mean and maximum across the comparable pairs inside the triple.

Again, no black-box classifier is trained. The statistic is the best single-feature AUC, calibrated against a sprinkling with random pseudo-labels.

The pseudo-label triple null gives:

$$
\mathrm{mean\ best\ separability}=0.540044148763020833,
\qquad
\mathrm{max}=0.5662841796875,
\qquad
\mathrm{guard}=0.6162841796875.
$$

The clustered schedules give:

| schedule | mean best triple separability | interpretation |
|---|---:|---|
| locked `J=0` | `1.0` | visible residue |
| fixed `J=4` | `0.998500823974609375` | visible residue |
| square-root `J=floor(sqrt(N))` | `0.693152109781901042` | visible residue |
| linear half `J=N/2` | `0.544464111328125` | pseudo-label-like |
| linear one `J=N` | `0.539515177408854167` | pseudo-label-like |
| linear two `J=2N` | `0.538472493489583333` | pseudo-label-like |

This result is narrower than the pair audit but points the same way. The boundary in this projection sits between square-root and linear rank mixing. Linear schedules that were pair-invisible do not become visible again through these same-label triple features.

The consequence is negative but valuable:

> **[CONSTRAINED] If the linear-window clustered law still differs from sprinkling, the residue is not captured by simple same-hidden-label pair or triple observability. It must be rooted, interval-based, mesoscopic, deletion-increment based, or genuinely process-level.**

### 9.25 Observable-law metric and degree-covariance campaign

The next step is to make the word "indistinguishable" less vague. The receipt defines a finite observable-law projection distance:

$$
D_{\Phi,N}(\mu,\nu)
=
\left\|
\mathrm{Profile}\bigl(Z_{\Phi,N}(\mu)\bigr)
-
\mathrm{Profile}\bigl(Z_{\Phi,N}(\nu)\bigr)
\right\|,
$$

where `\Phi` is a 46-dimensional order-visible feature map, `Z_{\Phi,N}` is z-calibrated on repeated `1+1` sprinklings, and the profile contains feature means and spreads. The feature map includes:

- global relation density, height scale, recursive interval density, and log-2 interval profile;
- sampled interval-size, load, effective-support, and overlap features;
- rooted past/future degree, nearest-neighborhood, through-root interval-size, and through-root overlap features.

This is not a full metric on record laws. It is a concrete scaffold for the metric the theorem needs.

At `N=768`, `w=4`, the sprinkling null has:

$$
\max D_{\Phi,N}(\text{sprinkling split},\text{sprinkling split})
=3.7792722868947745.
$$

The clustered schedules score as:

| schedule | score/null | phase |
|---|---:|---|
| fixed `J=4` | `1.44038658269306445` | visible |
| square-root `J=floor(sqrt(N))` | `1.00326969267651185` | marginal visible |
| linear half `J=N/2` | `0.978544975839934245` | camouflage |
| linear one `J=N` | `0.880571672298325785` | camouflage |
| linear two `J=2N` | `0.829118899870470496` | camouflage |

The visible fixed-jitter components are mainly load variance and rooted through-interval variance. The linear schedules show their largest shifts in rooted through-interval overlap and rooted degree tails, but the calibrated sprinkling spread still absorbs them.

The next lateral opening is degree covariance. Even if hidden partners are not near twins, they share a latent coordinate center; maybe the record order can see that through past/future degrees. The receipt tests pair and triple degree-covariance label classifiers against pseudo-label nulls.

For pseudo-labels at `N=768`, `w=4`:

$$
\mathrm{pair\ guard}=0.580689663357204861,
\qquad
\mathrm{triple\ guard}=0.589360894097222222.
$$

The degree-covariance results are:

| schedule | pair mean | triple mean | interpretation |
|---|---:|---:|---|
| fixed `J=4` | `0.902281549241807726` | `0.974098629421657986` | visible |
| square-root `J=floor(sqrt(N))` | `0.600239329867892795` | `0.656438191731770833` | visible |
| linear half `J=N/2` | `0.521217770046657986` | `0.533367580837673611` | pseudo-label-like |
| linear one `J=N` | `0.51907401614718967` | `0.528164757622612847` | pseudo-label-like |
| linear two `J=2N` | `0.516564369201660156` | `0.527008480495876736` | pseudo-label-like |

The best low-jitter degree feature is a past/future cross-degree difference; the best triple feature is the variance of the time-degree `past-future`. Both vanish to pseudo-label scale in the tested linear schedules.

This completes the finite-feature campaign in the intended sense:

1. fixed finite patterns wash out in the linear window by theorem;
2. pair hidden-label observability washes out in finite receipts;
3. triple hidden-label observability washes out in finite receipts;
4. combined global/rooted/interval/load-bracket projection does not recover linear residue;
5. degree covariance also does not recover linear residue.

The paper should therefore stop treating "find another finite feature" as the best next move. The next meaningful object is asymptotic:

> **[OPEN] Prove either contiguity/washout of `Q_N(w,J_N)` to sprinkling in the bounded-width linear window, or exhibit a limiting rooted/Palm/Mecke/bracket identity that separates them.**

### 9.26 Asymptotic marked bracket identity and order-only bracket shadow

The finite campaign failed to extract a linear-window residue from order-only feature vectors. The next honest move is asymptotic. The receipt starts with a marked one-dimensional coordinate shadow, where the calculation is exact enough to be theorem-shaped.

Let a parent coordinate be

$$
S\sim \mathrm{Unif}[0,1],
$$

and let an offspring coordinate be

$$
X=S+E,\qquad E\sim\mathrm{Unif}[-c,c].
$$

Let `F_c` be the marginal CDF of `X`, and define the rank-uniform coordinate

$$
R=F_c(X).
$$

For two siblings with the same parent `S`,

$$
\mathrm{Cov}(R_1,R_2)
=
\mathrm{Var}\left(\mathbb E[R\mid S]\right)
=B(c).
$$

For iid sprinkling the sibling term is zero. For fixed cluster width `w`, the marked empirical-rank bracket is:

$$
N\,\mathrm{Var}\!\left(\frac1N\sum_{i=1}^N R_i\right)
\longrightarrow
\frac1{12}+(w-1)B(c).
$$

The receipt computes `B(c)` in closed form using antiderivatives of `F_c`, at mpmath `dps=140`:

| `c` | `B(c)` | `N Var`, `w=4` |
|---:|---:|---:|
| `0.25` | `0.06765873015873015873015873015873015873016` | `0.2863095238095238095238095238095238095238` |
| `0.5` | `0.04087301587301587301587301587301587301587` | `0.205952380952380952380952380952380952381` |
| `1` | `0.01505456349206349206349206349206349206349` | `0.1284970238095238095238095238095238095238` |
| `2` | `0.004456535218253968253968253968253968253968` | `0.09670293898809523809523809523809523809524` |
| `4` | `0.001206267826140873015873015873015873015873` | `0.08695213681175595238095238095238095238095` |
| `8` | `0.0003134288485088045634920634920634920634921` | `0.08427361987885974702380952380952380952381` |
| `16` | `0.00007986151982867528521825396825396825396825` | `0.08357291789281935918898809523809523809524` |

The iid value is:

$$
\frac1{12}=0.08333333333333333333333333333333333333333.
$$

So the marked-coordinate process has a genuine bracket residue at finite `c`, and the residue washes out as `c\to\infty`.

This is the first clean asymptotic identity in the linear-window campaign:

> **[PRINCIPLE] Marked finite-`c` clustering is not iid sprinkling at the fluctuation-bracket level, even when fixed finite unrooted patterns wash out.**

But this is marked. The record law is order-only. The follow-up receipt therefore tests a finite order-visible bracket shadow: repeated laws are compared through `N`-scaled variances of relation density, vertex past/future degree observables, degree covariances, and `P_{\log 2}`.

At `N=768`, `w=4`, the order-visible bracket audit gives:

| schedule | score/null | phase |
|---|---:|---|
| fixed `J=4` | `1.37725863198932668` | visible |
| square-root `J=floor(sqrt(N))` | `0.627850694816361028` | camouflage |
| linear half `J=N/2` | `0.959480810579188548` | camouflage |
| linear one `J=N` | `0.553475513017930274` | camouflage |
| linear two `J=2N` | `0.54333257009582914` | camouflage |

This receipt does **not** recover the marked bracket residue in the tested linear schedules. The marked and order-only problems have separated:

1. marked coordinates retain a provable finite-`c` sibling bracket;
2. the tested order-only bracket shadows still camouflage the linear schedules;
3. the remaining theorem must decide whether the order-only law is contiguous to sprinkling, or whether a subtler order-only Palm/Mecke/bracket identity can recover the marked residue without access to coordinates.

### 9.27 Reconstructed coordinates and growing-window washout

The most natural order-only attempt to recover the marked coordinate bracket is to reconstruct approximate coordinates from the order itself. In a `1+1` sprinkling, for a record with lightcone coordinates `(u,v)`,

$$
\frac{|P_x|}{N}\approx uv,
\qquad
\frac{|F_x|}{N}\approx (1-u)(1-v).
$$

Thus the order gives:

$$
u+v
\approx
1+\frac{|P_x|}{N}-\frac{|F_x|}{N},
\qquad
uv\approx\frac{|P_x|}{N},
$$

and the unordered pair `{u,v}` is recovered as the two roots of a quadratic. This is still order-only; it uses no original coordinate marks.

The reconstructed-coordinate Palm receipt tests whether same-hidden-label pairs become visible again through these reconstructed coordinates. At `N=768`, `w=4`, the pseudo-label guard is:

$$
0.586066691080729167.
$$

The clustered schedules give:

| schedule | mean separability | interpretation |
|---|---:|---|
| fixed `J=4` | `0.902523782518174913` | visible |
| square-root `J=floor(sqrt(N))` | `0.589849154154459635` | barely visible |
| linear half `J=N/2` | `0.519100613064236111` | pseudo-label-like |
| linear one `J=N` | `0.516373316446940104` | pseudo-label-like |
| linear two `J=2N` | `0.519458664788140191` | pseudo-label-like |

So even degree-reconstructed coordinates do not recover the marked linear-window residue in this finite pair projection.

The campaign then proves the strongest honest order-only washout theorem currently available. For fixed hidden width `w`, a uniformly sampled `k_N`-record induced suborder contains a hidden sibling collision with probability at most:

$$
\binom{k_N}{2}\frac{w-1}{N-1}.
$$

Therefore if

$$
k_N=o(\sqrt N),
$$

then hidden sibling collisions vanish. Conditional on no sibling collision, the already proved no-collision rank-kernel convergence gives the same limiting sampled order law as `1+1` sprinkling. Thus:

> **[PRINCIPLE] In the bounded-width linear window, every uniformly sampled `k_N=o(\sqrt N)` induced-suborder test is asymptotically blind to the hidden clusters.**

The receipt checks the bound at width `w=4`. For `k_N=N^\beta`:

| `beta` | `N=10^8` collision bound | interpretation |
|---:|---:|---|
| `0.25` | `0.000148500001485000015` | washed |
| `0.40` | `0.0376120803761208038` | washing |
| `0.49` | `1.0374625903746259` | asymptotic but very slow |
| `0.50` | `1.49985001499850015` | boundary |
| `0.60` | `59.7137395471373955` | outside proof |

The `0.49` line matters: the theorem is asymptotic, but near the square-root boundary finite scales are brutal. This is consistent with the receipts where square-root-scale schedules remain visible or marginal.

The next theorem is now crisp:

> **[OPEN] Either extend washout from sampled `o(\sqrt N)` windows to full order-only contiguity in the bounded-width linear window, or find an order-only statistic whose effective sample size is at least square-root scale and whose limiting bracket recovers the marked sibling residue.**

### 9.28 Square-root collisions, partition likelihood, and local Palm kernels

The previous section says where small-window order-only tests become blind. The next question is what happens at the first scale where hidden multiplicity can accumulate. Let `N=mw` records be partitioned into hidden clusters of fixed width `w`, and let `C_N` be the number of same-hidden-cluster pairs in a uniformly sampled `k`-record subset. The exact no-collision probability is:

$$
\mathbb P(C_N=0)
=
\prod_{i=0}^{k-1}\frac{N-iw}{N-i}.
$$

The first two factorial moments give the square-root critical law. If:

$$
k=\lfloor a\sqrt N\rfloor,
$$

then:

$$
\mathbb E C_N
=
\binom{k}{2}\frac{w-1}{N-1}
\longrightarrow
\lambda(a,w)
=
\frac{a^2(w-1)}{2},
$$

and:

$$
\mathbb E[C_N(C_N-1)]\longrightarrow \lambda(a,w)^2.
$$

Thus the hidden collision field is Poisson at the square-root scale. For `w=4`, the receipt gives:

| `a` | `N=10^8` mean | `E2/mean^2` | exact `P(C_N=0)` | `exp(-mean)` |
|---:|---:|---:|---:|---:|
| `0.5` | `0.374925003749250037` | `0.999733313327998466` | `0.687319352543237194` | `0.687340824842918326` |
| `1.0` | `1.49985001499850015` | `0.999866666665999867` | `0.223107844900629856` | `0.223163628835672165` |
| `1.5` | `3.37477503374775034` | `0.999911114814617278` | `0.0341969461941355713` | `0.0342258170994528939` |

This is the Maxwell/Euler-style object: below `sqrt(N)` collisions vanish; at `sqrt(N)` the collision field has an explicit intensity. But it is still marked. The record law only sees the order.

The next receipt therefore tests a simple full-order hidden-partition likelihood shadow. For every unordered pair `{x,y}`, it computes order-only scores:

- external causal-neighborhood difference;
- past/future degree L1 difference;
- time-degree difference;
- reconstructed-coordinate sum distance.

It then asks whether the top `10` times the true hidden-pair count is enriched for actual hidden siblings. The pseudo-label null at `N=768`, `w=4` gives:

$$
\mathrm{mean\ enrichment}=1.07267554012345679,
\qquad
\mathrm{max}=1.13185763888888889,
\qquad
\mathrm{guard}=1.63185763888888889.
$$

The clustered schedules give:

| schedule | mean top-tail enrichment | mean separability | interpretation |
|---|---:|---:|---|
| fixed `J=4` | `19.6780478395061728` | `0.975791197357562385` | partition visible |
| square-root `J=floor(sqrt(N))` | `2.14535108024691358` | `0.633178777511623309` | partition visible |
| linear half `J=N/2` | `1.11706211419753086` | `0.507842031294816714` | pseudo-label-like |
| linear one `J=N` | `1.0800733024691358` | `0.508037316869282397` | pseudo-label-like |
| linear two `J=2N` | `1.08747106481481481` | `0.501727481132163604` | pseudo-label-like |

So a direct pair-ranking likelihood is not the missing linear-window identity. It is sensitive enough to recover fixed and square-root structure, then washes out in the tested linear schedules.

The last receipt checks the local Palm projection itself. For a sibling pair, the order-only pair kernel is exactly null:

$$
\mathbb P(x<y)=\frac14,
\qquad
\mathbb P(x\ \mathrm{comparable\ to}\ y)=\frac12,
$$

the same as for two iid `1+1` records. Pair comparability alone cannot see sibling collisions.

The first possible local residue is therefore a three-record Palm kernel: two siblings plus one independent outsider. The receipt compares its unlabeled triple-pattern law to the exact iid law:

$$
(\mathrm{antichain},\mathrm{one},\mathrm{vee},\mathrm{wedge},\mathrm{chain})
=
\left(\frac16,\frac13,\frac16,\frac16,\frac16\right).
$$

With `200000` deterministic-seed trials, the Palm-vs-exact L1 gaps are:

| mixing ratio `c` | Palm L1 gap | iid Monte Carlo L1 control | ratio |
|---:|---:|---:|---:|
| `0.5` | `0.0292833333333333333` | `0.00596` | `4.91331096197` |
| `1.0` | `0.00459333333333333333` | `0.00483` | `0.951000690131` |
| `2.0` | `0.00294` | `0.00319` | `0.921630094044` |
| `4.0` | `0.00296333333333333333` | `0.0033` | `0.89797979798` |

This is subtle but important. There is a local Palm-kernel residue at smaller linear ratio `c=0.5`, but by `c=1` the tested three-record Palm projection is inside the iid Monte Carlo control. That matches the broader story: square-root and smaller linear ratios can remain visible, while the harder linear schedules need either exact integral Palm kernels, square-root-scale accumulation, or full likelihood-ratio/contiguity analysis.

The next theorem-shaped object is now:

$$
\mathbb E[M_N\mid \mathcal O_N],
$$

where `M_N` is a marked collision/bracket field and `\mathcal O_N` is the sigma-field generated by the transitive order. Either this conditional projection has a nonzero square-root/Palm bracket limit, or the marked residue is genuinely washed out by forgetting coordinates and hidden labels.

### 9.29 Exact local Palm residue and pair-rooted signature failure

The Monte Carlo Palm receipt was too weak near `c=1`: it could not distinguish a real small residue from sampling noise. The next receipt replaces it with an exact one-coordinate integral.

Let siblings be:

$$
X_1=S+E_1,
\qquad
X_2=S+E_2,
$$

with `S` uniform on `[0,1]` and `E_i` uniform on `[-c,c]`. Let `Z` be an independent outsider with the same marginal CDF `F_c`. The one-coordinate order law of `(X_1,X_2,Z)` is controlled by:

$$
q(c)
=
\mathbb P(Z\ \mathrm{lies\ between}\ X_1\ \mathrm{and}\ X_2)
=
\mathbb E |F_c(X_1)-F_c(X_2)|.
$$

For fixed parent `S=s`, this is:

$$
\frac{1}{c^2}
\int_{s-c}^{s+c}(t-s)F_c(t)\,dt.
$$

The receipt evaluates this integral at `dps=140`, then enumerates the two independent lightcone-coordinate permutations to get the exact sibling-plus-outsider triple law. The iid `1+1` triple law is recovered at `q=1/3`. For finite `c`, the exact local Palm residue is nonzero:

| `c` | `q(c)` | triple L1 gap from iid |
|---:|---:|---:|
| `0.25` | `0.1416666666666666666666666666666666666667` | `0.1102083333333333333333333333333333333333` |
| `0.5` | `0.2333333333333333333333333333333333333333` | `0.03` |
| `1.0` | `0.3` | `0.003333333333333333333333333333333333333333` |
| `2.0` | `0.3239583333333333333333333333333333333333` | `0.000263671875` |
| `4.0` | `0.330859375` | `0.00001836140950520833333333333333333333333333` |
| `8.0` | `0.3326985677083333333333333333333333333333` | `0.000001208782196044921875` |

This changes the status of the local Palm branch. The pair kernel is exactly null, but the triple Palm kernel is not. It merely becomes very small near the linear ratios that were hard in finite samples. At `c=1`, the exact L1 gap is `1/300`, which explains why the earlier Monte Carlo and pair-ranking receipts did not stably see it.

The next finite receipt asks whether this exact local residue can be used to recover sibling pairs by their rooted third-record signature. For each pair `{x,y}`, it counts how every third record `z` sits relative to `x` and `y`:

$$
\mathrm{status}(z,x),\mathrm{status}(z,y)\in\{-1,0,+1\},
$$

and also counts the induced unlabeled triple pattern. These are order-only features. The pseudo-label null at `N=768`, `w=4` is:

$$
\mathrm{mean}=0.526310390896267361,
\qquad
\mathrm{max}=0.542180379231770833,
\qquad
\mathrm{guard}=0.592180379231770833.
$$

The clustered schedules give:

| schedule | mean best pair-Palm separability | interpretation |
|---|---:|---|
| fixed `J=4` | `0.86794175042046441` | visible |
| square-root `J=floor(sqrt(N))` | `0.623240788777669271` | visible |
| linear half `J=N/2` | `0.537787967258029514` | pseudo-label-like |
| linear one `J=N` | `0.532786263359917535` | pseudo-label-like |
| linear two `J=2N` | `0.526714960734049479` | pseudo-label-like |

So the exact local Palm residue is real, and pair-rooted signatures detect it up to the square-root boundary, but this finite pair-identification projection still does not recover the tested linear schedules.

The next object is therefore not "find the sibling pair." It is an aggregate square-root-scale likelihood:

$$
\sum_{\{x,y\}} \ell_N(x,y;\mathcal O_N),
$$

where each pair has only a tiny local Palm bias. This is closer to sparse planted-structure detection than to local feature classification. The open theorem is whether the sum has a nondegenerate limit, or whether its conditional variance collapses and contiguity holds.

### 9.30 Oriented aggregate pair-Palm bracket and source decomposition

The pair-rooted audit tried to identify hidden pairs. That is too much to ask. The next receipt sums pair-Palm status information over all pairs. This section is retained because it explains an attractive false breakthrough. The receipt treated the pair as unordered in the outer sum, but it still placed the two endpoints in ordered slots `(x,y)` using the implementation's record-index order. For each pair and each third record `z`, it records:

$$
(\mathrm{status}(z,x),\mathrm{status}(z,y))\in\{-1,0,+1\}^2.
$$

For the nine status counts over all pairs, it records means, variances, `q01`, and `q99` quantiles. This is an oriented aggregate pair-Palm bracket shadow: a finite U-statistic-like projection of the exact local Palm residue, but not yet a valid order-only invariant.

The receipt calibrates on eight `N=768` sprinklings and uses four held-out sprinklings. The held-out null is:

$$
\mathrm{heldout\ mean}=4.3048156103747607,
\qquad
\mathrm{heldout\ max}=5.7431020875069451.
$$

The clustered schedules give:

| schedule | mean score | mean / heldout max | interpretation |
|---|---:|---:|---|
| fixed `J=4` | `111.409739814257737` | `19.3988785358019304` | visible |
| square-root `J=floor(sqrt(N))` | `2247.82948159632159` | `391.396399950134668` | visible |
| linear half `J=N/2` | `3525.33504736540418` | `613.838130273553319` | visible |
| linear one `J=N` | `3781.36440161392428` | `658.418454695343511` | visible |
| linear two `J=2N` | `3945.9417743966126` | `687.074983915100185` | visible |

This looked like the first finite projection in the campaign that strongly separates **all** tested linear schedules.

The hostile opening is immediate: maybe this is not the sparse hidden sibling-pair effect at all. The source audit therefore evaluates the same aggregate bracket three ways:

1. all unordered pairs;
2. true hidden sibling pairs only;
3. non-hidden pairs only.

At `N=768`, `w=4`, removing true hidden sibling pairs does not remove the signal:

| schedule | all-pair ratio | hidden-only ratio | non-hidden ratio |
|---|---:|---:|---:|
| square-root `J=floor(sqrt(N))` | `237.385033718` | `255.24414557` | `236.689062605` |
| linear half `J=N/2` | `377.699959509` | `389.150385415` | `377.698699835` |
| linear one `J=N` | `420.283305632` | `436.448065792` | `420.282543971` |
| linear two `J=2N` | `401.412086949` | `447.440444306` | `401.411172279` |

For the oriented score, the finite aggregate pair-Palm bracket is **not** merely summing the `O(N)` true hidden sibling pairs. It sees a broad permutation residue across the ordinary non-hidden pair population.

But the stronger hostile review is decisive. The endpoint slots `(x,y)` are not intrinsic to an unordered pair. A relabeling of the same finite order can change which endpoint is called `x` and which is called `y`, and in the clustered generator the record index can carry construction history. Therefore this score is a diagnostic of a possible Palm-bracket direction, not a valid final order-only witness.

The lesson survives in a weaker form. If an all-pair Palm bracket is part of the click law, it cannot be:

$$
\text{find hidden pairs}.
$$

Nor can it be an oriented endpoint-slot statistic. It must be:

$$
\text{control an endpoint-symmetric, relabeling-invariant all-pair Palm-bracket field}.
$$

The oriented receipt is therefore demoted: useful as hostile evidence that tiny Palm biases can aggregate, rejected as a final record-law statistic.

### 9.31 Endpoint-invariant aggregate repair

The repair merges endpoint-swapped status classes. For every unordered pair `{x,y}` and third record `z`, it records the unordered status multiset:

$$
\{\mathrm{status}(z,x),\mathrm{status}(z,y)\}
\in
\{\{-1,-1\},\{-1,0\},\{-1,+1\},\{0,0\},\{0,+1\},\{+1,+1\}\}.
$$

Equivalently, the six categories are `mm`, `m0`, `mp`, `00`, `0p`, and `pp`. The receipt records means, variances, `q01`, and `q99` quantiles for these six endpoint-symmetric classes, calibrates on eight `N=768` sprinklings, and tests random record relabeling. The held-out null is:

$$
\mathrm{heldout\ mean}=8.77011109738470164,
\qquad
\mathrm{heldout\ max}=15.9700423385746535.
$$

The clustered schedules give:

| schedule | mean score | mean / heldout max | interpretation |
|---|---:|---:|---|
| fixed `J=4` | `10.4376717787055678` | `0.653578215850687798` | inside held-out max |
| square-root `J=floor(sqrt(N))` | `5.92636269822321365` | `0.371092485078042005` | inside held-out max |
| linear half `J=N/2` | `5.22483983867946849` | `0.327165058671083777` | inside held-out max |
| linear one `J=N` | `4.52249623182851433` | `0.283186239331670603` | inside held-out max |
| linear two `J=2N` | `4.43976785057342896` | `0.278006016292733501` | inside held-out max |

The relabeling spot checks give:

$$
\mathrm{max\ abs\ diff}_{\mathrm{fixed}}=0,
\qquad
\mathrm{max\ abs\ diff}_{J=N}=0.
$$

So the endpoint-invariant six-class repair does **not** recover the tested linear schedules. The earlier aggregate separation depended on endpoint ordering. This does not prove order-only contiguity, because the repaired vector is still only a small mean/variance/quantile projection. It does prove that the next candidate cannot use oriented endpoint slots.

The next theorem-shaped object is therefore:

$$
B_N^{\mathrm{sym}}
=
\sum_{\{x,y\}}
\Phi\left(
\left\{
\{\mathrm{status}(z,x),\mathrm{status}(z,y)\}:z\ne x,y
\right\}
\right),
$$

with `\Phi` endpoint-symmetric, relabeling-invariant, centered, and calibrated under `1+1` sprinkling. The open theorem is no longer "promote the oriented receipt." It is either to find a genuinely invariant `B_N^{sym}` with a nonzero limiting bracket/rate, or to prove that every such order-only aggregate loses the marked Palm residue in the linear window.

### 9.32 Endpoint-symmetric pair-flag likelihood ladder

The next invariant approximation to a likelihood ratio is not another status-bin moment. It is a rooted flag law around a typical unordered pair. For a root pair `{x,y}` and outsider set `S`, define the rooted flag code as the induced transitive order on `{x,y}\cup S`, canonicalized over:

1. swapping `x` and `y`;
2. permuting all outsider records in `S`;
3. random record relabeling, provided sampled vertices are mapped with the relabeling.

The receipt trains a smoothed sprinkling flag distribution and scores held-out and clustered samples by a frequency/NLL/chi-square bracket vector. It first tests four-record flags, with two outsiders per rooted pair. The first sample design uses `32768` rooted flags and sees `66` flag codes. Its held-out null is:

$$
\mathrm{heldout\ max}_{4a}=10.1934256621203576.
$$

The first four-record run gives:

| schedule | mean / heldout max | interpretation |
|---|---:|---|
| fixed `J=4` | `1.20286628792384997` | visible |
| square-root `J=floor(sqrt(N))` | `1.00662762236463568` | weakly visible |
| linear half `J=N/2` | `0.885955921750200987` | inside |
| linear one `J=N` | `1.05933847191521943` | weakly visible |
| linear two `J=2N` | `0.855460274730619825` | inside |

That opens a hostile path: the `J=N` signal is weak and may be a finite sample-design accident. The receipt therefore reruns the four-record flag audit with an independent sample design. The second design also uses `32768` rooted flags and sees `66` flag codes, but its held-out null is:

$$
\mathrm{heldout\ max}_{4b}=12.6252281353938218.
$$

The independent four-record run gives:

| schedule | mean / heldout max | interpretation |
|---|---:|---|
| fixed `J=4` | `1.6185977887554711` | visible |
| square-root `J=floor(sqrt(N))` | `1.03835832855911661` | weakly visible |
| linear half `J=N/2` | `0.736390675100958657` | inside |
| linear one `J=N` | `0.756292365995827559` | inside |
| linear two `J=2N` | `0.933815256506892182` | inside |

So the apparent `J=N` four-flag signal is not robust.

The receipt then follows the obvious next path before the next review pass: five-record rooted pair flags, with three outsiders. This uses `8192` rooted flags and sees `439` flag codes. The held-out null is:

$$
\mathrm{heldout\ max}_{5}=29.3211381207053303.
$$

The five-record run gives:

| schedule | mean / heldout max | interpretation |
|---|---:|---|
| fixed `J=4` | `0.898282905529662658` | inside |
| square-root `J=floor(sqrt(N))` | `0.856626256776867342` | inside |
| linear half `J=N/2` | `0.855769295550185496` | inside |
| linear one `J=N` | `0.904432975336874781` | inside |
| linear two `J=2N` | `0.859936761859127622` | inside |

All three flag receipts pass endpoint-swap, outsider-permutation, and relabel-mapped invariance checks with zero relabel code difference.

The result is negative but useful. Endpoint-symmetric rooted pair flags are the smallest honest likelihood-like repair of the oriented aggregate bracket. They still do not robustly recover the tested linear-window schedules. The next target therefore gets sharper again: either a larger mesoscopic rooted flag field is needed, or the true object is the exact second moment/contiguity calculation for the unlabeled order likelihood ratio.

### 9.33 Mesoscopic rooted flag field

The next receipt follows the larger-flag opening. It samples six-record rooted flags: an unordered root pair plus four outsiders. Exact code frequencies are now sparse, so the receipt uses endpoint-symmetric canonical codes hashed into calibrated bucket fields, plus entropy, collision, smoothed code-NLL, and code-chi-square features. It runs two independent sample designs before promoting any signal.

The primary six-record design uses `3072` rooted flags, sees `3391` training codes, and has held-out max:

$$
\mathrm{heldout\ max}_{6a}=983.316517143050609.
$$

The primary ratios are:

| schedule | mean / heldout max | interpretation |
|---|---:|---|
| fixed `J=4` | `0.614932399807547229` | inside |
| square-root `J=floor(sqrt(N))` | `0.723548157062015443` | inside |
| linear half `J=N/2` | `0.631540619472017349` | inside |
| linear one `J=N` | `0.589731664576670041` | inside |
| linear two `J=2N` | `0.564897201115129273` | inside |

The independent six-record design also uses `3072` rooted flags, sees `3401` training codes, and has a much lower held-out max:

$$
\mathrm{heldout\ max}_{6b}=427.545871037857312.
$$

The independent ratios are:

| schedule | mean / heldout max | interpretation |
|---|---:|---|
| fixed `J=4` | `1.13838241371208024` | visible |
| square-root `J=floor(sqrt(N))` | `1.23611609770777775` | visible |
| linear half `J=N/2` | `1.0783769512257903` | visible |
| linear one `J=N` | `1.17557144226012443` | visible |
| linear two `J=2N` | `1.11752493599292647` | visible |

The two sample designs disagree on every tested linear schedule. Both pass endpoint-swap, outsider-permutation, and relabel-mapped invariance checks with zero relabel code difference, so the problem is not endpoint leakage. It is finite calibration instability in a sparse mesoscopic flag field, dominated by out-of-vocabulary and code-chi-square components.

This receipt therefore does not promote a mesoscopic flag law. It demotes the finite flag-field path unless the next version has a stable asymptotic calibration or a theorem. The honest next target is the exact unlabeled likelihood ratio, not more sample-design-sensitive flags.

### 9.34 Small exact unlabeled likelihood second-moment proxy

The next receipt follows that fork at the smallest scale where the unlabeled law can be computed exactly by brute force. At `N=6`, the `1+1` sprinkling law is obtained by enumerating all `6! = 720` coordinate permutations and canonicalizing every induced order under all `6!` record relabelings. The exact unlabeled support has `315` codes.

The empirical sprinkling calibration uses `1024` samples per replicate. Its null maxima are:

$$
\chi^2_{\max}=0.374126434326171875,
\qquad
\mathrm{TV}_{\max}=0.232834201388888889,
\qquad
\mathrm{KL}_{\max}=0.201937841476050811.
$$

Width-2 clustered schedules projected to the same exact unlabeled code space give:

| schedule | mean chi-square / null max | mean TV / null max | mean KL / null max | interpretation |
|---|---:|---:|---:|---|
| fixed `J=4` | `0.837160336477185827` | `0.937063100009320533` | `0.849110739864550249` | inside |
| square-root `J=floor(sqrt(N))` | `0.78212337496813663` | `0.906701463323702116` | `0.805874840621101608` | inside |
| linear half `J=N/2` | `0.832709660973744583` | `0.94619722248112592` | `0.86101199172501817` | inside |
| linear one `J=N` | `0.845518735661483559` | `0.928231894864386243` | `0.871513923019243646` | inside |
| linear two `J=2N` | `0.775057354065765995` | `0.903625687389318669` | `0.796576473376467004` | inside |

No sampled clustered schedule leaves the exact `N=6` unlabeled sprinkling calibration. The canonical code also survives random record relabeling exactly.

This does not prove critical-window contiguity. It does, however, change the best mathematical question. The campaign now has a fully honest toy version of the likelihood object, and at that scale it supports the washout side. The next serious theorem is a second-moment calculation for the unlabeled order likelihood ratio:

$$
\mathbf E_{P_N}\left[\left(\frac{dQ_N}{dP_N}\right)^2\right],
$$

or an argument that this second moment diverges through a specific endpoint-symmetric statistic.

### 9.35 Unlabeled cross-second-moment ladder

The next receipt moves from a one-sample empirical square to a two-replica cross moment. For exact unlabeled `P_N`, it samples two independent empirical clustered laws `q_1,q_2` and computes:

$$
M_N(q_1,q_2)
=
\sum_o \frac{q_1(o)q_2(o)}{p(o)}.
$$

This is the finite empirical shadow of:

$$
\mathbf E_{P_N}\left[\left(\frac{dQ_N}{dP_N}\right)^2\right],
$$

but with the self-collision bias of one empirical sample reduced. The receipt computes exact unlabeled `P_N` at `N=6` and `N=8`. The exact supports are:

$$
|\mathrm{supp}(P_6)|=315,
\qquad
|\mathrm{supp}(P_8)|=14794.
$$

At `N=6`, with `2048` samples per replica, all tested linear schedules remain inside the exact-`P_6` calibrated null:

| schedule | mean cross-excess / null max | mean TV / null max | interpretation |
|---|---:|---:|---|
| linear half `J=N/2` | `-0.177759854116986955` | `0.950057001072961373` | inside |
| linear one `J=N` | `-0.0394690699957918362` | `0.941666107832618026` | inside |
| linear two `J=2N` | `0.251788469631084304` | `0.942613331545064378` | inside |

At `N=8`, the first ladder has a calibration warning: all six null cross-excess values are negative, so the raw null maximum is `-0.005290985107421875`. Under that bad one-sided threshold, `linear_two` appears visible while `linear_half` and `linear_one` remain inside:

| schedule | mean cross-excess | mean TV / null max | raw interpretation |
|---|---:|---:|---|
| linear half `J=N/2` | `-0.00918292999267578125` | `0.999085970501649318` | inside |
| linear one `J=N` | `-0.0516443252563476563` | `0.998053241871880684` | inside |
| linear two `J=2N` | `0.0327472686767578125` | `0.997758803364958723` | raw-visible |

This opens a hostile path, not a claim. A negative null maximum means the empirical cross moment is still under-sampled relative to the large unlabeled support. The next receipt must repair the null calibration before any `N=8` signal can be promoted.

### 9.36 N=8 second-moment stability repair

The stability receipt reruns `N=8` with `4096` samples per replica and a centered null guard:

$$
g_8=\max\left(0,\ \max_r e_r,\ \bar e+2s_e\right),
$$

where `e_r=M_8-1` over independent sprinkling replica pairs. The result is:

$$
\bar e_{\mathrm{null}}=0.0145052671432495117,
\qquad
s_e=0.0316958840734018749,
\qquad
g_8=0.0778970352900532616.
$$

The tested schedules then give:

| schedule | mean cross-excess / guard | mean TV / null max | interpretation |
|---|---:|---:|---|
| fixed `J=4` | `0.021011628227412446` | `0.998152954865377261` | inside |
| square-root `J=floor(sqrt(N))` | `-0.159146632620650394` | `0.998373867972888307` | inside |
| linear half `J=N/2` | `-0.0506146097591725592` | `0.996004307059726551` | inside |
| linear one `J=N` | `-0.115293084296926355` | `0.996988719734633046` | inside |
| linear two `J=2N` | `-0.0287643528159100025` | `0.996793573042362699` | inside |

The apparent `linear_two` signal from the first `N=8` ladder is therefore demoted to finite calibration noise. The receipt also records the top positive unlabeled classes for each linear schedule; their individual probabilities are tiny, typically `2.48015873016e-5`, `4.96031746032e-5`, or `9.92063492063e-5`, and they do not sum to a stable cross-moment excess above guard.

This is the strongest washout-side evidence in the likelihood branch so far:

$$
N=6,8\quad\text{exact-}P_N\text{ cross-second-moment proxies do not separate the tested linear schedules after hostile calibration.}
$$

It is still finite evidence. The theorem target is now precise: prove boundedness of the unlabeled second moment in the bounded-width linear window, or find the stable rare-order class that makes it diverge.

### 9.37 Exact-P8 rare-class stability audit

The next receipt follows the second branch directly. If the unlabeled second moment diverges, one plausible finite shadow is a rare unlabeled order class, or a rare structural group of classes, whose `Q`-mass is stably too large relative to exact `P`-mass. The audit uses exact `P_8` and tests three projections:

1. individual unlabeled isomorphism codes, with `14794` classes;
2. coarse structural groups `(relations, height, minima, maxima)`, with `873` groups;
3. interval-profile groups, with `4833` groups.

Each projection uses the same two-replica cross moment and a centered null guard. No tested linear schedule beats the guard in any projection:

| projection | linear half ratio | linear one ratio | linear two ratio |
|---|---:|---:|---:|
| individual code | `-0.161720530900742868` | `-0.226677102358940082` | `-0.348794881131240067` |
| coarse group | `0.0126418929152860348` | `-0.0441963595586621817` | `0.0707009539238394562` |
| interval group | `0.0572142382058820338` | `0.191668864723535681` | `-0.44967977487819426` |

The audit prints top positive classes and groups, but none is stable enough to exceed its null guard. At this scale, the stable-rare-class branch fails.

### 9.38 Two-replica hidden-partition overlap tax

The boundedness branch now has a precise combinatorial skeleton. A hidden-cluster mixture second moment compares two independent hidden explanations. If `H` and `H'` are two independent uniform partitions of `N` records into blocks of fixed width `w`, the relevant overlap count is:

$$
O_N(H,H')
=
\#\{\{x,y\}:x,y\text{ are in the same block in both }H\text{ and }H'\}.
$$

For fixed `w`,

$$
O_N \Rightarrow \mathrm{Poisson}\left(\lambda_w\right),
\qquad
\lambda_w=\frac{(w-1)^2}{2}.
$$

The receipt checks the exact leading factorial-moment contribution. For `r` disjoint specified record pairs, let `p_{N,w,r}` be the exact probability that all `r` pairs are co-blocked in one random width-`w` partition. Then the leading `r`th factorial contribution is:

$$
\frac{(N)_{2r}}{2^r}p_{N,w,r}^2
\longrightarrow
\left(\frac{(w-1)^2}{2}\right)^r.
$$

The exact `r=1` probability recovers:

$$
p_{N,w,1}=\frac{w-1}{N-1}.
$$

For the largest tested sizes, the leading moments are already close to the Poisson targets:

| width | `N` | `r=1` relative error | `r=2` relative error | `r=3` relative error | `r=4` relative error |
|---:|---:|---:|---:|---:|---:|
| `2` | `256` | `0.00392157` | `0.00788964` | `0.0119051` | `0.015969` |
| `3` | `384` | `0.00261097` | `0.00001367` | `0.00790136` | `0.0209965` |
| `4` | `512` | `0.00195695` | `0.00131699` | `0.00981148` | `0.0234339` |

Therefore, for any fixed local overlap weight `a`,

$$
\mathbf E[a^{O_N}]
\to
\exp\left(\lambda_w(a-1)\right)<\infty.
$$

This is not yet the full unlabeled likelihood theorem. It proves the **overlap tax**: bounded-width hidden partitions do not create `O(N)` two-replica overlap. Thus a divergence of the unlabeled second moment must come from one of two sources:

1. an unbounded local likelihood weight per overlapped hidden pair;
2. a stable rare unlabeled order class or group not explained by pair-overlap counting.

The rare-class receipt finds no such stable class at exact `P_8`. The proof target is now reduced to the local factor:

$$
\frac{dQ_N}{dP_N}
\ \text{must be bounded, in second moment, by a fixed weight per two-replica hidden-pair overlap.}
$$

If that factorization/bound is proved, boundedness of

$$
\mathbf E_{P_N}\left[\left(\frac{dQ_N}{dP_N}\right)^2\right]
$$

follows from the Poisson overlap moment-generating function.

### 9.39 The exact reduction lemma for the remaining proof

The preceding paragraph can be isolated as a clean second-moment lemma.

Let `P_N` be the sprinkling law on the observed, unlabeled order sigma-field, and let a hidden-partition mixture be written as

$$
Q_N=\int Q_{N,h}\,d\mu_N(h),
$$

with likelihoods

$$
L_{N,h}=\frac{dQ_{N,h}}{dP_N}.
$$

Assume that for some constants `C<infinity` and `a<infinity`, independent hidden explanations `H,H'` satisfy the overlap-dominated cross bound

$$
\mathbf E_{P_N}\!\left[L_{N,H}L_{N,H'}\mid H,H'\right]
\le
C\,a^{O_N(H,H')}.
$$

Then

$$
\mathbf E_{P_N}\left[\left(\frac{dQ_N}{dP_N}\right)^2\right]
\le
C\,\mathbf E\left[a^{O_N(H,H')}\right].
$$

For bounded width, the preceding overlap calculation gives

$$
O_N(H,H')\Rightarrow
\mathrm{Poisson}\left(\frac{(w-1)^2}{2}\right),
$$

and therefore the right-hand side has finite limit

$$
C\exp\!\left(\frac{(w-1)^2}{2}(a-1)\right).
$$

The proof is only Fubini and conditional expectation:

$$
\begin{aligned}
\mathbf E_{P_N}\left[\left(\frac{dQ_N}{dP_N}\right)^2\right]
&=
\mathbf E_{P_N}\left[
\left(\int L_{N,h}\,d\mu_N(h)\right)
\left(\int L_{N,h'}\,d\mu_N(h')\right)
\right] \\
&=
\mathbf E_{H,H'}\,
\mathbf E_{P_N}\!\left[L_{N,H}L_{N,H'}\mid H,H'\right] \\
&\le
C\,\mathbf E_{H,H'}\left[a^{O_N(H,H')}\right].
\end{aligned}
$$

Under the shared-pair-only ansatz, the boundedness theorem reduces to one hard local statement:

$$
\mathbf E_{P_N}\!\left[L_{N,H}L_{N,H'}\mid H,H'\right]
\le
C\,a^{O_N(H,H')}.
$$

If it fails, the failure must exhibit either an unbounded local factor, a rare order family, or an overlap-graph structure not counted by common hidden pairs. If it holds, the bounded-width linear-window second moment is bounded.

### 9.40 Exact small-size local-factor audit

The next receipt tests the conditional factor directly in the first exact labeled sizes. It uses exact labeled `1+1` sprinkling laws:

$$
P_N(o)=\frac{\#\{(\pi_u,\pi_v):o(\pi_u,\pi_v)=o\}}{(N!)^2},
$$

for `N=4,6`. For every width-2 hidden matching `H`, it samples the exchangeable conditional clustered law `Q_{N,H}` in the linear-window schedules and computes:

$$
\sum_o \frac{q_H(o)q_{H'}(o)}{p(o)}
$$

for every pair `H,H'`.

The fitted finite constants are:

| `N` | schedule | `C_N=max_{O=0}` | fitted `a_N` | max factors by overlap |
|---:|---|---:|---:|---|
| `4` | linear half | `0.965257108211517334` | `1.0655631955928378` | `O0:0.9652571082`, `O2:1.095976979` |
| `4` | linear one | `0.997816801071166992` | `1.01126562519216002` | `O0:0.9978168011`, `O2:1.020425498` |
| `4` | linear two | `1.00092592835426331` | `1.00647310177622975` | `O0:1.000925928`, `O2:1.013926059` |
| `6` | linear half | `1.07776522636413574` | `2.51246981034099723` | `O0:1.077765226`, `O1:1.163681746`, `O3:17.09333181` |
| `6` | linear one | `1.09220623970031738` | `2.50330006263412915` | `O0:1.092206240`, `O1:1.121217012`, `O3:17.13339329` |
| `6` | linear two | `1.11952185630798340` | `2.47483795379189148` | `O0:1.119521856`, `O1:1.091659069`, `O3:16.96964979` |

No sampled `Q_{N,H}` order lies outside the exact labeled sprinkling support. No single rare `O=0` order class dominates the worst zero-overlap cross factor; the largest top-class share in the `N=6` zero-overlap cases is below `0.008`.

This is evidence for the local factor inequality, but not a proof. The large `O=3` factors at `N=6` are exactly the expected same-hidden-explanation effect; they are absorbed by a fixed per-overlap factor in this finite audit. The important absence is different: the zero-overlap conditional cross factors stay near `1`, and no stable rare labeled order class appears at zero hidden-pair overlap.

### 9.41 Hidden-overlap graph cycle tax

The hostile review then finds a missing structure in the previous reduction. For width `2`, hidden explanations are perfect matchings. The union `H\cup H'` is an alternating graph. Common hidden pairs are only the 2-vertex components. But even when there are no common hidden pairs, the union contains nonshared alternating cycles.

Let `m=N/2` and let `C_k` be the number of alternating components containing `k` hidden `H`-edges. Exact counting gives:

$$
\mathbf E C_1=\frac{m}{2m-1},
$$

and for `k>=2`,

$$
\mathbf E C_k
=
\binom{m}{k}
2^{k-1}(k-1)!
\frac{(2m-2k-1)!!}{(2m-1)!!}.
$$

For every fixed `k`,

$$
\mathbf E C_k\to \frac{1}{2k}.
$$

Therefore:

$$
\mathbf E\sum_{k\ge 1}C_k
=
\frac{1}{2}\log m+O(1),
$$

while the common-pair overlap `C_1` remains `O(1)`.

The receipt gives:

| `m=N/2` | common `E C_1` | total components | nonshared components | total minus `0.5 log m` |
|---:|---:|---:|---:|---:|
| `64` | `0.503937007874015748` | `3.06120164073628786` | `2.55726463286227212` | `0.981760099056451936` |
| `256` | `0.500978473581213307` | `3.75434405314108292` | `3.25336557955986962` | `0.981755330901301687` |
| `1024` | `0.500244259892525647` | `4.44749093567864990` | `3.94724667578612425` | `0.981755032878923349` |
| `4096` | `0.500061042607740203` | `5.14063809761214702` | `4.64057705500440681` | `0.981755014252475160` |

This is a real correction to the theorem target. The shared-pair overlap tax is necessary but not sufficient by itself. If every nonshared alternating component carried a fixed factor `b>1`, then the second moment could still grow polynomially, because:

$$
\mathbf E\,b^{\sum_k C_k}
\quad\text{has a logarithmic component count in the exponent.}
$$

The local factor theorem must therefore prove a stronger statement:

$$
\text{nonshared alternating cycles are asymptotically neutral,}
$$

or replace the bound by a full overlap-graph bound that includes cycle counts. This is now the sharpest obstruction found in the campaign.

### 9.42 Exact-P8 overlap-signature neutrality audit

The next receipt tests whether nonshared cycles actually carry a visible finite factor. At `N=8`, width-2 hidden explanations are the `105` perfect matchings. The exact unlabeled sprinkling law has `14794` classes. The receipt samples every conditional law `Q_H`, computes every cross factor

$$
\sum_o\frac{q_H(o)q_{H'}(o)}{p(o)},
$$

and groups the result by the full overlap-graph signature:

- `(4,)`: one nonshared alternating 8-cycle;
- `(2,2)`: two nonshared alternating 4-cycles;
- `(1,3)`: one common pair and one nonshared 6-cycle;
- `(1,1,2)`: two common pairs and one nonshared 4-cycle;
- `(1,1,1,1)`: identical hidden matching.

The zero-common signatures are the important test. Their means are:

| schedule | mean `(4,)` | mean `(2,2)` | ratio `(2,2)/(4,)` |
|---|---:|---:|---:|
| linear half | `1.00032016815` | `1.00115806943` | `1.00083763309849502` |
| linear one | `1.00081527347` | `0.999300953699` | `0.998486913810994867` |
| linear two | `0.998777540903` | `0.999879576668` | `1.00110338460721425` |

Every zero-common signature mean is within `0.01` of `1`, and two nonshared cycles are not worse than one. The same-matching signature `(1,1,1,1)` remains large, with mean about `15.46`, as expected from true common hidden pairs.

This is finite evidence for cycle neutrality: nonshared alternating components are not acting like hidden shared pairs in the exact `P_8` unlabeled likelihood shadow.

### 9.43 Exact component mgf and the sufficient cycle-neutrality bound

The cycle count itself has an exact probability-generating function. If `K_m` is the total number of alternating components in the union of two width-2 matchings on `N=2m` records, then:

$$
\mathbf E z^{K_m}
=
\prod_{j=0}^{m-1}\frac{z+2j}{1+2j}
=
\frac{\Gamma(m+z/2)\Gamma(1/2)}
{\Gamma(z/2)\Gamma(m+1/2)}.
$$

Differentiating at `z=1` gives the exact mean:

$$
\mathbf E K_m
=
\sum_{j=0}^{m-1}\frac{1}{2j+1}
=
\frac{1}{2}\log m+O(1).
$$

Therefore a fixed factor per nonshared component is too expensive. If each nonshared component carried factor `b>1`, then:

$$
\mathbf E b^{K_m}
\asymp
m^{(b-1)/2}.
$$

The receipt checks this at `b=1.1`, where the exponent is `0.05`; the scaled value `E[1.1^{K_m}]/m^{0.05}` stabilizes at `1.096731...`.

The sufficient cycle-neutrality condition is now explicit. If the nonshared-cycle factor is:

$$
b_N=1+O\!\left(\frac{1}{\log N}\right),
$$

then the component mgf stays bounded. If:

$$
b_N=1+o\!\left(\frac{1}{\log N}\right),
$$

then the cycle tax becomes asymptotically neutral.

The receipt checks both regimes:

| factor | largest tested behavior |
|---|---:|
| fixed `b=1.1` | grows from `1.350261497` at `m=64` to `2.193462331` at `m=1048576` |
| `b_m=1+2/log(m)` | bounded, from `3.892493562` down to `3.186130346` |
| `b_m=1+1/log(m)^2` | tends back toward `1`, from `1.191240839` down to `1.054456683` |

Thus the boundedness theorem has a precise sufficient target:

$$
\mathbf E_{P_N}[L_HL_{H'}\mid H,H']
\le
C\,a^{C_1(H,H')}\,b_N^{K_{\ge2}(H,H')},
\qquad
b_N=1+O\!\left(\frac{1}{\log N}\right),
$$

where `C_1` counts common hidden pairs and `K_{\ge2}` counts nonshared alternating components. The exact `P_8` signature audit suggests the stronger possibility `b_N=1+o(1/log N)`, but that remains unproved.

### 9.44 Transfer-operator version of cycle neutrality

The preceding bound is sufficient but still too blunt. In the natural pair-factor approximation, a nonshared component does not carry the same factor at every length.

Assume an iid reference law `P` on record marks `X_i`, and suppose a fixed hidden matching `H` has conditional likelihood

$$
L_H=\prod_{(i,j)\in H}\phi(X_i,X_j),
$$

where the pair density ratio `phi` has both marginals equal to `1`. Let `K` be the integral operator

$$
Kf(x)=\int \phi(x,y)f(y)\,d\mu(y).
$$

Because the marginals are one,

$$
K=\Pi+A,
$$

where `Pi` is the constants projection and `A` is centered. A nonshared alternating component with `k` hidden `H`-edges contributes:

$$
\beta_k
=
\mathrm{tr}(K^{2k})
=
1+\mathrm{tr}(A^{2k}).
$$

Thus the real cycle question is spectral. If the centered eigenvalues are `lambda_i`, the asymptotic nonshared-cycle tax is:

$$
\exp\left(
\sum_{k\ge1}
\frac{\sum_i \lambda_i^{2k}}{2k}
\right)
=
\prod_i(1-\lambda_i^2)^{-1/2}.
$$

So nonshared cycles are harmless whenever the centered pair operator has spectral radius bounded below `1` and the determinant product is finite. A divergence requires one of two things:

1. the pair-factor approximation fails; or
2. the centered spectrum approaches `1`.

The receipt checks the exact finite matching recurrence. For one centered mode with eigenvalue `theta`, the limiting tax is:

$$
(1-\theta^2)^{-1/2}.
$$

The finite recurrence converges to it:

| `theta` | determinant tax | exact `m=512` tax | relative error |
|---:|---:|---:|---:|
| `0.1` | `1.00503781525921208` | `1.00504277719621722` | `0.000004937065` |
| `0.5` | `1.15470053837925153` | `1.15488880001329292` | `0.00016303936` |
| `0.9` | `2.29415733870561766` | `2.29898328391699680` | `0.0021035807` |
| `0.99` | `7.08881205008335901` | `7.28378791546881097` | `0.027504731` |

For a three-mode spectrum `[0.4,-0.25,0.125]`, the determinant tax is:

$$
1.13578055999989318,
$$

and the exact `m=512` recurrence gives:

$$
1.13593218110672383.
$$

This is the best theorem-shaped formulation so far:

$$
\mathbf E_P[L_HL_{H'}\mid H,H']
\le
C\,a^{C_1(H,H')}\,
\prod_{\gamma\in\mathcal C_{\ge2}(H,H')}
\left(1+\mathrm{tr}(A^{2|\gamma|})\right),
$$

with `rho(A)<1` and finite determinant tax

$$
\det(I-A^2)^{-1/2}.
$$

The click-law target is no longer merely "nonshared cycles are neutral." It is:

> **[OPEN] Prove a pair-factor/transfer-operator representation of the conditional order likelihood, then prove the centered transfer operator has spectral radius below one in the bounded-width linear window.**

### 9.45 Hostile check: component factorization fails at exact `P_8`

The transfer-operator theorem is a clean model, but it assumes that the conditional likelihood factorizes over overlap-graph components. The next receipt tests that assumption directly.

At exact unlabeled `P_8`, the receipt estimates signature means for all hidden-matching pairs and asks whether there are component weights `beta_1,beta_2,beta_3,beta_4` such that:

$$
M(s)\approx\prod_{k\in s}\beta_k.
$$

The hostile calibration uses the full-identity signature `(1,1,1,1)` to estimate `beta_1`, the zero-common signature `(2,2)` to estimate `beta_2`, and then predicts `(1,1,2)`. It fails by a factor of about `4`:

| schedule | observed `(1,1,2)` | predicted `(1,1,2)` | predicted/observed |
|---|---:|---:|---:|
| linear half | `1.00517510308159722` | `3.94810612480318612` | `3.92777946120964581` |
| linear one | `0.999340699210999504` | `3.92003960411794798` | `3.92262579439914904` |
| linear two | `0.996215844532800099` | `3.93825456795784258` | `3.95321414487719158` |

Least-squares component factorization also fails, with max residual factors around `2.49`.

The important positive observation is that all **non-identical** overlap signatures stay near null:

| schedule | max non-identical signature mean | full-identity mean divided by `105` matchings |
|---|---:|---:|
| linear half | `1.00638226705884177` | `0.147511324028309240` |
| linear one | `1.00207745688302176` | `0.146914595346602183` |
| linear two | `1.00435051690964472` | `0.147284749348958333` |

So the transfer-operator toy theorem is not yet the actual unlabeled likelihood theorem. The exact-`P_8` evidence points to a different decomposition:

1. all non-identical hidden explanations may have cross factor `1+o(1)`;
2. the full hidden-identity diagonal may spike;
3. the diagonal is rare in the hidden-explanation average.

### 9.46 Diagonal hidden-identity rarity

The diagonal spike is only dangerous if it is enormous. For `N=2m` records, the number of width-2 hidden matchings is:

$$
M_m=(2m-1)!!.
$$

Stirling gives:

$$
M_m\sim \sqrt{2}\left(\frac{2m}{e}\right)^m.
$$

If:

$$
\mathbf E_{H,H'}B(H,H')
=
\mathbf P(H=H')B_{\rm diag}
+
\mathbf P(H\ne H')B_{\rm mix},
$$

then the diagonal contribution is:

$$
\frac{B_{\rm diag}}{(2m-1)!!}.
$$

Thus any diagonal self-likelihood of size:

$$
\exp(o(m\log m))
$$

is killed by hidden-identity rarity. The receipt checks polynomial, fixed-exponential, and sub-`m log m` diagonal growth. At `m=256`:

| diagonal growth | diagonal ratio |
|---|---:|
| `m^4` | `1.22685406642228924e-573` |
| `10^m` | `2.85649221954468927e-327` |
| `exp(m sqrt(log m))` | `1.83350885648698562e-321` |
| `(2m-1)!!` | `1` |

This gives the new theorem target:

$$
\sup_{H\ne H'}
\mathbf E_P[L_HL_{H'}\mid H,H']
=1+o(1),
$$

and

$$
\mathbf E_P[L_H^2\mid H]
=\exp(o(m\log m)).
$$

If both hold, the hidden-matching second moment is bounded without needing component multiplicativity. A divergence must then come from either:

1. a non-identical overlap signature whose factor stays above `1+c`; or
2. a diagonal self-likelihood growing on the scale of the number of hidden matchings.

### 9.47 Split-sample correction: the hidden diagonal was an estimator artifact

The next hostile check attacks the premise of Section 9.46. The exact-`P_8` component audit used the same empirical conditional histogram on both sides when `H=H'`:

$$
\sum_o \widehat q_H(o)^2/P(o).
$$

That is a biased plug-in estimator. Rare order classes with one sampled hit contribute `1/(S^2P(o))`, so a same-histogram reuse can create a large artificial diagonal even when the true split likelihood is near null.

The bias is exact. If `R` independent samples from `q` produce `\widehat q`, then:

$$
\mathbf E\left[\sum_o\frac{\widehat q(o)^2}{P(o)}\right]
=
\sum_o\frac{q(o)^2}{P(o)}
+
\frac{1}{R}
\left(
\sum_o\frac{q(o)}{P(o)}
-
\sum_o\frac{q(o)^2}{P(o)}
\right).
$$

For two independent halves `\widehat q^A,\widehat q^B`, however:

$$
\mathbf E\left[\sum_o\frac{\widehat q^A(o)\widehat q^B(o)}{P(o)}\right]
=
\sum_o\frac{q(o)^2}{P(o)}.
$$

Thus same-histogram reuse is the wrong estimator for the object under investigation.

The quotient symmetry also says that hidden-matching identity should not be a physical event after labels are forgotten. Let `U` be the quotient map from labeled orders to unlabeled orders. If the conditional labeled law is equivariant under record relabeling and `\pi H=H'`, then:

$$
\mathcal L(X_{H'})=\mathcal L(\pi X_H).
$$

Since `U(\pi x)=U(x)`, the unlabeled conditional law is the same for every hidden matching:

$$
q_H(o)=\mathbf P(U(X_H)=o)=q_{H'}(o).
$$

Therefore the true hidden-pair cross factor collapses to the direct unlabeled likelihood second moment:

$$
\sum_o\frac{q_H(o)q_{H'}(o)}{P(o)}
=
\sum_o\frac{q(o)^2}{P(o)}.
$$

This does not prove washout. It changes the target. Hidden-explanation overlap cannot by itself create or erase a record-visible law after the quotient; only the direct order law `q` versus `P` matters.

The receipt reruns the exact-`P_8` audit with independent halves `\widehat q_H^A,\widehat q_H^B`. It compares same-histogram reuse, split same-`H`, and split different-`H`:

| schedule | reuse same histogram | split same `H` | split different `H` | `|split same - split diff|` |
|---|---:|---:|---:|---:|
| linear half | `15.4458321707589286` | `0.990392485119047619` | `1.00088491614484962` | `0.0104924310258019975` |
| linear one | `15.4143031529017857` | `0.997680082775297619` | `0.999937967153695913` | `0.00225788437839829441` |
| linear two | `15.4150966099330357` | `1.00916021437872024` | `1.00162380064800109` | `0.00753641373071915064` |

The audit is not blind to clustering. For exact zero-jitter width-2 clustering at `N=8`, the direct unlabeled likelihood second moment is enormous:

$$
\sum_o\frac{q_{\rm sharp}(o)^2}{P(o)}
=1362.66666666666667.
$$

The consequence is a correction:

1. the apparent hidden-identity spike in the empirical `P_8` component audit is not promoted;
2. the hidden-diagonal rarity route is only conditional bookkeeping, not the current theorem path;
3. the live problem is the direct split/unbiased unlabeled likelihood second moment

$$
S_N=\sum_o\frac{q_N(o)^2}{P_N(o)}
$$

for the linear-window clustered law itself.

The next honest theorem is therefore:

> **[OPEN] Prove `S_N=1+o(1)` for bounded-width linear jitter, or find a stable rare unlabeled order class whose split likelihood contribution survives unbiased estimation.**

### 9.48 Direct split `S_8` ladder and the finite boundary below half scale

The next receipt attacks the live object directly, keeping the denominator exact:

$$
S_N=\sum_o\frac{q_N(o)^2}{P_N(o)}.
$$

For `N=8`, exact `P_8` is obtained by enumerating all `8! = 40320` coordinate permutations and quotienting to `14794` unlabeled order classes. The receipt then estimates `S_8` by independent split samples from the clustered law. It does **not** use a sparse empirical denominator for `N=10,12`; that would be a different biased object. The full-law extension beyond `N=8` requires either exact selected-class `P_N` probabilities or a theorem.

The split null calibration uses `8192` samples per half and `12` null replicas. Its hostile guard is:

$$
\mathrm{guard}_{\chi^2}=0.0448912985139292758.
$$

The exact zero-jitter clustered baseline remains enormous:

$$
S_8^{\rm sharp}=1362.66666666666667.
$$

Thus the direct ladder is sensitive to real clustering. The finite linear-window results are:

| schedule | mean `S_8` | mean excess `S_8-1` | classification |
|---|---:|---:|---|
| `linear_quarter` | `1.06292017300923665` | `0.0629201730092366536` | visible |
| `linear_5_16` | `1.02231673399607340` | `0.0223167339960734049` | inside guard |
| `linear_3_8` | `1.00318491458892822` | `0.00318491458892822266` | inside guard |
| `linear_7_16` | `1.00065080324808757` | `0.000650803248087565104` | inside guard |
| `linear_half` | `0.993998845418294271` | `-0.00600115458170572917` | inside guard |
| `linear_one` | `1.00536195437113444` | `0.00536195437113444010` | inside guard |
| `linear_two` | `0.997635642687479655` | `-0.00236435731252034505` | inside guard |

The top accumulated positive rare-order contribution above the half scale is only:

$$
0.00475691538008.
$$

The finite opening therefore moved downward. The exact `P_8` direct likelihood sees:

1. sharp zero-jitter clustering immediately;
2. `linear_quarter` as a visible low-mixing residue;
3. `linear_5_16` and above inside the split-null guard;
4. no stable rare unlabeled class above half scale.

This does **not** prove the asymptotic boundary is `N/4` or `5N/16`. At `N=8`, those are coarse grid points. The useful conclusion is narrower and cleaner:

> **[OPEN] Above the finite half-scale guard, the next obstruction is not found by exact `P_8` direct likelihood. To advance, derive exact selected-class probabilities beyond `N=8` or prove `S_N\to1` for the linear-window quotient law.**

### 9.49 Selected-class denominator formula

The exact-denominator wall can be partly reduced. Let `C` be an unlabeled `N`-record two-dimensional order. Let `r(C)` be the number of first linear orders `L` with the following property:

1. every comparable pair in `C` has the same orientation in `L`;
2. the second order forced by `C` and `L` is linear, where comparable pairs keep their orientation and incomparable pairs reverse their `L` orientation.

Equivalently, `L` is the first member of a realizer pair `(L,L')` for `C`, with `L'` forced once `L` is chosen. Let `Aut(C)` be the automorphism group of `C`. Then the selected-class count in the fixed-first-coordinate permutation enumeration is:

$$
\#\{\pi:\ U(C_\pi)=C\}
=
\frac{r(C)}{|\mathrm{Aut}(C)|}.
$$

Therefore:

$$
P_N(C)
=
\frac{r(C)}{|\mathrm{Aut}(C)|\,N!}.
$$

This is the missing exact denominator object for rare-class follow-up. It does not enumerate the whole support of `P_N`; it computes `P_N(C)` for a selected class `C`, provided `r(C)` and `|\mathrm{Aut}(C)|` can be counted.

The receipt checks the formula exhaustively for every exact class through `N=6`:

| `N` | classes | exact total | status |
|---:|---:|---:|---|
| 2 | `2` | `2` | ok |
| 3 | `5` | `6` | ok |
| 4 | `16` | `24` | ok |
| 5 | `63` | `120` | ok |
| 6 | `315` | `720` | ok |

It also checks `32` selected exact `N=8` classes, including common classes, rare classes, and random classes. Every selected class matches the exact enumeration. Chain and antichain sanity checks reduce to one coordinate permutation through `N=9`; for the antichain, `r(C)=|\mathrm{Aut}(C)|=N!`, so the quotient count is one.

This moves the next computational problem:

> from: enumerate all of `P_N`;
>
> to: count `r(C)` and `|\mathrm{Aut}(C)|` for the rare classes produced by split `S_N` audits.

The next concrete campaign is now:

1. sample `N=10,12` direct split clustered laws;
2. collect repeated positive rare classes;
3. compute exact `P_N(C)` for those selected classes using the realizer/aut formula;
4. decide whether their contribution survives or washes out.

### 9.50 Selected rare-class audit at `N=10` and the `N=12` canonicalization wall

The next receipt starts that campaign without substituting a sparse empirical denominator. It samples split clustered laws at `N=10`, collects repeated candidate classes, and computes exact selected denominators:

$$
P_N(C)=\frac{r(C)}{|\mathrm{Aut}(C)|\,N!}.
$$

The `N=10` scan uses `2048` samples per half and `4` split replicas for each schedule. The merged split supports are almost disjoint: the top candidates have counts only `2x1`, `1x2`, or `1x1` across `8192` samples per side. This is already evidence against a large repeated rare-class survivor.

For the half-scale and above, exact selected-denominator contributions are:

| schedule | largest selected contribution |
|---|---:|
| `linear_half` | `0.0270366668701` |
| `linear_one` | `0.0540733337402` |

The largest exact selected contribution among resolved half/one candidates is therefore:

$$
0.0540733337402.
$$

This is not a divergence signal. It is a small selected contribution from extremely sparse repeated hits.

For lower schedules the selected contributions are also small in this receipt:

| schedule | largest selected contribution |
|---|---:|
| `linear_quarter` | `0.0135183334351` |
| `linear_5_16` | `0.00675916671753` |
| `linear_3_8` | `0.0135183334351` |
| `linear_7_16` | `0.0135183334351` |

The `N=12` leg exposes the next computational wall. Exact unlabeled canonicalization is already costly enough that the receipt treats `N=12` as a feasibility boundary and does **not** replace exact `P_12(C)` with sparse empirical `P`. This is important: a sparse empirical denominator would produce another estimator, not the selected exact denominator needed for the likelihood question.

The new status is:

1. `N=10` selected rare classes are tractable by `r(C)/(|Aut(C)|N!)`;
2. the tested `N=10` half/one candidates have no large selected contribution;
3. `N=12` needs faster canonicalization and selected realizer/aut counting before the same audit can be trusted.

The next concrete algorithmic target is therefore:

> build faster canonicalization and realizer/aut counting for sampled `N=12` candidate classes, then repeat the selected contribution test without sparse empirical denominators.

### 9.51 `N=12` invariant-screen selected-count audit

The next receipt softens the `N=12` wall without pretending to solve it. It replaces full canonicalization of every sampled order by a two-stage screen:

1. group sampled orders by a cheap degree-block invariant;
2. only if a split-repeated invariant key appears, refine that group by exact isomorphism;
3. only if an exact repeated class appears, compute its selected denominator by

$$
P_N(C)=\frac{r(C)}{|\mathrm{Aut}(C)|\,N!}.
$$

The receipt samples `4096` orders per split side for four `N=12` schedules:

| schedule | invariant keys A | invariant keys B | overlap keys |
|---|---:|---:|---:|
| `linear_quarter` | `4096` | `4096` | `0` |
| `linear_5_16` | `4096` | `4096` | `0` |
| `linear_half` | `4096` | `4096` | `0` |
| `linear_one` | `4096` | `4096` | `0` |

So in this first `N=12` invariant-screen run, no split-repeated invariant key appears at all. That means no exact isomorphism class is promoted and no selected denominator is needed.

This is not a proof of washout. But it is evidence against an easy rare-class survivor: even a coarse invariant does not repeat across split samples at this size and sample count. It also confirms the algorithmic direction:

> raise the `N=12` sample size using cheap invariant grouping; if repeated keys appear, perform exact isomorphism and selected denominator counting only inside those keys.

The live wall is now practical rather than conceptual: sample enough `N=12` orders to see repeated invariant keys without falling back to sparse empirical `P_N`.

---

## 10. A sharper mathematical program

The campaign now points to a sharper theorem-shaped question:

> Given a finite transitive order whose global observables, exact finite-pattern densities, interval observables, interval-pair covariance structure, order-visible rooted/Palm neighborhood laws, Mecke/Palm deletion-increment compensators, and joint global/interval bracket field match the calibrated sprinkling null across scales, what non-manifold or non-Poisson-like orders remain feasible?

This should be attacked with tools from several fields:

- causal-set interval abundance and BDG layer actions;
- extremal poset theory and KR-style enumeration;
- poset limits and exchangeable random posets;
- flag-algebra/semidefinite methods for finite transitive pattern densities;
- topological data analysis on interval nerves;
- point-process regularity, multiscale empty-interval statistics, and Palm-style local laws, translated into order-only observables;
- quantum-information ideas only where they are conditional-on-interval, not naive spatial locality;
- cross-linked fiber/blow-up adversaries, where each manifoldlike point is replaced by a small non-manifold cloud but the construction is tuned to preserve the height law;
- staged-reservoir adversaries with enough cross-links to restore the MM pair density without producing interval-profile or overlap spikes;
- exact and approximate external-twin statistics, because distributed hidden fibers can evade the older load test;
- full finite-dimensional induced-pattern laws, because the density branch shows that small finite checklists can be tuned around;
- calibrated joint martingale brackets, because mean laws and local interval brackets can both be tuned;
- rooted/Palm record laws, because fixed-width hidden clusters have global pair mass `O(1/N)` but order-one hidden multiplicity from the viewpoint of a typical record;
- observability audits, because a hidden construction label is physically relevant only insofar as it leaves an order-visible causal signature;
- Mecke/Slivnyak-style deletion-increment compensators, because they are closer to a characterization of Poisson sprinkling than another finite feature checklist;
- asymptotic phase-boundary analysis for clustered coordinate processes, because high jitter can pass small finite projections and still separate at larger `N`;
- dimensionless scaling analysis, because the controlling parameter is not "jitter equals 4" but the relation between jitter scale, hidden width, base spacing, and `N`;
- a process-level classification of `Q_N(w_N,j_N)`, because the exponent audit shows that fixed-width and fixed-jitter statements are too narrow;
- a washout/residue dichotomy, because sufficiently large rank mixing can erase order-visible hidden-label structure in some finite projections, while other large-mixing cases remain visible;
- mesoscopic/full-law critical-window invariants, because fixed unrooted finite patterns provably wash out in the bounded-width linear window;
- square-root collision fields, because hidden sibling multiplicity first becomes order-one at `k=a sqrt(N)`;
- conditional projection of marked brackets onto the order sigma-field, because a marked residue is physically relevant only if `E[M_N | O_N]` remains nonzero;
- endpoint-symmetric, relabeling-invariant all-pair Palm-bracket U-statistics, because the oriented aggregate pair-Palm receipt exposed a tempting aggregate direction but the first invariant six-class repair did not recover the tested linear schedules;
- mesoscopic rooted pair-flag fields and exact unlabeled likelihood second moments, because the four/five-record flag ladder fails to robustly recover the tested linear-window schedules, the six-record hashed flag field is sample-design unstable, and the exact-`P_N` unlabeled cross-second-moment proxies at `N=6,8` stay inside sprinkling calibration after hostile null repair;
- two-replica hidden-partition overlap bounds, because bounded-width hidden partitions have only Poisson `O(1)` common-pair overlap;
- two-replica hidden-overlap graph cycle neutrality, because width-2 matchings have logarithmically many nonshared alternating components, so the boundedness theorem must either prove those cycles carry a summable transfer-operator tax or include them directly;
- transfer-operator/Fredholm determinant control, because a pair-factor likelihood with centered operator `A` gives nonshared cycle factors `1+tr(A^{2k})` and a finite tax `det(I-A^2)^(-1/2)` when the centered spectrum stays below one.
- split-sample and quotient-equivariance control, because the exact-`P_8` diagonal spike is produced by same-histogram reuse; after labels are forgotten, hidden-matching identity is not itself a record-visible event.
- direct split exact-denominator likelihood ladders, because after quotient-equivariance collapse the only honest full-law target is `S_N=sum_o q_N(o)^2/P_N(o)`, not hidden-explanation overlap bookkeeping.
- selected-class denominator formulas, because rare-order follow-up beyond `N=8` needs exact `P_N(C)` for chosen classes rather than sparse empirical denominators.

The most useful next formal object is now a **conditional rooted Mecke/Palm multiscale joint global-and-interval transitive bracket and likelihood problem**:

`Find or rule out non-manifold or clustered non-Poisson poset limits satisfying the same calibrated global observables, exact finite-pattern densities, recursive interval kernels, no-hidden-fiber/extensional tails, density-regularity laws, interval-pair covariance laws, order-visible rooted/Palm neighborhood laws, endpoint-symmetric relabeling-invariant all-pair Palm-bracket U-statistics, stabilized rooted pair-flag likelihood fields, Mecke/Palm deletion-increment compensators, joint global/interval covariance brackets, conditional marked-bracket projections, direct split/unbiased exact-denominator unlabeled order likelihood second moments, two-replica overlap-graph cycle-neutrality laws, transfer-operator determinant bounds, quotient-equivariance collapse constraints, and selected-class `P_N` probability formulas beyond `N=8` as 1+1 sprinklings.`

One concrete projection of that object is the soft external-neighborhood tail. For records `x,y`, define

$$
\Delta_C(x,y)=
\left|(P_x\setminus\{y\})\triangle(P_y\setminus\{x\})\right|
+
\left|(F_x\setminus\{y\})\triangle(F_y\setminus\{x\})\right|,
$$

where `P_x` and `F_x` are the past and future of `x`. Then define the finite-N tail

$$
T_C(\tau)=
\#\{\{x,y\}: \Delta_C(x,y)\le \tau\}.
$$

Exact twins are only `T_C(0)`. The twin-free motif adversary shows that `T_C(0)` can be repaired while `T_C(8)` and `T_C(16)` remain highly non-sprinkling-like. The target should therefore be a calibrated tail law, not just a zero-exact-twin rule.

The corresponding law-first object is not a list of thresholds but a joint empirical kernel with a rooted companion:

$$
\mathcal{K}_C =
\mathrm{Law}\left(
|I(x,y)|,\ C|_{I(x,y)},\ L_z,\ \Delta_C(u,v)
\right),
$$

sampled over records and intervals with the appropriate finite-N conditioning. The click law should make the sprinkling-like `\mathcal{K}_C` typical or low-action and make staged/fibered quotients high-action.

The rooted companion samples a typical record first:

$$
\mathcal{R}_C =
\mathrm{Law}_{x\sim C}
\left(
C|_{\mathrm{near}(x)},\
\Delta_C(x,y),\
|I(u,v)|,\
C|_{I(u,v)}
\right),
$$

where the exact definition of `near(x)` must be order-only and calibrated. The reason this companion is necessary is not aesthetic. For a fixed hidden cluster width `w`,

$$
\frac{\#\{\text{same-hidden-cluster pairs}\}}{\binom{N}{2}}
=
\frac{w-1}{N-1}
\to 0,
$$

while the rooted hidden multiplicity stays equal to `w-1`. A global pair law can lose the defect; a rooted law is the first place where the defect could remain visible.

The first rooted/Palm receipt adds the missing caveat. A hidden construction label is not automatically an order-visible defect. With jittered width `16`, the rooted hidden multiplicity is `15`, but the same-label fraction with `Delta <= tau` is only `0.000347222222222222222`. In that regime, the label has largely ceased to define a near-twin causal role. The law should not chase unobservable labels; it should constrain the induced order process.

The deletion-increment Mecke/Palm receipt adds the next caveat. It catches a gross density-modulated/Cox-like process with score/max `5.87295382945095778`, but all tested jittered width processes remain inside the finite null. The finite shadow is useful, but it is not the compensator itself.

The asymptotic jittered-cluster receipt adds the first phase-boundary signal. Exact triple-pattern densities and rooted features still let high-jitter clusters pass at `N=192` and `N=384`, but not at `N=768`, where jitter `4` has score/max `17.7158721626271524`. The phase-diagram receipt then varies the effective jitter scale and finds locked hidden-fiber, finite-camouflage, and later-reappearing visible phases. The exponent audit adds that hidden width and the scaling of the rank-mixing radius are independent controls: at `N=768`, fixed small jitter remains visible for `w=2,4,8`, while larger fixed or square-root-scale jitter can camouflage for some widths. Linear and superlinear washout receipts add the missing interpretation: some large-mixing generators become close to sprinkling in a finite empirical law-distance projection and lose order-visible same-label near twins, while others remain visible. The plausible next theorem is no longer a finite rejection theorem; it is a washout/residue classification theorem for clustered coordinate processes `Q_N(w_N,j_N)`.

The coordinate-jitter branch adds the density wall. Endpoint-load profiles, conditional endpoint residuals, and sampled size-4/5 induced-pattern densities still did not reject the best regularity-aware clustered candidate once finite-N sprinkling variability was calibrated. Interval brackets then catch that candidate, but bracket-tuned clusters reopen the problem. A finite joint global-and-interval bracket field rejects density-modulated and staged families and the original regularity-aware cluster, but tuned jittered clusters still sit inside the held-out null. A multiscale interval-pair covariance projection rejects density-modulated and staged families again, but still leaves tuned jitter clusters at finite scale and exposes a finite-null instability on a fresh `N=384` sprinkling. A compact stability audit improves conditioning but still leaks fresh sprinklings, and the fixed-width scaling calculation shows why unrooted global statistics alone cannot rule out hidden multiplicity asymptotically. A first rooted/Palm score is stable on fresh sprinklings but does not reject the jittered width sweep, because same-label hidden partners cease to be order-visible near twins. A deletion-increment score rejects gross density modulation but not jittered clustering. The scaling audits then show that high-jitter clustering can camouflage at one scale and reappear at another through exact triple-pattern/rooted signatures. This is evidence against treating any one finite projection as the click law.

The most dangerous next adversary is no longer the single reused block, a plain fiber blow-up, independent distributed staging, exact-twin decoration, bounded coordinate jitter, one more endpoint statistic, a local interval-bracket spoof, a finite interval-pair covariance score, an unrooted global empirical law, a finite rooted score, a finite deletion-increment score, a small-N jittered cluster, or any fixed unrooted finite-pattern law. It is a clustered-coordinate limit `Q_N(w_N,j_N)` that either matches the sprinkling law asymptotically by washing out its hidden structure, or matches all fixed unrooted finite projections while retaining a mesoscopic/full-law/order-compensator residue. The click law should penalize the second case, not the unobservable implementation history of the first.

---

## 11. Precision receipt

The receipt `v7/code/p23_recursive_interval_law.py` uses integer bitset counts for finite posets and mpmath `dps=140` for non-integer arithmetic. No float64 arithmetic is used for asserted quantities. The command used in this workspace is:

`isp/code/.venv/bin/python isp/v7/code/p23_recursive_interval_law.py`

Executed checks:

- full fixed-N interval histogram expectation sums to expected relation density: pass;
- full histogram expectation reproduces the generating-function expectation: pass;
- fixed sprinkling coarse interval histogram stays in a broad finite-N band: pass;
- fixed sprinkling recursive interval relation fraction is near `1/2`: pass;
- chain fails recursive interval relation fraction: pass;
- thin-middle adversary fails recursive interval relation fraction: pass;
- staged adversary keeps MM dimension in the 2D band: pass;
- staged adversary has 2D longest-chain height from the isolated chain: pass;
- staged adversary spoofs the recursive interval relation mean: pass;
- full interval histogram rejects the staged recursive-mean spoof: pass;
- fixed sprinkling has broad interior support in the tested band: pass;
- staged adversary has concentrated reused interiors: pass;
- load concentration separates staged adversary from sprinkling by a large factor: pass;
- fixed sprinkling all-interior load is close to the 2D continuum mean-field null: pass;
- staged all-interior load is far below the 2D continuum mean-field null: pass;
- fixed sprinkling sampled interior overlaps are not near-duplicate dominated: pass;
- staged sampled interior overlaps are near-duplicate dominated: pass;
- antichain fiber blow-up exposes hidden thickness by too-low height: pass;
- chain fiber blow-up exposes hidden thickness by too-high height: pass;
- fiber variants keep similar quotient MM scale but not the 1+1 height law: pass;
- distributed staging lowers exact duplicate concentration versus one reused block: pass;
- independent distributed staging pays by leaving the MM 2D band: pass;
- distributed staging still has concentrated overlap compared with sprinkling: pass;
- baseline sprinkling has negligible exact external twin pairs in this receipt: pass;
- tuned mixed fiber reaches the global height/MM band: pass;
- tuned mixed fiber is exposed by exact external twins: pass;
- tuned mixed fiber shifts the log-2 interval profile by more than five percent: pass;
- cross-linked staging search restores height but not the full 2D global profile: pass;
- cross-linked staging still has a visible module-middle histogram spike: pass;
- cross-linked staging has exact external twin classes: pass;
- decorated fiber reaches the broad global height/MM band: pass;
- single-tag decoration does not close the exact-twin opening: pass;
- single-tag decorated fiber is exposed by the soft near-twin tail: pass;
- decorated fiber still shifts the log-2 interval profile: pass;
- double-decorated fiber reaches the broad global height/MM band: pass;
- naive double decoration still does not close the exact-twin opening: pass;
- double-decorated fiber is still exposed by the soft near-twin tail: pass;
- double-decorated fiber still shifts the log-2 interval profile: pass;
- twin-free motif fiber reaches the broad global height/MM band: pass;
- twin-free motif sharply lowers exact twins relative to naive double decoration: pass;
- twin-free motif is still exposed by the soft near-twin tail: pass;
- twin-free motif closes exact-twin and log-2 scalar alarms: pass;
- rich random motif remains in a broad global height/MM band: pass;
- rich random motif search does not improve the soft `diff<=8` tail: pass;
- rich random motif still has excess near-twin mass over sprinkling: pass;
- rich random motif pays through interval profile or recursive-content drift: pass;
- bounded coordinate jitter remains in a broad global height/MM band: pass;
- bounded coordinate jitter reduces the soft `diff<=8` tail versus twin-free motifs: pass;
- bounded coordinate jitter still leaves excess near-twin mass over sprinkling: pass;
- over-jitter washout moves closer to the sprinkling soft tail: pass;
- over-jitter washout pays through density/profile drift or ceases to preserve hidden-cluster nearness: pass;
- regularity-aware clustered search matches the soft near-tail and scalar profile: pass;
- endpoint-load density projection is not enough against the regularity-aware cluster: pass;
- conditional endpoint residuals stay within calibrated finite sprinkling variability: pass;
- sampled small induced-pattern densities stay within finite sprinkling variability: pass.

Final receipt line:

`CHECKS PASSED: 55/55`.

Collapsed continuation receipts:

1. `v7/code/p24_projective_fixed_point_law.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p24_projective_fixed_point_law.py`

   Result:

   `CHECKS PASSED: 8/8`.

   Main checks:

   - fixed sprinkling is deletion-projective within finite sampled calibration: pass;
   - deletion-projective mean signatures are too weak to reject the clustered candidate: pass;
   - causally selected interval recursion is sharper than random deletion: pass;
   - interval-only recursion can be tuned below the fixed-sprinkling interval calibration: pass;
   - mean combined global-plus-interval scoring is still too weak in the bounded search: pass;
   - fluctuation/bracket data are independent information beyond mean interval signatures: pass.

2. `v7/code/p25_interval_bracket_action.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p25_interval_bracket_action.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - original clustered adversary is disfavored by the calibrated interval bracket action: pass;
   - mean-tuned adversary is still visible to the calibrated interval bracket action: pass;
   - bounded bracket-tuned clustered adversary still exists at that receipt resolution: pass;
   - bracket-tuned winner keeps hidden clustered multiplicity diagnostically: pass;
   - global full-size context is independent of the interval bracket score: pass.

3. `v7/code/p23_joint_global_interval_bracket.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_joint_global_interval_bracket.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - held-out null distribution is finite and nondegenerate: pass;
   - current interval-bracket-tuned adversary is explicitly ranked against the held-out null: pass;
   - joint action ranks the fixed sprinkling inside the held-out null support: pass;
   - broadened adversary menu is scored against the same held-out null: pass;
   - compression audit completed on the best broadened adversary: pass.

4. `v7/code/p23_multiscale_interval_pair_covariance.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_multiscale_interval_pair_covariance.py`

   Result:

   `CHECKS PASSED: 9/9`.

   Main checks:

   - `N=192` and `N=384` held-out interval-pair null distributions are finite and nondegenerate: pass;
   - fixed fresh sprinklings are explicitly ranked against the held-out interval-pair nulls: pass;
   - density-modulated and staged adversaries are rejected by interval-pair covariance at both tested scales: pass;
   - tuned jitter clusters remain inside at least one finite interval-pair null: pass;
   - interval-pair covariance is useful but not a complete click law: pass;
   - the finite interval-pair null exposes calibration instability or adversary leakage: pass.

5. `v7/code/p23_stability_adversarial_limit_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_stability_adversarial_limit_audit.py`

   Result:

   `CHECKS PASSED: 11/11`.

   Main checks:

   - compact held-out interval-pair nulls at `N=192` and `N=384` are finite and nondegenerate: pass;
   - compact fresh-sprinkling rank audits are bounded but not leakage-free: pass;
   - surviving jittered clusters are explicitly ranked by the compact action: pass;
   - compact projection reduces but does not eliminate finite calibration leakage: pass;
   - fixed-width hidden-pair mass decays like `1/N` in unrooted pair statistics: pass;
   - rooted hidden multiplicity remains order-one for fixed hidden width: pass;
   - order-only near-root excess is not a reliable complete detector at finite scale: pass;
   - the adversarial-limit audit shifts the target to rooted/Palm or process-level laws: pass.

6. `v7/code/p23_rooted_palm_bracket_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_rooted_palm_bracket_audit.py`

   Result:

   `CHECKS PASSED: 7/7`.

   Main checks:

   - rooted/Palm held-out null is finite and nondegenerate: pass;
   - rooted/Palm projection gives a bounded fresh-sprinkling rank audit: pass;
   - finite rooted/Palm action does not reject the jittered width sweep: pass;
   - fixed small hidden widths can remain inside the finite rooted/Palm null: pass;
   - jittered hidden labels are not the same as order-visible near twins: pass;
   - rooted hidden multiplicity grows while global pair mass can stay small: pass;
   - rooted/Palm audit is necessary but not yet a complete click law: pass.

7. `v7/code/p23_mecke_palm_poisson_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_mecke_palm_poisson_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - Mecke/Palm held-out null is finite and nondegenerate: pass;
   - Mecke/Palm projection gives a bounded fresh-sprinkling rank audit: pass;
   - Mecke/Palm compensator explicitly ranks jittered clustered processes: pass;
   - order-only Mecke/Palm score is a diagnostic projection, not a complete law: pass;
   - the audit keeps non-Poisson/Cox alternatives on the target list: pass.

8. `v7/code/p23_asymptotic_jittered_cluster_limit_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_asymptotic_jittered_cluster_limit_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact three-record pattern densities partition every audited poset: pass;
   - low-jitter hidden fibers remain order-visible in the scaling audit: pass;
   - high jitter reduces same-label near-twin visibility: pass;
   - high-jitter clustered orders are not eliminated by this finite asymptotic projection at all tested smaller scales: pass;
   - the scaling audit leaves a phase-boundary problem rather than a completed law: pass.

9. `v7/code/p23_jitter_scaling_phase_diagram.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_jitter_scaling_phase_diagram.py`

   Result:

   `CHECKS PASSED: 6/6`.

   Main checks:

   - exact three-record pattern densities partition every audited poset: pass;
   - locked hidden fibers are separated at every tested scale: pass;
   - same-label near-twin visibility decreases as jitter scale increases: pass;
   - at least one high-jitter schedule has finite camouflage at small `N` and separates later: pass;
   - the tested diagram has a nontrivial phase boundary rather than one universal score cutoff: pass;
   - no tested fixed-jitter schedule proves full washout across all scales: pass.

10. `v7/code/p23_jitter_scaling_exponent_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_jitter_scaling_exponent_audit.py`

   Result:

   `CHECKS PASSED: 6/6`.

   Main checks:

   - exact three-record pattern densities partition every audited poset: pass;
   - at least one exponent schedule changes phase across tested `N` at fixed width: pass;
   - width is an independent control parameter at fixed `N` and exponent schedule: pass;
   - the largest tested scale still contains both visible and camouflage regimes: pass;
   - fixed small jitter is not uniformly washed out at the largest tested scale: pass;
   - large square-root-scale jitter is not uniformly separated at the largest tested scale: pass.

11. `v7/code/p23_jitter_linear_washout_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_jitter_linear_washout_audit.py`

   Result:

   `CHECKS PASSED: 7/7`.

   Main checks:

   - exact three-record pattern densities partition every audited poset: pass;
   - same-label near-twin visibility is not a monotone one-parameter curve in finite samples: pass;
   - fixed small jitter remains order-visible at the largest tested scale: pass;
   - linear-scale jitter can enter finite camouflage at the largest tested scale: pass;
   - linear and superlinear mixing erase order-visible same-label near twins at the largest scale: pass;
   - superlinear mixing is not automatically a better finite match than linear mixing: pass;
   - at least one linear or superlinear schedule changes phase across tested `N`: pass.

12. `v7/code/p23_washout_two_sample_distance_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_washout_two_sample_distance_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact three-record pattern densities partition every audited poset: pass;
   - fixed small jitter is two-sample visible in at least one tested case: pass;
   - at `N=768` at least one linear/superlinear washed family is inside the two-sample null: pass;
   - washed families at `N=768` have negligible same-label near-twin visibility: pass;
   - large mixing is not a theorem-level guarantee in this finite projection: pass.

13. `v7/code/p23_washout_residue_dichotomy_bounds.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_washout_residue_dichotomy_bounds.py`

   Result:

   `CHECKS PASSED: 6/6`.

   Main checks:

   - unrooted same-cluster pair mass vanishes while rooted multiplicity stays order-one: pass;
   - residue witness exists for tested exponent schedules below one half: pass;
   - the `alpha=1/2` boundary is not covered by the residue witness: pass;
   - a sufficient full-record washout bound tends to zero for `J_N=N^gamma`, `gamma>2`: pass;
   - fixed-k center/noise ratio tends to zero for `J_N=N^gamma`, `gamma>1`: pass;
   - linear mixing is a genuine critical window for this proof: pass.

14. `v7/code/p23_linear_critical_kernel_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_linear_critical_kernel_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - fixed-k hidden-cluster collision probability vanishes for bounded width: pass;
   - the no-collision three-record law equals the `1+1` sprinkling triple law: pass;
   - pair relation probability is exactly one quarter after rank symmetrization: pass;
   - positive linear jitter destroys microscopic same-cluster nearness: pass;
   - the linear critical window cannot be settled by fixed unrooted finite patterns: pass.

15. `v7/code/p23_linear_window_interval_variance_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_linear_window_interval_variance_audit.py`

   Result:

   `CHECKS PASSED: 4/4`.

   Main checks:

   - mesoscopic interval-size law sees at least one linear-window clustered family at `N=384`: pass;
   - interval-size projection is not a complete critical-window classifier: pass;
   - at `N=768`, interval-size moments can wash out all tested linear-window residue: pass;
   - critical-window visibility depends on width and mixing scale, not only fixed patterns: pass.

16. `v7/code/p23_linear_window_load_bracket_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_linear_window_load_bracket_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - load/bracket projection has a nonempty finite camouflage set: pass;
   - load/bracket projection has a nonempty finite visible set: pass;
   - at `N=768`, finite load/bracket projection is not a complete classifier: pass;
   - at `N=768`, finite load/bracket projection still sees one marginal residue: pass;
   - critical-window bracket visibility depends on width and mixing scale: pass.

17. `v7/code/p23_observable_label_information_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_observable_label_information_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pseudo-label null has near-random order-only separability: pass;
   - locked or small-jitter hidden clusters leave order-visible label residue: pass;
   - at least one linear-window schedule washes hidden labels to pseudo-label separability: pass;
   - at least one non-locked schedule remains order-visible in this finite projection: pass;
   - observable-label audit splits hidden implementation from record-law residue: pass.

18. `v7/code/p23_higher_order_label_residue_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_higher_order_label_residue_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pseudo-label triple null has near-random order-only separability: pass;
   - locked or fixed-jitter same-label triples leave higher-order residue: pass;
   - linear-window schedules remain pseudo-label-like in this triple projection: pass;
   - triple audit does not close the higher-order gap: pass;
   - residue boundary remains between square-root and linear mixing in this projection: pass.

19. `v7/code/p23_observable_law_metric_campaign.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_observable_law_metric_campaign.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - observable projection metric is nondegenerate on sprinklings: pass;
   - low or square-root jitter remains visible in the observable projection metric: pass;
   - at least one linear-window schedule remains inside the observable projection null: pass;
   - metric campaign either extracts a linear residue or records linear washout: pass;
   - observable-law distance is a projection, not a complete proof of equivalence: pass.

20. `v7/code/p23_degree_covariance_label_residue_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_degree_covariance_label_residue_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pseudo-label degree-covariance null is near random: pass;
   - low-jitter degree covariance is order-visible: pass;
   - degree covariance tests the remaining linear-window opening: pass;
   - at least one linear schedule is classified by the degree-covariance audit: pass;
   - degree covariance either promotes a residue or confirms finite washout: pass.

21. `v7/code/p23_asymptotic_bracket_identity.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_asymptotic_bracket_identity.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - finite mixing ratio has positive marked sibling bracket: pass;
   - marked sibling bracket decreases across the tested large-mixing tail: pass;
   - strong mixing drives the marked bracket toward the iid value: pass;
   - linear `c=2` still has a nonzero marked bracket residue: pass;
   - receipt distinguishes marked bracket residue from finite feature washout: pass.

22. `v7/code/p23_order_visible_bracket_variance_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_order_visible_bracket_variance_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - order-visible bracket null is nondegenerate: pass;
   - low or square-root jitter is visible to the order-visible bracket audit: pass;
   - bracket audit follows the linear-window opening: pass;
   - at least one linear schedule remains bracket-camouflaged or a residue is promoted: pass;
   - order-visible bracket variance is still a finite projection: pass.

23. `v7/code/p23_reconstructed_coordinate_palm_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_reconstructed_coordinate_palm_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pseudo-label reconstructed-coordinate null is near random: pass;
   - low-jitter reconstructed coordinates are order-visible: pass;
   - reconstructed coordinates test the linear-window marked-bracket opening: pass;
   - at least one linear schedule remains reconstructed-coordinate camouflaged or a residue is promoted: pass;
   - the audit distinguishes order reconstruction from original coordinate marks: pass.

24. `v7/code/p23_growing_window_washout_bounds.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_growing_window_washout_bounds.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - sibling-collision bound decreases across tested `N` for every beta below one half: pass;
   - subcritical `beta=0.49` converges slowly and is still order-one at `N=1e8`: pass;
   - critical `beta=1/2` does not vanish in this bound: pass;
   - supercritical beta has a growing collision obstruction: pass;
   - theorem is a growing-window washout result, not full contiguity: pass.

25. `v7/code/p23_sqrt_collision_poisson_law.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_sqrt_collision_poisson_law.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - square-root mean tends to `lambda=a^2(w-1)/2`: pass;
   - second factorial moment is Poisson-like at the largest tested `N`: pass;
   - exact no-collision probability is asymptotic to `exp(-lambda)`: pass;
   - critical field is order-one, unlike the `o(sqrt(N))` washout field: pass;
   - law is marked and therefore only locates the possible order-only residue scale: pass.

26. `v7/code/p23_hidden_partition_likelihood_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_hidden_partition_likelihood_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pseudo-label top-tail enrichment is finite: pass;
   - low-jitter hidden partition is recoverable by an order-only top-tail score: pass;
   - top-tail audit tests the linear-window hidden-partition opening: pass;
   - at least one linear schedule remains top-tail camouflaged or the opening is promoted: pass;
   - audit is order-only but not a full likelihood-ratio theorem: pass.

27. `v7/code/p23_palm_kernel_projection_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_palm_kernel_projection_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pair comparability projection is exactly null: pass;
   - three-record Palm-kernel audit was run at high precision ratios: pass;
   - local Palm-kernel opening is classified by the receipt: pass;
   - finite Monte Carlo noise is calibrated by an iid Monte Carlo control: pass;
   - result does not prove or refute full order-only contiguity: pass.

28. `v7/code/p23_exact_palm_kernel_integral.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_exact_palm_kernel_integral.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - independent one-axis law is recovered when `q=1/3`: pass;
   - finite `c` has a nonzero exact local Palm triple residue: pass;
   - residue decreases along the tested large-mixing tail: pass;
   - exact `c=0.5` signal matches the Monte Carlo Palm-kernel scale: pass;
   - exact `c=1` residue is real but small enough to be hidden by the previous Monte Carlo control: pass.

29. `v7/code/p23_pair_palm_signature_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_pair_palm_signature_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - pseudo-label pair-Palm null remains near random: pass;
   - low-jitter pair-Palm signature is order-visible: pass;
   - square-root pair-Palm signature is tested at the collision boundary: pass;
   - linear-window pair-Palm signature opening is classified: pass;
   - audit is still a finite projection of the exact Palm kernel: pass.

30. `v7/code/p23_aggregate_pair_palm_bracket_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_aggregate_pair_palm_bracket_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - held-out sprinkling aggregate pair-Palm bracket is finite: pass;
   - low-jitter aggregate pair-Palm bracket is visible: pass;
   - square-root aggregate pair-Palm bracket is tested at the collision boundary: pass;
   - linear aggregate pair-Palm opening is classified: pass;
   - receipt remains a finite aggregate bracket, not a likelihood-ratio theorem: pass.

31. `v7/code/p23_aggregate_pair_palm_source_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_aggregate_pair_palm_source_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - held-out sprinkling source audit has finite null: pass;
   - hidden-pair-only scores are visible when evaluated as a Palm source: pass;
   - linear non-hidden pairs remain visible or the signal is sparse-hidden dominated: pass;
   - source of the aggregate signal is classified: pass;
   - this is a finite source audit, not an asymptotic decomposition: pass.

32. `v7/code/p23_invariant_aggregate_pair_palm_bracket_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_invariant_aggregate_pair_palm_bracket_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - held-out endpoint-invariant sprinkling bracket is finite: pass;
   - endpoint-invariant low-jitter bracket is classified under the held-out null: pass;
   - endpoint-invariant linear opening is classified: pass;
   - endpoint-invariant vector survives random record relabeling: pass;
   - receipt repairs endpoint-order leakage from the previous aggregate bracket: pass.

33. `v7/code/p23_endpoint_symmetric_pair_flag_likelihood_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_endpoint_symmetric_pair_flag_likelihood_audit.py`

   Result:

   `CHECKS PASSED: 7/7`.

   Main checks:

   - four-record rooted pair flags are endpoint and relabel invariant: pass;
   - independent four-record rooted pair flags are endpoint and relabel invariant: pass;
   - five-record rooted pair flags are endpoint and relabel invariant: pass;
   - four-record pair-flag likelihood opening is classified: pass;
   - independent four-record follow-up tests the weak visibility opening: pass;
   - five-record follow-up is classified before the next review pass: pass;
   - receipt distinguishes invariant flag likelihoods from the rejected oriented endpoint score: pass.

34. `v7/code/p23_mesoscopic_rooted_flag_field_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_mesoscopic_rooted_flag_field_audit.py`

   Result:

   `CHECKS PASSED: 6/6`.

   Main checks:

   - primary mesoscopic rooted flag field is endpoint and relabel invariant: pass;
   - independent mesoscopic rooted flag field is endpoint and relabel invariant: pass;
   - primary mesoscopic linear opening is classified: pass;
   - independent mesoscopic follow-up is classified before next review pass: pass;
   - any promoted mesoscopic linear signal survives the independent repeat or is demoted: pass;
   - receipt follows the rooted-flag opening beyond four/five records: pass.

35. `v7/code/p23_small_unlabeled_likelihood_second_moment.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_small_unlabeled_likelihood_second_moment.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact `N=6` sprinkling law is normalized on unlabeled codes: pass;
   - empirical sprinkling second-moment null is finite: pass;
   - clustered small-N likelihood opening is classified: pass;
   - canonical unlabeled code survives random relabeling: pass;
   - receipt is an exact small-N proxy, not the critical-window theorem: pass.

36. `v7/code/p23_unlabeled_second_moment_ladder.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_unlabeled_second_moment_ladder.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact unlabeled `P` laws are computed and normalized: pass;
   - canonical unlabeled code survives random relabeling in the ladder: pass;
   - `N=6` two-replica linear opening is classified: pass;
   - `N=8` two-replica linear opening is classified: pass;
   - receipt estimates a cross second moment rather than a one-sample square: pass.

37. `v7/code/p23_unlabeled_second_moment_n8_stability.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_unlabeled_second_moment_n8_stability.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact `P_8` law is computed and canonical code is relabel invariant: pass;
   - centered `N=8` null guard is finite and nonnegative: pass;
   - `N=8` stability audit classifies the linear schedules: pass;
   - top contributing unlabeled classes are reported for the linear schedules: pass;
   - audit repairs the negative-null-max opening from the first ladder: pass.

38. `v7/code/p23_unlabeled_rare_class_stability_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_unlabeled_rare_class_stability_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact `P_8` rare-class projections are computed: pass;
   - individual-code rare-class search is classified: pass;
   - structural-group rare-class search is classified: pass;
   - stable rare-class candidates are either found or explicitly absent: pass;
   - receipt targets rare classes rather than another arbitrary feature vector: pass.

39. `v7/code/p23_partition_overlap_poisson_bound.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_partition_overlap_poisson_bound.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - specified-pair probability recovers the exact `r=1` formula: pass;
   - leading disjoint factorial moments approach Poisson targets: pass;
   - overlap intensity is `O(1)` for bounded width: pass;
   - Poisson-overlap moment-generating function is finite for fixed overlap weight: pass;
   - receipt supplies the overlap tax, not the full likelihood theorem: pass.

40. `v7/code/p23_local_factor_inequality_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_local_factor_inequality_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact labeled `P_N` supports are computed: pass;
   - sampled conditional `Q_H` support stays inside exact labeled sprinkling support: pass;
   - finite overlap-dominated constants fit every tested `H,H'` pair: pass;
   - fitted constants are finite in the exact small-size audit: pass;
   - no single rare zero-overlap order class dominates the worst zero-overlap cross factor: pass.

41. `v7/code/p23_overlap_graph_cycle_tax.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_overlap_graph_cycle_tax.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - common-pair component has exact `O(1)` mean: pass;
   - fixed-`k` component means approach `1/(2k)`: pass;
   - total alternating component mean grows logarithmically: pass;
   - nonshared cycle mean is not controlled by common-pair overlap: pass;
   - receipt identifies the missing neutrality condition: pass.

42. `v7/code/p23_cycle_neutrality_signature_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_cycle_neutrality_signature_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact unlabeled `P_8` law and all hidden matchings are used: pass;
   - conditional samples stay inside exact unlabeled `P_8` support: pass;
   - all width-2 overlap graph signatures at `N=8` are covered: pass;
   - zero-common signature means stay near the null scale: pass;
   - two zero-common cycles do not show a larger mean factor than one zero-common cycle: pass.

43. `v7/code/p23_overlap_graph_mgf_bound.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_overlap_graph_mgf_bound.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - component mgf derivative matches the exact component mean: pass;
   - fixed nonshared-component factor grows with `m`: pass;
   - fixed factor growth matches the polynomial exponent scale: pass;
   - log-neutral component factors have bounded tested mgf: pass;
   - strict-neutral component factors tend back toward one: pass.

44. `v7/code/p23_transfer_operator_cycle_theorem.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_transfer_operator_cycle_theorem.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - neutral beta gives exact expectation one: pass;
   - one-mode finite expectations converge to determinant cycle tax: pass;
   - multi-mode finite expectation converges to product determinant tax: pass;
   - spectral radius below one gives finite cycle tax: pass;
   - approaching spectral radius one exposes the divergence mechanism: pass.

45. `v7/code/p23_overlap_component_factorization_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_overlap_component_factorization_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - exact `P_8` support and all matchings are used: pass;
   - conditional samples remain inside exact `P_8` support: pass;
   - naive multiplicative component factorization is rejected: pass;
   - all non-identical overlap signatures stay near the null mean: pass;
   - the full-identity spike is rare after averaging over hidden matchings: pass.

46. `v7/code/p23_diagonal_identity_rarity_bound.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_diagonal_identity_rarity_bound.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - Stirling matching asymptotic is accurate at large `m`: pass;
   - polynomial diagonal spikes are killed: pass;
   - fixed exponential diagonal spikes are killed: pass;
   - sub-`m log m` diagonal spikes are killed: pass;
   - a matching-count-scale diagonal spike is the dangerous threshold: pass.

47. `v7/code/p23_split_sample_diagonal_artifact_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_split_sample_diagonal_artifact_audit.py`

   Result:

   `CHECKS PASSED: 8/8`.

   Main checks:

   - exact `P_8` support and all matchings are used: pass;
   - conditional samples remain inside exact `P_8` support: pass;
   - exact zero-jitter clustered law has real unlabeled likelihood excess: pass;
   - same-histogram reuse creates a large artificial diagonal spike: pass;
   - split same-`H` diagonal returns to split different-`H` scale: pass;
   - split estimates stay near the null second-moment scale: pass;
   - non-identical overlap signatures are flat under split estimation: pass;
   - linear-jitter split likelihood is much closer to null than zero-jitter clustering: pass.

48. `v7/code/p23_direct_unlabeled_likelihood_ladder.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_direct_unlabeled_likelihood_ladder.py`

   Result:

   `CHECKS PASSED: 7/7`.

   Main checks:

   - exact `P_8` law is computed and canonical code is relabel invariant: pass;
   - exact zero-jitter clustered law has large direct unlabeled second moment: pass;
   - split null guard is finite and calibrated: pass;
   - linear half/one/two direct split estimates stay inside the hostile null guard: pass;
   - the finite `N=8` boundary opening is followed below linear half: pass;
   - no stable large rare-order contribution survives in the linear split ladder: pass;
   - the `N=10,12` exact denominator barrier is explicitly not bypassed by sparse empirical `P`: pass.

49. `v7/code/p23_selected_class_probability_formula.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_selected_class_probability_formula.py`

   Result:

   `CHECKS PASSED: 4/4`.

   Main checks:

   - selected-class formula matches every exact class for `N<=6`: pass;
   - selected-class formula matches a hostile `N=8` sample: pass;
   - chain and antichain probabilities reduce to one coordinate permutation: pass;
   - the formula exposes the exact denominator task beyond `N=8`: pass.

50. `v7/code/p23_selected_rare_class_n10_n12_audit.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_selected_rare_class_n10_n12_audit.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - candidate classes are collected for `N=10` and the `N=12` feasibility scan completes: pass;
   - at least one `N=10` candidate receives an exact selected denominator: pass;
   - the audit handles `N=12` without sparse empirical `P`: pass;
   - resolved half/one candidates do not show a large selected contribution: pass;
   - unresolved selected denominators are reported rather than replaced by empirical `P`: pass.

51. `v7/code/p23_n12_invariant_screen_selected_count.py`

   Command:

   `isp/code/.venv/bin/python isp/v7/code/p23_n12_invariant_screen_selected_count.py`

   Result:

   `CHECKS PASSED: 5/5`.

   Main checks:

   - `N=12` invariant screen completes without full canonicalization: pass;
   - repeated invariant keys are examined when present, otherwise absence is explicit: pass;
   - repeated exact classes receive selected denominators or the absence is explicit: pass;
   - resolved half/one `N=12` selected contributions are not large: pass;
   - no sparse empirical `P_N` denominator is used: pass.

Across the collapsed Paper 23 receipt suite:

`CHECKS PASSED: 341/341`.

---

## 12. Claims and non-claims

**Claims.**

1. The exact fixed-N 1+1 expectation for the full interval-size histogram is derived and receipt-checked. **[STRESS TEST]**

2. First-order interval abundance, even as a full histogram, is too shallow because it does not inspect the order inside intervals. **[CONSTRAINED]**

3. A first recursive interval statistic catches the chain and thin-middle adversaries that first-order statistics can miss. **[STRESS TEST]**

4. A staged order with one reused first-order-good middle block can pass MM dimension, correct 1+1 height scale, and the pooled recursive interval relation mean, while failing the full interval histogram and deeper heredity. **[COUNTEREXAMPLE]**

5. Interior-load concentration, a 1+1 continuum load null, and sampled soft-overlap statistics expose that staged reuse in the tested finite examples. **[STRESS TEST]**

6. Plain fiber blow-ups are detected by the height law even when their quotient-looking MM scale and recursive mean are tolerable in the finite receipt. **[STRESS TEST]**

7. A tuned mixed two-fiber adversary can match the global height scale, keep MM dimension within a broad 2D band, and evade the older load/overlap alarm, but is still exposed by a shifted interval profile and many external-twin pairs. **[STRESS TEST / CONSTRAINED]**

8. A twin-free local motif can close the exact-twin alarm and the log-2 scalar interval-profile alarm while preserving broad global statistics, but it leaves a large soft near-twin tail. **[STRESS TEST / CONSTRAINED]**

9. Rich random local motifs up to width `16` do not reduce the tested soft near-tail in the broad global band and pay interval-profile or recursive-content drift in the receipt. **[STRESS TEST]**

10. Bounded coordinate jitter can greatly reduce the hidden-fiber soft near-tail while preserving strong scalar profiles, but in this receipt it still leaves excess `diff<=8` mass over sprinkling; over-jitter can match the tail only by washing out hidden-cluster nearness and becoming a clustered coordinate process. **[STRESS TEST / CONSTRAINED]**

11. A regularity-aware and pattern-aware clustered search can tune the soft near-tail, endpoint-load profile, conditional endpoint residuals, and sampled small-pattern densities into finite sprinkling variability while preserving strong scalar profiles. This is evidence against a small finite diagnostic checklist and for a full finite-dimensional record law. **[STRESS TEST / CONSTRAINED]**

12. Independent and cross-linked staged reservoirs reduce some exact duplicate signals but pay through MM, recursive-content, histogram, or external-twin costs in the tested finite families. **[STRESS TEST]**

13. The click-law target should be upgraded to a specific recursive record law whose projections include hereditary interval statistics, no-hidden-staging/overlap concentration, a soft no-hidden-fiber/extensional tail law, and a full calibrated density/regularity law, not merely a full interval generating function or finite checklist. **[CONSTRAINED / OPEN]**

14. Random deletion projectivity is too geometry-blind; causally selected interval recursion is sharper, but interval mean signatures can still be tuned by coordinate-jitter clusters. **[STRESS TEST / COUNTEREXAMPLE]**

15. A calibrated interval-bracket action catches the regularity-aware cluster and the mean-tuned cluster, but a bracket-tuned clustered adversary beats the interval-only bracket score at finite search resolution. **[STRESS TEST / COUNTEREXAMPLE]**

16. A better-conditioned 47-dimensional joint global-and-interval bracket projection rejects density-modulated and staged families and the original regularity-aware cluster, but tuned jittered clusters remain inside the held-out null. **[STRESS TEST / CONSTRAINED]**

17. A multiscale 59-dimensional interval-pair covariance projection rejects density-modulated and staged adversaries at `N=192` and `N=384`, but tuned jitter clusters remain inside at least one finite held-out null and the `N=384` fresh sprinkling exposes finite calibration instability. **[STRESS TEST / CONSTRAINED]**

18. A compact 32-dimensional interval-pair projection improves conditioning but still leaks fresh sprinklings above the held-out maximum: `1/12` at `N=192` and `2/12` at `N=384` in the receipt. **[STRESS TEST / CONSTRAINED]**

19. Fixed-width hidden clusters are asymptotically invisible to unrooted global pair statistics: for width `w`, the same-hidden-cluster pair fraction is `(w-1)/(N-1)`, while the rooted hidden multiplicity remains `w-1`. **[PRINCIPLE / COUNTEREXAMPLE]**

20. A first 36-dimensional rooted/Palm projection is stable on fresh sprinklings at `N=384` but does not reject the jittered hidden-width sweep up to width `16`; same hidden construction labels cease to be order-visible near twins under sufficient jitter. **[STRESS TEST / COUNTEREXAMPLE]**

21. A finite order-only deletion-increment Mecke/Palm projection rejects a gross density-modulated/Cox-like process at score/max `5.87295382945095778`, but all tested jittered width processes remain inside the held-out null. **[STRESS TEST / CONSTRAINED]**

22. Exact full three-record pattern densities plus rooted/global interval features reveal a scaling separation for jittered clusters: jitter `4` is inside the finite null at `N=192,384` but has score/max `17.7158721626271524` at `N=768`. **[STRESS TEST / CONSTRAINED]**

23. A finite jitter phase diagram at width `4` separates locked hidden-fiber, finite-camouflage, and later-reappearing visible regimes; no tested fixed-jitter schedule proves full washout across `N=192,384,768`. **[STRESS TEST / CONSTRAINED]**

24. A finite exponent audit over `w=2,4,8` and schedules `j_N=4,16,\sqrt{N}/2,\sqrt{N},2\sqrt{N},N/24` shows that the phase boundary is not controlled by raw jitter alone. Hidden width, effective rank-mixing radius, and `N` remain independent controls. **[STRESS TEST / CONSTRAINED]**

25. A linear/superlinear washout audit shows that sufficiently large rank mixing can erase same-label near-twin visibility and enter finite camouflage, but the finite phase is nonmonotone: increasing the mixing radius is not automatically a better match. **[STRESS TEST / CONSTRAINED]**

26. A two-sample empirical law-distance audit supports a washout/residue split. At `N=768`, fixed small jitter is visible for `w=2,4,8`; `N`-scale mixing is inside the two-sample null for `w=2` and `w=8` but not `w=4`; and `2N`-scale mixing is inside for `w=2` but not `w=4` or `w=8`. **[STRESS TEST / CONSTRAINED]**

27. A partial washout/residue theorem is proved for the clustered-coordinate generator. If `w_NJ_N=o(\sqrt N)`, hidden clusters leave a rooted/Palm residue. If `J_N\gg N^2/w_N`, the full record-order law converges to sprinkling by a product-TV coupling. Fixed-k unrooted laws wash out already when `m_N/J_N\to0`. **[PRINCIPLE / CONSTRAINED]**

28. In the bounded-width linear critical window `J_N/m_N\to L\in(0,\infty)`, every fixed unrooted `k`-record pattern law converges to the `1+1` sprinkling law, while same-hidden-cluster records are no longer microscopic near twins. **[PRINCIPLE / CONSTRAINED]**

29. A mesoscopic interval-size audit shows that interval-size moments can see one smaller-scale linear-window family, but at `N=768` all tested linear-window families lie inside the finite interval-size null; the largest ratio is `0.958659265823868755`. **[STRESS TEST / CONSTRAINED]**

30. A 38-dimensional order-visible load/bracket audit restores only a weak partial `N=768` signal: `w=4`, `J_N=2N` has score/null `1.03424395062355414`, while many linear-window families remain camouflaged. **[STRESS TEST / CONSTRAINED]**

31. An observable-label information audit separates hidden implementation labels from record-law residue. At `N=768`, `w=4`, pseudo-label null max separability is `0.555891036987304688`; locked and fixed-jitter clusters are strongly visible (`1.0` and `0.976752853393554687`), square-root jitter is marginally visible (`0.632798576354980469`), and linear schedules are pseudo-label-like (`0.527651023864746094`, `0.520104789733886719`, `0.521009635925292969`). **[STRESS TEST / CONSTRAINED]**

32. A higher-order label audit tests same-hidden-label triples. At `N=768`, `w=4`, pseudo-label triple null max separability is `0.5662841796875`; locked, fixed-jitter, and square-root clusters are visible (`1.0`, `0.998500823974609375`, `0.693152109781901042`), while linear schedules remain pseudo-label-like (`0.544464111328125`, `0.539515177408854167`, `0.538472493489583333`). **[STRESS TEST / CONSTRAINED]**

33. A 46-dimensional observable-law projection metric combining global, rooted, interval, and load/bracket features detects fixed jitter (`1.44038658269306445`) and barely detects square-root jitter (`1.00326969267651185`), but all tested linear schedules remain inside the finite null (`0.978544975839934245`, `0.880571672298325785`, `0.829118899870470496`). **[STRESS TEST / CONSTRAINED]**

34. A degree-covariance audit tests the plausible shared-center leak. It detects fixed and square-root jitter, but all tested linear schedules remain pseudo-label-like in pair and triple degree-covariance features. **[STRESS TEST / CONSTRAINED]**

35. A marked-coordinate asymptotic bracket identity is derived and receipt-checked. For finite mixing ratio `c`, sibling clusters contribute `(w-1)B(c)` to `N Var(N^{-1}\sum R_i)`, with `B(2)=0.004456535218253968253968253968253968253968`; as `c\to\infty`, the bracket tends to the iid value `1/12`. **[PRINCIPLE / CONSTRAINED]**

36. A finite order-visible bracket-variance audit does not recover the marked coordinate-bracket residue in the tested linear schedules. Fixed jitter is visible, but `J=N/2`, `J=N`, and `J=2N` remain inside the calibrated null. **[STRESS TEST / CONSTRAINED]**

37. A reconstructed-coordinate Palm audit uses only order-visible past and future degrees to estimate the unordered lightcone pair `{u,v}`. It detects fixed jitter and barely detects square-root jitter, but the tested linear schedules remain pseudo-label-like. **[STRESS TEST / CONSTRAINED]**

38. A growing-window washout theorem is proved for bounded hidden width in the linear window. A uniformly sampled `k_N`-record induced suborder has sibling-collision probability at most `binom(k_N,2)(w-1)/(N-1)`, so every sampled `k_N=o(sqrt(N))` induced-suborder test is asymptotically blind after conditioning on the no-collision rank-kernel convergence. **[PRINCIPLE / CONSTRAINED]**

39. The square-root collision law is derived and receipt-checked. For `k=floor(a sqrt(N))`, hidden sibling collisions have mean tending to `a^2(w-1)/2`, second factorial moment tending to the square of that mean, and no-collision probability asymptotic to `exp(-a^2(w-1)/2)`. **[PRINCIPLE / CONSTRAINED]**

40. A simple full-order hidden-partition top-tail likelihood recovers fixed and square-root schedules but not the tested linear schedules. At `N=768`, `w=4`, the pseudo-label top-tail guard is `1.63185763888888889`; fixed jitter has mean enrichment `19.6780478395061728`, square-root jitter `2.14535108024691358`, and the tested linear schedules remain near null (`1.11706211419753086`, `1.0800733024691358`, `1.08747106481481481`). **[STRESS TEST / CONSTRAINED]**

41. The local Palm-kernel projection splits. The sibling-pair comparability kernel is exactly the iid pair kernel, but the sibling-plus-outsider triple Palm kernel is visible at mixing ratio `c=0.5` and falls inside the iid Monte Carlo control by `c=1,2,4` in the receipt. **[STRESS TEST / CONSTRAINED]**

42. The exact local Palm integral proves the sibling-plus-outsider triple residue is nonzero for every tested finite `c`. The L1 gap is `0.03` at `c=0.5`, `1/300` at `c=1`, and `0.000263671875` at `c=2`, decaying rapidly toward zero as mixing grows. **[PRINCIPLE / CONSTRAINED]**

43. A finite pair-rooted Palm-signature audit detects fixed and square-root schedules but not the tested linear schedules. At `N=768`, `w=4`, the pseudo-label guard is `0.592180379231770833`; fixed jitter scores `0.86794175042046441`, square-root jitter `0.623240788777669271`, and the tested linear schedules stay pseudo-label-like (`0.537787967258029514`, `0.532786263359917535`, `0.526714960734049479`). **[STRESS TEST / CONSTRAINED]**

44. The oriented aggregate pair-Palm bracket audit strongly separates all tested linear schedules at `N=768`, `w=4`, but it uses endpoint slots tied to record-index ordering and is therefore not a valid final order-only witness. Against held-out sprinkling max `5.7431020875069451`, the oriented mean/heldout-max ratios are `613.838130273553319` for `J=N/2`, `658.418454695343511` for `J=N`, and `687.074983915100185` for `J=2N`. **[STRESS TEST / COUNTEREXAMPLE / CONSTRAINED]**

45. The oriented aggregate pair-Palm source audit shows that the oriented finite signal is not merely the `O(N)` true hidden sibling pairs. Removing hidden sibling pairs leaves the non-hidden pair ratios essentially unchanged in the tested linear schedules: `377.698699835`, `420.282543971`, and `401.411172279`. Because the parent statistic is endpoint-oriented, this is evidence about a broad oriented permutation residue, not a final order-law separation. **[STRESS TEST / CONSTRAINED]**

46. The endpoint-invariant aggregate pair-Palm repair is relabeling-invariant but does not recover the tested schedules. Against held-out sprinkling max `15.9700423385746535`, the mean/heldout-max ratios are `0.653578215850687798` for fixed `J=4`, `0.371092485078042005` for square-root `J`, `0.327165058671083777` for `J=N/2`, `0.283186239331670603` for `J=N`, and `0.278006016292733501` for `J=2N`; random relabeling spot checks give zero vector difference. **[STRESS TEST / CONSTRAINED]**

47. The endpoint-symmetric rooted pair-flag likelihood ladder tests the smallest honest repair of the oriented aggregate bracket. A first four-record flag design weakly sees `J=N` with ratio `1.05933847191521943`, but an independent four-record design puts all tested linear schedules inside the held-out null (`0.736390675100958657`, `0.756292365995827559`, `0.933815256506892182`), and the five-record flag design also keeps them inside (`0.855769295550185496`, `0.904432975336874781`, `0.859936761859127622`). Endpoint swap, outsider permutation, and relabel-mapped invariance checks all pass. **[STRESS TEST / CONSTRAINED]**

48. The six-record mesoscopic rooted flag field is endpoint/relabel invariant but sample-design unstable. One design keeps all tested linear schedules inside the held-out null (`0.631540619472017349`, `0.589731664576670041`, `0.564897201115129273`), while an independent design sees all three (`1.0783769512257903`, `1.17557144226012443`, `1.11752493599292647`). This is finite calibration instability, not a promoted law. **[STRESS TEST / CONSTRAINED]**

49. The exact `N=6` unlabeled likelihood proxy computes the sprinkling law over `315` unlabeled codes exactly and calibrates empirical chi-square, TV, and KL. Width-2 clustered schedules, including fixed, square-root, and all tested linear schedules, remain inside the calibrated sprinkling null; the linear chi-square/null-max ratios are `0.832709660973744583`, `0.845518735661483559`, and `0.775057354065765995`. **[STRESS TEST / CONSTRAINED]**

50. The unlabeled cross-second-moment ladder computes exact `P_N` for `N=6,8` and uses independent empirical replicas `sum_o q_1(o)q_2(o)/p(o)`. At `N=6`, all tested linear schedules remain inside the exact-`P_6` calibrated null. At `N=8`, a raw `linear_two` opening appears only because the first null cross-excess maximum is negative, which triggers the stability repair. **[STRESS TEST / CONSTRAINED]**

51. The repaired `N=8` stability audit uses a centered null guard `g_8=0.0778970352900532616` and demotes the raw `linear_two` opening. The linear guard ratios are `-0.0506146097591725592`, `-0.115293084296926355`, and `-0.0287643528159100025`; all tested linear schedules remain inside the repaired exact-`P_8` cross-second-moment calibration. **[STRESS TEST / CONSTRAINED]**

52. An exact-`P_8` rare-class stability audit tests individual unlabeled codes, coarse structural groups, and interval-profile groups. No tested linear schedule produces a stable rare-order excess above the centered null guard; the largest positive linear ratios are `0.0707009539238394562` for the coarse group projection and `0.191668864723535681` for the interval-profile projection. **[STRESS TEST / CONSTRAINED]**

53. A two-replica hidden-partition calculation proves the correct overlap scale for bounded hidden width. For two independent uniform width-`w` partitions, the number of record pairs co-blocked in both partitions converges to `Poisson((w-1)^2/2)`, so any second-moment divergence must come from an unbounded local overlap likelihood factor or from a stable rare-order class not found by the exact-`P_8` audit. **[PRINCIPLE / CONSTRAINED]**

54. A mixture second-moment reduction lemma proves that, if the conditional cross-likelihood factor satisfies `E_P[L_H L_H' | H,H'] <= C a^{O_N(H,H')}`, then the unlabeled second moment is bounded by the finite Poisson-overlap moment-generating function. The remaining mathematical obstruction is exactly that local factor inequality. **[PRINCIPLE / CONSTRAINED]**

55. An exact small-size labeled conditional audit tests the local factor itself for `N=4,6`, width `2`, and all hidden matchings. Every tested `H,H'` pair is absorbed by finite fitted constants `C_N,a_N`; the zero-overlap factors stay near `1`, and no single rare zero-overlap labeled order class dominates. **[STRESS TEST / CONSTRAINED]**

56. The hidden-overlap graph has a logarithmic cycle tax. For width-2 matchings, common hidden pairs have mean tending to `1/2`, but the expected number of nonshared alternating components grows as `(1/2) log(N/2)+O(1)`. Thus common-pair overlap alone is not a complete theorem target unless nonshared alternating cycles are proved neutral. **[PRINCIPLE / CONSTRAINED]**

57. An exact-`P_8` overlap-signature audit gives finite evidence for nonshared-cycle neutrality. Zero-common signatures `(4,)` and `(2,2)` have means within `0.01` of `1`, and the ratio `mean(2,2)/mean(4)` is `1.00083763309849502`, `0.998486913810994867`, and `1.00110338460721425` across the three linear schedules. **[STRESS TEST / CONSTRAINED]**

58. The overlap-graph component count has exact mgf `E z^{K_m}=prod_{j=0}^{m-1}(z+2j)/(1+2j)`. A fixed nonshared-component factor `b>1` gives polynomial growth `m^{(b-1)/2}`, while `b_N=1+O(1/log N)` has bounded cycle mgf and `b_N=1+o(1/log N)` is strictly neutral. **[PRINCIPLE / CONSTRAINED]**

59. In a pair-factor likelihood model, the nonshared-cycle tax is governed by a centered transfer operator. A `2k`-record alternating component contributes `1+tr(A^{2k})`, and the total asymptotic tax is `det(I-A^2)^(-1/2)` when the centered spectrum stays below one. **[PRINCIPLE / CONSTRAINED]**

60. Exact-`P_8` hostile review rejects naive multiplicative component factorization of the actual unlabeled conditional likelihood. Edge-calibrated component weights overpredict `(1,1,2)` by factors `3.92777946120964581`, `3.92262579439914904`, and `3.95321414487719158`, while all non-identical signatures have mean below `1.007`. **[STRESS TEST / CONSTRAINED]**

61. Hidden-identity diagonal rarity gives only a conditional sufficient route. If a genuine non-empirical hidden-identity diagonal existed, then sub-`m log m` diagonal growth would be killed by `(2m-1)!! ~ sqrt(2)(2m/e)^m`; however the split-sample audit below demotes the observed exact-`P_8` diagonal spike to an estimator artifact. **[PRINCIPLE / CONSTRAINED]**

62. A split-sample exact-`P_8` hostile audit shows that the large same-`H` spike in the component-factorization receipt is a same-histogram plug-in artifact. Same-histogram reuse gives means near `15.4`, while independent split same-`H` estimates are `0.990392485119047619`, `0.997680082775297619`, and `1.00916021437872024`, matching split different-`H` estimates. The exact zero-jitter clustered law still has direct second moment `1362.66666666666667`, so the audit is not blind to real clustering. **[STRESS TEST / CONSTRAINED]**

63. The current best click-law target is an order-visible rooted/Palm Mecke compensator, mesoscopic/full-law invariant, observable-label information dichotomy, asymptotic law-distance theorem, square-root collision Palm field, endpoint-symmetric relabeling-invariant all-pair Palm-bracket U-statistic, stabilized mesoscopic rooted pair-flag field, direct split/unbiased unlabeled likelihood second-moment theorem `S_N=sum_o q_N(o)^2/P_N(o)`, or process-level joint martingale bracket field for the remaining critical window for `Q_N(w_N,J_N)` versus `P_N`, not any finite scalar, finite mean profile, local interval bracket, finite joint projection, finite interval-pair covariance score, unrooted global empirical law, finite rooted score, finite deletion-increment score, fixed unrooted finite-pattern law, finite interval-size moment law, finite load/bracket score, pairwise or triple label classifier, degree-covariance classifier, finite order-visible bracket vector, reconstructed-coordinate pair classifier, sampled `o(sqrt(N))` induced-suborder test, simple pair top-tail partition ranking, finite pair-rooted Palm-signature classifier, oriented aggregate pair-Palm bracket, six-bin endpoint-invariant aggregate bracket, small rooted pair-flag likelihood ladder, unstable six-record rooted flag field, tiny `N=6` likelihood proxy, finite `N=6,8` cross-second-moment proxy, small-N jitter audit, exact-`P_8` rare-class audit, partition-overlap tax, conditional reduction lemma, exact small-size local-factor audit, overlap-graph cycle audit, exact-`P_8` signature audit, component-mgf bound, transfer-operator toy theorem, component-factorization audit, diagonal-rarity bound, split-sample diagonal-artifact audit, or the partial easy-regime theorem alone. **[PRINCIPLE / OPEN]**

64. The direct exact-denominator split `S_8` ladder detects sharp clustering (`S_8=1362.66666666666667`) and a low-mixing `linear_quarter` residue (`S_8-1=0.0629201730092366536`) but places `linear_5_16`, `linear_3_8`, `linear_7_16`, `linear_half`, `linear_one`, and `linear_two` inside the hostile split-null guard. The finite opening is therefore below half scale at `N=8`, not a stable residue above half scale. **[STRESS TEST / CONSTRAINED]**

65. A selected-class denominator formula reduces exact `P_N(C)` for a chosen unlabeled two-dimensional order class to `r(C)/(|Aut(C)|N!)`, where `r(C)` counts first linear orders whose forced mate is linear. The receipt verifies the formula for all exact classes through `N=6` and for `32` selected exact `N=8` classes. **[PRINCIPLE / CONSTRAINED]**

66. The first selected rare-class campaign at `N=10` finds no large exact selected contribution among resolved half/one candidates. The largest half/one selected contribution is `0.0540733337402`. The `N=12` leg exposes exact unlabeled canonicalization as the next computational wall and does not substitute a sparse empirical denominator. **[STRESS TEST / CONSTRAINED]**

67. A cheap `N=12` invariant-screen audit samples `4096` orders per split side for `linear_quarter`, `linear_5_16`, `linear_half`, and `linear_one`; every sample has a unique degree-block invariant across the split, so no repeated invariant key appears. This is not a proof of washout, but it is evidence against an easy repeated rare-class survivor at that sample scale. **[STRESS TEST / CONSTRAINED]**

**Non-claims.**

1. No manifoldlikeness theorem is proved.

2. No unique click law is derived.

3. No final action over finite orders is proposed.

4. The receipt thresholds are not universal constants.

5. The staged, fiber, mixed-fiber, decorated-fiber, rich-motif, coordinate-jitter, and distributed adversaries are finite constructions, not an asymptotic classification.

6. The no-hidden-staging statistic is not a martingale bracket.

7. Long-range entanglement is not excluded; the condition is on causal intervals and their record support.

8. No claim is made that "any" order passing these finite diagnostics must be manifoldlike.

9. Exact external-twin detection is not a final law; the receipt explicitly constructs a twin-free fiber that closes the exact alarm.

10. The soft near-twin tail thresholds are finite diagnostics, not proposed universal constants.

11. The coordinate-jitter branch does not prove that clustered point processes are forbidden; it only shows that this becomes a separate density/regularity question.

12. The sampled size-4 and size-5 induced-pattern probes are finite, sampled projections, not proof of equality or inequality of full finite-dimensional laws.

13. The regularity-aware clustered candidate is not claimed to be an acceptable physical click law; it is an adversary showing which small diagnostics are insufficient.

14. The projective, interval-bracket, and joint-bracket scores are finite receipt constructions, not universal actions.

15. The 47-dimensional joint vector is not claimed to be complete; it deliberately leaves tuned clustered coordinate processes inside the held-out null.

16. Held-out rank inside the finite null is not evidence that an adversary is physical. It only means this finite projection does not reject it.

17. The multiscale interval-pair covariance receipt is not claimed to define a stable null law; the `N=384` fixed sprinkling lies above the small held-out maximum.

18. The compact stability audit is not a stable law; it explicitly records fresh-sprinkling leakage.

19. No rooted/Palm click law is derived. The paper only identifies why such a component appears necessary.

20. Hidden construction labels are not assumed to be physical observables. If jitter makes them invisible to the order, the remaining adversary is a clustered order process, not a label-detection problem.

21. No Mecke/Palm theorem is proved. The deletion-increment receipt is a finite projection, not a characterization of Poisson sprinkling.

22. No asymptotic phase boundary is proved. The jittered-cluster scaling receipt tests three finite sizes and one width-4 jitter schedule.

23. The phase-diagram receipt is finite and width-specific. It does not classify all jitter schedules `j_N`, all hidden widths `w`, or growing-width clustered processes.

24. The exponent audit is still finite. It tests three widths, three sizes, and six schedules; it does not classify arbitrary `w_N`, arbitrary `j_N`, growing hidden width, curved backgrounds, or higher-dimensional sprinklings.

25. The washout receipts do not prove convergence to sprinkling. They show finite-law camouflage for some linear/superlinear schedules and visibility for others.

26. The two-sample law distance is still a projection of the full record law. It uses exact three-record densities, rooted features, and global interval-profile features, not the full finite-dimensional distribution over orders.

27. The washout/residue theorem is not a full classification. It proves the low-jitter rooted/Palm residue regime and a strong high-jitter full-record washout regime, but leaves the linear and near-linear critical window open.

28. The full-record washout condition `J_N\gg N^2/w_N` is sufficient, not claimed sharp.

29. The linear critical-kernel theorem does not prove full-record washout in the linear window. It only proves fixed unrooted finite-pattern washout and failure of microscopic near-twin detection.

30. The interval-size and load/bracket audits do not prove an asymptotic critical-window residue. The `N=768` load/bracket residue is marginal and finite; it is useful as a pointer, not as a theorem.

31. A clustered construction that converges to the same observable record-order process as sprinkling should be counted as washout at the record level, not as a physically meaningful hidden-fiber counterexample.

32. The observable-label audit is only a pair-feature projection. Pseudo-label-like behavior in that receipt does not prove full record-law convergence; it only shows that the tested hidden labels are not recoverable by those order-visible pair features.

33. The higher-order label audit is only a finite same-label triple-feature projection. It does not prove that all higher-order, rooted, interval, or bracket residues vanish in the linear window.

34. The observable-law metric and degree-covariance receipts do not prove contiguity or full convergence of `Q_N` to sprinkling. They show that a broad finite projection failed to extract a linear-window residue after several obvious openings were followed.

35. The marked-coordinate bracket identity is not yet an order-only record-law separation. It shows that a coordinate-marked clustered process has a fluctuation residue at finite `c`; it does not prove that the causal order alone retains that residue.

36. The finite order-visible bracket-variance audit is not a theorem of order-only contiguity. It only says the tested bracket vector did not recover the marked residue.

37. The reconstructed-coordinate Palm audit is not a coordinate-recovery theorem. It uses degree-based proxies in finite `1+1` samples and tests a pair classifier; it does not rule out a global reconstruction, a nonlinear statistic, or a limiting Palm/Mecke identity.

38. The growing-window washout theorem is not full order-only contiguity in the linear window. It proves washout for uniformly sampled `o(sqrt(N))` induced suborders; square-root-scale, mesoscopic, and full-configuration statistics remain open.

39. The square-root collision Poisson law is still a marked law. It identifies the first scale at which hidden sibling collisions accumulate; it does not prove that those collisions are measurable from the transitive order after hidden labels are forgotten.

40. The hidden-partition likelihood/top-tail audit is not a full likelihood-ratio theorem. It tests direct pair ranking by several order-only scores and does not rule out nonlinear, collective, spectral, or exact maximum-likelihood witnesses.

41. The local Palm-kernel receipt is a finite Monte Carlo projection, not an exact integral theorem. Its `c=0.5` signal should be promoted to exact integration before being used as a claimed asymptotic bracket.

42. The exact local Palm integral is not a full order-law separation theorem. It proves a nonzero conditioned sibling-plus-outsider kernel; it does not by itself prove that unlabeled finite orders are distinguishable in total variation or likelihood ratio.

43. The pair-rooted Palm-signature audit is a finite pair-identification projection. Its failure on tested linear schedules does not rule out aggregate sparse-pair likelihoods, square-root-scale U-statistics, or full contiguity failure.

44. The oriented aggregate pair-Palm bracket audit is not an order-only statistic. It uses endpoint slots chosen by implementation record-index order; the receipt is retained as a hostile diagnostic and as evidence for an aggregate direction, not as a valid final witness.

45. The oriented source audit does not prove the exact mechanism of the broad non-hidden-pair residue. It only shows that deleting true hidden sibling pairs does not remove the finite oriented aggregate signal.

46. The endpoint-invariant aggregate repair does not prove order-only contiguity or full washout in the linear window. It only says that this six-category mean/variance/quantile projection does not recover the tested schedules.

47. No endpoint-symmetric all-pair Palm-bracket likelihood-ratio theorem is proved. The open problem is still whether a richer invariant U-statistic has a nonzero limiting bracket/rate, or whether every order-only aggregate projection loses the marked Palm residue.

48. The endpoint-symmetric pair-flag likelihood ladder is sampled and finite. Its failure is not a theorem that all rooted flag fields fail; it only rules out this four/five-record finite likelihood shadow at the tested calibration.

49. The weak first four-record `J=N` signal is not promoted. The independent four-record sample design and the five-record follow-up both fail to reproduce a linear-window separation.

50. The six-record mesoscopic rooted flag field is not a stable law. The two independent sample designs disagree qualitatively on the linear schedules, so the visible second design is treated as finite calibration instability.

51. The exact `N=6` unlabeled likelihood proxy is not evidence of asymptotic contiguity by itself. It is a tiny brute-force check that defines the right object and finds no separation at that scale.

52. No likelihood-ratio second-moment theorem is proved. The paper only identifies it as the next exact object after finite invariant flag fields became unstable or too weak.

53. The `N=6,8` cross-second-moment ladder is not an asymptotic contiguity theorem. It is exact in `P_N` at those sizes but empirical in `Q_N`, and it only tests width `2`.

54. The first raw `N=8` `linear_two` opening is not promoted. It relies on a negative null maximum and disappears under the centered null guard with larger samples.

55. Reporting top positive unlabeled classes is not a structural classification. It only records candidates for future rare-class analysis if a stable second-moment excess reappears.

56. The exact-`P_8` rare-class stability audit is not a theorem that no rare-order class exists. It tests one small size, width `2`, three projections, and empirical clustered replicas.

57. The two-replica hidden-partition overlap tax is not the unlabeled second-moment theorem. It proves the hidden-partition overlap scale, but it does not yet prove the needed local likelihood-factor bound from overlap count to order likelihood ratio.

58. The Poisson overlap law concerns overlap between hidden explanations. It does not by itself show that the unlabeled transitive order has bounded likelihood ratio under `Q_N` versus `P_N`.

59. The reduction lemma is conditional. It proves that the local cross-likelihood factor inequality would imply boundedness; it does not prove that inequality for the actual jittered clustered order law.

60. The exact small-size local-factor audit is labeled, finite, and empirical in `Q_H`. It does not prove the unlabeled asymptotic second-moment bound.

61. The overlap-graph cycle tax is not a divergence proof. It proves that nonshared alternating components are logarithmically abundant; it does not prove that those components carry a nonneutral likelihood factor.

62. The exact-`P_8` overlap-signature audit is finite and empirical in the conditional clustered laws `Q_H`. It supports cycle neutrality but does not prove the asymptotic nonshared-cycle factor is `1+o(1/log N)`.

63. The component-mgf bound is a theorem about random hidden-overlap graphs. It becomes a second-moment theorem only after the actual likelihood factor is bounded by the common-pair and nonshared-component factors.

64. The transfer-operator cycle theorem is conditional on a pair-factor representation of the conditional likelihood. The actual unlabeled order likelihood may have higher-order factors; proving or refuting that representation is now part of the open theorem.

65. The component-factorization audit is finite, sampled in `Q_H`, and exact only in `P_8`. It rejects one naive multiplicative model; it does not prove all non-identical signatures are asymptotically null.

66. The diagonal-rarity bound does not bound the diagonal self-likelihood. It only proves that sub-`m log m` diagonal growth would be killed by the rarity of identical hidden matchings.

67. The split-sample diagonal-artifact audit is finite and empirical in `Q_H`. It corrects the interpretation of the exact-`P_8` diagonal spike, but it does not prove asymptotic order-only contiguity in the linear window.

68. The direct `S_8` ladder does not prove the asymptotic phase boundary. Its `linear_quarter` visibility and `linear_5_16` invisibility are finite `N=8` grid facts, not constants proposed for the continuum record law.

69. The selected-class denominator formula is not a fast algorithm by itself. It replaces whole-support enumeration with selected realizer/aut counting, but `r(C)` can still be expensive for large or highly symmetric classes.

70. The `N=10/N=12` selected rare-class audit is not a full `S_N` computation. It tests selected repeated candidates; the `N=12` branch is explicitly a canonicalization wall, not a completed rare-class audit.

71. The `N=12` invariant-screen audit is not an exact full-law likelihood audit. It uses a cheap necessary invariant to find repeated candidates; zero repeated invariant keys at the tested sample size does not rule out rarer survivors or survivors invisible to this sampling scale.

---

## 13. Hostile review pass

**Review A: "The new adversaries are too easy."**  
Correct. The antichain and chain fiber blow-ups are not hard imposters because the height diagnostic catches them immediately. The paper now states this as a narrowing result, not a proof. The remaining adversary is a tuned cross-linked fiber or staged-reservoir construction that preserves height, MM dimension, interval abundance, recursive content, and overlap simultaneously.

**Review B: "Distributed staging fails by construction, so it proves little."**  
Correct. Independent reservoirs destroy the global related-pair fraction. The value of the test is negative: lowering exact duplicate count alone is easy, but doing so while restoring the 2D MM scale requires cross-links, and cross-links change the interval histogram and mixed-interior profile. The paper now names cross-linked distributed staging as the next hard target.

**Review C: "The phrase 'the law penalizes' sounds derived."**  
Repaired. The law-first language is now explicitly a candidate formulation. The receipt only supplies finite projections and adversarial constraints; it does not derive an action, transition kernel, or martingale bracket for the full record law.

**Review D: "Do not make a checklist theorem."**  
Repaired. The paper now says the finite diagnostics are shadows of a possible specific recursive record law, not sufficient conditions for manifoldlikeness. The strongest defensible conclusion is that the click law has been narrowed: it must control recursive interval kernels, hidden-staging overlap, hidden-fiber/extensional structure, and density/regularity; the next adversary must be decorated, cross-linked, tuned, or clustered enough to test the density projection.

**Review E: "The tuned mixed fiber is close enough that the old story is incomplete."**  
Accepted. The mixed fiber reaches the global height scale and keeps the old load/overlap measures benign. The paper treats this as the point where hidden-fiber/extensional structure becomes necessary, then follows the decoration branch to the stronger twin-free motif adversary.

**Review F: "Exact external twins are easy to break by decoration."**  
Accepted and followed. Single-tag and double-tag decorations did not close the exact-twin opening, but the twin-free motif did: it reaches zero exact external twins and keeps `P_log2` close. The paper no longer treats exact twins as enough.

**Review G: "If exact twins and scalar interval profile can both be closed, what remains?"**  
Answered by the soft near-twin tail. The twin-free motif has `674` pairs with external-neighborhood difference `<=8`, versus `95` for the fixed sprinkling. This becomes the surviving finite diagnostic and motivates the `T_C(tau)` tail law.

**Review H: "Can richer local motifs reduce the soft tail?"**  
Tested in a bounded search over varied random local motifs of width `6`, `8`, `12`, and `16`. The best broad-band candidate did not improve `diff<=8` over the twin-free motif and paid interval-profile drift. This is not an impossibility proof; it ends the pure local-motif branch tested here.

**Review I: "What if the hidden fiber gets different external neighborhoods by jittering its records?"**  
Accepted and followed. Bounded coordinate jitter is much stronger: it lowers `diff<=8` from `674` to `153` while keeping `P_log2` at `0.98839205290919710349` and `d_MM` near `2`. But it still exceeds the sprinkling soft tail `95`. Over-jitter can match the tail with `93`, but same-hidden-cluster `diff<=8` pairs fall to `19`, so the hidden fiber has effectively washed out into a clustered 1+1 point process. This opens the density/regularity projection.

**Review J: "Endpoint loads, conditional endpoint residuals, or small induced patterns should catch the clustered process."**  
Tested and not cleanly supported. The regularity-aware clustered candidate has `diff<=8=100` against sprinkling `95`, `P_log2` ratio `0.98835534054519469285`, `d_MM=1.9890145938921685549`, and only one exact external-twin pair. Its endpoint-profile log gap is `0.20994800275991994882`. Its conditional endpoint residual gap, `0.36261367215434820561`, is below the independent sprinkling-vs-sprinkling calibration `0.70446455247920145541`. Its sampled size-4/5 induced-pattern gaps are close to the independent sprinkling calibration, and a pattern-aware search keeps the same candidate. The review therefore changes the target: finite density diagnostics are shadows, not the law.

**Review K: "If the full law is the target, how do we find it?"**  
Followed through deletion projectivity, causal interval fixed points, mean interval actions, and crude moment scores. Random deletion is too geometry-blind. Causal intervals are better, but mean interval laws and crude variance scores can be tuned. This moves the target to compensated interval observables and their brackets.

**Review L: "Does a calibrated interval bracket solve the clustered adversary?"**  
Partly. It catches the regularity-aware cluster and the mean-tuned cluster. But a bracket-tuned cluster with `jitter=3/1`, `seed=16003` beats the interval-only bracket score at search resolution. Interval brackets are an advance, not the law.

**Review M: "Then use a joint global-and-interval bracket field."**  
Tested with a 47-dimensional joint vector, 56 train sprinklings, and 16 held-out sprinklings. This rejects density-modulated and staged families strongly and rejects the original regularity-aware cluster beyond the held-out maximum. But tuned jittered clusters remain inside the finite null; the best broadened one has joint score `18.23981593188092237` and held-out rank `0.25`. The finite joint projection is still not the click law.

**Review N: "Are we advancing or just adding features?"**  
Advancing, but not finished. Each pass converts a vague requirement into a sharper object and then finds its finite failure mode. The surviving target is now specific: a process-level joint martingale bracket field, or a compact principle implying it. No such compact principle has been derived here.

**Review O: "Interval-pair covariance should catch the remaining clustered process."**  
Partly, but not decisively. It rejects density-modulated processes and staged sandwiches at both `N=192` and `N=384`, and it rejects one of the previously best tuned clusters at `N=192`. But a tuned jitter cluster remains inside the `N=384` held-out null with score/max ratio `0.54517708242182852`, and the fixed fresh `N=384` sprinkling itself lies above the small held-out maximum. The review therefore forces the next correction: interval-pair covariance is a necessary projection of the law, not the law.

**Review P: "Maybe a better-conditioned finite vector solves the calibration problem."**  
Tested with a compact 32-dimensional interval-pair projection. It improves the behavior but does not finish it: fresh sprinklings still leak above the held-out maximum at both tested scales, and tuned jitter clusters remain inside the held-out support. The more serious obstruction is asymptotic. For fixed hidden width `w`, same-hidden-cluster pairs have unrooted global mass `(w-1)/(N-1)`, which goes to zero, while a typical rooted record still has `w-1` hidden partners. A final law must therefore have a rooted/Palm component, not merely a better finite unrooted vector.

**Review Q: "Then rooted/Palm should detect the hidden width."**  
Tested directly. The first rooted/Palm projection is stable on fresh sprinklings, but it does not reject the jittered width sweep: widths `2`, `4`, `8`, and `16` all score below the held-out maximum. The reason is instructive. Under jitter, same hidden construction labels stop being order-visible near twins. At width `16`, the rooted hidden label multiplicity is `15`, but the same-label fraction with `Delta <= tau` is only `0.000347222222222222222`. The review therefore splits the target: rooted/Palm laws are necessary for order-visible hidden multiplicity, but they should not chase labels that no longer leave a causal signature. Such adversaries must be treated as clustered order processes.

**Review R: "Use the real Poisson clue: Mecke/Slivnyak."**  
Followed as an order-only deletion-increment audit. The finite Mecke/Palm shadow is useful: it rejects the density-modulated/Cox-like process with score/max `5.87295382945095778`. But it does not reject the jittered width sweep; all tested widths remain below the held-out maximum. This is not a failure of the Mecke idea. It is a warning that the finite deletion-increment vector is only a projection. The next target is an asymptotic order-only Mecke/Palm compensator or a process principle that implies one.

**Review S: "Maybe the jittered cluster is just the same order law in disguise."**  
Partly tested by exact triple-pattern scaling. Low jitter is strongly separated at every tested scale. High jitter can pass the finite null at `N=192` and `N=384`, but at `N=768` the same jitter `4` process separates with score/max `17.7158721626271524`; the largest components are rooted softness and exact triple antichain/chain densities. This suggests the jittered adversary may be order-distinct after all, but the receipt is still finite. The later washout receipts sharpen this into a washout/residue classification problem for clustered coordinate processes.

**Review T: "Then draw the phase diagram."**  
Done for fixed width `4` and six jitter scales. The result is not monotone in a naive way, which is useful. Locked and micro-jittered fibers are separated; moderate/high jitter can camouflage at small or intermediate `N`; fixed jitter can reappear as an exact-pattern/rooted defect at larger `N`; and no tested fixed-jitter schedule proves full washout across `N=192,384,768`. The review changes the target from "find a better finite score" to "prove the critical scaling curve for `Q_N(w,j_N)` versus `P_N`."

**Review U: "A phase diagram at one width is not a scaling law."**  
Correct. The exponent audit tests widths `2,4,8` and schedules from fixed jitter through square-root and weakly linear rank-mixing radius. It does not produce a clean universal threshold. At `N=768`, fixed `4` remains visible for all tested widths, but fixed `16`, `sqrt(N)`, `2 sqrt(N)`, and `N/24` can sit inside the finite null depending on width. The review therefore changes the target again: the theorem must classify `Q_N(w_N,j_N)`, not just fixed-width or fixed-jitter families.

**Review V: "Maybe sufficiently large jitter just washes the hidden structure away."**  
Partly yes, and that matters. The linear/superlinear washout audit finds that `N`-scale and `2N`-scale rank mixing can erase same-label near-twin visibility and enter finite camouflage. But the effect is not monotone and not universal: some large-mixing cases remain visible. The click-law target should therefore penalize order-visible residue, not hidden implementation labels that leave no record-law trace.

**Review W: "One washed-out sample is not a law."**  
Correct. The two-sample law-distance audit compares repeated sprinklings against repeated clustered samples. It confirms fixed small jitter is robustly visible, while some large-mixing families are inside the empirical sprinkling null and others are not. At `N=768`, `w=2` with `N` and `2N` mixing is inside the finite null, `w=4` is visible for both, and `w=8` is borderline/split. The review changes the theorem target from "reject clustered coordinate generators" to "prove a washout/residue dichotomy for their induced record laws."

**Review X: "Then prove the dichotomy."**  
Partly proved, and the limitation is now explicit. If `w_NJ_N=o(\sqrt N)`, same-cluster partners are closer than any sprinkling neighbor at a calibrated rooted/Palm microscopic threshold, so a residue persists. If `J_N\gg N^2/w_N`, a product-TV coupling washes the entire finite record order to sprinkling. Fixed-k unrooted laws wash out under the weaker condition `m_N/J_N\to0`. The linear and near-linear window is not solved by this proof; it is exactly the hard regime exposed by the finite receipts.

**Review Y: "Try fixed finite patterns in the linear window."**  
They provably cannot finish the job. For bounded hidden width, a fixed `k`-sample hits the same hidden cluster with probability `O(k^2w/N)`. Conditional on avoiding that collision, the two coordinate rankings converge to independent random permutations, exactly as in `1+1` sprinkling. The linear critical-kernel theorem therefore kills the next tempting but wrong path: another fixed unrooted finite-pattern checklist cannot classify the critical window.

**Review Z: "Try mesoscopic interval moments or finite load brackets."**  
Partly useful, but not decisive. Interval-size moments see one `N=384` family with score/null `1.46499376027173406`, then wash out on every tested `N=768` linear-window family. A 38-dimensional load/bracket projection restores a marginal `N=768` witness for `w=4`, `J_N=2N`, with score/null `1.03424395062355414`, but admits many other linear-window families. This review changes the target from "find a bigger finite feature vector" to "prove or refute equality of the process-level bracket/Palm/Mecke law."

**Review AA: "A hidden variable is already bad."**  
No. A hidden construction label matters only if it leaves record-visible information. The observable-label audit makes this operational: low-jitter labels are recoverable from order-only pair features, while the tested linear schedules fall to pseudo-label separability. This does not prove full washout, but it gives the right principle: penalize observable residue, not unobservable implementation history.

**Review AB: "Pair-invisible labels may still be triple-visible."**  
Tested and not found in the finite triple projection. Same-label triples are strongly visible for locked, fixed-jitter, and square-root schedules, but the tested linear schedules remain inside the pseudo-label guard. This does not close the problem; it moves the next search away from simple label classifiers and toward rooted/Palm, interval, deletion-increment, or process-level bracket witnesses.

**Review AC: "Maybe a combined metric or degree covariance still sees the linear window."**  
Tested in two receipts. A 46-dimensional observable-law projection sees fixed jitter and barely sees square-root jitter, but all tested linear schedules remain inside the calibrated null. Degree covariance catches fixed and square-root jitter through past/future degree structure, but again leaves all linear schedules pseudo-label-like. This does not prove contiguity, but it makes further finite feature-chasing look low yield. The next serious target is an asymptotic law-distance or Palm/Mecke/bracket theorem.

**Review AD: "The asymptotic bracket might separate the laws."**  
Yes in the coordinate-marked shadow. The receipt derives `N Var(N^{-1}\sum R_i) -> 1/12+(w-1)B(c)`, and `B(c)>0` for finite `c`; for `w=4`, `c=2`, the bracket is `0.0967029389880952381` instead of `1/12`. But the finite order-visible bracket-variance receipt does not recover this residue in the tested linear schedules. This is now the central split: marked clustered coordinates are not iid at the bracket level, while the causal order alone may still be contiguous, or may require a subtler Palm/Mecke bracket to reveal the residue.

**Review AE: "Recover the marked residue from the order, or prove washout."**  
Partly done, with a sharper failure boundary. The reconstructed-coordinate Palm audit uses only order-visible past/future degrees to recover approximate `{u,v}` roots, but it still does not recover the marked residue in the tested linear schedules. The growing-window theorem proves a real order-only washout result: for bounded width, every uniformly sampled `k_N=o(sqrt(N))` induced-suborder test is asymptotically blind, because sibling collisions vanish and the no-collision rank kernel converges to the sprinkling kernel. This is not full contiguity. It says any surviving order-only witness must use square-root-scale or larger information, or a global Palm/Mecke/bracket identity not reducible to small induced suborders.

**Review AF: "Think like Maxwell, Euler, Kolmogorov, Tao: find the real object."**  
Followed in three directions. The square-root collision receipt gives the exact critical object: at `k=a sqrt(N)`, hidden sibling collisions have Poisson intensity `a^2(w-1)/2`. The direct hidden-partition likelihood audit then asks whether the full order can recover those siblings by simple pair top-tail scoring; it succeeds for fixed and square-root schedules but fails for the tested linear schedules. Finally, the local Palm-kernel audit shows that pair comparability is exactly null, while the sibling-plus-outsider triple kernel is visible at `c=0.5` but not at `c=1,2,4` above Monte Carlo control. This is progress, not closure. The next honest object is the conditional projection `E[M_N | O_N]`: either the marked collision/bracket field has a nonzero order-only square-root/Palm projection, or the marked residue is lost when records forget coordinates and hidden labels.

**Review AG: "The local Palm kernel should be exact, not Monte Carlo."**  
Repaired and followed. The exact integral reduces the one-coordinate sibling-plus-outsider law to `q(c)=E|F_c(X_1)-F_c(X_2)|`, then enumerates the two independent lightcone-coordinate permutations. This proves a nonzero local order-only Palm residue for finite `c`; at `c=1` the exact triple L1 gap is `1/300`. But the follow-up pair-rooted Palm-signature audit still fails to recover the tested linear schedules. The residue is real but too diluted for pair identification at this finite scale. The remaining problem is now sparse aggregate detection: sum many tiny pair-Palm biases, or prove that their order-only conditional projection has vanishing likelihood ratio.

**Review AH: "Actually sum the tiny Palm biases."**  
Followed, and the first result looked like the strongest finite separation in the linear-window branch. The aggregate pair-Palm bracket sums third-record status information around all pairs and separates all tested linear schedules by hundreds of held-out null units. The source audit prevents one wrong interpretation: deleting true hidden sibling pairs leaves the oriented signal essentially unchanged, so the effect is not merely sparse hidden-pair accumulation. But this review opens the next, more serious objection: the score uses endpoint slots `(x,y)`.

**Review AI: "Endpoint ordering is a hidden coordinate leak."**  
Accepted. For an unordered pair `{x,y}`, the statistic must be invariant under swapping endpoints and under arbitrary record relabeling. The repaired receipt merges endpoint-swapped status classes into six unordered categories and verifies zero vector change under random relabeling. That repair does **not** recover the tested linear schedules: at `N=768`, `w=4`, the ratios to held-out sprinkling max are `0.327165058671083777`, `0.283186239331670603`, and `0.278006016292733501` for `J=N/2`, `J=N`, and `J=2N`. The previous aggregate separation is therefore demoted to an instructive false breakthrough. The next theorem cannot promote the oriented score; it must either find a genuinely endpoint-symmetric relabeling-invariant all-pair U-statistic, or prove that the marked Palm residue is lost when only the unlabeled transitive order is observed.

**Review AJ: "Then use the smallest invariant likelihood, not six bins."**  
Followed. The endpoint-symmetric rooted pair-flag receipt canonicalizes the full induced order around `{x,y}` plus two or three outsiders, under endpoint swap, outsider permutation, and relabel-mapped samples. The first four-record flag design weakly sees `J=N`, but the independent four-record design removes that signal, and the five-record design keeps all tested linear schedules inside the held-out null. This is not proof of contiguity. It is a useful failed rung: local rooted flag likelihoods are now too small to carry the remaining marked Palm residue robustly. The next honest fork is a mesoscopic rooted flag field or an exact second-moment/contiguity calculation for the unlabeled order likelihood ratio.

**Review AK: "Make the rooted flags mesoscopic."**  
Followed with six-record rooted flags and hashed calibrated code fields. The result is not promotable. The primary sample design keeps every tested linear schedule inside the held-out null; the independent sample design sees every tested linear schedule. Since both designs pass endpoint and relabel invariance, the disagreement is not a hidden-coordinate leak. It is finite calibration instability in a sparse mesoscopic flag field. The path is not dead, but the next version needs either stable asymptotic calibration or a theorem; otherwise the flag field is just a sample-design dial.

**Review AL: "Then compute the likelihood object directly, even if tiny."**  
Followed at `N=6`, where the unlabeled `1+1` sprinkling law can be computed exactly by enumerating all `6!` coordinate permutations and all `6!` relabelings. The exact support has `315` unlabeled codes. Against empirical sprinkling calibration, all tested width-2 clustered schedules stay inside null for chi-square, TV, and KL. This does not prove contiguity in the critical window, but it is the cleanest object so far. The next theorem should be a true second-moment calculation for `dQ_N/dP_N` on the unlabeled order sigma-field, or a proof that this second moment diverges through a specific invariant statistic.

**Review AM: "Use the two-replica second moment, not a one-sample square."**  
Followed. The cross ladder computes exact `P_N` at `N=6,8` and estimates `sum q_1q_2/p` from independent clustered replicas. At `N=6`, all linear schedules remain inside. At `N=8`, `linear_two` appears raw-visible, but only because the null cross-excess maximum is negative. That is not a valid promotion; it opens a calibration repair.

**Review AN: "Repair the N=8 null before believing linear_two."**  
Followed with larger samples and a centered null guard. The repaired `N=8` guard is `0.0778970352900532616`, and all tested linear schedules stay inside. The top positive unlabeled classes are recorded, but their rare probabilities and failure to produce stable excess demote the first ladder's `linear_two` signal to finite calibration noise. The second-moment path now points toward a theorem: bounded unlabeled second moment in the bounded-width linear window, or a stable rare-class mechanism that survives this guard.

**Review AO: "Find the stable rare class if the second moment diverges."**  
Followed at exact `P_8`. The audit checks individual unlabeled codes, coarse structural groups, and interval-profile groups. No tested linear schedule beats the centered null guard in any projection. The rare-class route is not disproved, but its first exact small-`N` shadow fails. If divergence exists, it is not showing up as a stable `P_8` code/group excess in these projections.

**Review AP: "Then prove boundedness from the hidden-partition overlap."**  
Partly followed. For two independent width-`w` hidden partitions, the number of pairs co-blocked in both hidden explanations has Poisson limit with intensity `(w-1)^2/2`. Thus bounded-width hidden clusters do not create extensive two-replica overlap. The remaining proof gap is now very specific: bound the unlabeled likelihood factor by a fixed local weight per two-replica hidden-pair overlap. If that factorization is proved, the second moment is bounded by a finite Poisson-overlap moment-generating function.

**Review AQ: "Test the local factor itself before calling it plausible."**  
Followed in the first exact labeled sizes. For `N=4,6`, exact labeled `P_N` is computed by enumerating all coordinate-permutation pairs, and every width-2 hidden matching `H` is tested against every `H'`. The zero-overlap factors stay close to `1`; no zero-overlap rare labeled order dominates; same-hidden-explanation factors at `N=6` are large but absorbed by a finite per-overlap factor. This is support for the local factor inequality, not the proof.

**Review AR: "Common-pair overlap is not the whole overlap graph."**  
Accepted and followed. For width `2`, the union of two hidden matchings contains nonshared alternating cycles. Exact counting gives `E C_k -> 1/(2k)` for fixed component size `k`, so the total number of alternating components has mean `(1/2) log(N/2)+O(1)`, while common hidden-pair overlap stays `O(1)`. This is a real correction: the boundedness theorem must prove that nonshared alternating cycles are asymptotically neutral, or carry a full overlap-graph cycle tax. The shared-pair Poisson bound alone is not enough.

**Review AS: "Do nonshared cycles actually carry a factor?"**  
Tested at exact unlabeled `P_8` by conditioning on every width-2 hidden matching and grouping all `H,H'` pairs by overlap-graph signature. The zero-common signatures `(4,)` and `(2,2)` stay at mean `1` across the linear schedules, and two nonshared cycles are not worse than one. This is finite evidence for cycle neutrality, not a proof.

**Review AT: "How neutral is neutral enough?"**  
Answered by the exact component-count mgf. If `K_m` is the number of alternating components in the union of two matchings on `2m` records, then `E z^{K_m}=prod_{j=0}^{m-1}(z+2j)/(1+2j)`. A fixed factor per nonshared component grows like `m^{(b-1)/2}`. A factor `1+O(1/log N)` has bounded mgf, and `1+o(1/log N)` is strictly neutral. The theorem target is now numerically and asymptotically precise.

**Review AU: "Per-cycle neutrality is too strong; use a transfer operator."**  
Accepted and followed. In a pair-factor likelihood model, a nonshared alternating component with `k` hidden edges contributes `1+tr(A^{2k})`, where `A` is the centered pair operator. The full nonshared-cycle tax is then `det(I-A^2)^(-1/2)` if the centered spectrum stays below one. This is stronger and cleaner than demanding each cycle carry factor `1+O(1/log N)`. It also exposes the true divergence mechanism: a centered eigenvalue approaching one, or failure of pair-factorization.

**Review AV: "Does the actual unlabeled likelihood factor over components?"**  
Hostile-tested at exact `P_8`, and the naive answer is no. Component weights calibrated from `(1,1,1,1)` and `(2,2)` overpredict `(1,1,2)` by about a factor of `4`. This demotes the transfer-operator theorem to a toy theorem until a real pair-factor representation is proved. But it also reveals a stronger finite pattern: every non-identical signature is near null, and the spike is concentrated on full hidden-matching identity.

**Review AW: "If only full identity spikes, is that dangerous?"**  
Only if the diagonal self-likelihood is enormous. The identical-hidden-matching event has probability `1/(2m-1)!!`, and `(2m-1)!! ~ sqrt(2)(2m/e)^m`. Polynomial, fixed-exponential, and `exp(o(m log m))` diagonal spikes are killed. A diagonal divergence would require self-likelihood on the scale of the number of hidden matchings. The best theorem target is now: prove all non-identical cross factors are `1+o(1)`, and prove diagonal self-likelihood is `exp(o(m log m))`.

**Review AX: "Was the hidden diagonal just same-sample histogram bias?"**  
Yes, at exact `P_8` under the tested estimator. Reusing the same empirical histogram gives same-`H` means near `15.4`, but independent split same-`H` estimates fall to `0.990392485119047619`, `0.997680082775297619`, and `1.00916021437872024`, matching split different-`H`. The receipt also computes an exact zero-jitter clustered baseline with second moment `1362.66666666666667`, so this is not a powerless test. This demotes the hidden-diagonal rarity path: the live theorem is now the direct split/unbiased unlabeled likelihood second moment `S_N=sum_o q_N(o)^2/P_N(o)`.

**Review AY: "What does the direct `S_N` test say once the denominator is exact?"**  
At `N=8`, it says the half-scale and larger linear schedules are not separating under the hostile split guard. Sharp zero-jitter clustering gives `S_8=1362.66666666666667`, so the test is sensitive. `linear_quarter` remains visible with excess `0.0629201730092366536`, but `linear_5_16`, `linear_3_8`, `linear_7_16`, `linear_half`, `linear_one`, and `linear_two` are inside the guard. The opening is therefore below half scale in this finite ladder. The next wall is exact `P_N` beyond `N=8`: do not replace it with a sparse empirical denominator unless the estimator itself is the object under study.

**Review AZ: "Can exact denominators beyond `N=8` be selected rather than global?"**  
Partly yes. For a selected unlabeled two-dimensional class `C`, `P_N(C)=r(C)/(|Aut(C)|N!)`, where `r(C)` counts first linear orders whose forced mate is linear. This is verified for every exact class through `N=6` and for `32` selected exact `N=8` classes. It does not make `N=12` automatic, but it changes the next task: sample candidate rare classes at `N=10,12`, then compute selected denominators by realizer/aut counting.

**Review BA: "Do selected rare classes survive at `N=10`?"**  
Not in the first exact selected-denominator audit. The merged split supports are almost disjoint, and the repeated candidates have tiny counts. Exact `r(C)/(|Aut(C)|N!)` denominators are tractable for the tested `N=10` candidates; the largest resolved half/one selected contribution is only `0.0540733337402`. This is not a divergence signal. The `N=12` branch exposes a different wall: exact unlabeled canonicalization and selected counting must be made faster before the same audit can be trusted there. Sparse empirical denominators remain rejected.

**Review BB: "Can the `N=12` wall be softened without sparse `P_N`?"**  
Yes, partially. A cheap degree-block invariant screen runs quickly at `N=12` and avoids full canonicalization of every sample. In `4096` samples per side for `linear_quarter`, `linear_5_16`, `linear_half`, and `linear_one`, every split side has `4096` invariant keys and there are zero overlap keys. Thus no exact class is promoted and no denominator is computed. This is not a theorem, but it says an easy repeated rare-class survivor is not appearing at this scale. The next step is larger invariant-screen sampling plus exact isomorphism/selected denominators only when repeated keys appear.

Status after this pass: **accepted as a stress-test, partial theorem, and narrowing paper, rejected as a manifoldlikeness theorem. The target has moved from finite interval diagnostics to an endpoint-symmetric relabeling-invariant all-pair Palm-bracket U-statistic, a stabilized mesoscopic rooted pair-flag field, a direct split/unbiased exact-denominator unlabeled likelihood second-moment theorem, selected-class `P_N` probability formulas beyond `N=8`, fast invariant screening plus canonicalization and realizer/aut counting for rare classes, an asymptotic order-only bracket law, or a process-level joint global-and-interval bracket law for the critical clustered-coordinate window left between proved residue and proved washout. The oriented aggregate score, small rooted flag ladder, unstable six-record rooted flag field, tiny likelihood proxy, finite `N=6,8` cross-second-moment proxies, exact-`P_8` rare-class search, partition-overlap tax, exact small-size local-factor audit, exact-`P_8` cycle-signature audit, transfer-operator toy theorem, component-factorization audit, hidden-diagonal rarity route, direct `S_8` ladder, selected-class formula alone, first `N=10` selected rare-class audit, and first `N=12` invariant-screen audit are rejected as final record-law witnesses.**

---

## References

**Companion program.**

- *The record click-law, XI* (v7) -- order plus number, `l_step`, and manifoldlikeness as the field-shared gate.
- *The record click-law, XX* (v7) -- deterministic hidden machines can realize the scalar record-facing click law.
- *The record click-law, XXI* (v7) -- scalar record martingale principle.
- *The record click-law, XXII* (v7) -- marked compensators, interval-profile calibration, moment underdetermination, and transitivity tax.
- `note-C2-covariance-premise-deferral.md` -- BHS no-finite-valency obstruction and covariance deferral.
- `v7/code/p23_recursive_interval_law.py` -- high-precision recursive interval/no-hidden-staging receipt.
- `v7/code/p24_projective_fixed_point_law.py` -- collapsed projective fixed-point and bracket-wall receipt.
- `v7/code/p25_interval_bracket_action.py` -- collapsed calibrated interval-bracket receipt.
- `v7/code/p23_joint_global_interval_bracket.py` -- collapsed joint global-and-interval held-out bracket receipt.
- `v7/code/p23_multiscale_interval_pair_covariance.py` -- collapsed multiscale interval-pair covariance receipt.
- `v7/code/p23_stability_adversarial_limit_audit.py` -- collapsed stability and adversarial-limit receipt.
- `v7/code/p23_rooted_palm_bracket_audit.py` -- collapsed rooted/Palm bracket receipt.
- `v7/code/p23_mecke_palm_poisson_audit.py` -- collapsed order-only Mecke/Palm compensator receipt.
- `v7/code/p23_asymptotic_jittered_cluster_limit_audit.py` -- collapsed asymptotic jittered-cluster limit receipt.
- `v7/code/p23_jitter_scaling_phase_diagram.py` -- collapsed jitter scaling phase-diagram receipt.
- `v7/code/p23_jitter_scaling_exponent_audit.py` -- collapsed jitter scaling exponent receipt.
- `v7/code/p23_jitter_linear_washout_audit.py` -- collapsed linear/superlinear jitter washout receipt.
- `v7/code/p23_washout_two_sample_distance_audit.py` -- collapsed two-sample washout law-distance receipt.
- `v7/code/p23_washout_residue_dichotomy_bounds.py` -- collapsed proof-bound receipt for the washout/residue theorem.
- `v7/code/p23_linear_critical_kernel_audit.py` -- collapsed linear critical-window kernel receipt.
- `v7/code/p23_linear_window_interval_variance_audit.py` -- collapsed linear-window interval-size moment receipt.
- `v7/code/p23_linear_window_load_bracket_audit.py` -- collapsed linear-window order-visible load/bracket receipt.
- `v7/code/p23_observable_label_information_audit.py` -- collapsed observable hidden-label information receipt.
- `v7/code/p23_higher_order_label_residue_audit.py` -- collapsed higher-order hidden-label residue receipt.
- `v7/code/p23_observable_law_metric_campaign.py` -- collapsed observable-law metric campaign receipt.
- `v7/code/p23_degree_covariance_label_residue_audit.py` -- collapsed degree-covariance hidden-label residue receipt.
- `v7/code/p23_asymptotic_bracket_identity.py` -- collapsed asymptotic marked bracket identity receipt.
- `v7/code/p23_order_visible_bracket_variance_audit.py` -- collapsed order-visible bracket variance receipt.
- `v7/code/p23_reconstructed_coordinate_palm_audit.py` -- collapsed reconstructed-coordinate Palm receipt.
- `v7/code/p23_growing_window_washout_bounds.py` -- collapsed growing-window washout bound receipt.
- `v7/code/p23_sqrt_collision_poisson_law.py` -- collapsed square-root collision Poisson-law receipt.
- `v7/code/p23_hidden_partition_likelihood_audit.py` -- collapsed hidden-partition likelihood/top-tail receipt.
- `v7/code/p23_palm_kernel_projection_audit.py` -- collapsed local Palm-kernel projection receipt.
- `v7/code/p23_exact_palm_kernel_integral.py` -- collapsed exact local Palm-kernel integral receipt.
- `v7/code/p23_pair_palm_signature_audit.py` -- collapsed pair-rooted Palm-signature receipt.
- `v7/code/p23_aggregate_pair_palm_bracket_audit.py` -- collapsed oriented aggregate pair-Palm bracket receipt.
- `v7/code/p23_aggregate_pair_palm_source_audit.py` -- collapsed oriented aggregate pair-Palm source audit.
- `v7/code/p23_invariant_aggregate_pair_palm_bracket_audit.py` -- collapsed endpoint-invariant aggregate pair-Palm repair receipt.
- `v7/code/p23_endpoint_symmetric_pair_flag_likelihood_audit.py` -- collapsed endpoint-symmetric rooted pair-flag likelihood receipt.
- `v7/code/p23_mesoscopic_rooted_flag_field_audit.py` -- collapsed mesoscopic rooted pair-flag field receipt.
- `v7/code/p23_small_unlabeled_likelihood_second_moment.py` -- collapsed small-N exact unlabeled likelihood second-moment proxy.
- `v7/code/p23_unlabeled_second_moment_ladder.py` -- collapsed exact-P unlabeled cross-second-moment ladder.
- `v7/code/p23_unlabeled_second_moment_n8_stability.py` -- collapsed N=8 centered-guard second-moment stability audit.
- `v7/code/p23_unlabeled_rare_class_stability_audit.py` -- collapsed exact-P8 rare-class stability audit.
- `v7/code/p23_partition_overlap_poisson_bound.py` -- collapsed two-replica hidden-partition overlap-tax receipt.
- `v7/code/p23_local_factor_inequality_audit.py` -- collapsed exact small-size local cross-likelihood factor audit.
- `v7/code/p23_overlap_graph_cycle_tax.py` -- collapsed hidden-overlap graph cycle-tax receipt.
- `v7/code/p23_cycle_neutrality_signature_audit.py` -- collapsed exact-P8 overlap-graph signature neutrality audit.
- `v7/code/p23_overlap_graph_mgf_bound.py` -- collapsed overlap-graph component mgf bound receipt.
- `v7/code/p23_transfer_operator_cycle_theorem.py` -- collapsed transfer-operator cycle-tax theorem receipt.
- `v7/code/p23_overlap_component_factorization_audit.py` -- collapsed exact-P8 overlap-component factorization hostile audit.
- `v7/code/p23_diagonal_identity_rarity_bound.py` -- collapsed diagonal hidden-identity rarity bound receipt.
- `v7/code/p23_split_sample_diagonal_artifact_audit.py` -- collapsed split-sample diagonal-artifact and quotient-collapse receipt.
- `v7/code/p23_direct_unlabeled_likelihood_ladder.py` -- collapsed direct exact-denominator split `S_8` likelihood ladder.
- `v7/code/p23_selected_class_probability_formula.py` -- collapsed selected-class exact `P_N(C)` denominator formula receipt.
- `v7/code/p23_selected_rare_class_n10_n12_audit.py` -- collapsed selected rare-class audit at `N=10` and `N=12` canonicalization wall.
- `v7/code/p23_n12_invariant_screen_selected_count.py` -- collapsed `N=12` invariant-screen selected-count receipt.

**External.**

- L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, *Space-time as a causal set*, Phys. Rev. Lett. 59, 521 (1987) -- order plus number as geometry.
- D. Kleitman, B. Rothschild, *Asymptotic enumeration of partial orders on a finite set*, Trans. Amer. Math. Soc. 205, 205 (1975), https://www.ams.org/journals/tran/1975-205-00/S0002-9947-1975-0369090-9/S0002-9947-1975-0369090-9.pdf -- KR dominance of layered orders.
- L. Glaser, S. Surya, *Towards a Definition of Locality in a Manifoldlike Causal Set*, Phys. Rev. D 88, 124026 (2013), https://arxiv.org/abs/1309.3403 -- interval abundance as a locality/manifoldlikeness diagnostic.
- A. Eichhorn, H. Mack, K. T. Le, F. Wagner, *Charting causal set configuration space with graph observables*, https://arxiv.org/abs/2605.27514 -- graph observables and interval abundance distinguishing causal-set classes.
- S. Carlip, *Causal Sets and an Emerging Continuum*, https://arxiv.org/html/2405.14059v2 -- overview of the non-manifold dominance and action-suppression problem.
- S. Janson, *Poset limits and exchangeable random posets*, https://arxiv.org/abs/0902.0306 -- poset limits by finite pattern densities.
- J. Hladky, A. Mathe, V. Patel, O. Pikhurko, *Poset limits can be totally ordered*, https://arxiv.org/abs/1211.2473 -- ordered-kernel representation of poset limits.
- A. A. Razborov, *Flag algebras*, J. Symbolic Logic 72, 1239-1282 (2007), https://doi.org/10.2178/jsl/1203350785 -- finite-pattern density inequalities via flag algebras.
- D. M. T. Benincasa, F. Dowker, *Scalar Curvature of a Causal Set*, Phys. Rev. Lett. 104, 181301 (2010), https://arxiv.org/abs/1001.2725 -- nonlocal layer/action route.
- S. A. Adamson, P. Wallden, *Benincasa-Dowker-Glaser causal set actions by quantum counting*, https://arxiv.org/pdf/2505.22217 -- interval-volume counting for BDG actions.
