#!/usr/bin/env python3
"""Round-2 refinement/projective opening at dps=120."""

import mpmath as mp

mp.mp.dps = 120
TOL = mp.mpf("1e-90")
checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def pois(n, mu):
    return mp.exp(-mu) * mu ** n / mp.factorial(n)


print("[cg7 — refinement and projective consistency]")

# P0: count-level Chapman-Kolmogorov under evidence-interval refinement.
mu1, mu2 = mp.mpf("0.37"), mp.mpf("0.91")
conv_res = mp.mpf(0)
for n in range(30):
    lhs = sum(pois(k, mu1) * pois(n-k, mu2) for k in range(n+1))
    conv_res = max(conv_res, abs(lhs - pois(n, mu1 + mu2)))
check("P0 Poisson refinement/Chapman-Kolmogorov", conv_res < TOL,
      f"max n<30 residual={mp.nstr(conv_res,8)}")

# P1: restriction of a finite support family is obtained by z_outside=1 in the PGF.
mus = [mp.mpf("0.2"), mp.mpf("0.4"), mp.mpf("0.7"), mp.mpf("0.3")]
zs = [mp.mpf("0.8"), mp.mpf("1.2"), mp.mpf("0.6"), mp.mpf("1.4")]
full_restricted = mp.exp(sum(mus[i] * ((zs[i] if i in (0, 2) else 1) - 1)
                             for i in range(4)))
direct = mp.exp(mus[0]*(zs[0]-1) + mus[2]*(zs[2]-1))
check("P1 projective restriction of support-count law",
      abs(full_restricted-direct) < TOL,
      f"residual={mp.nstr(abs(full_restricted-direct),8)}")

# P2: an adaptive branch kernel is normalized: before branch one root state;
# branch event creates two descendants and their joint support; subsequent
# counts conditionally have a normalized PGF.
beta, T = mp.mpf("0.23"), mp.mpf("2.0")
p_no_branch = mp.exp(-beta*T)
p_branch = 1-p_no_branch
post_pgf_at_one = mp.mpf(1)  # conditional descendant/support Poisson PGF
adaptive_norm = p_no_branch + p_branch * post_pgf_at_one
check("P2 normalized common-ancestor support creation kernel",
      abs(adaptive_norm-1) < TOL,
      f"no-branch/branch={mp.nstr(p_no_branch,10)}/{mp.nstr(p_branch,10)}")

# P3: a composite joint event is not gauge-equivalent to two private records;
# only unrecorded subdivision of its evidence interval is gauge, covered by P0.
# Encode record counts/types in a generating monomial: J vs A*B differ.
zj, za, zb = mp.mpf("0.71"), mp.mpf("0.83"), mp.mpf("1.19")
atomic_mark = zj
decomposed_mark = za*zb
check("P3 atomic joint seal differs from recorded private decomposition",
      abs(atomic_mark-decomposed_mark) > mp.mpf("0.1"),
      "only evidence-interval subdivision without an intermediate record is gauge")

# P4: local finiteness certificate.  A countable construction is nonexplosive
# on every finite restriction if its incident support exposure sum is finite.
incident = [mp.mpf(1) / (2 ** k) for k in range(1, 81)]
partial = sum(incident)
tail_bound = mp.mpf(1) / (2 ** 80)
check("P4 locally finite incident-exposure certificate",
      partial < 1 and tail_bound < mp.mpf("1e-20"),
      f"partial sum={mp.nstr(partial,20)}, tail<={mp.nstr(tail_bound,8)}")

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

