# Critique of "Non-Markovian Gravitational Decoherence from Indivisible Stochastic Processes"

Preprint, not peer reviewed, version 2026-06-02.

## Overall assessment

This is a promising foundations/phenomenology manuscript, but it is not yet strong enough as a standalone physics paper. Its best version is a narrower paper: **a non-Markovian generalization of Diósi-Penrose gravitational decoherence with a proposed onset-shape discriminator**. Its weakest current form is as a claim that ISP itself derives a parameter-free Gaussian law at the DP energy scale.

Recommendation in referee language: **major revision before journal submission**. The central idea is interesting, the writing is clear, and the numerical threshold table is internally consistent, but the manuscript currently overclaims the derivation, the fit-free status, and the specificity to ISP.

## Main strengths

1. **Clear physical target.** The paper identifies a real pressure point in DP-style gravitational decoherence: the exponential law is tied to Markovian/white-noise dynamics.

2. **Good experimental instinct.** Framing the test around the onset shape of residual log-coherence is the right move. Linear-vs-quadratic onset is a cleaner observable than trying to infer a single collapse rate.

3. **Honest scope in several places.** The paper repeatedly admits that the quadratic onset is generic to non-Markovianity and not unique to ISP. That honesty helps.

4. **Numerical threshold table checks out.** Using the stated saturated self-energy formula and rho = 2000 kg m^-3, the masses/radii in Section 6 are consistent.

## Major issues

### 1. Indivisibility does not yet derive the decoherence law

The paper moves from "the underlying process is indivisible" to a colored-noise decoherence functional, then to a Gaussian onset. But the missing step is the most important one: **why does Barandes-style indivisibility imply this particular positive decoherence kernel for gravitational record mismatch?**

As written, ISP motivates non-Markovianity, but it does not derive:

- a stochastic variable delta E(t),
- its covariance K(s),
- why K is positive and stationary,
- why the coherence functional is the standard second-cumulant expression,
- why sigma_E should be of order E_G,
- why the channel is decohering rather than merely producing non-Markovian phase noise.

Without that bridge, the paper reads as "if gravitational DP noise is non-Markovian, the onset is Gaussian", not "ISP predicts this law."

What to add: an explicit minimal stochastic model or proposition:

```text
Given an ISP transition kernel with record-memory correlation K_rr'(t,t'), the branch coherence obeys ...
```

Then prove the Gaussian onset from that model. Even a toy model would help.

### 2. The Markovian limit and Gaussian coefficient are not normalized consistently

Section 4 uses

```text
Gamma(T) = (1 / 2 hbar^2) int_0^T int_0^T K(t1 - t2) dt1 dt2
K(s) = sigma_E^2 exp(-|s|/tau_c)
```

This gives, for long times,

```text
Gamma(T) ~ (sigma_E^2 tau_c / hbar^2) T.
```

To recover DP,

```text
Gamma(T) = (E_G / hbar) T,
```

one must impose

```text
sigma_E^2 tau_c = E_G hbar.
```

But the pure Gaussian result later sets sigma_E ~ E_G, which implies tau_c ~ hbar / E_G = tau_G. These are compatible only for a particular choice of tau_c, not for an arbitrary tau_c -> 0 Markov limit.

So the statement "DP is recovered as tau_c -> 0" is not true with fixed sigma_E = E_G. In that limit, the long-time slope goes to zero. To get a white-noise limit, the kernel amplitude must scale like 1/tau_c.

This is the paper's most important technical fix.

Possible repair:

- Choose a normalized memory kernel

```text
K_tau(s) = (hbar E_G / tau_c) f(|s|/tau_c)
```

with integral fixed so the long-time DP rate is recovered.

- Then the short-time Gaussian coefficient becomes proportional to E_G / (hbar tau_c), not simply 1/tau_G^2.

That would make the paper less parameter-free, but more correct.

### 3. "Fit-free" is overclaimed

The onset-shape test can be fit-light, but not fully fit-free.

The experiment still needs to determine:

- the environmental subtraction,
- the residual gravitational channel,
- the relevant E_G for realistic extended bodies,
- the memory time tau_c or at least the regime T << tau_c,
- the coefficient of the quadratic onset if sigma_E is not exactly E_G.

The shape-only claim is defensible:

```text
linear onset vs zero-slope quadratic onset is a qualitative discriminator
```

The stronger claim

```text
C(T) = C(0) exp[-1/2 (T/tau_G)^2]
```

is not fit-free unless the paper derives sigma_E = E_G and tau_c >= T from ISP.

### 4. The paper cannot claim that the two-axis test singles out ISP

The table in Section 5 is useful, but the line saying the ISP cell is unique is too strong. A non-Markovian gravitational collapse model could occupy exactly the same cell:

```text
Gaussian/non-Markovian onset + gravitational E_G scaling
```

The manuscript says such a model is "ISP under another name", but a referee will not accept that without a theorem showing equivalence. Better:

```text
This cell supports the ISP-motivated non-Markovian gravitational-channel hypothesis, but does not uniquely establish ISP.
```

This adjustment preserves the value of the test while avoiding a vulnerable claim.

### 5. The tau_c argument is dimensional, not predictive

Section 7 says tau_c ~ tau_G because "division = stabilization." This is suggestive, but not a derivation. The table of possible tau_c scales is good, but it means tau_c is a new physical parameter.

The paper should state earlier:

```text
ISP motivates a finite memory time tau_c; this paper explores the consequences of tau_c in the experimentally relevant range.
```

Then the paper can present tau_c ~ tau_G as a natural ansatz, not as something fixed by the theory.

### 6. The radiation-bound section is too rhetorically strong at the end

The paper is careful in Section 8, then ends with:

```text
non-observation of collapse radiation mildly favours the large-tau_c branch
```

This is not secure. If the Adler/Bassi/Donadi zero-frequency argument applies, quasi-static noise may not help. The safer conclusion:

```text
The radiation bound does not straightforwardly decide the non-Markovian case; a dedicated emission calculation for this kernel is needed.
```

Avoid saying the bound favors your branch unless you compute the emission rate for your actual kernel and mass-density smearing.

### 7. Experimental feasibility is underdeveloped

"Accessible now" is too optimistic. The thresholds are useful, but they are not an experimental error budget.

A referee will want:

- required visibility precision,
- required number of T points near onset,
- environmental decoherence slope and curvature,
- whether varying d changes environmental noise,
- whether the E_G -> 0 control really keeps the same pulse sequence and heating,
- realistic coherence times for the listed platforms,
- finite-size and geometry corrections beyond the saturated/harmonic limits.

The paper should soften "accessible now" to "targets the same parameter range pursued by current and proposed platforms."

## Suggested restructure

### Better title

Current title is too long and overcommits. A stronger title:

```text
Non-Markovian Onset in Gravitational Decoherence: A Gaussian Alternative to the Diósi-Penrose Exponential
```

Mention ISP in the subtitle or introduction, not necessarily in the title.

### Better core claim

Replace:

```text
ISP predicts C(T)=C(0) exp[-1/2(T/tau_G)^2].
```

with:

```text
An ISP-motivated finite-memory gravitational record channel generically replaces the Markovian DP linear log-decay by a quadratic short-time onset. If the mismatch-energy fluctuation scale is E_G and the memory time is at least of order tau_G, the onset takes the Gaussian form C(T) ~ C(0) exp[-1/2(T/tau_G)^2].
```

This is less flashy, but much more publishable.

### Add a model section

Before the current Section 4, add a short section:

```text
Minimal finite-memory gravitational record model
```

Define:

- branch label r,
- gravitational record variable X_r(t),
- energy mismatch delta E_rr'(t),
- covariance K_rr'(t,t'),
- assumptions needed for Gaussian cumulant truncation,
- relation to E_G.

Then derive the decoherence functional.

### Fix the kernel normalization

Choose one of two routes:

1. **DP-normalized colored kernel**

Keep the long-time DP rate fixed. Then the short-time coefficient depends on tau_c.

2. **ISP-amplitude kernel**

Set sigma_E = E_G. Then admit DP is recovered only for tau_c = tau_G in the long-time slope, not as tau_c -> 0 with fixed amplitude.

Route 1 is more conventional. Route 2 is more ontological but must be stated honestly.

## Publishability judgement

As currently written, the paper is likely to face desk rejection or a severe referee report if sent to a mainstream physics journal, because the central derivation is under-specified and the parameter-free claim is not technically stable.

With revision, it could become a credible short theoretical/phenomenological paper if narrowed to:

```text
Finite-memory gravitational decoherence has a quadratic onset; this gives a clean experimental discriminator against strict Markovian DP/CSL. ISP supplies one motivation for such finite memory.
```

That version is much harder to dismiss.

## Priority revision checklist

1. Fix the K(s) normalization and the tau_c -> 0 limit.
2. Downgrade "parameter-free" and "fit-free" to "shape-based" unless sigma_E = E_G is derived.
3. Recast ISP as motivation unless a concrete ISP-to-kernel derivation is added.
4. Remove or soften claims that the two-axis test uniquely identifies ISP.
5. Replace "accessible now" with a quantified feasibility paragraph.
6. Add a dedicated emission-rate caveat for the spontaneous-radiation bound.
7. Update the literature around colored CSL, non-Markovian collapse, and recent mesoscopic interferometry proposals before submission.

## Bottom line

The paper has a publishable seed: **linear DP onset versus quadratic finite-memory onset is a clean and interesting discriminator**. The current manuscript should stop trying to prove too much from indivisibility alone. Make it a disciplined finite-memory gravitational-decoherence paper, with ISP as the ontology that motivates the memory, and it becomes much stronger.
