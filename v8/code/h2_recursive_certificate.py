#!/usr/bin/env python3
"""
h2_recursive_certificate.py — v8 paper 11 §4–§5: the heredity (recursive-interval)
certificate axis, and a Metropolis drift toy under the misfit action.

HEREDITY (paper 11 Thm 2.1): every order interval of a faithfully embedded order
is itself faithful — so manifoldlikeness can be tested INSIDE intervals,
recursively. Axis implemented: for the largest intervals (interior >= 24),
score the internal ordering fraction r_I against 1/2 and the internal height
against the 2 sqrt(k) law; recurse one level into each interval's own largest
sub-interval. Populations: geometric / KR / KR+spine (paper 7's designed
adversary) / a CLUSTER adversary (tight c-point jittered clusters on geometric
centers — a blow-up order, the v7-linear-jitter class's cousin). Honest-report
discipline: whatever each axis catches or misses is printed and asserted as
measured; an adversary surviving an axis is a FINDING, not a failure to hide.

DRIFT TOY (paper 11 §5): Metropolis-style local search on labeled posets at
n = 28 under e^{-beta S_misfit} (m0 = 6 at this size, disclosed), beta = 15 >
beta* ~ 11 (h1 CHECK 4). Moves: add a random non-cycle relation (+ transitive
closure) or remove a random COVER (keeps transitivity). This is a DRIVEN LOCAL
SEARCH, not an exact MCMC sampler (the closure step breaks proposal symmetry —
disclosed); the demonstration is DRIFT of the action and of the internal
statistics away from the KR start, against a beta = 0 control. n = 28 is a toy:
no convergence or mixing claim is made.

Float discipline: measurement landscape float64. Seed: default_rng(20260702).
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


# ------------------------------------------------------------ populations
def sprinkle_2d(N):
    uv = rng.random((N, 2))
    return (uv[None, :, 0] > uv[:, None, 0]) & (uv[None, :, 1] > uv[:, None, 1])

def kr_3layer(N, p=0.5):
    n1, n2 = N // 4, N // 2
    n3 = N - n1 - n2
    C = np.zeros((N, N), dtype=bool)
    L1 = np.arange(0, n1); L2 = np.arange(n1, n1 + n2); L3 = np.arange(n1 + n2, N)
    C[np.ix_(L1, L2)] = rng.random((n1, n2)) < p
    C[np.ix_(L2, L3)] = rng.random((n2, n3)) < p
    C[np.ix_(L1, L3)] = (C[np.ix_(L1, L2)].astype(np.float32)
                         @ C[np.ix_(L2, L3)].astype(np.float32)) > 0
    return C

def kr_with_spine(N, p, spine_len):
    m = int(spine_len)
    Nk = N - m
    C = np.zeros((N, N), dtype=bool)
    C[:Nk, :Nk] = kr_3layer(Nk, p)
    for i in range(Nk, N):
        C[i, i + 1:N] = True
    return C

def cluster_adversary(N, c=6, jit=1e-3):
    """Blow-up order: N/c geometric centers, c tightly-jittered points each."""
    M = N // c
    ctr = rng.random((M, 2))
    pts = np.repeat(ctr, c, axis=0) + rng.normal(0, jit, (M * c, 2))
    C = (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])
    return C

# ------------------------------------------------------------ internal axes
def height_of(C):
    N = C.shape[0]
    indeg = C.sum(axis=0).astype(int)
    stack = [i for i in range(N) if indeg[i] == 0]
    Clist = [np.nonzero(C[i])[0] for i in range(N)]
    L = np.ones(N, dtype=int)
    topo = []
    while stack:
        v = stack.pop()
        topo.append(v)
        for w in Clist[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    for v in topo:
        succ = Clist[v]
        if len(succ):
            L[succ] = np.maximum(L[succ], L[v] + 1)
    return int(L.max())

def interval_pass(sub):
    """Internal axes on one interval interior: r_I near 1/2, height near 2 sqrt(k).
    Bands (disclosed): |r - 1/2| <= 0.15; H/(2 sqrt k) in (0.55, 1.35) — wide,
    calibrated to accept geometric interiors at k ~ 24-200 incl. BDJ deficit."""
    k = sub.shape[0]
    if k < 2:
        return False, 0.0, 0.0
    r = 2.0 * sub.sum() / (k * (k - 1))
    hr = height_of(sub) / (2.0 * np.sqrt(k))
    return (abs(r - 0.5) <= 0.15) and (0.55 < hr < 1.35), r, hr

def top_intervals(C, kmin=24, top=6):
    Cf = C.astype(np.float32)
    between = np.rint(Cf @ Cf).astype(np.int32)
    sizes = np.where(C, between, -1)
    flat = np.argsort(sizes, axis=None)[::-1]
    out = []
    for f in flat[:top * 4]:
        x, y = np.unravel_index(f, sizes.shape)
        if sizes[x, y] < kmin:
            break
        inner = np.nonzero(C[x] & C[:, y])[0]
        out.append(C[np.ix_(inner, inner)])
        if len(out) >= top:
            break
    return out

def recursive_axis(C, kmin=24):
    """Level-1: top intervals pass rate; level-2: each interval's own largest
    sub-interval (kmin/2). Returns (pass1, pass2, n1, n2)."""
    ivs = top_intervals(C, kmin=kmin)
    if not ivs:
        return 0.0, 0.0, 0, 0
    p1 = [interval_pass(s)[0] for s in ivs]
    subs = []
    for s in ivs:
        subs.extend(top_intervals(s, kmin=kmin // 2, top=1))
    p2 = [interval_pass(s)[0] for s in subs]
    return (float(np.mean(p1)), float(np.mean(p2)) if p2 else 0.0,
            len(p1), len(p2))

# --------------------------------------- CHECK 1-3: the four populations
print("CHECK 1-3: the heredity axis on the four populations (N = 384, 5 seeds)")
NP_ = 384
res = {}
for name, gen in (("geometric", lambda: sprinkle_2d(NP_)),
                  ("KR", lambda: kr_3layer(NP_)),
                  ("KR+spine", lambda: kr_with_spine(NP_, 0.90, 39)),
                  ("cluster", lambda: cluster_adversary(NP_, c=6))):
    p1s, p2s = [], []
    for _ in range(5):
        p1, p2, n1, n2 = recursive_axis(gen())
        p1s.append(p1); p2s.append(p2)
    res[name] = (float(np.mean(p1s)), float(np.mean(p2s)))
    print(f"      {name:<10}  level-1 pass {res[name][0]:5.0%}   "
          f"level-2 pass {res[name][1]:5.0%}")
ok = res["geometric"][0] >= 0.8 and res["geometric"][1] >= 0.6
check("geometric interiors pass at both levels (>= 80% / >= 60%)", ok,
      f"{res['geometric'][0]:.0%} / {res['geometric'][1]:.0%}")
ok = res["KR"][0] <= 0.1 and res["KR+spine"][0] <= 0.2
check("KR and KR+spine interiors FAIL level-1 (antichain/chain intervals; "
      "the global-axis-fooling adversary is caught INSIDE its intervals)", ok,
      f"{res['KR'][0]:.0%} / {res['KR+spine'][0]:.0%}")
# the cluster adversary: the FINDING asserted as measured (was a hardcoded-True
# report pre-review; now the check pins §4's claim — if a future change catches
# the cluster class, this check fails and flags the paper's survival claim stale)
ok = res["cluster"][0] >= 0.5 and res["cluster"][1] >= 0.5
check("cluster adversary SURVIVES the r/height heredity axes at these sizes "
      "(>= 50% pass both levels) — the honest §4 finding: blow-up orders need "
      "the abundance-profile internal axis (named next axis; frontier)", ok,
      f"level-1 {res['cluster'][0]:.0%}, level-2 {res['cluster'][1]:.0%}")

# --------------------------------------- CHECK 4-6: the Metropolis drift toy
print("CHECK 4-6: drift toy at n = 28 under e^{-beta S}, beta = 15 vs 0")
M0_TOY = 6

def misfit_toy(C):
    N = C.shape[0]
    Cf = C.astype(np.float32)
    between = np.rint(Cf @ Cf).astype(np.int32)
    S = 0.0
    ii, jj = np.nonzero(C & (between >= M0_TOY))
    for x, y in zip(ii, jj):
        inner = np.nonzero(C[x] & C[:, y])[0]
        k = len(inner)
        sub = C[np.ix_(inner, inner)]
        r = 2.0 * sub.sum() / (k * (k - 1)) if k > 1 else 0.0
        S += (r - 0.5) ** 2
    return S

def closure(C):
    Cf = C.astype(np.float32)
    R = Cf.copy()
    for _ in range(6):                    # n = 28: log2 depth ample
        R = np.minimum(R + R @ R, 1.0)
    return R > 0.5

def covers(C):
    Cf = C.astype(np.float32)
    two = (Cf @ Cf) > 0.5
    return C & ~two

def drift_run(beta, steps, seed_C):
    C = seed_C.copy()
    S = misfit_toy(C)
    n = C.shape[0]
    for _ in range(steps):
        i, j = rng.integers(0, n, 2)
        if i == j:
            continue
        Cn = None
        if C[i, j]:
            cov = covers(C)
            if cov[i, j]:
                Cn = C.copy(); Cn[i, j] = False
        else:
            if not C[j, i]:
                Cn = C.copy(); Cn[i, j] = True
                Cn = closure(Cn)
        if Cn is None:
            continue
        Sn = misfit_toy(Cn)
        if Sn <= S or rng.random() < np.exp(-beta * (Sn - S)):
            C, S = Cn, Sn
    return C, S

n_toy = 28
seed_C = kr_3layer(n_toy, p=0.90)
S0 = misfit_toy(seed_C)
r0 = None
iv0 = top_intervals(seed_C, kmin=M0_TOY, top=1)
if iv0:
    _, r0, _ = interval_pass(iv0[0])
C_hot, S_hot = drift_run(15.0, 4000, seed_C)
C_ctl, S_ctl = drift_run(0.0, 4000, seed_C)
print(f"      start: S = {S0:.3f};  beta=15: S = {S_hot:.3f};  "
      f"beta=0 control: S = {S_ctl:.3f}")
ok = S_hot < 0.3 * S0
check("beta = 15 drift: the action falls below 0.3x the KR start within 4k steps "
      "(driven local search, NOT an equilibrium sampler — disclosed)", ok,
      f"{S0:.2f} -> {S_hot:.2f}")
ok = S_ctl > 0.5 * S0 or S_ctl > 3 * max(S_hot, 1e-9)
check("beta = 0 control stays high (the drift is the action's, not the move set's)",
      ok, f"control S = {S_ctl:.2f}")
iv1 = top_intervals(C_hot, kmin=M0_TOY, top=1)
if iv0 and iv1:
    _, r_end, _ = interval_pass(iv1[0])
    ok = abs(r_end - 0.5) < abs(r0 - 0.5)
    check("the largest interval's internal r moves TOWARD 1/2 from the KR "
          "antichain start (toy-scale direction, no convergence claim)", ok,
          f"r: {r0:.3f} -> {r_end:.3f}")
else:
    check("largest-interval r drift measurable", False, "no qualifying interval")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
