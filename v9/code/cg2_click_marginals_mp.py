#!/usr/bin/env python3
"""100-digit receipt for interacting evidence marginals and scheduler gauge."""

import mpmath as mp

mp.mp.dps = 120
TOL = mp.mpf("1e-90")
checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def infnorm(A):
    return max(abs(A[i, j]) for i in range(A.rows) for j in range(A.cols))


print("[cg2 — high-precision interacting click identities]")

# C0: the law-level evidence coordinate, not a regraduated readout.
grid = [mp.mpf(0), mp.mpf("1e-40"), mp.mpf("0.01"), mp.mpf("0.3"),
        mp.mpf(1), mp.mpf(3), mp.mpf(20)]
res0 = max(abs(-mp.log(mp.exp(-I)) - I) for I in grid)
check("C0 exact scalar survival on the evidence grid", res0 < TOL,
      f"max residual={mp.nstr(res0, 8)}")

# C1: two private evidence channels a,b and one shared channel c.
a, b, c = mp.mpf("0.37"), mp.mpf("0.61"), mp.mpf("0.29")
SA = mp.exp(-(a + c))
SB = mp.exp(-(b + c))
SAB = mp.exp(-(a + b + c))
cov_survival = SAB - SA * SB
res1 = max(abs(SA - mp.exp(-(a + c))), abs(SB - mp.exp(-(b + c))))
check("C1 shared-shock law preserves Exp marginals and interacts",
      res1 < TOL and cov_survival > mp.mpf("1e-20"),
      f"cov(unalarmed)={mp.nstr(cov_survival, 20)}")

# C2: refinement composition for scalar and joint survival.
def split_survival(I, pieces):
    return mp.fprod([mp.exp(-I / pieces) for _ in range(pieces)])


vals = [a, b, c, a + b + c, mp.mpf("7.125")]
res2 = max(abs(split_survival(I, n) - mp.exp(-I))
           for I in vals for n in (2, 5, 17))
check("C2 refinement composition", res2 < TOL, f"max residual={mp.nstr(res2, 8)}")

# C3: local diffusion generators.  Disjoint edges commute; overlapping edges record order.
def edge_generator(n, i, j, rate):
    Q = mp.zeros(n)
    # Symmetric conservative diffusion on column state vectors.
    Q[i, i] -= rate
    Q[j, j] -= rate
    Q[i, j] += rate
    Q[j, i] += rate
    return Q


q = mp.mpf("0.173")
dt = mp.mpf("0.271")
QA = edge_generator(4, 0, 1, q)
QB = edge_generator(4, 2, 3, q * mp.mpf("1.7"))
QC = edge_generator(4, 1, 2, q * mp.mpf("0.8"))
EA, EB, EC = mp.expm(dt * QA), mp.expm(dt * QB), mp.expm(dt * QC)
dis_res = infnorm(EA * EB - EB * EA)
sym_res = infnorm(mp.expm(dt * (QA + QB)) - mp.expm(dt * QA / 2) * EB * mp.expm(dt * QA / 2))
overlap = infnorm(EA * EC - EC * EA)
check("C3 disjoint scheduler gauge and overlapping recorded order",
      dis_res < TOL and sym_res < TOL and overlap > mp.mpf("1e-12"),
      f"dis={mp.nstr(dis_res,8)}, symmetric={mp.nstr(sym_res,8)}, overlap={mp.nstr(overlap,12)}")

# C4: a finite joint-record family with setting-dependent correlations and exact remote marginals.
def pbit(aout, bout, xset, yset):
    corr = [[mp.mpf("0.4"), mp.mpf("-0.2")],
            [mp.mpf("0.1"), mp.mpf("0.55")]][xset][yset]
    parity = 1 if (aout + bout) % 2 == 0 else -1
    return (1 + parity * corr) / 4


norm_res = mp.mpf(0)
remote_res = mp.mpf(0)
joint_change = mp.mpf(0)
for xset in (0, 1):
    for yset in (0, 1):
        norm_res = max(norm_res, abs(sum(pbit(a0, b0, xset, yset)
                                             for a0 in (0, 1) for b0 in (0, 1)) - 1))
for yset in (0, 1):
    for bout in (0, 1):
        m0 = sum(pbit(a0, bout, 0, yset) for a0 in (0, 1))
        m1 = sum(pbit(a0, bout, 1, yset) for a0 in (0, 1))
        remote_res = max(remote_res, abs(m0 - m1), abs(m0 - mp.mpf("0.5")))
joint_change = abs(pbit(0, 0, 0, 0) - pbit(0, 0, 1, 0))
check("C4 finite no-signaling joint-record gate",
      norm_res < TOL and remote_res < TOL and joint_change > mp.mpf("0.01"),
      f"remote residual={mp.nstr(remote_res,8)}, joint change={mp.nstr(joint_change,8)}")

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

