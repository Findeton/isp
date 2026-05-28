# Tier 2 Finite-Slab Free Stochastic-Curvature Theorem

Author: Felix Robles Elvira

Date: 2026-05-12

Status: theorem-level proof for a narrow, explicit finite-slab lift. The theorem uses log-smeared finite comparison maps built from the exact singleton collar-excision comparison maps. It proves the finite-slab stochastic-curvature limit under a very-thin-slab scaling condition.

Scope warning: this proves a canonical log-smeared Tier 2 theorem. It does not prove that every possible smooth-lapse primitive-kernel regularization has the same finite-slab limit. In particular, it does not yet prove a weighted-Hamiltonian primitive-kernel theorem, an all-support theorem, an all-order regulator theorem, or any interacting/gauge/gravity extension.

## 1. Statement

Let `N,M` be smooth compactly supported real lapse profiles on the line, and let `phi` be a smooth compactly supported two-component spinor. Put

```math
\beta=N\partial_xM-M\partial_xN.
```

Let

```math
(\iota_a\phi)_{n,s}=a^{1/2}\phi_s(an)
```

be the lattice sampling map on a periodic lattice whose seam is outside the supports of `N`, `M`, and `phi` for all sufficiently small `a`.

For `0<lambda<=1`, let `J_{n,lambda}(a,Delta)` be the exact singleton comparison map of the free one-particle lattice Dirac model:

```math
J_{n,\lambda}(a,\Delta)
=
\Gamma\left(e^{-i\Delta(H_D-\lambda C_n)}\right)\Gamma_0(\Delta)^{-1},
```

where

```math
\Gamma_0(\Delta)=\Gamma(e^{-i\Delta H_D}),
\qquad
c_\lambda=\lambda(2-\lambda).
```

For small enough `Delta/a`, take the principal logarithm of `J_{n,lambda}` and define the log-smeared finite comparison map

```math
\mathbb J_{a,\Delta}^{(\lambda)}[N]
:=
\exp\left(a\sum_n N(an)\log J_{n,\lambda}(a,\Delta)\right).
```

Define the finite-slab exchange defect

```math
\mathbb E_{a,\Delta}^{(\lambda)}[N,M]
:=
\mathbb J_{a,\Delta}^{(\lambda)}[N]
\mathbb J_{a,\Delta}^{(\lambda)}[M]
\mathbb J_{a,\Delta}^{(\lambda)}[N]^{-1}
\mathbb J_{a,\Delta}^{(\lambda)}[M]^{-1}.
```

Assume a coupled very-thin-slab limit

```math
a\to0,
\qquad
\Delta=\Delta(a)\to0,
\qquad
\frac{\Delta(a)}{a^2}\to0.
```

Then

```math
\left\|
\frac{1}{c_\lambda^2\Delta(a)^4}
\left(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I\right)
\iota_a\phi
-
\iota_a K_\parallel[\beta]\phi
\right\|_{\ell^2}
\to0,
```

where

```math
K_\parallel[\beta]
=
\left(\beta\partial_x+\frac12\partial_x\beta\right)(I-\alpha).
```

Equivalently, the Tier 2 normalization for this log-smeared finite-slab construction is

```math
Z_{a,\Delta}^{(\lambda)}=c_\lambda^{-2}\Delta^{-4}.
```

## 2. Why This Is A Finite-Slab Object

The construction uses the exact finite-slab comparison maps `J_{n,lambda}(a,Delta)`, not only their coefficients. The smearing is done at the level of their logarithms:

```math
a\sum_nN_n\log J_{n,\lambda}(a,\Delta).
```

This is the finite-slab analog of the coefficient-level smeared deformation

```math
\mathcal K_{a,\lambda}[N]
=
a\sum_nN_nA_{n,\lambda}^{(1)}.
```

The logarithmic definition has three advantages.

1. It is exact at finite lattice spacing and finite slab size wherever the principal logarithms exist.
2. It gives a canonical smooth-lapse map for non-integer and sign-changing lapse profiles.
3. Its leading small-slab coefficient is exactly the coefficient-level object proved in Tier 1.

The price is that this is a particular finite-slab lift. A different primitive smooth-lapse Hamiltonian regularization would need its own proof.

## 3. Local Analytic Estimate

We need a uniform estimate for the logarithms of the exact singleton comparison maps.

### Lemma 1: singleton logarithm expansion

For `Delta/a` sufficiently small,

```math
\log J_{n,\lambda}(a,\Delta)
=
c_\lambda\Delta^2A_n^{(1)}+R_{n,\lambda}(a,\Delta),
```

where the translated remainder satisfies the local bound

```math
\left\|a\sum_nN(an)R_{n,\lambda}(a,\Delta)\right\|
\le
C_N\frac{\Delta^4}{a^3}
```

for every fixed smooth compactly supported `N`. The constant depends on finitely many bounds on `N`, on `lambda`, and on the fixed mass, but not on `a` or `Delta` in the small-slab regime.

Proof. The exact singleton comparison map has the expansion

```math
J_{n,\lambda}(a,\Delta)
=
I+c_\lambda\Delta^2A_n^{(1)}+O(\Delta^4a^{-4})
```

locally, because each additional pair of powers of `Delta` can introduce at most two additional powers of the nearest-neighbor Dirac scale `a^{-1}`. The principal logarithm is analytic for `||J_{n,lambda}-I||<1`, which holds uniformly for `Delta/a` small. Therefore

```math
\log J_{n,\lambda}
=
c_\lambda\Delta^2A_n^{(1)}+O(\Delta^4a^{-4})
```

with finite-propagation coefficient bounds order by order. At any fixed order, only finitely many translates overlap at a given lattice site, and the prefactor `a` in the smearing gives

```math
a\cdot O(a^{-4})=O(a^{-3})
```

for the first omitted term. The analytic tail is a geometric series in `(Delta/a)^2`, so the same bound holds after summing the tail for `Delta/a` small. This proves the estimate. `square`

### Lemma 2: smeared logarithm expansion

Define

```math
L_{a,\Delta}^{(\lambda)}[N]
:=
a\sum_nN(an)\log J_{n,\lambda}(a,\Delta).
```

Then

```math
L_{a,\Delta}^{(\lambda)}[N]
=
c_\lambda\Delta^2\mathcal K_a[N]+B_{a,\Delta}^{(\lambda)}[N],
```

where

```math
\mathcal K_a[N]=a\sum_nN(an)A_n^{(1)},
```

and

```math
\|\mathcal K_a[N]\|\le C_Na^{-1},
\qquad
\|B_{a,\Delta}^{(\lambda)}[N]\|\le C_N\Delta^4a^{-3}.
```

Proof. The identity and the bound on `B` are Lemma 1 summed against `aN_n`. The bound on `K_a[N]` follows from the local norm `||A_n^{(1)}||=O(a^{-2})`, finite overlap of singleton neighborhoods, and the smearing factor `a`. `square`

## 4. Group-Commutator Estimate

Let

```math
L_N:=L_{a,\Delta}^{(\lambda)}[N],
\qquad
L_M:=L_{a,\Delta}^{(\lambda)}[M].
```

Then

```math
\mathbb E_{a,\Delta}^{(\lambda)}[N,M]
=
e^{L_N}e^{L_M}e^{-L_N}e^{-L_M}.
```

### Lemma 3: finite group-commutator expansion

If `||L_N||+||L_M||` is sufficiently small, then

```math
e^{L_N}e^{L_M}e^{-L_N}e^{-L_M}
=
I+[L_N,L_M]+R_G,
```

with

```math
\|R_G\|
\le
C(\|L_N\|+\|L_M\|)^3.
```

Proof. Expand the four exponentials in a Banach algebra through second order. All linear terms cancel. The surviving second-order term is `[L_N,L_M]`. The remaining terms are at least cubic and are bounded by the displayed analytic estimate for sufficiently small `||L_N||+||L_M||`. `square`

By Lemma 2,

```math
\|L_N\|+\|L_M\|
\le
C\left(\frac{\Delta^2}{a}+\frac{\Delta^4}{a^3}\right).
```

The scaling `Delta/a^2 -> 0` implies both terms go to zero, so Lemma 3 applies for small enough `a`.

## 5. Reduction To The Tier 1 Curvature

Using Lemma 2,

```math
[L_N,L_M]
=
c_\lambda^2\Delta^4[\mathcal K_a[N],\mathcal K_a[M]]
 +
R_C,
```

where

```math
\|R_C\|
\le
C\left(\Delta^6a^{-4}+\Delta^8a^{-6}\right).
```

Indeed, the first error term comes from one leading piece `c_lambda Delta^2 K_a` and one logarithmic remainder `B=O(Delta^4a^{-3})`; the second comes from the commutator of the two logarithmic remainders.

Combining with Lemma 3 gives

```math
\left\|
\frac{1}{c_\lambda^2\Delta^4}
\left(\mathbb E_{a,\Delta}^{(\lambda)}[N,M]-I\right)
-
[\mathcal K_a[N],\mathcal K_a[M]]
\right\|
\le
C\left(
\frac{\Delta^2}{a^4}
+
\frac{\Delta^4}{a^6}
+
\frac{\Delta^2}{a^3}
\right).
```

The right-hand side goes to zero under

```math
\frac{\Delta}{a^2}\to0.
```

Thus

```math
\frac{1}{c_\lambda^2\Delta^4}
\left(\mathbb E_{a,\Delta}^{(\lambda)}[N,M]-I\right)
=
[\mathcal K_a[N],\mathcal K_a[M]]+o(1)
```

in operator norm along the stated coupled limit.

Applying this to `iota_a phi` gives

```math
\frac{1}{c_\lambda^2\Delta^4}
\left(\mathbb E_{a,\Delta}^{(\lambda)}[N,M]-I\right)\iota_a\phi
=
[\mathcal K_a[N],\mathcal K_a[M]]\iota_a\phi+o(1).
```

## 6. Insert The Tier 1 Theorem

The coefficient-level free stochastic-curvature theorem gives

```math
[\mathcal K_a[N],\mathcal K_a[M]]\iota_a\phi
=
\iota_a K_\parallel[\beta]\phi+O(a).
```

Therefore

```math
\frac{1}{c_\lambda^2\Delta(a)^4}
\left(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I\right)\iota_a\phi
=
\iota_a K_\parallel[\beta]\phi+o(1)+O(a).
```

Since `a->0`, the error goes to zero. This proves

```math
\left\|
\frac{1}{c_\lambda^2\Delta(a)^4}
\left(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I\right)\iota_a\phi
-
\iota_a K_\parallel[\beta]\phi
\right\|_{\ell^2}
\to0.
```

This is the Tier 2 finite-slab stochastic-curvature theorem for the log-smeared free one-particle construction.

## 7. What Was Proved

The theorem proves the following.

1. A genuine finite-slab exchange defect can be defined for smooth lapse profiles by log-smearing the exact finite singleton comparison maps.
2. Its normalized group commutator has the same continuum action as the coefficient-level stochastic curvature.
3. The normalization is

```math
Z_{a,\Delta}^{(\lambda)}=c_\lambda^{-2}\Delta^{-4}.
```

4. The required coupled scaling is very thin:

```math
\Delta(a)/a^2\to0.
```

5. The proof is stable for the exact `lambda` family after division by `c_lambda^2`.

## 8. What Remains Open

The theorem does not prove the broader finite-slab program. The following remain separate proof burdens.

1. Replace log-smearing by a primitive weighted-Hamiltonian smooth-lapse kernel and prove the same limit.
2. Weaken the very-thin-slab condition if sharper local estimates permit it.
3. Extend the finite-slab theorem beyond singleton leading curvature to larger supports and higher strip moments.
4. Include Lie-Trotter or other onset classes with their own normalizations.
5. Lift the result to Fock sectors, gauge coupling, interacting fields, or geometry.

The theorem is nevertheless a real Tier 2 result: the finite, exact comparison maps themselves have a normalized small-slab exchange defect whose continuum action is the stochastic-curvature operator already identified at coefficient level.
