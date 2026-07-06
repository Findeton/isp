#!/usr/bin/env python3
"""
s6_repricing_test.py — v9 round 7: THE RE-PRICING TEST (note-s6; gates
pinned there pre-run). Arm A: r-term centered by exact Var(r_k). Arm B:
the allowance form dS~ = dS - c_bar_t * |D| (c_bar_t = the arrival-level
faithful mean per-pair charge, empirically calibrated from 4 oracle
profiles this round — CALIBRATED, not yet derived; closed form = the
accompanying theory task). G1: s5's marginal-preference rate per arm
(>= 0.6 REPRICED-PREFERRED / <= 0.3 rejected). G2 (best arm, PURE kernel
menus — the production setting): endpoints r in [0.35, 0.60] (overshoot
guard), r_I in [0.35, 0.65] >= 3/4, m_ab <= 3x faithful.
Seed 20260713; float64 with the float32 Gram fast-path (decision-
invariance verified 0/1536 flips by the round-7 code review); s5
machinery verbatim; n = 256. Smoothing edge-normalized (round-7 fix).
"""
import numpy as np
from mpmath import mp, beta as mbeta, digamma, mpf, binomial

mp.dps = 60
rng = np.random.default_rng(20260713)

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

def s_comp(nrel, n):
    if n < 2:
        return 0.0
    r = 2.0 * nrel / (n * (n - 1))
    return (n * (n - 1) / 2) * (r - 0.5) ** 2

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

def delta_S0_centered(Ct, Ctf, D):
    """Arm A: qualifying pairs pay (r-1/2)^2 - Var(r_k); links unchanged."""
    if not D.any(): return 0.0
    Didx = np.nonzero(D)[0]
    Mm = (Ct[Didx, :] & D[None, :]).astype(np.float32)
    k = Mm.sum(1)
    edges = ((Mm @ Ctf) * Mm).sum(1)
    r = 2.0 * edges / np.maximum(k * (k - 1), 1.0)
    vr = (2.0 / np.maximum(k * (k - 1), 1.0)) * (2 * np.maximum(k - 2, 0) / 36.0 + 0.25)
    charge = np.where(k >= M0, (r - 0.5) ** 2 - vr, 0.25)
    return float(charge.sum())

N = 256
print("[s6 re-pricing test, n = 256]")

# calibrate c_bar_t from 4 oracle trajectories (mean per-pair A1 charge by t)
def sprinkling_order(n):
    pts = rng.random((n, 2))
    order = np.argsort(pts[:, 0] + pts[:, 1])
    pts = pts[order]
    C = (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])
    return pts, C

cbar_acc = np.zeros(N); cbar_cnt = np.zeros(N)
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Cw[:t, t] = Ctrue[:t, t]
        D = Ctrue[:t, t]
        nd = int(D.sum())
        if nd > 0:
            Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
            d0 = delta_S0(Ct, Ctf, D)
            cbar_acc[t] += d0 / nd; cbar_cnt[t] += 1
        nrel += nd
cbar = np.where(cbar_cnt > 0, cbar_acc / np.maximum(cbar_cnt, 1), 0.25)
# smooth (moving average, window 15) for a stable allowance profile
kern = np.ones(15)
num = np.convolve(cbar, kern, mode="same")
den = np.convolve(np.ones_like(cbar), kern, mode="same")
cbar_s = num / den
print(f"      c_bar_t calibrated: mean {cbar_s[64:].mean():.4f}, max "
      f"{cbar_s[64:].max():.4f} over t >= 64 (mean AND max < 0.25 as the "
      f"wall arithmetic requires: "
      f"{bool(cbar_s[64:].mean() < 0.25 and cbar_s[64:].max() < 0.25)}; "
      f"spread across t: sd {cbar_s[64:].std():.4f})")

def dS_arm(Ct, Ctf, D, nrel, t, arm):
    if arm == "A":
        d = delta_S0_centered(Ct, Ctf, D)
    else:
        d = delta_S0(Ct, Ctf, D) - cbar_s[t] * float(D.sum())
    d += s_comp(nrel + int(D.sum()), t + 1) - s_comp(nrel, t)
    return d

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


# G1: marginal preference per arm along faithful trajectories
rates = {}
for arm in ("A", "B"):
    prefs = []
    for rep in range(4):
        pts, Ctrue = sprinkling_order(N)
        Cw = np.zeros((N, N), dtype=bool)
        nrel = 0; wins = 0; tot = 0
        for t in range(1, N):
            Cw[:t, t] = Ctrue[:t, t]
            if t >= 64:
                Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
                truth = Ctrue[:t, t].copy()
                menu = kernel_menu(Ct, t)
                dT = dS_arm(Ct, Ctf, truth, nrel, t, arm)
                dK = [dS_arm(Ct, Ctf, D, nrel, t, arm) for D in menu]
                tot += 1
                if dT <= min(dK): wins += 1
            nrel += int(Ctrue[:t, t].sum())
        prefs.append(wins / tot)
    rates[arm] = float(np.mean(prefs))
    print(f"      arm {arm}: marginal-preference rate = {rates[arm]:.1%} "
          f"(reps {[round(x, 3) for x in prefs]})")
brA = "REPRICED-PREFERRED" if rates["A"] >= 0.6 else ("REJECTED" if rates["A"] <= 0.3 else "MIXED")
brB = "REPRICED-PREFERRED" if rates["B"] >= 0.6 else ("REJECTED" if rates["B"] <= 0.3 else "MIXED")
check("G1: the centered-action family's marginal-preference branches are "
      "decided (pinned 0.6/0.3) — the inverse problem's first derivation-"
      "shaped candidates measured against s5's landscape verdict",
      (rates["A"] >= 0.6 or rates["A"] <= 0.3) and (rates["B"] >= 0.6 or rates["B"] <= 0.3),
      f"arm A = {brA} ({rates['A']:.1%}); arm B = {brB} ({rates['B']:.1%})")

# G2: free-run production bench under the better arm (pure kernel menus)
best = "B" if rates["B"] >= rates["A"] else "A"
print(f"      [G2 bench under arm {best} — pure kernel menus]")
frs = []
for rep in range(4):
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
        menu = kernel_menu(Ct, t)
        dS = [dS_arm(Ct, Ctf, D, nrel, t, best) for D in menu]
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
check("G2 (the production bench): endpoints under the re-priced argmin "
      "with PURE kernel menus — r in the overshoot-guarded window, "
      "interiors in the faithful band >= 3/4, m_ab <= 3x faithful "
      "(passing = the production mechanism reborn, DEMONSTRATED-"
      "calibrated; the branch verdicts either way are the round's result)",
      g2, f"r ok: {r_ok}; r_I in-band {band}/4; m_ab {mabm:.4f} vs 3x "
          f"faithful {3*base:.4f}")

print()
print(f"PRE-REGISTERED GATE LEDGER: G1 arm A = {brA}, arm B = {brB}; "
      f"G2 {'HELD' if g2 else 'REFUSED'} (arm {best})")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
