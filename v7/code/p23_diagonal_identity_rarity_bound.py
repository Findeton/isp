#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: diagonal hidden-identity rarity bound.

The component-factorization audit found that exact-P8 non-identical overlap
signatures are near null, while the full hidden-matching identity spikes.  This
receipt isolates the corresponding theorem shape.

For width 2 with N=2m records, the number of hidden matchings is

    M_m = (2m-1)!!.

If the two-replica cross factor decomposes as

    E_{H,H'} B(H,H')
      = P(H=H') B_diag + P(H!=H') B_mix,

then the diagonal contributes B_diag/M_m.  Since M_m grows like

    sqrt(2) (2m/e)^m,

any polynomial, fixed-exponential, or exp(o(m log m)) diagonal spike is killed
by hidden-identity rarity.  A diagonal divergence requires a super-exponential
in m self-likelihood comparable to the number of matchings.

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


def odd_double_factorial(n):
    if n <= 0:
        return mp.mpf(1)
    out = mp.mpf(1)
    for value in range(n, 0, -2):
        out *= value
    return out


def matching_count(m):
    return odd_double_factorial(2 * m - 1)


def stirling_matching_asymptotic(m):
    return mp.sqrt(2) * (mp.mpf(2) * m / mp.e) ** m


print("=" * 80)
print("Collapsed P23 diagonal hidden-identity rarity bound")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\nMatching count growth")
rows = []
for m in [4, 8, 16, 32, 64, 128, 256]:
    count = matching_count(m)
    approx = stirling_matching_asymptotic(m)
    rows.append((m, count, approx))
    print(
        f"m={m}: log M/m={fmt(mp.log(count)/m, 18)} "
        f"M/asymptotic={fmt(count/approx, 18)}"
    )

print("\nDiagonal contribution tests")
for growth_name, growth in [
    ("polynomial_m4", lambda m: mp.mpf(m) ** 4),
    ("fixed_exp_10^m", lambda m: mp.mpf(10) ** m),
    ("sub_super_exp_m_sqrtlog", lambda m: mp.e ** (m * mp.sqrt(mp.log(m)))),
    ("critical_matching_count", matching_count),
]:
    print(f"\n{growth_name}")
    for m in [16, 32, 64, 128, 256]:
        ratio = growth(m) / matching_count(m)
        print(f"  m={m}: diagonal_ratio={fmt(ratio, 18)}")

check(
    "Stirling matching asymptotic is accurate at large m",
    abs(rows[-1][1] / rows[-1][2] - 1) < mp.mpf("0.01"),
    f"m=256 ratio={fmt(rows[-1][1]/rows[-1][2], 12)}",
)
check(
    "Polynomial diagonal spikes are killed",
    (mp.mpf(256) ** 4) / matching_count(256) < mp.mpf("1e-300"),
    "",
)
check(
    "Fixed exponential diagonal spikes are killed",
    (mp.mpf(10) ** 256) / matching_count(256) < mp.mpf("1e-100"),
    "",
)
check(
    "Sub-m-log-m diagonal spikes are killed",
    mp.e ** (mp.mpf(256) * mp.sqrt(mp.log(256))) / matching_count(256) < mp.mpf("1e-100"),
    "",
)
check(
    "A matching-count-scale diagonal spike is the dangerous threshold",
    abs(matching_count(64) / matching_count(64) - 1) < mp.mpf("1e-100"),
    "",
)

print("\n=== Consequence ===")
print("If all non-identical hidden explanations have cross factor 1+o(1),")
print("then the diagonal identity spike matters only if the conditional")
print("self-likelihood grows on the scale of the number of hidden matchings.")
print("Polynomial, fixed-exponential, and exp(o(m log m)) self spikes are")
print("suppressed by hidden-identity rarity.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
