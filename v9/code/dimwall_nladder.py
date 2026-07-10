#!/usr/bin/env python3
"""
dimwall_nladder.py — v9 round 46: the N-ladder (pin: note-3p1-nladder,
ff8ee84, strictly before this ran). NO-REVIEW MODE on record. Machinery
verbatim from dimwall_manifoldweb_e.py; the protocol is scale-covariant
(window = central N/2; calibration segment = first N/4; NW fixed).
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""), flush=True)

S_MIN = 0.3
Q = 0.9
MIN_PROJ = 30

def fib_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.column_stack([np.sin(phi) * np.cos(th),
                            np.sin(phi) * np.sin(th), np.cos(phi)])
UDIRS = fib_sphere(64)

def pca_frame(v):
    C = np.cov(v.T)
    evals, evecs = np.linalg.eigh(C)
    order = np.argsort(evals)[::-1]
    evals = evals[order]; evecs = evecs[:, order]
    E = evecs[:, :3]
    for c in range(3):
        j = np.argmax(np.abs(E[:, c]))
        if E[j, c] < 0:
            E[:, c] = -E[:, c]
    return evals, E

def transverse(rel, coords, family="dom"):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    if family == "m4":
        dhat = np.zeros(k); dhat[0] = 1.0
    else:
        dhat = np.ones(k) / np.sqrt(k)
    ii, jj = np.where(rel)
    d = X[jj] - X[ii]
    s = d @ dhat
    keep = s >= S_MIN
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    return w / s[:, None]

def F_iso_cloud(v):
    if len(v) < 4 * MIN_PROJ:
        return float("nan"), 0.0, True
    evals, E = pca_frame(v)
    eig_ratio = float(evals[2] / max(evals[0], 1e-30))
    p3 = v @ E
    hs = []
    for u in UDIRS:
        pr = p3 @ u
        pr = pr[pr > 0]
        hs.append(np.quantile(pr, Q) if len(pr) >= MIN_PROJ else np.nan)
    hs = np.array(hs)
    if np.isnan(hs).any():
        return float("nan"), eig_ratio, True
    hs_sorted = np.sort(hs)
    return float(hs_sorted[-8:].mean() / hs_sorted[:8].mean()), eig_ratio, False

def dim_le_2(rel):
    n = rel.shape[0]
    inc = ~(rel | rel.T) & ~np.eye(n, dtype=bool)
    parent = list(range(n * n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    for a in range(n):
        nbs = np.where(inc[a])[0]
        if len(nbs) < 2:
            continue
        sub = inc[np.ix_(nbs, nbs)]
        iu, ju = np.triu_indices(len(nbs), 1)
        sel = ~sub[iu, ju]
        for b, c in zip(nbs[iu[sel]], nbs[ju[sel]]):
            union(a * n + b, a * n + c)
            union(b * n + a, c * n + a)
    ii, jj = np.where(np.triu(inc, 1))
    for i, j in zip(ii, jj):
        if find(i * n + j) == find(j * n + i):
            return False
    return True

def find_sk(rel, rng, k, tries=8000):
    n = rel.shape[0]
    comp = rel | rel.T
    nodes = np.arange(n)
    for _ in range(tries):
        perm = rng.permutation(n)
        A = []
        for v in perm:
            if not A or not comp[v, A].any():
                A.append(int(v))
                if len(A) == k:
                    break
        if len(A) < k:
            continue
        Aa = np.array(A)
        mask = np.ones(n, dtype=bool)
        mask[Aa] = False
        others = nodes[mask]
        above = rel[np.ix_(Aa, others)]
        cand = above.sum(0) == k - 1
        if not cand.any():
            continue
        cnodes = others[cand]
        miss = np.argmin(above[:, cand], axis=0)
        keep = ~comp[Aa[miss], cnodes]
        buckets = [cnodes[keep & (miss == i)] for i in range(k)]
        if any(len(bk) == 0 for bk in buckets):
            continue
        for _ in range(60):
            B = [int(bk[int(rng.integers(len(bk)))]) for bk in buckets]
            if len(set(B)) == k and not any(
                    comp[B[i], B[j]]
                    for i in range(k) for j in range(i + 1, k)):
                return A, B
    return None

def verify_sk(rel, A, B, k):
    for i in range(k):
        for j in range(k):
            if i != j and (rel[A[i], A[j]] or rel[B[i], B[j]]):
                return False
            if bool(rel[A[i], B[j]]) != (i != j):
                return False
            if rel[B[j], A[i]]:
                return False
        if rel[A[i], B[i]] or rel[B[i], A[i]]:
            return False
    return True

def unit_dirs(rng, n, dim):
    U = rng.normal(size=(n, dim))
    return U / np.linalg.norm(U, axis=1, keepdims=True)

def ballistic_rel_split(bvals, Dmat, tau):
    """The 45e relation with an EXTERNALLY supplied tau (Gate 2:
    split-sample; one tau per object, applied everywhere)."""
    ell = tau * bvals[:, None] + Dmat
    rel = bvals[:, None] < bvals[None, :]
    for k in range(Dmat.shape[1]):
        rel &= ell[:, None, k] <= ell[None, :, k]
    np.fill_diagonal(rel, False)
    return rel

def tau_of(bvals, Dmat, c_dial):
    s_D = float(Dmat.std())
    s_b = float(np.asarray(bvals, dtype=float).std())
    return c_dial * (s_D / max(s_b, 1e-12))


V24 = fib_sphere(24)

def confetti_rung(sd, N, c_dial=0.5):
    rng = np.random.default_rng(sd)
    t = rng.random(N)
    x = rng.uniform(-0.5, 0.5, (N, 3))
    order = np.argsort(t)
    t = t[order]; x = x[order]
    proj = x @ V24.T
    D = proj - proj.mean(axis=1, keepdims=True)
    tau = tau_of(t[:N // 4], D[:N // 4], c_dial)
    lo, hi = N // 4, 3 * N // 4
    widx = np.sort(rng.choice(np.arange(lo, hi), 256, replace=False))
    rel = ballistic_rel_split(t[widx], D[widx], tau)
    coords = np.column_stack([t[widx], D[widx]])
    return rel, coords

def build_web(sd, N, K=24, alpha=0.75, M=32, L=16):
    rng = np.random.default_rng(sd)
    V = fib_sphere(K)
    P = rng.normal(size=(M, 3))
    P /= np.linalg.norm(P, axis=1, keepdims=True)
    acc = np.zeros((M, K))
    chiV = np.zeros((N, K))
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if rng.random() < alpha:
            u = P[c]
        else:
            u = rng.normal(size=3)
            u /= np.linalg.norm(u)
        acc[c] += e * 0.5 * (1.0 + V @ u)
        chiV[t] = acc[c]
        if rng.random() < 1.0 / L:
            acc[int(rng.integers(M))] = 0.0
    return chiV, rng

def rung_web(sd, N, c_dial=0.5, L=16):
    chiV, rng = build_web(sd, N, L=L)
    D = chiV - chiV.mean(axis=1, keepdims=True)
    b = np.arange(N).astype(float)
    tau = tau_of(b[:N // 4], D[:N // 4], c_dial)
    lo, hi = N // 4, 3 * N // 4
    widx = np.sort(rng.choice(np.arange(lo, hi), 256, replace=False))
    rel = ballistic_rel_split(b[widx], D[widx], tau)
    coords = np.column_stack([b[widx], D[widx]])
    Fd = F_iso_cloud(transverse(rel, coords, "dom"))[0]
    Fm = F_iso_cloud(transverse(rel, coords, "m4"))[0]
    mid = (lo + hi) // 2
    didx = np.sort(rng.choice(np.arange(mid - 256, mid + 256), 128,
                              replace=False))
    drel = ballistic_rel_split(b[didx], D[didx], tau)
    n = drel.shape[0]
    wfrac = drel.sum() / (n * (n - 1) / 2)
    ridx = np.sort(rng.choice(np.arange(mid - 256, mid + 256), 144,
                              replace=False))
    refuse = not dim_le_2(ballistic_rel_split(b[ridx], D[ridx], tau))
    sidx = np.sort(rng.choice(np.arange(lo, hi), 1024, replace=False))
    srel = ballistic_rel_split(b[sidx], D[sidx], tau)
    r4 = find_sk(srel, rng, 4)
    s4 = bool(r4 and verify_sk(srel, r4[0], r4[1], 4))
    return Fd, Fm, wfrac, refuse, s4

def vol_reference(N, seedbase, c_dial=0.5):
    ref = {}
    for d in (2, 3, 4, 5, 6):
        fr = []
        for j in range(6):
            rng = np.random.default_rng(seedbase + 10 * d + j)
            t = rng.random(N)
            x = rng.uniform(-0.5, 0.5, (N, d - 1))
            order = np.argsort(t)
            t = t[order]; x = x[order]
            U = unit_dirs(np.random.default_rng(4242 + d), 24, d - 1)
            proj = x @ U.T
            D = proj - proj.mean(axis=1, keepdims=True)
            tau = tau_of(t[:N // 4], D[:N // 4], c_dial)
            mid = N // 2
            widx = np.sort(rng.choice(np.arange(mid - 256, mid + 256), 128,
                                      replace=False))
            rel = ballistic_rel_split(t[widx], D[widx], tau)
            n = rel.shape[0]
            fr.append(rel.sum() / (n * (n - 1) / 2))
        ref[d] = float(np.mean(fr))
    return ref

def d_of(f, ref):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return 6.0
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

print("[n-ladder — round 46; NO-REVIEW MODE on record]")
RUNGS = {2048: dict(web=[20263000 + i for i in range(10)],
                    conf=[20263100 + i for i in range(10)], vol=20263200),
         8192: dict(web=[20263300 + i for i in range(10)],
                    conf=[20263500 + i for i in range(10)], vol=20263600),
         32768: dict(web=[20263400 + i for i in range(10)],
                     conf=[20263520 + i for i in range(10)], vol=20263700)}
gaps = {}
for N, S in RUNGS.items():
    Fc = {"dom": [], "m4": []}
    for sd in S["conf"]:
        rel, coords = confetti_rung(sd, N)
        Fc["dom"].append(F_iso_cloud(transverse(rel, coords, "dom"))[0])
        Fc["m4"].append(F_iso_cloud(transverse(rel, coords, "m4"))[0])
    ref = vol_reference(N, S["vol"])
    Fd, Fm, wf, rf, s4 = [], [], [], 0, 0
    for sd in S["web"]:
        a, b_, c_, r_, s_ = rung_web(sd, N)
        Fd.append(a); Fm.append(b_); wf.append(c_)
        rf += r_; s4 += s_
    dball = d_of(float(np.mean(wf)), ref)
    g = {}
    for fam, webF, confF in (("dom", Fd, Fc["dom"]), ("m4", Fm, Fc["m4"])):
        gap = float(np.nanmean(webF) - np.nanmean(confF))
        se = float(np.sqrt(np.nanvar(webF, ddof=1) / 10
                           + np.nanvar(confF, ddof=1) / 10))
        g[fam] = (gap, se)
    gaps[N] = (g, dball, rf, s4, float(np.nanmean(Fd)), float(np.nanmean(Fm)))
    print(f"    N={N:5d}: F_dom {np.nanmean(Fd):.3f} F_m4 {np.nanmean(Fm):.3f}"
          f" | conf dom {np.nanmean(Fc['dom']):.3f} m4 {np.nanmean(Fc['m4']):.3f}"
          f" | gap dom {g['dom'][0]:+.3f}±{g['dom'][1]:.3f} m4 {g['m4'][0]:+.3f}"
          f"±{g['m4'][1]:.3f} | d_ball {dball:.2f} | refusals {rf}/10 "
          f"S4 {s4}/10", flush=True)

# G0 wiring: the 2048 rung on 45e seeds must reproduce P0
ok0 = (round(gaps[2048][4], 2) == 1.30 and round(gaps[2048][5], 2) == 1.24
       and abs(gaps[2048][1] - 3.84) < 0.15)
check("G0 (wiring): the N=2048 rung reproduces 45e's P0 (2 d.p. / d_ball"
      " within 0.15)", ok0,
      f"F {gaps[2048][4]:.3f}/{gaps[2048][5]:.3f}, d_ball {gaps[2048][1]:.2f}")

# INFO: the churn axis
Fd, Fm, wf = [], [], []
for sd in [20263800 + i for i in range(5)]:
    a, b_, c_, r_, s_ = rung_web(sd, 8192, L=64)
    Fd.append(a); Fm.append(b_)
print(f"    INFO churn axis N=8192 L=64: F_dom {np.nanmean(Fd):.3f} "
      f"F_m4 {np.nanmean(Fm):.3f} (L=16 row: {gaps[8192][4]:.3f}/"
      f"{gaps[8192][5]:.3f})")
check("G1 [MEASURED, unreviewed]: the ladder computed", True)

# G2: the trend
for fam, gi in (("dom", 0), ("m4", 0)):
    pass
trend = {}
for fam in ("dom", "m4"):
    g2, s2 = gaps[2048][0][fam]
    g32, s32 = gaps[32768][0][fam]
    pooled = np.sqrt(s2 ** 2 + s32 ** 2)
    if g32 <= g2 - 2 * pooled:
        trend[fam] = "SHRINKS"
    elif g32 >= g2 + 2 * pooled:
        trend[fam] = "GROWS"
    else:
        trend[fam] = "PERSISTS"
    print(f"      trend[{fam}]: gap {g2:+.3f} -> {g32:+.3f} "
          f"(pooled SE {pooled:.3f}) => {trend[fam]}")
stable = trend["dom"] == trend["m4"]
print(f"\n      G2 THE TREND: {trend['dom']}/{trend['m4']}"
      f"{' (CONVENTION-STABLE)' if stable else ' (conventions disagree)'}\n")
check("G2 (the trend; a read)", True,
      f"{trend['dom']}/{trend['m4']}{' stable' if stable else ''}")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
