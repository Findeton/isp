#!/usr/bin/env python3
"""
s8_paper3_repairs.py — v9 round 9: the two receipts paper 3's round-1
review demands (note-s8; gates pinned there pre-run; seed 20260716).

PART A — THE JOINT ARM (review MAJOR-1): dS~ = [A - c|D|] + staged-C_rho
increment — both terms centered at their faithful expectations (note-s6
SS1's derivation shape COMPLETED). Registered predictions (the review's
arithmetic, adopted): at c = c_bar truth beats the EMPTY set at typical
loss steps; the large decoys decide. Measured, paired on one evaluation:
  A1 joint family curve at c in {0, 0.05, c_bar, 0.15, 0.20, 0.24};
  A2 staged-base dominance (larger AND staged-cheaper => loses all c>=0);
  A3 staged-base per-step oracle over c in [0, 1/4) — BOUNDS THE WHOLE
     TWO-TERM FAMILY.
  Gates: G-A1 branch at c_bar (>= 0.6 JOINT-PREFERRED / <= 0.3 REJECTED);
  G-A2 free-run bench at c_bar (r in [0.35,0.60] all; r_I in-band >= 3/4;
  m_ab <= 3x base); the CLASS verdict rides A3 vs the 0.3 line.

PART B — CHURN'S INTERIORS (review MAJOR-2): web_j3 (paper-16 corner,
M = 32, L = 2, verbatim u1 port) at N in {256, 512}, 4 reps; order =
dominance on (b, chi); instruments r_I / m_ab vs matching-N faithful
base. Gates per N: G-B1 r_I in [0.35, 0.65] >= 3/4; G-B2 m_ab <= 3x base.
web_kernel (u2 beta = 0) = ungated INFO rows. Both directions live.
Refused pinned gates print the ledger; exits 1 by design if any refuse.
"""
import numpy as np
from mpmath import mp, beta as mbeta, digamma, mpf, binomial

mp.dps = 60
rng = np.random.default_rng(20260716)

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
print("[s8 paper-3 repairs: (A) the joint arm; (B) churn interiors]")

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


# ---- c_bar calibration (arrival-level faithful mean per-pair charge, s6 form)
cb_acc = np.zeros(N); cb_cnt = np.zeros(N)
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    Cw = np.zeros((N, N), dtype=bool)
    for t in range(1, N):
        Cw[:t, t] = Ctrue[:t, t]
        D = Ctrue[:t, t]
        nd = int(D.sum())
        if nd > 0:
            Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
            cb_acc[t] += delta_S0(Ct, Ctf, D) / nd; cb_cnt[t] += 1
cbar_t = np.where(cb_cnt > 0, cb_acc / np.maximum(cb_cnt, 1), 0.25)
CBAR = float(cbar_t[64:].mean())
print(f"      c_bar calibrated: {CBAR:.4f} (scalar mean over t >= 64; < 1/4: {CBAR < 0.25})")

C_GRID = [0.0, 0.05, CBAR, 0.15, 0.20, 0.24]
WALL = 0.25

# ---- PART A: joint family on forced-faithful trajectories
fam_wins = np.zeros(len(C_GRID)); n_scored = 0
n_dom = 0; n_feas = 0
rep_wins_cbar = []
for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0; wc = 0; tot = 0
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
            n_scored += 1; tot += 1
            for ci, c in enumerate(C_GRID):
                dSt = dS - c * szs
                if dSt[0] <= dSt[1:].min():
                    fam_wins[ci] += 1
                    if ci == 2: wc += 1
            if bool(np.any((szs[1:] > szs[0]) & (dS[1:] <= dS[0]))):
                n_dom += 1
            lo, hi = 0.0, WALL
            feas = True
            for K in range(1, len(cands)):
                dsz = szs[0] - szs[K]; gap = dS[0] - dS[K]
                if dsz == 0:
                    if gap > 0: feas = False; break
                elif dsz > 0: lo = max(lo, gap / dsz)
                else: hi = min(hi, gap / dsz)
            if feas and lo <= hi and lo < WALL:
                n_feas += 1
        nrel += int(Ctrue[:t, t].sum())
    rep_wins_cbar.append(wc / tot)
print("      A1 joint family curve (paired, staged base):")
for ci, c in enumerate(C_GRID):
    tag = " <- c_bar (the derived point)" if ci == 2 else ""
    print(f"        c = {c:.4f}: truth-win rate {fam_wins[ci]/n_scored:.1%}{tag}")
rate_j = float(np.mean(rep_wins_cbar))
v = np.array(rep_wins_cbar)
tstat = (v.mean() - 1/14) / (v.std(ddof=1) / 2)
print(f"      G-A1 at c_bar: {rate_j:.1%} (reps {[round(x,3) for x in rep_wins_cbar]}); "
      f"chance [7.1%, 7.7%]; rep-level t vs 1/14 = {tstat:+.2f}")
branch_j = ("JOINT-PREFERRED" if rate_j >= 0.6 else
            ("REJECTED" if rate_j <= 0.3 else "MIXED"))
check("G-A1: the joint (fully-centered) arm's branch is decided at the "
      "pinned 0.6/0.3 lines — the review's live member, measured",
      rate_j >= 0.6 or rate_j <= 0.3, f"{branch_j} ({rate_j:.1%})")
dom_f = n_dom / n_scored; feas_f = n_feas / n_scored
print(f"      A2 staged-base dominance: {dom_f:.1%} of steps (truth loses "
      f"there at every c >= 0)")
print(f"      A3 staged-base per-step oracle: ANY c in [0, 0.25) rescues "
      f"truth at {feas_f:.1%} of steps — the TWO-TERM family's ceiling")
check("A-consistency: wins-at-c_bar <= feasible AND dominated <= infeasible "
      "(the s6b I-check treatment)",
      rate_j <= feas_f + 1e-9 and dom_f <= 1 - feas_f + 1e-12,
      f"{rate_j:.3f} <= {feas_f:.3f}; {dom_f:.3f} <= {1-feas_f:.3f}")
check("A3 CLASS GATE (pinned): the two-term family's oracle ceiling vs the "
      "0.3 rejection line — < 0.3 closes the class (paper 3 part 5 TRUE "
      "class-wide); >= 0.3 = the surviving-arm finding",
      feas_f < 0.3, f"oracle {feas_f:.1%} vs 0.30")

def dS_joint(Ct, Ctf, D, nrel, t):
    d = delta_S0(Ct, Ctf, D) - CBAR * float(D.sum())
    d += s_comp_stage(nrel + int(D.sum()), t + 1) - s_comp_stage(nrel, t)
    return d

print("      [G-A2 bench under the joint arm at c_bar — pure kernel menus]")
frs = []
for rep in range(4):
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Ct = Cw[:t, :t]; Ctf = Ct.astype(np.float32)
        menu = kernel_menu(Ct, t)
        dS = [dS_joint(Ct, Ctf, D, nrel, t) for D in menu]
        pick = int(np.argmin(dS))
        Cw[:t, t] = menu[pick]
        nrel += int(menu[pick].sum())
    r, H = descriptors(Cw)
    rI = heredity_axis2(Cw)
    mab = sampled_mab2(Cw)
    frs.append((r, rI, mab))
    print(f"      rep {rep}: r = {r:.3f}, r_I = {rI:.3f}, m_ab = {mab:.4f}")
base256 = float(np.mean([sampled_mab2((lambda p: (p[None,:,0]>p[:,None,0])&(p[None,:,1]>p[:,None,1]))(rng.random((N,2)))) for _ in range(3)]))
r_ok = all(0.35 <= x[0] <= 0.60 for x in frs)
band = sum(1 for x in frs if not np.isnan(x[1]) and 0.35 <= x[1] <= 0.65)
mabm = float(np.mean([x[2] for x in frs if not np.isnan(x[2])]))
gA2 = r_ok and band >= 3 and mabm <= 3 * base256
check("G-A2 (the joint production bench): r in-window all, r_I in-band "
      ">= 3/4, m_ab <= 3x faithful", gA2,
      f"r ok: {r_ok}; r_I in-band {band}/4; m_ab {mabm:.4f} = "
      f"{mabm/base256:.1f}x faithful (3x = {3*base256:.4f})")

# ---- PART B: churn interiors (web_j3 verbatim u1 port; M = 32, L = 2)
def web_j3(Nn, M, L):
    chi_acc = np.zeros(M)
    chi = np.zeros(Nn); lineage = np.zeros(Nn, dtype=np.int64)
    lid = np.arange(M).copy(); next_id = M
    mean_c = 0.109551
    for t in range(Nn):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(mean_c)
        chi[t] = chi_acc[c]; lineage[t] = lid[c]
        if rng.random() < 1.0 / L:
            chi_acc[c] = 0.0
            lid[c] = next_id; next_id += 1
    return np.arange(Nn), chi, lineage

def web_kernel(Nn, M, L):
    chi_acc = np.zeros(M)
    chi = np.zeros(Nn); lineage = np.zeros(Nn, dtype=np.int64)
    lid = np.arange(M).copy(); next_id = M
    mean_c = 0.109551
    for t in range(Nn):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(mean_c)
        chi[t] = chi_acc[c]; lineage[t] = lid[c]
        if rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            chi_acc[v] = 0.0
            lid[v] = next_id; next_id += 1
    return np.arange(Nn), chi, lineage

def churn_order(b, chi):
    return (b[None, :] > b[:, None]) & (chi[None, :] > chi[:, None])

gB_all = True
for Nn in (256, 512):
    base_N = float(np.mean([sampled_mab2((lambda p: (p[None,:,0]>p[:,None,0])&(p[None,:,1]>p[:,None,1]))(rng.random((Nn,2)))) for _ in range(3)]))
    rows = []
    for rep in range(4):
        b, chi, lin = web_j3(Nn, 32, 2)
        C = churn_order(np.arange(Nn), chi)
        r = 2.0 * C.sum() / (Nn * (Nn - 1))
        rI = heredity_axis2(C)
        mab = sampled_mab2(C)
        rows.append((r, rI, mab))
        print(f"      churn j3 N={Nn} rep {rep}: r = {r:.3f}, r_I = {rI:.3f}, "
              f"m_ab = {mab:.4f}")
    band = sum(1 for x in rows if not np.isnan(x[1]) and 0.35 <= x[1] <= 0.65)
    mabm = float(np.mean([x[2] for x in rows if not np.isnan(x[2])]))
    b1 = band >= 3
    b2 = mabm <= 3 * base_N
    check(f"G-B1 (churn interiors, N = {Nn}): r_I in the faithful band "
          f">= 3/4 reps — the bench every action arm faced, now the builder",
          b1, f"in-band {band}/4 (values {[round(x[1],3) for x in rows]})")
    check(f"G-B2 (churn abundance, N = {Nn}): m_ab <= 3x the matching-N "
          f"faithful base", b2,
          f"m_ab {mabm:.4f} = {mabm/base_N:.1f}x faithful (3x = {3*base_N:.4f})")
    gB_all = gB_all and b1 and b2
    for rep in range(2):
        b, chi, lin = web_kernel(Nn, 32, 2)
        C = churn_order(np.arange(Nn), chi)
        r = 2.0 * C.sum() / (Nn * (Nn - 1))
        print(f"      INFO kernel-variant N={Nn} rep {rep}: r = {r:.3f}, "
              f"r_I = {heredity_axis2(C):.3f}, m_ab = {sampled_mab2(C):.4f}")

print()
print(f"PRE-REGISTERED GATE LEDGER: G-A1 = {branch_j}; A3 oracle "
      f"{'< 0.3 (class CLOSED)' if feas_f < 0.3 else '>= 0.3 (LIVE WINDOW)'}; "
      f"G-A2 {'HELD' if gA2 else 'REFUSED'}; "
      f"Part B churn {'PASSED both N' if gB_all else 'REFUSED at >= 1 gate'}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
