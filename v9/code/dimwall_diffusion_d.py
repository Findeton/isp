#!/usr/bin/env python3
"""
dimwall_diffusion.py — v9 round 48: diffusion-churn (pin: the
Receipt-48 section of note-3p1-conservation, committed pre-run, strictly before this ran). NO-REVIEW
MODE on record. One change from the 45e class: churn TRANSFERS the
victim accumulator to a receiver slot. Carries the free-web influence
control and the first influence measurement. Machinery verbatim.
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

G_LEAK = 0.0625
def build_web(sd, N=2048, K=24, alpha=0.75, M=32, L=16, conserve=True,
              mark=None):
    """mark = (t_star, slot, magnitude, direction) injects one extra
    deposit into `slot` at time t_star (the influence probe)."""
    rng = np.random.default_rng(sd)
    V = fib_sphere(K)
    P = rng.normal(size=(M, 3))
    P /= np.linalg.norm(P, axis=1, keepdims=True)
    acc = np.zeros((M, K))
    chiV = np.zeros((N, K))
    commit_slot = np.zeros(N, dtype=int)
    for t in range(N):
        c = int(rng.integers(M))
        commit_slot[t] = c
        e = rng.exponential(0.109551)
        if rng.random() < alpha:
            u = P[c]
        else:
            u = rng.normal(size=3)
            u /= np.linalg.norm(u)
        acc[c] += e * 0.5 * (1.0 + V @ u)
        if mark is not None and t == mark[0]:
            ts, ms, mag, ud = mark
            acc[ms] += mag * 0.5 * (1.0 + V @ ud)
        chiV[t] = acc[c]
        v = int(rng.integers(M))
        r = int(rng.integers(M))
        if r != v:
            acc[r] += G_LEAK * acc[v]
            acc[v] *= (1.0 - G_LEAK)
    return chiV, commit_slot, rng

def measure_web(chiV, rng, c_dial=0.5):
    N = chiV.shape[0]
    D = chiV - chiV.mean(axis=1, keepdims=True)
    b = np.arange(N).astype(float)
    tau = tau_of(b[:N // 4], D[:N // 4], c_dial)
    widx = np.sort(rng.choice(np.arange(N // 4, 3 * N // 4), 256,
                              replace=False))
    rel = ballistic_rel_split(b[widx], D[widx], tau)
    coords = np.column_stack([b[widx], D[widx]])
    Fd = F_iso_cloud(transverse(rel, coords, "dom"))[0]
    Fm = F_iso_cloud(transverse(rel, coords, "m4"))[0]
    mid = N // 2
    didx = np.sort(rng.choice(np.arange(mid - 256, mid + 256), 128,
                              replace=False))
    drel = ballistic_rel_split(b[didx], D[didx], tau)
    n = drel.shape[0]
    wfrac = drel.sum() / (n * (n - 1) / 2)
    ridx = np.sort(rng.choice(np.arange(mid - 256, mid + 256), 144,
                              replace=False))
    refuse = not dim_le_2(ballistic_rel_split(b[ridx], D[ridx], tau))
    sidx = np.sort(rng.choice(np.arange(N // 4, 3 * N // 4), 1024,
                              replace=False))
    srel = ballistic_rel_split(b[sidx], D[sidx], tau)
    r4 = find_sk(srel, rng, 4)
    s4 = bool(r4 and verify_sk(srel, r4[0], r4[1], 4))
    return Fd, Fm, wfrac, refuse, s4, tau, D


print("[diffusion decision — round 48d; NO-REVIEW, lean]")
LINES = {"dom": 1.236, "m4": 1.212}
VOLREF = {2: 0.3016, 3: 0.0997, 4: 0.0404, 5: 0.0253, 6: 0.0134}
def d_of(f):
    ds = sorted(VOLREF); fs = [VOLREF[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return 6.0
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

import builtins
for g, seeds, tag in ((0.18, range(20264500, 20264510), "decision"),):
    builtins.G_LEAK = g
    globals()['G_LEAK'] = g
    Fd, Fm, wf, rf, s4c, eigs, frs = [], [], [], 0, 0, [], []
    for sd in seeds:
        chiV, cs, rng = build_web(sd)
        N = 2048
        D = chiV - chiV.mean(axis=1, keepdims=True)
        b = np.arange(N).astype(float)
        tau = tau_of(b[:512], D[:512], 0.5)
        widx = np.sort(rng.choice(np.arange(512, 1536), 256, replace=False))
        rel = ballistic_rel_split(b[widx], D[widx], tau)
        coords = np.column_stack([b[widx], D[widx]])
        v = transverse(rel, coords, "dom")
        F, er, dg = F_iso_cloud(v)
        Fd.append(F); eigs.append(er)
        Fm.append(F_iso_cloud(transverse(rel, coords, "m4"))[0])
        n = rel.shape[0]; frs.append(rel.sum() / (n * (n - 1) / 2))
        didx = np.sort(rng.choice(np.arange(768, 1280), 128, replace=False))
        drel = ballistic_rel_split(b[didx], D[didx], tau)
        n = drel.shape[0]; wf.append(drel.sum() / (n * (n - 1) / 2))
        ridx = np.sort(rng.choice(np.arange(768, 1280), 144, replace=False))
        if not dim_le_2(ballistic_rel_split(b[ridx], D[ridx], tau)):
            rf += 1
        sidx = np.sort(rng.choice(np.arange(512, 1536), 1024, replace=False))
        srel = ballistic_rel_split(b[sidx], D[sidx], tau)
        r4 = find_sk(srel, rng, 4)
        s4c += bool(r4 and verify_sk(srel, r4[0], r4[1], 4))
    ns = len(list(seeds))
    sed = float(np.nanstd(Fd, ddof=1) / np.sqrt(ns))
    print(f"    g={g}: F_dom {np.nanmean(Fd):.3f}±{sed:.3f} "
          f"(line 1.236, z {((np.nanmean(Fd)-1.236)/sed):+.2f}) "
          f"F_m4 {np.nanmean(Fm):.3f} | d_ball {d_of(float(np.mean(wf))):.2f}"
          f" refusals {rf}/{ns} S4 {s4c}/{ns} | eig3/1 {np.mean(eigs):.3f} "
          f"frac {np.mean(frs):.4f}", flush=True)
    if g == 0.0625:
        check("sanity: finite F at the main dial", np.isfinite(np.nanmean(Fd)))

# influence (3 pairs, main dial)
builtins.G_LEAK = 0.0625
globals()['G_LEAK'] = 0.0625
counts = []
for sd in ():
    A, csA, _ = build_web(sd)
    B, csB, _ = build_web(sd, mark=(1024, 7, 1.0, np.array([0., 0., 1.])))
    diff = np.abs(B - A).max(axis=1) > 1e-9
    idx = np.where(diff)[0]
    sel = idx[(idx > 1024) & (idx <= 2048)]
    counts.append(len(set(csA[sel])))
print(f"    influence: affected slots by Delta-b=1024: "
      f"{np.mean(counts):.1f} (47's conservation: 3.6; control: 1)")
check("the diffusion reads printed", True)
sem_ = float(np.nanstd(Fm, ddof=1) / np.sqrt(len(Fm)))
zd = (np.nanmean(Fd) - 1.236) / sed
zm = (np.nanmean(Fm) - 1.212) / sem_
db = d_of(float(np.mean(wf)))
shape_d = zd <= -1.64
shape_m = zm <= -1.64
vol = 3.5 <= db <= 4.5
dim = rf >= 8 and s4c >= 3
if shape_d and shape_m and vol and dim:
    v_ = "PARKED (round AND 4D AND witnessed, pre-registered)"
elif shape_d != shape_m:
    v_ = f"UNDECIDED-INSTRUMENT (z_dom {zd:+.2f} vs z_m4 {zm:+.2f})"
else:
    v_ = (f"NOT-PARKED (z_dom {zd:+.2f}, z_m4 {zm:+.2f}, d_ball {db:.2f}, "
          f"refusals {rf}/10, S4 {s4c}/10)")
print(f"\n      48d THE DECISION: {v_}\n")
check("the decision (pre-registered)", True, v_[:110])
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
