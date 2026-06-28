#!/usr/bin/env python3
"""
Paper 29 receipt: defect saddle motion audit.

This receipt does not recompute matching sums.  It takes the exact audited
near-top beta table from the previous receipts and asks what it says about the
moving defect saddle.

The purpose is hostile: after N=26 falsifies the old 0.65 guard, do not replace
it with another unsupported slogan.  Check whether fixed k=2 and beta<0.7 are
stable claims or only finite observations.

All arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

from p29_matching_lib import fmt

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


print("=" * 80)
print("Paper 29 defect saddle motion audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

profiles = {
    14: {0: "0.370195190621980969652009", 1: "0.390151408060616090354847", 2: "0.374826066699430466861526", 3: "0.330197241864047115370633"},
    16: {0: "0.409684017745808057347166", 1: "0.435065185055689707255959", 2: "0.428361126341251505892912", 3: "0.396211516024141534048125"},
    18: {0: "0.450240250624399189778881", 1: "0.479986457701842568620624", 2: "0.479718081839213852898461", 3: "0.456785281893599881457646"},
    20: {0: "0.491591844259603802774792", 1: "0.525013405473671034573828", 2: "0.529840941923840414118627", 3: "0.5138912590741687864763"},
    22: {0: "0.533561402196658302936626", 1: "0.570175895875374602950499", 2: "0.579203708263368313058318", 3: "0.568814776626046356298542"},
    24: {0: "0.576028244284529771482569", 1: "0.615477973311486669870347", 2: "0.628074591028772453046948", 3: "0.62226424258862154236681", 4: "0.600795393575369499703429"},
    26: {0: "0.618907903345212430917128", 1: "0.660915234633738459465654", 2: "0.676614267360108067757209", 3: "0.674676438601639337734454", 4: "0.658054755763025963517734"},
}

profiles = {n: {k: mp.mpf(v) for k, v in row.items()} for n, row in profiles.items()}

print("\n=== Audited saddle table ===")
best_rows = []
for n in sorted(profiles):
    row = profiles[n]
    best_k = max(row, key=lambda k: row[k])
    best_beta = row[best_k]
    best_rows.append((n, best_k, best_beta))
    values = ", ".join(f"k={k}: {fmt(row[k], 12)}" for k in sorted(row))
    print(f"N={n}, best_k={best_k}, best_beta={fmt(best_beta, 18)} | {values}")

print("\n=== Motion diagnostics ===")
gap_23 = []
gap_peak_guard = []
for n in [20, 22, 24, 26]:
    row = profiles[n]
    gap = row[2] - row[3]
    gap_23.append((n, gap))
    gap_peak_guard.append((n, mp.mpf("0.7") - max(row.values())))
    print(
        f"N={n}, beta(k=2)-beta(k=3)={fmt(gap, 18)}, "
        f"0.7-peak={fmt(mp.mpf('0.7') - max(row.values()), 18)}"
    )

# Linear extrapolation of the k=2 minus k=3 gap against N using N=20..26.
xs = [mp.mpf(n) for n, _gap in gap_23]
ys = [gap for _n, gap in gap_23]
s0 = mp.mpf(len(xs))
s1 = mp.fsum(xs)
s2 = mp.fsum(x * x for x in xs)
t0 = mp.fsum(ys)
t1 = mp.fsum(x * y for x, y in zip(xs, ys))
det = s0 * s2 - s1 * s1
a_gap = (t0 * s2 - t1 * s1) / det
b_gap = (s0 * t1 - s1 * t0) / det
cross_n = -a_gap / b_gap

peak_ns = [mp.mpf(n) for n, _k, _beta in best_rows[-4:]]
peak_ys = [beta for _n, _k, beta in best_rows[-4:]]
s0 = mp.mpf(len(peak_ns))
s1 = mp.fsum(peak_ns)
s2 = mp.fsum(x * x for x in peak_ns)
t0 = mp.fsum(peak_ys)
t1 = mp.fsum(x * y for x, y in zip(peak_ns, peak_ys))
det = s0 * s2 - s1 * s1
a_peak = (t0 * s2 - t1 * s1) / det
b_peak = (s0 * t1 - s1 * t0) / det
guard_cross = (mp.mpf("0.7") - a_peak) / b_peak

print(f"linear gap fit: gap23 ~= {fmt(a_gap, 18)} + {fmt(b_gap, 18)} N")
print(f"predicted k=3 over k=2 crossing N ~= {fmt(cross_n, 18)}")
print(f"linear peak fit from N=20..26: peak ~= {fmt(a_peak, 18)} + {fmt(b_peak, 18)} N")
print(f"predicted 0.7 crossing N ~= {fmt(guard_cross, 18)}")

best_k_sequence = [k for _n, k, _beta in best_rows]
peak_betas = [beta for _n, _k, beta in best_rows]

check(
    "fixed k=1 is falsified and fixed k=2 is not secure",
    best_k_sequence[:3] == [1, 1, 1] and best_k_sequence[-4:] == [2, 2, 2, 2] and cross_n < 30,
    f"best_k_sequence={best_k_sequence} predicted_k3_cross={fmt(cross_n, 18)}",
)
check(
    "audited peak beta is monotone increasing",
    all(peak_betas[i] < peak_betas[i + 1] for i in range(len(peak_betas) - 1)),
    f"last_peak={fmt(peak_betas[-1], 18)}",
)
check(
    "old 0.65 guard is false and 0.7 guard is not proved safe",
    peak_betas[-1] > mp.mpf("0.65") and guard_cross < 30,
    f"N26_peak={fmt(peak_betas[-1], 18)} predicted_0.7_cross={fmt(guard_cross, 18)}",
)
check(
    "moving-saddle theorem is now the honest target",
    cross_n > 26 and guard_cross > 26,
    f"cross_n={fmt(cross_n, 18)} guard_cross={fmt(guard_cross, 18)}",
)

print("\n=== Theorem status ===")
print(
    "The exact data are consistent with a moving defect saddle: k=1 gives way "
    "to k=2, and the k=3 gap is closing.  The 0.7 guard is only a finite "
    "observation, not a theorem.  The next proof must derive the saddle motion "
    "and limiting peak beta."
)

print("\n" + "=" * 80)
failed = False
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
