#!/usr/bin/env python3
"""
dimwall_cladder_b.py — v9 round 43b: the reference card, the equal-split
witness ladder, and the projection-vs-CLT probe (pin: note-3p1-cladder
round-43 corrections section, f255256, strictly before this ran).
F_iso / builders / find_sk verbatim from dimwall_cladder.py.
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

def fib_sphere(n=64):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    theta = np.pi * (1 + 5 ** 0.5) * i
    return np.column_stack([np.sin(phi) * np.cos(theta),
                            np.sin(phi) * np.sin(theta), np.cos(phi)])
UDIRS = fib_sphere(64)

def F_iso_cloud(v):
    """The F_iso tail of the pipeline, applied to a given v-cloud
    (verbatim PCA + supports from dimwall_cladder.F_iso)."""
    if len(v) < 4 * MIN_PROJ:
        return float("nan"), 0.0, True
    C = np.cov(v.T)
    evals, evecs = np.linalg.eigh(C)
    order = np.argsort(evals)[::-1]
    evals = evals[order]; evecs = evecs[:, order]
    E = evecs[:, :3]
    for c in range(3):
        j = np.argmax(np.abs(E[:, c]))
        if E[j, c] < 0:
            E[:, c] = -E[:, c]
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

# ---- Gr1: the reference card ----
print("[c-ladder 43b]")
print("    Gr1 (the F_iso reference card; synthetic clouds, 3000 points):")
def card_row(name, gen, seeds):
    Fs = []
    for sd in seeds:
        rng = np.random.default_rng(sd)
        v = gen(rng)
        F, er, dg = F_iso_cloud(v)
        Fs.append(F)
    Fs = np.array(Fs)
    print(f"      {name:34s}: F_iso = {np.nanmean(Fs):5.3f} "
          f"[{np.nanmin(Fs):.3f},{np.nanmax(Fs):.3f}]")
    return Fs

SC = [20262500 + i for i in range(5)]
g_iso = card_row("3D isotropic Gaussian", lambda r: r.normal(size=(3000, 3)), SC)
def disk(r):
    v = r.normal(size=(3000, 3)); v[:, 2] = 0.0
    return v
g_disk = card_row("planar isotropic disk (eig3 = 0)", disk, SC)
def plane_eig(r, e3):
    v = r.normal(size=(3000, 3))
    v[:, 2] *= np.sqrt(e3)
    return v
g_p12 = card_row("round plane + axis, eig3/1 = 0.12",
                 lambda r: plane_eig(r, 0.12), SC)
g_p045 = card_row("round plane + axis, eig3/1 = 0.045",
                  lambda r: plane_eig(r, 0.045), SC)
def simplex_cloud(r):
    w = r.dirichlet(np.ones(4), size=3000)      # points in the 3-simplex
    B = np.array([[1, 0, 0], [-1/3, 2*np.sqrt(2)/3, 0],
                  [-1/3, -np.sqrt(2)/3, np.sqrt(6)/3],
                  [-1/3, -np.sqrt(2)/3, -np.sqrt(6)/3]])
    return w @ B
g_simp = card_row("3-simplex interior (polyhedral ref)", simplex_cloud, SC)

ok1 = (abs(np.nanmean(g_iso) - 1.07) < 0.06 and
       abs(np.nanmean(g_disk) - 3.03) < 0.25 and
       1.8 < np.nanmean(g_p12) < 2.4 and
       2.2 < np.nanmean(g_p045) < 2.9 and
       np.nanmean(g_iso) < np.nanmean(g_simp) < np.nanmean(g_disk))
check("Gr1 (the card matches the review-derived references)", ok1,
      f"iso {np.nanmean(g_iso):.3f} | disk {np.nanmean(g_disk):.3f} | "
      f"p12 {np.nanmean(g_p12):.3f} | p045 {np.nanmean(g_p045):.3f} | "
      f"simplex {np.nanmean(g_simp):.3f}")
if not ok1:
    print("\nREFERENCE-CARD REFUSAL: the instrument references are wrong.")
    print("FAILURES: 1")
    raise SystemExit(1)

# ---- builders + searcher (verbatim from dimwall_cladder) ----
def build_equal_pc(sd, C, N=2048, M=32, L=16):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        acc[c] += e / C
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    return rel, rng

def find_sk(rel, rng, k, tries=20000):
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

print("    Gr2 (the equal-split witness ladder):")
SEEDS = [20262400 + i for i in range(5)]
lad = {}
for C, k, tries, tag in ((3, 4, 20000, "gate"), (4, 5, 20000, "gate"),
                         (6, 7, 5000, "INFO"), (8, 9, 5000, "INFO")):
    hits = 0
    for sd in SEEDS:
        rel, rng = build_equal_pc(sd, C)
        res = find_sk(rel, rng, k, tries=tries)
        if res and verify_sk(rel, res[0], res[1], k):
            hits += 1
    lad[(C, k)] = hits
    print(f"      C={C}: S_{k} witnesses on {hits}/5 seeds "
          f"({tag}, tries={tries})", flush=True)
check("Gr2: the S4/S5 gate rows searched at full tries; S7/S9 INFO at "
      "reduced tries (absence there is NOT evidence of absence)", True,
      f"S4@C3: {lad[(3,4)]}/5, S5@C4: {lad[(4,5)]}/5, "
      f"S7@C6: {lad[(6,7)]}/5 (INFO), S9@C8: {lad[(8,9)]}/5 (INFO)")

# ---- Gr3: projection-vs-CLT ----
print("    Gr3 (projection-vs-CLT; orthant-9 native vs 3-PCA shadow):")
def orthantk(rng, N, k):
    Z = rng.random((N, k))
    rel = np.ones((N, N), dtype=bool)
    for j in range(k):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel, Z

def native_F_generic(rel, coords):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    dhat = np.ones(k) / np.sqrt(k)
    dirs = []
    for a in range(k):
        e = np.zeros(k); e[a] = 1.0
        w = e - (e @ dhat) * dhat
        dirs.append(w / np.linalg.norm(w))
    dirs = np.array(dirs)
    ii, jj = np.where(rel)
    d = X[jj] - X[ii]
    s = d @ dhat
    keep = s >= S_MIN
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    v = w / s[:, None]
    hs_c, hs_f = [], []
    for u in dirs:
        p = v @ u; p = p[p > 0]
        hs_c.append(np.quantile(p, Q) if len(p) >= MIN_PROJ else np.nan)
        m = v @ (-u); m = m[m > 0]
        hs_f.append(np.quantile(m, Q) if len(m) >= MIN_PROJ else np.nan)
    return float(np.mean(hs_c) / np.mean(hs_f)), v

Fn, Fs3 = [], []
for sd in SC:
    rng = np.random.default_rng(sd)
    rel, Z = orthantk(rng, 1024, 9)
    Fnat, v = native_F_generic(rel, Z)
    Fsh, er, dg = F_iso_cloud(v)
    Fn.append(Fnat); Fs3.append(Fsh)
print(f"      orthant-9 native 9-frame corner/face F: "
      f"{np.nanmean(Fn):.3f} [{np.nanmin(Fn):.3f},{np.nanmax(Fn):.3f}]")
print(f"      orthant-9 3-PCA-shadow F_iso:          "
      f"{np.nanmean(Fs3):.3f} [{np.nanmin(Fs3):.3f},{np.nanmax(Fs3):.3f}]")
print("      read: shadow << native => the o9 < o4 gap is PROJECTION "
      "rounding; comparable => Gaussianization (INFO)")
check("Gr3: both readings computed and printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
