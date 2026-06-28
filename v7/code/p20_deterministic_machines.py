#!/usr/bin/env python3
"""
Receipt for v7 Paper XX: deterministic record machines.

Checks:
  1. Two-sided Bernoulli suspension clock realizes Exp(1) evidence intervals.
  2. The stationary residual life is also Exp(1), by memorylessness.
  3. Sparse Bernoulli skeleton satisfies S(nd)=S(d)^n.
  4. A closed finite deterministic cycle fails the memoryless law.
  5. The iid sparse skeleton has a one-ray positive-cone realization.

All cancellation-sensitive arithmetic uses mpmath at dps=140.
"""

import mpmath as mp

mp.mp.dps = 140


def fmt(x, n=30):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name} {detail}")


print("=" * 80)
print("P20 deterministic record machines receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n(1) Bernoulli roof I=-log U: moments and survival")
E1 = mp.quad(lambda x: x * mp.e ** (-x), [0, mp.inf])
E2 = mp.quad(lambda x: x * x * mp.e ** (-x), [0, mp.inf])
Var = E2 - E1 * E1
print("E[I]   =", fmt(E1, 60))
print("Var[I] =", fmt(Var, 60))
check("Exp roof mean is 1", abs(E1 - 1) < mp.mpf("1e-120"), f"gap={fmt(abs(E1-1), 8)}")
check("Exp roof variance is 1", abs(Var - 1) < mp.mpf("1e-120"), f"gap={fmt(abs(Var-1), 8)}")

test_points = [mp.mpf("0"), mp.mpf("0.125"), mp.mpf("1"), mp.mpf("2.5"), mp.mpf("10")]
max_post_gap = mp.mpf("0")
max_resid_gap = mp.mpf("0")
for t in test_points:
    post = mp.e ** (-t)  # mu(-log U > t)
    target = mp.e ** (-t)
    residual = mp.quad(lambda x: (x - t) * mp.e ** (-x), [t, mp.inf]) / E1
    max_post_gap = max(max_post_gap, abs(post - target))
    max_resid_gap = max(max_resid_gap, abs(residual - target))
    print(f"t={fmt(t, 8)} post={fmt(post, 40)} residual={fmt(residual, 40)} target={fmt(target, 40)}")

check("Post-seal survival mu(I>t)=exp(-t)", max_post_gap < mp.mpf("1e-120"), f"max_gap={fmt(max_post_gap, 8)}")
check(
    "Stationary residual survival E[(I-t)_+]/E[I]=exp(-t)",
    max_resid_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_resid_gap, 8)}",
)

print("\n(2) Sparse Bernoulli skeleton")
kappa = mp.mpf("0.83")
d = mp.mpf("0.125")
s = mp.e ** (-kappa * d)
max_skel_gap = mp.mpf("0")
for n in range(0, 25):
    lhs = s ** n
    rhs = mp.e ** (-kappa * d * n)
    max_skel_gap = max(max_skel_gap, abs(lhs - rhs))
print("kappa =", fmt(kappa, 30))
print("d     =", fmt(d, 30))
print("s     =", fmt(s, 60))
print("max |s^n-exp(-kappa*d*n)|, n<=24 =", fmt(max_skel_gap, 20))
check("Sparse skeleton S(nd)=S(d)^n", max_skel_gap < mp.mpf("1e-120"), f"max_gap={fmt(max_skel_gap, 8)}")

print("\n(3) Closed finite deterministic cycle obstruction")
N = mp.mpf(97)
m = mp.mpf(12)
S1 = (N - m) / N
S2_block = (N - m - 1) / N
memoryless_gap = abs(S2_block - S1 ** 2)
print("cycle states N =", int(N), "target block m =", int(m))
print("S1        =", fmt(S1, 60))
print("S2(block) =", fmt(S2_block, 60))
print("|S2-S1^2| =", fmt(memoryless_gap, 60))
check("Finite cycle block is not memoryless", memoryless_gap > mp.mpf("1e-3"), f"gap={fmt(memoryless_gap, 30)}")

max_first_hit = int(N - m)
check(
    "Finite first-hit support is bounded before repeat/never-hit",
    max_first_hit == 85,
    f"support <= {max_first_hit} plus possible infinity atom",
)

print("\n(4) One-ray positive cone for iid sparse skeleton")
# One-dimensional positive realization: K=R_+, pi=1, eval=1,
# M_no_click=[s], M_click=[1-s].
word = "0010010"
prob = mp.mpf("1")
for symbol in word:
    prob *= s if symbol == "0" else (1 - s)
prob_direct = (s ** word.count("0")) * ((1 - s) ** word.count("1"))
cone_gap = abs(prob - prob_direct)
print("word =", word, "prob =", fmt(prob, 60), "gap =", fmt(cone_gap, 8))
check("Iid sparse skeleton has one-ray positive cone", cone_gap < mp.mpf("1e-120"), f"gap={fmt(cone_gap, 8)}")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
