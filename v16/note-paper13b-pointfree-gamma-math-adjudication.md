# Paper 13B mathematical hostile adjudication

Date: 2026-08-20

Status: **TERMINAL FOR THIS CANDIDATE / REJECT / NO RUST**

## 1. Immutable record

The adjudicated corpus is:

| artifact | SHA-256 |
|---|---|
| `v16/note-paper13b-pointfree-gamma-physics-pin.md` | `df2c60be816e2aaf5261f954d6e1d12142ad528f572f7c77c1ff5a91464b4f47` |
| `v16/paper-13b-pointfree-whole-history-gamma.md` | `5f55d1249e68e9b019790dda52254f819b68917637752cc32f0580ea07f7ff18` |
| `v16/note-paper13b-pointfree-gamma-mathematical-construction.md` | `ad13c0ba07110f608047a48a7b3cf921dac66c4beb4e857b000dc7d127c8f9f7` |
| `v16/note-paper13b-pointfree-gamma-math-review-protocol.md` | `034fbe56a79a91860812bfbe4322e635a4a579f79f2b9b135877db2536e6a409` |
| `v16/review-paper13b-pointfree-gamma-physics.md` | `8cf32b6831f60839a3c55b269207916b6a9994cca201411722fa6e081f5fc507` |
| `v16/review-paper13b-pointfree-gamma-probability.md` | `9245c620d3f5299b5ff640a4474362c2c65a716ba46d84bb12781e247cda836b` |
| `v16/review-paper13b-pointfree-gamma-groupoid.md` | `622f92fe5d6d787a61b83c682d0413e36ebd354b5c4ad268f8c3033dc48f9291` |

The reports were mutually blind and implementation-free. Their verdicts are:

```text
physics/ontology        REJECT
probability/intervention ACCEPT
groupoid/referent       REJECT
```

The user then supplied an architectural analysis, raw-text SHA-256
`77469bcf006fb948dcb0476c8e0893d3d6ef27b56c6b96215d7cffecd3e1d424`,
which independently accepts the two decisive defects and proposes a new
interventionally complete law. This analysis is adopted below where verified.

## 2. Adjudication method

The adjudicator independently checked the decisive examples against the
frozen definitions. Arithmetic agreement is not enough: each positive
coordinate must consume a mathematical referent actually determined by the
paper.

No software exists, so no finding concerns Python, Rust, mutability, hashing,
serialization, CLI behavior, cache state, memory, or performance.

## 3. Finding A — a static joint law does not determine intervention

### 3.1 Frozen definition

The paper defines the observational law as a product of displayed source and
assignment factors. It then defines `do(X=a)` by replacing one displayed
assignment while retaining the other factors.

At the same time, the paper says its factorization notation is a
representation and claims the physical primitive is the static whole-history
probability $\Gamma_*$.

### 3.2 Exact counterexample

Let $P_0$ be the paper's complete static joint law. Its $X,Y$ marginal obeys

$$
P_0(x)=\frac12,
\qquad
P_0(y=x\mid x)=\frac{337}{625}.
$$

The paper's common-source factorization gives

$$
P_0(y=1\mid\operatorname{do}(x=1))=\frac12.
$$

But the same joint law has the exact chain-rule factorization

$$
P_0(x)P_0(y\mid x)P_0(c,\eta_X,\eta_Y\mid x,y),
$$

with all other variables and deterministic outputs appended unchanged.
Truncating this equally valid factorization at $X$ gives

$$
P_0(y=1\mid\operatorname{do}(x=1))=\frac{337}{625}.
$$

The observational law, every labeled-history mass, every orbit mass, and all
static readers are identical. The `do` laws differ.

### 3.3 Decision

The physics seat is correct. Intervention is not identifiable from the static
joint distribution. One must either:

1. promote a directed structural factorization as extra physical data, which
   violates this candidate's claim that factorization is merely
   representational and imports a local operational order; or
2. define one primitive global intervention operator on typed experiments.

The frozen paper does neither completely. Its explicit response calculations
are valid relative to its chosen factorization, but they are not determined by
the promoted static $\Gamma_*$.

The probability seat's acceptance correctly verifies the calculations after
accepting the displayed factor rule. It does not answer the identifiability
counterexample because it treats the contested rule as primitive without
reconciling that move with the paper's ontology claim.

## 4. Finding B — the total experiment object is undefined

The groupoid seat identifies an independent defect. The paper transports a
six-component packet but never determines:

- the admissible intervention-slot set;
- the alternatives permitted at each slot;
- how a mechanism-changing intervention retypes dependent variables;
- the complete context domain;
- the reader objects and their complete partitions; or
- the intervention probability measure for every admitted packet.

This is visible without the chain-rule counterexample. The paper says the
mode $w$ may be intervened upon. Starting from a $U$ atom, `do(w=R)` has at
least three possible readings:

- retype the atom, create $m,r$, and use $B^2$, giving
  $(B^2)_{00}=337/625$;
- retain the $U$ carrier and $C$, giving $C_{00}=49/625$; or
- refuse the intervention as inadmissible.

The frozen law chooses none. Simultaneously transporting undefined packet
fields proves covariance only after a packet category is supplied; it does
not construct that category.

Decision: `P13B-POINT-FREE-EXPERIMENT-ACTION-CONSTRUCTED` is not earned.

## 5. Finding C — the negative kernel is cut-relative, not native as written

The arithmetic is exact:

$$
CB^{-1}=\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

Therefore no positive stochastic $K$ satisfies $C=KB$ for the stipulated
first leg $B$.

Mode $U$, however, explicitly contains no intermediate random variable or
typed $B$ boundary. It contains only the whole transition $C$. The static
kernel admits positive factorizations such as

$$
C=CI=IC.
$$

These do not refute the $B$-specific obstruction. They show why $B$ must be a
native typed candidate boundary before its failure can be called native
nondivision.

The probability and groupoid seats accepted the word “declared” as enough to
make $B$ native. The physics seat correctly requires an actual boundary
referent in the law. The pin likewise requires a typed candidate frontier,
not a matrix selected only for comparison.

Decision: the scoped statement

> No positive normalized second leg completes the stipulated first leg $B$
> to $C$.

survives. `P13B-NATIVE-INDIVISIBLE-CUT-CONSTRUCTED` does not.

## 6. Surviving mathematics

The rejection does not erase independent results. The following survive
exactly:

1. the finite typed local atom definition;
2. the $X\leftrightarrow Y$ local presentation action;
3. the endpoint-generated inter-atom bond rule;
4. the full wreath-product history action;
5. orbit pushforward rather than representative mass;
6. local, bond, fixed-size, and all-size normalization;
7. exact occurrence multiplicity under automorphisms;
8. exchangeability and uniform-deletion projectivity;
9. the finite licensed-grammar record intertwining theorem;
10. the recorded complete frontier and stable-but-incomplete record-only
    control;
11. the division-without-new-record control;
12. the $B$-specific negative-factorization theorem;
13. the explicit factorization-relative response arithmetic; and
14. the absence of any actuality, chronology, dimension, geometry, metric,
    curvature, gravity, GR, or QFT result.

The response arithmetic remains a calibration of one declared structural
factorization. It is not promoted as a response derived from the static
physical law.

## 7. Terminal product vector

```text
referent    P13B-POINT-FREE-HISTORY-REFERENT-CONSTRUCTED
law         P13B-ONE-WHOLE-HISTORY-GAMMA-CONSTRUCTED
             [static observational law only]
experiment  P13B-EXPERIMENT-PRESENTATION-ONLY
record      P13B-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13B-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
nondivision P13B-NONDIVISION-UNPROVEN
size        P13B-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13B-RECIPROCAL-RESPONSE-UNCONSTRUCTED
actuality   P13B-ACTUALIZATION-UNCONSTRUCTED
```

The law coordinate is deliberately scoped: one exact normalized point-free
static history measure exists. It is not the interventionally complete
$\mathbf\Gamma$ required for operational chronology.

## 8. Adopted successor architecture

The user's proposed architecture is mathematically appropriate:

$$
\mathbf\Gamma:
\mathsf{Experiment}\longrightarrow
\operatorname{Prob}(\mathsf{CompleteHistories}),
$$

with

$$
\Gamma_*=\mathbf\Gamma(\mathrm{id}).
$$

For this to remain one law rather than a fitted kernel menu, a successor must
freeze:

1. a complete typed experiment category, including admissible marked slots,
   values, contexts, readers, and composition;
2. one uniform global evaluation rule producing every
   $\mathbf\Gamma(e)$;
3. presentation covariance of the complete experiment and output law;
4. equality of law identity only when the intervention mechanism is equal;
5. observational and regional laws as derived shadows;
6. a native typed boundary chain $B_0\to B_1\to B_2$ in mode $U$ with
   $\Gamma(B_1\mid B_0)=B$ and $\Gamma(B_2\mid B_0)=C$;
7. the cut-relative question whether a positive
   $\Gamma(B_2\mid B_1)$ exists; and
8. the continued absence of dimension, geometry, metric, or desired outcome
   from law selection.

This adds an operational intervention interface. It need not insert spacetime
chronology. The later response relation and its possible closure remain
derived. A directed Bayesian-network factorization, by contrast, would make a
local causal order primitive and must be admitted as such.

## 9. Stopping rule

The successor architecture changes the mathematical primitive and the native
boundary object. It is not a prose correction and not a code-conformance
repair. The user's original authorization allowed one clean-sheet candidate
and expressly forbade an automatic repair chain.

Therefore:

- the frozen candidate is terminal `REJECT`;
- no Rust implementation pin is authorized;
- no Python or Rust implementation may begin;
- no automatic Paper 13B-v2 construction may begin; and
- adopting the architecture in §8 as a new candidate requires explicit user
  authorization.

The failure is physical and mathematical, not a programming-language issue.
