# Fourth Review of "Non-Markovian Gravitational Decoherence"

Preprint, not peer reviewed, version 2026-06-02.

## Referee-style verdict

**Recommendation: minor-to-major revision before submission; suitable for preprint circulation after tightening.**

This draft has crossed an important threshold. It now reads less like an overextended claim that ISP derives a new collapse law, and more like a coherent phenomenological paper: the Diósi-Penrose exponential is identified as a white-noise limit, finite memory produces a quadratic onset, and ISP is presented as a motivation for the finite-memory channel rather than as a completed microscopic derivation.

That is the right paper. The remaining problem is not that the argument is confused; it is that the manuscript still sometimes advertises a stronger result than it actually proves. A publishable version should make the hierarchy almost impossible to miss:

```text
finite memory -> zero initial slope / quadratic log-coherence onset
DP energy scale -> inherited gravitational normalization
tau_c ~ tau_G and sigma_E ~ E_G -> benchmark Gaussian-onset model
ISP -> motivation for finite record memory, not yet a derivation of K(s)
```

If the paper maintains that discipline throughout, it becomes a credible foundations/phenomenology manuscript.

## What now works well

The technical center of the paper is now Section 4, and it mostly succeeds. The assumptions M1-M3 are explicit, the decoherence functional is standard, and the introduction of the noise power

```text
D_E = sigma_E^2 tau_c
```

makes the Markovian limit intelligible. The paper correctly distinguishes the fixed-power white-noise limit from the fixed-amplitude limit, which was the most important normalization issue.

Section 4.2 is especially helpful. The distinction between generic finite-memory onset, benchmark closure, and benchmark prediction is exactly the conceptual architecture the paper needed. This section should be treated as the controlling statement of the whole manuscript.

The experimental section is also much improved. The visibility table gives the reader a concrete sense of the difference between

```text
exp(-T/tau_G)
```

and

```text
exp[-(1/2)(T/tau_G)^2].
```

The claim is no longer just "measure the shape"; it now says where the curves separate and what kind of visibility precision would matter. That makes the proposal feel less decorative and more operational.

The discussion of spontaneous radiation is now appropriately cautious. The paper no longer claims that finite memory evades existing DP bounds. It instead says the issue is undecided without a dedicated emission calculation, which is the scientifically defensible position.

## Main remaining weaknesses

### 1. The title still promises more ISP than the paper delivers

The subtitle says:

```text
An indivisible-stochastic-process motivation and a shape-based interferometric test
```

This is accurate. The main title, however, foregrounds "Non-Markovian Gravitational Decoherence" and the abstract quickly moves into ISP. The problem is not the title itself, but the reader may still expect an ISP-derived kernel. The paper later admits that the kernel is not derived. That admission is honest, but it should appear even earlier and more bluntly.

Suggested abstract-level wording:

```text
We do not derive the gravitational noise kernel from ISP. We use ISP as a motivation for replacing the DP white-noise channel by a finite-memory channel, then study the resulting onset shape.
```

That sentence would prevent the most predictable referee objection.

### 2. "Any such finite-memory noise" is too broad

The abstract says that any such finite-memory noise generically replaces the DP exponential with a non-exponential coherence decay whose short-time exponent is quadratic. This is nearly right, but it is too broad unless the required regularity assumptions are named.

The result needs finite, nonsingular covariance near the origin and no residual white component. If the noise has both colored and delta-correlated pieces, the initial slope need not vanish. If the covariance is singular or the process is nonstationary, the short-time expansion may not have the simple quadratic form.

Suggested repair:

```text
For a finite, regular covariance with no delta-correlated component, the short-time exponent is quadratic.
```

This is less sweeping and more referee-proof.

### 3. The benchmark closure remains the most vulnerable point

The paper now calls

```text
sigma_E ~ E_G,     tau_c ~ tau_G
```

a benchmark closure and an ansatz. Good. But the conclusion still says the new time scale `tau_c` is "fixed dimensionally to the order of tau_G." That sounds stronger than the discussion justifies.

Dimensional analysis does not fix a scale; it proposes a natural scale once one decides which physical quantity is controlling the channel. Section 7 itself lists three possible scales: `tau_G`, the gravitational dynamical time, and `R/c`. That means `tau_c ~ tau_G` is preferred by the paper's interpretation, not fixed by the theory.

Suggested conclusion wording:

```text
The benchmark model identifies tau_c with the DP time tau_G; other choices interpolate between a visibly non-Markovian onset and the Markovian DP limit.
```

That wording preserves the proposal without overselling the derivation.

### 4. The "maximally indivisible" limit needs caution

Section 4.1 says that `tau_c -> infinity`, with no internal decorrelation, is the natural meaning of a single indivisible transition over the hold. This is evocative, but it may be too strong. Indivisibility is failure of Chapman-Kolmogorov factorization; it does not automatically mean an infinite correlation time or a constant covariance over the whole hold.

The constant-kernel limit is a useful limiting model, but the paper should not imply that this is the literal mathematical content of indivisibility.

Suggested wording:

```text
As an idealized fully correlated limit over the experimental hold time...
```

instead of "the natural meaning."

### 5. The experimental discriminator still needs the log-coherence version of the table

The visibility table is useful, but the paper defines the residual observable as

```text
L(T) = ln[V(T) / V_env(T)].
```

Then the table compares raw visibility curves. That is fine for intuition, but the actual discriminator is the leading power of the residual log-coherence:

```text
L_exp = -x
L_Gauss = -x^2 / 2
```

The paper should add either a second small table or one line below the visibility table showing the log-coherence difference:

```text
Delta L = x - x^2/2.
```

This matters because experimental noise is often analyzed in log visibility, not visibility itself. It would align the quantitative example with the defined observable.

### 6. The finite-size energy formula section is too compressed

Section 6 gives saturated and harmonic formulas for a homogeneous sphere. That is useful, but a referee may ask how `E_G(d)` transitions between the two regimes and whether the proposed `d`-variation campaign can actually map the scaling without entering ambiguous geometry.

The paper does not need a full appendix, but it should add a sentence saying that realistic predictions must compute `E_G(d)` numerically from the actual mass density and branch geometry. The table is an order-of-magnitude threshold table, not a platform-specific prediction.

Suggested insertion:

```text
For an actual experiment the self-energy should be evaluated with the measured density profile and branch geometry; the two formulas above are limiting estimates used only to locate the relevant mass-time scale.
```

### 7. The references are now the largest practical submission weakness

The manuscript has a respectable core bibliography, but it still reads under-referenced for a paper claiming contact with current and proposed platforms. The references lean heavily on older foundational and review sources. Before journal submission, the paper needs a more current map of:

- recent levitated optomechanics and nanosphere-interferometry proposals,
- current macroscopic-superposition bounds,
- colored CSL and non-Markovian collapse phenomenology,
- DP regularization/smearing and radiation constraints,
- matter-wave interferometry beyond the older macroscopicity review.

This is now probably the easiest way to improve perceived seriousness. The physics argument has become clearer; the literature embedding has not caught up.

## Specific comments

### Abstract

The abstract is strong, but dense. It tries to do title, model, result, experiment, radiation bound, and caveat all at once. Consider shortening it by removing platform names and moving them to Section 6. The most important abstract message is:

```text
DP exponential = white-noise limit.
Finite memory = quadratic onset.
Benchmark ISP-motivated closure = Gaussian onset at tau_G.
Test = residual log-coherence shape plus E_G scaling.
```

Everything else can wait.

### Section 3

The Cauchy argument is acceptable now because the text says it is not the historical DP derivation. Still, it occupies conceptual space that may distract from the actual stochastic-kernel model. If the paper becomes too long, this is the first material I would move to an appendix.

### Section 4

This is the best section and should be protected from rhetorical inflation elsewhere. The sentence "Only M3 is ISP's" is excellent. The paper should echo that exact clarity in the abstract and conclusion.

### Section 5

The two-axis test is now fair. The honest-limits paragraph does important work and should stay. The only remaining issue is that environmental subtraction is still described at the level of principle. A future version should specify how many independent `d` values, how many `T` values, and what scaling residual would count as failure.

### Section 7

The phrase "division = stabilization" is a useful intuition, but it is not a derivation. Treat it as motivation for the benchmark model. Avoid saying that it fixes `tau_c`.

### Section 8

This section is now appropriately modest. Keep the "no exclusion claim" language. It is one of the most important credibility moves in the manuscript.

## Suggested final framing

The paper should present itself with this central claim:

```text
If the DP gravitational decoherence channel is not white-noise Markovian but has finite record memory, then the residual gravitational log-coherence has zero initial slope. An ISP ontology motivates such finite memory. The simplest DP-scale closure gives a Gaussian-onset law at tau_G, experimentally distinguishable from the Markovian DP exponential by shape and E_G scaling.
```

That claim is publishable in spirit because it is precise, falsifiable, and honest about what is assumed.

The claim to avoid is:

```text
ISP predicts a parameter-free Gaussian replacement for DP.
```

The manuscript mostly avoids this now, but a few phrases still drift in that direction.

## Bottom line

This is now a strong draft for a speculative preprint. For journal submission, I would require one more revision focused on:

1. tightening abstract and conclusion language around what ISP does and does not derive;
2. qualifying the "any finite-memory noise" statement with regularity/no-white-component assumptions;
3. softening the claim that `tau_c` is fixed to `tau_G`;
4. aligning the quantitative experimental example with residual log-coherence;
5. expanding and updating the bibliography.

The core idea is no longer the weak point. The weak point is presentation discipline: the paper must keep saying exactly what it has actually shown, even when the more dramatic sentence is tempting.
