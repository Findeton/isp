# D18 protocol — the minimal complete covariant history rulebook

**Status:** frozen before D18 outcomes, 2026-07-11.

## 1. Question

D17 tests a fixed action and finds that it does not select the state, gauge-orbit
measure, extension weights, or record commit. D18 asks the constructive
question left behind:

> What is the smallest supplied covariant packet from which every local
> next-record conditional can actually be calculated, without a preferred
> global click order, and which entries can present evidence select?

This is not allowed to call a concise formula unique merely because it is
complete. Every field must be tested by deleting or changing it while holding
the others fixed.

## 2. Frozen candidate packet

Write the candidate **covariant history-instrument packet** as

```text
Q = (C, F, nu, S, rho_boundary, J, coarse, units).
```

Its fields are:

```text
C             typed admissible finite regions/histories and their sewing;
F             local dynamical fields, carriers and gauge group;
nu            gauge-fixed/groupoid reference measure, including contours;
S             local covariant action and all coefficients;
rho_boundary  normalized positive boundary/cosmological state;
J             local completely positive record instruments and future algebra;
coarse        declared record questions/cylinder maps;
units         operational dictionary to seconds, metres, hbar, c and G.
```

For a record history `alpha`, regional amplitudes form its class operator
`C_alpha[Q]`. The proposed whole-history decoherence functional is

```math
D_Q(alpha,beta)=Tr(C_alpha rho_boundary C_beta^dagger).
```

On a decoherent record partition,

```math
P_Q(alpha)=D_Q(alpha,alpha),
```

and every licensed local next-record probability is a conditional of this one
projective family. There is no second click lottery.

## 3. Scope distinction

The action density may be local and generally covariant while the normalized
state and resulting correlations are global. "No global clock" means the
packet is invariant under construction-order refinements and is evaluated by
regional sewing; it does not mean that arbitrary conditionals can be computed
from a bounded collar unless a separate finite-memory theorem proves that.

## 4. Gates

### Q0 — exact packet typing

Every factor in `Q` is explicit. State, measure, domain, instrument, coarse
graining, and unit conversion may not be hidden in `S`.

### Q1 — finite sufficiency witness

One dependency-free exact packet must produce amplitudes, interference,
durable D14 records, a normalized decoherence functional, a projective history
family, and a visible non-Markov next-record conditional.

### Q2 — necessity by interventions

For each nonredundant field of `Q`, either:

1. exhibit two packets differing only in that field and producing distinct
   operational predictions; or
2. prove that the field is derived from the remaining fields.

Pure coordinate/gauge changes do not count as physical differences.

### Q3 — gauge and construction order

Labeled presentations related by admissible relabeling give identical
observables. A sampler order may be used computationally only if its different
linear extensions induce the same cylinder law.

### Q4 — local generation

Regional amplitudes sew on owned unsealed boundaries. No update may inspect a
universe ledger. If a prediction depends on old information, the information
must be carried by the boundary state/memory or by a whole-history amplitude,
not retrieved superluminally at a click.

### Q5 — quantum probability

`D` is Hermitian, strongly positive on the tested event algebra, normalized,
and additive under disjoint coarse graining. Diagonal values are read once.
Records suppress an interference observable by a modeled physical commit.

### Q6 — projective/profinite law

Finite cylinder restrictions commute with truncation. A compatible family
extends to the declared inverse-limit event domain; profinite completion hosts
the law but is not credited with selecting it.

### Q7 — relativistic recovery

The rulebook must distinguish:

```text
fundamental order/locality,
effective Lorentz cone,
operational rods and clocks,
construction-order gauge.
```

No preferred foliation may enter a physical observable.

### Q8 — empirical selection ledger

Each packet entry is labeled `derived`, `fixed by independent observation`,
`convention/gauge`, or `open`. A fitted datum cannot be reported as a new
prediction. Known low-energy evidence may select an effective packet without
selecting a unique ultraviolet completion.

### Q9 — geometry consequence gate

Round-cone `F`, dimension, scale-ladder, influence speed, and gravity tests may
run only after the candidate fixes the relevant cross-candidate predictions
before inspecting the held-out result. If 3+1 dimension or a Lorentzian metric
is an input, their recovery is calibration, not emergence.

### Q10 — rival architectures

At minimum compare:

```text
covariant history/action packet;
classical sequential growth;
quantum sequential growth;
process tensor/quantum comb;
general-boundary amplitudes;
canonical Hamiltonian evolution;
collapse or stochastic modification.
```

The comparison must ask whether each architecture supplies dynamics or merely
represents a supplied dynamics.

### Q11 — hostile closure

Independent mathematical, ontology/locality, and clean-room reviewers must
attack sufficiency, hidden global time, Born duplication, gauge weights,
state/instrument freedom, and all claims of uniqueness or physical selection.

## 5. Countercontrols

```text
same S, different rho_boundary -> different records;
same S and state, different physical nu -> different records;
same amplitudes, record commit present/absent -> interference changes;
same finite marginals, different projective continuation -> future changes;
same dynamics, different units dictionary -> dimensionless predictions same;
different construction orders -> observables identical;
independent per-depth normalization -> projectivity fails;
action phase without modulus/state/measure -> no normalized law;
```

## 6. Verdicts

```text
UNIQUE-FUNDAMENTAL-RULEBOOK-SELECTED
  one physical equivalence class passes Q0-Q11 and an untouched empirical
  prediction;

MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK
  Q is necessary and sufficient at the stated finite/regulated scope, but one
  or more physical fields remain empirically supplied;

EFFECTIVE-RULEBOOK-SELECTED
  independent observations select a low-energy packet and new holdouts pass,
  without a unique ultraviolet completion;

INCOMPLETE-INVESTIGATION
  any promised theorem, receipt, geometry gate, or hostile review is missing.
```

No nonselection theorem by itself completes the full thread objective. It
does, however, forbid relabeling an incomplete action as "the rulebook."
