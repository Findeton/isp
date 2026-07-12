# D13 theorem note — finite kernel nonselection and the candidate amplitude bridge

**Status:** final after three hostile rounds at narrowed scope, 2026-07-11.  The filename is
retained for provenance; no maximal/universal architecture theorem is claimed.

## 1. What is proposed, not proved

General-boundary amplitudes are the strongest candidate bridge between
physical dynamics and sealed diamonds:

```text
typed lower/upper boundaries
-> regional linear amplitude
-> coherent contraction on shared unsealed boundaries
-> boundary state plus instruments
-> decoherence functional
-> durable record histories.
```

This architecture can avoid a preferred global clock.  It is not derived here
from SHARD.  In particular, D13 has not defined and proved a symmetric
monoidal category of all sealed diamonds, its construction-presentation
quotient, or a universal sewing theorem.  Gauge theories and gravity may need
edge modes, boundary charges, ghosts, anomaly cancellation and theory-specific
sewing measures.  The formal expression `integral exp(iS/hbar)` is conditional
on all those data.

The safe statement is:

> if a supplied regional quantum action has a well-defined local sewing law,
> it is a natural candidate generator for sealed-diamond history amplitudes.

## 2. Exact theorem that is proved

Fix one operational diamond interval/evidence slab, one four-dimensional
two-qubit carrier, one allowed outcome set, and the same preparation/effect.
Let

```math
X_{ex}=|01><10|+|10><01|,
\qquad U_\theta=e^{i\theta X_{ex}}.
```

The dependency-free exact receipt compares `theta=pi/4` and `theta=pi/2`.
They share the ambient carrier, types, allowed grammar/outcome labels,
interaction support in the ownership sense, generator symmetries and fixed
operational interval.  They do **not** share positive prediction support: the
half-iSWAP member has an exact zero where the quarter member has positive
mass.

The receipt proves 21 exact cells in `Q(sqrt(2),i)`:

1. both kernels are unitary;
2. the generator respects excitation number and leg exchange;
3. two quarter kernels compose to the half kernel;
4. one disjoint tensor-factor schedule cell commutes;
5. one overlap control is order-sensitive;
6. independent input/output unitary frame covariance holds;
7. the declared seal-and-output-birth map is isometric;
8. its orthogonal record alternatives are exclusive;
9. their probabilities normalize;
10. both kernels have a maximal-entanglement witness;
11. the fixed-interval record probabilities are `1/2` and `0`;
12. coherent path addition differs from an inserted-record probability sum;
13. one entangled disjoint-laboratory no-signalling cell passes;
14. an exact dephasing Kraus family is complete;
15. its open-system output is positive and normalized;
16. the Born weight is read once, not squared twice;
17. a sealed record persists under the licensed later system-only algebra;
18. repeat-read meaning is stable in that algebra;
19. the seal emits one declared live collar;
20. a reversible hidden-memory circuit gives an explicit visible non-Markov
    history;
21. the check count and semantic hash are frozen.

For the fixed preparation `|10>` and effect `|10><10|`,

```math
P_{\pi/4}(10|10)=1/2,
\qquad P_{\pi/2}(10|10)=0.
```

An allowed relabeling must preserve every instrument probability, so the
kernels are physically inequivalent.  They are also not related by unitary
conjugation and a common phase because their eigenvalue ratios differ.

### Theorem

The shared finite local-unitary kernel premises tested above do not uniquely
select the interaction angle/coupling on a fixed operational diamond interval.

This theorem was already present in core form in D12.  D13 adds the fixed-
interval action framing and the repaired quantum/record cells; it makes no
priority claim for the iSWAP counterfamily.

## 3. Visible non-Markov scope

The amplitude architecture does not force non-Markovity.  The receipt proves
only that it permits it.  A reversible circuit copies the first visible
record `X` to an unobserved memory, makes the current visible record `Y=0` for
both branches, then copies memory to the next record `Z`.  Hence

```math
P(Z=1|Y=0,X=1)=1,
\qquad P(Z=1|Y=0,X=0)=0.
```

The enlarged process is reversible/Markov on system plus memory; the visible
record process is non-Markov.  This is a compatibility witness, not a general
Barandes-equivalence theorem.  The distinction between instantaneous
probability dynamics and a measure on trajectories remains as in the D12
Egri audit.

## 4. Support-relative polar representation

For a fixed positive scalar reference `nu`, fixed amplitude normalization and
global phase, and a nonzero scalar amplitude `K(H)`, one may write on its
positive amplitude support

```math
K(H)=nu(H)^{1/2} exp[-I(H)/2+i Phi(H)],
```

with

```math
I(H)=-log(|K(H)|^2/nu(H)),
\qquad Phi(H)=arg K(H).
```

Without fixing normalization/global phase, `I` and `Phi` are defined only
modulo common additive constants.  Zeros require an explicit support field.
Changing `nu` changes `I`.

This is only an atomwise polar coordinate representation of a supplied scalar
amplitude.  `I` is SHARD RN/KL evidence only after a normalized positive
record law and the evidence-gluing/survival hypotheses are proved.  `Phi` is
sealed holonomy only after transports, loops, gauge action and cocycle laws
are supplied.  Before unresolved alternatives are coherently summed, path
moduli are not record probabilities.

## 5. Narrow continuum counterfamily

Take a real scalar EFT on Minkowski or a suitable asymptotically flat
background, with fixed vacuum/asymptotic particle states, fixed field
normalization and renormalization convention, and no symmetry forbidding
`phi^4`.  For two distinct small positive renormalized couplings,

```math
S_\lambda=S_{kinetic}-\int d^4x\,{\lambda\over4!}\phi^4,
```

the classical differential principal part and Minkowski causal cone agree,
while the perturbative connected `2 -> 2` amplitude differs.  Covariantizing
the scalar density gives diffeomorphism-covariant EFTs on the declared
background class, but a generic curved spacetime need not possess an S-matrix.

This is a continuum coefficient nonuniqueness witness in a restricted EFT
sector, not a theorem about every generally covariant scalar theory.

## 6. Honest gate ledger after round 1

| gate | repaired status |
|---|---|
| A0 | frozen antecedent census plus interpretive ledger; late V7 P47–P51 added; final hostile audit pending |
| A1 | not closed: types, grammar, state, records, reference and units remain primitive |
| A2 | one exact disjoint/overlap cell plus D12 adjacent-swap theorem; no universal diamond category proof |
| A3 | exact finite matrix composition; general action sewing conditional |
| A4 | finite interference, positivity, normalization, entanglement, no-signalling, Kraus and Born-once cells pass; not universal |
| A5 | one declared seal/birth instrument is persistent only under its licensed future algebra; instrument not derived |
| A6 | unitary endpoint-frame covariance only; Lorentz/diffeomorphism/network gauge not passed by the finite receipt |
| A7 | finite-kernel unique selection refuted; architecture universality not proved |
| A8 | fields/couplings remain primitive or empirical |
| A9 | physical-unit bridge and `G` remain open |
| A10 | D9 conditionally selects `pi/4` inside a frozen preparation family, then refutes its one-coupling geometry map; no complete-action selector |
| A11 | correctly withheld |
| A12 | three rounds pass the narrowed exact theorem; full objective remains incomplete |

## 7. Final D13 verdict

The protocol verdict remains

```text
INCOMPLETE-INVESTIGATION.
```

The exact surviving theorem is

```text
FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED.
```

The candidate scientific interpretation is that regional amplitudes generate
records more naturally than a separate global click race.  It remains a
proposal until the sealed-diamond source category, general sewing, physical
action-to-record dictionary and empirical selector are derived.
