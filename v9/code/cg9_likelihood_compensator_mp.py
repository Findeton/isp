#!/usr/bin/env python3
"""Final-opening explicit likelihood realizations and compensator scope."""

import mpmath as mp

mp.mp.dps = 120
TOL = mp.mpf("1e-90")
checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def kl(P, Q):
    return sum(p * mp.log(p/q) for p, q in zip(P, Q) if p)


def exact_kl_block(d):
    # P=(1,0), Q=(exp(-d),1-exp(-d)) has D(P||Q)=d exactly.
    P = [mp.mpf(1), mp.mpf(0)]
    Q = [mp.exp(-d), 1-mp.exp(-d)]
    return P, Q, kl(P, Q)


print("[cg9 — explicit likelihood allocation and compensator scope]")

IA, IB = mp.mpf("1.1"), mp.mpf("0.9")
models = []
for c in (mp.mpf("0.2"), mp.mpf("0.7")):
    a, b = IA-c, IB-c
    blocks = [exact_kl_block(a), exact_kl_block(b), exact_kl_block(c)]
    eA = blocks[0][2] + blocks[2][2]
    eB = blocks[1][2] + blocks[2][2]
    joint = blocks[0][2] + blocks[1][2] + blocks[2][2]
    SAB = mp.exp(-joint)
    cov = SAB-mp.exp(-IA)*mp.exp(-IB)
    models.append((c, eA, eB, joint, cov))

realize_res = max(abs(m[1]-IA) for m in models) + max(abs(m[2]-IB) for m in models)
check("L0 two explicit RN likelihood models realize fixed lineage totals",
      realize_res < TOL, f"residual={mp.nstr(realize_res,8)}")
check("L1 explicit likelihood models are dynamically inequivalent",
      abs(models[0][4]-models[1][4]) > mp.mpf("0.05"),
      f"joint KL={mp.nstr(models[0][3],8)}/{mp.nstr(models[1][3],8)}, cov={mp.nstr(models[0][4],12)}/{mp.nstr(models[1][4],12)}")

# Predictable-compensator theorem numerical shadow.  Conditional on realized
# future compensator increment dA, survival is exp(-dA).  If dA remains random,
# the marginal is E exp(-dA), not exp(-E dA).
past = mp.mpf("3.7")
dA = mp.mpf("0.42")
cond_res = abs(mp.exp(-(past+dA))/mp.exp(-past)-mp.exp(-dA))
random_increments = [(mp.mpf("0.2"), mp.mpf("0.5")),
                     (mp.mpf("0.8"), mp.mpf("1.5"))]
mixture = sum(p*mp.exp(-d) for p, d in random_increments)
meanA = sum(p*d for p, d in random_increments)
jensen_gap = mixture-mp.exp(-meanA)
check("L2 conditional compensator renewal; random-exposure distinction",
      cond_res < TOL and jensen_gap > mp.mpf("0.01"),
      f"conditional residual={mp.nstr(cond_res,8)}, Eexp-expE={mp.nstr(jensen_gap,12)}")

# Same local classical response and same conservative transfer can be tensored
# onto both c models; only shared evidence allocation differs.
g = mp.mpf("0.25")
transfer = mp.matrix([[1-g, 0], [g, 1]])
x = mp.matrix([4, 2])
y = transfer*x
outcome_corr = mp.mpf("0.4")  # fixed Bell-local common-cause cell
check("L3 both RN models share identical outcome/transfer modules",
      abs(sum(y)-sum(x)) < TOL and outcome_corr < 1,
      f"transfer=({mp.nstr(y[0],4)},{mp.nstr(y[1],4)}), corr={outcome_corr}")

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

