# CRL coupling-family addendum: isospectrality and calibrated visibility

**Recorded:** 2026-08-18, v16 ledger #119.

**Status:** post-#118 exploratory audit addendum. This is neither a Paper 10
pin nor a physics result. It narrows an external response to the #118 audit
and leaves QSF, WRC, and the Paper 10 hold unchanged.

## 1. Family tested

Keep the exposed CRL matter controls, real `3-4-5` coin, shift writer `W`, and
`Z_4` register. Replace the clock factor in `T` by

```text
C^k,                    k in {0,1,2,3},
```

so its record phase is `i^(kn)`. Let

```text
E_k = T_k W,
Omega_k = (W T_k)^dagger (T_k W).
```

The external response claims that all four `Omega_k` have one characteristic
polynomial, while fixed-calibration multi-tick counts distinguish some `k`.
Independent exact reconstruction confirms both facts.

## 2. Exact isospectrality

For every `k=0,1,2,3`, Faddeev-LeVerrier reconstruction over Gaussian
rationals returns

```text
charpoly(Omega_k)
 = (x-1)^2
   (x^2 + (14/25)x + 1)
   (x^2 - (18/25)x + 1)^2.
```

Therefore every conjugacy-invariant spectral function of this one-event
holonomy family is `k`-blind. In particular, the trace is `72/25`, the five
distinct eigenvalues are the #118 set, and no spectral classifier can recover
the clock power.

Because each `Omega_k` is unitary and the multiplicities agree, the four are
unitarily similar as **unlabelled operators**. This makes the correct lesson
representation-sensitive: `k` cannot be physical from `Omega_k` alone; it can
only be physical relative to fixed preparations, observables, and event
labels.

## 3. “Multi-event only” is too strong

The matrices are isospectral but not equal. An exact entry already moves:

```text
(Omega_k)_(0,5) = (12/25) i^k.
```

Consequently the one-event state-fed quantity for

```text
|s> = (|0>+|5>)/sqrt(2)
```

is

| `k` | `<s|Omega_k|s>` |
|---:|---:|
| 0 | `9/25` |
| 1 | `9/25 + 12i/25` |
| 2 | `9/25` |
| 3 | `9/25 - 12i/25` |

Thus the coupling is not invisible to every one-event probe. Its imaginary
part is measurable after a phase-reference/Hadamard-test-type calibration.
The external phrase “dynamical, multi-event, state-relative” must be narrowed
to **state/observable-relative rather than spectrally intrinsic**; multiple
events are sufficient in the exposed count assay but not necessary in
principle.

This state-fed witness was found after exposure and cannot become a
pre-registered Paper 10 success. It is a control that tells a future pin what
must be frozen before running.

## 4. The `k` versus `-k` degeneracy is a real-slice theorem

For the exposed law, `W` and the coin are real, so

```text
E_{-k} = conjugate(E_k).
```

For every real initial vector and every computational-basis count projector,
complex conjugation leaves probabilities unchanged. Hence `k=1` and `k=3`
are count-indistinguishable at **every tick** on the registered real
calibration, not merely at tick four.

The degeneracy is not universal. With the normalized complex seed
`(3/5,4i/5)`, it breaks at tick three:

```text
k=1: [1296, 12304,  1296, 729] / 15625,
k=3: [1296,  3088, 10512, 729] / 15625.
```

Therefore chirality is hidden by the real preparation/measurement slice. A
future claim of physical orientation needs a declared complex phase reference
or an equivalent relational calibration; no open-ended search for an
unspecified observable is required at this fixture.

## 5. The exact fourth-tick family

For the registered real seed `(3/5,4/5)`, the coherent count distributions at
tick four are

```text
k=0: [18225, 262800,  77200,  32400] / 390625,
k=1: [18225,  64656, 192400, 115344] / 390625,
k=2: [18225,  32400, 307600,  32400] / 390625,
k=3: [18225,  64656, 192400, 115344] / 390625.
```

This proves that the clock power moves a fixed calibrated multi-event
observable while the one-event spectral multiset remains fixed. It does not
select a power, make the power gauge-invariant under the future relational
theory, or turn the register into geometry.

## 6. Corrected disposition

The external response correctly withdraws centrality, two-eigenphase stratum
membership, and curvature. Its isospectrality finding is exact. Two further
qualifications are binding:

1. “duality-forced” still means forced only after declaring the cyclic
   register, representation, and generator powers; and
2. “coupling physical” is presently **calibration-relative toy content**. A
   future graph law must quotient its allowed record-basis automorphisms and
   show that a held-out observable still moves.

The corrected family statement is

```text
BARE-WEYL-RELATION-EXACT-CONDITIONAL-ON-THE-DECLARED-Z4-PAIR;
EVENT-HOLONOMY-NONCENTRAL-FIVE-PHASE-AND-K-ISOSPECTRAL;
K-VISIBLE-RELATIVE-TO-FIXED-STATES-AND-OBSERVABLES;
K-AND-MINUS-K-BLIND-ON-THE-REAL-COUNT-SLICE-BUT-NOT-GENERALLY;
CURVATURE-GEOMETRY-AND-COUPLING-SELECTION-UNBUILT.
```

## 7. Consequence for Paper 10

This addendum improves a possible CRL module; it does not make the current
toy a Paper 10 pin. The next result-neutral instrument still needs the #118
and Q30/Q31 requirements. In particular it must freeze before execution:

- the allowed record-basis gauge/automorphism group;
- a graph-generated plaquette rather than an isolated event-order loop;
- both spectral and state-fed loop observables;
- real-slice and complex-reference chirality controls;
- multiple `k`, coin, seed, and `q` rivals;
- local causal/no-signalling and durable-division constructions; and
- held-out graph growth plus E-37 parity adversaries.

An abelian sub-fixture with central holonomy would show only that such a sector
exists. The word **curvature** is earned only if the same joint graph law
generates a gauge-invariant loop response that survives these controls and
does geometric work elsewhere in the fixture.

## 8. The later `q=3` extrapolation does not select a law

A later external response reports that a `q=3` run first splits at tick three
and calls `q=3` “the corpus dial.” The timing is consistent with an independent
generalization of the exposed `3-4-5`-coin construction. It reinforces only
the already registered conclusion that split time is dial- and seed-relative.

The rest of the promotion is not licensed:

1. CRL's `q` is the cardinality of a cyclic **record register**. WRC's use of
   Eisenstein arithmetic does not identify that register with a WRC object or
   derive its cardinality. Equal roots of unity in neighboring formulas are
   not an ontological weld.
2. The supplied source has a two-state matter fiber and the rational
   `3-4-5` coin. No hashed `q=3` Grover-coin successor, redundancy division,
   winding-growth map, or nine-family regression was supplied. Those phrases
   describe a proposed new object, not the audited law.
3. The #118 five-phase ledger is specific to `q=4`. Exact reconstruction of
   the same rational-coin construction at `q=3` gives, for every
   `k=0,1,2`,

   ```text
   charpoly(Omega_k)
    = (x-1)^2 (x^2 - (2/25)x + 1)^2,
   ```

   hence **three** distinct phases, not five. Results cannot be transported
   between these dials without rerunning every gate.
4. “The split's existence is generic” has not been proved. The exact control
   `R=I` has no matter mixing and gives identical coherent and measured count
   distributions at every tick for every seed. A future census may find an
   open dense splitting class under specified nondegeneracy conditions, but
   a handful of positive seeds and dials does not establish that theorem.

The assertion that CRL contains the committed walk as its “unlawful
sample-every-write shadow” also remains false for the reason in #118: CRL's
sampled step collapses to a basis ray and is a lawful instrument, whereas WRC
retains an input-dependent noncollapsed ray and QSF finds that the displayed
projective law preserves `0/9` WRC observable families.

Finally, “maximally forced” is not a measured status. Even before graph growth,
the form still declares the record catalogue, `q`, generator powers, control
projectors, coin, circuit ordering, and preparation. Division redundancy,
growth-at-winding, locality, coupling recurrence, and actualization add more
law data. Calling these “dials” is honest pricing; it does not make their
values or the surrounding form derived.

The claimed meta-theorem is also too broad. The adjudicated units establish
nonselection by their **registered finite consistency surfaces**. They do not
prove that no deeper principle or larger arena can select a law. Likewise,
regression, spatial no-signalling, and a discriminator census are necessary
contacts for CRL, not the only remaining contacts. Passing all three would
still leave the graph-generated successor, durable division construction,
carrier growth, geometric irreducibility, continuum recovery, and mapping to
real experimental observables open. CRL is not one census away from being a
law of nature.
