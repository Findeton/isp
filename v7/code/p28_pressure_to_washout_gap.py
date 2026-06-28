#!/usr/bin/env python3
"""
Paper 28 receipt: pressure-density versus washout gap.

The pressure-density campaign found a strong staged/fiber diagnostic:

    p_N(D) = N^{-1} log Z_N(D; N).

But the bounded second-moment washout theorem needs a different analytic
object: the unscaled polymer/cycle sum, roughly Z_N(D;1)-1 after the one-pair
envelope and quotient reductions.

This receipt prevents a false proof:

  * bounded pressure density does not by itself imply bounded second moment;
  * a coefficient-level N^{-r} envelope does imply washout;
  * pressure density is best read as a geometry regularity/action diagnostic,
    while washout requires a true all-orders polymer summability theorem.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def z_from_coeffs(coeffs, z):
    z = mp.mpf(z)
    return 1 + mp.fsum(q * (z ** r) for r, q in coeffs.items())


def pressure_density(coeffs, N):
    return mp.log(z_from_coeffs(coeffs, N)) / mp.mpf(N)


def washout_excess(coeffs):
    return z_from_coeffs(coeffs, 1) - 1


def coeffs_washout_model(N, C, beta):
    """q_r = C beta^r / N^r for r>=2."""
    N_int = int(N)
    N = mp.mpf(N)
    return {
        r: mp.mpf(C) * (mp.mpf(beta) ** r) / (N ** r)
        for r in range(2, N_int // 2 + 1)
    }


def coeffs_pressure_only_model(N, gamma):
    """
    Concentrate all mass at r=N/2 so p_N(D) is gamma at z=N.
    The unscaled Z(1)-1 is still exp(gamma N)/N^(N/2), so it can be tiny.
    This shows pressure can be high without washout failure.
    """
    N_int = int(N)
    N = mp.mpf(N)
    r = N_int // 2
    return {r: mp.e ** (mp.mpf(gamma) * N) / (N ** r)}


def coeffs_bounded_pressure_diverging_washout(N, gamma):
    """
    Put q_2=exp(gamma N)/N^2.  Then p_N(D) is about gamma, but Z(1)-1
    diverges exponentially.  This shows p_N <= gamma is not a washout proof.
    """
    N = mp.mpf(N)
    return {2: mp.e ** (mp.mpf(gamma) * N) / (N ** 2)}


print("=" * 80)
print("Paper 28 pressure-density versus washout gap")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Coefficient-level washout model ===")
washout_rows = []
for N in [16, 32, 64, 128, 256, 512]:
    coeffs = coeffs_washout_model(N, C=mp.mpf("0.1"), beta=mp.mpf("0.5"))
    pN = pressure_density(coeffs, N)
    z1 = washout_excess(coeffs)
    washout_rows.append((N, pN, z1))
    print(f"N={N} p_N={fmt(pN)} Z(1)-1={fmt(z1)}")

check(
    "an N^{-r} coefficient envelope gives washout",
    washout_rows[-1][2] < washout_rows[0][2] / mp.mpf("100"),
    f"N16={fmt(washout_rows[0][2])} N512={fmt(washout_rows[-1][2])}",
)
check(
    "the same envelope also has vanishing pressure density",
    all(washout_rows[i][1] > washout_rows[i + 1][1] for i in range(len(washout_rows) - 1))
    and washout_rows[-1][1] < mp.mpf("1e-3"),
    f"N16 p_N={fmt(washout_rows[0][1])} N512 p_N={fmt(washout_rows[-1][1])}",
)

print("\n=== High pressure can be harmless for washout ===")
high_pressure_rows = []
for N in [16, 32, 64, 128]:
    coeffs = coeffs_pressure_only_model(N, gamma=mp.mpf("0.5"))
    pN = pressure_density(coeffs, N)
    z1 = washout_excess(coeffs)
    high_pressure_rows.append((N, pN, z1))
    print(f"N={N} p_N={fmt(pN)} Z(1)-1={fmt(z1)}")

check(
    "high pressure density alone need not imply washout failure",
    high_pressure_rows[-1][1] > mp.mpf("0.1")
    and high_pressure_rows[-1][2] < mp.mpf("1e-20"),
    f"N128 p_N={fmt(high_pressure_rows[-1][1])} Z1minus1={fmt(high_pressure_rows[-1][2])}",
)

print("\n=== Bounded pressure can still allow washout failure ===")
bad_rows = []
for N in [16, 32, 64, 128]:
    coeffs = coeffs_bounded_pressure_diverging_washout(N, gamma=mp.mpf("0.25"))
    pN = pressure_density(coeffs, N)
    z1 = washout_excess(coeffs)
    bad_rows.append((N, pN, z1))
    print(f"N={N} p_N={fmt(pN)} Z(1)-1={fmt(z1)}")

check(
    "bounded pressure density is not sufficient for washout",
    bad_rows[-1][1] < mp.mpf("0.26")
    and bad_rows[-1][2] > bad_rows[0][2] * mp.mpf("1e6"),
    f"N16 Z1={fmt(bad_rows[0][2])} N128 Z1={fmt(bad_rows[-1][2])}",
)

print("\n=== Consequence ===")
print("The washout theorem needs coefficient-level polymer summability.")
print("Pressure density is still useful, but as a staged-geometry regularity")
print("or action diagnostic, not as a standalone contiguity proof.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
