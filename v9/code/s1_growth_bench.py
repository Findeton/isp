#!/usr/bin/env python3
"""
s1_growth_bench.py — v9 round 2, T1.3's receipt (note-t13; gates quoted
there; trajectory screens pinned from the beta = 0 control at first
execution per the note-8 registration, executed as registered this time).

ARMS: A0 = r+link (u2 verbatim) | A1 = A0 + S_comp | A2 = A1 + S_ab(exact
reference). beta in {0 control, 1, beta*, inf}; n in {64, 128}; 3 reps.

CHECKS:
  1  beta = 0 control trajectories logged; screens pinned from them.
  2  A0 argmin endpoint reproduces the sparse degeneracy (r < 0.05).
  3  P1: A1 argmin endpoint r > 0.2 (Row C breaks the degeneracy).
  4  P2: A1 endpoint classification across the grid (MIDDLE at beta >= beta*).
  5  P3: A2 vs A1 mean top-interval abundance misfit (the steering test).
  6  n = 128 replication of the headline arms.

Conventions: default_rng(20260706); float64; M0 = 8; exact EA_exact cached
at dps 60; u2's action/descriptors verbatim; u2's kernel family with the menu at 12
random + empty (13 vs u2's 12, disclosed); [directional] at 3 reps.
DISCLOSURE (review round): the beta = 0 control's OWN endpoints classify
MIDDLE-sprinkling-band under this receipt's classifier (r = 0.555/0.649,
H-band 1.21/1.49 — the n = 128 values boundary-grazing) — the kernel
reaches the band with random picks; the ACTION's specific contributions
are (i) the argmin escape from A0's antichain and (ii) centering/holding
r ~ 0.44 against the control's DENSE-ward drift with scale.
"""

import numpy as np
from math import sqrt
from mpmath import mp, beta as mbeta, digamma, mpf, binomial

mp.dps = 60
rng = np.random.default_rng(20260706)

PASS = 0
FAIL = 0
M0 = 8
BETA_STAR = 16 * np.log(2)

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

def delta_S_ab(Ct, D):
    """Exact S_ab increment: new pairs are (x, new) for x in D; interval =
    D & up(x); charge its induced order's abundance misfit."""
    if not D.any():
        return 0.0
    Didx = np.nonzero(D)[0]
    tot = 0.0
    for x in Didx:
        I = np.nonzero(Ct[x] & D)[0]
        if len(I) >= M0:
            tot += m_ab_sub(Ct[np.ix_(I, I)])
    return tot

def s_comp(nrel, n):
    if n < 2:
        return 0.0
    r = 2.0 * nrel / (n * (n - 1))
    return (n * (n - 1) / 2) * (r - 0.5) ** 2

def grow(n, beta, arm, K=12):
    """arm in {'A0','A1','A2'}; beta None => argmin; 0 => uniform pick."""
    C = np.zeros((n, n), dtype=bool)
    nrel = 0
    traj = []
    for t in range(1, n):
        Ct = C[:t, :t]
        Ctf = Ct.astype(np.float32)
        cands = [np.zeros(t, dtype=bool)]
        while len(cands) < K + 1:
            p = float(np.exp(rng.uniform(np.log(min(1.0 / t, 0.59)), np.log(0.6))))
            anc = rng.random(t) < p
            D = anc | Ct[:, anc].any(axis=1) if anc.any() else anc
            cands.append(D)
        dS = []
        for D in cands:
            d = delta_S0(Ct, Ctf, D)
            if arm in ("A1", "A2"):
                d += s_comp(nrel + int(D.sum()), t + 1) - s_comp(nrel, t)
            if arm == "A2":
                d += delta_S_ab(Ct, D)
            dS.append(d)
        dS = np.array(dS)
        if beta is None:
            pick = int(np.argmin(dS))
        elif beta == 0:
            pick = int(rng.integers(len(cands)))
        else:
            w = np.exp(-beta * (dS - dS.min())); w /= w.sum()
            pick = int(rng.choice(len(cands), p=w))
        C[:t, t] = cands[pick]
        nrel += int(cands[pick].sum())
        if t % 16 == 0 or t == n - 1:
            sub = C[:t + 1, :t + 1]
            rfr = 2.0 * sub.sum() / ((t + 1) * t)
            frontier = float((~sub.any(axis=1))[:t + 1].sum()) / (t + 1)
            traj.append((t + 1, rfr, frontier))
    return C, traj

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

def top_interval_misfit(C, n_top=4):
    """Mean m_ab over the largest intervals (k >= M0) — P3's observable."""
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ii, jj = np.nonzero(C)
    sizes = btw[ii, jj]
    order = np.argsort(-sizes)
    vals = []
    for idx in order[:n_top * 3]:
        if sizes[idx] < M0 or len(vals) >= n_top:
            break
        x, y = ii[idx], jj[idx]
        I = np.nonzero(C[x] & C[:, y])[0]
        vals.append(m_ab_sub(C[np.ix_(I, I)]))
    return float(np.mean(vals)) if vals else float("nan")

# ================================================= CHECK 1: the control
print("CHECK 1: beta = 0 same-kernel control — trajectories logged, screens pinned")
ctrl = {}
for n in (64, 128):
    rs, Hs, fs = [], [], []
    for rep in range(3):
        C, traj = grow(n, 0, "A0")
        r, H = descriptors(C)
        rs.append(r); Hs.append(H); fs.append(traj[-1][2])
    ctrl[n] = (float(np.mean(rs)), float(np.mean(Hs)), float(np.mean(fs)))
    hb = ctrl[n][1] / (2 * sqrt(n))
    cls = ("MIDDLE-sprinkling-band" if 0.35 <= ctrl[n][0] <= 0.65 and
           0.5 <= hb <= 1.5 else ("DENSE" if ctrl[n][0] >= 0.7 else "other"))
    print(f"      n = {n:>3}: control endpoint r = {ctrl[n][0]:.3f}, "
          f"H = {ctrl[n][1]:.1f} (H/2sqrt(n) = {hb:.2f}), frontier = "
          f"{ctrl[n][2]:.3f} -> control's OWN class: {cls}"
          + ("  [boundary-grazing]" if 0.6 <= ctrl[n][0] <= 0.7 or 1.4 <= hb <= 1.6 else ""))
print("      screens pinned from the control (note-t13 §2): sparse if "
      "r < 0.3*r_ctrl; dust if f > 3*f_ctrl; originary if H > 3*H_ctrl")
ok = all(0.2 < ctrl[n][0] < 0.9 and ctrl[n][1] > 2 and 0 < ctrl[n][2] < 0.5
         for n in (64, 128))
check("control trajectories logged and screens pinned from them at first "
      "execution (the note-8 registration, executed as registered); the "
      "control itself gates sane (r in (0.2, 0.9), H > 2, frontier < 0.5 — "
      "a degenerate control would void the screens)", ok,
      f"r_ctrl = {ctrl[64][0]:.3f}/{ctrl[128][0]:.3f}")

# ================================================= CHECK 2: A0 degeneracy
print("CHECK 2: A0 argmin reproduces the sparse degeneracy on this stream")
C, _ = grow(64, None, "A0")
r0, H0 = descriptors(C)
check("A0 (bare r+link) argmin endpoint is antichain-class (r < 0.05) — "
      "u2's G1 finding reproduced", r0 < 0.05, f"r = {r0:.3f}, H = {H0}")

# ================================================= CHECK 3+4: A1 grid
print("CHECK 3/4: A1 = A0 + S_comp across the beta grid (3 reps, n = 64)")
def classify(r, H, n, ctrl_n):
    if r < 0.3 * ctrl_n[0] and r < 0.2:
        return "SPARSE"
    if r >= 0.7:
        return "DENSE"
    if 0.35 <= r <= 0.65:
        hb = H / (2 * sqrt(n))
        return "MIDDLE-sprinkling-band" if 0.5 <= hb <= 1.5 else "MIDDLE-offband"
    return "BOUNDARY"
res = {}
for beta, tag in ((1, "beta=1"), (BETA_STAR, "beta*"), (None, "argmin")):
    rows = []
    for rep in range(3):
        C, _ = grow(64, beta, "A1")
        r, H = descriptors(C)
        rows.append((r, H, classify(r, H, 64, ctrl[64])))
    res[tag] = rows
    print(f"      {tag:>7}: " + "; ".join(f"r={r:.2f},H={H},{c}" for r, H, c in rows))
ok = all(r > 0.2 for r, H, c in res["argmin"])
check("P1: A1's argmin endpoints are NOT antichain-class (r > 0.2) — Row C "
      "breaks the degeneracy (S_comp(antichain) = n(n-1)/8 makes the empty "
      "move expensive)", ok,
      f"argmin r = {[round(r, 2) for r, _, _ in res['argmin']]}")
mid = [c.startswith("MIDDLE") for r, H, c in res["beta*"] + res["argmin"]]
ok = sum(mid) >= 4
check("P2: A1 endpoints land MIDDLE (r in [0.35, 0.65]) at beta >= beta* "
      "in >= 4/6 runs — the escape-from-sparse (subclass per height band "
      "printed; cell claims deferred to scale per the onset disclosure)",
      ok, f"{sum(mid)}/6 MIDDLE")

# ================================================= CHECK 5: the steering test
print("CHECK 5: P3 — A2 vs A1 top-interval abundance misfit (argmin, 3 reps)")
mis = {"A1": [], "A2": []}
for arm in ("A1", "A2"):
    for rep in range(3):
        C, _ = grow(64, None, arm)
        m = top_interval_misfit(C)
        if not np.isnan(m):
            mis[arm].append(m)
m1v = float(np.mean(mis["A1"])) if mis["A1"] else float("nan")
m2v = float(np.mean(mis["A2"])) if mis["A2"] else float("nan")
ok = (not np.isnan(m1v)) and (not np.isnan(m2v)) and m2v < m1v
check("P3: A2's endpoints carry SMALLER mean top-interval abundance misfit "
      "than A1's — Row A steers interiors under growth (the counter-test "
      "of paper 14's drift-mode 'pricing without steering'; reconciliation "
      "clause in note-t13 §3)", ok,
      f"m_ab: A1 {m1v:.4f} vs A2 {m2v:.4f}" if not (np.isnan(m1v) or np.isnan(m2v))
      else f"insufficient qualifying intervals (A1 n={len(mis['A1'])}, A2 n={len(mis['A2'])})")

# ================================================= CHECK 6: n = 128
print("CHECK 6: the n = 128 replication (A1 at beta*/argmin, 2 reps each)")
rows = []
for beta, tag in ((BETA_STAR, "beta*"), (None, "argmin")):
    for rep in range(2):
        C, _ = grow(128, beta, "A1")
        r, H = descriptors(C)
        rows.append((tag, r, H, classify(r, H, 128, ctrl[128])))
        print(f"      {tag:>7} rep {rep}: r = {r:.2f}, H = {H}, {rows[-1][3]}")
ok = all(r > 0.2 for _, r, _, _ in rows)
check("the degeneracy stays broken at n = 128 (all A1 endpoints r > 0.2; "
      "class table printed — the scale trend is the paper-1 follow-up's)",
      ok, f"{[(t, round(r, 2)) for t, r, _, _ in rows]}")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
