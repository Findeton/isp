# Relativistic ISP v7 Paper XXXIV: Boundary-Work Potential Campaign

**Status:** campaign note, not peer reviewed, version 2026-06-29.

Paper XXXIII narrowed the missing click-law theorem to:

$$
\mathcal C_N
\to
\mathcal P_N
\to
h_{\mathcal P_N}.
$$

The missing object was identified as:

$$
\psi_{\mathcal P_N},
$$

the record-intrinsic boundary-work potential whose commitment minimizer gives
the positive h-weight on the selected shadow.

This paper attacks that object directly.

Receipt:

```text
isp/v7/code/p34_boundary_work_potential_campaign.py
```

The receipt passed:

```text
CHECKS PASSED: 9/9
```

All record/deck/forward-law calculations are exact integer/Fraction
calculations. Decimal precision for transcendental roots is `140`.

## 1. Executive Result

The campaign did not derive the final boundary-work potential.

But it found a stronger bridge than expected:

> deletion and insertion drift exactly self-identify the selected positive
> shadow at the audited levels, while the shadow remains nonlookup at the
> record level.

At `N=6`:

```text
selected shadow atoms = 180 / 315
TV_5_to_6             = 0
```

At `N=7`:

```text
selected shadow atoms = 1018 / 1956
TV_6_to_7             = 0
```

The smaller descriptors fail:

- metric-only is too coarse;
- known low-order data is too coarse;
- atom-size is too coarse.

But deletion drift and insertion drift recover the selected shadow exactly:

```text
N=6 delete cells = 180 / 180 shadow cells
N=6 insert cells = 180 / 180 shadow cells

N=7 delete cells = 1018 / 1018 shadow cells
N=7 insert cells = 1018 / 1018 shadow cells
```

So the new target is not:

$$
\psi
=
\text{a scalar function of metric-only or drift-size data}.
$$

It is:

$$
\boxed{
\psi_{\mathcal P_N}
=
\text{boundary-work functional on the deletion/insertion coalgebra of }
\mathcal P_N
}
$$

The shadow itself appears to be a drift-stable coalgebra object.

## 2. Setup

The campaign used the Paper XXX selected positive shadow:

$$
\mathcal P_N
=
\left(
\text{known order packet},
E_{\rm total},
Q_{\rm odd}
\right),
$$

where:

$$
E_{\rm total}
=
\sum_j(F_j+F_j^*),
$$

and:

$$
Q_{\rm odd}
=
\sum_j m_j(F_j-F_j^*)^2.
$$

The selected dual-sector pairs are:

$$
(912,25104),
\qquad
(17288,525076),
\qquad
(24576,540672),
$$

and the selected odd quadratic metric is:

$$
(m_1,m_2,m_3)=(5,5,3).
$$

For each shadow atom `A`, the extracted effective h-weight is the exact
atom-average presentation count:

$$
h(A)
=
\frac{1}{|A|}
\sum_{R\in A}
\operatorname{pres}(R).
$$

This is still a teacher value. The question is whether a smaller
record-intrinsic boundary-work descriptor determines it.

## 3. Tested Boundary-Work Descriptors

The campaign tested these descriptors over selected shadow atoms:

1. `metric`: only `(E_total,Q_odd)`;
2. `known`: only the known scalar/interval/regularity/matching packet;
3. `atom_size`: the number of records in the atom;
4. `delete`: the deletion profile into child shadow atoms;
5. `insert`: the insertion profile into parent shadow atoms;
6. `delete_insert`: both deletion and insertion profiles;
7. `metric_delete_insert`: metric plus drift;
8. `known_metric_delete_insert`: known packet plus metric plus drift;
9. `shadow`: the selected shadow atom itself.

For a descriptor to replace the shadow as `\psi` input, it should ideally:

- determine `h`;
- preserve exact forward prediction;
- be coarser than the selected shadow;
- remain nonlookup at the record level.

The first two requirements are exact. The third is the nonreconstruction
pressure.

## 4. N=6 Results

At `N=6`, the selected shadow has:

```text
180 atoms / 315 records
TV_5_to_6 = 0
```

Descriptor scan:

| descriptor | cells / shadow atoms | h conflicts | TV |
|---|---:|---:|---:|
| metric | 15 / 180 | 10 | 0.108475207209513006352488 |
| known | 179 / 180 | 1 | 0.000925925925925925925925926 |
| atom_size | 3 / 180 | 2 | 0.110938680139298342408085 |
| delete | 180 / 180 | 0 | 0 |
| insert | 180 / 180 | 0 | 0 |
| delete_insert | 180 / 180 | 0 | 0 |
| metric_delete_insert | 180 / 180 | 0 | 0 |
| known_metric_delete_insert | 180 / 180 | 0 | 0 |
| shadow | 180 / 180 | 0 | 0 |

Interpretation:

- metric-only and atom-size are far too coarse;
- known data is almost enough, but still fails;
- deletion drift and insertion drift exactly recover the selected shadow.

## 5. N=7 Results

At `N=7`, the selected shadow has:

```text
1018 atoms / 1956 records
TV_6_to_7 = 0
```

Descriptor scan:

| descriptor | cells / shadow atoms | h conflicts | TV |
|---|---:|---:|---:|
| metric | 107 / 1018 | 45 | 0.104711388455767167347662 |
| known | 999 / 1018 | 6 | 0.00285365569308605066709292 |
| atom_size | 3 / 1018 | 3 | 0.111380458675619873771261 |
| delete | 1018 / 1018 | 0 | 0 |
| insert | 1018 / 1018 | 0 | 0 |
| delete_insert | 1018 / 1018 | 0 | 0 |
| metric_delete_insert | 1018 / 1018 | 0 | 0 |
| known_metric_delete_insert | 1018 / 1018 | 0 | 0 |
| shadow | 1018 / 1018 | 0 | 0 |

The result repeats at the next level. Deletion and insertion drift do not
compress the shadow, but they identify it exactly.

This is not a failure. It is a strong structural clue:

$$
\mathcal P_N
\quad\text{is a fixed point of its deletion/insertion drift profile.}
$$

## 6. Commitment Alone Still Does Not Fix Psi

The v6 commitment scalar is:

$$
\tanh(h)=e^{-h}.
$$

The receipt solved:

$$
h_{\rm commit}
=
0.6093778634360062315368033711683986954285392793128541477762892366225152051203195768397057073419585497249233347078073628047232738007518566486.
$$

Residual:

$$
-3E-140.
$$

But commitment alone still cannot identify `\psi`.

For arbitrary targets:

$$
(0.41,0.83,1.97),
$$

one can build a strictly convex potential centered at those targets, with
stationarity residual:

$$
0E-140.
$$

So the theorem cannot say only:

$$
\nabla\psi(h)=e^{-h}.
$$

It must derive the physical `\psi` from the drift-stable shadow itself.

## 7. What Changed

Before this campaign, the missing object looked like a smaller scalar
boundary-work descriptor. The campaign falsifies that expectation.

The smaller descriptors fail:

$$
\text{metric-only},\quad
\text{known-only},\quad
\text{atom-size}.
$$

The drift descriptors succeed, but only by identifying the selected shadow:

$$
\operatorname{DeleteProfile}(\mathcal P_N)
\equiv
\mathcal P_N,
$$

and:

$$
\operatorname{InsertProfile}(\mathcal P_N)
\equiv
\mathcal P_N
$$

in the audited window.

So `\psi_{\mathcal P_N}` should not be sought on a smaller scalar quotient. It
should be sought on the deletion/insertion coalgebra of the selected shadow.

## 8. Updated Theorem Target

The living theorem is:

> Among nonlookup quotients of the no-silent diamond center, the physical
> shadow is the coarsest quotient whose deletion and insertion profiles
> self-identify it and whose RN/KL boundary-work potential has a commitment
> minimizer giving the positive h-transform weight.

More formally:

1. Construct the no-silent diamond center:

   $$
   \mathcal C_N.
   $$

2. Search quotients:

   $$
   \mathcal P_N\preceq\mathcal C_N.
   $$

3. Require drift self-identification:

   $$
   \operatorname{Del}(\mathcal P_N)
   \simeq
   \mathcal P_N,
   \qquad
   \operatorname{Ins}(\mathcal P_N)
   \simeq
   \mathcal P_N.
   $$

4. Require nonlookup:

   $$
   |\mathcal P_N|
   \ll
   |\text{records}_N|.
   $$

5. Derive boundary work:

   $$
   \psi_{\mathcal P_N}
   =
   \text{RN/KL work of this drift-stable shadow coalgebra}.
   $$

6. Select h by commitment:

   $$
   h_{\mathcal P_N}
   =
   \operatorname*{argmin}_h
   \left(
   \psi_{\mathcal P_N}(h)+\sum_j e^{-h_j}
   \right).
   $$

7. Use the h-transform:

   $$
   \Pr(P\mid C)
   =
   \frac{D(P,C)h_{\mathcal P_{N+1}}(P)}
   {\sum_{P'}D(P',C)h_{\mathcal P_{N+1}}(P')}.
   $$

## 9. Hostile Review

### Review 1: "This still uses atom-average presentation counts."

Sustained.

The extracted h is still teacher h. The campaign does not derive h. It shows
where h must live: on a drift-stable shadow coalgebra.

### Review 2: "Delete and insert profiles are just another way to name the shadow."

Sustained, and important.

They are exactly another way to name the shadow in the audited window. The
point is that this naming is record-intrinsic and nonlookup at the record
level. It is not a hidden presentation label.

### Review 3: "No smaller descriptor was found."

Sustained.

The campaign searched metric-only, known-only, atom-size, deletion, insertion,
and combinations. No exact descriptor was both coarser than the shadow and
predictive.

### Review 4: "Commitment still does not supply psi."

Sustained.

Commitment supplies the exponential term. The physical boundary-work potential
must be derived from the shadow coalgebra.

### Review 5: "Is this enough for the click law?"

No.

The result is a structural bridge, not the final law. The final missing step is
to construct:

$$
\psi_{\mathcal P_N}
$$

from the deletion/insertion coalgebra itself.

## 10. Bottom Line

The campaign found a real new invariant:

$$
\boxed{
\mathcal P_N
\text{ is self-identified by deletion and insertion drift}
}
$$

for the audited selected shadow at `N=6` and `N=7`.

This means the positive shadow is not an arbitrary feature packet. It behaves
like a stable coalgebra under the record deletion/insertion operators.

The click law is still not closed, but the missing object has moved:

from:

$$
\text{find a smaller scalar boundary-work descriptor}
$$

to:

$$
\boxed{
\text{derive the RN/KL boundary-work potential on the drift-stable shadow
coalgebra}
}
$$

That is the next exact theorem.

