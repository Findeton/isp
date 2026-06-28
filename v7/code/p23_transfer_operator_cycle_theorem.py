#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: transfer-operator cycle theorem.

The previous cycle-neutrality target was too blunt.  In a pair-factor model,
one hidden explanation H has likelihood

    L_H = product_{(i,j) in H} phi(X_i,X_j)

under an iid reference law P, where phi has both marginals equal to 1.  Let K be
the integral operator with kernel phi, and write

    K = Pi + A

where Pi is the constants projection.  If H union H' has a nonshared
alternating component with k hidden H-edges (2k records), its factor is

    beta_k = tr(K^{2k}) = 1 + tr(A^{2k}).

Thus nonshared components need not be neutral one by one.  They are summable if
the centered transfer operator has spectral radius below 1.  In the finite-rank
case with centered eigenvalues lambda_i, the asymptotic cycle tax is

    exp(sum_{k>=1} (sum_i lambda_i^{2k})/(2k))
      = prod_i (1-lambda_i^2)^(-1/2).

This receipt checks the exact finite matching recurrence and the determinant
limit.  It gives a sharper theorem target: prove a pair-factor approximation
and a spectral gap for the centered order-visible pair kernel.

All arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def connected_count(k):
    if k == 1:
        return mp.mpf(1)
    return mp.power(2, k - 1) * mp.factorial(k - 1)


def odd_double_factorial(n):
    if n <= 0:
        return mp.mpf(1)
    out = mp.mpf(1)
    for value in range(n, 0, -2):
        out *= value
    return out


def component_probabilities(m):
    """Distribution of the component size containing a fixed H-edge."""
    probs = [mp.mpf(0)] * (m + 1)
    if m == 0:
        return probs
    p = mp.mpf(1) / (2 * m - 1)
    probs[1] = p
    for k in range(1, m):
        # p_{k+1}/p_k = 2(m-k)/(2m-2k-1).
        p *= mp.mpf(2 * (m - k)) / (2 * m - 2 * k - 1)
        probs[k + 1] = p
    return probs


def finite_weighted_expectation(m, beta):
    """Exact E prod_k beta(k)^C_k for random H' against fixed H."""
    expectations = [mp.mpf(1)]
    for size in range(1, m + 1):
        value = mp.mpf(0)
        probabilities = component_probabilities(size)
        for k in range(1, size + 1):
            value += probabilities[k] * beta(k) * expectations[size - k]
        expectations.append(value)
    return expectations[m]


def determinant_limit(eigenvalues):
    out = mp.mpf(1)
    for lam in eigenvalues:
        out *= (1 - lam * lam) ** (mp.mpf("-0.5"))
    return out


def beta_from_eigenvalues(eigenvalues):
    def beta(k):
        return 1 + mp.fsum(lam ** (2 * k) for lam in eigenvalues)

    return beta


print("=" * 80)
print("Collapsed P23 transfer-operator cycle theorem")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\nExact recurrence sanity check")
for m in [4, 8, 16, 32]:
    value = finite_weighted_expectation(m, lambda _k: mp.mpf(1))
    print(f"m={m}: neutral expectation={fmt(value, 24)}")

print("\nOne-mode centered spectrum")
one_mode_rows = []
for theta in [mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99")]:
    eigenvalues = [theta]
    beta = beta_from_eigenvalues(eigenvalues)
    limit = determinant_limit(eigenvalues)
    finite_values = []
    for m in [16, 64, 256, 512]:
        value = finite_weighted_expectation(m, beta)
        finite_values.append((m, value))
    one_mode_rows.append((theta, limit, finite_values))
    print(f"theta={fmt(theta, 6)} limit={fmt(limit, 24)}")
    for m, value in finite_values:
        print(f"  m={m}: exact={fmt(value, 24)} relerr={fmt(abs(value / limit - 1), 8)}")

print("\nMulti-mode centered spectrum")
multi_eigenvalues = [mp.mpf("0.4"), mp.mpf("-0.25"), mp.mpf("0.125")]
multi_limit = determinant_limit(multi_eigenvalues)
multi_beta = beta_from_eigenvalues(multi_eigenvalues)
multi_rows = []
for m in [16, 64, 256, 512]:
    value = finite_weighted_expectation(m, multi_beta)
    multi_rows.append((m, value))
    print(f"m={m}: exact={fmt(value, 24)} limit={fmt(multi_limit, 24)} relerr={fmt(abs(value / multi_limit - 1), 8)}")

print("\nNear-gap warning")
for theta in [mp.mpf("0.9"), mp.mpf("0.99"), mp.mpf("0.999")]:
    limit = determinant_limit([theta])
    print(f"theta={fmt(theta, 8)} determinant_tax={fmt(limit, 24)}")

check(
    "Neutral beta gives exact expectation one",
    all(abs(finite_weighted_expectation(m, lambda _k: mp.mpf(1)) - 1) < mp.mpf("1e-100") for m in [4, 8, 16]),
    "",
)
check(
    "One-mode finite expectations converge to determinant cycle tax",
    all(abs(values[-1][1] / limit - 1) < mp.mpf("0.01") for _theta, limit, values in one_mode_rows[:3]),
    "theta=0.1,0.5,0.9 at m=512",
)
check(
    "Multi-mode finite expectation converges to product determinant tax",
    abs(multi_rows[-1][1] / multi_limit - 1) < mp.mpf("0.005"),
    f"limit={fmt(multi_limit, 18)} m=512={fmt(multi_rows[-1][1], 18)}",
)
check(
    "Spectral radius below one gives finite cycle tax",
    all(determinant_limit([theta]) < mp.inf for theta in [mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99")]),
    "",
)
check(
    "Approaching spectral radius one exposes the divergence mechanism",
    determinant_limit([mp.mpf("0.999")]) > determinant_limit([mp.mpf("0.99")]) > determinant_limit([mp.mpf("0.9")]),
    "",
)

print("\n=== Consequence ===")
print("The nonshared-cycle problem is better stated as a transfer-operator")
print("problem.  If the centered pair operator has spectral radius bounded")
print("below one, all alternating cycles have a finite determinant tax.  A")
print("divergence would require the centered spectrum to approach one, or a")
print("failure of the pair-factor approximation.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
