# Second Review of "Non-Markovian Gravitational Decoherence"

## Referee-style verdict

**Recommendation: major revision, but substantially improved.**

This version is much stronger than the earlier framing. The title is cleaner, the abstract now admits that ISP motivates rather than derives the kernel, the white-noise limit is handled more correctly, and the spontaneous-radiation discussion is appropriately cautious. The manuscript is now close to being a coherent *phenomenological proposal*.

It is still not yet publishable as a standalone theoretical physics paper, because the central mechanism remains under-derived. The paper now says the right modest things in many places, but the mathematical body still has stronger claims than the derivation supports. The manuscript should either add a concrete model connecting ISP to the kernel, or explicitly reframe itself as a finite-memory DP phenomenology with ISP as one motivation.

## Summary of the paper

The paper argues that the standard Diósi-Penrose exponential decoherence law is the Markovian/white-noise limit of a broader gravitational decoherence channel. If the gravitational record-mismatch noise has a finite correlation time, the short-time log-coherence is quadratic rather than linear. At a proposed self-consistent point, with memory time `tau_c ~ tau_G = hbar/E_G` and energy fluctuation scale `sigma_E ~ E_G`, the onset becomes approximately

```text
C(T) = C(0) exp[-1/2 (T/tau_G)^2],
```

with a later DP-slope exponential tail. The proposed experimental discriminator is the onset shape of residual gravitational log-coherence after environmental subtraction.

## What improved

1. **The title is now much better.** The previous title overcommitted to ISP. The current title foregrounds non-Markovian gravitational decoherence, which is the actual defensible contribution.

2. **The abstract is more honest.** It now says indivisibility motivates finite memory rather than directly deriving the noise kernel.

3. **The kernel normalization issue is partly fixed.** Section 4.1 now correctly states that the DP limit requires `tau_c -> 0` at fixed noise power `sigma_E^2 tau_c`, not fixed amplitude.

4. **The radiation-bound discussion is improved.** The manuscript no longer claims a clean evasion of Donadi et al.; it acknowledges the zero-frequency issue and calls for a dedicated emission-rate calculation.

5. **The discussion section now contains the right caveats.** Especially useful is the explicit statement that the clean Gaussian-onset/DP-tail picture holds at a self-consistent ansatz point, not as a theorem.

## Remaining major problems

### 1. The paper still lacks a derivation from ISP to a decoherence kernel

The central missing bridge remains:

```text
ISP indivisibility -> finite-memory stochastic gravitational record channel -> positive decoherence kernel K(s)
```

The paper says ISP motivates finite memory, but a skeptical referee will ask why an indivisible stochastic process should produce this particular kind of Gaussian cumulant dephasing. Non-divisibility alone does not imply:

- a stationary autocorrelation function `K(t1 - t2)`,
- Gaussian statistics,
- a second-cumulant truncation,
- positive monotone decoherence,
- an energy-noise variable `delta E(t)`,
- the amplitude estimate `sigma_E ~ E_G`,
- or a gravitational record channel rather than non-Markovian unitary phase evolution.

This is the paper's main publishability blocker.

Minimum repair: add a "minimal model" section that defines the stochastic record variable and derives the coherence functional from it. The model can be phenomenological, but it must be explicit enough that a reader can see which assumptions are doing the work.

### 2. The "self-consistent point" is still too convenient

The revised paper proposes:

```text
tau_c ~ tau_G
sigma_E ~ E_G
```

This makes the noise power

```text
sigma_E^2 tau_c ~ E_G hbar,
```

which recovers the DP long-time slope. That is elegant. But it is currently a dimensional closure, not a physical derivation.

The paper should not call this "the physically natural ISP prediction" unless it can explain why ISP selects these two scalings. As written, the point looks chosen because it gives the desired result: Gaussian onset at the DP time and DP-slope tail.

Better wording:

```text
A particularly simple closure, sigma_E ~ E_G and tau_c ~ hbar/E_G, preserves the DP long-time slope while replacing the onset by a Gaussian. We treat this as the benchmark finite-memory model.
```

That would be honest and still useful.

### 3. "Requires no fitted constant" remains overstated

The manuscript now uses "shape-based", which is good, but the abstract still says the distinction "requires no fitted constant", and Section 5 says the test does not require knowing `tau_G` in advance.

A real experiment will still need to fit or infer:

- environmental visibility loss,
- residual baseline drift,
- the curvature of `L(T)`,
- the range where `T << tau_c`,
- whether `sigma_E ~ E_G`,
- the finite-size/geometry value of `E_G`,
- and the statistical difference between a small linear slope and a small quadratic curvature.

The discriminator is not parameter-free; it is **less dependent on absolute rate calibration** than a one-rate collapse search.

Suggested replacement:

```text
The onset-shape test is rate-robust: it compares the leading power of T rather than relying only on an absolute collapse-rate fit.
```

### 4. The theorem-like Cauchy argument is too clean for DP

Section 3 derives an exponential from time multiplicativity and cost additivity. This is pedagogically nice but slightly artificial. DP is not normally introduced as a Cauchy functional equation over a survival factor; it is derived from a Lindblad/master-equation structure or stochastic potential model.

The argument is acceptable as intuition, but the paper should not imply that this is the actual DP derivation. It should add a sentence:

```text
This functional argument is not meant as a derivation of DP, but as a way of isolating the semigroup assumption behind any exponential survival law.
```

That will prevent a referee from attacking a straw-DP presentation.

### 5. The non-Markovian environmental control is still too abstract

The paper correctly says environmental non-Markovianity must be controlled, but this is not enough for a standalone experimental proposal. Since the core observable is a quadratic short-time onset, ordinary residual environmental memory is a direct false positive.

The paper needs a concrete control strategy:

- vary separation `d` while keeping pulse sequence, mass, charge state, trap history, and thermal conditions fixed;
- show that the residual curvature scales as the DP self-energy, not as optical intensity, gas pressure, trap noise, or blackbody emission;
- include a null geometry where `E_G` changes little but electromagnetic/control noise changes similarly;
- specify what is subtracted and what is not.

Without this, Section 5 is a concept, not yet an experimental discriminator.

### 6. The table still risks overstating uniqueness

The paper now says the two-axis result supports the ISP-motivated hypothesis "without uniquely establishing ISP", which is good. But the table still presents ISP as a theory cell and says "ISP occupies a cell that no other named theory does."

This can be softened further. The actual cell is:

```text
finite-memory gravitational collapse/decoherence channel
```

ISP is one motivation for that cell. A future non-Markovian gravitational collapse model could occupy it without being equivalent to ISP.

Suggested table row:

```text
ISP-motivated finite-memory gravitational channel | yes | Gaussian/non-Markovian | gravitational E_G
```

That phrasing is safer.

### 7. The references are thin for a submission

The reference list is respectable but not enough for a publishable manuscript in this area. It needs more direct engagement with:

- DP regularization and smearing choices,
- non-Markovian collapse models,
- colored CSL phenomenology,
- master-equation derivations of DP,
- recent optomechanical and levitated tests after the older Arndt/Hornberger and Marshall references,
- current bounds on CSL/DP parameters.

This is not just cosmetic. Several of the paper's claims live in an active literature where the details matter.

## Technical comments

### Kernel normalization

The revised text correctly distinguishes fixed-amplitude and fixed-noise-power limits. However, the notation still invites confusion:

```text
K(s) = sigma_E^2 exp(-|s|/tau_c)
```

then later:

```text
white-noise limit K -> 2 sigma_E^2 tau_c delta
```

If `sigma_E` changes with `tau_c`, call the fixed power something else, e.g.

```text
D_E = sigma_E^2 tau_c
```

Then write:

```text
K_tau(s) = (D_E/tau_c) exp(-|s|/tau_c)
```

or with the factor of 2 convention chosen explicitly. This will make the Markovian limit transparent.

### Factor-of-two convention

For `K(s)=sigma_E^2 exp(-|s|/tau_c)`,

```text
int_0^T int_0^T K(t1-t2) dt1 dt2
= 2 sigma_E^2 tau_c^2 (T/tau_c - 1 + exp(-T/tau_c)).
```

With the prefactor `1/(2 hbar^2)`, the paper's expression for `Gamma(T)` is correct. But in the white-noise statement, be explicit about whether `K -> 2D_E delta(s)` or `K -> D_E delta(s)`, because this fixes whether `D_E = E_G hbar` or `D_E = E_G hbar / 2`.

### Use of "Gaussian"

Strictly, the short-time *exponent* is quadratic. The coherence is Gaussian in time only over the onset regime or in the constant-kernel limit. The abstract mostly handles this, but the title and boxed equation may still encourage readers to think the whole law is Gaussian. Consider calling it "Gaussian-onset" everywhere.

### E_G controls phase as well as decoherence

The manuscript distinguishes unitary gravitational phase from gravitational record stabilization, which is good. But the model should explain why the same `E_G` enters the decohering noise amplitude rather than only the relative phase. This is currently inherited from DP, not derived.

## Minor comments

1. Replace "needs no fitted rate" with "does not rely only on an absolute rate fit."

2. In the abstract, "confirms a non-Markovian fundamental channel" is too strong. Observing a quadratic residual after subtraction would be evidence for such a channel, not confirmation.

3. "Real physical noise is never white" is rhetorically true but imprecise. Effective white-noise descriptions are standard and often valid. Say "white noise is an idealization."

4. The phrase "division events are the natural locus of effective measurement and record formation" needs either a citation to Barandes or a softer wording.

5. The experimental thresholds should state that they are order-of-magnitude DP-energy thresholds, not full feasibility estimates.

6. Section 8 should not say "one expects radiation to be strongly suppressed" without immediately saying that this expectation is challenged by zero-frequency emission calculations. The later caveat helps, but the first statement still sounds too confident.

7. The conclusion still says "free of fitted constants." Soften it.

## Recommended revision strategy

The most publishable version would be structured as:

1. DP exponential as Markovian/white-noise benchmark.
2. General finite-memory gravitational record kernel.
3. Derivation of quadratic onset and DP-normalized colored kernel.
4. Benchmark ansatz: `tau_c ~ tau_G`, `sigma_E ~ E_G`.
5. Experimental onset-shape discriminator and scaling campaign.
6. Bounds, limitations, and what ISP adds.

In that structure, the paper does not have to prove ISP. It only has to show that finite-memory gravitational decoherence is a meaningful alternative to strict DP and that ISP makes such finite memory conceptually natural.

## Revised publishability judgement

Compared with the earlier version, this manuscript has moved from "likely desk rejection" to "potentially viable as a speculative phenomenology paper after another serious revision." It is not yet suitable for a high-selectivity journal, but it could become plausible for a foundations-oriented or open theoretical physics venue if the claims are narrowed and the kernel model is made explicit.

The core paper should not be sold as:

```text
ISP predicts the DP-scale Gaussian law.
```

It should be sold as:

```text
Finite-memory gravitational decoherence replaces the DP linear onset by a quadratic onset; ISP motivates such finite memory, and the resulting shape/scaling test is experimentally meaningful.
```

That is a real, defensible contribution.

## Bottom line

The manuscript is now pointed in the right direction. The central insight is good: **the onset shape is where Markovian DP and finite-memory gravitational decoherence differ most cleanly**. The next revision should make the model less rhetorical and more mathematical. Define the kernel, define the assumptions, name the benchmark ansatz, and stop just short of claiming that ISP uniquely predicts it. That version will be much harder for a referee to dismiss.
