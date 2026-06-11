# Registered prediction: the neutrino inter-generation step and the record marginality constant

*Registration date: 2026-06-10.  Local document — registered for
internal discipline only; not posted or submitted anywhere.*

> **PRECISION NOTE 4 (2026-06-11, from corpus Paper 35).**  The
> registered numbers were computed at 3-digit eps = 0.0318.  At
> the exact eps = 0.0317686364466 (P8's closed form), the
> registered point is S = 0.1754721, not 0.1755561 - an 8.4e-5
> shift = 0.23 sigma at JUNO-final precision.  Rule adopted: all
> registered comparisons use eps to >= 10 digits.  The registered
> CLAIM (the undressed spectrum point) is unchanged; its exact
> evaluation is 0.1754721.  Separately, corpus Paper 35 maps the
> post-JUNO observation that the dressed base eps(1-eps) lands at
> -0.05 sigma: a POST-DICTION with counted look-elsewhere cost
> (6/12 natural forms fit today), registered as derivation target
> O35.1 only - NOT as a claim.
>
> **STATUS UPDATE 3 (2026-06-11, JUNO first data).**  JUNO has
> published its first measurement (59.1 days; arXiv:2511.14593;
> Nature 654, 343 (2026)): dm^2_21 = (7.50 +- 0.12) e-5 (NO),
> already 1.6x better than all prior data combined.  Recomputed:
> S_nu = 0.17283 +- 0.00167 (was 0.17179 +- 0.00260); registered
> point 0.17556 now at +1.64 sigma (was +1.45); the point needs
> dm^2_21 = 7.74e-5 = +2.0 sigma from JUNO's value.  The central
> value MOVED TOWARD the prediction (~1/3 of the drift the
> survival branch needs) while the error shrank - significance
> nearly unchanged, no pre-committed threshold crossed.  Deciding
> dataset: sub-percent JUNO (~2027-2028).  TIMING CORRECTION: an
> earlier draft claimed this registration predates JUNO's first
> release - false (arXiv:2511.14593 is November 2025); the
> forward-test character attaches to the sub-percent dataset
> only.  Texture compatibility against the new data: corpus
> Paper 34, Sec. 9 (C_needed = 0.985 +- 0.009; the minimal
> texture's C = 1 at +1.64 sigma; the unattainable sqrt(1-eps)
> anchor at -0.11 sigma).
>
> **CORRECTION 2 (2026-06-11, hostile review).**  The
> registered claim itself was rebuilt: "exponent x_nu = 1/2 with
> free O(1) coefficient" is UNFALSIFIABLE (the program's own 68%
> coefficient spread [0.22, 1.26] covers an exponent interval of
> width 0.506 >= the rung spacing 0.5 - the lattice covers the
> whole axis).  The registered content is now the UNDRESSED
> SPECTRUM POINT m1:m2:m3 = eps : sqrt(eps) : 1, i.e. S_nu =
> sqrt(eps/(1+eps)) = 0.17556 exactly.  EXPECTED OUTCOME, stated
> against interest: at current centrals, JUNO precision excludes
> this at ~5.6 sigma - the claim is expected to DIE, and (2,5]
> sigma is pre-assigned as FAILED.  Trials record corrected
> (m_e/m_mu at exponent 1.546 IS a band-grade hit of rung 1.5).
> Running escape hatch closed (SM bound ~5e-5, Lambda <= 1e12 GeV
> declared).  Full detail: v6/publishable/paper-VII Appendix A
> items 5-9.
>
> **CORRECTION (2026-06-11, hostile-review campaign).**  Three
> repairs, all preserved in v6/publishable/paper-VII (Appendix A):
> (1) the strict form quoted 2.5 sigma against sqrt(eps) — that
> arithmetic sets m1 = 0 while the program's own spectrum asserts
> m1 = eps*m3; the SELF-CONSISTENT strict prediction is
> sqrt(eps/(1+eps)) = 0.17556, and the tension is 1.4 sigma (the
> correction reduces the tension; made because it is right).
> (2) The band C in [0.80, 1.25] is WITHDRAWN: it contradicted the
> program's own coefficient no-go (68% spread [0.22, 1.26]); the
> registered content is the EXPONENT x_nu = 1/2.  (3) The IO line
> was meaningless under IO and is deleted; IO is now an explicit
> voiding scenario.  The honest trials accounting (band-grade
> ~26%/trial; >= 3 clean lepton trials) is also in paper-VII.

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
