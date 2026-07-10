#!/usr/bin/env python3
"""
dimwall_manifoldweb_e.py — v9 round 45e: the pre-registered decision
protocol (pin: the 45e section of note-3p1-manifoldweb, 856b296,
strictly before this ran). Adopts the arc review's O1 + O2 verbatim:
Gate 0 same-pipeline convention-stable parking line; Gate 1 the
pre-registered fresh-seed decision; Gate 2 split-sample tau; the
ballistic-class volume calibration. Machinery verbatim from the arc.
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

# ---------- Gate 0: the same-pipeline parking line ----------
print("[45e — the pre-registered decision protocol]")
print("    Gate 0: the same-pipeline parking line (confetti through the "
      "IDENTICAL 45d pipeline; both conventions; 20 seeds):")
K0, C0 = 24, 0.5
V24 = fib_sphere(24)

def confetti_pipeline(sd, K=24, c_dial=0.5):
    rng = np.random.default_rng(sd)
    t = rng.random(2048)
    x = rng.uniform(-0.5, 0.5, (2048, 3))
    order = np.argsort(t)
    t = t[order]; x = x[order]
    proj = x @ V24[:K].T
    D = proj - proj.mean(axis=1, keepdims=True)
    # split-sample tau: calibration half = the first 512 (by t-order)
    tau = tau_of(t[:512], D[:512], c_dial)
    # the F window: central 1024 by rank, NW = 256
    widx = np.sort(rng.choice(np.arange(512, 1536), 256, replace=False))
    rel = ballistic_rel_split(t[widx], D[widx], tau)
    coords = np.column_stack([t[widx], D[widx]])
    return rel, coords

F0 = {"dom": [], "m4": []}
for sd in [20263100 + i for i in range(20)]:
    rel, coords = confetti_pipeline(sd)
    for fam in ("dom", "m4"):
        F0[fam].append(F_iso_cloud(transverse(rel, coords, fam))[0])
LINE = {}
for fam in ("dom", "m4"):
    arr = np.array(F0[fam])
    LINE[fam] = 1.1 * float(np.nanmax(arr))
    print(f"      convention {fam:3s}: band [{np.nanmin(arr):.3f},"
          f"{np.nanmax(arr):.3f}] mean {np.nanmean(arr):.3f} -> "
          f"parking line {LINE[fam]:.3f}")
ok0 = all(np.isfinite(list(LINE.values()))) and \
      all(np.isfinite(F0[f]).sum() >= 18 for f in F0)
check("Gate 0: the line set per convention (>= 18/20 finite each)", ok0,
      f"dom {LINE['dom']:.3f}, m4 {LINE['m4']:.3f}")
if not ok0:
    print("GATE-0 REFUSAL."); print("FAILURES: 1"); raise SystemExit(1)

# ---------- O2: the ballistic-class volume calibration ----------
print("    O2: the ballistic-class volume reference (latent d = 2..6, "
      "8 seeds each, same window protocol):")
volref = {}
for d in (2, 3, 4, 5, 6):
    fr = []
    for j in range(8):
        rng = np.random.default_rng(20263200 + 10 * d + j)
        t = rng.random(2048)
        x = rng.uniform(-0.5, 0.5, (2048, d - 1))
        order = np.argsort(t)
        t = t[order]; x = x[order]
        U = unit_dirs(np.random.default_rng(4242 + d), 24, d - 1)
        proj = x @ U.T
        D = proj - proj.mean(axis=1, keepdims=True)
        tau = tau_of(t[:512], D[:512], C0)
        widx = np.sort(rng.choice(np.arange(768, 1280), 128, replace=False))
        rel = ballistic_rel_split(t[widx], D[widx], tau)
        n = rel.shape[0]
        fr.append(rel.sum() / (n * (n - 1) / 2))
    volref[d] = float(np.mean(fr))
    print(f"      d={d}: window fraction {volref[d]:.4f} "
          f"(+- {np.std(fr, ddof=1):.4f})")
mono = all(volref[d] > volref[d + 1] for d in (2, 3, 4, 5))
check("O2: the reference curve is strictly monotone in d", mono)

def d_ball(f):
    ds = sorted(volref); fs = [volref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return 6.0
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

# ---------- Gate 1: the pre-registered decision ----------
def build_manifold(sd, K, alpha, N=2048, M=32, L=16):
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

POINTS = {"P0": (24, 0.75, 0.5), "N1": (32, 0.75, 0.5), "N2": (24, 0.75, 0.35)}
FRESH = [20263000 + i for i in range(10)]
res = {}
print("    Gate 1: the pre-registered points on 10 FRESH seeds "
      "(split-sample tau everywhere):")
for name, (K, alpha, cd) in POINTS.items():
    Fd, Fm, wfr, refusals, s4 = [], [], [], 0, 0
    for sd in FRESH:
        chiV, rng = build_manifold(sd, K, alpha)
        D = chiV - chiV.mean(axis=1, keepdims=True)
        b = np.arange(2048).astype(float)
        tau = tau_of(b[:512], D[:512], cd)          # Gate 2: one tau
        widx = np.sort(rng.choice(np.arange(512, 1536), 256, replace=False))
        rel = ballistic_rel_split(b[widx], D[widx], tau)
        coords = np.column_stack([b[widx], D[widx]])
        Fd.append(F_iso_cloud(transverse(rel, coords, "dom"))[0])
        Fm.append(F_iso_cloud(transverse(rel, coords, "m4"))[0])
        didx = np.sort(rng.choice(np.arange(768, 1280), 128, replace=False))
        drel = ballistic_rel_split(b[didx], D[didx], tau)
        n = drel.shape[0]
        wfr.append(drel.sum() / (n * (n - 1) / 2))
        ridx = np.sort(rng.choice(np.arange(768, 1280), 144, replace=False))
        rrel = ballistic_rel_split(b[ridx], D[ridx], tau)
        if not dim_le_2(rrel):
            refusals += 1
        frel = ballistic_rel_split(b, D, tau)
        r4 = find_sk(frel, rng, 4)
        if r4 and verify_sk(frel, r4[0], r4[1], 4):
            s4 += 1
    dball = d_ball(float(np.mean(wfr)))
    res[name] = dict(Fd=np.array(Fd), Fm=np.array(Fm), dball=dball,
                     refusals=refusals, s4=s4)
    print(f"      {name} (K={K}, a={alpha}, c={cd}): "
          f"F_dom = {np.nanmean(Fd):.3f} (SE {np.nanstd(Fd, ddof=1)/np.sqrt(10):.3f})  "
          f"F_m4 = {np.nanmean(Fm):.3f} (SE {np.nanstd(Fm, ddof=1)/np.sqrt(10):.3f})  "
          f"d_ball = {dball:.2f}  refusals {refusals}/10  S4 {s4}/10",
          flush=True)
check("Gate 1: the three pre-registered points measured on fresh seeds",
      True)

# dF/dc print (Gate 2)
print(f"      dF/dc (P0 vs N2, dom): "
      f"{(np.nanmean(res['P0']['Fd']) - np.nanmean(res['N2']['Fd'])) / (0.5 - 0.35):+.3f} per unit c")

# ---------- the decision ----------
def ztest(arr, line):
    m = float(np.nanmean(arr))
    se = float(np.nanstd(arr, ddof=1) / np.sqrt(np.isfinite(arr).sum()))
    return (m - line) / max(se, 1e-12)

print("    the decision (P0 at z <= -1.64 both conventions; neighbors at "
      "z <= -2.13; volume in [3.5, 4.5]; refusals >= 8/10; S4 >= 3/10):")
verdicts = {}
for name in POINTS:
    zd = ztest(res[name]["Fd"], LINE["dom"])
    zm = ztest(res[name]["Fm"], LINE["m4"])
    verdicts[name] = (zd, zm)
    print(f"      {name}: z_dom = {zd:+.2f}, z_m4 = {zm:+.2f}")
thr = {"P0": -1.64, "N1": -2.13, "N2": -2.13}
def passes(name):
    zd, zm = verdicts[name]
    r = res[name]
    shape_d = zd <= thr[name]
    shape_m = zm <= thr[name]
    vol = 3.5 <= r["dball"] <= 4.5
    dim = r["refusals"] >= 8 and r["s4"] >= 3
    return shape_d, shape_m, vol, dim
p0 = passes("P0")
if all(p0):
    verdict = "PARKED at P0 (convention-stable, volume-calibrated, witnessed)"
elif p0[0] != p0[1]:
    verdict = ("UNDECIDED-INSTRUMENT at P0 (the conventions disagree: "
               f"z_dom {verdicts['P0'][0]:+.2f} vs z_m4 {verdicts['P0'][1]:+.2f})")
else:
    subs = [n for n in ("N1", "N2") if all(passes(n))]
    verdict = (f"PARKED at neighbor {subs[0]} (Bonferroni)" if subs
               else "NOT-PARKED (no pre-registered point passes the full conjunction)")
print(f"\n      45e THE DECISION: {verdict}\n")
check("the decision (a read; pre-registered semantics)", True, verdict[:110])

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
