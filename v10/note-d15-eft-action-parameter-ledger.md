# D15 EFT action and parameter ledger

**Status:** pre-hostile-review scope ledger, 2026-07-11.

## 1. Domain and equivalence

The `EFT4` claim is restricted to processes with characteristic energy and
curvature scales below the lightest omitted threshold and below the regime in
which the derivative expansion fails.  Schematically,

```math
E/Lambda_cut << 1,
|R|/Lambda_cut^2 << 1.
```

An order-`N` truncation must carry an error of the scale of the first omitted
operator, modified by known loop/logarithmic enhancements.  D15 does not yet
assign a universal numerical `Lambda_cut`; it is sector- and candidate-
dependent.

Operator lists are equivalence classes under:

```text
integration by parts;
algebraic tensor/group identities;
leading equations of motion for on-shell observables;
invertible perturbative field redefinitions;
four-dimensional topological densities at fixed topology.
```

Therefore coefficient counts depend on a printed basis and observable scope.

## 2. Leading curved-space action

Given the observed fields and gauge representations, a representative leading
action is

```math
S_0 = integral d^4x sqrt(-g) [
  M_Pl^2 R/2 - M_Pl^2 Lambda
  - (1/4) sum_A Z_A F_A^2
  + i sum_f Z_f bar(f) gamma^mu D_mu f
  + Z_H |D H|^2
  - m_H^2 H^dagger H - lambda_H (H^dagger H)^2
  - (bar(q)Y_u tilde(H)u + bar(q)Y_d H d + bar(l)Y_e H e + h.c.)
  + xi_H H^dagger H R
  + theta_3 G tilde(G) + theta_2 W tilde(W) + theta_1 B tilde(B)
].
```

Wave-function factors can be moved into canonically normalized fields and
couplings.  Some electroweak theta combinations are unphysical or depend on
the global/anomaly/matter assumptions; the ledger prints them before that
quotient rather than silently discarding them.  Neutrino masses require
either the dimension-five Weinberg operator or extra fields beyond the
minimal renormalizable content.

## 3. Higher operators

The gravitational derivative expansion includes, modulo the printed
equivalences,

```math
a_R2 R^2 + a_Ric2 R_{mu nu}R^{mu nu}
+ a_Riem2 R_{mu nu rho sigma}R^{mu nu rho sigma}
+ higher derivatives and matter-curvature operators.
```

In four dimensions one curvature-squared combination is the Euler density,
so only two local bulk combinations are independent at fixed topology before
matter/boundary qualifications.  The Standard Model sector contains the
dimension-five neutrino-mass operator and a finite basis at each higher
dimension, including the dimension-six Warsaw basis.  Wilson coefficients
are not fixed by symmetry alone.

## 4. Parameter classification

| Parameter class | What fixes relations | What fixes values in D15 |
|---|---|---|
| normalization of fields | convention/canonical kinetic terms | convention, without changing observables |
| gauge-vertex relations | local gauge invariance | one measured running coupling per independent gauge factor at a reference scale |
| `G` / `M_Pl` | coefficient location fixed by gravity normalization | measured gravitational strength; not derived |
| `Lambda` | diffeomorphism covariance permits it | cosmological observation; not derived |
| Higgs mass/quartic | operator form fixed by symmetry | measured renormalized coefficients |
| Yukawa matrices and mixing | gauge representations restrict allowed entries | measured; flavor pattern not derived |
| theta/CP coefficients | topology and anomaly structure constrain observability | bounded/measured; strong-CP smallness unexplained |
| `xi_H` | curved-space locality permits it | free/bounded and scale dependent; not fixed by flat-space SM data alone |
| higher Wilson coefficients | symmetry/basis and RG mixing constrain relations | fitted/bounded or predicted only after a UV model is supplied |
| boundary/corner coefficients | well-posed variational principle and chosen boundary conditions | conditional on action/domain; finite counterterms may remain scheme/data dependent |
| state parameters | not action coefficients | cosmological/laboratory preparation data or separate state law |
| record scale/basis | interaction, environment, state and coarse graining | conditional apparatus/environment data; no universal D15 derivation |

## 5. `G` and proper units

The action places `G` through

```math
M_Pl^2 = 1/(8 pi G)
```

in units with `c=hbar=1` for the reduced Planck mass convention.  Restoring
units gives the usual combinations such as

```math
l_Pl = sqrt(hbar G/c^3).
```

This explains how a measured gravitational coefficient defines a physical
length scale once `hbar` and `c` are calibrated.  It does not calculate `G`
from dimensionless records.  Rescaling record distance axes into metres does
not change cone anisotropy; only the dynamics/refinement limit can do that.

## 6. Ledger verdict

```text
LEADING OPERATOR FORM = STRONGLY CONSTRAINED GIVEN OBSERVED 3+1 FIELD CONTENT
INDEPENDENT COEFFICIENT VALUES = MOSTLY EMPIRICAL/RG DATA
HIGHER OPERATOR TOWER = REQUIRED AND UV-SENSITIVE
G = MEASURED ACTION COEFFICIENT, NOT SHARD-DERIVED
STATE + RECORD INSTRUMENT = SEPARATE CONDITIONAL DATA
```

This ledger supports `LOW-ENERGY-EFFECTIVE-RULEBOOK-IDENTIFIED`, not a unique
fundamental action claim.

