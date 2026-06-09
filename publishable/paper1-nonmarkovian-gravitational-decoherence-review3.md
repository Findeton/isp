# Third Review of "Non-Markovian Gravitational Decoherence"

## Overall verdict

This version is much closer to a publishable standalone paper. The manuscript now presents its core claim as a finite-memory, phenomenological alternative to the strict Diósi-Penrose exponential, rather than as a completed derivation of a new gravitational decoherence law from first principles. That is the right direction. The distinction between a white-noise Markovian limit and a finite-correlation-time channel is now clear, and the minimal model in Section 4 gives the reader a concrete mathematical object to assess.

My recommendation remains **major revision**, but the reason has changed. Earlier versions needed conceptual repair. This version mostly needs calibration: it should more carefully separate universal consequences of finite memory, benchmark assumptions, and genuinely ISP-specific content. With that separation made explicit, the paper could become a credible speculative phenomenology paper suitable for preprint circulation and later submission to a foundations or quantum-gravity phenomenology venue.

## Main strengths

The paper's strongest improvement is that it no longer treats the Gaussian law as if it were directly forced by indivisibility alone. The revised framing makes clear that finite memory modifies the short-time behavior of the decoherence exponent, while the specific Gaussian benchmark follows after additional assumptions about the noise amplitude and correlation time. That distinction makes the paper substantially more defensible.

Section 4 is now the technical center of the manuscript. The assumptions M1-M3 are legible, and the use of

```text
D_E = sigma_E^2 tau_c
```

clarifies how the Markovian Diósi-Penrose limit is recovered. This is a real improvement. The discussion of the white-noise limit also now correctly shows that keeping the Markovian rate fixed while sending the correlation time to zero requires an increasingly singular noise amplitude. That makes the mathematical idealization visible instead of hiding it inside terminology.

The experimental section is also better. The proposed discriminator is now framed as a shape test in time and geometry, rather than as a single absolute-rate comparison. That is the right experimental instinct: if the paper's claim survives, it will survive through a pattern of visibility decay, not through one number.

The radiation discussion is more careful than before. The manuscript no longer leans too heavily on a simple quasi-static suppression argument and now admits that a dedicated radiation calculation would be needed before claiming safety from known constraints.

## Remaining publication blockers

### 1. The ISP content is still under-derived

The main remaining issue is that ISP motivates the finite-memory assumption, but does not yet derive the kernel. In Section 4, the actual mathematical assumptions are:

```text
M1: Gaussian stationary noise
M2: amplitude set by E_G
M3: finite memory
```

Only M3 is distinctively ISP-motivated. M1 is a common modeling choice, and M2 inherits the Diósi-Penrose energy scale rather than deriving it from ISP. This is acceptable if the paper is explicit that the model is an ISP-motivated finite-memory completion of DP phenomenology. It is not acceptable if the paper implies that ISP uniquely predicts the Gaussian kernel.

Recommended fix: add a short paragraph near the end of Section 4 saying exactly what is derived, what is inherited, and what is assumed. For example:

```text
The model should therefore be read as a finite-memory DP-family phenomenology motivated by ISP, not as a first-principles derivation of the memory kernel from ISP dynamics.
```

That sentence, or something close to it, would remove a lot of possible reviewer resistance.

### 2. The benchmark closure is still too central

The relation

```text
sigma_E ~ E_G,     tau_c ~ tau_G
```

is now presented more honestly, but the paper still gives the boxed Gaussian law too much status. The most general finite-memory result is not the Gaussian with timescale `tau_G`; it is the quadratic onset with a timescale determined by both `sigma_E` and `tau_c`. The Gaussian form at `tau_G` is a benchmark closure.

Recommended fix: present the hierarchy explicitly:

```text
Generic finite-memory consequence:
  chi(T) = (sigma_E^2 / 2 hbar^2) T^2 + O(T^3)

Benchmark closure:
  sigma_E ~ E_G and tau_c ~ hbar / E_G

Benchmark prediction:
  C(T) ~ exp[-1/2 (T / tau_G)^2]
```

This would make the paper harder to misread and easier to defend.

### 3. The abstract still overclaims "no fitted constant"

The abstract says the distinction requires no fitted constant. This is still too strong. The comparison is rate-robust, but the finite-memory model contains a memory time and an amplitude scale. Even if the benchmark choice identifies both with `E_G`, that is still a modeling closure, not the absence of a parameter.

Recommended fix: replace "requires no fitted constant" with "is rate-robust" or "does not rely only on fitting a single exponential rate."

This is a small sentence-level issue, but it matters because the abstract sets the reader's trust level.

### 4. The experimental proposal needs one quantitative worked example

The experimental discriminator is conceptually strong but still too abstract. A skeptical reader will ask: what visibility precision, mass scale, separation scale, and interrogation-time window would actually distinguish the two curves?

The paper needs one figure or table showing synthetic curves for:

```text
L_exp(T) = exp[-T / tau_G]
L_Gauss(T) = exp[-1/2 (T / tau_G)^2]
```

at one or two representative `tau_G` values. It should mark the region where the two models differ most and estimate the required visibility precision. This does not need to be a full experimental design, but it must make the proposed test feel numerically real.

Without this, the paper has a good conceptual discriminator but not yet a convincing phenomenological proposal.

### 5. The exclusion-plot language still needs more caution

The model-comparison table is useful, but the claim that other mechanisms are separated from the ISP-motivated channel can still sound too clean. A generic non-Markovian collapse model with a gravitationally scaled memory kernel could occupy almost the same phenomenological cell.

The line saying that such a model would be "ISP's own content under another name" is too strong. A reviewer would likely object that another theory can share the same effective kernel while differing in ontology.

Recommended fix: replace that claim with something like:

```text
A non-Markovian gravitational collapse model could share this phenomenological signature; the present paper distinguishes it from ISP only at the level of motivation and ontology, not by the visibility curve alone.
```

That is both more accurate and more scientifically generous.

### 6. "Indivisibility forces" is too strong

The phrase that indivisibility forces non-exponential decay should be softened. Finite memory produces the quadratic onset. Indivisibility motivates finite memory in this paper, but indivisibility alone has not been shown to mathematically force the kernel.

Recommended fix: use:

```text
Finite memory forces the short-time decay away from a strict exponential.
```

and then say that ISP motivates why such finite memory may be physically natural.

### 7. The radiation section should end in agnosticism

The radiation section is now better, but it still has a slight tension: it says the model is plausibly not excluded, while also admitting that memory-colored noise could be constrained comparably to other collapse models. The cleanest scientific position is:

```text
No exclusion claim is made here; a dedicated radiation calculation is required.
```

The paper can still argue that the Markovian DP radiation objection does not automatically transfer unchanged to the finite-memory benchmark. But it should not imply more than that.

### 8. The literature base needs updating before submission

The manuscript still needs a stronger current bibliography. In particular, a publishable version should cite recent experimental work and proposals on matter-wave interferometry, macroscopic superpositions, collapse-model bounds, gravitational decoherence, and radiation constraints. The present reference base is enough for an internal draft, but too thin for journal submission.

This is not cosmetic. The paper's claim is about a near-future discriminator, so the reader needs to see that the author knows the present experimental and theoretical landscape.

## Suggested restructure

The current structure mostly works, but the paper would be clearer if it made the prediction hierarchy explicit:

1. **DP baseline:** strict Markovian exponential, recovered from white noise.
2. **Generic finite-memory result:** quadratic short-time exponent.
3. **ISP motivation:** indivisible records make finite memory physically natural.
4. **Benchmark closure:** identify amplitude and memory scale with the DP energy scale.
5. **Experimental discriminator:** compare exponential and Gaussian-onset visibility shapes across `T` and `d`.

This ordering would prevent the reader from thinking the paper has derived more than it has, while preserving the genuine novelty of the argument.

## Line-level and notation notes

The symbol `Gamma` appears to carry more than one conceptual role. If it denotes a transition law in one section and a decoherence exponent or rate elsewhere, the notation should be separated. Reviewers are unforgiving about reused symbols in speculative theory papers because notation ambiguity can look like conceptual ambiguity.

The Section 3 Cauchy-functional-equation argument is helpful but slightly pedagogical. Consider moving it to an appendix or shortening it. The real physics enters through the noise kernel, not through the abstract functional equation.

The phrase "same parameter range as current/proposed platforms" should be backed by a concrete table or softened. "Overlaps the order-of-magnitude range targeted by current and proposed platforms" is safer unless the manuscript provides detailed feasibility estimates.

## Recommendation

This paper is now worth developing seriously. Its best version is not "ISP derives a new law of gravitational decoherence." Its best version is:

```text
The Diósi-Penrose exponential is the white-noise member of a broader finite-memory family. If gravitational decoherence has a finite record-formation time motivated by ISP, the experimentally relevant signature is not merely a rate change but a change in the shape of visibility loss. The simplest benchmark gives a Gaussian onset on the DP timescale.
```

That is a clean, interesting, and testable claim.

Before submission, I would require:

1. A clearer distinction between generic finite-memory behavior, DP-scale benchmark closure, and ISP-specific motivation.
2. Replacement of "no fitted constant" with "rate-robust" language.
3. One quantitative visibility-shape figure or table.
4. Softer claims about uniqueness relative to other non-Markovian collapse models.
5. A current bibliography and a more explicit relation to existing bounds.

If those changes are made, the manuscript could be posted as a serious speculative preprint. For journal submission, it should be positioned as phenomenological quantum-gravity foundations, not as a completed derivation of gravitational decoherence from ISP.
