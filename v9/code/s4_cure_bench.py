#!/usr/bin/env python3
"""
s4_cure_bench.py — v9 round 5: THE CURE BENCH (note-s4; ALL gates pinned
there pre-run per #45). Phi_rate = argmin dS/max(|D|,1) vs argmin-dS vs the
beta = 0 control (with its own interior baseline printed — the M3 lesson),
at the forgery's own scale (n = 512) + an n = 256 continuity grid.
Pinned: P1 rate-arm r_I in [0.35, 0.65] >= 3/4 reps @512; P2 m_ab(rate) <
0.5 x m_ab(argmin) @512; P3 global r in [0.35, 0.55] every rate rep.
Verdicts: CURE-SUPPORTED / PARTIAL / CURE-REFUTED per the note.
Seed 20260709; float64; s1/s2 machinery verbatim.
"""
import numpy as np
from math import sqrt
from mpmath import mp, beta as mbeta, digamma, mpf, binomial

mp.dps = 60
rng = np.random.default_rng(20260709)

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


K_AB_CAP = 64      # S_ab increment truncation (note-s2, disclosed)

def delta_S_ab_capped(Ct, D):
    if not D.any():
        return 0.0
    Didx = np.nonzero(D)[0]
    tot = 0.0
    for x in Didx:
        I = np.nonzero(Ct[x] & D)[0]
        if M0 <= len(I) <= K_AB_CAP:
            tot += m_ab_sub(Ct[np.ix_(I, I)])
    return tot

def grow2(n, beta, arm, K=12):
    C = np.zeros((n, n), dtype=bool)
    nrel = 0
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
                d += delta_S_ab_capped(Ct, D)
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
    return C

def heredity_axis(C, n_top=6):
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

def sampled_mab(C, n_samp=40):
    ii, jj = np.nonzero(C)
    if len(ii) == 0:
        return float("nan")
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ok_idx = np.nonzero((btw[ii, jj] >= M0) & (btw[ii, jj] <= 256))[0]
    if len(ok_idx) == 0:
        return float("nan")
    pick = rng.choice(len(ok_idx), size=min(n_samp, len(ok_idx)), replace=False)
    vals = []
    for pdx in pick:
        x, y = ii[ok_idx[pdx]], jj[ok_idx[pdx]]
        I = np.nonzero(C[x] & C[:, y])[0]
        vals.append(m_ab_sub(C[np.ix_(I, I)]))
    return float(np.mean(vals))

def faithful_mab_baseline(N, n_samp=40, reps=3):
    vals = []
    for _ in range(reps):
        pts = rng.random((N, 2))
        C = (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])
        v = sampled_mab(C, n_samp)
        if not np.isnan(v):
            vals.append(v)
    return float(np.mean(vals))

# dim <= 2 capped oracle (u2's, standalone)
def dim_le_2_capped(C, cap=2_000_000):
    N = C.shape[0]
    nodes = list(range(N))
    incomp = [(i, j) for i in range(N) for j in range(i + 1, N)
              if not (C[i, j] or C[j, i])]
    if not incomp:
        return True
    adj = set()
    for (a, b) in incomp:
        adj.add((a, b)); adj.add((b, a))
    direction = {}
    work = [0]
    def force(a, b):
        changed = []
        stack = [(a, b)]
        while stack:
            work[0] += 1
            if work[0] > cap:
                raise TimeoutError
            x, y = stack.pop()
            key = frozenset((x, y))
            if key in direction:
                if direction[key] != (x, y):
                    for k in changed: del direction[k]
                    return None
                continue
            direction[key] = (x, y); changed.append(key)
            for z in nodes:
                if z == x or z == y: continue
                kyz = frozenset((y, z))
                if kyz in direction and direction[kyz] == (y, z):
                    if (x, z) in adj: stack.append((x, z))
                    else:
                        for k in changed: del direction[k]
                        return None
                kzx = frozenset((z, x))
                if kzx in direction and direction[kzx] == (z, x):
                    if (z, y) in adj: stack.append((z, y))
                    else:
                        for k in changed: del direction[k]
                        return None
        return changed
    elist = list(incomp)
    import sys
    sys.setrecursionlimit(100000)
    def bt(ei):
        if ei == len(elist): return True
        a, b = elist[ei]
        if frozenset((a, b)) in direction: return bt(ei + 1)
        for (x, y) in ((a, b), (b, a)):
            ch = force(x, y)
            if ch is not None:
                if bt(ei + 1): return True
                for k in ch:
                    if k in direction: del direction[k]
        return False
    try:
        return bt(0)
    except (TimeoutError, RecursionError):
        return None


def grow_rate(n, mode, arm="A1", K=12):
    """mode: 'rate' (argmin dS/max(|D|,1)), 'argmin', or 0 (uniform pick)."""
    C = np.zeros((n, n), dtype=bool)
    nrel = 0
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
            dS.append(d)
        dS = np.array(dS)
        if mode == "rate":
            nd = np.array([max(int(D.sum()), 1) for D in cands], dtype=float)
            pick = int(np.argmin(dS / nd))
        elif mode == "argmin":
            pick = int(np.argmin(dS))
        else:
            pick = int(rng.integers(len(cands)))
        C[:t, t] = cands[pick]
        nrel += int(cands[pick].sum())
    return C

print("[s4 cure bench]")
base512 = faithful_mab_baseline(512)
rows = {}
for tag, n, mode, arm, reps in (("rate-512", 512, "rate", "A1", 4),
                                 ("argmin-512", 512, "argmin", "A1", 2),
                                 ("ctrl-512", 512, 0, "A0", 2),
                                 ("rate-256", 256, "rate", "A1", 3),
                                 ("argmin-256", 256, "argmin", "A1", 3)):
    rows[tag] = []
    for rep in range(reps):
        C = grow_rate(n, mode, arm)
        r, H = descriptors(C)
        hed = heredity_axis(C)
        mab = sampled_mab(C)
        rows[tag].append((r, H, hed, mab))
        print(f"      {tag:>10} rep {rep}: r = {r:.3f}, H = {H}, r_I = "
              f"{hed:.3f}, m_ab = {mab:.4f}")
print(f"      faithful m_ab @512 = {base512:.4f}")

hd = [x[2] for x in rows["rate-512"] if not np.isnan(x[2])]
in_band = sum(1 for h in hd if 0.35 <= h <= 0.65)
p1 = in_band >= 3
check("P1 (the cure, primary): the rate arm's interiors land in the "
      "faithful band [0.35, 0.65] in >= 3/4 reps at n = 512 — vs the "
      "argmin's forged 0.69-0.88 (pinned pre-run, note-s4)", p1,
      f"r_I = {[round(h,3) for h in hd]} ({in_band}/4 in-band); argmin "
      f"this stream: {[round(x[2],3) for x in rows['argmin-512']]}; "
      f"ctrl (M3 baseline): {[round(x[2],3) for x in rows['ctrl-512']]}")

m_rate = float(np.mean([x[3] for x in rows["rate-512"]]))
m_arg = float(np.mean([x[3] for x in rows["argmin-512"]]))
p2 = m_rate < 0.5 * m_arg
check("P2: m_ab(rate) < 0.5 x m_ab(argmin) at 512 (pinned factor)", p2,
      f"rate {m_rate:.4f} vs argmin {m_arg:.4f} "
      f"({m_rate/m_arg:.2f}x; ctrl {float(np.mean([x[3] for x in rows['ctrl-512']])):.4f}; "
      f"faithful {base512:.4f})")

rs = [x[0] for x in rows["rate-512"]]
p3 = all(0.35 <= r <= 0.55 for r in rs)
check("P3 (no wall resurrected): the rate arm's global r stays in "
      "[0.35, 0.55] every rep", p3, f"r = {[round(r,3) for r in rs]}")

verdict = ("CURE-SUPPORTED" if (p1 and p2 and p3) else
           ("PARTIAL" if (p2 and not p1) else "CURE-REFUTED"))
print(f"  [INFO] pinned-verdict partition (note-s4): {verdict}")
print()
print(f"PRE-REGISTERED GATE LEDGER: P1 {'HELD' if p1 else 'REFUSED'}; "
      f"P2 {'HELD' if p2 else 'REFUSED'}; P3 {'HELD' if p3 else 'REFUSED'}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
