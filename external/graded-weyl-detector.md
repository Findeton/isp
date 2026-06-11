# A graded local Weyl criterion for coefficient regularity of divergence-form operators

*Standalone note in plain mathematical language. Code:
`code/v6_p27c_graded_detector_campaign.py`,
`code/v6_p24a_regularity_detector_campaign.py`. Local draft — not
submitted anywhere.*

## Abstract

For the operator L = -d/dx ( c(x) d/dx ) on the circle, define the
local Weyl remainder r_t(x) = K_t(x,x) sqrt(4 pi c(x) t) - 1, with K_t
the heat kernel diagonal. We present numerical evidence, with exact
spectral computations, for a graded law: for coefficients of Holder
class C^(0,alpha), the sup-norm of the remainder decays as
t^(min(1, alpha/2)) — measured exponents 0.243, 0.465, 0.706, 0.956
for alpha = 0.5, 1.0, 1.5 and smooth coefficients, against the
predicted 0.25, 0.50, 0.75, 1.00. The detector also LOCALIZES
singularities: for an interface (jump) coefficient the remainder is
pinned at O(1) exactly at the jump while decaying elsewhere; for
fast-oscillating coefficients it is O(1) globally between the micro
and macro scales (the homogenization regime). For smooth coefficients
the remainder's linear coefficient field lies in the span of c'' and
(c')^2/c with a leading coefficient -1/4 that is metric-independent
at the 1e-3 level. We propose the corresponding equivalence — decay
exponent of the local Weyl remainder = Holder class of the
coefficient, with localization at the singular set — as a conjecture
in classical heat-kernel analysis; the forward direction (regularity
implies decay) is standard parametrix calculus, the rigidity converse
appears open.

## 1. The detector

For c smooth, the leading local heat asymptotic of L = -d(c d.) is
K_t(x,x) ~ (4 pi c(x) t)^(-1/2), so

    r_t(x) := K_t(x,x) sqrt(4 pi c(x) t) - 1 -> 0   as t -> 0,

with rate t and a curvature-type coefficient. The heuristic for rough
coefficients: diffusion at time t resolves the coefficient at scale
sqrt(t); a C^(0,alpha) modulus contributes (sqrt t)^alpha to the
parametrix error, so

    sup_x |r_t| ~ t^(min(1, alpha/2)),

the smooth rate saturating the grading.

## 2. Numerical results (exact eigensolves, n = 512-1024 grid)

Strata separation (jump coefficient c: 1 -> 4; oscillation
c = 1 + 0.45 sin(64 pi x); smooth control):

```text
   smooth:    sup |r_t| = 0.088, 0.047, 0.024, 0.012  at
              t = 0.02, 0.01, 0.005, 0.0025 (ratios 1.89/1.94/1.96:
              linear in t)
   interface: sup pinned at 0.3334 across the same t-range, attained
              AT the jump; values away from the jump decay
   oscillatory: 0.27, t-independent between micro and macro scales
```

The graded law (kink family c_alpha = 1 + 0.5 |sin(pi x)|^alpha):

```text
   class                fitted exponent     predicted min(1, alpha/2)
   C^0,1/2                  0.243                 0.25
   C^0,1                    0.465                 0.50
   C^1,1/2                  0.706                 0.75
   smooth                   0.956                 1.00
```

The smooth coefficient field (Richardson extraction in t, fit to the
complete two-term local basis):

```text
   r_t / t -> a_1(x) = alpha c''(x) + beta c'(x)^2 / c(x),
   alpha = -0.2482 / -0.2495 across two independent metrics
   (= -1/4 to ~1e-3, metric-independent);
   beta = 0.08-0.10 (extraction-limited: the t -> 0 and grid limits
   compete).
```

## 3. The conjecture

**Graded local Weyl criterion.** For L = -d(c d.) with c bounded
between positive constants:

1. (forward, classical) c in C^(0,alpha) implies sup_x |r_t| <=
   C t^(min(1, alpha/2));
2. (rigidity, conjectured) if sup |r_t| = O(t^(gamma)) with
   gamma <= 1, then c in C^(0, 2 gamma - eps) for every eps > 0;
   localized non-decay identifies the singular support;
   t-independent global persistence at level O(1) between scales
   identifies a homogenization regime, where the operator's spectral
   limit is governed by the harmonic mean of the sampled coefficient
   rather than its pointwise values.

The forward direction is parametrix calculus; the closed form of the
smooth coefficient field is classical (Minakshisundaram-Pleijel-type)
and the measured -1/4 invites the short computation. The rigidity
direction appears open and is the substantive question: heat-kernel
diagnostics that GRADE coefficient regularity, rather than assume it,
would give spectral numerics a model-free regularity test.

## References

- S. Minakshisundaram and A. Pleijel, Can. J. Math. 1, 242 (1949).
- P. Gilkey, Invariance Theory, the Heat Equation, and the
  Atiyah-Singer Index Theorem.
- A. Bensoussan, J.-L. Lions, G. Papanicolaou, Asymptotic Analysis
  for Periodic Structures (1978) (the homogenization regime).
- E. B. Davies, Heat Kernels and Spectral Theory (1989).
```
