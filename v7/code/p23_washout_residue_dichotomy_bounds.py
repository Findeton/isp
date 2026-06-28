#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: washout/residue dichotomy bounds.

This is not another Monte Carlo adversary search.  It records the asymptotic
inequalities behind the provable part of the clustered-coordinate dichotomy.

For N = m w records, Q_N(w, J_N) is the clustered coordinate generator with
hidden width w and rank-mixing radius J_N.  The receipt checks three analytic
facts used in the paper:

1. unrooted same-cluster pair mass is (w-1)/(N-1), so unrooted finite pattern
   laws can lose fixed hidden width;
2. if w J_N << tau_N << sqrt(N), then a Palm/rooted soft-near threshold can
   separate same-cluster partners from sprinkling neighbors;
3. if J_N dominates the full coordinate center range strongly enough, a
   product-TV coupling gives a sufficient full-record washout bound.

All non-integer arithmetic uses mpmath with dps=140.
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


def pair_mass(N, w):
    return mp.mpf(w - 1) / mp.mpf(N - 1)


def palm_multiplicity(w):
    return mp.mpf(w - 1)


def residue_witness(N, w, alpha):
    """J=N^alpha, tau=sqrt(wJ sqrt(N))."""
    N = mp.mpf(N)
    w = mp.mpf(w)
    J = N ** mp.mpf(alpha)
    tau = mp.sqrt(w * J * mp.sqrt(N))
    cluster_ratio = w * J / tau
    sprinkling_ratio = tau ** 2 / N
    return J, tau, cluster_ratio, sprinkling_ratio


def full_tv_bound(N, w, gamma):
    """Sufficient product-TV washout bound for J=N^gamma."""
    N = mp.mpf(N)
    w = mp.mpf(w)
    J = N ** mp.mpf(gamma)
    m = N / w
    # Two coordinates, N records, per-coordinate shift TV O(m/J).
    return 2 * N * m / J


def finite_k_center_ratio(N, w, gamma):
    """Center/noise ratio m/J for fixed-k order washout."""
    N = mp.mpf(N)
    w = mp.mpf(w)
    J = N ** mp.mpf(gamma)
    return (N / w) / J


print("=" * 80)
print("Collapsed P23 washout/residue dichotomy bounds")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [mp.mpf(2) ** k for k in [10, 14, 18, 22]]
widths = [2, 4, 8]

print("\n(1) Unrooted pair mass versus rooted multiplicity")
pair_mass_decreases = True
for w in widths:
    masses = [pair_mass(N, w) for N in Ns]
    pair_mass_decreases = pair_mass_decreases and all(masses[i] > masses[i + 1] for i in range(len(masses) - 1))
    print(
        f"w={w}: pair_mass={ [fmt(value, 12) for value in masses] }, "
        f"Palm multiplicity={fmt(palm_multiplicity(w), 12)}"
    )

print("\n(2) Residue witness for J_N=N^alpha with alpha<1/2")
residue_ok = True
for alpha in [mp.mpf("0.0"), mp.mpf("0.25"), mp.mpf("0.49")]:
    rows = []
    for N in Ns:
        J, tau, cluster_ratio, sprinkling_ratio = residue_witness(N, 4, alpha)
        rows.append((cluster_ratio, sprinkling_ratio))
    cluster_decreases = all(rows[i][0] > rows[i + 1][0] for i in range(len(rows) - 1))
    sprinkling_decreases = all(rows[i][1] > rows[i + 1][1] for i in range(len(rows) - 1))
    residue_ok = residue_ok and cluster_decreases and sprinkling_decreases
    print(
        f"alpha={fmt(alpha, 4)}: "
        f"wJ/tau={ [fmt(row[0], 12) for row in rows] }, "
        f"tau^2/N={ [fmt(row[1], 12) for row in rows] }"
    )

print("\n(3) Boundary failure at alpha=1/2")
boundary_rows = [residue_witness(N, 4, mp.mpf("0.5")) for N in Ns]
boundary_sprinkling = [row[3] for row in boundary_rows]
print("alpha=1/2 tau^2/N =", [fmt(value, 12) for value in boundary_sprinkling])

print("\n(4) Sufficient full-record washout bound")
tv_ok = True
for gamma in [mp.mpf("2.25"), mp.mpf("3.0")]:
    bounds = [full_tv_bound(N, 4, gamma) for N in Ns]
    tv_ok = tv_ok and all(bounds[i] > bounds[i + 1] for i in range(len(bounds) - 1)) and bounds[-1] < mp.mpf("0.02")
    print(f"gamma={fmt(gamma, 4)}: TV_bound={ [fmt(value, 12) for value in bounds] }")

print("\n(5) Fixed-k washout center/noise ratio")
fixed_k_ok = True
for gamma in [mp.mpf("1.25"), mp.mpf("1.5")]:
    ratios = [finite_k_center_ratio(N, 4, gamma) for N in Ns]
    fixed_k_ok = fixed_k_ok and all(ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1))
    print(f"gamma={fmt(gamma, 4)}: m/J={ [fmt(value, 12) for value in ratios] }")

print("\n(6) Critical window marker")
critical_linear = [finite_k_center_ratio(N, 4, mp.mpf("1.0")) for N in Ns]
print("gamma=1 m/J =", [fmt(value, 12) for value in critical_linear])

check(
    "Unrooted same-cluster pair mass vanishes while rooted multiplicity stays order-one",
    pair_mass_decreases and all(palm_multiplicity(w) >= 1 for w in widths),
    "pair mass=(w-1)/(N-1), Palm multiplicity=w-1",
)
check(
    "Residue witness exists for tested alpha below one half",
    residue_ok,
    "w J_N / tau_N -> 0 and tau_N^2 / N -> 0 for tau_N=sqrt(w J_N sqrt(N))",
)
check(
    "The alpha equals one-half boundary is not covered by the residue witness",
    all(abs(value - 4) < mp.mpf("1e-40") for value in boundary_sprinkling),
    "for w=4, tau_N^2/N remains constant at 4",
)
check(
    "A sufficient full-record washout bound tends to zero for J_N=N^gamma, gamma>2",
    tv_ok,
    "bound is 2 N (N/w) / J_N",
)
check(
    "Fixed-k center/noise ratio tends to zero for J_N=N^gamma, gamma>1",
    fixed_k_ok,
    "m_N/J_N -> 0",
)
check(
    "Linear mixing is a genuine critical window for this proof",
    all(abs(value - mp.mpf("0.25")) < mp.mpf("1e-40") for value in critical_linear),
    "for w=4 and J_N=N, m_N/J_N=1/4, not zero",
)

print("\n(7) Consequence")
print("The proof gives two rigorous regimes and a named middle window.  If")
print("w_N J_N << sqrt(N), a rooted/Palm threshold separates hidden partners")
print("from sprinkling.  If J_N is overwhelmingly larger than the center range,")
print("a coupling washes out the full record law.  Linear and near-linear mixing")
print("remain the critical window where the finite receipts live.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
