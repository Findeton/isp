# Relativistic ISP v7 Paper XXXIII: Intrinsic Center-Shadow-Weight Campaign

**Status:** campaign note, not peer reviewed, version 2026-06-29.

This paper attacks the sharpened missing theorem:

$$
\mathcal C_N
\to
\mathcal P_N
\to
h_{\mathcal P_N}
$$

intrinsically, without hidden presentation counts.

Here:

- `N` is the number of committed records in the finite record order.
- `\mathcal C_N` is the candidate diamond center: the smallest licensed
  boundary/collar structure needed to remove no-silent seam residue.
- `\mathcal P_N` is the physical shadow: a nonreconstructive quotient of the
  center allowed to enter the click law.
- `h_{\mathcal P_N}` is the positive effective weight on that shadow.

The target is:

$$
\Pr(P\mid C)
=
\frac{D(P,C)h_{\mathcal P_{N+1}}(P)}
{\sum_{P'}D(P',C)h_{\mathcal P_{N+1}}(P')}.
$$

Here:

- `C` is the current committed record.
- `P` is a possible next/parent record.
- `D(P,C)` is the deletion multiplicity: the number of ways deleting one
  record from `P` yields `C`.
- `h_{\mathcal P_{N+1}}(P)` is the positive weight assigned by the selected
  physical shadow at size `N+1`.

The campaign did not find the universal click law. It did something useful:
it falsified the tempting shortcuts and narrowed the living theorem to a much
smaller target.

Receipt:

```text
isp/v7/code/p33_intrinsic_center_shadow_hweight_campaign.py
```

The receipt passed:

```text
CHECKS PASSED: 10/10
```

All ranks, decks, forward laws, and total-variation distances are exact
integer/Fraction calculations. Decimal precision for transcendental roots is
`140`.

## 1. Executive Result

The missing theorem is not:

$$
\text{presentation count is determined by deletion equations}.
$$

It is not:

$$
\text{delete many records at once}.
$$

It is not:

$$
\text{use the full deletion deck as the center}.
$$

It is not:

$$
\text{use more flags until exact}.
$$

It is not:

$$
\text{RN/KL commitment alone selects }h.
$$

All five shortcuts were attacked. Each fails for a specific reason.

The surviving target is:

$$
\boxed{
\text{minimal no-silent diamond center}
\to
\text{controlled positive nonreconstructive shadow}
\to
\text{boundary-work-selected }h
}
$$

The word "boundary-work-selected" matters. Commitment supplies the exponential
term, but not the whole potential. The missing physical object is the
record-intrinsic boundary work functional:

$$
\psi_{\mathcal P_N}.
$$

Without it, the commitment term can be made to select arbitrary positive
weights.

## 2. Attack A: Deletion Projectivity

The exact hidden teacher in the 2D permutation-order sector is presentation
count:

$$
\operatorname{pres}_N(R).
$$

Here `R` is an unlabeled committed record order. `\operatorname{pres}_N(R)` is
the number of labeled 2D permutation presentations that project to `R`.

The exact forward law is easy if this hidden count is allowed:

$$
\Pr(P\mid C)
\propto
D(P,C)\operatorname{pres}_{N+1}(P).
$$

The problem is that `\operatorname{pres}` is not allowed as a primitive hidden
coordinate. It must be replaced by a record-intrinsic effective weight.

Deletion projectivity gives the exact harmonic identity:

$$
\sum_{P:D(P,C)>0}
D(P,C)\operatorname{pres}_N(P)
=
N^2\operatorname{pres}_{N-1}(C).
$$

This says presentation count is a positive harmonic function on the deletion
graph. The first hope was that this equation might determine it.

It does not.

Exact rank table:

| N | records | rank one-step | nullity one-step |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 1 |
| 3 | 5 | 2 | 3 |
| 4 | 16 | 5 | 11 |
| 5 | 63 | 16 | 47 |
| 6 | 315 | 63 | 252 |
| 7 | 1956 | 315 | 1641 |

At `N=7`, the deletion equations leave `1641` exact harmonic degrees of
freedom. So deletion projectivity is necessary, but far from sufficient.

## 3. Attack B: Delete Multiple Records At Once

The natural next opening was:

> maybe one-record deletion is too weak; delete several records at once.

For `m<N`, the exact multi-delete identity is:

$$
\sum_P D_{N\to m}(P,C)\operatorname{pres}_N(P)
=
\binom{N}{m}^2 (N-m)! \operatorname{pres}_m(C).
$$

Here:

- `D_{N\to m}(P,C)` is the number of `m`-record induced suborders of `P`
  isomorphic to `C`;
- `\binom{N}{m}^2 (N-m)!` counts the labeled extension multiplicity of an
  `m`-point permutation into an `N`-point permutation.

The exact stacked rank table is:

| N | one-step rank | all-delete rank | one-step nullity | all-delete nullity |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 |
| 3 | 2 | 2 | 3 | 3 |
| 4 | 5 | 5 | 11 | 11 |
| 5 | 16 | 16 | 47 | 47 |
| 6 | 63 | 63 | 252 | 252 |
| 7 | 315 | 315 | 1641 | 1641 |

So multi-delete adds no rank through the audited window. It is not the missing
principle.

This is an important closure: deleting multiple records at once is still
useful for defining boundary residue, but it does not by itself determine the
forward h-weight.

## 4. Attack C: Use The Full Deletion Deck As Center

Another opening was:

> maybe `\mathcal C_N` is simply the deletion deck.

For a record `R`, the one-step deck is:

$$
\operatorname{Deck}_1(R)
=
\{R\setminus x:x\in R\}.
$$

The all-delete deck is:

$$
\operatorname{Deck}_{\rm all}(R)
=
\{\operatorname{Deck}_{N\to m}(R):1\le m<N\}.
$$

The receipt tests whether these decks form useful centers.

They are exact, but only because they reconstruct the record.

| N | partition | atoms / records | forward TV |
|---:|---|---:|---:|
| 5 | deck1 | 63 / 63 | 0 |
| 5 | deckall | 63 / 63 | 0 |
| 6 | deck1 | 315 / 315 | 0 |
| 6 | deckall | 315 / 315 | 0 |
| 7 | deck1 | 1956 / 1956 | 0 |
| 7 | deckall | 1956 / 1956 | 0 |

So the full deletion deck is too strong. It is not an admissible physical
shadow, and it is not the desired center if the center must remain
nonreconstructive.

This also explains why "backward-then-forward" needs care. Deletion is the
right diagnostic, but closing under all deletion information collapses into
lookup.

## 5. Attack D: Low-Order Intrinsic Shadows

The next opening was:

> perhaps ordinary intrinsic order features are enough.

The tested known packet included:

- relation count;
- height;
- width;
- interval-count profile;
- degree moments;
- matching counts.

This packet is nonlookup, but it fails forward exactness.

| N | partition | atoms / records | presentation conflicts | forward TV |
|---:|---|---:|---:|---:|
| 5 | known | 39 / 63 | 0 | 0 |
| 6 | known | 179 / 315 | 1 | 0.000925925925925925925925926 |
| 7 | known | 999 / 1956 | 6 | 0.00285365569308605066709292 |

So the low-order packet is promising at small `N`, but it breaks at `N=6` and
worsens at `N=7`.

## 6. Attack E: Add Induced Flags

The next opening was:

> perhaps flags solve the shadow.

Flags improve the result, but the finite data shows the danger:

| N | partition | atoms / records | forward TV |
|---:|---|---:|---:|
| 5 | flags3 | 62 / 63 | 0 |
| 6 | flags3 | 309 / 315 | 0 |
| 7 | flags3 | 1893 / 1956 | 0.000330961230881204519579514 |
| 7 | flags4 | 1955 / 1956 | 0 |
| 7 | flags5 | 1956 / 1956 | 0 |

The pattern is clear:

- `flags3` remains nonlookup, but fails at `N=7`;
- `flags4` becomes exact at `N=7`, but only as near-lookup;
- `flags5` is lookup.

Thus "just add flags" is not the law. It reproduces the forward law by
approaching reconstruction.

The Paper 30 diamond-shadow result is different. It achieved exact held-out
forward law at `N=9` with:

$$
65521/131526
$$

atoms, i.e. about:

$$
0.498160059607986253668476
$$

of record lookup. That is a genuinely nonreconstructive witness.

## 7. Attack F: Commitment Alone

The v6 commitment law gives:

$$
S(I+J)=S(I)S(J),
\qquad
S(I)=e^{-I}.
$$

It also gives the scalar fixed point:

$$
\tanh(h)=e^{-h}.
$$

The receipt solved:

$$
h_{\rm commit}
=
0.6093778634360062315368033711683986954285392793128541477762892366225152051203195768397057073419585497249233347078073628047232738007518566486.
$$

It also solved the one-diamond Diamond Work-Balance root:

$$
\eta_*
=
1.0903443548794921962205077083509499533582197857502947304430449706378495187012211801530749701632256720938879002552211976806351593056361869318.
$$

These are distinct. The gap is large enough that they should not be identified.

The deeper problem is that commitment alone does not select a vector h-weight.
For a candidate shadow with coordinates `h_j`, v6 suggests:

$$
\Phi(h)
=
\psi(h)+\sum_j e^{-h_j},
$$

with the stationary equation:

$$
\nabla\psi(h)=e^{-h}.
$$

But if `\psi` is not fixed by record data, this selects nothing. For any
positive target `h^*`, one can build a strictly convex potential with:

$$
\nabla\psi(h^*)=e^{-h^*}.
$$

The receipt checked this explicitly for:

$$
h^*=(0.37,1.41,2.03),
$$

with stationarity residual:

$$
0E-140.
$$

Therefore:

$$
\text{commitment term}
\ne
\text{complete h-law}.
$$

The missing object is:

$$
\psi_{\mathcal P_N},
$$

the boundary-work potential generated by the selected primitive quotient
ledger.

## 8. Surviving Route

All easy routes failed. The finite Paper 30/31 route survives:

```text
N=9 center  = 131518 / 131526
N=9 shadow  = 65521 / 131526
TV9         = 0
rec9        = 0
qrec9       = 0
```

This is the only audited object in the campaign that is both:

1. exact for the held-out forward law; and
2. substantially nonreconstructive.

Its interpretation is now sharper:

$$
\mathcal C_N
\ne
\operatorname{Deck}(R),
$$

and:

$$
\mathcal P_N
\ne
\text{arbitrary flag list}.
$$

Instead:

$$
\mathcal C_N
=
\text{minimal no-silent whole-history diamond center},
$$

and:

$$
\mathcal P_N
=
\text{coarsest admissible positive shadow of that center}.
$$

## 9. Updated Theorem Target

The right theorem should have this shape.

### 9.1 Center

For every committed finite record diamond `R`, construct a boundary/collar
transport ledger:

$$
B_R\to T_R\to \mathcal C_R.
$$

Here:

- `B_R` is the boundary/collar data;
- `T_R` is the record-intrinsic transport or conditional-information object;
- `\mathcal C_R` is the minimal no-silent center.

The center is not allowed to be full deletion-deck lookup. It must be generated
only by residue that cannot be silently washed out.

### 9.2 Shadow

Among quotients:

$$
\mathcal P_R\preceq\mathcal C_R,
$$

select the coarsest one satisfying:

- exact or asymptotically exact deletion harmonicity;
- controlled insertion/deletion drift;
- reflection positivity;
- dual compatibility;
- density/regularity stability;
- nonreconstruction.

This is where the Paper 30 dual-even/quadratic-dual-odd metric belongs. It is
not a flag rule. It is a finite coordinate witness for an admissible positive
shadow.

### 9.3 Weight

On the primitive quotient ledger of `\mathcal P_N`, derive:

$$
\psi_{\mathcal P_N}.
$$

Then select:

$$
h_{\mathcal P_N}
=
\operatorname*{argmin}_h
\left(
\psi_{\mathcal P_N}(h)+\sum_j e^{-h_j}
\right).
$$

This is the first form that avoids both hidden presentation counts and arbitrary
commitment potentials.

## 10. Hostile Review

### Review 1: "Deletion should have solved it."

Rejected by exact rank.

At `N=7`, deletion projectivity leaves `1641` harmonic degrees of freedom.
Deletion is necessary, not sufficient.

### Review 2: "Delete multiple records at once."

Rejected by exact rank.

Through `N=7`, all lower-deletion equations have the same rank as one-step
deletion.

### Review 3: "Use the whole deletion deck."

Rejected by reconstruction.

The one-step and all-delete decks are exact because they become lookup at
`N=5,6,7`.

### Review 4: "Use ordinary intrinsic features."

Rejected by forward error.

Known low-order sectors are nonlookup but fail at `N=6` and `N=7`.

### Review 5: "Use flags."

Rejected as a universal principle.

Flags improve prediction, but exactness arrives by near-lookup in the audited
simple family. The real finite witness is the diamond shadow, which is much
coarser.

### Review 6: "Use commitment."

Rejected as incomplete.

Commitment gives the exponential term. It does not provide `\psi`. Without
`\psi`, arbitrary positive h-vectors can be made stationary.

### Review 7: "Then nothing was found."

Rejected.

The campaign did not close the law, but it ruled out the main false routes.
The remaining theorem is small enough to state:

$$
\boxed{
\text{derive the primitive boundary-work potential } \psi_{\mathcal P_N}
\text{ from the no-silent diamond center.}
}
$$

That is the missing bridge between v6 diamonds and the v7 h-transform.

## 11. Bottom Line

The law is still hidden, but its hiding place is now much narrower.

The final click law is probably not:

$$
\Pr(P\mid C)\propto D(P,C)\operatorname{pres}(P),
$$

because `\operatorname{pres}` is hidden.

It is probably:

$$
\Pr(P\mid C)
=
\frac{D(P,C)h_{\mathcal P_{N+1}}(P)}
{\sum_{P'}D(P',C)h_{\mathcal P_{N+1}}(P')},
$$

where:

$$
\mathcal P_N
=
\text{coarsest admissible positive shadow of the no-silent diamond center},
$$

and:

$$
h_{\mathcal P_N}
=
\text{commitment minimizer for the primitive boundary-work potential}.
$$

The exact missing object is not another flag, another scalar, or another
deletion deck. It is:

$$
\boxed{\psi_{\mathcal P_N}}
$$

the record-intrinsic boundary-work potential of the selected positive shadow.

