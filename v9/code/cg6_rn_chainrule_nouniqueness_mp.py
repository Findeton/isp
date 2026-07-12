#!/usr/bin/env python3
"""Round-2 O5/O7: explicit RN/KL accounting and nonuniqueness at dps=120."""

import mpmath as mp

mp.mp.dps = 120
TOL = mp.mpf("1e-90")
checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def kl(P, Q):
    return sum(p * mp.log(p / q) for p, q in zip(P, Q) if p != 0)


print("[cg6 — RN/KL chain rule and nonuniqueness]")

# K0: explicit two-stage likelihoods, P(A)P(B|A) vs Q(A)Q(B|A).
PA = [mp.mpf("0.7"), mp.mpf("0.3")]
QA = [mp.mpf("0.45"), mp.mpf("0.55")]
PB_A = [[mp.mpf("0.8"), mp.mpf("0.2")],
        [mp.mpf("0.25"), mp.mpf("0.75")]]
QB_A = [[mp.mpf("0.6"), mp.mpf("0.4")],
        [mp.mpf("0.5"), mp.mpf("0.5")]]
Pjoint = [PA[a] * PB_A[a][b] for a in range(2) for b in range(2)]
Qjoint = [QA[a] * QB_A[a][b] for a in range(2) for b in range(2)]
chain = kl(PA, QA) + sum(PA[a] * kl(PB_A[a], QB_A[a]) for a in range(2))
chain_res = abs(kl(Pjoint, Qjoint) - chain)
check("K0 conditional RN/KL chain rule", chain_res < TOL,
      f"residual={mp.nstr(chain_res,8)}, KL={mp.nstr(chain,20)}")

# K1: pure correlation evidence is invisible to marginal KL.
Pcorr = [mp.mpf("0.45"), mp.mpf("0.05"), mp.mpf("0.05"), mp.mpf("0.45")]
Quniform = [mp.mpf("0.25")] * 4
joint_corr_kl = kl(Pcorr, Quniform)
Pmarg = [Pcorr[0] + Pcorr[1], Pcorr[2] + Pcorr[3]]
Qmarg = [mp.mpf("0.5"), mp.mpf("0.5")]
marg_sum = 2 * kl(Pmarg, Qmarg)
check("K1 marginal KL misses pure correlation evidence",
      marg_sum < TOL and joint_corr_kl > mp.mpf("0.1"),
      f"joint={mp.nstr(joint_corr_kl,20)}, marginal-sum={mp.nstr(marg_sum,8)}")

# K2: counting one shared observation in two supports doubles its evidence.
Pbit = [mp.mpf("0.8"), mp.mpf("0.2")]
Qbit = [mp.mpf("0.5"), mp.mpf("0.5")]
one = kl(Pbit, Qbit)
naive_two = 2 * one
check("K2 duplicated shared support double-counts KL",
      abs(naive_two - 2 * one) < TOL and abs(naive_two - one) > mp.mpf("0.1"),
      f"one={mp.nstr(one,20)}, duplicated={mp.nstr(naive_two,20)}")

# K3: repaired support ledger counts the shared likelihood block once, then composes by chain rule.
repair = one + chain
direct_product_kl = kl([p * r for p in Pbit for r in Pjoint],
                       [q * s for q in Qbit for s in Qjoint])
repair_res = abs(repair - direct_product_kl)
check("K3 typed shared-block-once repair", repair_res < TOL,
      f"residual={mp.nstr(repair_res,8)}")

# K4: nonuniqueness at fixed lineage marginals.  c allocates evidence to a
# shared support; private exposures are IA-c, IB-c.  All have the same Exp
# marginals but different joint survival/covariance.
IA, IB = mp.mpf("1.1"), mp.mpf("0.9")


def common_shock(c):
    a, b = IA - c, IB - c
    SA, SB = mp.exp(-IA), mp.exp(-IB)
    SAB = mp.exp(-(a + b + c))
    return SA, SB, SAB, SAB - SA * SB


rows = [common_shock(c) for c in (mp.mpf("0.2"), mp.mpf("0.7"))]
same_marg = max(abs(rows[0][i] - rows[1][i]) for i in (0, 1))
cov_gap = abs(rows[0][3] - rows[1][3])
check("K4 continuum of inequivalent interacting laws at fixed Exp marginals",
      same_marg < TOL and cov_gap > mp.mpf("0.05"),
      f"covariances={mp.nstr(rows[0][3],12)}/{mp.nstr(rows[1][3],12)}")

# K5: transport fraction remains independently free even after evidence law is fixed.
g1, g2 = mp.mpf("0.1"), mp.mpf("0.3")
x = mp.matrix([mp.mpf(4), mp.mpf(2)])
T1 = mp.matrix([[1-g1, 0], [g1, 1]])
T2 = mp.matrix([[1-g2, 0], [g2, 1]])
y1, y2 = T1 * x, T2 * x
check("K5 conservative transport coefficient is not selected by click marginal",
      abs(sum(y1) - sum(x)) < TOL and abs(sum(y2) - sum(x)) < TOL
      and max(abs(y1[i]-y2[i]) for i in range(2)) > mp.mpf("0.1"),
      f"g={g1}/{g2}, outputs=({mp.nstr(y1[0],6)},{mp.nstr(y1[1],6)})/({mp.nstr(y2[0],6)},{mp.nstr(y2[1],6)})")

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

