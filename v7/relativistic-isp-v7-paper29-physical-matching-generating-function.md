# Relativistic ISP v7 Paper XXIX: The Physical Matching Generating Function

**Status:** preprint, not peer reviewed, version 2026-06-27. Twenty-ninth paper of the v7 program. This paper follows the remaining fork from Paper XXVIII: find the exact generating object behind the physical coefficient-root envelope, or falsify the plausible simpler objects. It then pivots the result into the projection-sufficiency invariant: the matching/root campaign is a diagnostic for record-visible likelihood residue, not the law itself. Numerical receipts are in `v7/code/p29_matching_generating_identity.py`, `v7/code/p29_cycle_determinant_surrogate.py`, `v7/code/p29_labelled_cycle_index_correction.py`, `v7/code/p29_exact_2core_sector_decomposition.py`, `v7/code/p29_sector_cancellation_stability.py`, `v7/code/p29_sector_signature_audit.py`, `v7/code/p29_matching_root_radius_audit.py`, `v7/code/p29_profile_envelope_implication.py`, `v7/code/p29_zero_free_radius_no_go.py`, `v7/code/p29_sector_shape_amplitude_no_go.py`, `v7/code/p29_top_order_lambda_boundary.py`, `v7/code/p29_top_order_beta_boundary.py`, `v7/code/p29_lower_order_dominance_audit.py`, `v7/code/p29_near_top_defect_profile.py`, `v7/code/p29_deep_defect_peak_boundary.py`, `v7/code/p29_defect_saddle_motion_audit.py`, `v7/code/p29_projection_sufficiency_invariant.py`, `v7/code/p29_projected_likelihood_basis_audit.py`, `v7/code/p29_controlled_projection_martingale.py`, `v7/code/p29_flag_deck_reconstruction_audit.py`, `v7/code/p29_deck_ambiguity_certificate.py`, `v7/code/p29_flag_compression_no_go.py`, `v7/code/p29_flag_operator_family_audit.py`, `v7/code/p29_flag_interaction_expansion_audit.py`, `v7/code/p29_greedy_flag_operator_selection.py`, `v7/code/p29_greedy_operator_robustness.py`, `v7/code/p29_score_polynomial_sufficiency.py`, `v7/code/p29_adversarial_score_family_audit.py`, `v7/code/p29_unresolved_nullspace_audit.py`, `v7/code/p29_projection_ward_tower.py`, `v7/code/p29_effective_action_projection_identity.py`, `v7/code/p29_flag_deletion_projectivity.py`, `v7/code/p29_multivariate_score_polynomial.py`, `v7/code/p29_rook_hit_expansion_certificate.py`, `v7/code/p29_rare_spike_amplification.py`, `v7/code/p29_targeted_atom_amplification.py`, `v7/code/p29_n8_transfer_and_nullspace.py`, `v7/code/p29_n8_polynomial_minimal_cover.py`, `v7/code/p29_minimal_cover_ladder.py`, `v7/code/p29_deletion_flow_conflict_cover.py`, `v7/code/p29_washout_sector_promotion_bound.py`, `v7/code/p29_admissibility_norm_audit.py`, `v7/code/p29_n9_feasibility_probe.py`, `v7/code/p29_n9_active_flag_scan.py`, `v7/code/p29_n9_active_minimal_cover.py`, `v7/code/p29_worst_unresolved_atom_attack.py`, `v7/code/p29_omitted_local_flag_spike_scan.py`, `v7/code/p29_hidden_lift_realizability.py`, `v7/code/p29_admissibility_candidate_norms.py`, `v7/code/p29_palm_flag_sufficiency_audit.py`, `v7/code/p29_cover_transfer_matrix.py`, `v7/code/p29_external_math_campaigns.py`, `v7/code/p29_rooted_deletion_score_recurrence.py`, `v7/code/p29_boundary_histogram_minimal_cover.py`, and `v7/code/p29_boundary_cover_transfer.py`, at mpmath `dps = 140`.

## 1. What is settled and what is not

Paper XXVIII ended with the narrowed theorem target:

$$
q_{N,r}(D_{\mathrm{phys}})
\le
C\left(\frac{\beta}{N}\right)^r
$$

for the physical density-matched rank-copula in the bounded-width domain.

This paper does not prove that all-`N`, all-`r` theorem.

It does settle the generating object:

$$
R_N(z;D)
=
\sum_{r=0}^{\lfloor N/2\rfloor}
\rho_{N,r}(D)z^r,
$$

where

$$
\rho_{N,r}(D)
=
\frac{1}{(N)_{2r}}
\sum_{\substack{(i_1,j_1,\ldots,i_r,j_r)\\ \text{all }2r\text{ endpoints distinct}}}
\prod_{a=1}^r D_{i_a j_a}.
$$

For symmetric zero-diagonal `D`, this is the ordinary weighted matching polynomial followed by falling-factor normalization:

$$
\rho_{N,r}(D)
=
\frac{2^r r!}{(N)_{2r}}
m_{N,r}(D),
$$

if `m_{N,r}` counts each unordered edge set once. In the dynamic-program convention used in the receipts, the edge ordering is already included, so the equivalent formula is

$$
\rho_{N,r}(D)
=
\frac{2^r}{(N)_{2r}}
\widetilde m_{N,r}(D).
$$

The click-law coefficient is then

$$
q_{N,r}(D)
=
\binom{\lfloor N/2\rfloor}{r}
\rho_{N,r}(D)^2.
$$

So the missing theorem is not about choosing a better diagnostic. It is about bounding this exact normalized matching generating function.

## 2. Literature orientation

This object sits near three known structures, but is not identical to any one of them.

1. **Monomer-dimer matching polynomials.** Heilmann and Lieb prove strong zero-location results for monomer-dimer systems with nonnegative dimer activities in [Theory of monomer-dimer systems](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-25/issue-3/Theory-of-monomer-dimer-systems/cmp/1103857921.pdf). That positivity hypothesis is exactly what fails here: the physical residue kernel is signed.

2. **MacMahon/master-theorem determinant shadows.** Reciprocal determinants naturally enumerate cycle structures; see the standard statement of [MacMahon's master theorem](https://en.wikipedia.org/wiki/MacMahon%27s_master_theorem). This explains why a determinant appears in the leading 2-core expansion.

3. **Degenerate U-statistic expansions.** Row-zero kernels force leading independent terms to vanish; collision diagrams and trace/cycle terms become the first surviving terms.

4. **Flag algebras.** Razborov's [flag algebra](https://doi.org/10.2178/jsl/1203350785) framework explains why finite induced pattern densities and positive semidefinite constraints form a natural algebra of local observables.

5. **Graph and poset limits.** Lovasz-Szegedy graph limits and Janson's [poset limits and exchangeable random posets](https://arxiv.org/abs/0902.0306) show how all finite pattern densities can converge to a limiting object. This paper needs a stricter, interval-rooted and causal version, not plain dense-pattern convergence.

6. **Causal-set locality and curvature.** Benincasa-Dowker [causal-set scalar curvature](https://arxiv.org/abs/1001.2725) and Glaser-Surya [manifoldlike locality](https://arxiv.org/abs/1309.3403) are nearby because they extract continuum-like data from order intervals and layers.

7. **Local weak limits.** Benjamini-Schramm/Aldous-Lyons style local weak convergence, including Aldous-Lyons [processes on unimodular random networks](https://arxiv.org/abs/math/0603062), suggests the right form of a rooted Palm law, but causal sets are not bounded-degree graphs. The replacement neighborhood has to be an order interval or causal diamond.

8. **Rook, heap, and ordered-partition theory.** The score-polynomial receipts are close to q-rook/hit polynomials, as in Haglund's [q-rook polynomials](https://arxiv.org/abs/math/9706219), Cartier-Foata/Viennot heap expansions, and Stanley's [ordered structures and partitions](https://bookstore.ams.org/memo-1-119), where hidden permutation weights are converted into local incompatibility, hit, or partition data.

9. **Sufficiency and comparison of experiments.** Blackwell's [comparison of experiments](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-24/issue-2/Equivalent-Comparisons-of-Experiments/10.1214/aoms/1177729032.full) and Halmos-Savage [sufficiency via Radon-Nikodym](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-20/issue-2/Application-of-the-Radon-Nikodym-Theorem-to-the-Theory-of/10.1214/aoms/1177730032.full) are the statistical ancestor of the projection rule: only the likelihood visible to the committed record sigma-field can matter.

10. **Information projection and renormalization.** Csiszár's [I-divergence geometry](https://projecteuclid.org/journals/annals-of-probability/volume-3/issue-1/I-Divergence-Geometry-of-Probability-Distributions-and-Minimization-Problems/10.1214/aop/1176996454.short) supports the KL projection identity, while Wilson's [renormalization group](https://link.aps.org/doi/10.1103/RevModPhys.47.773) gives the physical analogy: hidden variables should be integrated out into an effective record action, not retained as unobservable machinery.

11. **Local covariance.** Brunetti-Fredenhagen-Verch's [generally covariant locality principle](https://arxiv.org/abs/math-ph/0112041) is not imported as a theorem here, but it gives the right discipline: the object assigned by the theory must be natural under the allowed embeddings/presentations. In this paper the analogous discipline is record covariance.

12. **Causal reconstruction.** The Hawking-King-McCarthy-Malament line, summarized in causal-set reviews such as [Surya's review](https://link.springer.com/article/10.1007/s41114-019-0023-1), explains why causal order plus volume is the right continuum target. The record-law problem is stricter: it must also suppress or penalize non-manifoldlike finite orders.

13. **Algebraic statistics and Markov bases.** Diaconis-Sturmfels [Markov bases](https://projecteuclid.org/journals/annals-of-statistics/volume-26/issue-1/Algebraic-algorithms-for-sampling-from-conditional-distributions/10.1214/aos/1030563990.full) give the closest external language for hidden fibers, sufficient statistics, and finite binomial conflict certificates. In this paper they are proof/gauge moves inside fibers, not physical Markov dynamics.

14. **Incidence algebras and decomposition spaces.** Rota-style incidence algebra and modern [decomposition-space](https://arxiv.org/abs/1404.3202) language fit the deletion/insertion recurrences: finite records decompose into smaller records plus boundary data. This is decomposition bookkeeping, not stochastic divisibility.

15. **Gibbs/non-Gibbs projection.** Projecting a local hidden law can produce a non-quasilocal visible law; see van Enter-Fernandez-Sokal on [non-Gibbsian images under transformations](https://doi.org/10.1007/BF02099312). The record version is the atom-spike warning: projection covariance does not imply admissible projected locality.

16. **Weisfeiler-Leman and coherent configurations.** WL/color-refinement and coherent configurations are a possible compression language for record-intrinsic tuple observables. They are compatible only when quotient-invariant and causal/Palm-rooted; bounded-depth WL equivalence is not physical equivalence if the projected likelihood differs.

17. **Modular/noncongruence and Tutte universality, as warnings.** Atkin-Swinnerton-Dyer/Scholl-style noncongruence phenomena motivate caution about finite q-polynomial certificates without stable Hecke-like operators; see Li-Long's [survey](https://arxiv.org/abs/1303.6228). Tutte universality motivates deletion recurrences, but the ordinary graph/matroid Tutte polynomial is not the record law.

13. **Entropy of non-manifoldlike orders.** Kleitman-Rothschild [asymptotic enumeration of finite partial orders](https://www.ams.org/journals/tran/1975-205-00/S0002-9947-1975-0369090-9/S0002-9947-1975-0369090-9.pdf) is the background warning: generic posets are not manifoldlike. A record law cannot merely sample "orders"; it must contain a projection/admissibility principle strong enough to avoid staged or clustered entropy.

14. **Palm and Mecke structure.** Last-Penrose [Lectures on the Poisson Process](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf) and the Cambridge chapter on the [Mecke equation and factorial measures](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/2A82E29EEA4CECC1C90B9ABE2358BB1E/9781316104477c4_p26-37_CBO.pdf/mecke_equation_and_factorial_measures.pdf) support the Palm/Mecke analogy. The import here is structural, not literal: causal sets need rooted intervals and diamonds in place of Euclidean balls.

15. **Kretschmann warning.** Norton's discussion of [general covariance and the Kretschmann objection](https://www.cambridge.org/core/books/symmetries-in-physics/general-covariance-gauge-theories-and-the-kretschmann-objection/8C755B19E8F302B034E2CD3E970AA4E2) is the caution behind record covariance. Covariance is empty unless the allowed presentations, committed sigma-field, and admissible likelihood class are specified.

The paper therefore uses these literatures as orientation, not as a solved theorem imported wholesale.

## 3. Receipt 1: exact matching identity

The first receipt, `p29_matching_generating_identity.py`, computes `rho_{N,r}` in two independent ways:

1. directed disjoint-pair dynamic programming;
2. unordered weighted matching dynamic programming plus the exact `2^r`/falling-factor normalization.

For the physical kernel and two hostile kernels at `N=12`, the maximum identity error is

$$
4.10026617893499069\times 10^{-142}.
$$

The maximum error in the `q` transform is

$$
4.61279945130186453\times 10^{-143}.
$$

This proves the finite bookkeeping theorem used by the rest of the campaign:

> the coefficient-root envelope is a theorem about a normalized signed matching polynomial.

## 4. Receipt 2: naive reciprocal determinant

The obvious next guess is the reciprocal determinant

$$
C_N(z;D)
=
\det\left(I+2z\frac{D}{N}\right)^{-1}.
$$

Its logarithm is

$$
\log C_N(z;D)
=
-\operatorname{Tr}\log\left(I+2z\frac{D}{N}\right)
=
\sum_{k\ge 1}
(-1)^k\frac{2^k}{k}
\operatorname{Tr}\left(\frac{D}{N}\right)^k z^k.
$$

This is the right spectral shadow at the first cycle level. For `r=2`, the physical relative error decreases from

$$
0.58984375
$$

at `N=8` to

$$
0.300411522633744856
$$

at `N=18`.

But the naive determinant is falsified as the full finite object. The maximum physical fixed-`r` error in the audit is

$$
0.999186775289901438.
$$

The determinant also does not select physical kernels. It tracks the same spectral shadow for adversaries whose beta values are much too high.

Therefore:

> the determinant is not the answer. It is the leading shadow of the answer.

## 5. Receipt 3: labelled cycle-index correction

The failed determinant guess opened the next object: labelled 2-regular quotient cycles plus exact falling-factor inflation.

For `r<=5`, the labelled cycle shapes are:

| `r` | cycle shapes |
|---:|---|
| 2 | `(2): 2` |
| 3 | `(3): 8` |
| 4 | `(2,2): 12`, `(4): 48` |
| 5 | `(2,3): 160`, `(5): 384` |

The labelled cycle-index contribution is exact at `r=2`; the maximum `r=2` error is

$$
4.89515787022036771\times 10^{-141}.
$$

It improves the higher-order story but still fails as the full finite object. At `N=12,c=0.5,r=5`, the physical exact scaled coefficient is

$$
N^5\rho_{N,5}
=
-14.2307626321130969,
$$

while the labelled cycle-index contribution is

$$
-807.961247086147345.
$$

So the cycle-index term is not a small perturbation around the answer. It is one large term in a larger signed cancellation.

## 6. Receipt 4: exact 2-core sector decomposition

The fourth receipt, `p29_exact_2core_sector_decomposition.py`, follows the opening fully. It decomposes the exact Möbius/falling-factor expansion by quotient vertex count `v`.

For `r` directed pair factors and endpoint partition `\pi`, the exact term is

$$
\frac{N^r}{(N)_{2r}}
\mu(\pi)\operatorname{hom}_D(G_\pi),
$$

where

$$
\mu(\pi)
=
\prod_{B\in\pi}
(-1)^{|B|-1}(|B|-1)!.
$$

After row-zero and zero-diagonal cancellation, only 2-core quotient graphs survive.

At `N=12,c=0.5,r=5`, the physical sector decomposition is:

| `v` | signed sector |
|---:|---:|
| 2 | `144.969538289564006` |
| 3 | `-870.768695951944937` |
| 4 | `1519.52964211641518` |
| 5 | `-807.961247086147345` |
| total | `-14.2307626321130969` |

The exact reconstruction error is

$$
3.6207253\times 10^{-136}.
$$

For the `q_2`-calibrated staged block at the same `N,r`, the sectors are:

| `v` | signed sector |
|---:|---:|
| 2 | `5.46915262905555514` |
| 3 | `-232.887277933964008` |
| 4 | `1060.65697707749537` |
| 5 | `-1066.35027530610238` |
| total | `-233.111423533515465` |

The physical cancellation factor at `r=5` is

$$
234.929723014264218,
$$

while the staged block cancellation factor is

$$
10.1469230769230769.
$$

This is the first genuinely new object of the campaign:

> the physical coefficient is small because large signed 2-core sectors cancel, not because every sector is individually small.

Positive activity bounds are therefore the wrong theorem.

## 7. Receipt 5: cancellation-factor no-go

The fifth receipt asks whether the scalar cancellation factor is itself the theorem.

It is not.

Across the physical bounded-width grid `N in {10,12,14}`, `c in {0.5,1,2,4}`, the `r=5` sector expansion reconstructs the physical coefficients with maximum error

$$
3.6986106644724053\times 10^{-136}.
$$

Physical cancellation is real; the minimum audited physical cancellation factor is

$$
13.8901713368661863.
$$

But staged blocks overlap this scalar. The maximum staged cancellation factor in the audit is

$$
23.4229296575866973,
$$

while the staged beta remains high:

$$
\min \beta_{\mathrm{block}}
=
1.51275055859471921.
$$

Therefore:

> cancellation factor alone is falsified as a separator.

The theorem must use the full signed sector profile.

## 8. Receipt 6: sector-signature audit

The sixth receipt keeps the full `r=5` sector signature:

$$
(S_2,S_3,S_4,S_5).
$$

It audits three profile numbers:

$$
\text{top share}
=
\frac{|S_5|}{\sum_v |S_v|},
$$

$$
\text{low share}
=
\frac{|S_2|+|S_3|}{\sum_v |S_v|},
$$

and

$$
\text{centroid}
=
\frac{\sum_v v|S_v|}{\sum_v |S_v|}.
$$

On the audited rows, physical kernels separate from staged blocks.

The physical maximum top-sector share is

$$
0.300771101927395313,
$$

while the staged minimum is

$$
0.388236832641318207.
$$

The physical maximum centroid is

$$
3.97259660463784737,
$$

while the staged minimum is

$$
4.24593548146037766.
$$

This does not prove the all-order theorem, but it gives the right next invariant:

> physical kernels distribute signed 2-core mass lower in quotient-vertex sectors; staged blocks concentrate too much mass near the top sector.

## 9. Receipt 7: scaled matching-root radius

The final receipt studies the scaled generating polynomial

$$
A_N(w)
=
R_N(Nw)
=
\sum_r N^r\rho_{N,r}w^r.
$$

In same-`N` comparisons, the physical scaled root radius is larger than the `q_2`-calibrated staged block radius. The minimum same-`N` margin in the audit is

$$
0.24492434200180929.
$$

The physical radius decreases across the audited ladder:

| `N` | physical minimum scaled root radius |
|---:|---:|
| 8 | `0.630819890685779344` |
| 10 | `0.536971735211171587` |
| 12 | `0.466618320505914817` |
| 14 | `0.411958113858324506` |
| 16 | `0.368398198926458998` |
| 18 | `0.332951926772831977` |

So the missing theorem is not a naive constant-radius theorem. It is a correctly scaled zero-free/radius theorem for the physical sector-profile generating function.

## 10. Receipt 8: factorial-normalized profile envelope

The eighth receipt, `p29_profile_envelope_implication.py`, gives the exact bridge that the previous radius language was missing.

Define

$$
a_{N,r}
=
N^r\rho_{N,r},
$$

and

$$
\lambda_{N,r}
=
\left(\frac{|a_{N,r}|}{\sqrt{r!}}\right)^{1/r}.
$$

Then, for even `N`,

$$
N q_{N,r}^{1/r}
=
\lambda_{N,r}^2
\frac{((N/2)_r)^{1/r}}{N}.
$$

This is exact, not asymptotic. It means that a factorial-normalized profile envelope for the scaled matching coefficients is precisely the missing coefficient-root envelope, with the finite falling factor included.

In particular, if

$$
\lambda_{N,r}
\le
\Lambda
$$

uniformly, then the conservative bound

$$
q_{N,r}
\le
\left(\frac{\Lambda^2}{2N}\right)^r
$$

follows immediately.

The audited physical grid stays below the conservative threshold

$$
\sqrt{2}.
$$

The maximum audited physical value is

$$
1.39792118738412459,
$$

at `N=18,c=0.5,r=9`. The threshold is sharp enough to be meaningful: the conservative beta from this value is

$$
0.977091823068720388.
$$

The `q_2`-calibrated high-beta adversaries violate the threshold. At `N=12`, the balanced block has

$$
\max_r \lambda_{N,r}
=
2.83638575425714721,
$$

and the rank-one Fourier witness has

$$
\max_r \lambda_{N,r}
=
1.87666305764351588.
$$

The low-beta three-mode Fourier witness remains below it:

$$
1.24235521305765043.
$$

So the theorem target changes from

> prove a vague zero-free disk,

to

> prove a uniform physical bound on the factorial-normalized sector profile `lambda_{N,r}`.

## 11. Receipt 9: zero-free radius no-go

The ninth receipt, `p29_zero_free_radius_no_go.py`, closes a tempting shortcut.

A zero-free disk alone does not imply the coefficient-root envelope. The counterexample is the polynomial

$$
A(w)
=
\left(1+\frac{w}{\gamma}\right)^d.
$$

All roots sit at `-\gamma`, so the root radius is exactly `\gamma`. With `N=80`, `d=40`, and `\gamma=0.5`, the fake coefficient-root stress is

$$
1089.21072341397741
$$

at `r=2`. The factorial-normalized profile sees the problem immediately:

$$
\lambda
=
46.969917578190706.
$$

Thus:

> root location is useful only after a coefficient majorant or sector-profile envelope is present.

## 12. Receipt 10: sector shape/amplitude no-go

The tenth receipt, `p29_sector_shape_amplitude_no_go.py`, closes the other tempting shortcut:

> maybe the sector shape alone is the law.

It is not. Scaling the physical kernel by a factor `s` leaves top-sector share and centroid invariant, but it scales `lambda` linearly and beta quadratically.

At `N=12,c=0.5,r=5`, the physical top-sector share and centroid remain fixed under scaling:

$$
\text{top share}
=
0.241670916725508611,
$$

$$
\text{centroid}
=
3.89448927596038074.
$$

But scaling by `2` changes

$$
\lambda_5:
1.0537255492513266
\mapsto
2.1074510985026532,
$$

and changes maximum beta by a factor of `4`, reaching

$$
1.37974956318634114.
$$

Therefore:

> the theorem must be amplitude-normalized sector-profile control, not sector shape alone.

## 13. Receipt 11: top-order lambda boundary

The eleventh receipt, `p29_top_order_lambda_boundary.py`, follows the sharpest possible opening from the `sqrt(2)` profile envelope:

> the hostile physical point is top matching order at `c=0.5`.

The receipt computes only the top-order perfect-matching coefficient, allowing the ladder to go beyond the all-order audit.

The result is decisive:

> the conservative `lambda < sqrt(2)` shortcut is false.

The top-order ladder is:

| `N` | top `lambda` | top beta |
|---:|---:|---:|
| 8 | `0.978384019965538353825448` | `0.264838747230478634450751` |
| 10 | `1.06691245580852806991486` | `0.296547194676158672416138` |
| 12 | `1.1539628867735697542917` | `0.332219040523683031806839` |
| 14 | `1.23828348272101172768352` | `0.370195190621980969652009` |
| 16 | `1.31959137895626684555982` | `0.409684017745808057347166` |
| 18 | `1.39792118738412459053476` | `0.450240250624399189778881` |
| 20 | `1.47342888930282125807905` | `0.491591844259603802774792` |
| 22 | `1.54630964551661346009444` | `0.533561402196658302936626` |

The first crossing of `sqrt(2)` occurs at

$$
N=20.
$$

This does not falsify the coefficient-root envelope. It only falsifies the conservative shortcut. The exact finite-falling beta remains below the working guard through `N=22`:

$$
\max \beta_{\mathrm{top}}
=
0.533561402196658302936626.
$$

Therefore the theorem target moves again:

> prove the finite-falling top-order beta boundary, not `lambda<sqrt(2)`.

## 14. Receipt 12: top-order beta boundary

The twelfth receipt, `p29_top_order_beta_boundary.py`, attacks the revised target directly.

For top order `r=N/2`,

$$
\beta_{N,N/2}
=
\lambda_{N,N/2}^2
\frac{((N/2)!)^{2/N}}{N}.
$$

This falling factor is what saves the coefficient-root envelope after the `sqrt(2)` crossing. At `N=22`, the falling factor is

$$
0.2231472172538361526834.
$$

The receipt proves the finite identity on the ladder with maximum error

$$
2.62417035451839404\times 10^{-141}.
$$

Top beta is monotone increasing through `N=22` and remains below `0.65`.

But the receipt also follows the hostile opening: naive tail fits are unstable. A linear `1/N` fit gives a limit

$$
0.8054462835082274131211,
$$

while a quadratic `1/N` fit gives

$$
1.199786459402558009681.
$$

So finite fits do not prove subcriticality. The next proof must be analytic: a top-order saddle, a finite-falling majorant, or an exact recurrence.

## 15. Receipt 13: lower-order dominance audit

The thirteenth receipt, `p29_lower_order_dominance_audit.py`, checks whether a top-order proof alone would imply the full all-order coefficient-root envelope.

It does not.

On the all-order physical `c=0.5` ladder through `N=18`, the maximum beta is close to top order, but not at top order except for `N=8`.

| `N` | beta-max order | max beta | top beta |
|---:|---:|---:|---:|
| 8 | 4 | `0.2648387472304786344508` | `0.2648387472304786344508` |
| 10 | 4 | `0.2985614753474662522816` | `0.2965471946761586724161` |
| 12 | 5 | `0.3449373907965852842989` | `0.3322190405236830318068` |
| 14 | 6 | `0.3901514080606160903548` | `0.370195190621980969652` |
| 16 | 7 | `0.435065185055689707256` | `0.4096840177458080573472` |
| 18 | 8 | `0.4799864577018425686206` | `0.4502402506243991897789` |

The maximum stays within one order of top in the audited ladder, and the largest max-minus-top margin is

$$
0.0297462070774433788.
$$

Thus:

> top order is the boundary layer, but not an exact dominance theorem.

The surviving proof target is a near-top/bulk split.

## 16. Receipt 14: near-top defect profile

The fourteenth receipt, `p29_near_top_defect_profile.py`, follows the near-top opening directly. It computes

$$
r
=
\frac{N}{2}-k,
\qquad
k=0,1,2,3,
$$

without computing all lower orders. For each subset `S` of size `2r`, it computes the perfect-matching sum `Haf(D|_S)` and uses

$$
\rho_{N,r}
=
\frac{2^r r!}{(N)_{2r}}
\sum_{|S|=2r}\operatorname{Haf}(D|_S).
$$

The method agrees with the all-order beta profile through `N=18`, with maximum error

$$
9.18459624081437915\times 10^{-141}.
$$

It then extends the near-top audit to `N=20,22`. The maximum audited near-top beta remains subcritical:

$$
0.579203708263368313058318
$$

at `N=22,k=2,r=9`.

But this receipt also falsifies the next tempting theorem:

> fixed one-defect dominance.

The best defect layers are:

| `N` | best `k` | best `r` | best near-top beta |
|---:|---:|---:|---:|
| 14 | 1 | 6 | `0.390151408060616090354847` |
| 16 | 1 | 7 | `0.435065185055689707255959` |
| 18 | 1 | 8 | `0.479986457701842568620624` |
| 20 | 2 | 8 | `0.529840941923840414118627` |
| 22 | 2 | 9 | `0.579203708263368313058318` |

So the boundary layer is not fixed. It widens.

The target is now:

> a widening near-top boundary layer plus a bulk bound.

## 17. Receipt 15: deep defect peak boundary

The fifteenth receipt, `p29_deep_defect_peak_boundary.py`, pushes the exact near-top defect method to `N=24,26` for `k=0..4`.

At `N=24`, the near-top peak remains at `k=2`:

| `k` | `r` | beta |
|---:|---:|---:|
| 0 | 12 | `0.576028244284529771482569` |
| 1 | 11 | `0.615477973311486669870347` |
| 2 | 10 | `0.628074591028772453046948` |
| 3 | 9 | `0.62226424258862154236681` |
| 4 | 8 | `0.600795393575369499703429` |

At `N=26`, the old `0.65` guard is falsified:

| `k` | `r` | beta |
|---:|---:|---:|
| 0 | 13 | `0.618907903345212430917128` |
| 1 | 12 | `0.660915234633738459465654` |
| 2 | 11 | `0.676614267360108067757209` |
| 3 | 10 | `0.674676438601639337734454` |
| 4 | 9 | `0.658054755763025963517734` |

The coefficient-root program is not dead: the `N=26` peak is still below `0.7`, and it is locally bracketed at `k=2`.

But the old numerical guard is dead:

$$
0.65
$$

is not the right theorem.

## 18. Receipt 16: defect saddle motion audit

The sixteenth receipt, `p29_defect_saddle_motion_audit.py`, stops recomputing matchings and analyzes the exact audited saddle table.

The best defect sequence through `N=26` is

$$
1,1,1,2,2,2,2
$$

for

$$
N=14,16,18,20,22,24,26.
$$

The peak beta is monotone increasing and reaches

$$
0.676614267360108067757209
$$

at `N=26`.

The gap between `k=2` and `k=3` is closing:

| `N` | `beta(k=2)-beta(k=3)` |
|---:|---:|
| 20 | `0.0159496828496716276` |
| 22 | `0.0103889316373219568` |
| 24 | `0.00581034844015091068` |
| 26 | `0.00193782875846873002` |

A linear diagnostic predicts `k=3` overtaking `k=2` around

$$
N\approx 26.6562712178195635.
$$

The same kind of diagnostic predicts the `0.7` guard being stressed around

$$
N\approx 26.9480141979238886.
$$

These are not proofs. They are warnings against the next false theorem:

> fixed `k=2` and beta `<0.7` are finite observations, not laws.

The real target is a moving defect saddle and its limiting peak beta.

## 19. The invariant behind the failed numerical guards

The campaign above shows what the invariant is not.

It is not the `sqrt(2)` lambda guard. It is not the `0.65` beta guard. It is not fixed one-defect dominance. It is not fixed `k=2`. Those were useful stress probes, but every one of them tried to turn a certificate into a principle.

The principle lives one level higher.

Let

$$
\pi_N:\widetilde\Omega_N\to \mathcal R_N
$$

be a hidden lift of the committed finite record space. The hidden space may contain coordinates, stages, fibers, labels, cellular automaton states, density fields, or construction clocks. The projection forgets all uncommitted machinery and keeps only the record object.

Let

$$
\widetilde P_N,\widetilde Q_N
$$

be two hidden laws, and let their record pushforwards be

$$
P_N=(\pi_N)_\#\widetilde P_N,
\qquad
Q_N=(\pi_N)_\#\widetilde Q_N.
$$

The only likelihood ratio available to the click law is

$$
L_N(R)
=
\frac{dQ_N}{dP_N}(R).
$$

Equivalently, if the hidden likelihood is

$$
\widetilde L_N(\omega)
=
\frac{d\widetilde Q_N}{d\widetilde P_N}(\omega),
$$

then the record likelihood is the predictable projection

$$
L_N(\pi_N(\omega))
=
\mathbb E_{\widetilde P_N}
\left[
\widetilde L_N
\mid
\pi_N
\right](\omega).
$$

Thus every hidden lift has an exact decomposition

$$
\widetilde L_N
=
L_N\circ\pi_N+\eta_N,
\qquad
\mathbb E_{\widetilde P_N}
\left[
\eta_N
\mid
\pi_N
\right]
=0.
$$

The second moment splits as

$$
\mathbb E_{\widetilde P_N}
\left[
\widetilde L_N^2
\right]
=
\mathbb E_{P_N}
\left[
L_N^2
\right]
+
\mathbb E_{\widetilde P_N}
\left[
\eta_N^2
\right].
$$

This is the invariant:

> the click law may depend on `L_N`, the record-visible likelihood residue, but not on `eta_N`, the hidden conditional residue, unless `eta_N` is promoted to committed records.

In nontechnical terms: hidden machinery may be used to generate records, but it is not allowed to keep a private account book. If the account book changes record predictions, its projected likelihood field is part of the record law. If it does not change record predictions, it is representation-only.

## 20. Receipt 17: projection-sufficiency invariant

The seventeenth receipt, `p29_projection_sufficiency_invariant.py`, checks the finite algebra exactly.

The test uses a hidden space with eight hidden atoms projected to four committed record atoms. First, it changes only hidden bookkeeping inside the fibers. The record pushforward is unchanged:

| record | `P_R` | hidden-bookkeeping `Q_R` |
|---|---:|---:|
| `A` | `0.25` | `0.25` |
| `B` | `0.416666666666666667` | `0.416666666666666667` |
| `C` | `0.25` | `0.25` |
| `D` | `0.0833333333333333333` | `0.0833333333333333333` |

Every record test has zero gap. The record second moment is

$$
S_{\mathrm{record}}=1,
$$

but the hidden second moment is

$$
S_{\mathrm{hidden}}
=
1.69444444444444444444444444444444444.
$$

The excess

$$
0.694444444444444444444444444444444444
$$

is pure hidden conditional residue. It is invisible to committed records.

Second, the receipt applies a fiber-measurable record likelihood with levels

$$
L\in\{0.5,1.2,3.0\}.
$$

The record-visible tilted law is

| record | `Q_R` |
|---|---:|
| `A` | `0.125` |
| `B` | `0.5` |
| `C` | `0.125` |
| `D` | `0.25` |

Now the hidden and record second moments agree:

$$
S_{\mathrm{record}}
=
S_{\mathrm{hidden}}
=
1.475.
$$

Third, the receipt mixes record-visible tilt with hidden conditional scrambling. The record second moment remains

$$
S_{\mathrm{record}}=1.475,
$$

but the hidden second moment rises to

$$
S_{\mathrm{hidden}}=2.1775.
$$

The difference

$$
0.7025
$$

is again non-record residue.

Finally, grouping records by exact likelihood level preserves the full record chi-square:

| likelihood level | `P` mass | `Q` mass |
|---:|---:|---:|
| `0.5` | `0.5` | `0.25` |
| `1.2` | `0.416666666666666667` | `0.5` |
| `3.0` | `0.0833333333333333333` | `0.25` |

The receipt ends with

`CHECKS PASSED: 8/8`

The finite conclusion is exact:

> the canonical sector promoted by a hidden refinement is its projected likelihood field, not its hidden construction history.

## 21. What this does to the matching/root campaign

The matching polynomial remains valuable, but its status changes.

The exact coefficient

$$
q_{N,r}(D)
$$

is no longer a candidate law by itself. It is a detector for one family of projected likelihood residues: sparse-pair, 2-core, without-replacement residue in the physical rank-copula.

So the right question is not:

> what numerical beta guard is the click law?

The right question is:

> is the matching/root sector a complete certificate for the projected likelihood residue of the hidden refinement under attack?

If yes, proving the moving defect saddle plus the bulk bound proves washout for that hidden refinement. If no, the missing sector is not "a better beta constant"; it is a record-visible likelihood component not represented by the matching polynomial.

This explains the repeated pattern in Papers XXII-XXIX:

| failed target | why it failed | invariant replacement |
|---|---|---|
| finite alpha profile | hidden constructions can fake finitely many moments | full projected likelihood field |
| recursive interval profile | staged/fiber laws can match selected intervals | projective sufficiency across all committed records |
| bracket/action scalar | tuned laws can hide outside the chosen action basis | action as approximation to `log L_N` |
| root radius | coefficients can stress despite radius control | coefficient profile as one residue sector |
| fixed beta guard | near-top saddle moves with `N` | asymptotic projected likelihood bound |

The old numerical campaign was not wasted. It found a real sector. But the invariant says that a sector is final only when it is the whole projected likelihood field or a provably sufficient representation of it.

## 22. Projection classification of adversaries

The hidden-refinement fork now has a sharper decision table.

| hidden construction | projected status | click-law consequence |
|---|---|---|
| deterministic machine with the same record law | same `Q_N=P_N` | representation-only |
| hidden labels permuted inside record fibers | same `Q_N=P_N` | no click-law dependence |
| staged/fiber block with changed order frequencies | nontrivial `L_N` | record-visible sector or action required |
| density modulation with no record pushforward change | no record residue | physically redundant at record level |
| density modulation with interval/order residue | nontrivial `L_N` | density/regularity sector required |
| coordinate marks used only in a construction | hidden conditional residue | inadmissible unless committed as records |
| quadratic/bracket action | approximation to `\log L_N` | useful if it represents the projected field |
| matching/root sector | sparse-pair projection of `L_N` | useful certificate, not the principle |

This also states the missing theorem more cleanly.

For each admissible hidden refinement family:

$$
\widetilde Q_N
\xrightarrow{\pi_N}
Q_N,
$$

one must prove either

$$
\sup_N
\mathbb E_{P_N}
\left[
\left(\frac{dQ_N}{dP_N}\right)^2
\right]
<\infty,
$$

or identify a projectively stable record statistic approximating

$$
\log\frac{dQ_N}{dP_N}.
$$

The matching/root theorem is one possible proof of the first alternative for a particular sparse-pair hidden residue. It is not the general invariant.

## 23. Receipt 18: projected likelihood basis audit

The eighteenth receipt, `p29_projected_likelihood_basis_audit.py`, performs the first direct basis audit against the invariant.

The finite record space is the quotient of two-dimensional permutation orders by unlabeled order isomorphism. The null law `P_N` is the pushforward of the uniform permutation law. The hidden staged/fiber adversary weights a permutation `pi` by

$$
3^{s(\pi)},
$$

where `s(pi)` is the number of points whose coarse `x` half and coarse `y` half agree. This hidden block score is then projected to unlabeled record orders, giving `Q_N` and hence the exact record likelihood

$$
L_N=\frac{dQ_N}{dP_N}.
$$

All probabilities are exact rational counts. The projection of `log L_N` is computed with mpmath `dps=140`.

The first basis is the current known-sector family:

| sector | features |
|---|---|
| scalar | relation count, height, width |
| interval | interval counts by interior size |
| regularity | comparability-degree moments and range |
| matching | disjoint relation-edge matchings of sizes `2` and `3` |

Then the receipt follows the residual into induced-suborder flag profiles: all unlabeled `3`-, `4`-, and `5`-point induced suborder counts. Finally, the full record-type flag is included as a tautological exact basis.

The result is:

| `N` | record classes | `S=E_P[L^2]` | known-sector `R^2` | +`3`-flags | +`4`-flags | +`5`-flags | full type |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `6` | `315` | `4.958979279498760018240537721057201576682` | `0.772903111821423431628657` | `0.772903111821423431628657` | `0.828554175791134904002946` | `0.847023845449284316256691` | `1.0` |
| `7` | `1956` | `6.09942419269613979182159246416269920088` | `0.704097056696214224579348` | `0.743630056668416402190381` | `0.781720618765961743458022` | `0.841428360108242087515858` | `1.0` |

The known sectors do not reconstruct the projected likelihood. At `N=7`, the known-sector residual norm is

$$
0.779162260977320502517295,
$$

with maximum pointwise residual

$$
2.44581758342566716575218.
$$

The induced flags improve the projection but also do not close it at finite `k=5`. The full record-type flag reconstructs `log L_N` exactly, as it must, because it is the whole finite record atom.

The receipt ends with

`CHECKS PASSED: 4/4`

The conclusion is not that finite flags are the final law. The conclusion is narrower and more useful:

> the missing projected likelihood is not spanned by the present scalar/interval/regularity/matching basis; the next natural closure is a flag-algebra or induced-suborder profile, with coefficient decay or projective compression still to be proved.

## 24. Receipt 19: controlled projection martingale

The nineteenth receipt, `p29_controlled_projection_martingale.py`, turns the projection principle into an exact predictive law.

Let `G` be any committed record-sector sigma-field: scalar features, interval features, regularity features, matching features, flags, or any projective combination of them. The optimal predictor of the full projected likelihood

$$
L_N=\frac{dQ_N}{dP_N}
$$

using only `G` is not chosen by regression. It is forced:

$$
L_{N,G}
=
\mathbb E_{P_N}[L_N\mid G].
$$

If `A` is a `G`-atom, then

$$
L_{N,G}(A)
=
\frac{Q_N(A)}{P_N(A)}.
$$

The captured second moment is

$$
S_{N,G}
=
\mathbb E_{P_N}[L_{N,G}^2],
$$

and the residual obeys the exact Pythagorean identity

$$
\mathbb E_{P_N}
\left[
(L_N-L_{N,G})^2
\right]
=
S_N-S_{N,G}.
$$

If

$$
G_1\subseteq G_2,
$$

then

$$
S_{N,G_1}\le S_{N,G_2}.
$$

So a controlled predictive law is a martingale problem:

$$
L_{N,G_0}
\to
L_{N,G_1}
\to
L_{N,G_2}
\to
\cdots
\to
L_N.
$$

The law is not the arbitrary choice of a feature vector. Once the filtration is chosen, the predictor is uniquely fixed by conditional likelihood.

The receipt audits the same finite staged/fiber toy from Receipt 18. The exact chi-square capture is:

| `N` | filtration | atoms | captured fraction | residual |
|---:|---|---:|---:|---:|
| `6` | scalar | `62` | `0.548619974328496410444752` | `1.78700416881310108166067941282` |
| `6` | scalar+interval | `131` | `0.990451010552338094706572` | `0.0378042513634457922054383563889` |
| `6` | +regularity | `174` | `0.999386523666932338104732` | `0.00242874009107775341541575307809` |
| `6` | +matching | `179` | `1.0` | `0.0` |
| `7` | scalar | `114` | `0.411428746338337441395702` | `3.00137449004777850428357786223` |
| `7` | scalar+interval | `527` | `0.661255820224746097720283` | `1.72740026548094017501711656163` |
| `7` | +regularity | `918` | `0.67010595551493292754564` | `1.68226967147352758346739737506` |
| `7` | +matching | `999` | `0.670990762176797956908217` | `1.67775766697615433977169060247` |
| `7` | +`3`-flags | `1893` | `0.996506455472859703065718` | `0.0178150654799604261245847744242` |
| `7` | +`4`-flags | `1955` | `0.999999124863595405737241` | `0.00000446269175349710073261141643892` |
| `7` | +`5`-flags | `1956` | `1.0` | `0.0` |

The receipt ends with

`CHECKS PASSED: 5/5`

This is the strongest predictive result in the paper:

> for any proposed controlled record-sector filtration, the predictive law is the likelihood martingale `E[L_N|G]`; the remaining physical problem is to find a projective filtration whose increments decay, compress, or expose a stable missing sector.

In the finite toy, the existing scalar/interval/regularity/matching filtration is not stable: it is exact at `N=6` but captures only

$$
0.670990762176797956908217
$$

of the chi-square residue at `N=7`. The first robust repair is induced-suborder flags. This points at a reconstruction/flag-algebra theorem rather than another scalar envelope.

## 25. Receipt 20: flag-deck reconstruction audit

The twentieth receipt, `p29_flag_deck_reconstruction_audit.py`, follows the flag opening directly.

It audits pure induced-suborder decks and known-sector-plus-deck filtrations for the same finite staged/fiber toy. The results are:

| `N` | filtration | atoms/classes | ambiguous atoms | max atom | captured fraction | residual |
|---:|---|---:|---:|---:|---:|---:|
| `6` | `flags3` | `293/315` | `19` | `3` | `0.949199110434071112257838` | `0.201119669171617223565275513327` |
| `6` | `flags4` | `315/315` | `0` | `1` | `1.0` | `0.0` |
| `6` | known | `179/315` | `131` | `4` | `1.0` | `0.0` |
| `7` | `flags3` | `1510/1956` | `325` | `6` | `0.911290256094027633551594` | `0.452368614201994441405740960387` |
| `7` | `flags4` | `1955/1956` | `1` | `2` | `0.999999124863595405737241` | `0.00000446269175349710073261141643892` |
| `7` | `flags5` | `1956/1956` | `0` | `1` | `1.0` | `0.0` |
| `7` | known | `999/1956` | `890` | `4` | `0.670990762176797956908217` | `1.67775766697615433977169060247` |
| `7` | known+`3`-flags | `1893/1956` | `63` | `2` | `0.996506455472859703065718` | `0.0178150654799604261245847744242` |
| `7` | known+`4`-flags | `1955/1956` | `1` | `2` | `0.999999124863595405737241` | `0.00000446269175349710073261141643892` |
| `7` | known+`5`-flags | `1956/1956` | `0` | `1` | `1.0` | `0.0` |

The receipt ends with

`CHECKS PASSED: 5/5`

The finite conclusion is:

> induced-suborder decks behave like a reconstruction filtration in the audited toy: `4`-decks reconstruct the `N=6` quotient, `5`-decks reconstruct the `N=7` quotient, and `4`-decks leave only one `N=7` ambiguity.

This is evidence for a flag-deck/projection theorem. It is not yet an asymptotic theorem.

## 26. Receipt 21: deck-ambiguity certificate

The twenty-first receipt, `p29_deck_ambiguity_certificate.py`, follows the single surviving `N=7` ambiguity after known sectors plus `4`-flags.

The ambiguous pair agrees on scalar, interval, regularity, matching, `3`-flag, and `4`-flag sectors. Both records have:

| quantity | value |
|---|---:|
| relations | `7` |
| height | `3` |
| width | `4` |
| interval profile prefix | `[6, 1, 0, 0, 0]` |

But their projected likelihoods differ:

$$
L_1
=
0.0187466523835029459025174076058,
\qquad
L_2
=
0.168719871451526513122656668452.
$$

The likelihood gap is

$$
0.149973219068023567220139260846.
$$

The `5`-flag deck separates them through ten finite flag entries. For example:

| flag | counts | delta | flag relations | flag height | flag width | flag intervals |
|---|---:|---:|---:|---:|---:|---|
| `flag5_16904` | `(2,3)` | `-1` | `3` | `2` | `3` | `[3,0,0,0]` |
| `flag5_17288` | `(0,1)` | `-1` | `5` | `3` | `2` | `[4,1,0,0]` |
| `flag5_24848` | `(2,1)` | `1` | `4` | `2` | `3` | `[4,0,0,0]` |
| `flag5_525076` | `(1,0)` | `1` | `5` | `3` | `2` | `[4,1,0,0]` |

The receipt ends with

`CHECKS PASSED: 4/4`

The point is precise:

> the last finite residue is not an unnamed hidden effect. It lives in the next induced-suborder layer.

## 27. Receipt 22: flag compression no-go

The twenty-second receipt, `p29_flag_compression_no_go.py`, performs the hostile check opened by Receipt 20.

Exact flag martingales repair the likelihood, but do they do so by a compact law or by nearly resolving record atoms? For `N=7`:

| filtration | atoms/classes | exact capture | linear/action rank | linear/action `R^2` |
|---|---:|---:|---:|---:|
| `flags3` | `1510/1956` | `0.911290256094027633551594` | `4` | `0.621301343061677535541682` |
| `flags4` | `1955/1956` | `0.999999124863595405737241` | `15` | `0.778620931186946918826415` |
| `flags5` | `1956/1956` | `1.0` | `62` | `0.839012543661347024802523` |
| known | `999/1956` | `0.670990762176797956908217` | `14` | `0.704097056696214224579348` |
| known+`3`-flags | `1893/1956` | `0.996506455472859703065718` | `15` | `0.743630056668416402190381` |
| known+`4`-flags | `1955/1956` | `0.999999124863595405737241` | `23` | `0.781720618765961743458022` |
| known+`5`-flags | `1956/1956` | `1.0` | `69` | `0.841428360108242087515858` |

The receipt ends with

`CHECKS PASSED: 4/4`

This blocks the false victory:

> finite deck exactness alone is too close to a lookup table. The click law needs controlled martingale increments, coefficient decay, renormalization, or compression. "Use all flags" is not yet a predictive law.

## 28. Receipt 23: flag operator-family audit

The twenty-third receipt, `p29_flag_operator_family_audit.py`, tests the Riemann-style hope that exact flag types can be grouped into simple geometric/operator families.

For each induced `k`-flag, the receipt groups flags by:

1. relation count, height, and width;
2. relation count, height, width, and interval profile;
3. relation count, height, width, interval profile, and degree moments.

At `N=7`, the result is:

| filtration | features | atoms/classes | exact capture | linear/action `R^2` |
|---|---:|---:|---:|---:|
| known | `16` | `999/1956` | `0.670990762176797956908217` | `0.704097056696214224579348` |
| grouped `(r,h,w)` | `40` | `776/1956` | `0.568489907585262289548864` | `0.722648215873733659654144` |
| known+grouped `(r,h,w)` | `56` | `1013/1956` | `0.671063398498379280717221` | `0.744412391034823373040183` |
| known+grouped interval geometry | `66` | `1029/1956` | `0.671063398498379280717221` | `0.745604201598357362594922` |
| known+degree-refined geometry | `71` | `1029/1956` | `0.671063398498379280717221` | `0.748548211240418446822517` |
| exact `3`-flags | `5` | `1510/1956` | `0.911290256094027633551594` | `0.621301343061677535541682` |
| known+exact `3`-flags | `21` | `1893/1956` | `0.996506455472859703065718` | `0.743630056668416402190381` |
| known+exact `5`-flags | `100` | `1956/1956` | `1.0` | `0.841428360108242087515858` |

The receipt ends with

`CHECKS PASSED: 5/5`

The conclusion is hostile to a simple geometric compression:

> relation/height/width/interval/degree grouping is informative but far too lossy. The projected likelihood sees finer induced order type.

## 29. Receipt 24: flag interaction expansion audit

The twenty-fourth receipt, `p29_flag_interaction_expansion_audit.py`, follows the next opening. If a linear flag action is too weak, perhaps the compact law is an operator-product expansion.

At `N=7`, adding products helps:

| action basis | features | rank | `R^2` |
|---|---:|---:|---:|
| known | `16` | `14` | `0.704097056696214224579348` |
| `3`-flags | `5` | `4` | `0.621301343061677535541682` |
| known+`3`-flags | `21` | `15` | `0.743630056668416402190381` |
| `3`-flags + quadratic products | `20` | `14` | `0.651056527881917381961495` |
| known+`3`-flags+quadratic products | `36` | `24` | `0.763684127367371025293373` |
| known+`3`-flags+known-by-`3` cross terms | `101` | `67` | `0.799908687294355449892666` |
| known+`3`-flags+quadratic+cross terms | `116` | `68` | `0.800037784431876780553483` |
| `4`-flags | `16` | `15` | `0.778620931186946918826415` |
| `4`-flags + quadratic products | `152` | `134` | `0.833281991455195432757126` |
| known+`5`-flags | `100` | `69` | `0.841428360108242087515858` |

The receipt ends with

`CHECKS PASSED: 5/5`

The conclusion is:

> operator products are real but insufficient in the audited basis. Quadratic/cross terms improve the action, but the gap remains.

## 30. Receipt 25: greedy flag-operator selection

The twenty-fifth receipt, `p29_greedy_flag_operator_selection.py`, follows the most important opening from the compression no-go.

Instead of asking whether all flags form a compact linear action, it asks:

> is the projected likelihood carried by a small exact subset of local flag operators?

Starting from known scalar/interval/regularity/matching sectors at `N=7`, greedy exact-martingale selection gives:

| step | captured fraction | atoms/classes | selected operator |
|---:|---:|---:|---|
| base | `0.670990762176797956908217` | `999/1956` | known sectors |
| `1` | `0.996506455472859703065718` | `1893/1956` | `flag3_36` |
| `2` | `0.999994603325505002046319` | `1946/1956` | `flag4_206` |
| `3` | `0.999999416575730270491494` | `1953/1956` | `flag5_17288` |
| `4` | `1.0` | `1955/1956` | `flag4_0` |
| `9` | `1.0` | `1956/1956` | full atom resolution reached |

The selected operators are concrete local suborder counts:

| operator | shape |
|---|---|
| `flag3_36` | relations `2`, height `2`, width `2`, intervals `[2,0]` |
| `flag4_206` | relations `5`, height `3`, width `2`, intervals `[3,2,0]` |
| `flag5_17288` | relations `5`, height `3`, width `2`, intervals `[4,1,0,0]` |
| `flag4_0` | relations `0`, height `1`, width `4`, intervals `[0,0,0]` |

The receipt ends with

`CHECKS PASSED: 4/4`

This is stronger than full deck reconstruction:

> finite predictive sufficiency arrives before full atom reconstruction. The target may be a small local operator filtration sufficient for `L_N`, not a full reconstruction of every record atom.

## 31. Receipt 26: greedy operator robustness

The twenty-sixth receipt, `p29_greedy_operator_robustness.py`, checks that the greedy result is not a coincidence of one staged/fiber strength.

For weight bases `2`, `3`, and `5`, the same four selected operators close the exact projected-likelihood gap before full atom reconstruction:

| weight base | `S_full` | known capture | step 1 | step 2 | step 3 | step 4 |
|---:|---:|---:|---:|---:|---:|---:|
| `2` | `2.3302175191730778535830067257` | `0.728588350335919302639399` | `0.995879779211011997838545` | `0.999907997483891034351253` | `0.999990053782042273983919` | `1.0` |
| `3` | `6.09942419269613979182159246416` | `0.670990762176797956908217` | `0.996506455472859703065718` | `0.999994603325505002046319` | `0.999999416575730270491494` | `1.0` |
| `5` | `15.647090631644014517222785232` | `0.634496576624514219150831` | `0.996548904820301419830171` | `0.999999893982788859107474` | `0.999999988538679876660268` | `1.0` |

In all three cases, step 4 has `1955/1956` atoms, not full atom reconstruction.

The receipt ends with

`CHECKS PASSED: 3/3`

The new theorem target is now sharper:

> find the projective local operator filtration that is predictively sufficient for the projected likelihood before it becomes a full record lookup table.

## 32. Receipt 27: score-polynomial sufficiency

The twenty-seventh receipt, `p29_score_polynomial_sufficiency.py`, follows the Ramanujan/Euler opening in the robustness result. The bases `2`, `3`, and `5` should not be treated as three numerological hits if there is an exact generating polynomial behind them.

For an unlabeled record class `R`, define the hidden-score fiber polynomial

$$
W_R(t)
=
\sum_{\pi:\,\pi\mapsto R} t^{s(\pi)},
$$

where `s(pi)` is the same-half staged/fiber score. The record-visible likelihood for weight base `t` is determined by the normalized projected partition function

$$
\frac{W_R(t)}{|\{\pi:\pi\mapsto R\}|}.
$$

Therefore a sector filtration is predictively sufficient for all weight bases `t` iff this normalized polynomial is identical for every record in each sector atom.

The receipt proves this exact finite statement at `N=7`:

| filtration | atom count | polynomial-violating atoms |
|---|---:|---:|
| known sectors | `999/1956` | `466` |
| known sectors + four greedy operators | `1955/1956` | `0` |

Removing any one of the four operators breaks the polynomial certificate:

| removed operator | polynomial-violating atoms |
|---|---:|
| `flag3_36` | `90` |
| `flag4_206` | `9` |
| `flag5_17288` | `6` |
| `flag4_0` | `1` |

The receipt ends with

`CHECKS PASSED: 5/5`

This upgrades the robustness result. The four-operator success is not merely a fit at bases `2`, `3`, and `5`; it is an exact score-polynomial identity for the whole one-parameter staged/fiber family at `N=7`.

It also reframes the problem. The record law is looking for a projected partition function:

$$
R
\mapsto
\mathbb E[t^{s(\pi)}\mid \pi\mapsto R],
$$

or, in the full physical setting,

$$
R
\mapsto
\mathbb E[\widetilde L_N\mid R].
$$

The hard part is proving that this conditional partition function has a projectively stable local-operator representation rather than an atom lookup table.

## 33. Receipt 28: adversarial score-family audit

The twenty-eighth receipt, `p29_adversarial_score_family_audit.py`, follows the hostile Feynman opening. If the four operators are truly structural, they should survive nearby hidden-score families. If they are merely a lucky finite list, an adversary should expose the gap.

The receipt tests six score families at `N=7`:

| score family | known capture | fixed-four capture | fixed-four polynomial bad atoms | fresh greedy flags |
|---|---:|---:|---:|---|
| same-half control | `0.670990762176797956908217` | `1.0` | `0` | `flag3_36`, `flag4_206`, `flag5_17288`, `flag4_0` |
| diagonal band | `0.999994176222854904007878` | `1.0` | `0` | `flag5_25088`, `flag3_0`, `flag3_32`, `flag3_36` |
| anti-diagonal band | `0.999935692964964798924095` | `1.0` | `0` | `flag4_2062`, `flag4_14`, `flag3_0`, `flag3_32` |
| parity match | `1.0` | `1.0` | `0` | `flag3_0`, `flag3_32`, `flag3_36`, `flag3_38` |
| lower-left block | `0.752154341310380224901671` | `1.0` | `0` | `flag3_36`, `flag4_206`, `flag5_17288`, `flag4_0` |
| central square | `0.996161485881111202252533` | `1.0` | `0` | `flag4_206`, `flag4_192`, `flag3_0`, `flag3_32` |

The surprising result is that the fixed four operators survive every audited natural coordinate tilt. They are not universal, however. The same receipt also targets the single unresolved two-record atom left by known sectors plus the four fixed operators. That hostile law gives:

| hostile score | known capture | fixed-four capture | fixed-four polynomial bad atoms | fresh greedy capture |
|---|---:|---:|---:|---:|
| targeted unresolved atom | `0.249702262802699483922191` | `0.499801508535132989281461` | `1` | `1.0` |

The receipt ends with

`CHECKS PASSED: 6/6`

So the scoped conclusion is:

> the four operators are a strong finite certificate for smooth coordinate-style hidden tilts in this toy, but not a universal record law. A spiky law aimed at the unresolved atom breaks them.

The next theorem must include an admissibility condition. The plausible split is:

$$
\text{regular hidden score}
\Rightarrow
\text{controlled local-operator sufficiency},
$$

while

$$
\text{spiky rare-atom score}
\Rightarrow
\text{promote a new sector or reject the hidden refinement}.
$$

## 34. Receipt 29: unresolved nullspace audit

The twenty-ninth receipt, `p29_unresolved_nullspace_audit.py`, follows the opened rare-pair path. It asks whether the information missed by known sectors plus the four greedy operators is a broad invisible subspace or a single rare spike.

Let `G` be the filtration generated by known sectors plus

$$
\{\texttt{flag3\_36},\texttt{flag4\_206},\texttt{flag5\_17288},\texttt{flag4\_0}\}.
$$

For every remaining exact `3`-, `4`-, and `5`-flag operator `O`, the receipt computes

$$
\mathbb E_P[\operatorname{Var}_P(O\mid G)]
$$

exactly. The result is:

| quantity | value |
|---|---:|
| `G` atoms | `1955/1956` |
| unresolved atoms | `1` |
| positive invisible flag operators | `20` |
| unresolved null mass | `0.000793650793650793650793650793651` |

The unresolved pair has identical known-sector data:

| field | value |
|---|---|
| relations | `10` |
| height | `3` |
| width | `3` |
| intervals | `[7, 3, 0, 0, 0, 0]` |
| degree moments | `(20, 60, 188, 4, 2)` |
| null mass per record | `0.000396825396825396825396825396825` |

The top invisible local separators are:

| operator | conditional variance mass | unresolved-pair values |
|---|---:|---|
| `flag5_920` | `0.00178571428571428571428571428571428571` | `[1,4]` |
| `flag5_664` | `0.00178571428571428571428571428571428571` | `[3,0]` |
| `flag5_17304` | `0.000793650793650793650793650793650793651` | `[2,0]` |
| `flag4_200` | `0.000793650793650793650793650793650793651` | `[10,8]` |

The receipt ends with

`CHECKS PASSED: 5/5`

The finite hidden nullspace is therefore narrow. It is not a broad family of invisible local modes; it is concentrated on one rare two-record atom and is separated by ordinary local flags. This supports the scoped theorem target:

> regular hidden scores should wash out the rare nullspace, while spiky rare-atom scores must be promoted as sectors or excluded by admissibility.

## 35. Receipt 30: projection Ward tower

The thirtieth receipt, `p29_projection_ward_tower.py`, makes the Einstein/Noether branch finite and exact.

Let `Omega_tilde_N` be a hidden state space, `R_N` be the committed record space, and `pi_N: Omega_tilde_N -> R_N` be the projection that forgets hidden labels, coordinates, stages, fibers, and construction clocks. If `P_tilde_N` and `Q_tilde_N` are hidden laws, then the hidden likelihood is

$$
\widetilde L_N
=
\frac{d\widetilde Q_N}{d\widetilde P_N},
$$

where `dQ/dP` means the likelihood ratio. The record likelihood is

$$
L_N
=
\frac{dQ_N}{dP_N},
$$

where `P_N` and `Q_N` are the hidden laws pushed forward to records.

The exact Ward identity is

$$
L_N\circ\pi_N
=
\mathbb E_{\widetilde P_N}[\widetilde L_N\mid \pi_N].
$$

The receipt also checks the tower law for a further committed coarsening `c`:

$$
L_{\mathrm{coarse}}\circ c
=
\mathbb E_{P_N}[L_N\mid c].
$$

The finite model has `12` hidden atoms, `5` record atoms, and `3` coarse atoms. A vertical perturbation changes the hidden second moment from

$$
1.07949996648291681108616153239
$$

to

$$
1.08057557561801136617758485979,
$$

while leaving record and coarse likelihoods unchanged. The record and tower gaps are exactly zero.

The receipt ends with

`CHECKS PASSED: 5/5`

This is the finite record-covariance theorem:

> hidden likelihood has a unique record-visible representative, and that representative has a unique coarsened representative. Vertical hidden bookkeeping can inflate hidden second moments, but it has zero record charge.

## 36. Receipt 31: effective action projection identity

The thirty-first receipt, `p29_effective_action_projection_identity.py`, follows the Witten/action branch.

For a committed feature filtration `G`, the projected law is

$$
Q_G(R)
=
P(R)\,\mathbb E_P[L\mid G](R),
$$

where `R` is a record, `P` is the baseline record law, `L=dQ/dP` is the full likelihood ratio, and `E_P[L|G]` is the average likelihood ratio inside the `G`-atom containing `R`.

Equivalently, the effective record action is

$$
S^{\mathrm{eff}}_G(R)
=
-\log \mathbb E_P[L\mid G](R)
+\text{constant}.
$$

The exact KL decomposition is

$$
D(Q\|P)
=
D(Q\|Q_G)
+
D(Q_G\|P).
$$

Here `D(A||B)` is relative entropy: the information distance from law `A` to law `B`.

For the staged/fiber `N=7` quotient:

| filtration | atoms | `D(Q||Q_G)` | `D(Q_G||P)` | `S_G` |
|---|---:|---:|---:|---:|
| known sectors | `999/1956` | `0.189619228902405465576048805567016212` | `0.854036908484484239292183630016604317` | `4.4216665257199854520499018616894308` |
| known+four | `1955/1956` | `0.0` | `1.04365613738688970486823243558362053` | `6.0994241926961397918215924641626992` |
| full atom | `1956/1956` | `0.0` | `1.04365613738688970486823243558362053` | `6.0994241926961397918215924641626992` |

The receipt ends with

`CHECKS PASSED: 5/5`

Thus action language is legitimate only when it means projected effective record action. Quadratic/bracket actions are approximations to this object, not replacements for it.

## 37. Receipt 32: flag deletion projectivity

The thirty-second receipt, `p29_flag_deletion_projectivity.py`, checks whether induced-flag operators at least belong to a projectively natural record algebra.

For a `k`-record flag `F` inside an `N`-record order `R`, the exact deletion identity is

$$
\sum_{v\in R}
\operatorname{count}_F(R\setminus v)
=
(N-k)\operatorname{count}_F(R).
$$

Here `count_F(R)` is the number of induced copies of `F` in `R`, and `R\v` is the record order after deleting one record `v`. Every copy of `F` survives exactly `N-k` one-record deletions.

The receipt checks all `3`-, `4`-, and `5`-flags in every `N=7` record class:

| quantity | value |
|---|---:|
| checked identities | `46072` |
| violations | `0` |

The selected operators are included in this projective family:

| operator | total count across classes |
|---|---:|
| `flag3_36` | `12295` |
| `flag4_206` | `3364` |
| `flag5_17288` | `807` |
| `flag4_0` | `1974` |

The receipt ends with

`CHECKS PASSED: 4/4`

This does not prove the four selected flags are physical, but it does prove they are not arbitrary coordinates. They sit in an exact deletion-covariant algebra of record-intrinsic local operators.

## 38. Receipt 33: multivariate projected score polynomial

The thirty-third receipt, `p29_multivariate_score_polynomial.py`, strengthens the score-polynomial result.

For a record `R`, define the multivariate projected partition function

$$
W_R(u_1,\ldots,u_m)
=
\sum_{\pi:\pi\mapsto R}
\prod_{i=1}^m u_i^{s_i(\pi)}.
$$

Here `pi` is a hidden labelled permutation projecting to public record `R`; `s_i(pi)` are hidden scores; and `u_i` are independent score weights.

The receipt uses six natural coordinate scores:

`same_half`, `diagonal`, `anti_diagonal`, `parity`, `lower_left`, and `central_square`.

Results:

| filtration | atoms | multivariate-bad atoms |
|---|---:|---:|
| known sectors | `999` | `485` |
| known+four | `1955` | `0` |

Adding a deliberate targeted atom coordinate breaks exactly one atom:

| extension | known+four bad atoms |
|---|---:|
| natural scores only | `0` |
| natural scores + targeted atom | `1` |

The receipt ends with

`CHECKS PASSED: 5/5`

So known+four does not merely determine one hidden score polynomial. At `N=7`, it determines the joint projected partition function for six natural hidden scores simultaneously. The break remains exactly the atom-spike branch.

## 39. Receipt 34: rook/hit expansion certificate

The thirty-fourth receipt, `p29_rook_hit_expansion_certificate.py`, gives the algebraic interpretation of the same-half score polynomial.

Writing

$$
t=1+z,
$$

the projected score polynomial becomes

$$
W_R(1+z)
=
\sum_k H_{R,k} z^k,
$$

where

$$
H_{R,k}
=
\sum_{\pi:\pi\mapsto R}
\binom{s(\pi)}{k}.
$$

Here `H_R,k` counts hidden permutations over `R` together with `k` selected nonattacking hits in the same-half board. This is the conditional rook/hit expansion of the projected partition function.

Results:

| check | value |
|---|---:|
| binomial-transform errors | `0` |
| known-sector hit-vector bad atoms | `466` |
| known+four hit-vector bad atoms | `0` |

The receipt ends with

`CHECKS PASSED: 4/4`

Thus the finite polynomial identity is not opaque numerology. It is a conditional hit-polynomial identity over hidden fibers.

## 40. Receipt 35: local-flag rare-spike amplification

The thirty-fifth receipt, `p29_rare_spike_amplification.py`, tests a hostile-looking but still local score: amplify the separator flag `flag5_920`.

For weight bases from `2` to `1000`, known sectors alone capture about half the chi-square residue, but known+four remains essentially exact:

| base | known capture | fixed-four capture | `+flag5_920` capture |
|---:|---:|---:|---:|
| `2` | `0.533928617200617240607321` | `0.998823170834189511973243` | `1.0` |
| `3` | `0.50976618254891811328337` | `0.999885509303909471764639` | `1.0` |
| `1000` | `0.499900770587307889153848` | `0.999999999999999999999999` | `1.0` |

The receipt ends with

`CHECKS PASSED: 4/4`

This falsified the first hostile expectation. Amplifying an ordinary local flag that separates the unresolved atom does not defeat known+four. The real adversary must directly target the unresolved atom rather than merely raise a local flag correlated with it.

## 41. Receipt 36: targeted rare-atom amplification

The thirty-sixth receipt, `p29_targeted_atom_amplification.py`, tests the genuinely hostile atom-spike law.

The target is one record in the single unresolved known+four atom. The unresolved atom has null mass

$$
0.000793650793650793650793650793650793651.
$$

For all audited bases, fixed-four capture remains

$$
0.499801508535132989281461,
$$

while adding `flag4_14` repairs the target exactly. The second moment grows from

$$
1.000396353297906471006496638077515
$$

at base `2` to

$$
1607.94874723561810778027175831485244
$$

at base `10000`.

The receipt ends with

`CHECKS PASSED: 4/4`

This proves the literal four-operator law is false over all possible projected laws. Atom-spiky residues must be promoted or excluded by an admissibility/regularity principle.

## 42. Receipt 37: `N=8` transfer and nullspace growth

The thirty-seventh receipt, `p29_n8_transfer_and_nullspace.py`, is the first finite projective stress test beyond `N=7`.

At `N=8`, the record quotient has `14794` classes. The same fixed four operators still determine the same-half projected polynomial and close the base-3 likelihood:

| filtration | capture | atoms |
|---|---:|---:|
| known sectors | `0.999330286645276266601345053127` | `7163/14794` |
| fixed four | `1.0` | `14757/14794` |

The fixed-four polynomial bad atom count is `0`.

But the nullspace grows:

| quantity | value |
|---|---:|
| unresolved atoms | `35` |
| max unresolved atom size | `4` |
| unresolved mass | `0.00381944444444444444444444444444444444` |
| invisible local flags | `74` |

Fresh greedy selection is not literally stable:

| step | operator | capture |
|---:|---|---:|
| `1` | `flags4:flag4_2062` | `0.999844156374668167045847307541` |
| `2` | `flags4:flag4_2176` | `0.9999985960520794309223109095` |
| `3` | `flags5:flag5_16904` | `1.0` |

The receipt ends with

`CHECKS PASSED: 5/5`

Conclusion:

> fixed four transfer strongly, but their literal greedy priority is not stable. The object is a bounded controlled local-operator filtration, not a canonical four-name list.

## 43. Receipt 38: `N=8` polynomial minimal cover

The thirty-eighth receipt, `p29_n8_polynomial_minimal_cover.py`, asks the finite algebraic question directly: what is the smallest local-flag subset that repairs the known-sector same-half polynomial conflicts at `N=8`?

The known sectors have `85` polynomial-bad atoms and `427` polynomial conflict pairs. Among exact `3`-, `4`-, and `5`-flag operators:

| search | result |
|---|---:|
| active conflict-cover flags | `80` |
| single-flag solutions | `0` |
| pair solutions | `0` |
| triple solutions listed | `6` |

The first sufficient triple is

$$
\{\texttt{flags4:flag4\_192},
\texttt{flags4:flag4\_2248},
\texttt{flags5:flag5\_16904}\}.
$$

It gives `14683/14794` atoms, max atom size `2`, and unresolved mass

$$
0.00887896825396825396825396825396825397.
$$

The receipt ends with

`CHECKS PASSED: 5/5`

Thus the finite object is best described as a small local conflict-cover problem. The cover size stays tiny, but the actual representatives drift.

## 44. Receipt 39: minimal conflict-cover ladder

The thirty-ninth receipt, `p29_minimal_cover_ladder.py`, follows the Euler recurrence demand. It asks how the exact minimal local-flag cover behaves across `N=6,7,8`.

For each `N`, it forms the known-sector atoms and asks for the smallest subset of exact induced `3`-, `4`-, and `5`-flag operators that makes the normalized same-half hidden score polynomial constant on every atom.

The ladder is:

| `N` | record classes | known bad atoms | minimal local cover size |
|---:|---:|---:|---:|
| `6` | `315` | `0` | `0` |
| `7` | `1956` | `466` | `4` |
| `8` | `14794` | `85` | `3` |

At `N=7`, the first listed minimal cover is exactly the four-operator certificate:

$$
\{\texttt{flags3:flag3\_36},
\texttt{flags4:flag4\_0},
\texttt{flags4:flag4\_206},
\texttt{flags5:flag5\_17288}\}.
$$

It leaves one unresolved atom of mass

$$
0.000793650793650793650793650793650793651.
$$

At `N=8`, the first listed minimal cover is the triple from Receipt 38:

$$
\{\texttt{flags4:flag4\_192},
\texttt{flags4:flag4\_2248},
\texttt{flags5:flag5\_16904}\}.
$$

It leaves unresolved mass

$$
0.00887896825396825396825396825396825397.
$$

The receipt ends with

`CHECKS PASSED: 5/5`

This is the cleanest finite statement so far:

> the exact cover size stays tiny through the audited ladder, but the representatives drift. The law is therefore not a fixed flag list; it is a controlled local conflict-cover problem.

## 45. Receipt 40: deletion flow of conflict covers

The fortieth receipt, `p29_deletion_flow_conflict_cover.py`, tests a possible confusion opened by Receipt 39.

If the selected finite covers drift, does that mean the local flag algebra itself is not projective?

No. For every `N=8` record class and every exact induced `3`-, `4`-, and `5`-flag operator, the receipt verifies

$$
\sum_{v\in R}
\operatorname{count}_F(R\setminus v)
=
(8-|F|)\operatorname{count}_F(R).
$$

It checks

$$
1242696
$$

identities with zero violations.

It then compares finite sufficiency across sizes:

| cover | `N=7` bad atoms | `N=8` bad atoms |
|---|---:|---:|
| `N=7` fixed four | `0` | `0` |
| first `N=8` minimal triple | `23` | `0` |

The first `N=8` triple leaves `N=7` unresolved mass

$$
0.015873015873015873015873015873015873.
$$

The receipt ends with

`CHECKS PASSED: 5/5`

So the algebra is projective, but finite sufficient covers are not immutable. This is exactly the distinction the click law needs:

> projective local operator algebra, controlled drifting covers, no sacred finite operator names.

## 46. Receipt 41: washout versus sector promotion

The forty-first receipt, `p29_washout_sector_promotion_bound.py`, makes the Feynman/adversary fork exact.

For any committed filtration `G`, the predictive miss is

$$
\mathbb E_P[(L-\mathbb E[L\mid G])^2]
=
\sum_{A\in G}P(A)\operatorname{Var}_P(L\mid A).
$$

If all non-singleton `G`-atoms live in a rare set `U`, then

$$
\mathbb E_P[(L-\mathbb E[L\mid G])^2]
\le
\mathbb E_P[L^2\mathbf 1_U]
\le
P(U)\sup_U L^2.
$$

This is the finite washout/sector-promotion theorem. Rare unresolved atoms are harmless only if the projected likelihood on them is controlled.

For the `N=7` known+four filtration, the unresolved mass is

$$
P(U)=0.000793650793650793650793650793650793651.
$$

The same-half hidden score has zero residual. An ordinary local-flag amplification by `flag5_920` also washes out in the audited high-base range:

| law | base | residual | capture |
|---|---:|---:|---:|
| local `flag5_920` spike | `1000` | `5.03982851249832520279889378734e-21` | `0.999999999999999999999999` |

But a direct atom target does not wash out:

| law | base | residual | `Q(U)` |
|---|---:|---:|---:|
| unresolved atom target | `10000` | `803.793339228614059469290359459` | `0.798865724099368959182043294193` |

The receipt ends with

`CHECKS PASSED: 5/5`

This is the first exact finite form of the admissibility rule:

> rare residue must either wash out under controlled projected likelihood, or be promoted as a record sector. A hidden law that concentrates most of its mass on a rare unresolved atom is no longer harmless hidden structure.

## 47. Receipt 42: admissibility norm audit

The forty-second receipt, `p29_admissibility_norm_audit.py`, follows the opening from Receipt 41. It turns the bound into a norm:

$$
A_2(G,L)
=
\mathbb E_P[L^2\mathbf 1_U],
\qquad
A_\infty(G,L)
=
P(U)\sup_U L^2,
$$

where `U` is the union of non-singleton atoms of the committed filtration `G`.

It audits three cases:

1. `N=7` fixed-four cover;
2. `N=8` fixed-four cover;
3. `N=8` first minimal triple.

The same-half law is exactly captured in all three cases. Direct atom targets concentrate sector-scale mass on `U`. The important surprise is that locality alone is not enough.

For the `N=8` fixed-four cover, a local `flag5_920` spike at base `2` has

$$
A_2
=
0.957817256204899537036401173248.
$$

So a local score can still be inadmissible relative to the wrong cover. When the relevant local separator is promoted into the cover, the residue can vanish. For the first `N=8` minimal triple, the audited local `flag5_16904` spike has residual zero at bases `2` and `10`.

The receipt ends with

`CHECKS PASSED: 6/6`

The refined admissibility lesson is:

> locality is not admissibility. The admissibility norm decides whether residue washes out, requires operator promotion, or forces sector promotion/exclusion.

## 48. Receipt 43: `N=9` feasibility probe

The forty-third receipt, `p29_n9_feasibility_probe.py`, does the cautious next step beyond `N=8`.

It exactly enumerates the `N=9` permutation-order quotient:

| quantity | value |
|---|---:|
| permutations | `362880` |
| record classes | `131526` |
| max class count | `40` |
| min class count | `1` |

Then it computes a lightweight known-sector partition using scalar, interval, and degree-regularity features, excluding matching counts. This is a feasibility probe, not the final known-sector theorem.

The known-lite conflict landscape is:

| quantity | value |
|---|---:|
| atoms | `47851/131526` |
| bad atoms | `25793` |
| bad mass | `0.634124228395061728395061728395061728` |
| conflict pairs | `87066` |
| max bad atom size | `46` |

A deterministic sample of `1024` record classes already sees the full `3`- and `4`-flag universes and most `5`-flags:

| flag size | observed types |
|---:|---:|
| `3` | `5` |
| `4` | `16` |
| `5` | `58` |

The receipt ends with

`CHECKS PASSED: 5/5`

This makes the next step precise:

> full `N=9` enumeration is feasible, but blind cover search is not the right first move. The right move is an active-flag scan over actual conflict pairs.

## 49. Receipt 44: `N=9` active-flag scan

The forty-fourth receipt, `p29_n9_active_flag_scan.py`, follows the active-scan opening.

It uses the exact `N=9` quotient and known-lite conflict pairs from Receipt 43, then computes induced `3`-, `4`-, and `5`-flag counts only on records that appear in those conflicts.

The exact scan finds:

| quantity | value |
|---|---:|
| conflict pairs | `87066` |
| conflict records | `80042` |
| observed flag universe | `84` |
| active flags | `84` |

The top active flags are already very strong:

| flag | conflicts separated |
|---|---:|
| `flags4:flag4_192` | `80066/87066` |
| `flags4:flag4_2176` | `79977/87066` |
| `flags3:flag3_36` | `76855/87066` |
| `flags3:flag3_6` | `76855/87066` |
| `flags4:flag4_2248` | `76061/87066` |

The greedy active cover closes all known-lite conflict pairs in eight steps:

| step | operator | remaining conflicts |
|---:|---|---:|
| `1` | `flags4:flag4_192` | `7000` |
| `2` | `flags4:flag4_2248` | `929` |
| `3` | `flags5:flag5_24848` | `296` |
| `4` | `flags4:flag4_14` | `118` |
| `5` | `flags5:flag5_25088` | `46` |
| `6` | `flags3:flag3_36` | `12` |
| `7` | `flags5:flag5_25104` | `3` |
| `8` | `flags5:flag5_25472` | `0` |

The receipt ends with

`CHECKS PASSED: 5/5`

This is not a minimal-cover theorem, and it uses known-lite sectors rather than the full known sector. But it is strong evidence for the controlled conflict-cover target:

> at `N=9`, local flags do not merely reduce conflict residue; a small greedy active set closes the exact known-lite score-polynomial conflicts.

## 50. Receipt 45: `N=9` active-mask minimal cover

The forty-fifth receipt, `p29_n9_active_minimal_cover.py`, turns the `N=9` greedy closure into an exact finite set-cover certificate on the active masks.

The setting is still known-lite: scalar, interval, and degree-regularity features, excluding matching counts. The conflict universe is the same `87066` known-lite score-polynomial conflict pairs from Receipt 43.

The receipt builds exact masks for all active induced `3`-, `4`-, and `5`-flags, then searches the finite set-cover instance. It finds:

| quantity | value |
|---|---:|
| active flags | `84` |
| nondominated flags | `80` |
| greedy cover size | `8` |
| exact cover size | `7` |
| exact search calls | `121363` |

Depths `1` through `6` fail. The first size-`7` witness is

$$
\{\texttt{flags3:flag3\_36},
\texttt{flags5:flag5\_16904},
\texttt{flags5:flag5\_25104},
\texttt{flags5:flag5\_8704},
\texttt{flags4:flag4\_14},
\texttt{flags4:flag4\_2248},
\texttt{flags5:flag5\_25488}\}.
$$

It covers all `87066` known-lite conflict pairs.

The receipt ends with

`CHECKS PASSED: 5/5`

This is the strongest finite conflict-cover result in the paper:

> `N=9` known-lite has `131526` record classes and `87066` exact score-polynomial conflict pairs, but the active local flag cover number is `7`.

The qualifier remains essential. This is not yet the comparable full-known `N=9` theorem, because matching features are omitted from the base sector. But it makes the controlled-cover hypothesis much harder to dismiss as a small-`N` accident.

## 51. Receipt 46: worst unresolved-atom attack

The forty-sixth receipt, `p29_worst_unresolved_atom_attack.py`, makes the rare-atom adversary exact.

Let `G` be a committed record filtration. Suppose `A` is a non-singleton `G`-atom and `x` is one record inside `A`. If a hostile projected law concentrates on `x`, then the projected miss after conditioning on `G` has the limiting residual

$$
\lim_{b\to\infty}
\mathbb E_P[(L_b-\mathbb E[L_b\mid G])^2]
=
\frac{1}{P(x)}-\frac{1}{P(A)}.
$$

This formula is the finite version of the washout/residue dichotomy. Small unresolved mass is not enough. A rare unresolved sector washes out only if the likelihood on it is controlled. If a law is allowed to put nearly all probability on one point inside the unresolved sector, the residue survives at order one or larger.

The receipt evaluates the exact limiting formula on the audited covers:

| cover | unresolved atom size | projected residual limit | capture at base `10^6` |
|---|---:|---:|---:|
| `N=7` fixed four | `2` | `1260` | `0.499801508535132989281461` |
| `N=8` fixed four | `4` | `15120` | `0.249962795773599880955197` |
| `N=8` first minimal triple | `2` | `20160` | `0.499987598898782211860807` |

The receipt ends with

`CHECKS PASSED: 5/5`

This proves a hard negative result:

> every non-singleton atom in a proposed finite filtration is a possible high-residue adversary unless the click law supplies an admissibility bound or promotes the atom-separating feature.

## 52. Receipt 47: omitted local-flag spike scan

The forty-seventh receipt, `p29_omitted_local_flag_spike_scan.py`, tests whether ordinary omitted local flags can act as high-residue adversaries.

For each omitted induced flag `F`, it defines the projected law

$$
Q_F(R)
\propto
P(R)\,2^{\operatorname{count}_F(R)}.
$$

This is deliberately milder than direct atom targeting: it is an ordinary local flag score. The result is still hostile.

For the `N=8` fixed-four cover, the strongest omitted local score in the audit is `flags5:flag5_920`:

| quantity | value |
|---|---:|
| residual | `0.446774178043229120847326` |
| `A_2` | `0.957817256204899537036401` |
| `Q(U)` | `0.00956644110425773998443021` |

For the first `N=8` minimal triple, the strongest omitted local score is `flags5:flag5_926`:

| quantity | value |
|---|---:|
| residual | `18956.9690726015044985623` |
| `A_2` | `37913.9382173321428162582` |
| `Q(U)` | `0.990490350856278364341481` |

The receipt ends with

`CHECKS PASSED: 5/5`

This corrects a tempting overstatement. The `N=7` fixed-four certificate survives the audited local `flag5_920` spike, but locality by itself is not an admissibility principle. At `N=8`, omitted local flags can be extremely relevant.

The correct rule is sharper:

> a local operator is harmless only relative to a committed filtration and a controlled likelihood class. If its projected residue is large, it must be added to the filtration, bounded by an admissibility theorem, or promoted as a physical sector.

## 53. Receipt 48: hidden-lift realizability

The forty-eighth receipt, `p29_hidden_lift_realizability.py`, closes a possible escape route.

One might try to reject the atom-spike or local-flag spike by saying that it is not a real hidden refinement. The receipt proves the opposite in the finite projection sense.

For any dominated projected law `Q << P`, choose any hidden fiber sizes `m_R` over records `R` and define

$$
\widetilde P(R,a)=\frac{P(R)}{m_R},
\qquad
\widetilde Q(R,a)=\frac{Q(R)}{m_R}.
$$

Then the hidden likelihood is fiber-constant:

$$
\widetilde L(R,a)=L(R).
$$

So

$$
\mathbb E[\widetilde L\mid R]=L(R),
\qquad
\mathbb E[(\widetilde L-L(R))^2]=0.
$$

The receipt checks this exactly for two hostile cases:

| case | hidden atoms | hidden/record second-moment gap | vertical residue |
|---|---:|---:|---:|
| `N=7` atom spike | `2586` | `0` | `0` |
| `N=7` local flag spike | `2586` | `0` | `0` |

The receipt ends with

`CHECKS PASSED: 5/5`

This is the cleanest version of the projection lesson:

> record projection is an invariant, not an admissibility condition. A hostile projected likelihood can always be realized by a fiber-constant hidden lift. To exclude it, the law needs a physical admissibility principle on projected likelihoods themselves, not merely a ban on hidden machinery.

## 54. Receipt 49: admissibility candidate norms

The forty-ninth receipt, `p29_admissibility_candidate_norms.py`, begins the first of the three theorem targets directly: admissibility of projected likelihoods.

The receipt tests three candidate finite controls:

1. unresolved `A_2` mass;
2. bounded local coefficient size;
3. promotion of the record-visible separator.

For the first `N=8` minimal triple, the omitted local score

$$
Q_F(R)\propto P(R)2^{\operatorname{count}_{\texttt{flag5\_926}}(R)}
$$

has only coefficient `log 2`, but it is still violently inadmissible relative to that filtration:

| quantity | value |
|---|---:|
| unresolved records | `222` |
| residual before promotion | `18956.9690726015044985622758129513822` |
| `A_2` before promotion | `37913.9382173321428162582099805815254` |
| `Q(U)` before promotion | `0.990490350856278364341481440869474689` |
| residual after promoting `flag5_926` | `0.0` |

For the direct atom spike at base `10^6`, the same filtration gives:

| quantity | value |
|---|---:|
| exact residual limit | `20160.0` |
| residual before full atom promotion | `18627.5869156693814040485065436003291` |
| `A_2` before promotion | `37255.24835509831481415948141383996` |
| `Q(U)` before promotion | `0.961586782515747573580795890491282001` |
| residual after full atom promotion | `0.0` |

The receipt ends with

`CHECKS PASSED: 5/5`

This receipt falsifies a tempting admissibility rule:

> bounded local coefficient size is not enough.

The finite rule that survives is filtration-relative:

> large unresolved `A_2` requires promoting the separator/sector or rejecting the projected likelihood class.

## 55. Receipt 50: causal Palm-flag sufficiency audit

The fiftieth receipt, `p29_palm_flag_sufficiency_audit.py`, begins the second theorem target: causal Palm-flag sufficiency.

It builds rooted, endpoint-symmetric, record-intrinsic features at `N=7`:

1. pair-rooted `3`-flags: an unordered root pair plus one outside record;
2. pair-rooted `4`-flags: an unordered root pair plus two outside records;
3. interval-overlap flags: two causal intervals and the sizes of their interiors, intersection, and union.

The feature counts are:

| family | count |
|---|---:|
| pair-rooted `3`-flags | `11` |
| pair-rooted `4`-flags | `66` |
| interval-overlap flags | `22` |

The likelihood-projection audit gives:

| filtration | rank | `R^2` | residual norm |
|---|---:|---:|---:|
| known sectors | `14` | `0.704097056696214224579348` | `0.779162260977320502517295` |
| known + pair-rooted `3` | `15` | `0.743630056668416402190381` | `0.725248468419146659265187` |
| known + pair-rooted `3,4` | `23` | `0.781720618765961743458022` | `0.669205687982860353617586` |
| known + pair-rooted `3,4` + overlap | `44` | `0.785725278312020578000384` | `0.663038484117538012108897` |
| known + unrooted `3`-flags | `15` | `0.743630056668416402190381` | `0.725248468419146659265187` |

The receipt ends with

`CHECKS PASSED: 5/5`

The result is deliberately scoped:

> rooted, endpoint-symmetric Palm flags add real projected-likelihood information beyond known sectors, but the audited rooted family does not close the staged/fiber likelihood.

So causal Palm-flag geometry is supported as a record-intrinsic carrier, not proved as a finished sufficiency theorem.

## 56. Receipt 51: cover-transfer matrix

The fifty-first receipt, `p29_cover_transfer_matrix.py`, begins the third theorem target: a finite-algebra recurrence for conflict covers.

It compares several covers across `N=6,7,8`:

- no local cover;
- the `N=7` fixed four;
- the first `N=8` minimal triple;
- the union of those two covers;
- the scoped `N=9` known-lite seven-flag witness, restricted to the flags that exist at the smaller `N`.

For `N=7`, the transfer rows are:

| cover | atoms/classes | bad atoms | conflicts | unresolved mass |
|---|---:|---:|---:|---:|
| none | `999/1956` | `466` | `508` | `0.931349206349206349206349` |
| `N=7` fixed four | `1955/1956` | `0` | `0` | `0.000793650793650793650793651` |
| first `N=8` triple | `1922/1956` | `23` | `23` | `0.015873015873015873015873` |
| union cover | `1956/1956` | `0` | `0` | `0.0` |
| `N=9` known-lite witness | `1956/1956` | `0` | `0` | `0.0` |

For `N=8`, the transfer rows are:

| cover | atoms/classes | bad atoms | conflicts | unresolved mass |
|---|---:|---:|---:|---:|
| none | `7163/14794` | `85` | `427` | `0.967410714285714285714286` |
| `N=7` fixed four | `14757/14794` | `0` | `0` | `0.00381944444444444444444444` |
| first `N=8` triple | `14683/14794` | `0` | `0` | `0.00887896825396825396825397` |
| union cover | `14777/14794` | `0` | `0` | `0.00183531746031746031746032` |
| `N=9` known-lite witness | `14787/14794` | `0` | `0` | `0.000694444444444444444444444` |

The receipt ends with

`CHECKS PASSED: 5/5`

The transfer result is asymmetric:

> the `N=7` fixed four close the audited `N=8` conflicts, but the first `N=8` minimal triple does not close `N=7`.

The scoped `N=9` witness transfers down for this audited score, but that is not a comparable physical theorem because the `N=9` base sector was known-lite.

The recurrence target is therefore not fixed operator names. It is:

> a transfer rule for residual conflict hypergraphs, probably requiring rooted deletion/insertion score-boundary tensors for `W_R(t)`.

## 57. Receipt 52: external mathematics compatibility campaigns

The fifty-second receipt, `p29_external_math_campaigns.py`, stress-tests seven outside mathematical programs against the finite staged/fiber quotient, with the Barandes/Shard rule enforced:

> hidden rewrites are proof or gauge structure, not physical divisible evolution.

The campaigns are deliberately hostile. Each outside analogy is allowed to help only if it respects indivisible committed records and the projected likelihood law.

| campaign | finite result | verdict |
|---|---:|---|
| algebraic statistics / Markov bases | adjacent same-fiber rewrites leave `1808` disconnected fibers | compatible only as fiber/binomial certificates, not dynamics |
| incidence Hopf / decomposition spaces | rooted deletion score-boundary recurrence has `0` errors and `8` boundary types at `N=6` | strongly compatible as decomposition bookkeeping |
| Gibbs/non-Gibbs projection | same-half law has `0` known+four bad atoms, atom-spike oscillation is `2012.73903666427030913012221423` | compatible as projected quasilocality/nonquasilocality |
| Weisfeiler-Leman / coherent configurations | bad atoms refine `466 -> 22 -> 1` under known, known+`3`-flags, known+`3,4`-flags | compatible as record-intrinsic refinement algebra |
| flag algebras / poset limits | `3`-flag deletion identity has `0` violations | compatible as deletion-projective flag-density coordinates |
| modular/noncongruence forms | fixed four transfer `N=7 -> N=8`, but first `N=8` triple fails at `N=7` with `23` bad atoms | useful only as a warning about missing Hecke-like stability |
| Tutte universality | full vertex-deletion deck gives `1956` groups for `1956` records | too reconstructive as a law; ordinary coarse sectors remain too weak |

The receipt ends with

`CHECKS PASSED: 10/10`

The strongest positive import is not modularity. It is:

> algebraic statistics plus incidence/decomposition algebra plus quasilocal projection.

Algebraic statistics says the right finite object is a fiber partition function and a sufficiency test:

$$
R
\mapsto
\frac{W_R(t)}{|\pi^{-1}(R)|}.
$$

Incidence/decomposition algebra says the right recurrence is not temporal divisibility, but record deletion with boundary data:

$$
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b}.
$$

Projected Gibbs/quasilocality says the admissibility condition should forbid nonlocal dependence on unresolved record atoms, not forbid hidden presentations. The atom-spike branch is the finite non-Gibbs warning.

WL/coherent configurations and flag algebras give a candidate compression language for the committed record filtration. Modular/noncongruence and Tutte universality remain useful hostile analogies, but they are not literal structures in the current paper.

## 58. Receipt 53: rooted deletion score recurrence

The fifty-third receipt, `p29_rooted_deletion_score_recurrence.py`, attacks the score-boundary theorem directly.

For a hidden permutation `pi` at size `N`, deleting position `i` gives `d_i pi` at size `N-1`. Define

$$
R=\rho_N(\pi),
\qquad
A=\rho_{N-1}(d_i\pi),
\qquad
a=s_{N-1}(d_i\pi),
\qquad
b=s_N(\pi)-s_{N-1}(d_i\pi).
$$

The raw rooted deletion tensor is

$$
B_N^\downarrow(R,A;a,b)
=
\#\{(\pi,i):\rho_N(\pi)=R,\rho_{N-1}(d_i\pi)=A,
s_{N-1}(d_i\pi)=a,\Delta_i^-(\pi)=b\}.
$$

The receipt verifies exactly, for `N=6,7,8`,

$$
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b}.
$$

It also verifies the insertion/deletion mass identity for every child score sector. The receipt ends with

`CHECKS PASSED: 8/8`

The key finite results are:

| `N` | record classes | unique `Wbar` | unique compressed `Hbar` | unique full `Bbar` | recurrence errors |
|---:|---:|---:|---:|---:|---:|
| `6` | `315` | `9` | `28` | `315` | `0` |
| `7` | `1956` | `12` | `70` | `1956` | `0` |
| `8` | `14794` | `24` | `130` | `14794` | `0` |

Here `Hbar_R(a,b)` is the compressed score-loss histogram obtained from `Bbar` by forgetting the child record `A`.

The hostile result is important:

> the full boundary tensor is exact but too reconstructive. It is essentially full record data in this toy.

The live theorem target is therefore not the full `Bbar`. It is the compressed boundary needed for likelihood transfer:

$$
H_R(a,b)
=
\mathbb P(a,b\mid R).
$$

This compressed `Hbar` still reconstructs the normalized score polynomial `Wbar_R` exactly. The fixed four close `Wbar` at `N=7`, but not the full boundary tensor. The first `N=8` triple closes `Wbar` at `N=8`, but leaves `111` full-boundary conflicts.

## 59. Receipt 54: boundary-histogram minimal cover

The fifty-fourth receipt, `p29_boundary_histogram_minimal_cover.py`, follows the opening from Receipt 53. If `Hbar` is the compressed transfer object, is it locally coverable by record-intrinsic flags?

At `N=7`, known sectors leave:

| quantity | value |
|---|---:|
| known atoms | `999/1956` |
| `Hbar` bad atoms | `469` |
| `Hbar` conflict pairs | `532` |
| active local flags | `76` |

The exact local cover found has size `4`:

$$
\{
\texttt{flags3:flag3\_36},
\texttt{flags4:flag4\_2062},
\texttt{flags4:flag4\_192},
\texttt{flags5:flag5\_525184}
\}.
$$

At `N=8`, known sectors leave:

| quantity | value |
|---|---:|
| known atoms | `7163/14794` |
| `Hbar` bad atoms | `4616` |
| `Hbar` conflict pairs | `5922` |
| active local flags | `84` |

The exact local cover found has size `5`:

$$
\{
\texttt{flags3:flag3\_36},
\texttt{flags5:flag5\_549376},
\texttt{flags4:flag4\_2176},
\texttt{flags4:flag4\_206},
\texttt{flags5:flag5\_24576}
\}.
$$

The receipt ends with

`CHECKS PASSED: 4/4`

The result keeps the recurrence path alive:

> `Hbar` is stricter than `Wbar`, but still locally coverable in the audited window.

It also sharpens the cost. At `N=8`, the `Wbar` conflict cover has size `3`, while the `Hbar` cover has size `5`.

## 60. Receipt 55: boundary-histogram cover transfer

The fifty-fifth receipt, `p29_boundary_cover_transfer.py`, follows the next hostile opening. Do the small `Hbar` covers transfer, or do they drift?

For `N=7`:

| cover | atoms/classes | `Hbar` bad atoms | `Hbar` conflicts | unresolved mass |
|---|---:|---:|---:|---:|
| none | `999/1956` | `469` | `532` | `0.931349206349206349206349` |
| `Wbar` `N=7` fixed four | `1955/1956` | `0` | `0` | `0.000793650793650793650793651` |
| `Wbar` `N=8` triple | `1922/1956` | `24` | `24` | `0.015873015873015873015873` |
| `Hbar` `N=7` cover | `1955/1956` | `0` | `0` | `0.000793650793650793650793651` |
| `Hbar` `N=8` cover | `1955/1956` | `0` | `0` | `0.000793650793650793650793651` |
| `Hbar` union | `1956/1956` | `0` | `0` | `0.0` |

For `N=8`:

| cover | atoms/classes | `Hbar` bad atoms | `Hbar` conflicts | unresolved mass |
|---|---:|---:|---:|---:|
| none | `7163/14794` | `4616` | `5922` | `0.967410714285714285714286` |
| `Wbar` `N=7` fixed four | `14757/14794` | `12` | `14` | `0.00381944444444444444444444` |
| `Wbar` `N=8` triple | `14683/14794` | `62` | `62` | `0.00887896825396825396825397` |
| `Hbar` `N=7` cover | `14766/14794` | `8` | `10` | `0.00292658730158730158730159` |
| `Hbar` `N=8` cover | `14776/14794` | `0` | `0` | `0.00193452380952380952380952` |
| `Hbar` union | `14791/14794` | `0` | `0` | `0.000297619047619047619047619` |

The receipt ends with

`CHECKS PASSED: 5/5`

The result is the clean recurrence-campaign endpoint:

> the compressed boundary is locally coverable, but its small covers drift across `N`.

Thus the theorem must control boundary-cover drift. It cannot be a fixed-name law, and it cannot stop at finite `Wbar` sufficiency.

## 61. Six-campaign synthesis

The six independent review angles converged on the same invariant.

**Einstein/Noether angle.** The fundamental covariance is record covariance: no law may depend on hidden labels, stages, fibers, coordinates, or machine states except through their committed record projection. The finite Ward identity is

$$
L_N\circ\pi_N
=
\mathbb E[\widetilde L_N\mid \pi_N].
$$

Vertical hidden perturbations with zero conditional expectation have no record charge.

**Feynman/adversary angle.** The four-operator certificate is not fake, but the universal version is false without scope. Natural coordinate tilts pass; direct unresolved-atom tilts fail by the exact formula `1/P(x)-1/P(A)`; and at `N=8`, ordinary omitted local flags can also fail hard. This points to a regularity/admissibility axiom on projected likelihoods, not a literal four-operator law and not locality alone.

**Riemann/geometric angle.** The geometric object should be a causal Palm-flag metric-measure law: rooted interval flags, overlap flags, rank-copula/volume bins, and layer-curvature probes, sampled intrinsically from the order. The deletion receipt proves that induced flags already have exact projective covariance under one-record deletion. The target filtration is

$$
\mathcal G^{\mathrm{geom}}_{m,N}
=
\sigma(
\text{rooted interval flags, overlap flags, volume bins, curvature probes up to complexity }m
).
$$

The predictive theorem would be

$$
\lim_{m\to\infty}
\limsup_{N\to\infty}
\mathbb E_{P_N}
\left[
\left(L_N-\mathbb E[L_N\mid\mathcal G^{\mathrm{geom}}_{m,N}]\right)^2
\right]
=0.
$$

**Witten/action angle.** The record action should be an effective action after integrating out hidden machinery:

$$
\exp(-S^{\mathrm{eff}}_N(R))
\propto
\mathbb E[
\exp(-S^{\mathrm{hidden}}_N(\omega))
\mid
\pi_N(\omega)=R
].
$$

The flag operators are candidate relevant operators in this effective record action. A quadratic/bracket action is only a low-order approximation unless it is tied to this projection identity. The KL receipt proves the projected action identity exactly in the finite quotient.

**Ramanujan/polynomial angle.** The numeric robustness became an exact generating-polynomial theorem:

$$
R
\mapsto
\frac{W_R(t)}{|\pi_N^{-1}(R)|}.
$$

This suggests q-rook, hit-polynomial, heap, and cluster-expansion methods. The theorem target is a multivariate projected partition function, not one fitted base. The rook/hit receipt proves the conditional hit expansion exactly for the same-half score polynomial.

**Euler/finite-algebra angle.** The finite algebraic core is a sequence of exact partitions of record classes by local operators. The `N=9` active-mask cover number `7` is the strongest scoped finite certificate so far, while the atom-spike and omitted-flag receipts prove why every cover result must be paired with an admissibility norm. The central question is minimal sufficient filtration:

$$
\mathcal G_0
\subset
\mathcal G_1
\subset
\cdots
\subset
\sigma(R_N),
\qquad
L_{N,k}
=
\mathbb E[L_N\mid\mathcal G_k],
$$

with controlled increments and no atom lookup. The `N=8` receipts sharpen this into a local conflict-cover problem: fixed four transfer, but minimal covers drift, so the invariant is controlled cover size and projective stability rather than fixed operator names.

The common rule is therefore:

> hidden structure is admissible only through its record-projected effective likelihood; a click law is a projectively stable, record-intrinsic, controlled local-operator filtration sufficient for that likelihood.

## 62. Six parallel campaign expansion

The scientist-audit campaigns make the preceding rule more explicit. The six lines of attack are not six rival laws. They are six constraints on the same missing object.

### Campaign A: record covariance and hidden-presentation equivalence

The Einstein/Noether branch says that hidden presentation variables are not physical coordinates unless their likelihood survives projection to committed records.

Let

$$
\pi_N:\widetilde \Omega_N\to \mathcal R_N
$$

forget labels, stages, construction clocks, coordinates, and uncommitted fibers. Let `P_tilde_N,Q_tilde_N` be hidden laws, and let `P_N,Q_N` be their record pushforwards. The only record-covariant likelihood is

$$
L_N
=
\frac{dQ_N}{dP_N}
=
\frac{d(\pi_N)_\#\widetilde Q_N}{d(\pi_N)_\#\widetilde P_N}.
$$

Equivalently,

$$
L_N\circ \pi_N
=
\mathbb E_{\widetilde P_N}
\left[
\widetilde L_N\mid \pi_N
\right].
$$

Thus every hidden likelihood decomposes into a record-visible representative plus a vertical residue of zero conditional mean. The vertical residue is presentation gauge: it may inflate hidden norms, but it has no record charge. If it predicts future records, then it is not hidden and must be promoted to a committed mark, sector, or action.

The hostile objection is the Kretschmann objection: covariance can be empty if the allowed presentation maps and committed sigma-field are not specified. The repair is to state record covariance as a projective equivalence principle:

> two hidden presentations are physically equivalent iff they induce the same projected record likelihood on every committed coarsening/deletion of the record sigma-field.

But this principle has a converse warning. Every dominated projected law `Q_N << P_N` has a fiber-constant hidden lift. Therefore projection covariance alone does not exclude hostile projected likelihoods.

### Campaign B: operational admissibility fork

The Feynman/adversary branch says: a law is not saved by being rare, local, flag-like, or hidden. The only operational question is whether the projected likelihood can concentrate on an unresolved committed sector.

Let `G_N` be a committed record filtration and let `U_N` be the union of non-singleton `G_N`-atoms. The finite operational admissibility norm is

$$
A_2(G_N,L_N)
=
\mathbb E_{P_N}
\left[
L_N^2\mathbf 1_{U_N}
\right].
$$

Rare unresolved atoms wash out only when this norm is controlled. If `A_2(G_N,L_N)` stays large, the residue is not representation-only. Either the operator separating it must be promoted to the committed filtration, or the hidden refinement must be rejected as physically inadmissible.

The direct atom-spike family proves the point. If `A` is a non-singleton `G_N`-atom and `x in A`, then the spike

$$
Q_b(R)
\propto
P_N(R)b^{\mathbf 1_{R=x}}
$$

has limiting residual

$$
\lim_{b\to\infty}
\mathbb E_{P_N}
\left[
\left(L_b-\mathbb E[L_b\mid G_N]\right)^2
\right]
=
\frac{1}{P_N(x)}-\frac{1}{P_N(A)}.
$$

The omitted-local-flag scan proves that locality alone is not admissibility. An omitted bounded-size local flag can carry sector-scale likelihood mass on `U_N`.

The operational theorem target is:

> define a physically preparable class `A_phys` of projected likelihoods such that, for the chosen projective filtration `G_N`, either `sup_{L in A_phys} A_2(G_N,L)->0`, or the non-vanishing residue is represented by a promoted record sector.

The next concrete receipts should test preparability by bounded local action norm, deletion stability, omitted-operator `A_2` scans, and sector-promotion stability under deletion.

### Campaign C: causal Palm-flag geometry

The Riemann/geometric branch says that the finite flag names are coordinates, not geometry. The geometric object is a rooted, interval-intrinsic, deletion-projective algebra of causal flags, together with a Palm law saying what a typical record sees from inside its causal order.

Let `R_N` be a finite committed record order. A rooted interval is a triple

$$
(x,y;J(x,y)),
\qquad
x<y,
\qquad
J(x,y)=\{z:x<z<y\}.
$$

More generally, an `m`-rooted causal flag is a finite induced suborder `F` together with a distinguished root tuple `rho` of endpoints, records, intervals, or unordered endpoint pairs. Two rooted flags are the same only up to order isomorphism preserving the root structure, including endpoint swap when the root is an unordered pair. This condition matters: endpoint orientation can leak presentation data.

For every rooted flag `(F,rho)`, define the intrinsic operator

$$
T_{F,\rho}(R_N)
$$

as the number, or normalized density, of induced embeddings of `F` into `R_N` preserving the root type. Special cases include:

- unrooted induced flags, as audited in the flag-deck receipts;
- interval-rooted flags, where non-root records lie inside `J(x,y)`;
- pair-Palm flags, where the root is an unordered pair `{x,y}`;
- overlap flags, where several rooted intervals are sampled jointly and the operator records the isomorphism type of their union and intersection pattern.

These operators are record-intrinsic. They use only the committed causal order and record count. They do not use coordinates, labels, hidden fibers, construction stages, endpoint orientation, finite-valency nearest-neighbor choices, or a background metric.

The causal Palm deck is the law of `(R_N,rho_N)` when `rho_N` is sampled uniformly from a chosen root class and observed through finite rooted interval flags. A sequence `P_N` has a causal Palm-flag limit if every bounded rooted flag observable has a limit under this root sampling. This is the causal-set analogue of local weak/Palm convergence, but order intervals and causal diamonds replace bounded graph balls.

The deletion identity

$$
\sum_{v\in R_N}
\operatorname{count}_F(R_N\setminus v)
=
(N-|F|)\operatorname{count}_F(R_N)
$$

shows why these flags form a projective record algebra. Finite sufficient covers may drift with `N`, but they drift inside a stable algebra. The law is therefore not `flag3_36` or any other finite name. The law is a controlled conflict-cover process inside the causal Palm-flag algebra.

The theorem target is:

> causal Palm-flag sufficiency: for the admissible null record law `P_N`, there exists a projective causal Palm-flag filtration `G_{N,k}` with controlled cover complexity and controlled martingale increments such that every admissible hidden refinement either has bounded projected second moment relative to `P_N`, or its residual likelihood field is represented by a promoted record sector.

This does not forbid long-distance entanglement or covariant nonlocal kernels. Palm-flag locality constrains causal-order geometry; it is not a ban on record correlations that are nonlocal in emergent spacetime.

### Campaign D: projected effective action and operator RG

The Witten/action branch says that action language is legitimate only after projection.

For any committed record filtration `G_{m,N}`, the effective likelihood is forced:

$$
L_{m,N}
=
\mathbb E_{P_N}
\left[
L_N\mid G_{m,N}
\right],
\qquad
S^{\mathrm{eff}}_{m,N}(R)
=
-\log L_{m,N}(R)+\mathrm{const}.
$$

A quadratic, bracket, interval, matching, or flag action is admissible only as an approximation or representation of this projected action. Its error is a residual likelihood/KL term, not a stylistic defect.

The RG object is the filtration

$$
G_{0,N}\subset G_{1,N}\subset \cdots \subset \sigma(R_N),
$$

generated by record-intrinsic operators: scalar compensators, interval and rooted Palm flags, overlap flags, induced suborder counts, matching/2-core sectors, pressure sectors, and committed mark/stress sectors.

The increment

$$
\Delta_{m,N}
=
\mathbb E_{P_N}
\left[
\left(L_{m+1,N}-L_{m,N}\right)^2
\right]
$$

measures relevance. Operators whose increments vanish are irrelevant. Operators with persistent increments are relevant or marginal. Operators whose omission produces large `A_2` on unresolved atoms must be promoted as record sectors or excluded by an admissibility theorem.

Deletion gives a beta defect:

$$
\beta_{m,N}
=
D_{N\to N-1}S^{\mathrm{eff}}_{m,N}
-S^{\mathrm{eff}}_{m,N-1}.
$$

The fixed point is not a finite list of sacred operators. It is a projectively stable local-operator filtration whose martingale increments are summable, compressible, or explicitly promoted.

The anomaly dictionary is:

- Ward anomaly: failure of `L_N o pi_N = E[L_tilde_N|pi_N]`;
- deletion anomaly: failure of effective action to commute with deletion;
- truncation anomaly: projected likelihood leaves the finite operator span;
- admissibility anomaly: unresolved `A_2` does not vanish or remain bounded;
- sector anomaly: record-visible likelihood residue has no committed carrier.

Sector promotion is anomaly cancellation: add the minimal record-intrinsic operator or sector that carries the residue, then recompute the projected effective action.

The safe import from quadratic-gravity thinking is finite action, bracket control, fixed-point flow, and anomaly-cancellation discipline. It is not metric curvature-squared dynamics as a fundamental rule.

### Campaign E: algebraic conflict-cover spine

The Ramanujan/generating-function branch says that the finite object is a conflict-cover theorem for projected generating polynomials.

For a committed base filtration `G`, let

$$
\overline W_R(t)
=
\frac{1}{|\pi^{-1}(R)|}
\sum_{\pi\mapsto R}
t^{s(\pi)}
$$

be the normalized hidden-fiber score polynomial. A filtration is sufficient for the whole one-parameter hidden score family iff `Wbar_R(t)` is constant on every filtration atom.

Define the polynomial conflict set

$$
E_N(G)
=
\left\{
\{R,S\}:
R,S\text{ lie in the same }G\text{-atom but }
\overline W_R(t)\ne \overline W_S(t)
\right\}.
$$

Every candidate local flag/operator `F` covers the conflicts it separates:

$$
C_F
=
\left\{
\{R,S\}\in E_N(G):F(R)\ne F(S)
\right\}.
$$

Thus a local-operator certificate is exactly a finite set-cover certificate:

$$
\bigcup_{F\in\mathcal C}C_F
=
E_N(G).
$$

Equivalently, the minimal cover number obeys the recurrence

$$
\tau(U)
=
\begin{cases}
0,&U=\varnothing,\\
1+\min_F\tau(U\setminus C_F),&U\ne\varnothing.
\end{cases}
$$

The weighted/admissible version stops when the remaining conflict mass is below tolerance:

$$
\tau_\epsilon(U)=0
\quad\text{if}\quad
\sum_{\{R,S\}\in U}P(R,S)\le \epsilon.
$$

The audited ladder gives `tau_N=0,4,3` for `N=6,7,8`, and the scoped `N=9` known-lite active-mask instance gives `tau_9=7`. The invariant is therefore not a fixed flag list. It is small conflict-cover complexity inside a deletion-covariant local algebra.

The physical sparse-pair sector remains a separate coefficient problem. Its exact object is

$$
R_N(z;D)=\sum_r \rho_{N,r}(D)z^r,
\qquad
q_{N,r}=\binom{\lfloor N/2\rfloor}{r}\rho_{N,r}^2.
$$

The right zero-free theorem is not raw root radius. Since

$$
A_N(w)=R_N(Nw)=1+\sum_{r\ge 2}a_{N,r}w^r,
\qquad
a_{N,r}=N^r\rho_{N,r},
$$

any majorant satisfying

$$
\sum_{r\ge2}|a_{N,r}|R^r<1
$$

gives a zero-free disk. But the zero-free receipt proves the converse is false. The theorem target is coefficient control, not radius alone.

### Campaign F: finite algebra and proof engine

The Euler/finite-algebra branch packages the campaign as a sequence of exact partitions of the record quotient.

Let `Omega_N=S_N` be the hidden labelled permutation space, and let

$$
\pi_N:\Omega_N\to R_N
$$

project to the unlabeled record/order class. A finite feature family `F` generates a sigma-field `G_N(F)` whose atoms are records with identical feature vectors. Predictive sufficiency for the score family is exactly constancy of the normalized fiber polynomial on `G_N(F)`-atoms.

The strongest all-`N` theorem currently available is deletion covariance of induced flags:

$$
\sum_{v\in R_N}
\operatorname{count}_F(R_N\setminus v)
=(N-|F|)\operatorname{count}_F(R_N).
$$

In normalized density form, uniform one-record deletion preserves the flag density:

$$
D_N
\left[
\frac{\operatorname{count}_F}{\binom{N}{|F|}}
\right]
=
\frac{\operatorname{count}_F}{\binom{N}{|F|}}.
$$

Thus flag densities are deletion-martingale coordinates. What remains blocked is not the local algebra but the recurrence for conflicts. If `C_N` is a chosen cover at size `N`, its lift to `N+1` leaves a residual hypergraph

$$
B_{N+1}(C_N)
=
\left\{
\{R,S\}\in E_{N+1}:
f(R)=f(S)\ \text{for every }f\in C_N
\right\}.
$$

The exact recurrence schema is

$$
\tau_{N+1}
\le
|C_N|+\tau(B_{N+1}(C_N)).
$$

This is not yet a closed theorem because deletion identities control flag counts, not the score-polynomial conflicts themselves. The next finite proof engine should enumerate rooted deletions and score-loss boundary terms for `W_R(t)`.

The next receipts are therefore:

1. `p29_rooted_deletion_score_recurrence.py`: rooted deletion/insertion recurrence for `W_R(t)`;
2. `p29_cover_transfer_matrix.py`: residual conflict hypergraphs after lifting covers across `N`;
3. `p29_full_n9_physical_minimal_cover.py`: restore matching features in the `N=9` base sector;
4. `p29_admissibility_norm_family.py`: classify structured local score families by washout, operator promotion, or sector promotion.

The final six-campaign invariant is:

> projective local algebra plus controlled drifting covers plus admissibility control on unresolved atoms.

## 63. Hostile review

### Review 1: "This only renames the old coefficient."

No. The first receipt proves the exact matching-polynomial identity and removes ambiguity about the generating object. The old coefficient is now located inside a standard finite object with a precise normalization.

### Review 2: "The reciprocal determinant solves it."

False. The naive determinant is falsified as the full finite object. It captures the first spectral shadow but misses higher coefficients by errors near one.

### Review 3: "The labelled cycle index solves it."

False. The labelled cycle sector is exact at `r=2` but overshoots the physical `r=5` coefficient by a factor

$$
56.7756815269270517
$$

at `N=12,c=0.5`.

### Review 4: "Then the problem is just large cancellation."

Too weak. A scalar cancellation factor is not a separator; staged blocks can overlap it while keeping high beta. The full sector profile is needed.

### Review 5: "The sector-profile result is only `r=5`."

Correct. This paper does not prove the all-order theorem. It identifies the first nontrivial exact finite algebra where physical and staged behavior separate after the simpler determinant/cancellation routes fail.

### Review 6: "The root-radius evidence decreases with `N`."

Correct, and that is why the paper does not claim a fixed zero-free disk. The surviving theorem must have the right scaling.

### Review 7: "Now the theorem is just root radius."

False. The ninth receipt gives a polynomial counterexample with fixed root radius and enormous coefficient stress. A radius theorem needs a Cauchy majorant or the factorial-normalized coefficient profile.

### Review 8: "Now the theorem is just sector proportions."

False. The tenth receipt scales the physical kernel. Sector proportions stay fixed while `lambda` and beta blow up. The theorem must include amplitude normalization.

### Review 9: "The `sqrt(2)` threshold is too close to the physical data."

Correct. This is not comfortable slack; it is a sharp candidate boundary. That is why the paper states it as an audited theorem target, not a proof.

### Review 10: "The `sqrt(2)` profile theorem is dead, so the whole path is dead."

False. The `sqrt(2)` shortcut is dead. The coefficient-root envelope uses the exact falling factor, and top beta remains below `0.65` through `N=22`.

### Review 11: "Top order proves everything."

False. The all-order audit shows the maximum beta sits one order below top for `N=10..18`. A full proof needs a near-top/bulk split.

### Review 12: "The finite beta ladder proves the asymptotic limit."

False. Naive tail fits are unstable and can predict supercritical limits. A real proof needs an analytic saddle, recurrence, or majorant.

### Review 13: "One-defect dominance is the right near-top theorem."

False. The near-top receipt shows the maximizer moves from `k=1` to `k=2` at `N=20`. The near-top theorem must allow a widening defect layer.

### Review 14: "Fine, then use `k=2` and beta below `0.7`."

Not as a theorem. The deep defect receipt keeps `k=2` through `N=26`, but the `k=3` gap is closing. The saddle-motion audit predicts both a `k=3` crossing and stress on the `0.7` guard near the next even size. The theorem must derive the moving saddle, not freeze it.

### Review 15: "Projection sufficiency is tautological."

It is tautological in the productive sense: it identifies the invariant sigma-field. The hard problem is not the finite identity

$$
L_N=\mathbb E[\widetilde L_N\mid \pi_N].
$$

The hard problem is constructing or bounding this `L_N` for the actual hidden refinements. The identity prevents false targets: no hidden coordinate, fiber, mark, or stage can enter the click law unless it survives this projection.

### Review 16: "Then Paper XXIX's matching polynomial was a detour."

No. It found an exact residue sector. The detour was treating a sector certificate as the law. The matching polynomial remains a candidate certificate for sparse-pair projected likelihood residue; it just no longer gets to claim principle status by itself.

### Review 17: "If hidden conditional residue is invisible, why care about it?"

Because it becomes physical the moment it is claimed to affect future records or click rates. Then it is no longer hidden conditional residue; it must be promoted to committed records, and its projected likelihood contribution must appear in `L_N`.

### Review 18: "The projected-likelihood audit is only a toy."

Correct. It is a finite quotient toy, not the physical record law. Its value is methodological: it computes the actual projected likelihood first, then asks which record sectors span it. That is the invariant-facing workflow the earlier campaigns lacked.

### Review 19: "The full record-type flag being exact is tautological."

Yes. That row is a sanity check, not a theorem. It proves the projection machinery is capable of exact reconstruction when the whole finite record atom is allowed. The hard theorem is to replace the tautological atom basis with a projective flag/action basis whose coefficients decay or compress.

### Review 20: "The known sectors failing in the toy does not prove they fail physically."

Correct. It proves only that the present basis is not projection-complete as a general principle. For the actual physical adversary one must compute its own `L_N`. But the toy already rules out the lazy answer that scalar counts, interval profiles, degree regularity, and sparse matchings are automatically sufficient.

### Review 21: "The martingale law is just conditional expectation."

Yes. That is exactly why it is the right invariant. The earlier campaigns kept trying to guess the right statistic. Conditional expectation says the predictor is forced once the committed record filtration is chosen. The nontrivial problem moves to the choice and control of the filtration.

### Review 22: "If the full atom filtration is exact, the problem is solved."

No. The full atom filtration is exact but non-predictive: it is a lookup table over records. A click law needs a projective, compressed, or summable filtration whose increments have a stable limit. Exactness at the full atom level is only the boundary condition.

### Review 23: "Known sectors being exact at `N=6` means they may be enough."

The `N=7` martingale audit rejects that shortcut. The same sector family captures only `0.670990762176797956908217` of the chi-square residue at `N=7`. Finite atom separation at one size is not a law.

### Review 24: "Flag decks reconstruct the finite toy, so flags are the law."

No. The compression audit blocks that conclusion. At `N=7`, `4`-flags capture `0.999999124863595405737241` of the exact martingale residue, but they use `1955` atoms for `1956` record classes. That is almost a lookup table.

### Review 25: "Then flags are useless."

Also false. Pure `3`-flags capture `0.911290256094027633551594` of the exact chi-square residue with `1510` atoms out of `1956`, and known+`3`-flags capture `0.996506455472859703065718`. Flags are a real reconstruction direction; they just need controlled compression.

### Review 26: "The last ambiguity is mysterious."

False in the finite audit. The only known+`4`-flag ambiguity is separated by ten explicit `5`-flag entries, while the projected likelihoods differ by `0.149973219068023567220139260846`. The residue is in the next deck layer.

### Review 27: "Just group flags by geometric summaries."

The operator-family audit rejects this in the staged/fiber toy. Relation count, height, width, interval profile, and degree moments barely move exact capture beyond known sectors: `0.671063398498379280717221` versus known `0.670990762176797956908217`.

### Review 28: "Then use a quadratic flag action."

Quadratic and cross terms help, but not enough. Known+`3`-flag cross terms reach `R^2=0.799908687294355449892666`; quadratic `4`-flags reach `R^2=0.833281991455195432757126`; neither closes the finite action gap.

### Review 29: "The greedy four-operator result proves the click law."

No. It is a finite toy theorem, not the physical law. It does prove a better target: predictive sufficiency can occur before full atom reconstruction. The missing theorem is projective stability of such a local operator filtration.

### Review 30: "The greedy result may depend on one hidden strength."

The robustness receipt weakens that objection for the audited toy. Weight bases `2`, `3`, and `5` select the same first four operators and close the exact finite likelihood gap at step 4. This is still finite evidence, not an asymptotic proof.

### Review 31: "The bases `2`, `3`, and `5` are still just a fit."

False for the finite staged/fiber family. The score-polynomial receipt proves exact equality of the normalized fiber polynomial

$$
\frac{W_R(t)}{|\pi_N^{-1}(R)|}
$$

on every known+four atom. The three bases are corollaries of a polynomial identity.

### Review 32: "Then the four flags are universal."

False. The adversarial score-family receipt targets the remaining unresolved atom and breaks the literal four-operator list. The four flags are a strong certificate for the audited natural tilts, not a universal law over all possible projected likelihoods.

### Review 33: "The targeted unresolved-atom attack is artificial."

Correct, and that is exactly its use. It separates two claims: natural coordinate-style hidden scores are captured by the four operators in this finite toy, while arbitrary spiky record laws are not. A physical theorem must therefore include regularity, admissibility, or sector promotion.

### Review 34: "The six-campaign synthesis is just analogy."

The analogies are not claims. Their common invariant is the already-proved finite identity:

$$
L_{N,G}
=
\mathbb E[L_N\mid G].
$$

The speculative part is the choice of projectively stable controlled filtration. That remains unproved.

### Review 35: "Effective action language is just decorative."

False if it means the projected action

$$
S^{\mathrm{eff}}_G(R)
=
-\log \mathbb E_P[L\mid G](R)+\text{constant}.
$$

The KL projection receipt proves the exact Pythagorean identity. Decorative action language would choose an action first; the correct rule integrates out hidden structure first.

### Review 36: "Deletion-covariant flags are still arbitrary."

Partly correct. Deletion covariance does not select the physical coefficients. But it rules out the charge that the operators are mere coordinate marks: every induced-flag count satisfies the exact projective identity

$$
\sum_{v\in R}\operatorname{count}_F(R\setminus v)
=
(N-|F|)\operatorname{count}_F(R).
$$

That is a real record-intrinsic algebraic structure.

### Review 37: "A big local flag spike should defeat the four-operator certificate."

False in the audited `N=7` toy. Amplifying `flag5_920` up to base `1000` leaves fixed-four capture essentially exact. The successful adversary is narrower: it must target the unresolved atom directly.

### Review 38: "The atom-spike attack is enough to kill the whole principle."

No. It kills the unrestricted principle, not the scoped one. The right theorem must include an admissibility condition, sector-promotion rule, or regularity condition that distinguishes smooth local hidden likelihoods from direct atom lookup.

### Review 39: "`N=8` proves the same four operators are the law."

No. At `N=8`, the fixed four still close the same-half polynomial, which is strong transfer evidence. But fresh greedy priority and minimal conflict covers drift. The invariant is not a four-name list; it is a projectively stable local conflict-cover or operator filtration.

### Review 40: "The `N=8` minimal triples solve the law."

No. They solve a finite conflict-cover problem for one projected score. They show that small local covers exist beyond `N=7`, and that no single or pair suffices there. They do not prove all-`N` stability, uniqueness, physical admissibility, or coefficient control.

### Review 41: "The cover-size ladder is too short."

Correct. `N=6,7,8` is not an asymptotic theorem. But the ladder is enough to falsify two bad simplifications at once: fixed known sectors are not enough, and fixed operator names are not the law. The surviving finite object is a small minimal conflict-cover sequence.

### Review 42: "If covers drift, projectivity is dead."

False. Receipt 40 checks `1242696` exact deletion identities with zero violations. The local flag algebra is deletion-natural; the sufficient finite covers drift inside that algebra.

### Review 43: "The washout bound is just a union bound."

It is deliberately elementary. Its value is that it names the exact admissibility fork:

$$
\mathbb E_P[(L-\mathbb E[L\mid G])^2]
\le
P(U)\sup_U L^2.
$$

Rare unresolved atoms wash out only if projected likelihood on them is controlled. If a hidden law concentrates most of `Q` on them, they must be promoted as sectors or excluded.

### Review 44: "Local hidden scores are automatically admissible."

False. Receipt 42 finds a local `flag5_920` spike at `N=8` with

$$
A_2=0.957817256204899537036401173248
$$

under the fixed-four cover. Locality is not enough. The admissibility norm and the chosen cover decide whether the residue washes out or needs promotion.

### Review 45: "`N=9` active closure proves the final law."

No. Receipt 44 closes known-lite conflict pairs, not the full physical law. It excludes matching features from the known sector and does not prove minimality. What it proves is still important: at `N=9`, exact local flags remain strongly sufficient against a large conflict landscape.

### Review 46: "`N=9` is too large for this route."

False as a blanket objection. The exact `N=9` quotient has `131526` record classes and was enumerated. The full blind cover search is not the right next move, but targeted active scans are feasible.

### Review 47: "The `N=9` exact cover proves finite local sufficiency."

Only in the scoped known-lite problem. Receipt 45 proves that no active local cover of size at most `6` closes the known-lite conflict universe, and that a cover of size `7` does. It does not include matching features in the base sector, does not prove the full physical likelihood, and does not prove projective stability.

### Review 48: "Small unresolved mass guarantees washout."

False. Receipt 46 gives the exact limiting formula

$$
\frac{1}{P(x)}-\frac{1}{P(A)}
$$

for a spike inside an unresolved atom `A`. Small `P(A)` can make the adversary worse, not better, if `L` is unbounded there. Washout needs likelihood control, not just small mass.

### Review 49: "Locality is the admissibility condition."

False. Receipt 47 finds omitted local flags that are highly relevant. Under the first `N=8` minimal triple, the ordinary local score `flags5:flag5_926` puts

$$
Q(U)=0.990490350856278364341481
$$

on the unresolved sector and has residual

$$
18956.9690726015044985623.
$$

Locality is necessary for a record-intrinsic law, but it is not sufficient.

### Review 50: "These adversaries are not real hidden refinements."

False in the projection sense. Receipt 48 constructs fiber-constant hidden lifts for hostile projected laws with zero vertical residue. Projection removes hidden presentation dependence; it does not restrict the projected likelihood itself. The missing axiom must therefore be a physical admissibility rule on record-visible likelihoods.

### Review 51: "Record covariance is empty."

It would be empty if stated as "all descriptions are allowed." The nonempty content is the specified projection groupoid: hidden presentations are equivalent only when they induce the same projected likelihood on every committed record coarsening. Record covariance must be paired with the committed sigma-field and the admissibility norm.

### Review 52: "Causal Palm-flags are just more flags."

No. A finite flag name is a coordinate. A causal Palm-flag is a rooted, endpoint-symmetric, interval-intrinsic observable inside a deletion-projective algebra. The law-level object is the controlled filtration generated by that algebra, not any fixed name like `flag3_36`.

### Review 53: "Palm locality forbids long-distance entanglement."

False. Palm-flag locality constrains causal-order geometry. It does not forbid record correlations, no-signaling entanglement, or covariant nonlocal kernels. The separation is between geometric support of the record law and correlation structure carried by admitted sectors.

### Review 54: "Effective action language solves the law."

Only after projection. The action is

$$
S^{\mathrm{eff}}_{m,N}(R)
=
-\log \mathbb E[L_N\mid G_{m,N}](R)+\mathrm{const}.
$$

Choosing a quadratic or bracket action first is an ansatz. The theorem must control the residual between that ansatz and the projected effective action.

### Review 55: "The conflict-cover recurrence proves asymptotic bounded cover size."

No. It gives an exact finite proof engine:

$$
\tau(U)=1+\min_F\tau(U\setminus C_F).
$$

The missing theorem is a closed bound or recurrence for the conflict hypergraphs themselves. Deletion covariance controls flag counts, not yet score-polynomial conflicts.

### Review 56: "Preparability is hand-waving."

It is hand-waving until it becomes a norm or stability condition. The finite candidates are bounded local action complexity, deletion stability, bounded `A_2` on unresolved atoms, and stable sector promotion. The paper does not yet prove that any one of these is the physical admissibility axiom.

### Review 57: "Bounded local coefficient size is the admissibility theorem."

False. Receipt 49 uses the bounded local score `flags5:flag5_926` with coefficient `log 2`, yet under the first `N=8` minimal triple it gives

$$
A_2=37913.9382173321428162582099805815254,
$$

and puts

$$
Q(U)=0.990490350856278364341481440869474689
$$

on the unresolved sector. Bounded coefficient size is not enough. The receipt also shows the repair: promoting that exact local separator makes the residual zero.

### Review 58: "Palm-flag geometry already proves sufficiency."

False. Receipt 50 gives real movement but not closure. At `N=7`, known sectors have

$$
R^2=0.704097056696214224579348,
$$

while known sectors plus endpoint-symmetric pair-Palm `3`-flags, `4`-flags, and interval-overlap flags reach only

$$
R^2=0.785725278312020578000384.
$$

The Palm-rooted operators are a credible intrinsic carrier. They are not yet a sufficiency theorem.

### Review 59: "The `N=9` known-lite witness proves the stable recurrence."

No. Receipt 51 shows that the scoped `N=9` known-lite witness transfers down for the audited same-half score, but that success is not a comparable physical all-`N` theorem. Known-lite excludes matching features, and downward transfer of one witness does not prove a deletion/insertion recurrence for score-polynomial conflicts.

### Review 60: "The recurrence should preserve fixed operator names."

False. Receipt 51 confirms the asymmetry already seen in the deletion-flow audit: the `N=7` fixed four close the audited `N=8` conflicts, while the first `N=8` minimal triple leaves `23` polynomial-bad atoms at `N=7`. The invariant is residual conflict-hypergraph transfer, not a fixed list of flag names.

### Review 61: "The three targets are independent."

Only as work packages. Mathematically they are coupled. Admissibility without Palm-flags has no intrinsic local carrier; Palm-flags without admissibility are beaten by spikes; finite covers without a deletion/insertion recurrence remain finite certificates. The proof target is the coupled triangle, not any one corner alone.

### Review 62: "Markov bases reintroduce physical Markov dynamics."

They would if interpreted ontically. Receipt 52 rejects that interpretation: adjacent same-fiber presentation swaps leave `1808` disconnected fibers, so naive hidden rewrites are not the physical dynamics. The compatible use is algebraic-statistical: fiber moves and binomial conflicts are proof certificates inside one committed record fiber.

### Review 63: "The incidence/Hopf language is decorative."

Not if it is tied to the score-boundary recurrence. Receipt 52 verifies the finite rooted deletion identity

$$
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b}
$$

with `0` recurrence errors at `N=6`. The danger is not decoration; the danger is mistaking decomposition bookkeeping for stochastic divisibility.

### Review 64: "Projected Gibbs language says hidden locality is enough."

False. The finite quasilocality test says the opposite. Same-half likelihood is quasilocal relative to known+four in the audited toy, but an atom spike inside the same unresolved sector has oscillation `2012.73903666427030913012221423`. Projection can create nonquasilocal record likelihoods.

### Review 65: "WL/coherent configurations solve sufficiency."

Not yet. The WL-style/flag refinement ladder is real: bad atoms decrease `466 -> 22 -> 1`. But bounded-depth refinement is not physical equivalence if `W_R` still differs. It is a compression candidate, not a law.

### Review 66: "Flag algebra or poset limits solve the continuum problem."

No. The receipt confirms deletion-projective induced flag densities, but a flag limit is not automatically manifoldlike and not automatically sufficient for likelihood. The physical version must be causal, rooted, endpoint-symmetric, admissible, and non-lookup.

### Review 67: "This is secretly modular forms."

No. There is no upper half-plane, modular group, congruence subgroup, Hecke algebra, or modular `q`-expansion in the current object. The useful analogy is hostile: finite q-polynomial-looking certificates are not enough without stable Hecke-like operator recurrence. Receipt 52 shows fixed-four and `N=8` triple covers do not behave like a fixed stable basis.

### Review 68: "Tutte universality gives the law."

No. The full vertex-deletion deck separates all `1956` audited `N=7` records, so it is too reconstructive to be a controlled law. Coarse known/Tutte-like sectors remain too weak, with `466` bad atoms. The compatible target is a record-deletion universal invariant with compression, not ordinary graph/matroid Tutte universality.

### Review 69: "The full boundary tensor is the theorem."

False. Receipt 53 shows the full normalized boundary tensor `Bbar` is exact, but too reconstructive: the number of unique `Bbar` signatures equals the number of record classes at `N=6,7,8`. The theorem must target a compressed boundary, not the full child-record tensor.

### Review 70: "The compressed boundary histogram is optional."

No. `Hbar_R(a,b)` reconstructs `Wbar_R` exactly and is the first non-lookup deletion-transfer object. Known sectors do not determine it: at `N=7`, they leave `469` `Hbar`-bad atoms; at `N=8`, they leave `4616`.

### Review 71: "The finite `Wbar` covers are enough for boundary transfer."

False. Receipt 55 shows that at `N=8`, the `Wbar` `N=7` fixed four leave `14` `Hbar` conflicts, and the `Wbar` `N=8` triple leaves `62`. Closing the score polynomial is not the same as closing the deletion boundary needed for transfer.

### Review 72: "The compressed boundary gives fixed operators."

False. Receipt 55 shows `Hbar` covers drift. The `N=7` `Hbar` cover leaves `10` conflicts at `N=8`, although the `N=8` `Hbar` cover closes both audited sizes in the downward direction. The theorem must control cover drift, not preserve names.

## 64. Claims and nonclaims

**Claim.** The exact generating object is the normalized signed matching polynomial `R_N(z;D)`.

**Claim.** The coefficient `q_{N,r}` is the binomial Hadamard-square transform of the matching coefficient `rho_{N,r}`.

**Claim.** The naive reciprocal determinant `det(I+2zD/N)^(-1)` is falsified as the full finite generating object.

**Claim.** The labelled cycle-index term is exact at `r=2` but not sufficient at `r>=4`.

**Claim.** The exact finite object through `r=5` is a signed 2-core sector sum by quotient vertex count.

**Claim.** Physical smallness at `r=5` comes from strong signed sector cancellation.

**Claim.** Scalar cancellation factor is not sufficient.

**Claim.** The audited sector-profile quantities, especially top-sector share and absolute-sector centroid, separate physical rows from staged blocks.

**Claim.** Same-`N` scaled root radii separate audited physical rows from staged blocks.

**Claim.** The exact coefficient-root bridge is

$$
N q_{N,r}^{1/r}
=
\lambda_{N,r}^2
\frac{((N/2)_r)^{1/r}}{N}.
$$

**Claim.** The original all-order audited physical grid through `N=18` satisfies `max lambda = 1.39792118738412459 < sqrt(2)`.

**Claim.** A uniform `lambda_{N,r}<sqrt(2)` profile envelope would imply a conservative beta-one coefficient-root envelope.

**Claim.** The deeper top-order ladder falsifies that conservative `sqrt(2)` envelope as an all-`N` theorem: top order crosses at `N=20`.

**Claim.** The coefficient-root envelope itself is not falsified by that crossing; top beta remains below `0.65` through `N=22`.

**Claim.** Naive top-beta tail fits are unstable and cannot prove subcriticality.

**Claim.** Top order alone is not an exact dominance theorem for all orders.

**Claim.** Fixed one-defect dominance is false; the best audited near-top layer moves to `k=2` at `N=20`.

**Claim.** The audited near-top beta profile remains below `0.65` through `N=22`.

**Claim.** The old `0.65` working guard is falsified at `N=26,k=2`, where beta is `0.676614267360108067757209`.

**Claim.** The `N=26` deep near-top peak remains below `0.7`, but the `0.7` guard is not established as a theorem.

**Claim.** Fixed `k=2` is not secure as an asymptotic theorem; the `k=3` gap is closing.

**Claim.** The invariant behind the campaign is projection sufficiency: the click law can depend only on the likelihood residue that survives projection to committed records.

**Claim.** For any hidden lift, the record likelihood is the conditional expectation of the hidden likelihood on the committed record sigma-field:

$$
L_N\circ\pi_N
=
\mathbb E_{\widetilde P_N}
\left[
\widetilde L_N\mid \pi_N
\right].
$$

**Claim.** The hidden second moment splits into record-visible residue plus hidden conditional residue:

$$
\mathbb E_{\widetilde P_N}
\left[
\widetilde L_N^2
\right]
=
\mathbb E_{P_N}
\left[
L_N^2
\right]
+
\mathbb E_{\widetilde P_N}
\left[
\eta_N^2
\right].
$$

**Claim.** The matching/root sector is a diagnostic or certificate for one projected likelihood sector, not the general click-law principle.

**Claim.** In the finite staged/fiber projected-likelihood toy, the known scalar/interval/regularity/matching basis does not span `log L_N`; the audited `N=7` known-sector `R^2` is `0.704097056696214224579348`.

**Claim.** Induced-suborder flag profiles improve the projected-likelihood reconstruction in the same toy; at `N=7`, adding `3`-, `4`-, and `5`-flags raises `R^2` to `0.841428360108242087515858`.

**Claim.** The full record-type flag reconstructs `log L_N` exactly in the finite toy, tautologically.

**Claim.** For every finite sector sigma-field `G`, the optimal predictive law is the conditional likelihood martingale:

$$
L_{N,G}
=
\mathbb E_{P_N}[L_N\mid G].
$$

**Claim.** Sector refinement gives monotone captured second moment:

$$
G_1\subseteq G_2
\implies
S_{N,G_1}\le S_{N,G_2}.
$$

**Claim.** The exact residual identity is

$$
\mathbb E_{P_N}[(L_N-L_{N,G})^2]
=
S_N-S_{N,G}.
$$

**Claim.** In the staged/fiber toy, known sectors are not stably complete: they capture all chi-square residue at `N=6`, but only `0.670990762176797956908217` at `N=7`.

**Claim.** In the same toy, induced flags repair most of the `N=7` residue: `3`-flags capture `0.996506455472859703065718`, `4`-flags capture `0.999999124863595405737241`, and `5`-flags capture all finite residue.

**Claim.** In the staged/fiber toy, pure induced decks reconstruct the audited quotients at one-below-top size: `4`-decks reconstruct the `N=6` quotient and `5`-decks reconstruct the `N=7` quotient.

**Claim.** At `N=7`, pure `4`-decks and known+`4`-decks leave exactly one two-record ambiguity, with residual `0.00000446269175349710073261141643892`.

**Claim.** The remaining `N=7` known+`4` ambiguity is separated by ten explicit `5`-flag entries.

**Claim.** Finite deck exactness is not enough to be a predictive law: at `N=7`, known+`5`-flags exactly reconstruct the martingale but the corresponding weighted linear/action projection has only `R^2=0.841428360108242087515858`.

**Claim.** Coarse geometric flag families are not enough in the staged/fiber toy: known+relation/height/width/interval/degree grouped flags capture only `0.671063398498379280717221`.

**Claim.** Low-order operator products improve the action but do not close it: known+`3`-flag quadratic/cross terms reach `R^2=0.800037784431876780553483`, and quadratic `4`-flags reach `R^2=0.833281991455195432757126`.

**Claim.** In the staged/fiber toy at `N=7`, greedy exact local-flag selection closes the projected likelihood gap after four operators while still leaving one two-record atom unresolved.

**Claim.** The same four greedy operators close the exact finite likelihood gap for weight bases `2`, `3`, and `5`.

**Claim.** In the staged/fiber toy at `N=7`, known sectors plus the four greedy operators make the normalized score polynomial `W_R(t)/|fiber(R)|` constant on every remaining sector atom.

**Claim.** In that same score-polynomial certificate, removing any one of the four greedy operators creates polynomial-violating atoms.

**Claim.** The fixed four operators survive the audited natural coordinate-score tilts: diagonal band, anti-diagonal band, parity match, lower-left block, and central square.

**Claim.** The fixed four operators are not universal over all projected laws: a targeted score on the single unresolved atom breaks them.

**Claim.** A fresh four-flag greedy repair closes all audited score polynomials, including the targeted unresolved-atom law.

**Claim.** The invisible local-flag nullspace after known sectors plus the four greedy operators is concentrated on the single unresolved two-record atom at `N=7`.

**Claim.** That unresolved atom has null mass `0.000793650793650793650793650793651` and is separated by ordinary local flags, including `flag5_920`, `flag5_664`, `flag5_17304`, and `flag4_200`.

**Claim.** The finite projection Ward tower is exact: hidden likelihood projects to record likelihood by conditional expectation, and record likelihood projects to coarse likelihood by the tower law.

**Claim.** Vertical hidden perturbations can change hidden second moment without changing record or coarse likelihood; in the finite tower receipt, record, coarse, Ward, and tower gaps are all exactly zero.

**Claim.** The projected effective action satisfies the exact KL Pythagorean identity

$$
D(Q\|P)
=
D(Q\|Q_G)
+
D(Q_G\|P).
$$

**Claim.** In the `N=7` staged/fiber toy, known sectors leave residual KL `0.189619228902405465576048805567016212`, while known+four has residual KL `0.0`.

**Claim.** Induced flag counts are deletion-covariant record operators: all `46072` audited `3`-, `4`-, and `5`-flag deletion identities at `N=7` hold exactly.

**Claim.** In the `N=7` staged/fiber toy, known+four determines the multivariate projected partition function for six natural hidden scores simultaneously.

**Claim.** Adding a deliberately targeted atom coordinate to those natural scores breaks exactly one known+four atom.

**Claim.** The same-half score polynomial has an exact conditional rook/hit expansion, and known+four determines the full hit vector at `N=7`.

**Claim.** Amplifying the ordinary local separator `flag5_920` does not defeat known+four in the audited range; at base `1000`, fixed-four capture is `0.999999999999999999999999`.

**Claim.** Directly amplifying one record inside the unresolved atom defeats known+four: fixed-four capture stays `0.499801508535132989281461`, while adding `flag4_14` repairs the target exactly.

**Claim.** The targeted atom-spike second moment can grow very large in the finite toy; at base `10000`, `S_full=1607.94874723561810778027175831485244`.

**Claim.** At `N=8`, the fixed four operators still determine the same-half projected polynomial and close the base-3 likelihood: fixed-four capture is `1.0`.

**Claim.** At `N=8`, the unresolved fixed-four nullspace grows to `35` atoms, maximum atom size `4`, unresolved mass `0.00381944444444444444444444444444444444`, and `74` invisible local flags.

**Claim.** At `N=8`, fresh greedy priority is not the same as the `N=7` four-name list; the first three greedy operators are `flags4:flag4_2062`, `flags4:flag4_2176`, and `flags5:flag5_16904`.

**Claim.** At `N=8`, no single local flag and no pair of local flags repairs all known-sector same-half polynomial conflicts; triples suffice, with six sufficient triples listed in the audit.

**Claim.** The first listed `N=8` sufficient triple is

$$
\{\texttt{flags4:flag4\_192},
\texttt{flags4:flag4\_2248},
\texttt{flags5:flag5\_16904}\}.
$$

**Claim.** The exact minimal conflict-cover ladder for the audited same-half score is `0,4,3` for `N=6,7,8`.

**Claim.** At `N=7`, the first listed minimal cover is the known four-operator certificate and leaves unresolved mass `0.000793650793650793650793650793650793651`.

**Claim.** At `N=8`, the first listed minimal triple leaves unresolved mass `0.00887896825396825396825396825396825397`.

**Claim.** The local flag algebra is exactly deletion-natural from `N=8` to `N=7`: `1242696` audited deletion identities have zero violations.

**Claim.** The first `N=8` minimal triple is not sufficient at `N=7`: it leaves `23` polynomial-bad atoms and unresolved mass `0.015873015873015873015873015873015873`.

**Claim.** For any committed filtration `G`, the finite predictive miss is exactly

$$
\mathbb E_P[(L-\mathbb E[L\mid G])^2]
=
\sum_{A\in G}P(A)\operatorname{Var}_P(L\mid A).
$$

**Claim.** If all non-singleton `G`-atoms lie in `U`, then

$$
\mathbb E_P[(L-\mathbb E[L\mid G])^2]
\le
\mathbb E_P[L^2\mathbf 1_U]
\le
P(U)\sup_U L^2.
$$

**Claim.** In the audited `N=7` known+four filtration, local `flag5_920` amplification at base `1000` has residual `5.03982851249832520279889378734e-21`.

**Claim.** In the audited `N=7` known+four filtration, direct unresolved-atom targeting at base `10000` has residual `803.793339228614059469290359459` and puts `Q(U)=0.798865724099368959182043294193` on the unresolved atom.

**Claim.** The finite admissibility norm

$$
A_2(G,L)=\mathbb E_P[L^2\mathbf 1_U]
$$

separates washout, operator promotion, and sector promotion in the audited cases.

**Claim.** Locality alone is not admissibility: for the `N=8` fixed-four cover, a local `flag5_920` spike at base `2` has `A_2=0.957817256204899537036401173248`.

**Claim.** Promoting a relevant separator can wash out residue: for the first `N=8` minimal triple, the audited local `flag5_16904` spike has residual zero at bases `2` and `10`.

**Claim.** The exact `N=9` permutation-order quotient has `362880` permutations and `131526` unlabeled record classes.

**Claim.** The `N=9` known-lite sector partition has `47851/131526` atoms, `25793` score-polynomial-bad atoms, bad mass `0.634124228395061728395061728395061728`, and `87066` conflict pairs.

**Claim.** In the deterministic `N=9` flag sample, `3`- and `4`-flags already show their full universes of `5` and `16` types, and `5`-flags show `58` types.

**Claim.** The `N=9` active scan over known-lite conflict pairs sees all `84` audited induced `3`-, `4`-, and `5`-flag types as active.

**Claim.** At `N=9`, the top active flag `flags4:flag4_192` separates `80066/87066` known-lite conflict pairs.

**Claim.** At `N=9`, a greedy active local-flag cover closes all known-lite conflict pairs in eight steps.

**Claim.** At `N=9`, the exact known-lite active-mask cover number is `7`: no active local cover of size at most `6` closes the `87066` conflict pairs, and the first size-`7` witness found is

$$
\{\texttt{flags3:flag3\_36},
\texttt{flags5:flag5\_16904},
\texttt{flags5:flag5\_25104},
\texttt{flags5:flag5\_8704},
\texttt{flags4:flag4\_14},
\texttt{flags4:flag4\_2248},
\texttt{flags5:flag5\_25488}\}.
$$

**Claim.** For a spike concentrating inside a non-singleton filtration atom `A` at target record `x`, the limiting projected residual is exactly

$$
\frac{1}{P(x)}-\frac{1}{P(A)}.
$$

**Claim.** The worst audited unresolved-atom residual limits are `1260` for `N=7` fixed four, `15120` for `N=8` fixed four, and `20160` for the first `N=8` minimal triple.

**Claim.** Omitted local flags can be highly relevant: under the first `N=8` minimal triple, `flags5:flag5_926` has residual `18956.9690726015044985623`, `A_2=37913.9382173321428162582`, and `Q(U)=0.990490350856278364341481`.

**Claim.** Any dominated projected law `Q << P`, including the hostile atom-spike and local-flag spike examples, has a fiber-constant hidden lift with zero vertical residue.

**Claim.** Record covariance has nonempty content only after specifying the committed record sigma-field, the projection maps, and the admissible projected likelihood class.

**Claim.** Two hidden presentations are physically equivalent only when they induce the same projected record likelihood on every committed coarsening/deletion.

**Claim.** The causal Palm-flag proposal is a rooted, endpoint-symmetric, interval-intrinsic, deletion-projective local algebra; individual flag names are coordinates in that algebra, not physical operators by themselves.

**Claim.** For an induced flag `F`, the deletion identity

$$
\sum_{v\in R_N}
\operatorname{count}_F(R_N\setminus v)
=(N-|F|)\operatorname{count}_F(R_N)
$$

makes normalized flag densities deletion-martingale coordinates.

**Claim.** The projected effective action for a committed filtration `G_{m,N}` is forced by

$$
S^{\mathrm{eff}}_{m,N}(R)
=
-\log \mathbb E[L_N\mid G_{m,N}](R)+\mathrm{const}.
$$

**Claim.** Operator relevance is filtration-relative and can be measured by nonvanishing likelihood increments

$$
\Delta_{m,N}
=
\mathbb E[(L_{m+1,N}-L_{m,N})^2],
$$

or by KL increments or unresolved `A_2` mass.

**Claim.** For a normalized hidden-fiber score polynomial `Wbar_R(t)`, a finite filtration is sufficient for that score family iff `Wbar_R(t)` is constant on every filtration atom.

**Claim.** The local-operator certificate for a projected score polynomial is exactly a finite set-cover problem over conflict pairs:

$$
E_N(G)
=
\{\{R,S\}:R,S\text{ lie in the same }G\text{-atom but }\overline W_R\ne\overline W_S\},
$$

with operator masks

$$
C_F
=
\{\{R,S\}\in E_N(G):F(R)\ne F(S)\}.
$$

**Claim.** The exact minimal-cover recurrence is

$$
\tau(U)
=
\begin{cases}
0,&U=\varnothing,\\
1+\min_F\tau(U\setminus C_F),&U\ne\varnothing.
\end{cases}
$$

**Claim.** The current finite-algebra invariant is projective local algebra plus controlled drifting covers plus admissibility control on unresolved atoms.

**Claim.** Receipt 49 falsifies bounded local coefficient size as an admissibility principle: `flags5:flag5_926` has coefficient `log 2` but residual `18956.9690726015044985622758129513822`, `A_2=37913.9382173321428162582099805815254`, and `Q(U)=0.990490350856278364341481440869474689` under the first `N=8` minimal triple.

**Claim.** Receipt 49 shows the finite repair mechanism: promoting the omitted local separator `flags5:flag5_926` makes that local-flag residual exactly zero.

**Claim.** Receipt 49 repeats the atom-spike theorem in the same filtration: a two-record atom with target record `212072348056830` has exact limiting residual `20160`, while full atom promotion makes the residual zero.

**Claim.** Receipt 50 constructs endpoint-symmetric pair-Palm and interval-overlap operators: `11` pair-rooted `3`-flags, `66` pair-rooted `4`-flags, and `22` interval-overlap flags.

**Claim.** Receipt 50 shows that causal Palm-flag operators are informative but incomplete in the audited `N=7` toy: known sectors have `R^2=0.704097056696214224579348`, while known plus pair-Palm and overlap flags reach `R^2=0.785725278312020578000384`.

**Claim.** Receipt 51 gives an exact cover-transfer matrix for the audited score: the `N=7` fixed four close `N=8` conflicts, the first `N=8` minimal triple leaves `23` polynomial-bad atoms at `N=7`, and the union closes both audited levels.

**Claim.** Receipt 51 shows that the scoped `N=9` known-lite witness transfers down for the audited score, but this is not a comparable physical recurrence because the base sector is known-lite.

**Claim.** The sharpened finite recurrence target is a rooted deletion/insertion score-boundary tensor, for example

$$
B_N^\downarrow(R,A;a,b)
=
\#\{(\pi,i):
\rho_N(\pi)=R,\,
\rho_{N-1}(d_i\pi)=A,\,
s_{N-1}(d_i\pi)=a,\,
\Delta_i^-(\pi)=b
\},
$$

which would imply the exact score-polynomial transfer

$$
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b}.
$$

**Claim.** The three theorem targets are coupled: admissibility needs an intrinsic carrier, Palm-flags need admissibility against spikes, and conflict covers need deletion/insertion score-boundary control.

**Claim.** Receipt 52 is compatible with Barandes/Shard indivisibility: Markov-basis and hidden-fiber moves are proof/gauge certificates inside a committed record fiber, not physical Markov dynamics.

**Claim.** Receipt 52 shows naive adjacent same-fiber hidden rewrites are not a physical Markov basis: there are `1808` disconnected same-record fibers under those moves.

**Claim.** Receipt 52 verifies an incidence/decomposition recurrence at finite size: the rooted deletion score-boundary recurrence reconstructs `N W_R` with `0` errors and `8` boundary types at `N=6`.

**Claim.** Receipt 52 gives a finite quasilocality split: the same-half law has `0` known+four bad atoms, while an atom spike in the same filtration has likelihood oscillation `2012.73903666427030913012221423`.

**Claim.** Receipt 52 supports WL/coherent-configuration refinement as a compression candidate: score-polynomial bad atoms decrease `466 -> 22 -> 1` under known sectors, known+`3`-flags, and known+`3,4`-flags.

**Claim.** Receipt 52 confirms induced flag densities as deletion-projective coordinates: the audited `3`-flag deletion identity has `0` violations.

**Claim.** Receipt 52 scopes the modular analogy: finite q-polynomial-looking certificates do not yet form a Hecke-like stable basis, since the first `N=8` triple closes `N=8` but leaves `23` bad atoms at `N=7`.

**Claim.** Receipt 52 scopes the Tutte analogy: the full vertex-deletion deck separates all `1956` audited `N=7` records, so it is too reconstructive to be the controlled law, while coarse known/Tutte-like sectors still leave `466` bad atoms.

**Claim.** The best external mathematical route is algebraic statistics plus incidence/decomposition algebra plus projected quasilocality; modular/noncongruence and Tutte universality are currently hostile analogies, not literal structures.

**Claim.** Receipt 53 verifies the rooted deletion score-boundary recurrence exactly for `N=6,7,8`: raw boundary reconstruction, insertion/deletion mass consistency, and compressed histogram reconstruction all have zero errors.

**Claim.** The full normalized boundary tensor `Bbar` is too reconstructive in the audited toy: unique `Bbar` signatures equal record classes at `N=6,7,8`.

**Claim.** The compressed boundary histogram `Hbar_R(a,b)` reconstructs the normalized score polynomial `Wbar_R` exactly while being much smaller than full `Bbar`: at `N=7`, unique `Wbar=12`, unique `Hbar=70`, unique `Bbar=1956`.

**Claim.** Known sectors do not determine `Hbar`: Receipt 53 finds `469` `Hbar`-bad known atoms at `N=7` and Receipt 54 finds `4616` at `N=8`.

**Claim.** Ordinary local flags refine `Hbar` uncertainty: at `N=7`, `Hbar`-bad atoms decrease `469 -> 27 -> 1` under known, known+`3`-flags, and known+`3,4`-flags.

**Claim.** Receipt 54 finds exact local covers for compressed `Hbar`: size `4` at `N=7` and size `5` at `N=8`.

**Claim.** The `N=7` `Hbar` cover is

$$
\{
\texttt{flags3:flag3\_36},
\texttt{flags4:flag4\_2062},
\texttt{flags4:flag4\_192},
\texttt{flags5:flag5\_525184}
\}.
$$

**Claim.** The `N=8` `Hbar` cover is

$$
\{
\texttt{flags3:flag3\_36},
\texttt{flags5:flag5\_549376},
\texttt{flags4:flag4\_2176},
\texttt{flags4:flag4\_206},
\texttt{flags5:flag5\_24576}
\}.
$$

**Claim.** Receipt 55 shows `Wbar` covers do not suffice for `Hbar` transfer: at `N=8`, the `Wbar` `N=7` fixed four leave `14` `Hbar` conflicts, and the `Wbar` `N=8` triple leaves `62`.

**Claim.** Receipt 55 shows compressed-boundary covers drift: the `N=7` `Hbar` cover leaves `10` `Hbar` conflicts at `N=8`, while the union of `N=7` and `N=8` `Hbar` covers closes both audited levels.

**Claim.** The recurrence-campaign target is now sharper: prove controlled drift of compressed boundary covers for `Hbar`, not fixed-name stability and not full-boundary reconstruction.

**Claim.** Zero-free radius alone is insufficient.

**Claim.** Sector shape alone is insufficient.

**Nonclaim.** This paper does not prove the all-`N`, all-`r` coefficient-root envelope.

**Nonclaim.** This paper does not prove a uniform sector-profile theorem.

**Nonclaim.** This paper disproves the all-`N` `sqrt(2)` profile envelope; it does not disprove the coefficient-root envelope.

**Nonclaim.** This paper does not prove the asymptotic top-order beta limit.

**Nonclaim.** This paper does not prove the near-top/bulk split.

**Nonclaim.** This paper does not prove the scaling law for the widening near-top defect layer.

**Nonclaim.** This paper does not prove any fixed numerical beta guard such as `0.65` or `0.7`.

**Nonclaim.** This paper does not prove that the audited `r=5` sector signature is the unique possible law.

**Nonclaim.** This paper does not prove quotient safety for unlabeled orders.

**Nonclaim.** This paper does not construct the full record law `P_N`.

**Nonclaim.** This paper does not prove that the matching/root sector is a complete representation of `L_N` for all hidden refinements.

**Nonclaim.** This paper does not prove that finite induced flags are the final click law.

**Nonclaim.** This paper does not prove coefficient decay, compression, or asymptotic closure for the flag-algebra expansion of `log L_N`.

**Nonclaim.** This paper does not prove that the induced-flag filtration is the final physical filtration.

**Nonclaim.** This paper does not prove an asymptotic reconstruction theorem from bounded-size flags.

**Nonclaim.** This paper does not prove that one-below-top decks reconstruct all large record orders.

**Nonclaim.** This paper does not prove a compressed flag action, coefficient decay, or renormalized flag expansion.

**Nonclaim.** This paper does not prove that the four greedy finite operators are universal.

**Nonclaim.** This paper does not prove that survival under natural coordinate tilts implies survival under all admissible hidden refinements.

**Nonclaim.** This paper does not prove the physical regularity or admissibility condition that would rule out spiky rare-atom tilts.

**Nonclaim.** This paper does not prove that the rare unresolved nullspace shrinks at larger `N`.

**Nonclaim.** This paper does not prove projective stability of the greedy operator filtration as `N` grows.

**Nonclaim.** This paper does not prove that the staged/fiber toy is representative of the physical hidden-refinement likelihood.

**Nonclaim.** This paper does not prove that the four named operators are canonical physical operators.

**Nonclaim.** This paper does not prove that the `N=8` minimal triples are unique, stable, or physical.

**Nonclaim.** This paper does not prove a general admissibility rule excluding direct atom-spike likelihoods.

**Nonclaim.** This paper does not prove all-`N` convergence of the local conflict-cover size.

**Nonclaim.** This paper does not prove coefficient decay or a complete effective action over the causal Palm-flag algebra.

**Nonclaim.** This paper does not prove that the audited `0,4,3` cover-size ladder persists beyond `N=8`.

**Nonclaim.** This paper does not prove that upward transfer of the `N=7` fixed four continues beyond `N=8`.

**Nonclaim.** This paper does not prove a quantitative physical bound on `P(U)\sup_U L^2`; it identifies the finite bound that such an admissibility theorem must control.

**Nonclaim.** This paper does not prove that every local hidden score is admissible.

**Nonclaim.** This paper does not prove a full `N=9` physical minimal cover theorem.

**Nonclaim.** The `N=9` exact cover theorem is minimal only for the known-lite active-mask instance audited in Receipt 45.

**Nonclaim.** The `N=9` known-lite audit excludes matching features from the base known sector; it is a staged feasibility result, not the final `N=9` known-sector theorem.

**Nonclaim.** This paper does not prove that locality alone is an admissibility condition.

**Nonclaim.** This paper does not prove that projection alone excludes hostile laws; hostile projected laws can have fiber-constant hidden lifts.

**Nonclaim.** This paper does not prove a physical upper bound on `A_2(G,L)` or on unresolved-atom spike likelihoods.

**Nonclaim.** This paper does not prove existence or uniqueness of a causal Palm-flag limit for the physical record law.

**Nonclaim.** This paper does not prove that the causal Palm-flag filtration is asymptotically sufficient.

**Nonclaim.** This paper does not prove that Palm-flag locality constrains or forbids entanglement-like long-distance record correlations.

**Nonclaim.** This paper does not prove deletion beta functions vanish or converge for the projected effective action.

**Nonclaim.** This paper does not prove increment summability for the operator filtration.

**Nonclaim.** This paper does not prove a physical preparability norm; it identifies bounded local action complexity, deletion stability, and unresolved `A_2` control as concrete candidates.

**Nonclaim.** This paper does not prove bounded local coefficient size is an admissibility condition; Receipt 49 falsifies that candidate in the audited toy.

**Nonclaim.** This paper does not prove that the causal Palm-flag operator family audited in Receipt 50 is sufficient.

**Nonclaim.** This paper does not prove that pair-Palm and interval-overlap flags exhaust the causal Palm-flag algebra.

**Nonclaim.** This paper does not prove a closed all-`N` recurrence for the conflict hypergraphs `E_N(G)`.

**Nonclaim.** This paper does not prove bounded all-`N` conflict-cover complexity.

**Nonclaim.** This paper does not prove the full `N=9` cover with matching features restored.

**Nonclaim.** This paper does not prove that the `N=9` known-lite witness is a stable physical all-`N` cover.

**Nonclaim.** This paper does not prove the rooted deletion/insertion score-boundary tensor theorem.

**Nonclaim.** This paper does not use Markov bases as physical Markov dynamics; that interpretation is incompatible with the indivisible-record reading.

**Nonclaim.** This paper does not construct a full algebraic-statistical toric model or a complete Markov basis for the physical record law.

**Nonclaim.** This paper does not prove an incidence Hopf algebra, decomposition space, or antipode theorem for the full record law; it verifies only finite deletion/decomposition shadows.

**Nonclaim.** This paper does not prove a Gibbs or quasilocal specification for the physical projected record law.

**Nonclaim.** This paper does not prove that bounded-depth Weisfeiler-Leman or coherent-configuration refinement is sufficient for the physical likelihood.

**Nonclaim.** This paper does not prove a flag-algebra/poset-limit theorem for manifoldlikeness or click-law sufficiency.

**Nonclaim.** This paper does not construct modular forms, a modular group action, a Hecke algebra, or congruence/noncongruence subgroup structure for `W_R(t)` or `R_N(z;D)`.

**Nonclaim.** This paper does not prove ordinary Tutte universality; the full deletion deck is too reconstructive, and the ordinary graph/matroid Tutte polynomial is not the record law.

**Nonclaim.** This paper does not prove the full boundary tensor `Bbar` is the right physical transfer law; Receipt 53 shows it is too reconstructive in the audited toy.

**Nonclaim.** This paper does not prove an all-`N` theorem for the compressed score-loss boundary histogram `Hbar`.

**Nonclaim.** This paper does not prove the `N=7` or `N=8` `Hbar` covers are canonical or unique.

**Nonclaim.** This paper does not prove fixed-name stability for `Hbar` covers; Receipt 55 shows cover drift.

**Nonclaim.** This paper does not prove that local flags of size at most `5` suffice for `Hbar` at all larger `N`.

**Nonclaim.** This paper does not prove the compressed boundary cover theorem for the physical record law; it proves finite staged/fiber receipts.

## 65. Receipt ledger

First command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_matching_generating_identity.py
```

First final line:

`CHECKS PASSED: 4/4`

Second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_cycle_determinant_surrogate.py
```

Second final line:

`CHECKS PASSED: 4/4`

Third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_labelled_cycle_index_correction.py
```

Third final line:

`CHECKS PASSED: 4/4`

Fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_exact_2core_sector_decomposition.py
```

Fourth final line:

`CHECKS PASSED: 4/4`

Fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_sector_cancellation_stability.py
```

Fifth final line:

`CHECKS PASSED: 4/4`

Sixth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_sector_signature_audit.py
```

Sixth final line:

`CHECKS PASSED: 3/3`

Seventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_matching_root_radius_audit.py
```

Seventh final line:

`CHECKS PASSED: 3/3`

Eighth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_profile_envelope_implication.py
```

Eighth final line:

`CHECKS PASSED: 5/5`

Ninth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_zero_free_radius_no_go.py
```

Ninth final line:

`CHECKS PASSED: 4/4`

Tenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_sector_shape_amplitude_no_go.py
```

Tenth final line:

`CHECKS PASSED: 4/4`

Eleventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_top_order_lambda_boundary.py
```

Eleventh final line:

`CHECKS PASSED: 4/4`

Twelfth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_top_order_beta_boundary.py
```

Twelfth final line:

`CHECKS PASSED: 4/4`

Thirteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_lower_order_dominance_audit.py
```

Thirteenth final line:

`CHECKS PASSED: 4/4`

Fourteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_near_top_defect_profile.py
```

Fourteenth final line:

`CHECKS PASSED: 4/4`

Fifteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_deep_defect_peak_boundary.py
```

Fifteenth final line:

`CHECKS PASSED: 4/4`

Sixteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_defect_saddle_motion_audit.py
```

Sixteenth final line:

`CHECKS PASSED: 4/4`

Seventeenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_projection_sufficiency_invariant.py
```

Seventeenth final line:

`CHECKS PASSED: 8/8`

Eighteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_projected_likelihood_basis_audit.py
```

Eighteenth final line:

`CHECKS PASSED: 4/4`

Nineteenth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_controlled_projection_martingale.py
```

Nineteenth final line:

`CHECKS PASSED: 5/5`

Twentieth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_flag_deck_reconstruction_audit.py
```

Twentieth final line:

`CHECKS PASSED: 5/5`

Twenty-first command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_deck_ambiguity_certificate.py
```

Twenty-first final line:

`CHECKS PASSED: 4/4`

Twenty-second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_flag_compression_no_go.py
```

Twenty-second final line:

`CHECKS PASSED: 4/4`

Twenty-third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_flag_operator_family_audit.py
```

Twenty-third final line:

`CHECKS PASSED: 5/5`

Twenty-fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_flag_interaction_expansion_audit.py
```

Twenty-fourth final line:

`CHECKS PASSED: 5/5`

Twenty-fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_greedy_flag_operator_selection.py
```

Twenty-fifth final line:

`CHECKS PASSED: 4/4`

Twenty-sixth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_greedy_operator_robustness.py
```

Twenty-sixth final line:

`CHECKS PASSED: 3/3`

Twenty-seventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_score_polynomial_sufficiency.py
```

Twenty-seventh final line:

`CHECKS PASSED: 5/5`

Twenty-eighth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_adversarial_score_family_audit.py
```

Twenty-eighth final line:

`CHECKS PASSED: 6/6`

Twenty-ninth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_unresolved_nullspace_audit.py
```

Twenty-ninth final line:

`CHECKS PASSED: 5/5`

Thirtieth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_projection_ward_tower.py
```

Thirtieth final line:

`CHECKS PASSED: 5/5`

Thirty-first command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_effective_action_projection_identity.py
```

Thirty-first final line:

`CHECKS PASSED: 5/5`

Thirty-second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_flag_deletion_projectivity.py
```

Thirty-second final line:

`CHECKS PASSED: 4/4`

Thirty-third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_multivariate_score_polynomial.py
```

Thirty-third final line:

`CHECKS PASSED: 5/5`

Thirty-fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_rook_hit_expansion_certificate.py
```

Thirty-fourth final line:

`CHECKS PASSED: 4/4`

Thirty-fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_rare_spike_amplification.py
```

Thirty-fifth final line:

`CHECKS PASSED: 4/4`

Thirty-sixth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_targeted_atom_amplification.py
```

Thirty-sixth final line:

`CHECKS PASSED: 4/4`

Thirty-seventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_n8_transfer_and_nullspace.py
```

Thirty-seventh final line:

`CHECKS PASSED: 5/5`

Thirty-eighth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_n8_polynomial_minimal_cover.py
```

Thirty-eighth final line:

`CHECKS PASSED: 5/5`

Thirty-ninth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_minimal_cover_ladder.py
```

Thirty-ninth final line:

`CHECKS PASSED: 5/5`

Fortieth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_deletion_flow_conflict_cover.py
```

Fortieth final line:

`CHECKS PASSED: 5/5`

Forty-first command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_washout_sector_promotion_bound.py
```

Forty-first final line:

`CHECKS PASSED: 5/5`

Forty-second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_admissibility_norm_audit.py
```

Forty-second final line:

`CHECKS PASSED: 6/6`

Forty-third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_n9_feasibility_probe.py
```

Forty-third final line:

`CHECKS PASSED: 5/5`

Forty-fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_n9_active_flag_scan.py
```

Forty-fourth final line:

`CHECKS PASSED: 5/5`

Forty-fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_n9_active_minimal_cover.py
```

Forty-fifth final line:

`CHECKS PASSED: 5/5`

Forty-sixth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_worst_unresolved_atom_attack.py
```

Forty-sixth final line:

`CHECKS PASSED: 5/5`

Forty-seventh command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_omitted_local_flag_spike_scan.py
```

Forty-seventh final line:

`CHECKS PASSED: 5/5`

Forty-eighth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_hidden_lift_realizability.py
```

Forty-eighth final line:

`CHECKS PASSED: 5/5`

Forty-ninth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_admissibility_candidate_norms.py
```

Forty-ninth final line:

`CHECKS PASSED: 5/5`

Fiftieth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_palm_flag_sufficiency_audit.py
```

Fiftieth final line:

`CHECKS PASSED: 5/5`

Fifty-first command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_cover_transfer_matrix.py
```

Fifty-first final line:

`CHECKS PASSED: 5/5`

Fifty-second command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_external_math_campaigns.py
```

Fifty-second final line:

`CHECKS PASSED: 10/10`

Fifty-third command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_rooted_deletion_score_recurrence.py
```

Fifty-third final line:

`CHECKS PASSED: 8/8`

Fifty-fourth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_boundary_histogram_minimal_cover.py
```

Fifty-fourth final line:

`CHECKS PASSED: 4/4`

Fifty-fifth command:

```bash
isp/code/.venv/bin/python isp/v7/code/p29_boundary_cover_transfer.py
```

Fifty-fifth final line:

`CHECKS PASSED: 5/5`

## 66. Bottom line

The campaign found the real generating object for the sparse-pair coefficient sector, and it is not just the determinant.

The hierarchy is now:

$$
\text{matching polynomial}
\rightarrow
\text{Möbius/falling-factor expansion}
\rightarrow
\text{signed 2-core sector profile}
\rightarrow
\text{factorial-normalized profile envelope}
\rightarrow
\text{finite-falling beta boundary}
\rightarrow
\text{moving near-top defect saddle}
\rightarrow
\text{bulk bound}.
$$

The `sqrt(2)` shortcut is dead. The `0.65` guard is dead. Fixed one-defect dominance is dead. Fixed `k=2` is not secure.

But the larger invariant is now visible:

$$
\text{hidden lift}
\rightarrow
\text{projection to committed records}
\rightarrow
L_N=\frac{dQ_N}{dP_N}
\rightarrow
\text{washout or sector promotion}.
$$

The click law is not a beta guard. It is a projective record law whose committed sigma-field is sufficient. Numerical envelopes, matching polynomials, bracket actions, interval profiles, and density regularity tests are admissible only as representations or certificates of the projected likelihood field.

The projected-likelihood basis audit adds a new warning: the current known-sector basis is not projection-complete even in a finite staged/fiber toy. The first basis that moves the residual in the right direction is not another scalar guard. It is the induced-suborder or flag profile:

$$
\log L_N
\approx
\sum_F a_F\, t_{\mathrm{ind}}(F,R_N),
$$

where `F` ranges over finite record suborders and `t_ind(F,R_N)` is the induced-suborder count or density. The full record atom is exact but tautological; the real theorem would need decay, locality, or projective compression of the coefficients `a_F`.

The controlled projection martingale receipt then gives the predictive rule that is actually proven:

$$
\boxed{
L_{N,G}
=
\mathbb E_{P_N}
\left[
L_N\mid G
\right]
}
$$

for any committed sector filtration `G`. This is the finite predictive law. The click law is not obtained by guessing a statistic; once the record filtration is specified, the predictor is forced.

So the remaining unknown is not the form of prediction. It is the admissible controlled filtration:

$$
G_0\subseteq G_1\subseteq G_2\subseteq\cdots,
\qquad
L_{N,G_k}
=
\mathbb E[L_N\mid G_k],
$$

with martingale increments whose residue is bounded, summable, compressible, or promoted as a physical sector.

The flag-deck campaign sharpens this. In the staged/fiber toy, induced suborder decks behave like a reconstruction filtration: `4`-decks reconstruct the audited `N=6` quotient; `5`-decks reconstruct the audited `N=7` quotient; and the single `N=7` known+`4` ambiguity is separated by explicit `5`-flag counts.

But the hostile compression audit prevents a false ending. Exact deck martingales can approach the full atom lookup table:

$$
\frac{1955}{1956}
$$

of the `N=7` records are already separated by pure `4`-decks, while the corresponding linear/action projection still has only

$$
R^2=0.778620931186946918826415.
$$

Thus the next law cannot merely say "use flags." It must say how flags are controlled: by coefficient decay, locality, renormalized increments, or a projective compression theorem.

The operator-family and interaction audits then rule out two tempting shortcuts. Coarse flag geometry is too lossy: known+relation/height/width/interval/degree grouped flags capture only

$$
0.671063398498379280717221
$$

of the exact chi-square residue, almost identical to known sectors alone. Low-order operator products help but do not close the action gap: the best audited known+`3`-flag quadratic/cross action reaches

$$
R^2=0.800037784431876780553483.
$$

The strongest finite opening is different. Greedy exact local-flag selection finds a tiny predictively sufficient filtration:

$$
\{\texttt{flag3\_36},\texttt{flag4\_206},\texttt{flag5\_17288},\texttt{flag4\_0}\}.
$$

At `N=7`, these four operators close the projected likelihood gap while leaving one two-record atom unresolved. The same four-step closure holds for staged/fiber weight bases `2`, `3`, and `5`.

The score-polynomial receipt strengthens this from numerical robustness to an exact finite identity. The normalized hidden fiber polynomial

$$
\frac{W_R(t)}{|\pi_N^{-1}(R)|}
$$

is constant on every known+four atom. The same four operators therefore suffice for all weight bases `t` in the audited one-parameter staged/fiber family.

The adversarial score-family receipt scopes the result. The fixed four survive natural coordinate tilts, but a hostile score aimed at the single unresolved atom breaks them. Fresh greedy flags repair that hostile law. So the literal list of four operators is not the law; the law would have to derive a controlled local-operator filtration from an admissibility or regularity principle.

The six-campaign receipts make that statement sharper.

The Noether/Ward receipt says hidden structure has no independent charge:

$$
L_N\circ\pi_N
=
\mathbb E[\widetilde L_N\mid \pi_N].
$$

The Witten/action receipt says the corresponding action is the effective projected action, with an exact KL Pythagorean identity. The Riemann/deletion receipt says induced flags belong to a deletion-covariant record algebra. The Ramanujan/rook receipt says the hidden score polynomial is a conditional hit polynomial, not a mysterious numerical fit. These are not separate metaphors; they are the same projection rule seen through statistics, action, geometry, and finite algebra.

The nullspace audit makes the scope sharper. The information missed by known sectors plus the four operators is not a broad invisible family at `N=7`; it is concentrated on one two-record atom with null mass

$$
0.000793650793650793650793650793651.
$$

Ordinary local flags separate it. Thus the next theorem target is not "add every possible flag." It is a regularity/washout theorem for rare spiky residue, plus a sector-promotion rule for residue that does not wash out.

The `N=8` transfer prevents a second false ending. The same four operators still close the audited same-half polynomial, but the unresolved nullspace grows to `35` atoms and fresh greedy priority changes. Minimal finite covers are still tiny: no single or pair of local flags closes the `N=8` conflicts, but triples do. Therefore the living invariant is not a fixed list of operators. It is a small projectively stable conflict-cover problem inside a deletion-covariant local algebra.

The cover-ladder receipt sharpens this from a slogan into finite algebra:

$$
N=6,7,8
\quad\Longrightarrow\quad
\text{minimal cover size}=0,4,3.
$$

The cover size does not monotonically grow in the audited window, and the representatives drift. That kills both lazy endings: not "known sectors are enough" and not "these four flag names are the law." The invariant is controlled cover complexity inside a projective local algebra.

The deletion-flow receipt then separates two notions that should not be conflated. The local algebra is projective:

$$
\sum_{v\in R}
\operatorname{count}_F(R\setminus v)
=
(N-|F|)\operatorname{count}_F(R),
$$

with `1242696` checked `N=8` to `N=7` identities and zero violations. But finite sufficient covers can drift inside that algebra: the first `N=8` minimal triple is sufficient at `N=8` and not sufficient at `N=7`.

The washout receipt gives the admissibility fork in its clean finite form. For a filtration `G`, let `U` be the union of its rare non-singleton atoms. Then

$$
\mathbb E_P[(L-\mathbb E[L\mid G])^2]
\le
\mathbb E_P[L^2\mathbf 1_U]
\le
P(U)\sup_U L^2.
$$

So "rare" is not enough. Rare residue washes out only when likelihood on it is controlled. If projected likelihood concentrates on that rare atom, the atom is a physical sector or an inadmissible hidden refinement. In the finite audit, local `flag5_920` amplification at base `1000` has residual about

$$
5.03982851249832520279889378734\times 10^{-21},
$$

while direct unresolved-atom targeting at base `10000` has residual

$$
803.793339228614059469290359459.
$$

The admissibility-norm receipt strengthens this again. The finite norm

$$
A_2(G,L)=\mathbb E_P[L^2\mathbf 1_U]
$$

is not a decorative diagnostic; it catches a real failure of a too-simple rule. A local `flag5_920` spike at `N=8` has

$$
A_2=0.957817256204899537036401173248
$$

under the fixed-four cover. So locality alone is not admissibility. The relevant operator has to be in the committed cover, or its residue has to be small in the admissibility norm. Under the first `N=8` minimal triple, the audited separator spike has residual zero.

The `N=9` receipts push the conflict-cover picture one step further. Exact `N=9` enumeration is feasible and gives

$$
131526
$$

unlabeled record classes. The known-lite sector partition still has a large conflict landscape:

$$
87066
$$

score-polynomial conflict pairs. The active-flag scan finds that all `84` audited local flag types are active, and an eight-step greedy local cover closes all known-lite conflict pairs. The exact active-mask search then improves this: the scoped known-lite cover number is `7`, with no cover of size at most `6`. One size-`7` witness is:

$$
\{\texttt{flags3:flag3\_36},
\texttt{flags5:flag5\_16904},
\texttt{flags5:flag5\_25104},
\texttt{flags5:flag5\_8704},
\texttt{flags4:flag4\_14},
\texttt{flags4:flag4\_2248},
\texttt{flags5:flag5\_25488}\}.
$$

This is not a full `N=9` physical minimal-cover theorem, because the base partition is known-lite and excludes matching features. But it is the strongest finite sign yet that the controlled local conflict-cover target is alive beyond `N=8`.

The adversarial receipts then prevent the wrong victory lap. Every unresolved non-singleton atom has an exact worst-spike residue

$$
\frac{1}{P(x)}-\frac{1}{P(A)}.
$$

For the audited covers the limits reach `1260`, `15120`, and `20160`. Ordinary omitted local flags can also be hostile: under the first `N=8` minimal triple, `flags5:flag5_926` drives residual

$$
18956.9690726015044985623
$$

and puts

$$
Q(U)=0.990490350856278364341481
$$

on the unresolved sector. Finally, these hostile projected laws are not excluded by saying "hidden variables are unphysical": they have fiber-constant hidden lifts with zero vertical residue. Projection is an invariant, not an admissibility condition.

So the current best target is not full reconstruction and not a coarse geometric action. It is:

> projective predictive sufficiency by a small controlled local-operator filtration.

The big missing theorem therefore has three layers.

First, for the specific sparse-pair residue studied here:

> derive the moving near-top defect saddle and its limiting peak beta from the physical rank-copula, then prove a bulk bound away from that saddle.

Second, for the record law itself:

> define the admissible projected likelihood class, then prove that every admissible hidden refinement either has bounded projected second moment, or promotes its projected likelihood residue as an explicit record sector.

Third, for projection-completeness:

> prove that the projected likelihood field admits a small projectively stable local-operator filtration with controlled martingale increments, or exhibit a stable residual outside every finite controlled basis.

The six-campaign synthesis gives the current best wording of that missing principle:

> hidden structure is admissible only through its record-projected effective likelihood; a click law is a projectively stable, record-intrinsic, controlled local-operator filtration sufficient for that likelihood.

The strongest concrete version now is:

> the click law is the projective limit of effective record likelihoods, approximated by a controlled causal Palm-flag filtration whose conflict-cover size grows slowly and whose rare residual atoms either wash out under admissible hidden scores or become promoted record sectors.

After the six parallel campaigns, the missing theorem can be named more sharply:

> prove a record-covariant admissibility theorem for projected likelihoods, a causal Palm-flag sufficiency theorem for the admitted class, and a finite-algebra conflict-cover recurrence that controls the drift of sufficient local operators under deletion/insertion.

Receipts 49-51 turn those three slogans into finite targets. Admissibility cannot mean bounded local coefficient size: a `log 2` local flag can still put essentially all of `Q` on an unresolved sector. Palm-flag geometry is a real carrier but not sufficient in the first audited family: endpoint-symmetric rooted flags raise `R^2`, but leave a large residual. Cover transfer is not fixed-name transfer: the `N=7` fixed four travel upward in this score, the first `N=8` triple fails downward, and the scoped `N=9` known-lite witness transfers down without yet being a comparable physical theorem.

Those three gates are coupled. A Palm-flag filtration without admissibility is beaten by atom spikes. Admissibility without Palm-flags has no intrinsic geometric carrier. Conflict covers without a deletion/insertion recurrence remain finite certificates rather than a law.

The next proof object is therefore not another greedy cover by itself. It is the score-boundary recurrence:

$$
N W_{N,R}(u)
=
\sum_A\sum_{a,b}
B_N^\downarrow(R,A;a,b)u^{a+b},
$$

plus an admissibility theorem saying which projected likelihoods are allowed to use that recurrence without becoming atom-spike sectors. If this recurrence closes in a causal Palm-flag algebra, the click law has a constructive route. If it fails, the paper has identified the obstruction sharply: there is stable record-visible residue outside every controlled local filtration, so it must be promoted as new record structure rather than hidden.

Receipt 52 ranks the external mathematics. The live route is not literal modular forms and not ordinary Tutte universality. It is:

$$
\text{algebraic-statistical fibers}
\quad+\quad
\text{incidence/decomposition recurrence}
\quad+\quad
\text{projected quasilocality}.
$$

WL/coherent configurations and flag algebras are the likely compression language for the committed filtration. Modular/noncongruence forms and Tutte universality remain useful hostile metaphors: they ask whether there is a stable operator algebra and a universal deletion rule. The current finite evidence says "not yet" for both literal imports.

Receipts 53-55 then resolve the immediate recurrence fork. The raw deletion tensor is exact, but too reconstructive. The compressed score-loss boundary

$$
H_R(a,b)
=
\mathbb P(a,b\mid R)
$$

is the first serious bridge object: it reconstructs `Wbar_R`, is much smaller than full `Bbar`, and is locally coverable at `N=7,8`. But its covers drift. The theorem target is therefore now:

> prove controlled drift of compressed boundary covers for `Hbar` inside the causal Palm/WL/flag algebra, with admissibility control on any unresolved residue.

This is better than the previous target. It no longer asks for a fixed list of operators, and it no longer asks the full boundary tensor to be physical. It asks for a stable compression of the deletion boundary sufficient for projected likelihood transfer.

The finite predictive law has now been found and proved. The final physical law is not yet proved because the controlled filtration is not yet derived. If the sparse-pair theorem fails, the click law must promote the sector-profile data itself as part of the record law. If the flag/action expansion succeeds, Paper XXVIII's record-sufficiency principle gets its first credible constructive language. In either case, the invariant is no hidden residue under record projection, and the predictive mechanism is the controlled likelihood martingale.
