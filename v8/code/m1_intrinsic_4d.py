#!/usr/bin/env python3
"""
m1_intrinsic_4d.py — v8 paper 15 addendum (Move 1): (A) the finder-gap test at
larger N in 2+1 (is the 1.5x/0.953 residual a finite-size effect?), and (B) the
INTRINSIC finder run in 3+1 — the last oracle step attacked.

(A) 2+1 GAP TEST: the paper-15 finder at N = 1000, K = 12 directions, 3
    bootstrap iterations (was N = 400, K = 8, 2 iters). Both gap metrics
    measured against the same verdict band (< 1.3x certified / 1.3-2x
    inconclusive / > 2x refused; (iii) gate 0.98).

(B) 4D INTRINSIC FINDER: t_hat = |past|^(1/4) - |future|^(1/4) (4D cones ~
    tau^4); transverse seed = chains -> coupling -> 3-COMPONENT MDS, extended
    to all elements by coupling weights; order-only scale calibration; the
    tomographic bootstrap with SPHERICAL harmonics (4-coefficient fit over the
    24 signed Fibonacci directions); scored by the 4D certifier with the
    verdict band; condition (iii) measured on the output. Whatever band it
    lands in is the result — all three arms admissible, none hardcoded.

Float discipline: float64; default_rng(20260702). DEMONSTRATED grade.
"""

import numpy as np

rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ============================== shared machinery ==============================
def sprinkle_3d(N):
    pts = np.empty((0, 3))
    while len(pts) < N:
        m = 6 * (N - len(pts)) + 64
        t = rng.uniform(-1, 1, m)
        x = rng.uniform(-1, 1, m)
        y = rng.uniform(-1, 1, m)
        keep = np.hypot(x, y) <= 1 - np.abs(t)
        pts = np.vstack([pts, np.column_stack([t, x, y])[keep]])
    return pts[:N]

def sprinkle_4d(N):
    pts = np.empty((0, 4))
    while len(pts) < N:
        m = 10 * (N - len(pts)) + 128
        t = rng.uniform(-1, 1, m)
        xyz = rng.uniform(-1, 1, (m, 3))
        keep = np.linalg.norm(xyz, axis=1) <= 1 - np.abs(t)
        pts = np.vstack([pts, np.column_stack([t, xyz])[keep]])
    return pts[:N]

def order_gen(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.linalg.norm(P[None, :, 1:] - P[:, None, 1:], axis=2)
    return (dt > 0) & (dt > dr)

def longest_chain(C, alive):
    idx = np.nonzero(alive)[0]
    if len(idx) == 0:
        return []
    sub = C[np.ix_(idx, idx)]
    n = len(idx)
    indeg = sub.sum(axis=0).astype(int)
    L = np.ones(n, dtype=int)
    par = -np.ones(n, dtype=int)
    stack = [i for i in range(n) if indeg[i] == 0]
    ind = indeg.copy()
    succ = [np.nonzero(sub[i])[0] for i in range(n)]
    while stack:
        v = stack.pop()
        for w_ in succ[v]:
            if L[v] + 1 > L[w_]:
                L[w_] = L[v] + 1
                par[w_] = v
            ind[w_] -= 1
            if ind[w_] == 0:
                stack.append(int(w_))
    end = int(np.argmax(L))
    chain = []
    v = end
    while v != -1:
        chain.append(int(idx[v]))
        v = int(par[v])
    return chain[::-1]

def chain_seed(C, d_trans, min_len, max_chains):
    """Order-only transverse seed: chains -> coupling -> d_trans-component MDS,
    coupling-weighted assignment to all elements. Raises on degenerate fleets."""
    N = C.shape[0]
    alive = np.ones(N, dtype=bool)
    chains = []
    while True:
        ch = longest_chain(C, alive)
        if len(ch) < min_len or len(chains) >= max_chains:
            break
        chains.append(ch)
        alive[ch] = False
    M = len(chains)
    if M < d_trans + 2:
        raise ValueError("degenerate chain fleet")
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(i + 1, M):
            ci, cj = chains[i], chains[j]
            cross = C[np.ix_(ci, cj)].sum() + C[np.ix_(cj, ci)].sum()
            W[i, j] = W[j, i] = cross / (len(ci) * len(cj))
    DIS = 1.0 - W
    np.fill_diagonal(DIS, 0.0)
    J = np.eye(M) - np.ones((M, M)) / M
    B = -0.5 * J @ (DIS ** 2) @ J
    w_eig, V = np.linalg.eigh(B)
    XY = V[:, -d_trans:] * np.sqrt(np.maximum(w_eig[-d_trans:], 0))
    coords = np.zeros((N, d_trans))
    for e in range(N):
        ws = np.array([
            (C[e, chains[c]].sum() + C[chains[c], e].sum()) / len(chains[c])
            for c in range(M)])
        if ws.sum() < 1e-9:
            ws = np.ones(M)
        ws = ws / ws.sum()
        coords[e] = ws @ XY
    return coords, M


# ============================== (A) 2+1 gap test ==============================
print("PART A: the 2+1 finder-gap test at N = 1000, K = 12, 3 bootstrap iters")
N3 = 1000
REF3 = sprinkle_3d(150_000)

def u3(P, th):
    return P[:, 0] - P[:, 1] * np.cos(th) - P[:, 2] * np.sin(th)

def certify3(r1, r2, th, Nn):
    ru = np.sort(u3(REF3, th))
    rv = np.sort(u3(REF3, th + np.pi))
    q1 = (r1 + 0.5) / Nn
    q2 = (r2 + 0.5) / Nn
    cu = np.searchsorted(ru, u3(REF3, th)) / len(REF3)
    cv = np.searchsorted(rv, u3(REF3, th + np.pi)) / len(REF3)
    order = np.argsort(q1)
    su, sv = q1[order], q2[order]
    ordr = np.argsort(cu)
    tu, tv = cu[ordr], cv[ordr]
    grid = np.linspace(0.05, 1.0, 40)
    best = 0.0
    for a in grid:
        k_sh = np.searchsorted(su, a, side="right")
        k_rf = np.searchsorted(tu, a, side="right")
        sh_v = np.sort(sv[:k_sh])
        rf_v = np.sort(tv[:k_rf])
        emp = np.searchsorted(sh_v, grid, side="right") / Nn
        tgt = np.searchsorted(rf_v, grid, side="right") / len(REF3)
        best = max(best, float(np.abs(emp - tgt).max()))
    return best

K3 = 12
TH3 = np.arange(K3) * np.pi / K3

def scores3(t_h, x_h, y_h, Nn):
    ws = []
    for th in TH3:
        u = t_h - x_h * np.cos(th) - y_h * np.sin(th)
        v = t_h + x_h * np.cos(th) + y_h * np.sin(th)
        ws.append(certify3(np.argsort(np.argsort(u)),
                           np.argsort(np.argsort(v)), th, Nn))
    return ws

def bootstrap3(t_h, x_h, y_h, Nn, iters=3):
    thetas = np.arange(2 * K3) * np.pi / K3
    A = np.column_stack([np.ones(2 * K3), np.cos(thetas), np.sin(thetas)])
    for _ in range(iters):
        U = np.empty((Nn, 2 * K3))
        for k_, th in enumerate(thetas):
            u = t_h - x_h * np.cos(th) - y_h * np.sin(th)
            ranks = np.argsort(np.argsort(u))
            ref_sorted = np.sort(u3(REF3, th))
            q = (ranks + 0.5) / Nn
            U[:, k_] = ref_sorted[np.clip((q * len(ref_sorted)).astype(int), 0,
                                          len(ref_sorted) - 1)]
        coef, _, _, _ = np.linalg.lstsq(A, U.T, rcond=None)
        t_h, x_h, y_h = coef[0], -coef[1], -coef[2]
    return t_h, x_h, y_h

P3 = sprinkle_3d(N3)
C3 = order_gen(P3)
past = C3.sum(axis=0).astype(float)
fut = C3.sum(axis=1).astype(float)
t_h = past ** (1 / 3) - fut ** (1 / 3)
tr, M3 = chain_seed(C3, 2, 8, 32)
t0 = (t_h - t_h.mean()) / max(t_h.std(), 1e-9)
sc = max(np.linalg.norm(tr, axis=1).std(), 1e-9)
xn, yn = tr[:, 0] / sc, tr[:, 1] / sc
best_s, best_w = None, np.inf
for s_ in np.geomspace(0.1, 3.0, 12):
    w_ = max(scores3(t0, s_ * xn, s_ * yn, N3)[:4])
    if w_ < best_w:
        best_w, best_s = w_, s_
th_, xh_, yh_ = bootstrap3(t0, best_s * xn, best_s * yn, N3, iters=3)
ws_A = scores3(th_, xh_, yh_, N3)
floors_A = []
for _ in range(3):
    sub = REF3[rng.choice(len(REF3), N3, replace=False)]
    floors_A.append(max(certify3(
        np.argsort(np.argsort(u3(sub, th))),
        np.argsort(np.argsort(u3(sub, th + np.pi))), th, N3) for th in TH3))
fl_A = float(np.mean(floors_A))
gap_A = max(ws_A) / fl_A
R_A = np.column_stack([th_, xh_, yh_])
agree_A = float((order_gen(R_A) == C3).mean())
verdict_A = ("CERTIFIED" if (gap_A < 1.3 and agree_A >= 0.98) else
             "INCONCLUSIVE" if gap_A < 2.0 else "REFUSED")
ok = gap_A < 2.0
check(f"2+1 at N = 1000/K = 12/3 iters: gap = {gap_A:.2f}x (was 1.5x at "
      f"N = 400), condition (iii) = {agree_A:.4f} (was 0.953; gate 0.98) — "
      f"verdict {verdict_A}; the finite-size hypothesis for the residual is "
      f"answered by these numbers, whichever way they fall", ok,
      f"max wD* = {max(ws_A):.4f} vs floor {fl_A:.4f}; M = {M3} chains")

# ============================== (B) intrinsic 4D ==============================
print("PART B: the INTRINSIC 4D finder (the last oracle step)")
N4 = 900
REF4 = sprinkle_4d(150_000)

def fib_hemi(K):
    out = []
    ga = np.pi * (3 - np.sqrt(5))
    for i in range(K):
        z = (i + 0.5) / K
        r = np.sqrt(1 - z * z)
        out.append([r * np.cos(ga * i), r * np.sin(ga * i), z])
    return np.array(out)

DIRS4 = fib_hemi(12)
DIRS4_ALL = np.vstack([DIRS4, -DIRS4])

def u4(P, n):
    return P[:, 0] - P[:, 1:] @ n

def certify4(r1, r2, n, Nn):
    ru = np.sort(u4(REF4, n))
    rv = np.sort(u4(REF4, -n))
    q1 = (r1 + 0.5) / Nn
    q2 = (r2 + 0.5) / Nn
    cu = np.searchsorted(ru, u4(REF4, n)) / len(REF4)
    cv = np.searchsorted(rv, u4(REF4, -n)) / len(REF4)
    order = np.argsort(q1)
    su, sv = q1[order], q2[order]
    ordr = np.argsort(cu)
    tu, tv = cu[ordr], cv[ordr]
    grid = np.linspace(0.05, 1.0, 40)
    best = 0.0
    for a in grid:
        k_sh = np.searchsorted(su, a, side="right")
        k_rf = np.searchsorted(tu, a, side="right")
        sh_v = np.sort(sv[:k_sh])
        rf_v = np.sort(tv[:k_rf])
        emp = np.searchsorted(sh_v, grid, side="right") / Nn
        tgt = np.searchsorted(rf_v, grid, side="right") / len(REF4)
        best = max(best, float(np.abs(emp - tgt).max()))
    return best

def scores4(t_h, XT, Nn):
    ws = []
    for n in DIRS4:
        u = t_h - XT @ n
        v = t_h + XT @ n
        ws.append(certify4(np.argsort(np.argsort(u)),
                           np.argsort(np.argsort(v)), n, Nn))
    return ws

def bootstrap4(t_h, XT, Nn, iters=3):
    A = np.column_stack([np.ones(len(DIRS4_ALL)), DIRS4_ALL])
    for _ in range(iters):
        U = np.empty((Nn, len(DIRS4_ALL)))
        for k_, n in enumerate(DIRS4_ALL):
            u = t_h - XT @ n
            ranks = np.argsort(np.argsort(u))
            ref_sorted = np.sort(u4(REF4, n))
            q = (ranks + 0.5) / Nn
            U[:, k_] = ref_sorted[np.clip((q * len(ref_sorted)).astype(int), 0,
                                          len(ref_sorted) - 1)]
        coef, _, _, _ = np.linalg.lstsq(A, U.T, rcond=None)
        t_h = coef[0]
        XT = -coef[1:4].T
    return t_h, XT

P4 = sprinkle_4d(N4)
C4 = order_gen(P4)
past4 = C4.sum(axis=0).astype(float)
fut4 = C4.sum(axis=1).astype(float)
t_h4 = past4 ** 0.25 - fut4 ** 0.25
tr4, M4 = chain_seed(C4, 3, 6, 40)
print(f"      chain fleet: M = {M4}")
# seed quality vs held-out
ct4 = float(np.corrcoef(t_h4, P4[:, 0])[0, 1])
A0 = tr4 - tr4.mean(0)
B0 = P4[:, 1:4] - P4[:, 1:4].mean(0)
U_, s_, Vt = np.linalg.svd(A0.T @ B0)
pc4 = float(np.corrcoef((A0 @ (U_ @ Vt)).ravel(), B0.ravel())[0, 1])
ok = ct4 > 0.9 and pc4 > 0.5
check(f"4D order-only seed quality: t_hat corr {ct4:.3f} (> 0.9); 3-component "
      f"transverse Procrustes {pc4:.3f} (> 0.5 — the 4D chains are shorter and "
      f"the transverse space bigger; the bar is deliberately lower and "
      f"disclosed)", ok, f"M = {M4} chains")

t04 = (t_h4 - t_h4.mean()) / max(t_h4.std(), 1e-9)
sc4 = max(np.linalg.norm(tr4, axis=1).std(), 1e-9)
XT0 = tr4 / sc4
best_s4, best_w4 = None, np.inf
for s_ in np.geomspace(0.1, 3.0, 12):
    w_ = max(scores4(t04, s_ * XT0, N4)[:4])
    if w_ < best_w4:
        best_w4, best_s4 = w_, s_
th4, XT4 = bootstrap4(t04, best_s4 * XT0, N4, iters=3)
ws_B = scores4(th4, XT4, N4)
floors_B = []
for _ in range(3):
    sub = REF4[rng.choice(len(REF4), N4, replace=False)]
    floors_B.append(max(certify4(
        np.argsort(np.argsort(u4(sub, n))),
        np.argsort(np.argsort(u4(sub, -n))), n, N4) for n in DIRS4))
fl_B = float(np.mean(floors_B))
gap_B = max(ws_B) / fl_B
R_B = np.column_stack([th4, XT4])
agree_B = float((order_gen(R_B) == C4).mean())
verdict_B = ("CERTIFIED" if (gap_B < 1.3 and agree_B >= 0.98) else
             "INCONCLUSIVE" if gap_B < 2.0 else "REFUSED")
# reconstruction quality vs held-out: the recovered SPATIAL frame is defined
# only up to a global rotation/reflection (the certificate is rotation-blind by
# construction), so per-axis correlations are meaningless — score t directly
# and the spatial block PROCRUSTES-ALIGNED
ct_rec = float(np.corrcoef(R_B[:, 0], P4[:, 0])[0, 1])
A0r = R_B[:, 1:4] - R_B[:, 1:4].mean(0)
B0r = P4[:, 1:4] - P4[:, 1:4].mean(0)
U_r, s_r, Vt_r = np.linalg.svd(A0r.T @ B0r)
pc_rec = float(np.corrcoef((A0r @ (U_r @ Vt_r)).ravel(), B0r.ravel())[0, 1])
ok = gap_B < 2.5 and ct_rec > 0.95 and pc_rec > 0.9
check(f"the INTRINSIC 4D finder: gap = {gap_B:.2f}x floor, condition (iii) = "
      f"{agree_B:.4f} — verdict {verdict_B} (band: <1.3 certified / 1.3-2 "
      f"inconclusive / >2 refused; all arms were admissible); held-out "
      f"reconstruction: t corr {ct_rec:.3f}, spatial Procrustes {pc_rec:.3f} "
      f"(the frame is recovered up to global rotation — per-axis correlations "
      f"are undefined under the certificate's own symmetry, a first-draft slip "
      f"corrected here)", ok,
      f"max wD* = {max(ws_B):.4f} vs floor {fl_B:.4f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
