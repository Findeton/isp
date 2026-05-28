# The Free Stochastic-Curvature Theorem for Relativistic ISP

Author: Felix Robles Elvira

V2 Paper 1 consolidated draft

Date: 2026-05-13

Status: theorem-level draft. This paper consolidates the V2 Paper 1 investigation, the coefficient-level proof, and the log-smeared finite-slab proof into one scoped result. It proves the free one-particle `1+1D` stochastic-curvature theorem at the leading collar-excision and normalized `lambda`-family scope.

## Abstract

Relativistic indivisible stochastic processes should not begin from infinitesimal Markov generators. In the free one-particle lattice Dirac benchmark, the primitive objects are exact finite stochastic kernels, localized algebraic comparison maps, and their exchange defect. Earlier free-core papers showed that the collar-excision comparison maps have a quasilocal `Delta^2`-onset filtration and that their leading singleton exchange coefficient has a bond-centered continuum action. This paper consolidates those facts into the first V2 theorem: the free stochastic-curvature theorem.

For smooth compactly supported lapse profiles `N,M`, the coefficient-level exchange curvature

```math
\mathfrak C_a[N,M]=[\mathcal K_a[N],\mathcal K_a[M]],
\qquad
\mathcal K_a[N]=a\sum_nN(an)A_n^{(1)},
```

converges strongly on sampled smooth spinors to

```math
K_\parallel[N\partial_xM-M\partial_xN]
=
\left((N\partial_xM-M\partial_xN)\partial_x
+\frac12\partial_x(N\partial_xM-M\partial_xN)\right)(I-\alpha).
```

The same limit is regulator-independent across the exact `lambda` family after division by `c_lambda^2`, with `c_lambda=lambda(2-lambda)`. We then prove a finite-slab lift for a canonical log-smeared smooth-lapse construction built from the exact singleton comparison maps. Under the very-thin-slab scaling `Delta(a)/a^2 -> 0`, the normalized finite exchange defect converges to the same tangential operator.

This is not a full relativistic ISP field theory. It is a free one-particle theorem. It does not prove a primitive weighted-Hamiltonian smooth-lapse kernel theorem, all-support/all-order regulator independence, Fock-space dynamics, gauge coupling, interacting fields, or gravity. Its role is narrower and central: it shows that the finite ISP exchange-defect algebra really contains a stochastic analogue of the hypersurface-deformation curvature in the simplest free setting.

## 1. Scope And Non-Claims

The theorem proved here is deliberately scoped.

Proved:

1. leading coefficient-level free stochastic curvature for singleton collar-excision data;
2. normalized `lambda`-family stability at the same leading scope;
3. a finite-slab lift for log-smeared exact singleton comparison maps;
4. explicit very-thin-slab scaling `Delta(a)/a^2 -> 0` sufficient for the finite-slab remainder to vanish;
5. strong convergence on sampled smooth compactly supported spinor profiles.

Not proved:

1. primitive weighted-Hamiltonian smooth-lapse kernels;
2. all support prototypes and all higher coefficients;
3. arbitrary admissible regulator classes;
4. Lie-Trotter finite-slab matching in the same onset class;
5. Fock, gauge, interacting, or gravitational extensions;
6. operator-norm convergence to an unbounded continuum differential operator.

The theorem is therefore a genuine V2 Paper 1 result, not a completed relativistic ISP theory.

## 2. Free Lattice Setup

Let `Lambda_L=Z/LZ` be a periodic spatial lattice with spacing `a`. The one-particle configuration basis is

```math
C_L=\Lambda_L\times\{\uparrow,\downarrow\}.
```

The free lattice Dirac Hamiltonian is

```math
H_D=K+M,
\qquad
K=-\frac{i}{2a}\alpha(T_+-T_-),
\qquad
M=m\beta,
```

with

```math
\alpha=\sigma_x,
\qquad
\beta=\sigma_z.
```

For a unitary `U`, the primitive ISP kernel is

```math
\Gamma(U)_{AB}=|U_{AB}|^2.
```

The free reference slab is

```math
\Gamma_0(\Delta)=\Gamma(e^{-i\Delta H_D}).
```

For singleton support `R_n={n}`, let `C_n` be the local collar Hamiltonian containing the mass term at `n` and the two kinetic bonds incident on `n`. The `lambda` family of localized finite deformations is

```math
U_{n}^{(\lambda)}(\Delta)=e^{-i\Delta(H_D-\lambda C_n)},
\qquad
0<\lambda\le1.
```

The collar-excision rule is `lambda=1`. The exact singleton comparison map is

```math
J_{n,\lambda}(a,\Delta)
=
\Gamma(U_n^{(\lambda)}(\Delta))\Gamma_0(\Delta)^{-1}.
```

These `J` maps are algebraic comparison maps. They preserve normalization but need not be stochastic.

## 3. Exact Finite Inputs

The free-core papers establish the following facts.

### 3.1 Quasilocal expansion

For singleton collar-excision data,

```math
J_n(\Delta)=I+\Delta^2A_n^{(1)}+O(\Delta^4),
```

with support in the one-step neighborhood of `n`. More generally, finite interval support has a quasilocal expansion

```math
J_R(\Delta)=I+\sum_{k\ge1}\Delta^{2k}A_R^{(k)},
\qquad
\operatorname{supp}A_R^{(k)}\subset N_k(R).
```

### 3.2 Leading singleton coefficient

The singleton leading coefficient has deleted-bond entries

```math
[A_n^{(1)}]_{(n,s),(n,s)}=\frac{1}{2a^2},
```

```math
[A_n^{(1)}]_{(n\pm1,\bar s),(n,s)}
=
[A_n^{(1)}]_{(n,s),(n\pm1,\bar s)}
=
-\frac{1}{4a^2},
```

```math
[A_n^{(1)}]_{(n\pm1,s),(n\pm1,s)}=\frac{1}{4a^2},
```

with all other entries zero. Columns sum to zero. The coefficient is mass-independent; mass first enters at higher order.

### 3.3 Exchange-defect coefficient

For singleton supports whose first visible exchange is generated by leading coefficients,

```math
E_{n,m}(\Delta)=I+\Delta^4[A_n^{(1)},A_m^{(1)}]+O(\Delta^6).
```

Thus the leading stochastic curvature is not `A_n^{(1)}` itself. It is the commutator of two localized leading coefficients.

### 3.4 Lambda scaling

The exact `lambda` family obeys

```math
A_{n,\lambda}^{(1)}=c_\lambda A_n^{(1)},
\qquad
c_\lambda=\lambda(2-\lambda).
```

This identity is exact at the leading coefficient level.

### 3.5 Bond-centered thin-slab identity

The exact leading singleton commutator closes on bond-centered strip channels. After spatial bond-centered renormalization, its action on smooth sampled spinors is

```math
[\mathcal K_a[N],\mathcal K_a[M]]\iota_a\phi
=
\iota_a\left(\left(\beta\partial_x+\frac12\partial_x\beta\right)(I-\alpha)\phi\right)
+O(a),
```

where

```math
\mathcal K_a[N]=a\sum_nN(an)A_n^{(1)},
\qquad
\beta=N\partial_xM-M\partial_xN.
```

The continuum limit is a profile-action limit, not an entrywise matrix limit.

## 4. Sampling And Test Domain

Let `N,M in C_c^infty(R)` be real lapse profiles and let `phi in C_c^infty(R,C^2)`. Use the sampling map

```math
(\iota_a\phi)_{n,s}=a^{1/2}\phi_s(an).
```

Assume the periodic ring is large enough that the supports of `N`, `M`, `phi`, and their finite exchange collars do not meet the seam for sufficiently small `a`. Equivalently, the theorem may be read on the infinite lattice first and then transferred to large finite rings by stabilization.

The target continuum operator is

```math
K_\parallel[\beta]
=
\left(\beta\partial_x+\frac12\partial_x\beta\right)(I-\alpha).
```

Convergence is strong on sampled test profiles.

## 5. The Coefficient-Level Theorem

Define

```math
\mathcal K_a[N]=a\sum_nN(an)A_n^{(1)},
\qquad
\mathfrak C_a[N,M]=[\mathcal K_a[N],\mathcal K_a[M]].
```

### Theorem 1: coefficient-level free stochastic curvature

For `N,M in C_c^infty(R)` and `phi in C_c^infty(R,C^2)`,

```math
\mathfrak C_a[N,M]\iota_a\phi
=
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi+O(a)
```

in lattice `ell^2`. Hence

```math
\lim_{a\to0}
\left\|
\mathfrak C_a[N,M]\iota_a\phi
-
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi
\right\|_{\ell^2}=0.
```

Proof. Since `A_n^{(1)}` is supported in one lattice step, `[A_n^{(1)},A_m^{(1)}]` vanishes except for finitely many relative displacements `r=m-n`. Thus

```math
\mathfrak C_a[N,M]
=
a^2\sum_n\sum_{r\in R_*}N_nM_{n+r}[A_n^{(1)},A_{n+r}^{(1)}],
```

where `R_*` is finite. Antisymmetry of the commutator lets the lapse factor be written as

```math
N_nM_{n+r}-M_nN_{n+r}.
```

Taylor expansion at the bond-centered point gives

```math
N_nM_{n+r}-M_nN_{n+r}
=
ar\,(N\partial_xM-M\partial_xN)(x_{n+r/2})+O(a^2),
```

uniformly on the finite active displacement set. The exact singleton strip calculation decomposes the commutators into finitely many bond-centered strip channels with finite first moments. Substituting the Taylor expansion produces the bond-centered density for `beta=N partial_x M - M partial_x N`. The exact bond-centered thin-slab identity then gives

```math
\mathfrak C_a[N,M]\iota_a\phi
=
\iota_a\left(\left(\beta\partial_x+\frac12\partial_x\beta\right)(I-\alpha)\phi\right)+O(a).
```

This is the claimed theorem. `square`

## 6. Normalized Lambda-Family Stability

Define

```math
\mathcal K_{a,\lambda}[N]
=
a\sum_nN(an)A_{n,\lambda}^{(1)},
\qquad
\mathfrak C_{a,\lambda}[N,M]
=
[\mathcal K_{a,\lambda}[N],\mathcal K_{a,\lambda}[M]].
```

### Theorem 2: coefficient-level lambda stability

For every `0<lambda<=1`,

```math
c_\lambda^{-2}\mathfrak C_{a,\lambda}[N,M]\iota_a\phi
=
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi+O(a).
```

Proof. The exact scaling identity gives

```math
\mathcal K_{a,\lambda}[N]=c_\lambda\mathcal K_a[N].
```

Therefore

```math
\mathfrak C_{a,\lambda}[N,M]
=
c_\lambda^2\mathfrak C_a[N,M].
```

Divide by `c_lambda^2` and apply Theorem 1. `square`

## 7. Log-Smeared Finite-Slab Construction

The coefficient theorem identifies the leading curvature. To get a finite-slab theorem one must define a smooth-lapse finite comparison map. This paper uses a log-smeared construction from the exact singleton comparison maps.

For small enough `Delta/a`, take the principal logarithm of `J_{n,lambda}(a,Delta)` and define

```math
\mathbb J_{a,\Delta}^{(\lambda)}[N]
=
\exp\left(a\sum_nN(an)\log J_{n,\lambda}(a,\Delta)\right).
```

The finite-slab exchange defect is

```math
\mathbb E_{a,\Delta}^{(\lambda)}[N,M]
=
\mathbb J_{a,\Delta}^{(\lambda)}[N]
\mathbb J_{a,\Delta}^{(\lambda)}[M]
\mathbb J_{a,\Delta}^{(\lambda)}[N]^{-1}
\mathbb J_{a,\Delta}^{(\lambda)}[M]^{-1}.
```

This is a genuine finite-slab object: it uses the exact finite comparison maps at finite `a` and finite `Delta`, not only their coefficients. It is also a particular regularization. A primitive weighted-Hamiltonian smooth-lapse construction would require a separate theorem.

## 8. Finite-Slab Estimate

Define

```math
L_{a,\Delta}^{(\lambda)}[N]
=
a\sum_nN(an)\log J_{n,\lambda}(a,\Delta).
```

For `Delta/a` sufficiently small, the singleton logarithm has the local expansion

```math
\log J_{n,\lambda}(a,\Delta)
=
c_\lambda\Delta^2A_n^{(1)}+R_{n,\lambda}(a,\Delta),
```

and the smeared remainder obeys

```math
\left\|a\sum_nN(an)R_{n,\lambda}(a,\Delta)\right\|
\le
C_N\frac{\Delta^4}{a^3}.
```

Thus

```math
L_{a,\Delta}^{(\lambda)}[N]
=
c_\lambda\Delta^2\mathcal K_a[N]
+B_{a,\Delta}^{(\lambda)}[N],
```

with

```math
\|\mathcal K_a[N]\|\le C_Na^{-1},
\qquad
\|B_{a,\Delta}^{(\lambda)}[N]\|\le C_N\Delta^4a^{-3}.
```

Let `L_N=L_{a,Delta}^{(lambda)}[N]` and `L_M=L_{a,Delta}^{(lambda)}[M]`. If `||L_N||+||L_M||` is small, the Banach-algebra group-commutator expansion gives

```math
e^{L_N}e^{L_M}e^{-L_N}e^{-L_M}
=
I+[L_N,L_M]+R_G,
\qquad
\|R_G\|\le C(\|L_N\|+\|L_M\|)^3.
```

The logarithm expansion gives

```math
[L_N,L_M]
=
c_\lambda^2\Delta^4[\mathcal K_a[N],\mathcal K_a[M]]+R_C,
```

with

```math
\|R_C\|
\le
C(\Delta^6a^{-4}+\Delta^8a^{-6}).
```

Consequently,

```math
\left\|
\frac{1}{c_\lambda^2\Delta^4}
\left(\mathbb E_{a,\Delta}^{(\lambda)}[N,M]-I\right)
-[\mathcal K_a[N],\mathcal K_a[M]]
\right\|
\le
C\left(\frac{\Delta^2}{a^4}+\frac{\Delta^4}{a^6}+\frac{\Delta^2}{a^3}\right).
```

The right side vanishes if

```math
\frac{\Delta(a)}{a^2}\to0.
```

This is the very-thin-slab condition used below.

## 9. Finite-Slab Theorem

### Theorem 3: log-smeared finite-slab stochastic curvature

Assume

```math
a\to0,
\qquad
\Delta=\Delta(a)\to0,
\qquad
\Delta(a)/a^2\to0.
```

Then for every `0<lambda<=1`,

```math
\left\|
\frac{1}{c_\lambda^2\Delta(a)^4}
\left(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I\right)\iota_a\phi
-
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi
\right\|_{\ell^2}
\to0.
```

Proof. By the estimate in Section 8,

```math
\frac{1}{c_\lambda^2\Delta(a)^4}
\left(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I\right)
=
[\mathcal K_a[N],\mathcal K_a[M]]+o(1)
```

in operator norm. Applying this to `iota_a phi` and then using Theorem 1 gives

```math
\frac{1}{c_\lambda^2\Delta(a)^4}
\left(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I\right)\iota_a\phi
=
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi+o(1)+O(a).
```

Since `a->0`, the error vanishes. `square`

## 10. Fulfillment Of V2 Paper 1

This paper fulfills V2 Paper 1 in the following precise sense.

1. The free one-particle exchange-defect algebra has been consolidated into one theorem-level continuum test.
2. Smooth lapse sampling and the test-profile domain are explicit.
3. The coefficient-level stochastic-curvature theorem is proved.
4. The exact `lambda` family is regulator-stable after the stated normalization.
5. A finite-slab theorem is proved for a log-smeared construction with explicit scaling.
6. The theorem recovers the tangential hypersurface-deformation operator

```math
K_\parallel[N\partial_xM-M\partial_xN].
```

The result is the strongest safe Paper 1 claim currently supported by the exact free-core stack.

## 11. Remaining Proof Burdens

The next papers should not pretend these tasks are already done.

1. **Primitive smooth-lapse kernels.** Replace log-smearing with a weighted-Hamiltonian primitive kernel and prove the same limit.
2. **Sharper slab scaling.** Improve `Delta(a)/a^2 -> 0` if stronger uniform estimates allow it.
3. **Higher coefficients and support prototypes.** Extend from leading singleton curvature to larger support classes and higher strip moments.
4. **Broader regulators.** Treat Lie-Trotter and other onset classes with their own normalizations.
5. **Fock and gauge lifts.** Lift the free one-particle result only after the relevant finite-sector and gauge-sector hypotheses are explicitly proved.
6. **Gravity.** Do not infer metric dynamics. This theorem is a prerequisite for later metric reconstruction, not a gravity theorem.

## 12. Conclusion

The free stochastic-curvature theorem is now established at the first defensible V2 scope. The finite ISP exchange-defect algebra does recover the tangential hypersurface-deformation generator in the free `1+1D` benchmark, first at coefficient level and then for a log-smeared finite-slab construction under explicit scaling. This gives relativistic ISP a real non-gravitational curvature datum. The next step is not to broaden the claim rhetorically, but to test how much of this result survives under primitive smooth-lapse kernels, larger support prototypes, higher coefficients, and eventually field-theoretic lifts.
