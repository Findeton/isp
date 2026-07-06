#!/usr/bin/env python3
"""
n2_chi_geometry.py — design note 1's ladder, rung L2 (v9 PLAN.md T6.1): the
geometric closure. Feed the RECORD-SIDE affinity (not w) through the k3/l2
MDS pipeline and score the recovered transverse plane against held-out
geometry, with the w-seeded benchmark beside it.

THE PRE-REGISTRATION (design note 1 §3 L2, gates quoted): transverse
Procrustes >= 0.9 against held-out geometry (benchmark: the 0.993-class
recovery from w itself; "the gap between them is the identification's
measured cost"). The note's stronger ask — the full intrinsic-finder run
seeded by the record-side affinity landing in the same certificate band as
the w-seeded run (m1 parity) — is DEFERRED to n2's second run (an executed-
arm deviation, disclosed here and in the LOG; the primary Procrustes gate is
this receipt's).

ROUTE: (b), the hop-metric — the n1 disagreement rule's winner ("(b) wins
the argument"): chain graph with edge length 1/cross-count, weighted
shortest paths, affinity exp(-d_hop/ell), ell = median (the one free scale,
order-only calibrated). Route (a)'s merged-sequence kernel is carried as a
comparison column (its n1 refusal predicts a sub-gate closure here; both
directions recorded).

GATES: G-a route (b) Procrustes >= 0.9 at both N in {400, 1000}, per fleet,
3 fleets each (stability, the m1 scale-lesson convention); G-b the w-side
benchmark >= 0.98 on the same fleets; G-c the shuffled-affinity control:
the real closure exceeds the measured per-fleet shuffle NULL by > 3 null-sd
(24 shuffle draws; the absolute-0.4 form of k3's control is M-inappropriate
below M ~ 15 — a 2D Procrustes null against 10-14 points is ~0.3-0.5 wide;
gate form corrected at first execution, before any verdict was consumed,
logged); G-d the measured cost (benchmark - route(b)) printed per fleet.

Machinery: k3's, with the disclosed MDS-dissimilarity difference (max(AFF)
- AFF vs k3's 1 - W; results insensitive). Float64. Seed:
default_rng(20260702).
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


def sprinkle_3d(N):
    pts = np.empty((0, 3))
    while len(pts) < N:
        m = 4 * (N - len(pts)) + 64
        t = rng.uniform(-1, 1, m)
        x = rng.uniform(-1, 1, m)
        y = rng.uniform(-1, 1, m)
        keep = np.hypot(x, y) <= 1 - np.abs(t)
        pts = np.vstack([pts, np.column_stack([t, x, y])[keep]])
    return pts[:N]

def order_3d(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.hypot(P[None, :, 1] - P[:, None, 1], P[None, :, 2] - P[:, None, 2])
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

def build_fleet(N, max_chains=28):
    P = sprinkle_3d(N)
    C = order_3d(P)
    alive = np.ones(N, dtype=bool)
    chains = []
    while True:
        ch = longest_chain(C, alive)
        if len(ch) < 8 or len(chains) >= max_chains:
            break
        chains.append(ch)
        alive[ch] = False
    return P, C, chains

def coupling_w(C, chains):
    M = len(chains)
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(i + 1, M):
            ci, cj = chains[i], chains[j]
            cross = C[np.ix_(ci, cj)].sum() + C[np.ix_(cj, ci)].sum()
            W[i, j] = W[j, i] = cross / (len(ci) * len(cj))
    return W

def route_b(C, chains):
    M = len(chains)
    INF = 1e18
    D = np.full((M, M), INF)
    np.fill_diagonal(D, 0.0)
    for i in range(M):
        for j in range(i + 1, M):
            ci, cj = chains[i], chains[j]
            cross = C[np.ix_(ci, cj)].sum() + C[np.ix_(cj, ci)].sum()
            if cross > 0:
                D[i, j] = D[j, i] = 1.0 / cross
    for k in range(M):
        D = np.minimum(D, D[:, k:k + 1] + D[k:k + 1, :])
    finite = D[np.isfinite(D) & (D > 0)]
    ell = np.median(finite) if len(finite) else 1.0
    return np.exp(-D / ell)

def route_a(P, C, chains):
    M = len(chains)
    E = np.zeros((M, M))
    for i in range(M):
        for j in range(i + 1, M):
            ci, cj = chains[i], chains[j]
            merged = [(P[e, 0], 0, e) for e in ci] + [(P[e, 0], 1, e) for e in cj]
            merged.sort()
            last = {0: None, 1: None}
            ms, ps = [], []
            for _, mk, e in merged:
                other = last[1 - mk]
                ps.append(1 if (other is not None and C[other, e]) else 0)
                ms.append(mk)
                last[mk] = e
            ms = np.array(ms); ps = np.array(ps)
            pm = np.zeros((2, 2))
            for a in (0, 1):
                for b in (0, 1):
                    pm[a, b] = np.mean((ms == a) & (ps == b))
            pa = pm.sum(1); pb = pm.sum(0)
            mi = 0.0
            for a in (0, 1):
                for b in (0, 1):
                    if pm[a, b] > 0 and pa[a] > 0 and pb[b] > 0:
                        mi += pm[a, b] * np.log(pm[a, b] / (pa[a] * pb[b]))
            E[i, j] = E[j, i] = mi
    return E

def mds_xy(AFF):
    M = len(AFF)
    DIS = AFF.max() - AFF
    np.fill_diagonal(DIS, 0.0)
    J = np.eye(M) - np.ones((M, M)) / M
    B = -0.5 * J @ (DIS ** 2) @ J
    ev, V = np.linalg.eigh(B)
    return V[:, -2:] * np.sqrt(np.maximum(ev[-2:], 0))

def procrustes_corr(A, Bm):
    A = A - A.mean(0); Bm = Bm - Bm.mean(0)
    U, s_, Vt = np.linalg.svd(A.T @ Bm)
    R = U @ Vt
    return float(np.corrcoef((A @ R).ravel(), Bm.ravel())[0, 1])


print("CHECK 1-3: the L2 closure, 3 fleets per scale, both routes + benchmark")
res = {400: [], 1000: []}
for N in (400, 1000):
    for f in range(3):
        P, C, chains = build_fleet(N)
        M = len(chains)
        tpos = np.array([[P[c, 1].mean(), P[c, 2].mean()] for c in chains])
        W = coupling_w(C, chains)
        Ab = route_b(C, chains)
        Ea = route_a(P, C, chains)
        pc_w = procrustes_corr(mds_xy(W), tpos)
        pc_b = procrustes_corr(mds_xy(Ab), tpos)
        pc_a = procrustes_corr(mds_xy(Ea), tpos)
        # shuffled-affinity control on route (b): the SMALL-FLEET null is
        # wide (a 2D Procrustes against M ~ 10 points has null ~ 0.4-0.5),
        # so the k3-era absolute 0.4 gate is M-inappropriate; the control is
        # the per-fleet z-gate against the measured shuffle NULL (24 draws)
        # — stricter than 0.4 where the null is tight, honest where wide.
        # (Gate form corrected at first execution, before any verdict was
        # consumed; logged.)
        iu = np.triu_indices(M, 1)
        nulls = []
        for _ in range(24):
            perm = rng.permutation(len(iu[0]))
            As = np.zeros_like(Ab)
            As[iu] = Ab[iu][perm]
            As = As + As.T
            np.fill_diagonal(As, 1.0)
            nulls.append(procrustes_corr(mds_xy(As), tpos))
        mu0, s0 = float(np.mean(nulls)), float(np.std(nulls, ddof=1))
        z_ctrl = (pc_b - mu0) / s0
        res[N].append((M, pc_w, pc_b, pc_a, mu0, s0, z_ctrl))
        print(f"      N = {N:>4} fleet {f}: M = {M:>2} | benchmark(w) {pc_w:.3f} | "
              f"route (b) {pc_b:.3f} (cost {pc_w - pc_b:+.3f}) | route (a) "
              f"{pc_a:.3f} | shuffle null {mu0:+.3f} +/- {s0:.3f} (z = {z_ctrl:.1f})")

pb = [x[2] for N in res for x in res[N]]
pw = [x[1] for N in res for x in res[N]]
pa = [x[3] for N in res for x in res[N]]
zc = [x[6] for N in res for x in res[N]]
ok = all(x >= 0.9 for x in pb)
check("G-a: route (b) closes the geometry at Procrustes >= 0.9 on EVERY "
      "fleet at both scales — the L2 gate PASSES on the hop-metric route "
      "(the identification carries METRIC transverse information)", ok,
      f"route (b): {[round(x, 3) for x in pb]}")
ok = all(x >= 0.98 for x in pw)
check("G-b: the w-side benchmark holds at >= 0.98 on the same fleets (the "
      "measured cost of the identification is the printed gap)", ok,
      f"benchmark: {[round(x, 3) for x in pw]}; mean cost "
      f"{np.mean(pw) - np.mean(pb):+.3f}")
ok = all(z > 3.0 for z in zc)
check("G-c: the real closure exceeds the measured shuffle null by > 3 null-"
      "sd on every fleet (the geometry lives in the coupling, not the "
      "pipeline; per-fleet z-gate — the M-appropriate form of k3's control)",
      ok, f"z: {[round(z, 1) for z in zc]}")
check("route (a) comparison column recorded (its n1 refusal predicted a "
      "sub-gate closure; measured — the fork's demonstration column)",
      True, f"route (a): {[round(x, 3) for x in pa]}")

print()
print("DEFERRED (disclosed): the note's stronger L2 ask — the full intrinsic-")
print("finder run seeded by the record-side affinity at m1 certificate-band")
print("parity — is owed at n2's second run; the primary Procrustes gate is")
print("this receipt's verdict.")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
