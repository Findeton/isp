# The record click-law, XXII: marked compensators and finite-order manifoldlikeness stress tests

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-24. Twenty-second paper of the v7 program. This paper follows Paper XXI's scalar record-martingale formulation and asks what kind of order-sensitive law would be needed before the click law could have a lever on the manifoldlikeness gate identified in Paper XI. Tags: **[PRINCIPLE]** = candidate formulation; **[STRESS TEST]** = finite diagnostic, not a theorem; **[COUNTEREXAMPLE]** = explicit obstruction or spoof; **[CONSTRAINED]** = narrowed but not unique; **[OPEN]** = disclosed residue. New numerical checks are in `v7/code/p22_marked_manifold_audit.py`, all at mpmath `dps = 140`.

---

## Scope guards

1. **This paper does not prove manifoldlikeness.** It builds finite stress tests. It does not show that SHARD records, causal sets, cellular automata, hidden machines, or any proposed substrate typically produce manifold-like orders.

2. **The scalar martingale is not a manifoldlikeness law.** Paper XXI's dense scalar law is `A_chi=kappa chi`. The receipt uses the toy normalization `chi=N` only to show that a scalar allowance is blind to the order placed on a fixed number of records. Nothing in this paper changes the Paper XXI compensator.

3. **Marked compensators are a candidate route, not a forced architecture.** The robust conclusion is weaker and cleaner: any record law that hopes to solve manifoldlikeness must be order-sensitive beyond the scalar count. Event-marked compensators, pair-update compensators, terminal order actions, or covariant nonlocal layer kernels are possible routes. This paper develops the marked-compensator route because it is the natural extension of Paper XXI.

4. **Event marks, pair statistics, and terminal diagnostics are different objects.** The event-marked process `xi(dchi,dm)` covers marks visible at commitment. Ordering fraction, height exponent, and interval-damped pair density are global or pair/update statistics. They cannot be silently treated as predictable event marks.

5. **`P_alpha` is not a martingale bracket.** The receipt uses

   `P_alpha = N^-1 sum_(x<y) exp(-alpha |I(x,y)|)`

   as an interval-damped pair density. It is not the predictable quadratic bracket `<M^f,M^g>`. Bracket/concentration laws remain a separate future target.

6. **The deterministic grid benchmark is not Lorentz evidence.** The product order `[n]x[n]` is a lightcone-coordinate grid benchmark with computable statistics. Passing that benchmark says nothing by itself about Lorentz covariance or typical Poisson-sprinkled intervals.

---

## Abstract

Paper XXI replaced the ontology-sounding statement "clicks are Poisson in `chi`" by the record-facing law

$$
N-A\quad\text{is the record martingale}.
$$

That statement is strong about scalar counts, but it is order-blind. If the same scalar content/count is assigned to different finite orders, the scalar compensator cannot distinguish a lightcone-coordinate grid benchmark, a chain, an antichain, or a KR-layered non-manifold order. Therefore the scalar click law cannot by itself be the full record law if the program needs the records to suppress non-manifold orders.

The natural next object is an order-sensitive law. One candidate extension is the event-marked record measure

$$
\xi(d\chi,dm)=\sum_k\delta_{(\chi_k,m_k)}(d\chi,dm),
$$

with predictable compensator

$$
\nu(d\chi,dm).
$$

For every bounded predictable event-mark test `f`, the compensated process

$$
\int f\,d\xi-\int f\,d\nu
$$

would be a martingale. But the manifoldlikeness diagnostics used here are not all event marks. Ordering fraction, longest-chain height, and interval-damped pair density are terminal or pair/update functionals of the finite order. They require either separate compensators for incremental order statistics or terminal concentration/action estimates. The event-marked point-process notation alone does not cover them.

The finite tests produce three results.

First, a scalar compensator is order-blind under the toy fixed-`chi=N` convention.

Second, a single Myrheim-Meyer dimension condition is explicitly spoofable. A KR three-layer expected family with layer sizes `(t,2t,t)` can be retuned at each scale so that its expected ordering fraction is `f(2)=1/2` to receipt precision, hence the naive Myrheim-Meyer dimension is `2`, while its height exponent remains `0` and its interval-damped pair density grows like `N`.

Third, a naive combined benchmark audit is not a manifoldlikeness gate. The audit accepts the deterministic `[n]x[n]` lightcone grid and rejects chain, antichain, ordinary KR, and spoofed KR examples. But the 1+1 binomial-sprinkling stress sample has the right Myrheim-Meyer dimension and height scaling while failing the same tightness threshold for `P_alpha`. That failure is valuable: it prevents mistaking a grid-calibrated statistic for a continuum law.

The follow-up calibration is the main new positive. For fixed-N 1+1 sprinklings, the finite-N expectation of `P_alpha` is derived:

$$
\mathbb{E}[P_\alpha]
=(N-1)\sum_{k=0}^{N-2}
\frac{\binom{N-2}{k}\left(-(1-e^{-\alpha})\right)^k}
{(k+1)^2(k+2)^2}.
$$

The calibrated statistic

$$
\rho_\alpha=\frac{P_\alpha}{\mathbb{E}_{\mathrm{sprinkle}}[P_\alpha]}
$$

stays within about `2.2%` of `1` on the fixed sprinkling stress sample, and a small eight-sample ensemble stays within about `6.6%`. A deliberately adversarial non-manifold family--a complete bilayer on `N-sqrt(N)` records plus an isolated chain of length `sqrt(N)`--matches `d_MM -> 2` and `H ~ sqrt(N)`, but has `rho_alpha ~ 79.94` at `N=4096` and is cleanly rejected.

A stronger adversary then breaks the single-alpha version: a complete three-layer order with a thin middle layer plus an isolated `sqrt(N)` chain matches `d_MM`, height, and `rho_(log 2)` at the tested scales. At `N=4096` it has `d_MM=2.033075382226986471`, `H=64`, and `rho_(log 2)=0.97067568003230303363`. A small multi-alpha profile exposes it: the same order has `rho_(log 1.5)=1.11581477423` and `rho_(log 3)=1.21179983464`. A wider five-alpha generating-function profile sharpens the stress test at `N=1024`: the fixed sprinkling sample has maximum log profile gap `0.014373367511807564295`, while chain, bilayer-plus-chain, and thin-middle adversaries have maximum log gaps `1.6559478550491456042`, `3.539519242504960864`, and `1.2427129828146969189`.

Finally, even the five-alpha profile is underdetermined at the interval-histogram level. The receipt constructs a positive real-weight interval-size measure matching all five tested alpha moments to receipt precision while hiding `93.287371980460700041%` of the relation mass at interval size `1000`. This is not yet a finite-poset construction, but it is the moment-problem warning: finitely many Laplace samples cannot define the order. A simple complete-sandwich attempt to realize that hidden mass as a poset then pays a large transitivity tax: the forced low-interval density is about `77.804057396441232631` times the sprinkling expectation at `alpha=log 2`.

The bottom line is narrow but useful: scalar count laws are too weak; MM-only laws are spoofable; pair-density-only laws are fooled by chains; naive grid tightness fails on actual sprinklings; single-alpha calibrated interval density is spoofable; finite multi-alpha samples are still not complete. The record-law problem is therefore not solved, but its next mathematical target is clearer: an order-sensitive law for event, pair, and global order statistics, with covariance-compatible concentration and no finite-neighbor overclaim.

---

## 1. What the scalar martingale cannot see

Paper XXI's scalar statement was:

`N - A` is the record martingale.

In the dense simple regime:

$$
A_\chi=\kappa\chi.
$$

The receipt for this paper uses a deliberately artificial convention, `chi=N`, only to demonstrate order-blindness at fixed size. With `kappa=0.73` and `N=256`, the scalar allowance is

$$
A=186.88
$$

for all of the following:

- deterministic `[n]x[n]` lightcone-coordinate grid benchmark;
- chain;
- antichain;
- KR three-layer order.

This is structural. A scalar count compensator knows only scalar content or count. It has no slot for local order type, height growth, interval structure, layer profile, or cross-chain constraints.

So the first conclusion is:

> **[CONSTRAINED] A scalar record martingale can be the scalar projection of the click law, but it cannot be the full manifoldlikeness law.**

---

## 2. Three different mathematical objects

The reviews forced a useful separation. There are at least three levels.

### 2.1 Event-marked records

At a committed event `k`, attach a mark `m_k` that is visible from the record at commitment time. Examples may include:

- channel label;
- local parent/past profile visible at the new commitment;
- immediate order relation labels supplied by the committing rule;
- joint ledger mark for a two-chain event;
- local content increment.

The event-marked measure is

$$
\xi_1(d\chi,dm)=\sum_k \delta_{(\chi_k,m_k)}(d\chi,dm).
$$

A marked-compensator law would specify its predictable projection

$$
\nu_1(d\chi,dm).
$$

Then, for bounded predictable event-mark tests `f`,

$$
M^f=\int f\,d\xi_1-\int f\,d\nu_1
$$

is the marked record martingale. The scalar law is the special test `f=1`.

### 2.2 Pair/update statistics

Many manifoldlikeness diagnostics are not event marks. They are pair or interval statistics. For a finite order `C_n`, define for example

$$
Z_n^\phi=\sum_{x<y\ \mathrm{in}\ C_n}\phi\!\left(|I_n(x,y)|\right).
$$

The interval-damped pair density used in the receipt is

$$
P_\alpha(C_n)=N^{-1}Z_n^\phi,\qquad \phi(k)=e^{-\alpha k}.
$$

If one wants a martingale law for such a statistic, the object is not `xi_1(dchi,dm)` alone. It is an incremental process:

$$
\Delta Z_j^\phi=Z_j^\phi-Z_{j-1}^\phi,
$$

with predictable compensator

$$
C_n^\phi=\sum_{j\le n}\mathbb{E}\!\left[\Delta Z_j^\phi\mid \mathcal{F}_{j-1}^{\mathrm{rec}}\right].
$$

Then `Z_n^phi-C_n^phi` could be a martingale if a law of this type were postulated and checked. This paper does not derive that law. It only identifies the missing object.

### 2.3 Terminal/global diagnostics

Ordering fraction, Myrheim-Meyer dimension, longest-chain height, and fitted exponents such as

$$
\beta_H=\frac{d\log H}{d\log N}
$$

are terminal or family-level diagnostics. They are useful for audits, but they are not automatically predictable marks. They require either:

- a terminal action/weight over finite orders;
- concentration estimates for order statistics;
- sequential compensators for their increments;
- or an alternative covariant order-kernel dynamics.

This separation is now part of the result. It prevents the marked-compensator slogan from becoming a hidden overclaim.

---

## 3. The finite statistics tested

### 3.1 Myrheim-Meyer ordering fraction

For a manifoldlike `d`-dimensional Minkowski Alexandrov interval, the expected related-pair fraction is

$$
f(d)=\frac{\Gamma(d+1)\Gamma(d/2)}{2\Gamma(3d/2)}.
$$

The receipt checks at `dps=140`:

- `f(1)=1`;
- `f(2)=1/2`;
- `f(3)=8/35`;
- `f(4)=1/10`;
- `f^-1(f(2))=2`.

This is a good dimension-like statistic when its assumptions hold. It is not a manifoldlikeness law.

### 3.2 Height exponent

A 2D lightcone-coordinate grid benchmark with `N=n^2` has longest chain length

$$
H=2n-1,
$$

so `H ~ N^(1/2)`. A chain has `H=N`, an antichain has `H=1`, and a KR three-layer order has height `3` independent of scale. The height exponent is therefore a necessary independent stress test.

### 3.3 Interval-damped pair density

The receipt defines

$$
P_\alpha=\frac{1}{N}\sum_{x<y}\exp\!\left(-\alpha |I(x,y)|\right),
$$

with

$$
\alpha=\log 2.
$$

This gives full weight to empty intervals and exponentially lower weight to pairs with large interiors. It is an order statistic, not a finite-neighbor graph and not a martingale bracket.

The statistic detects two obvious pathologies:

- antichains have `P_alpha=0`;
- KR layered orders have many adjacent-layer relations, so `P_alpha` grows like `N`.

But the statistic is not calibrated as a continuum criterion. The sprinkled stress test in Section 6 shows that the naive tightness threshold fails on an actual 1+1 binomial-sprinkling sample.

---

## 4. The KR expected-family spoof

Use a three-layer KR expected family with layer sizes

$$
(t,2t,t).
$$

Adjacent-layer relations occur with probability `p`; bottom-top relations are induced by at least one middle bridge. For each tested `t`, the receipt solves

$$
\mathbb{E}[r_{\mathrm{KR}}(p_t)]=f(2)=\frac{1}{2}
$$

to receipt precision.

At `t=256` (`N=1024`) it prints:

- `p_star = 0.7490234375` to displayed precision;
- bridge unsaturation defect at the displayed value:

  `8.3857807068945604467231020027090178106261655757775071150699e-184`;

- `r_KR(p_star)=0.5` to receipt precision;
- `d_MM=2.0` to receipt precision;
- `beta_H=0.0`.

The displayed dyadic value should not be read as an exact closed form for the finite model. The bridge defect is far below the `dps=140` equality threshold; at higher precision the true root differs beyond the displayed digits. The claim is therefore an expected-family, receipt-precision spoof, not an exact finite-poset enumeration.

There is also a scale issue: using the same `p_star` at every `t` is not the same as a retuned spoof family. The receipt therefore retunes `p_t` at each tested scale:

- `p(64)=0.74609375`;
- `p(128)=0.748046875`;
- `p(256)=0.7490234375`;
- `p(512)=0.74951171875`.

Along this retuned expected family, the interval-damped pair density exponent is

$$
\beta_P=1.002166452224335547350870187490795726306.
$$

So the corrected result is:

> **[COUNTEREXAMPLE] Myrheim-Meyer dimension alone is spoofable by a KR expected family. The spoof remains height-collapsed and pair-density divergent.**

That is enough to kill any proposed law that only targets `d_MM=2`.

---

## 5. Benchmark audit: useful but not final

The receipt compares:

- `grid2`: deterministic `[n]x[n]` lightcone-coordinate grid benchmark;
- `chain`;
- `antichain`;
- `KR p=1/2`;
- `KR spoof`: retuned expected-family spoof.

At the reference sizes:

| family | N | r | d_MM | H | beta_H | P_alpha | beta_P |
|---|---:|---:|---:|---:|---:|---:|---:|
| grid2 | 4096 | 0.515384615384615385 | 1.9595017549049 | 127 | 0.50659380713441 | 4.28478046004125398 | 0.028528255657992 |
| chain | 4096 | 1.0 | 1.0 | 4096 | 1.0 | 1.9990234375 | 0.0017766741408235 |
| antichain | 4096 | 0.0 | +inf | 1 | 0.0 | 0.0 | nan |
| KR p=1/2 | 1024 | 0.375366568914956012 | 2.3752285653636 | 3 | 0.0 | 128.0 | 0.9999999918286 |
| KR spoof | 1024 | 0.5 to receipt precision | 2.0 to receipt precision | 3 | 0.0 | grows like N | 1.002166452224335547350870187490795726306 |

The toy benchmark audit asks for:

- `d_MM` close to `2`;
- `beta_H` close to `1/2`;
- `P_alpha>0`;
- `beta_P` close to `0`.

Single diagnostics fail:

- MM-only accepts both the grid benchmark and the spoofed KR expected family;
- pair-density-only accepts both the grid benchmark and the chain.

The combined toy audit accepts the deterministic grid benchmark and rejects chain, antichain, ordinary KR, and spoofed KR:

`grid/chain/antichain/KR/spoofedKR = True False False False False`.

This is a useful benchmark result, not a manifoldlikeness criterion.

---

## 6. Sprinkling stress test: the naive pair-density threshold fails

The receipt also includes a fixed binomial-sprinkling stress sample. In 1+1 lightcone coordinates, sorting by one coordinate leaves the other as a random permutation; this lets the receipt compute the order type with integer combinatorics and no float sampling.

For sizes `N=128,256,512,1024`, the fixed stress sample gives:

| N | r | d_MM | H | P_alpha |
|---:|---:|---:|---:|---:|
| 128 | 0.525836614173228346 | 1.9325689685044 | 19 | 5.76365797158988573 |
| 256 | 0.474080882352941176 | 2.0707038508372 | 30 | 6.82393410916636629 |
| 512 | 0.471540178571428571 | 2.0778123396786 | 40 | 8.25247911707028853 |
| 1024 | 0.512908189760508309 | 1.9659506880548 | 57 | 9.80049379165319956 |

The fitted exponents are:

- `beta_H = 0.516992500144231236290747788789563301752`;
- `beta_P = 0.2571833011550796138328275745953037726407`.

So the sprinkled stress sample has the right MM behavior and height behavior, but fails the naive grid-calibrated tightness requirement `beta_P near 0`. The receipt explicitly checks:

`toy audit accepts fixed sprinkled stress sample? False`.

This is the most important negative result in the paper. It means the interval-damped pair density cannot be used with this normalization and threshold as a manifoldlikeness gate. At most, it is a pathology detector for the specific benchmark families.

The next mathematical question is now concrete:

> Find the correct covariant normalization, layer kernel, or terminal concentration law for interval statistics on actual sprinkled intervals, and then test adversarial non-manifold families against that calibrated object.

---

## 7. Finite-N sprinkling calibration

The correct first calibration is not a fitted power law. For fixed-N 1+1 binomial sprinklings, the expectation of `P_alpha` can be computed directly.

In lightcone coordinates, the Alexandrov interval is the unit square. For two random points, let `U` and `V` be the absolute coordinate gaps. They are independent with density `2(1-u)` and `2(1-v)`. A pair is causally comparable with probability `1/2`; if comparable, the interval volume between the two endpoints is `UV`. Conditional on `U,V`, the number of interior sprinkled points is

$$
K\sim \operatorname{Binomial}(N-2,UV).
$$

With `q=e^-alpha` and `c=1-q`,

$$
\mathbb{E}[q^K\mid U,V]=(1-cUV)^{N-2}.
$$

Expanding and integrating gives the exact finite-N expectation used in the receipt:

$$
\mathbb{E}_{\mathrm{spr}}[P_\alpha]
=(N-1)\sum_{k=0}^{N-2}
\frac{\binom{N-2}{k}(-c)^k}{(k+1)^2(k+2)^2}.
$$

This alternating sum is cancellation-heavy, so the receipt evaluates it with guard precision growing with `N`; downstream arithmetic and reporting consume it at the ambient receipt precision.

The leading asymptotic is logarithmic, not power-law:

$$
\mathbb{E}_{\mathrm{spr}}[P_\alpha]
=\frac{\log(cN)+\gamma-2}{c}+O\!\left(\frac{\log N}{N}\right),
$$

where `gamma` is Euler's constant. For the receipt value `alpha=log 2`, `c=1/2`, so

$$
\mathbb{E}_{\mathrm{spr}}[P_\alpha]
=2\left(\log(N/2)+\gamma-2\right)+O\!\left(\frac{\log N}{N}\right).
$$

That explains the earlier false alarm. Over small `N`, `P_alpha` can look like a weak power, but the continuum scaling is logarithmic.

Define the calibrated statistic:

$$
\rho_\alpha(C_N)=\frac{P_\alpha(C_N)}{\mathbb{E}_{\mathrm{spr},N}[P_\alpha]}.
$$

For the fixed sprinkling stress sample:

| N | P_alpha | E_spr[P_alpha] | rho_alpha |
|---:|---:|---:|---:|
| 128 | 5.76365797158988573 | 5.64374982130936748 | 1.02124618455 |
| 256 | 6.82393410916636629 | 6.95507052986244098 | 0.981145206201 |
| 512 | 8.25247911707028853 | 8.29848378105760074 | 0.994456256685 |
| 1024 | 9.80049379165319956 | 9.66063521973215122 | 1.01447716105 |

The maximum deviation from `1` is about `0.021246184554066429264`.

The receipt also runs a small ensemble band check with eight independent fixed-seed permutations at each size:

| N | reps | rho mean | rho sd | rho min | rho max |
|---:|---:|---:|---:|---:|---:|
| 128 | 8 | 0.997544576079026497 | 0.0352028914972 | 0.934352847144 | 1.05544606391 |
| 256 | 8 | 0.998536835616193409 | 0.0199053635641 | 0.969291106143 | 1.01873705875 |
| 512 | 8 | 0.997026187913509954 | 0.0117285433904 | 0.977893888339 | 1.01786141485 |

The maximum band deviation from `1` is `0.065647152855756993491`.

This repairs the first failed statistic only in a limited sense. The naive threshold `beta_P near 0` is not a continuum criterion; the calibrated finite-N statistic `rho_alpha near 1` is a usable first 1+1 sprinkling benchmark for this single interval statistic. It is not a concentration theorem and not a manifoldlikeness gate.

---

## 8. An adversary that matches MM and height

The next hostile test is a non-manifold family that matches the two old marks: Myrheim-Meyer dimension and height scaling.

For `N=n^2`, construct:

- a complete bilayer on `N-n` records, split as evenly as possible into bottom and top layers;
- an isolated chain of length `n`;
- no relations between the bilayer and the chain.

This is violently non-manifold. But it fools the first two large-scale marks:

- the complete bilayer has related-pair fraction tending to `1/2`, so `d_MM -> 2`;
- the isolated chain gives height `H=n=sqrt(N)`, so `beta_H=1/2`.

At the tested sizes:

| N | r | d_MM | H | beta_H | P_alpha | E_spr[P_alpha] | rho_alpha |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 | 0.470643939393939394 | 2.0803277740987 | 32 | 0.5 | 240.308593750000909 | 9.66063521973215122 | 24.875030293988 |
| 4096 | 0.484855769230769231 | 2.040917820539 | 64 | 0.5 | 992.2802734375 | 12.4124114374186207 | 79.942586373358 |
| 16384 | 0.492308624031007752 | 2.0206464262569 | 128 | 0.5 | 4032.265380859375 | 15.1787819884696313 | 265.65144580919 |

At `N=4096`, the adversary has `d_MM=2.0409178205389652714` and exact height exponent `1/2`, but `rho_alpha=79.942586373358417726`. It is rejected by the calibrated interval statistic.

This is a real improvement over the previous draft. The statistic is no longer "grid tightness." It is calibrated against the finite-N sprinkling expectation and then tested against a family that spoofs MM and height. But this adversary is crude: the complete bilayer creates `O(N^2)` empty intervals, so single-alpha `rho_alpha` rejects it easily. A more devious adversary can tune `rho_alpha`.

---

## 9. Thin-middle adversary: single-alpha rho is spoofable

The stronger adversary replaces the bilayer with a complete three-layer order `A < M < B`, where the middle layer is thin:

$$
|M|=m_N=O(\log N).
$$

It again adds an isolated chain of length `n=sqrt(N)` and no relations between the chain and the three-layer block. The three-layer block keeps the related-pair fraction near `1/2`; the isolated chain keeps `H=sqrt(N)`. The interval-damped density is approximately

$$
P_\alpha=
\frac{m_N(|A|+|B|)+|A||B|e^{-\alpha m_N}+O(n)}{N}.
$$

Therefore `m_N` can be tuned to match a single calibrated `rho_alpha`.

The receipt tunes the middle layer for `alpha=log 2`:

| N | middle | r | d_MM | H | rho(log 1.5) | rho(log 2) | rho(log 3) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 | 6 | 0.476274208822091887 | 2.0645936758881 | 32 | 2.0084290035 | 0.987985852458 | 0.801314191109 |
| 4096 | 12 | 0.487727506868131868 | 2.033075382227 | 64 | 1.11581477423 | 0.970675680032 | 1.21179983464 |
| 16384 | 15 | 0.493215795038588018 | 2.0181969590462 | 128 | 1.11737165812 | 0.988701726899 | 1.2594781569 |

At `N=4096`, this non-manifold order passes the current single-alpha story:

- `d_MM=2.033075382226986471`;
- `H=64=sqrt(N)`;
- `rho_(log 2)=0.97067568003230303363`.

But the multi-alpha profile exposes it:

$$
\max_\alpha|\rho_\alpha-1|=0.21179983463688568343
$$

over `alpha in {log 1.5, log 2, log 3}`.

So the corrected verdict is:

> `rho_(log 2)` is a useful calibrated stress statistic, but it is spoofable. A multi-alpha interval profile is strictly stronger, and even that is still only a finite stress test until concentration and adversarial completeness are understood.

---

## 10. The wider generating-function profile target

The natural next target is not a single `rho_alpha`, but the calibrated interval generating function

$$
G_C(q)=N^{-1}\sum_m H_m q^m,\qquad q=e^{-\alpha},
$$

where `H_m` is the number of related pairs whose open interval has size `m`. The tested statistic is the profile

$$
\rho_\alpha(C_N)=
\frac{G_C(e^{-\alpha})}{\mathbb{E}_{\mathrm{spr},N}[G(e^{-\alpha})]}.
$$

The receipt evaluates the five-point profile

$$
\alpha\in\{\log 1.25,\log 1.5,\log 2,\log 3,\log 4\}
$$

at `N=1024`. A fixed sprinkling sample stays close to the calibrated expectation:

| family | max `|log rho|` | rho(log 1.25) | rho(log 1.5) | rho(log 2) | rho(log 3) | rho(log 4) |
|---|---:|---:|---:|---:|---:|---:|
| fixed sprinkling | 0.0143733675118076 | 1.00969447447 | 1.01347713349 | 1.01447716105 | 1.01363546628 | 1.01296064982 |
| chain | 1.65594785504915 | 0.253052639622 | 0.225006405549 | 0.206621376814 | 0.195232128463 | 0.19091101395 |
| bilayer plus chain | 3.53951924250496 | 12.2255476561 | 18.0785998791 | 24.875030294 | 31.3213751822 | 34.4503529436 |
| thin-middle plus chain | 1.2427129828147 | 3.46500121335 | 2.0084290035 | 0.987985852458 | 0.801314191109 | 0.842330183437 |

This is the strongest finite stress result in the paper. The profile is not merely rejecting easy KR or bilayer empty-interval excess; it also rejects the thin-middle construction that was tuned to spoof `rho_(log 2)`.

But the result is still finite. A finite list of alpha values only samples a Laplace transform. The full finite histogram would be determined by enough information about `G_C(q)` as a polynomial, not by five samples.

So the honest target is:

> find a covariant law that controls the full interval/layer generating object, or an action/concentration principle equivalent to it for manifoldlikeness, then test transitive adversaries against that law rather than against a finite alpha checklist.

---

## 11. Finite alpha profiles are histogram-underdetermined

The next obstruction is more structural. For a fixed finite list of alphas, the data

$$
P_\alpha=N^{-1}\sum_m H_m e^{-\alpha m}
$$

are just finitely many Laplace-transform samples of the interval-size histogram `H_m`. A finite number of samples cannot determine a whole histogram.

The receipt demonstrates this directly at `N=4096` for

$$
\alpha\in\{\log 1.25,\log 1.5,\log 2,\log 3,\log 4\}.
$$

It constructs a positive real-weight histogram with thicknesses

`[0, 1, 2, 3, 4, 8, 1000]`

and weights

- `29775.2254126484171`;
- `11239.9854651288182`;
- `53977.9848650400055`;
- `7685.84893171081134`;
- `4989.49663384455552`;
- `173810.74690936495`;
- `3911800.71178226244`.

This real-weight measure matches all five tested alpha moments to receipt precision:

| alpha | moment target | matched moment | gap |
|---:|---:|---:|---:|
| 0.223143551314 | 108452.581012833222 | 108452.581012833222 | 1.6676173e-136 |
| 0.405465108108 | 71303.4573072431275 | 71303.4573072431275 | 6.737992e-137 |
| 0.69314718056 | 50841.2372476666705 | 50841.2372476666705 | 4.239567e-137 |
| 1.09861228867 | 39892.1924060194566 | 39892.1924060194566 | 1.6998757e-137 |
| 1.38629436112 | 36101.0795853034443 | 36101.0795853034443 | 6.1703337e-137 |

It also preserves the target related-pair count `r=1/2`, with `93.287371980460700041%` of the relation mass hidden at interval size `1000`, far beyond the tested alpha sensitivity.

This is not claimed as a finite-poset realization. It is a moment-problem adversary. Its message is sharp:

> Any finite alpha list is only a finite stress test. A law that really controls interval structure needs either the full interval-size distribution, a generating function over a continuum/rich family of alphas, or a separate action/concentration principle.

---

## 12. Finite-poset realizability audit

The histogram witness is deliberately not a finite-poset construction. The immediate question is whether it can be realized by a transitive poset without creating extra low-interval mass.

The simplest attempt is a complete sandwich: create `H` large-interval relations `A < B` by placing a middle layer of size `m` between bottom and top sets. If `|A||B|=H`, then even in the best balanced case

$$
|A|+|B|\ge 2\sqrt{H}.
$$

The same sandwich necessarily creates at least

$$
2m\sqrt{H}
$$

low-interval adjacent-layer relations of the forms `A < M` and `M < B`.

For the histogram witness at `N=4096`, the naive complete sandwich already fails the same-`N` vertex budget. To realize `H` large-interval relations with a middle layer of size `m`, the relaxed balanced lower bound requires

$$
|A|+|M|+|B|\ge m+2\sqrt{H}.
$$

For the receipt values:

- hidden large-interval mass: `3911800.71178226244268085`;
- hidden interval size: `1000`;
- minimum same-sandwich vertex count: `4955.65454092354351169787`, which is larger than `N=4096`;
- lower bound on low-interval tax: `2*m*sqrt(H)=3955654.54092354351169787`;
- tax density: `965.735971905161990160613`;
- sprinkling `E[P_alpha]` at `alpha=log 2`: `12.41241143741862072812732`;
- tax ratio: `77.8040573964412326305692`.

The review then opened the obvious next adversary: split the hidden mass across several independent sandwich reservoirs. That does not help. If reservoir `i` has hidden mass `H_i` and interval thickness at least `m`, the same complete-sandwich lower bound gives

$$
\sum_i 2m\sqrt{H_i}\ge 2m\sqrt{\sum_i H_i}.
$$

The receipt prints equal-split checks:

| independent reservoirs | tax / single-reservoir tax | tax density / E_spr[P_log2] |
|---:|---:|---:|
| 2 | 1.41421356237309504880169 | 110.031553177701910313443 |
| 4 | 2.0 | 155.608114792882465261138 |
| 16 | 4.0 | 311.216229585764930522277 |

So the moment witness is not automatically realizable by the naive sandwich construction. The same-`N` sandwich cannot fit the vertex budget, the relaxed sandwich pays too much low-interval tax, and splitting into independent complete sandwiches only worsens the bound. This does not prove that no poset can spoof the finite multi-alpha profile; it narrows the next adversarial problem:

> realize or rule out overlapping or staggered multi-thickness transitive posets whose interval histogram matches the tested profile without paying the independent-sandwich low-interval tax.

---

## 13. What still constrains the click law

The surviving constraint is not "the full click law must be exactly this marked point process." That would be too strong. The surviving constraint is:

> A scalar count law is too weak; any route that hopes to solve manifoldlikeness must control order-sensitive statistics beyond the scalar count.

The marked-compensator route would need at least three layers:

1. scalar projection:

   `N-A` martingale, with dense `A_chi=kappa chi`;

2. event-mark compensators:

   `xi_1(dchi,dm)-nu_1(dchi,dm)`;

3. pair/global statistic controls:

   compensators or concentration laws for `Z_n^phi`, ordering fractions, height, and related order statistics.

The predictable quadratic bracket

$$
\langle M^f,M^g\rangle
$$

is still a separate object. It may be needed to control fluctuations of event marks, but it is not derived from `P_alpha`. The receipt says that first-moment/dimension constraints are easy to spoof, that naive pair-density constraints are misnormalized, that single-alpha calibrated interval density catches only crude empty-interval excess, that a thin-middle non-manifold family can spoof `d_MM`, height, and one calibrated `rho_alpha`, that a wider calibrated generating-function profile rejects the tested transitive adversaries, and that finite alpha profiles remain underdetermined at the histogram level.

There are also non-marked routes. Causal-set work has long used covariant nonlocal layer kernels, such as Benincasa-Dowker-style d'Alembertian/action constructions, to build order-intrinsic dynamics without finite-neighbor locality. Those are not imported as SHARD results here, but they are the kind of alternative that should be compared with a marked-compensator route.

---

## 14. Hidden machines and cellular automata

Paper XX showed that deterministic hidden machines can realize the scalar record clock. Paper XXI then reframed the law as a record compensator. This paper adds only a conditional statement:

> Once a specific order-sensitive record law is stated, a hidden machine is admissible only if its record projection satisfies that law in the stated filtration and measure.

Before such a law is specified, there is no exclusion theorem against hidden variables, cellular automata, or deterministic machines.

After such a law is specified, matching the scalar count will not be enough. A deterministic machine that creates record-visible hazard aging, KR layering, wrong height scaling, or illegal order-statistic concentration would fail the order-sensitive projection. A deterministic machine whose projection matches the scalar, event-mark, pair/update, and terminal concentration laws would remain admissible.

So abandoning primitive stochastic processes does not weaken the target. It relocates the burden:

`hidden mechanism -> lawful record projection`.

---

## 15. Joint marked laws

Paper I's joint click-law residue asked whether a joint ledger has an irreducible mutual content term:

$$
\chi_{AB}.
$$

Receipt `p4a_joint_clicklaw.py` showed that the sequential exponential skeleton does not force additivity; a genuine mutual term can remain free under the guardrail.

The marked/order-sensitive problem is the natural place to revisit that residue. In a two-chain situation, candidate event marks include:

- chain label `A` or `B`;
- joint event label;
- local order relation between the two chains;
- mutual ledger increment;
- no-signaling guardrail data.

But manifoldlikeness is not built from isolated event marks alone. It is a correlated pattern of order relations. Therefore joint laws likely need pair/update statistics and cross-channel concentration controls as well.

The tension is real:

- too little joint structure permits KR-like or hidden long-range order while scalar counts remain correct;
- too much rigidity can collapse the mutual-content freedom from Paper I.

This remains one of the best next openings, but it is not solved here.

---

## 16. A finite penalty is still not the answer

One could package the first benchmark audit as a finite cost:

$$
C=c_1(d_{\mathrm{MM}}-2)^2+c_2(\beta_H-\tfrac12)^2+c_3\beta_P^2
+\operatorname{barriers}(P_\alpha=0\ \mathrm{or}\ P_\alpha=\infty).
$$

The receipt shows why that version is not the answer: it rejects the fixed 1+1 sprinkled stress sample. The repaired finite statistic replaces `beta_P` with the calibrated ratio

$$
\rho_\alpha=\frac{P_\alpha}{\mathbb{E}_{\mathrm{spr},N}[P_\alpha]}.
$$

That is a real improvement. It accepts the fixed sprinkling stress sample and rejects the crude bilayer-plus-chain adversary that matches MM and height. But it is still not the click law, and the thin-middle adversary shows that one calibrated alpha is not enough.

A real finite-order law would need at least:

- calibration on actual binomial/Poisson sprinklings;
- robustness against adversarial non-manifold families matching `d_MM`, height, `rho_alpha`, multi-`alpha` layer profiles, and eventually the full interval histogram or action-relevant equivalent, while respecting transitivity constraints;
- covariance-compatible layer or interval kernels;
- no finite-valency nearest-neighbor overclaim;
- a sequential or terminal probability/action interpretation;
- reduction to the scalar Paper XXI martingale under `f=1` or the corresponding scalar projection.

Until then, the finite penalty is an engineering stress test, not a foundational law. The calibrated `rho_alpha` statistic is a better third mark than grid tightness, the five-alpha generating-function profile is stronger, and the histogram moment construction shows why any finite profile remains incomplete.

---

## 17. One sufficient result for the marked-compensator route

For the marked-compensator route, a genuine unblocker would be a theorem of this form:

1. Start with the committed record filtration, scalar content `chi`, causal order, and admissible event/pair/global order statistics.

2. Require scalar compensator consistency, refinement consistency, joint guardrails, covariance-compatible order kernels, and concentration bounds.

3. Derive a unique or nearly unique family of event-mark and pair/statistic compensators.

4. Prove that typical finite orders under that law are manifoldlike, while KR-like and related non-manifold orders are suppressed.

5. Recover Paper XXI's scalar law as the scalar projection:

   `N_chi-kappa chi` in the dense simple regime.

This would remove manifoldlikeness as an external assumption for that route. But it is one possible route, not the only logically possible route. Terminal actions, covariant nonlocal order kernels, or matter-sector emergence could also carry the selection if they are made precise and pass the same hostile tests.

---

## 18. Precision receipt

The receipt `v7/code/p22_marked_manifold_audit.py` uses integer counts and mpmath ambient `dps=140`. No float64 arithmetic is used for asserted quantities. The fixed sprinkling stress sample is represented by random permutations of integer ranks, avoiding floating coordinate sampling. The exact finite-N expectation for `P_alpha` is an alternating sum with severe cancellation; it is evaluated with higher internal guard precision that scales with `N`, and downstream arithmetic and reporting consume it at the ambient receipt precision.

Executed checks:

- scalar compensator order-blind under the toy fixed-`chi=N` convention: pass;
- exact Myrheim-Meyer values `f(1)=1`, `f(2)=1/2`, `f(3)=8/35`, `f(4)=1/10`: pass;
- inverse returns `d=2` from `f(2)`: pass;
- deterministic 2D grid height exponent near `1/2`: pass;
- chain height exponent near `1`: pass;
- KR and antichain height exponent near `0`: pass;
- deterministic grid interval-damped pair density tight: pass;
- KR interval-damped pair density divergent: pass;
- antichain interval-damped pair density zero: pass;
- KR spoof has `p_star in (0,1)`: pass;
- KR spoof matches `f(2)` to receipt precision: pass;
- KR spoof has `d_MM=2` to receipt precision and `beta_H=0`: pass;
- retuned KR spoof still has divergent interval-damped pair density: pass;
- MM-only diagnostic is insufficient because spoofed KR passes: pass;
- pair-density-only diagnostic is insufficient because chain passes: pass;
- toy combined audit accepts the deterministic grid benchmark: pass;
- toy combined audit rejects chain, antichain, KR, and spoofed KR: pass;
- fixed sprinkled stress sample has MM dimension near `2` at largest `N`: pass;
- fixed sprinkled stress sample has height exponent near `1/2`: pass;
- naive tight pair-density threshold fails on fixed sprinkled stress sample: pass;
- toy audit is not a manifoldlikeness gate because it rejects the sprinkled stress sample: pass;
- calibrated sprinkled pair density `P_alpha/E_spr[P_alpha]` stays near `1`: pass;
- small sprinkling ensemble `rho_alpha` band stays near `1`: pass;
- bilayer-plus-chain adversary has MM dimension near `2` at `N=4096`: pass;
- bilayer-plus-chain adversary has height exponent `1/2`: pass;
- calibrated pair density rejects the crude MM+height adversary: pass;
- thin-middle adversary has MM dimension near `2` at `N=4096`: pass;
- thin-middle adversary has height `sqrt(N)` by construction: pass;
- thin-middle adversary spoofs single-alpha calibrated `rho_alpha`: pass;
- multi-alpha `rho_alpha` profile exposes the thin-middle adversary: pass;
- fixed sprinkled five-alpha generating profile stays near `1`: pass;
- five-alpha generating profile rejects the chain: pass;
- five-alpha generating profile rejects the bilayer-plus-chain adversary: pass;
- five-alpha generating profile rejects the thin-middle single-alpha spoof: pass;
- histogram moment adversary has positive weights: pass;
- histogram moment adversary matches all tested alpha moments: pass;
- histogram moment adversary preserves target related-pair count: pass;
- most histogram relation mass is hidden beyond tested interval scales: pass;
- finite five-alpha profile can be moment-spoofed to receipt precision: pass;
- complete-sandwich realization cannot fit the same-`N` vertex budget: pass;
- complete-sandwich realization of the hidden mass would create a huge low-interval tax: pass;
- independent split-sandwich reservoirs cannot lower the complete-sandwich tax bound: pass.

Final receipt line:

`CHECKS PASSED: 46/46`.

---

## 19. Claims and non-claims

**Claims.**

1. The scalar martingale is order-blind at fixed scalar content/count and cannot by itself solve manifoldlikeness. **[CONSTRAINED]**

2. Marked event compensators are the natural extension of Paper XXI, but pair/global manifoldlikeness diagnostics require additional statistic processes or terminal concentration/action laws. **[PRINCIPLE / OPEN]**

3. A KR expected family can be retuned to spoof the 2D Myrheim-Meyer ordering fraction to receipt precision while remaining height-collapsed and interval-density divergent. **[COUNTEREXAMPLE]**

4. MM-only and pair-density-only diagnostics are insufficient. **[COUNTEREXAMPLE]**

5. The first combined benchmark audit separates selected toy families but fails as a manifoldlikeness gate because it rejects a fixed 1+1 sprinkled stress sample. The calibrated ratio `rho_alpha=P_alpha/E_spr[P_alpha]` repairs that failure on the stress sample. **[STRESS TEST]**

6. A bilayer-plus-chain non-manifold family matches `d_MM -> 2` and `H ~ sqrt(N)` but is rejected by calibrated `rho_alpha` (`rho_alpha=79.942586373358417726` at `N=4096`). **[COUNTEREXAMPLE / STRESS TEST]**

7. A thin-middle three-layer-plus-chain non-manifold family matches `d_MM`, height, and `rho_(log 2)` at the tested scale; a small multi-alpha profile exposes it. **[COUNTEREXAMPLE / STRESS TEST]**

8. A wider five-alpha generating-function profile accepts the fixed sprinkling sample and rejects the tested chain, bilayer-plus-chain, and thin-middle transitive adversaries. **[STRESS TEST]**

9. A positive real-weight interval-size measure can match the tested five-alpha profile while hiding most relation mass at large interval size; finite alpha profiles are underdetermined at the histogram level. **[COUNTEREXAMPLE / OPEN]**

10. A naive complete-sandwich poset realization of that hidden histogram mass pays a large transitivity tax in low-interval relations, and splitting into independent complete-sandwich reservoirs only worsens the bound. Histogram moment matching is therefore not automatically a poset spoof; overlapping/staggered realizations remain open. **[STRESS TEST / OPEN]**

11. The valuable constraint is order-sensitivity beyond scalar count, not the specific finite penalty tested here. **[CONSTRAINED]**

**Non-claims.**

1. No theorem of manifoldlikeness is proved.

2. No unique marked compensator is derived.

3. No final probability law or action over finite orders is derived.

4. No Lorentz-invariant finite-neighbor graph is claimed; the BHS obstruction remains.

5. `P_alpha` is not a martingale bracket.

6. The deterministic `[n]x[n]` grid benchmark is not a Lorentz-covariant substrate proposal.

7. The KR spoof calculation is an expected-family calculation, not an exhaustive finite-poset enumeration.

---

## References

**Companion program.**

- *The record click-law, I* (v7) -- the original dense/sparse click-law and the joint click-law residue.
- *The record click-law, XI* (v7) -- order plus number, the `l_step` wall, and the manifoldlikeness gate.
- *The record click-law, XX* (v7) -- deterministic hidden machines can realize the scalar record-facing click law.
- *The record click-law, XXI* (v7) -- the scalar record martingale principle `N-A`.
- `note-C2-covariance-premise-deferral.md` -- the BHS no-finite-valency obstruction and the point-locality/covariance deferral.
- `v7/code/p4a_joint_clicklaw.py` -- joint click-law residue and mutual content.
- `v7/code/p22_marked_manifold_audit.py` -- high-precision receipt for this paper.

**External.**

- L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, *Space-time as a causal set*, Phys. Rev. Lett. 59, 521 (1987) -- order plus number as geometry.
- D. Malament, *The class of continuous timelike curves determines the topology of spacetime*, J. Math. Phys. 18, 1399 (1977); S. W. Hawking, A. R. King, P. J. McCarthy, J. Math. Phys. 17, 174 (1976) -- causal order determines conformal structure under manifold hypotheses.
- J. Myrheim, CERN preprint TH-2538 (1978); D. Meyer, *The dimension of causal sets* (PhD thesis, MIT, 1988) -- dimension from ordering fraction.
- D. Kleitman, B. Rothschild, *Asymptotic enumeration of partial orders on a finite set*, Trans. Amer. Math. Soc. 205, 205 (1975) -- dominance of three-layer partial orders.
- A. Bombelli, J. Henson, R. D. Sorkin, *Discreteness without symmetry breaking: a theorem*, Mod. Phys. Lett. A 24, 2579 (2009) -- Lorentz invariance of sprinklings and the no-finite-valency obstruction.
- D. M. T. Benincasa, F. Dowker, *Scalar Curvature of a Causal Set*, Phys. Rev. Lett. 104, 181301 (2010), https://arxiv.org/abs/1001.2725 -- nonlocal retarded order kernels and causal-set action route.
- F. Dowker, L. Glaser, *Causal set d'Alembertians for various dimensions*, https://arxiv.org/abs/1305.2588 -- dimension-dependent Lorentz-invariant causal-set d'Alembertian kernels.
- D. P. Rideout, R. D. Sorkin, *Classical sequential growth dynamics for causal sets*, Phys. Rev. D 61, 024002 (2000) -- causal-set dynamics and the selection problem.
