#!/usr/bin/env python3
"""
s7_stage_priced.py — v9 round 8: THE STAGE-PRICED GROWTH TEST ("arm C";
note-s7, gates pinned there pre-run). Row C's endpoint target 1/2 is
replaced ALONG THE PATH by the faithful stage profile rho(t) (calibrated,
4 oracle profiles, edge-normalized window-15 smoothing); the endpoint
functional is untouched (rho(N) -> 1/2), so the grader and its walls are
unchanged — arm C re-prices the path only. Row A untouched.

PINNED (note-s7 SS2-3):
  C-rho: calibrated rho over t in [64, 128] within +-0.02 of the DERIVED
     flat value 1/3 (sub-diagonal triangle, exact); |rho(N) - 1/2| <= 0.02.
  G1: marginal truth-preference (14-candidate menus, forced-faithful,
     t >= 64, 4 reps, tie-generous <=): >= 0.6 STAGE-PRICED-PREFERRED /
     <= 0.3 REJECTED / else MIXED. Chance line PRE-REGISTERED: null in
     [1/14, 1/13] = [7.1%, 7.7%]; rep-level t vs 1/14 printed.
  D1 (registered mechanism signature): the s6b decomposition in-receipt —
     EXPECTED: Row-C dominance collapses (|Row-C|>|Row-A| at losses falls
     from 93.8% to < 50%) and the truth-vs-winner Row-C gap centers near 0.
  G2 (runs whatever G1's branch): free-run pure-kernel endpoints, 4 reps:
     r in [0.35, 0.60] all reps; r_I in [0.35, 0.65] >= 3/4; m_ab <= 3x
     the 3-sprinkling faithful base.
Seed 20260715; float64 accumulators over the float32 Gram fast-path
(decision-invariance carried from the round-7 review, s5/s6 streams); n = 256.
Refused pinned gates print the ledger; exits 1 by design if any refuse.
"""
import numpy as np
from mpmath import mp, beta as mbeta, digamma, mpf, binomial

mp.dps = 60
rng = np.random.default_rng(20260715)

PASS = 0
FAIL = 0
M0 = 8

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ------------------------------------------------ exact abundance reference
_EA = {}
def EA_exact(k, j):
    if (k, j) not in _EA:
        if k - 2 - j < 0:
            _EA[(k, j)] = 0.0
        else:
            b = mpf(k - 1 - j)
            t1 = mbeta(j + 1, b) * (digamma(k) - digamma(j + 1))
            t2 = mbeta(j + 2, b) * (digamma(k + 1) - digamma(j + 2))
            t3 = -2 * mbeta(j + 1, k - j)
            _EA[(k, j)] = float(mpf(k) * (k - 1) * binomial(k - 2, j) * (t1 + t2 + t3))
    return _EA[(k, j)]

def m_ab_sub(sub):
    """Per-interval abundance misfit of an interval's induced order (bool
    matrix sub, k x k), per note-t11: sum_j (A_j/k - EA_j(k)/k)^2, J = 2."""
    k = sub.shape[0]
    if k < M0:
        return 0.0
    f = sub.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ints = btw[sub]
    tot = 0.0
    for j in range(3):
        A = int(np.sum(ints == j))
        tot += (A / k - EA_exact(k, j) / k) ** 2
    return tot

# ------------------------------------------------ u2's action machinery
def delta_S0(Ct, Ctf, D):
    if not D.any():
        return 0.0
    Didx = np.nonzero(D)[0]
    Mmat = (Ct[Didx, :] & D[None, :]).astype(np.float32)
    k = Mmat.sum(1)
    edges = ((Mmat @ Ctf) * Mmat).sum(1)
    denom = np.maximum(k * (k - 1), 1.0)
    r = 2.0 * edges / denom
    charge = np.where(k >= M0, (r - 0.5) ** 2, 0.25)
    return float(charge.sum())

def descriptors(C):
    N = C.shape[0]
    r_frac = 2.0 * C.sum() / (N * (N - 1))
    indeg = C.sum(axis=0).astype(int)
    L = np.ones(N, dtype=int)
    Cl = [np.nonzero(C[i])[0] for i in range(N)]
    ind = indeg.copy()
    stack = [i for i in range(N) if ind[i] == 0]
    topo = []
    while stack:
        v = stack.pop(); topo.append(v)
        for w in Cl[v]:
            ind[w] -= 1
            if ind[w] == 0: stack.append(w)
    for v in topo:
        if len(Cl[v]): L[Cl[v]] = np.maximum(L[Cl[v]], L[v] + 1)
    return float(r_frac), int(L.max())

def sprinkling_order(n):
    pts = rng.random((n, 2))
    order = np.argsort(pts[:, 0] + pts[:, 1])
    pts = pts[order]
    C = (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])
    return pts, C

def kernel_menu(Ct, t, K=12):
    cands = [np.zeros(t, dtype=bool)]
    while len(cands) < K + 1:
        p = float(np.exp(rng.uniform(np.log(min(1.0 / t, 0.59)), np.log(0.6))))
        anc = rng.random(t) < p
        D = anc | Ct[:, anc].any(axis=1) if anc.any() else anc
        cands.append(D)
    return cands

def heredity_axis2(C, n_top=6):
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ii, jj = np.nonzero(C)
    sizes = btw[ii, jj]
    order = np.argsort(-sizes)
    rIs = []
    for idx in order[:n_top * 3]:
        if sizes[idx] < 16 or len(rIs) >= n_top:
            break
        x, y = ii[idx], jj[idx]
        I = np.nonzero(C[x] & C[:, y])[0]
        k = len(I)
        sub = C[np.ix_(I, I)]
        rIs.append(2.0 * sub.sum() / (k * (k - 1)))
    return float(np.mean(rIs)) if rIs else float("nan")

def sampled_mab2(C, n_samp=40):
    ii, jj = np.nonzero(C)
    if len(ii) == 0: return float("nan")
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ok_idx = np.nonzero((btw[ii, jj] >= M0) & (btw[ii, jj] <= 256))[0]
    if len(ok_idx) == 0: return float("nan")
    pick = rng.choice(len(ok_idx), size=min(n_samp, len(ok_idx)), replace=False)
    vals = []
    for pdx in pick:
        x, y = ii[ok_idx[pdx]], jj[ok_idx[pdx]]
        I = np.nonzero(C[x] & C[:, y])[0]
        vals.append(m_ab_sub(C[np.ix_(I, I)]))
    return float(np.mean(vals))


N = 256
print("[s7 stage-priced growth test (arm C), n = 256]")

# ---- calibrate rho(t): faithful prefix comparability by stage (4 oracles)
rho_acc = np.zeros(N + 1); rho_cnt = np.zeros(N + 1)
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    nrel = 0
    for t in range(1, N):
        if t >= 2:
            rho_acc[t] += nrel / (t * (t - 1) / 2.0); rho_cnt[t] += 1
        nrel += int(Ctrue[:t, t].sum())
    rho_acc[N] += nrel / (N * (N - 1) / 2.0); rho_cnt[N] += 1
rho = np.where(rho_cnt > 0, rho_acc / np.maximum(rho_cnt, 1), 0.5)
kern = np.ones(15)
num = np.convolve(np.where(rho_cnt > 0, rho, 0.0), kern, mode="same")
den = np.convolve((rho_cnt > 0).astype(float), kern, mode="same")
rho_s = np.where(den > 0, num / den, 0.5)
rho_s[N] = rho[N]                      # endpoint pinned to its own estimate
flat = float(rho_s[64:129].mean())
print(f"      rho(t) calibrated: flat-regime mean {flat:.4f} (derived 1/3 = "
      f"0.3333); rho(N) = {rho[N]:.4f} (target 1/2); "
      f"range [{rho_s[64:].min():.3f}, {rho_s[64:].max():.3f}]")
check("C-rho: the calibration reproduces the DERIVED flat value 1/3 in the "
      "sub-diagonal regime and returns to 1/2 at completion — the stage "
      "profile is the derived object, not a fit",
      abs(flat - 1/3) <= 0.02 and abs(rho[N] - 0.5) <= 0.02,
      f"flat {flat:.4f} vs 1/3; endpoint {rho[N]:.4f} vs 0.5")

def s_comp_stage(nrel, n):
    if n < 2: return 0.0
    npair = n * (n - 1) / 2.0
    r = nrel / npair
    return npair * (r - rho_s[min(n, N)]) ** 2

def dS_armC(Ct, Ctf, D, nrel, t):
    d = delta_S0(Ct, Ctf, D)
    d += s_comp_stage(nrel + int(D.sum()), t + 1) - s_comp_stage(nrel, t)
    return d

# ---- G1 + D1 on forced-faithful trajectories
reps_rate = []
n_loss = 0; n_bigger = 0; n_C_dom = 0
gapA_acc = []; gapC_acc = []
aw_acc = []; at_acc = []; wsz_acc = []; tsz_acc = []
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    truth_wins = 0; total = 0
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Cw[:t, t] = Ctrue[:t, t]
        if t >= 64:
            Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
            truth = Ctrue[:t, t].copy()
            menu = kernel_menu(Ct, t)
            cands = [truth] + menu
            szs = np.array([int(D.sum()) for D in cands])
            A = np.array([delta_S0(Ct, Ctf, D) for D in cands])
            Cc = np.array([s_comp_stage(nrel + s, t + 1) - s_comp_stage(nrel, t)
                           for s in szs])
            dS = A + Cc
            total += 1
            if dS[0] <= dS[1:].min():
                truth_wins += 1
            else:
                w = 1 + int(np.argmin(dS[1:]))
                n_loss += 1
                if szs[w] > szs[0]: n_bigger += 1
                gA = A[0] - A[w]; gC = Cc[0] - Cc[w]
                gapA_acc.append(gA); gapC_acc.append(gC)
                aw_acc.append(float(A[w])); at_acc.append(float(A[0]))
                wsz_acc.append(int(szs[w])); tsz_acc.append(int(szs[0]))
                if abs(gC) > abs(gA): n_C_dom += 1
        nrel += int(Ctrue[:t, t].sum())
    reps_rate.append(truth_wins / total)
rate = float(np.mean(reps_rate))
v = np.array(reps_rate)
tstat = (v.mean() - 1 / 14) / (v.std(ddof=1) / 2)
print(f"      G1 rate: {rate:.1%} (reps {[round(r,3) for r in reps_rate]}); "
      f"chance null [7.1%, 7.7%]; rep-level t vs 1/14 = {tstat:+.2f}")
branch = ("STAGE-PRICED-PREFERRED" if rate >= 0.6 else
          ("REJECTED" if rate <= 0.3 else "MIXED"))
check("G1: the stage-priced branch is decided at the pinned 0.6/0.3 lines "
      "— the global term's derivation-shaped re-pricing, the re-pricing "
      "program's last member",
      rate >= 0.6 or rate <= 0.3, f"{branch} ({rate:.1%})")
dom = n_C_dom / max(n_loss, 1)
print(f"      D1 decomposition (loss steps: {n_loss}): winner larger "
      f"{n_bigger/max(n_loss,1):.1%}; Row-A gap mean "
      f"{np.mean(gapA_acc) if gapA_acc else 0:+.3f}; Row-C gap mean "
      f"{np.mean(gapC_acc) if gapC_acc else 0:+.3f}; |Row-C|>|Row-A| at "
      f"{dom:.1%}")
wsz = np.array(wsz_acc); awv = np.array(aw_acc)
print(f"      D1 winner anatomy (round-8 review, MINOR-3 print owed): "
      f"empty-set winner {float((wsz == 0).mean()):.1%} of losses; "
      f"A_winner mean {awv.mean():.3f} / median {np.median(awv):.3f} vs "
      f"A_truth mean {np.mean(at_acc):.3f}; winner |D| mean {wsz.mean():.1f} "
      f"/ median {np.median(wsz):.0f} vs truth |D| mean {np.mean(tsz_acc):.1f}; "
      f"gapA > 0 at {float((np.array(gapA_acc) > 0).mean()):.1%}")
check("D1 (registered signature): the Row-C dominance collapses under the "
      "stage profile (from 93.8% raw to < 50%) — the transient is "
      "neutralized; the residual selection is Row A + fluctuations",
      dom < 0.5, f"dominance {dom:.1%} vs registered < 50%")

# ---- G2: free-run production bench under arm C (pure kernel menus)
print("      [G2 bench under arm C — pure kernel menus]")
frs = []
for rep in range(4):
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
        menu = kernel_menu(Ct, t)
        dS = [dS_armC(Ct, Ctf, D, nrel, t) for D in menu]
        pick = int(np.argmin(dS))
        Cw[:t, t] = menu[pick]
        nrel += int(menu[pick].sum())
    r, H = descriptors(Cw)
    rI = heredity_axis2(Cw)
    mab = sampled_mab2(Cw)
    frs.append((r, rI, mab))
    print(f"      rep {rep}: r = {r:.3f}, r_I = {rI:.3f}, m_ab = {mab:.4f}")
base = float(np.mean([sampled_mab2((lambda p: (p[None,:,0]>p[:,None,0])&(p[None,:,1]>p[:,None,1]))(rng.random((N,2)))) for _ in range(3)]))
r_ok = all(0.35 <= x[0] <= 0.60 for x in frs)
band = sum(1 for x in frs if not np.isnan(x[1]) and 0.35 <= x[1] <= 0.65)
mabm = float(np.mean([x[2] for x in frs if not np.isnan(x[2])]))
g2 = r_ok and band >= 3 and mabm <= 3 * base
check("G2 (the production bench): free-run endpoints under arm C — r in "
      "the guard window all reps, r_I in the faithful band >= 3/4, m_ab "
      "<= 3x faithful (the branch verdicts either way are the round's "
      "result)", g2,
      f"r ok: {r_ok}; r_I in-band {band}/4; m_ab {mabm:.4f} = "
      f"{mabm/base:.1f}x faithful (3x ceiling {3*base:.4f})")

print()
print(f"PRE-REGISTERED GATE LEDGER: C-rho {'HELD' if abs(flat-1/3) <= 0.02 and abs(rho[N]-0.5) <= 0.02 else 'REFUSED'}; "
      f"G1 = {branch}; D1 {'COLLAPSED' if dom < 0.5 else 'PERSISTED'}; "
      f"G2 {'HELD' if g2 else 'REFUSED'}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
