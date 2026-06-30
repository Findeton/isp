# Relativistic ISP v7 Paper XXXV: Shadow-Coalgebra Variational Recurrence

**Status:** campaign note, not peer reviewed, version 2026-06-29.

Paper XXXIV found that the selected positive shadow is self-identified by its
deletion/insertion drift. This paper asks the next question:

> does the deletion/insertion coalgebra determine the h-weight, and can the
> boundary-work potential `\psi_{\mathcal P_N}` be reduced to a smaller
> invariant recurrence?

Receipt:

```text
isp/v7/code/p35_shadow_coalgebra_variational_recurrence.py
```

The receipt passed:

```text
CHECKS PASSED: 9/9
```

All combinatorial calculations are exact integer/Fraction calculations. Decimal
precision for the commitment fixed point is `140`.

## 1. Executive Result

The campaign found a new positive bridge:

$$
\boxed{
\text{scalar-work quotient}
\Rightarrow
\text{exact h-transform weights}
}
$$

at `N=6` and `N=7`.

The scalar-work quotient is:

$$
\mathcal W_N
=
\left(
M,
|A|,
\operatorname{DelScal}(A),
\operatorname{InsScal}(A)
\right),
$$

where:

- `A` is an atom of the selected positive shadow;
- `M` is the selected odd quadratic metric channel;
- `|A|` is the number of records in the atom;
- `\operatorname{DelScal}(A)` is the scalar summary of the deletion profile of
  atom `A`;
- `\operatorname{InsScal}(A)` is the scalar summary of the insertion profile of
  atom `A`.

This quotient is strictly coarser than the selected shadow:

```text
N=6: scalar-work cells = 156 / 180 shadow atoms
N=7: scalar-work cells = 748 / 1018 shadow atoms
```

and still gives exact forward h-transform prediction:

```text
N=6: TV_5_to_6 = 0
N=7: TV_6_to_7 = 0
```

This is the first campaign result after Paper XXXI where a smaller
record-intrinsic quotient of the selected shadow still carries the exact
effective h-weight in the audited window.

## 2. The Selected Shadow Is Aggregate, Not Strong

The first test asked whether the selected shadow is strongly lumpable
record-by-record.

It is not.

At `N=6`:

```text
strong deletion conflicts  = 2
strong insertion conflicts = 2
```

At `N=7`:

```text
strong deletion conflicts  = 15
strong insertion conflicts = 15
```

So records inside the same shadow atom do not all have identical individual
deletion/insertion profiles.

But the aggregate atom profiles are exact.

At `N=6`:

```text
aggregate delete cells        = 180 / 180
aggregate insert cells        = 180 / 180
aggregate delete_insert cells = 180 / 180
```

At `N=7`:

```text
aggregate delete cells        = 1018 / 1018
aggregate insert cells        = 1018 / 1018
aggregate delete_insert cells = 1018 / 1018
```

Thus the selected shadow is an aggregate coalgebra object. It is not a strict
Markov lump at the record level.

This matters. The law should not demand record-by-record lumpability. It should
demand aggregate no-silent boundary work.

## 3. The Aggregate h-Recurrence Is Exact But Underdetermined

Let:

$$
D_{B\to A}
$$

be the total number of deletion edges from parent shadow atom `B` to child
shadow atom `A`.

The aggregate recurrence is:

$$
\sum_B D_{B\to A}h_B
=
N^2 |A| h_A.
$$

Here:

- `N` is the parent record count;
- `A` is a child shadow atom;
- `B` is a parent shadow atom;
- `|A|` is the number of records in atom `A`;
- `h_A` and `h_B` are exact atom-average presentation weights.

The recurrence is exact:

```text
5 -> 6: max_error = 0
6 -> 7: max_error = 0
```

But it is underdetermined:

| step | rows | columns | rank | nullity |
|---|---:|---:|---:|---:|
| 5 -> 6 | 39 | 180 | 39 | 141 |
| 6 -> 7 | 180 | 1018 | 180 | 838 |

So bare coalgebra recurrence does not determine `h`.

This closes another tempting route:

$$
\text{recurrence exactness}
\ne
\text{h-law}.
$$

The variational principle still matters.

## 4. Scalar Descriptor Attacks

The campaign then tested whether smaller scalar descriptors determine h.

At `N=7`:

| descriptor | cells | h conflicts |
|---|---:|---:|
| metric | 107 | 45 |
| known | 999 | 6 |
| size | 3 | 3 |
| delete_scalar | 32 | 18 |
| insert_scalar | 466 | 15 |
| scalar_work | 748 | 0 |
| full_drift | 1018 | 0 |

The separate ingredients fail:

- metric alone fails;
- known order packet fails;
- atom size fails;
- deletion scalar alone fails;
- insertion scalar alone fails.

But the combined scalar-work packet succeeds:

$$
\mathcal W_N
=
\left(
M,
|A|,
\operatorname{DelScal}(A),
\operatorname{InsScal}(A)
\right).
$$

At `N=6`:

```text
scalar_work cells = 156 / 180
h conflicts       = 0
TV                = 0
```

At `N=7`:

```text
scalar_work cells = 748 / 1018
h conflicts       = 0
TV                = 0
```

This is not merely self-identifying the whole shadow. Full drift has:

```text
N=7 full_drift cells = 1018
```

while scalar-work has:

```text
N=7 scalar_work cells = 748
```

So the scalar-work quotient compresses the selected shadow by about:

$$
1-\frac{748}{1018}
\approx
26.5\%.
$$

and still preserves the exact h-transform weights.

## 5. Commitment Still Supplies Only The Exponential Term

The v6 commitment fixed point is:

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

But commitment alone still does not determine the physical potential. A
strictly convex potential can be centered on arbitrary targets unless the
record law supplies the physical `\psi`.

The new result says where to look:

$$
\psi
\quad\text{should live on}\quad
\mathcal W_N.
$$

## 6. Updated Theorem Target

The theorem target changes again.

Before Paper XXXV:

$$
\psi_{\mathcal P_N}
=
\text{boundary work on the drift-stable shadow coalgebra}.
$$

After Paper XXXV:

$$
\boxed{
\psi_{\mathcal W_N}
=
\text{RN/KL boundary work on the scalar-work quotient of the shadow coalgebra}
}
$$

The click law should be:

1. Build the no-silent diamond center:

   $$
   \mathcal C_N.
   $$

2. Select the positive nonreconstructive shadow:

   $$
   \mathcal P_N\preceq\mathcal C_N.
   $$

3. Compress the shadow to its scalar-work quotient:

   $$
   \mathcal W_N
   =
   \left(
   M,
   |A|,
   \operatorname{DelScal}(A),
   \operatorname{InsScal}(A)
   \right).
   $$

4. Derive the RN/KL boundary-work potential:

   $$
   \psi_{\mathcal W_N}.
   $$

5. Select h by commitment:

   $$
   h_{\mathcal W_N}
   =
   \operatorname*{argmin}_h
   \left(
   \psi_{\mathcal W_N}(h)+\sum_j e^{-h_j}
   \right).
   $$

6. Use:

   $$
   \Pr(P\mid C)
   =
   \frac{D(P,C)h_{\mathcal W_{N+1}}(P)}
   {\sum_{P'}D(P',C)h_{\mathcal W_{N+1}}(P')}.
   $$

## 7. Hostile Review

### Review 1: "This is still extracted from hidden presentation count."

Sustained.

The h-values are still teacher h-values. The campaign proves that the
scalar-work quotient can carry them exactly in the audited window. It does not
derive the potential.

### Review 2: "The recurrence is exact, so why not stop?"

Rejected.

The recurrence has nullity `141` at `5->6` and `838` at `6->7`. Exact
recurrence does not select h.

### Review 3: "The selected shadow is not strongly lumpable."

Sustained.

The law must be aggregate/coarse-grained, not a strong Markov lump at the
record level. This fits the record ontology: records do not exist as isolated
single arrows; they live in finite diamond contexts.

### Review 4: "Scalar work may be accidental at N=6,7."

Sustained.

The campaign does not prove universality. The next test is `N=8` and then
compatibility with the Paper XXX/XXXI `N=9` selected shadow.

### Review 5: "What is new?"

The new object is:

$$
\mathcal W_N.
$$

It is the first proper coarser quotient of the selected shadow that preserves
the exact h-transform weight in the audited levels.

## 8. Next Campaign

The immediate next campaign should test whether `\mathcal W_N` survives:

1. `N=8` h-weight extraction;
2. `N=8 -> 9` recurrence when feasible;
3. compatibility with Paper XXX's `N=9` diamond-boundary center;
4. adversarial comparison with other quotients of the selected shadow;
5. search for a closed formula for:

   $$
   \psi_{\mathcal W_N}.
   $$

If `\mathcal W_N` survives those tests, it is probably not just a descriptor.
It is the actual finite carrier of the boundary-work potential.

## 9. Bottom Line

Paper XXXV found the strongest positive result since the diamond-shadow
closure:

$$
\boxed{
\mathcal W_N
=
(M, |A|, \operatorname{DelScal}(A), \operatorname{InsScal}(A))
}
$$

is a proper coarser quotient of the selected positive shadow and carries the
exact h-transform weights at `N=6` and `N=7`.

The click law is still not closed. But the missing `\psi` has a much better
candidate domain:

$$
\boxed{
\psi\text{ lives on the scalar-work quotient }\mathcal W_N,
\text{ not on the whole shadow and not on bare recurrence.}
}
$$

