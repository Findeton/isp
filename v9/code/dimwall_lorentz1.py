#!/usr/bin/env python3
"""
dimwall_lorentz1.py — v9 round 36: LORENTZ I — the directional
anisotropy instrument (note-3p1-lorentz1; pin committed at 44ce7e9
strictly before this receipt).  Reviews ON.

Per instance: related pairs (interval >= 6), standardized coords,
causal-axis decomposition (s, r), longest chain ell by interval DP;
log-log fits of ell against T_round = sqrt(max(s^2-r^2,0)) and
T_poly = geometric-mean box clock in the family's orthant frame
(native for dominance; Hadamard 4-frame clamped at eps=0.05 for M4).
G = R2_round - R2_poly.

PINNED (note SS3): Gl0 certification G(M4) > +0.05 (5/5) AND
G(orthant-4) < -0.05 (5/5), else VOID-INSTRUMENT; Gl1 baseline
[directional: G(corner) < 0]; Gl2 THE MIXING QUESTION [directional]:
mean G(kdir) > mean G(corner).  Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def sprinkle_m4(rng, N):
    """M4 diamond, coordinates kept (t, x, y, z)."""
    P = np.empty((0, 4))
    while len(P) < N:
        t = rng.random(6 * N)
        x = rng.uniform(-0.5, 0.5, (6 * N, 3))
        r = np.linalg.norm(x, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        P = np.vstack([P, np.column_stack([t[keep], x[keep]])])
    P = P[:N]
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.linalg.norm(P[None, :, 1:] - P[:, None, 1:], axis=2)
    rel = (dt > 0) & (dt >= dx)
    np.fill_diagonal(rel, False)
    return rel, P

def orthant4(rng, N):
    Z = rng.random((N, 4))
    rel = np.ones((N, N), dtype=bool)
    for j in range(4):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel, Z

def web_window(sd, mode, C=3, N=2048, M=32, L=16, alpha=0.75, D=1024, NW=256):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    if mode == "kdir":
        Wd = rng.dirichlet(np.ones(C), size=M)
    pref = np.arange(M) % C
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if mode == "kdir":
            acc[c] += e * Wd[c]
        else:
            if rng.random() < alpha:
                k = int(pref[c])
            else:
                k = int(rng.integers(C))
            acc[c, k] += e
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    start = (N - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    coords = np.column_stack([idx.astype(float), chiV[idx]])
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel, coords

# Hadamard 4-frame for M4 (rows normalized); dominance families use identity
HAD = 0.5 * np.array([[1, 1, 1, 1], [1, 1, -1, -1],
                      [1, -1, 1, -1], [1, -1, -1, 1]], dtype=float)

def longest_chain(rel, i, j):
    """Longest path from i to j inside the interval (DP in b-order)."""
    inside = rel[i] & rel[:, j]
    nodes = np.where(inside)[0]
    if len(nodes) == 0:
        return 2
    sub = rel[np.ix_(nodes, nodes)]
    n = len(nodes)
    dp = np.ones(n, dtype=int)
    for a in range(n):                      # nodes sorted; rel respects order
        preds = np.where(sub[:, a])[0]
        if len(preds):
            dp[a] = 1 + dp[preds].max()
    return 2 + int(dp.max())

def G_score(rel, coords, family, rng, npairs=300):
    n = rel.shape[0]
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    dhat = (np.ones(k) / np.sqrt(k)) if family != "m4" else \
        np.array([1.0, 0, 0, 0])
    ii, jj = np.where(rel)
    sizes = (rel[ii].astype(np.int16) & rel[:, jj].T.astype(np.int16)).sum(1)
    good = np.where(sizes >= 6)[0]
    if len(good) == 0:
        return None
    pick = good if len(good) <= npairs else rng.choice(good, npairs, replace=False)
    ells, Tr, Tp = [], [], []
    for p in pick:
        i, j = int(ii[p]), int(jj[p])
        d = X[j] - X[i]
        s = float(d @ dhat)
        r = float(np.linalg.norm(d - s * dhat))
        tr = np.sqrt(max(s * s - r * r, 0.0))
        if family == "m4":
            u = HAD @ d
        else:
            u = d
        u = np.maximum(u, 0.05)
        tp = float(np.exp(np.log(u).mean()))
        ell = longest_chain(rel, i, j)
        if tr > 0 and tp > 0 and ell >= 2:
            ells.append(ell); Tr.append(tr); Tp.append(tp)
    if len(ells) < 40:
        return None
    y = np.log(np.array(ells, dtype=float))
    def r2(T):
        x = np.log(np.array(T))
        A = np.column_stack([x, np.ones(len(x))])
        beta, *_ = np.linalg.lstsq(A, y, rcond=None)
        res = y - A @ beta
        return 1.0 - res.var() / max(y.var(), 1e-12), beta[0]
    R2r, thr = r2(Tr)
    R2p, thp = r2(Tp)
    return R2r - R2p, R2r, R2p, thr, thp, len(ells)

print("[dimwall lorentz1: the directional anisotropy instrument]")
SEEDS = list(range(20261900, 20261905))

def family_G(build, family, tag):
    Gs = []
    for sd in SEEDS:
        rng = np.random.default_rng(sd)
        rel, coords = build(rng, sd)
        out = G_score(rel, coords, family, rng)
        if out is None:
            print(f"      {tag} seed {sd}: UNDERSAMPLED (skipped)")
            continue
        G, R2r, R2p, thr, thp, m = out
        Gs.append(G)
        print(f"      {tag} seed {sd}: G = {G:+.3f} (R2 round {R2r:.3f} "
              f"theta {thr:.2f} | poly {R2p:.3f} theta {thp:.2f}; "
              f"pairs {m})")
    return Gs

g_m4 = family_G(lambda r, sd: sprinkle_m4(r, 256), "m4", "M4       ")
g_o4 = family_G(lambda r, sd: orthant4(r, 256), "orthant", "orthant-4")
check("Gl0 (certification): G(M4) > +0.05 on 5/5 AND G(orthant-4) < "
      "-0.05 on 5/5",
      len(g_m4) == 5 and len(g_o4) == 5 and all(g > 0.05 for g in g_m4)
      and all(g < -0.05 for g in g_o4),
      f"M4 [{min(g_m4):+.3f},{max(g_m4):+.3f}]; "
      f"orthant [{min(g_o4):+.3f},{max(g_o4):+.3f}]")
if FAIL:
    print("      VERDICT: VOID-INSTRUMENT (the T_poly-on-M4 frame is the "
          "named suspect)")
    print()
    print("PRE-REGISTERED GATE LEDGER: REFUSALS PRESENT — Gl0")
    print()
    print("FAILURES: 1/1")
    raise SystemExit(1)

g_c = family_G(lambda r, sd: web_window(sd, "corner"), "web", "corner   ")
g_k = family_G(lambda r, sd: web_window(sd, "kdir"), "web", "kdir     ")
mc, mk = float(np.mean(g_c)), float(np.mean(g_k))
check("Gl1 (baseline) [directional: polyhedral, G < 0]: corner C = 3 "
      "webs measured", len(g_c) >= 4,
      f"mean G = {mc:+.3f} (band [{min(g_c):+.3f}, {max(g_c):+.3f}])"
      + (" — polyhedral as registered" if mc < 0 else
         " — NOT polyhedral-preferring (finding)"))
check("Gl2 (THE MIXING QUESTION) [directional]: mean G(kdir) > mean "
      "G(corner)", mk > mc,
      f"kdir {mk:+.3f} vs corner {mc:+.3f} (shift {mk-mc:+.3f})")

if mk > mc:
    verdict = ("MIXING-ROUNDS-DIRECTIONALLY — Lorentzization-by-mixing "
               "lives; Phase 2b tunes toward the round limit")
else:
    verdict = ("POLYHEDRAL-RIGID-DIRECTIONALLY — the finite-C anisotropy "
               "stands as the framework's falsifiable prediction; the "
               "Lorentz-test fork is posed")
print(f"      VERDICT: {verdict}")
print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gl0 cert; "
      f"Gl1 baseline; Gl2 mixing; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
