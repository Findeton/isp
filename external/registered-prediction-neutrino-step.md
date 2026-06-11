# Registered prediction: the neutrino inter-generation step and the record marginality constant

*Registration date: 2026-06-10.  Local document — registered for
internal discipline only; not posted or submitted anywhere.*

## 1. Provenance of the constant (declared before any neutrino comparison)

The corpus' single structural small dimensionless number is the
single-relation binding marginality

    eps_record = 3 kappa - 1 = 0.0318,

derived in Papers 8/10 from the relation-code binding laws — years of
corpus-time and ten papers before any neutrino data was consulted.
Paper 23 observed that the nine charged-fermion inter-generation mass
steps all lie between eps^2 and sqrt(eps) (the P-eps pattern claim,
9/9 postdictive).  The natural extension to the neutrino sector is
registered here as a forward test.

HONESTY NOTE.  The numerical proximity of the neutrino step to
sqrt(eps_record) was noticed BEFORE this registration (it motivated
it).  What registration adds: the precise claim forms, the declared
tolerances, the falsifiers, and the commitment to let future data
judge - the central-value coincidence is the seed, not the content.

## 2. The observable

Under a normal-ordered, hierarchical spectrum (m1 << m2 << m3), the
neutrino inter-generation step is

    S_nu := m2 / m3 = sqrt( dm^2_21 / dm^2_31 ).

Current global-fit inputs (NuFIT 5.x-class, normal ordering):
dm^2_21 = (7.41 +- 0.21) x 10^-5 eV^2;
dm^2_31 = (2.511 +- 0.027) x 10^-3 eV^2.

    S_nu = 0.1718 +- 0.0026  (1.5%)
    sqrt(eps_record) = 0.17833
    S_nu / sqrt(eps_record) = 0.963
    (inverted ordering, using |dm^2_32| = 2.449e-3: S_nu = 0.1740,
     ratio 0.975 - the ordering barely moves the comparison)

## 3. The registered claims

**P-eps-nu (band form; the registered prediction).**  The neutrino
step is an O(1)-coefficient rung of the record ladder at the
half-power:

    S_nu = C * sqrt(eps_record),    C in [0.80, 1.25].

Current status: C = 0.963 (NO) / 0.975 (IO) - INSIDE the band.
This is the form the corpus' P-eps pattern licenses (the charged
ladder carries O(1) coefficients throughout).

**P-eps-nu-strict (sharp form; registered as under tension).**  The
strict equality S_nu = sqrt(eps_record) is currently disfavored at
2.5 sigma of the measurement (deviation 3.8% against a 1.5%
measurement error).  Registered anyway, with eyes open: JUNO-class
precision on dm^2_21 (sub-percent) will either push this beyond
5 sigma (killing the strict form cleanly) or - if the global-fit
central values move - revive it.  Either outcome is recorded in
advance as informative.

## 4. Premises and falsifiers

```text
PREMISES:
  (h)  hierarchical normal-ish spectrum: m1 << m2 (so that
       m2/m3 = sqrt of the mass-squared ratio).  A quasi-degenerate
       spectrum breaks the identification.
FALSIFIERS (any one suffices):
  F1: cosmology or beta-decay endpoint establishing quasi-degeneracy
      (Sigma m_nu or m_beta implying m1 ~ m2): the observable S_nu
      is then not the step, and the registered claim is VOID (not
      passed) - voiding is recorded as a failure of the premise, not
      of the ladder.
  F2: future precision moving C outside [0.80, 1.25]: the band form
      FAILS and the P-eps extension to neutrinos dies.
  F3: (strict form) JUNO-era data holding the current central values
      at sub-percent errors: the strict form dies at > 5 sigma.
WHAT WOULD COUNT AS A PASS:
  the band form surviving JUNO-era precision, with C stable; the
  strict form would require the central values to drift ~4% upward
  in S_nu - quantified in advance.
```

## 5. Why this is the right registration

It is the only place in the corpus where a number that was derived
with no reference to the Standard Model (eps_record, from the binding
marginality) meets a number nature has measured independently (the
neutrino mass-squared ratio) with no fit parameter in between.  The
charged-fermion P-eps rows are postdictions; this row is the cheapest
genuine forward test the framework owns, and its strict form is
already under quantified tension - which is what a real prediction
looks like.

## 6. Computation record

```text
eps_record = 0.0318;  sqrt = 0.178326
NO:  S = sqrt(7.41e-5 / 2.511e-3) = 0.17179 +- 0.00260
     C = 0.9633;  strict-form deviation = +3.81% = 2.5 sigma
IO:  S = sqrt(7.41e-5 / 2.449e-3) = 0.17395;  C = 0.9754
(error propagation: half the quadrature sum of the relative
 mass-squared errors)
```
