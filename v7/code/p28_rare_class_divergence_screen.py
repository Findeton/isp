#!/usr/bin/env python3
"""
Paper 28 receipt: rare-class divergence screen.

The opposite of washout would be a stable family of unlabeled record classes
A_N whose contribution to the second moment does not stay bounded:

    q_N(A_N)^2 / p_N(A_N) -> infinity.

This receipt does not prove that no such class exists.  It formalizes what a
successful rare-class witness must do, and compares that demand with the
audited finite rare-class screens from Papers 23 and 27.

The conclusion is deliberately hostile:

  * current exact/screened finite classes are not divergence certificates;
  * a true residue must survive exact-denominator counting, repeated split
    sampling, and aggregation over selected families;
  * if it exists, it is subtler than the P8/N10/N12 screens already tried.

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


def rare_contribution(p, q):
    return (mp.mpf(q) * mp.mpf(q)) / mp.mpf(p)


def toy_divergent_contribution(N, a, b):
    """p=exp(-aN), q=exp(-bN). Diverges when 2b<a."""
    N = mp.mpf(N)
    a = mp.mpf(a)
    b = mp.mpf(b)
    return mp.e ** ((a - 2 * b) * N)


def toy_contiguous_q_bound(p, C):
    """From q(A) <= sqrt(C) sqrt(p(A))."""
    return mp.sqrt(mp.mpf(C)) * mp.sqrt(mp.mpf(p))


print("=" * 80)
print("Paper 28 rare-class divergence screen")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

finite_witnesses = {
    "P8_largest_positive_linear": mp.mpf("0.00478171696739"),
    "N10_max_half_one_selected": mp.mpf("0.0540733337402"),
    "N12_max_selected_contribution": mp.mpf("0.0557631254196"),
    "N12_max_per_schedule_q_null_ratio": mp.mpf("1.50457317073"),
    "N12_resolved_selected_count": mp.mpf("95"),
    "N12_invariant_screen_samples_per_side": mp.mpf("4096"),
    "N12_invariant_screen_repeated_keys": mp.mpf("0"),
}

print("\n=== What a rare-class witness must do ===")
toy_rows = []
for N in [8, 12, 16, 24, 32, 48]:
    divergent = toy_divergent_contribution(N, mp.mpf("1"), mp.mpf("0.4"))
    critical = toy_divergent_contribution(N, mp.mpf("1"), mp.mpf("0.5"))
    contiguous = toy_divergent_contribution(N, mp.mpf("1"), mp.mpf("0.6"))
    toy_rows.append((N, divergent, critical, contiguous))
    print(
        f"N={N} divergent={fmt(divergent)} "
        f"critical={fmt(critical)} contiguous_side={fmt(contiguous)}"
    )

check(
    "rare-class divergence requires q to beat sqrt(p) exponentially",
    toy_rows[-1][1] > toy_rows[0][1] * mp.mpf("1000")
    and toy_rows[-1][3] < toy_rows[0][3] / mp.mpf("100"),
    f"N8_div={fmt(toy_rows[0][1])} N48_div={fmt(toy_rows[-1][1])}",
)

print("\n=== Bounded-second-moment rare-class cap ===")
cap_rows = []
C = mp.mpf("4")
for exponent in [4, 8, 16, 32, 64]:
    p = mp.e ** (-mp.mpf(exponent))
    q_cap = toy_contiguous_q_bound(p, C)
    contribution = rare_contribution(p, q_cap)
    cap_rows.append((exponent, p, q_cap, contribution))
    print(
        f"p=e^-{exponent} q_cap={fmt(q_cap)} "
        f"q_cap^2/p={fmt(contribution)}"
    )

check(
    "bounded second moment permits tiny rare classes only at sqrt(p) scale",
    all(abs(row[3] - C) < mp.mpf("1e-120") for row in cap_rows),
    f"C={fmt(C)}",
)

print("\n=== Audited finite rare-class screens ===")
for name, value in finite_witnesses.items():
    print(f"{name} = {fmt(value)}")

max_individual = max(
    finite_witnesses["P8_largest_positive_linear"],
    finite_witnesses["N10_max_half_one_selected"],
    finite_witnesses["N12_max_selected_contribution"],
)

check(
    "finite exact/selected screens do not show a large individual rare-class contribution",
    max_individual < mp.mpf("0.1"),
    f"max_individual={fmt(max_individual)}",
)
check(
    "finite aggregate selected ratio is order-one, not a divergence certificate",
    finite_witnesses["N12_max_per_schedule_q_null_ratio"] < mp.mpf("2"),
    f"ratio={fmt(finite_witnesses['N12_max_per_schedule_q_null_ratio'])}",
)
check(
    "N12 invariant screen found no repeated cheap keys in the first pass",
    finite_witnesses["N12_invariant_screen_repeated_keys"] == 0
    and finite_witnesses["N12_invariant_screen_samples_per_side"] == 4096,
    f"samples={fmt(finite_witnesses['N12_invariant_screen_samples_per_side'])}",
)

print("\n=== Minimum growth needed to overturn the finite screen ===")
growth_rows = []
for target in [1, 10, 100, 1000]:
    needed_from_N12 = mp.mpf(target) / finite_witnesses["N12_max_selected_contribution"]
    per_record_12_to_24 = needed_from_N12 ** (mp.mpf(1) / 12)
    per_record_12_to_48 = needed_from_N12 ** (mp.mpf(1) / 36)
    growth_rows.append((target, needed_from_N12, per_record_12_to_24, per_record_12_to_48))
    print(
        f"target={target} multiplier_from_N12={fmt(needed_from_N12)} "
        f"per_record_to_N24={fmt(per_record_12_to_24)} "
        f"per_record_to_N48={fmt(per_record_12_to_48)}"
    )

check(
    "a divergence witness would need sustained growth absent from current screens",
    growth_rows[-1][1] > mp.mpf("10000") and growth_rows[-1][2] > mp.mpf("2"),
    f"target1000_multiplier={fmt(growth_rows[-1][1])} "
    f"per_record_to_N24={fmt(growth_rows[-1][2])}",
)

print("\n=== Verdict ===")
print("No finite screen here proves washout.")
print("But none supplies a divergence certificate either.")
print("A successful rare-class attack must produce exact denominators and")
print("stable repeated selected classes whose q^2/p contribution grows with N.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
