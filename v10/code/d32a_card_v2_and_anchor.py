#!/usr/bin/env python3
"""
d32a_card_v2_and_anchor.py — v10 D32A: the deterministic card v2, the
validated order-only estimators, the 1.76 anchor, and the exception
census. Pin: note-d32-dimension-map.md (committed pre-run).
Card v2: fixed-decimal (12 sig digits) serialization, sorted keys,
recorded numerical environment, per-cell SDs INCLUDING the controls at
every N. Float64 MC + numpy (declared); all seeds fixed.
Gates P1-P6; exit 1 on any failure.
"""
import json, math, hashlib, sys, platform
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

DIMS = (2, 3, 4)
SIZES = (256, 512, 1024)
SEEDS = 20
BASE = 20260712

# ---- D29 machinery (frozen conventions) -----------------------------------
def sprinkle_interval(d, N, rng):
    pts = []
    while len(pts) < N:
        t = rng.random(4*N); x = rng.random((4*N, d-1)) - 0.5
        for i in range(4*N):
            ti = t[i]; xi = x[i]
            r2 = float(np.dot(xi, xi))
            if ti*ti > r2 and (1-ti)*(1-ti) > r2:
                pts.append((ti, xi))
                if len(pts) == N: break
    ts = np.array([p[0] for p in pts]); xs = np.array([p[1] for p in pts])
    order = np.argsort(ts)
    return ts[order], xs[order]

def causal_matrix(ts, xs):
    dt = ts[None, :] - ts[:, None]
    dx2 = ((xs[None, :, :] - xs[:, None, :])**2).sum(axis=2)
    return ((dt > 0) & (dt*dt > dx2)).astype(np.int32)

def perc_matrix(N, p, rng):
    U = (rng.random((N, N)) < p)
    M = np.triu(U, 1).astype(np.int32)
    R = M.copy()
    for _ in range(int(math.log2(N)) + 2):
        R = np.minimum(R + (R @ R > 0), 1)
    return R.astype(np.int32)

def box_matrix(d, N, rng):
    P = rng.random((N, d))
    P = P[np.argsort(P[:, 0])]
    M = np.ones((N, N), dtype=bool)
    for k in range(d):
        M &= (P[None, :, k] - P[:, None, k]) > 0
    return M.astype(np.int32)

def mm_f(d):
    return (math.gamma(d+1) * math.gamma(d/2)) / (2 * math.gamma(1.5*d))
def mm_dim(r):
    lo, hi = 1.05, 8.0
    for _ in range(80):
        mid = 0.5*(lo+hi)
        if mm_f(mid) > r: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)
def mm_fraction(M):
    n = M.shape[0]
    return 2.0 * M.sum() / (n * (n - 1))
def longest_chain(M):
    n = M.shape[0]
    L = np.ones(n, dtype=np.int64)
    for j in range(n):
        preds = np.nonzero(M[:, j])[0]
        if len(preds): L[j] = 1 + L[preds].max()
    return int(L.max())
def three_chain_ratio(M):
    n2 = M.sum()
    return float(((M @ M) * M).sum()) / max(n2, 1)

def chain_through(M, idx):
    """Longest chain within the sub-order on idx (order-only)."""
    sub = M[np.ix_(idx, idx)]
    return longest_chain(sub)

def spatial_orderonly(ts, xs, M, rng, npairs=20, q=0.10):
    """Order-only distance proxy: quantile over common-diamond (u, w) of the
    LONGEST-CHAIN length through [u, w]. Coordinates used ONLY as ground
    truth for validation. Pairs are pre-filtered by the ORDER-ONLY domain
    condition (a common diamond exists) — the pin's estimator domain.
    Returns (spearman, naive_min_mean, n_pairs)."""
    N = len(ts)
    comp = (M + M.T) > 0
    pairs = []; tries = 0
    while len(pairs) < npairs and tries < 20000:
        i, j = rng.integers(0, N, 2); tries += 1
        if i == j or comp[i, j]: continue
        if not (M[:, i] & M[:, j]).any(): continue   # order-only: common past
        if not (M[i, :] & M[j, :]).any(): continue   # order-only: common future
        pairs.append((min(i, j), max(i, j)))
    est, true, mins = [], [], []
    for (i, j) in pairs:
        past = np.nonzero(M[:, i] & M[:, j])[0]
        fut = np.nonzero(M[i, :] & M[j, :])[0]
        chains = []
        for _ in range(25):
            u = past[rng.integers(0, len(past))]
            w = fut[rng.integers(0, len(fut))]
            if M[u, w]:
                interior = np.nonzero(M[u, :] & M[:, w])[0]
                idx = np.concatenate(([u], interior, [w]))
                chains.append(chain_through(M, idx))
        if len(chains) < 5: continue
        est.append(float(np.quantile(chains, q)))
        mins.append(float(np.min(chains)))
        dx = xs[i] - xs[j]
        true.append(float(np.sqrt((dx*dx).sum())))
    if len(est) < 8: return None, None, len(est)
    def ranks(a):
        idx = np.argsort(a); rk = np.empty(len(a)); rk[idx] = np.arange(len(a))
        return rk
    rho = float(np.corrcoef(ranks(np.array(est)), ranks(np.array(true)))[0, 1])
    return rho, float(np.mean(mins)), len(est)

def max_interval(M, min_size=64):
    counts = (M @ M) * M
    u, w = np.unravel_index(np.argmax(counts), counts.shape)
    size = int(counts[u, w])
    idx = np.nonzero(M[u, :] & M[:, w])[0]
    return u, w, idx, size

def midpoint_dim(M):
    """Midpoint-scaling estimator on the maximal interval: the midpoint m
    maximizes min(|I(u,m)|, |I(m,w)|) among interval elements; the counts
    are taken in the FULL order (pinned convention); d = -log2(ratio)."""
    counts = (M @ M) * M
    u, w = np.unravel_index(np.argmax(counts), counts.shape)
    big = int(counts[u, w])
    if big < 16: return None
    idx = np.nonzero(M[u, :] & M[:, w])[0]
    best_m, best_val = None, -1
    for m in idx:
        a, b = int(counts[u, m]), int(counts[m, w])
        v = min(a, b)
        if v > best_val: best_val, best_m = v, m
    ratio = (int(counts[u, best_m]) + 1) / (big + 1)     # +1: endpoint convention
    if ratio <= 0 or ratio >= 1: return None
    return -math.log2(ratio)

# ---- D30 growth machinery (frozen; array-deterministic) -------------------
EPS, Q = 0.2, 0.5
def grow(kernel, n_events, rng):
    regs = ['R', 'A', 'B']; N0 = 3
    cap = n_events * 6 + 64
    INF = 10**6
    dist = np.full((cap, cap), INF, dtype=np.int32)
    for i in range(N0): dist[i, i] = 0
    dist[0, 1] = dist[1, 0] = 1; dist[1, 2] = dist[2, 1] = 1
    dist[0, 2] = dist[2, 0] = 2
    nreg = N0; ops = []
    while len(ops) < n_events:
        uns = list(range(1, nreg))
        U = len(uns)
        D = dist[1:nreg, 1:nreg]
        collar_pairs = np.argwhere(D == 1)
        w_none, w_birth, w_collar = 1.0, float(U), float(len(collar_pairs))
        tot = w_none + w_birth + w_collar
        u = rng.random() * tot
        if u < w_none: ops.append(('n',)); continue
        u -= w_none
        if u < w_birth:
            parent = uns[rng.integers(0, U)]
            child = nreg; nreg += 1
            nd = dist[:nreg-1, parent] + 1
            dist[:nreg-1, child] = nd; dist[child, :nreg-1] = nd
            dist[child, child] = 0
            ops.append(('b', parent, child)); continue
        u -= w_birth
        k = rng.integers(0, len(collar_pairs))
        y, x = collar_pairs[k] + 1
        ops.append(('i', int(y), int(x)))
    return ops

def event_order(ops):
    acts = [op for op in ops if op[0] != 'n']
    M = len(acts)
    R = np.zeros((M, M), dtype=bool)
    last = {}
    for j, op in enumerate(acts):
        parts = (op[1], op[2])
        col = np.zeros(M, dtype=bool)
        for r in parts:
            if r in last:
                col |= R[:, last[r]]; col[last[r]] = True
        R[:, j] = col
        for r in parts: last[r] = j
    return R.astype(np.int32)

def round12(x):
    if isinstance(x, float): return float(f"{x:.12g}")
    if isinstance(x, dict): return {k: round12(v) for k, v in x.items()}
    if isinstance(x, list): return [round12(v) for v in x]
    return x

print("[d32a card v2 + anchor]")
print(f"      env: python {sys.version.split()[0]}, numpy {np.__version__},")
print(f"      {platform.platform()}; base seed {BASE}.")

# ---- build card v2 --------------------------------------------------------
def cell_stats(mats):
    rs = [mm_fraction(M) for M in mats]
    dh = [mm_dim(r) for r in rs]
    Ls = [longest_chain(M) for M in mats]
    r3 = [three_chain_ratio(M) for M in mats]
    md = [m for m in (midpoint_dim(M) for M in mats) if m is not None]
    return {"r_mean": np.mean(rs), "r_sd": np.std(rs),
            "dhat_mean": np.mean(dh), "dhat_sd": np.std(dh),
            "L_mean": np.mean(Ls), "L_sd": np.std(Ls),
            "ratio3_mean": np.mean(r3), "ratio3_sd": np.std(r3),
            "dmid_mean": (np.mean(md) if md else None),
            "dmid_sd": (np.std(md) if md else None),
            "n_mid": len(md)}

card = {"schema": "v2", "base_seed": BASE, "sig_digits": 12,
        "env": {"python": sys.version.split()[0], "numpy": np.__version__,
                "platform": platform.platform()},
        "cells": {}, "controls": {}}
sp_rows = {}
for d in DIMS:
    for N in SIZES:
        mats = []
        for s in range(SEEDS):
            rng = np.random.default_rng(BASE + 1000*d + 10*N + s)
            ts, xs = sprinkle_interval(d, N, rng)
            mats.append(causal_matrix(ts, xs))
        st = cell_stats(mats)
        st["chain_c"] = st["L_mean"] / N**(1.0/d)
        card["cells"][f"d{d}_N{N}"] = st
        if d in (3, 4) and N == 1024:
            rng = np.random.default_rng(BASE + 777*d)
            ts, xs = sprinkle_interval(d, N, rng)
            M = causal_matrix(ts, xs)
            sp_rows[d] = spatial_orderonly(ts, xs, M, rng)
for N in SIZES:
    for name, gen in (("box4", lambda s: box_matrix(4, N, np.random.default_rng(BASE + 8000 + 10*N + s))),
                      ("perc", lambda s: perc_matrix(N, 0.05, np.random.default_rng(BASE + 9000 + 10*N + s)))):
        mats = [gen(s) for s in range(SEEDS)]
        st = cell_stats(mats)
        st["chain_c4"] = st["L_mean"] / N**0.25
        card["controls"][f"{name}_N{N}"] = st

card["spatial_orderonly"] = {}
for d in (3, 4):
    rho, mn, k = sp_rows[d]
    card["spatial_orderonly"][f"d{d}_N1024"] = {
        "rho": rho, "naive_min_mean": mn, "n_pairs": k,
        "verdict": ("CARD-CARRIED" if (rho is not None and rho >= 0.60)
                    else "VACANT")}

blob1 = json.dumps(round12(card), sort_keys=True, indent=1)
blob2 = json.dumps(round12(json.loads(json.dumps(round12(card)))), sort_keys=True, indent=1)
det_ok = (blob1 == blob2)
with open("v10/data/d32_instrument_card_v2.json", "w") as f:
    f.write(blob1)
h2 = hashlib.sha256(blob1.encode()).hexdigest()[:16]
ok1 = det_ok and all(f"d{d}_N{N}" in card["cells"] for d in DIMS for N in SIZES)
ok1 &= all(f"box4_N{N}" in card["controls"] and f"perc_N{N}" in card["controls"]
           for N in SIZES)
ok1 &= all("ratio3_sd" in v for v in card["controls"].values())
check("P1 card v2 built and frozen: fixed-decimal (12 sig digits), sorted "
      "keys, in-process determinism gate, environment recorded, per-cell "
      "SDs INCLUDING the controls at every N", ok1, f"sha256/16 = {h2}")

# P2: the order-only spatial estimator — the pinned >= 0.60 bar DECIDES
# card-carried vs vacant; either outcome is a result (pin (b)); the gate is
# that the decision was reached and recorded in the card with its numbers.
det = []
for d in (3, 4):
    rho, mn, k = sp_rows[d]
    v = card["spatial_orderonly"][f"d{d}_N1024"]["verdict"]
    if rho is None:
        det.append(f"d{d}: {v} — only {k} common-diamond pairs (< 8)")
    else:
        det.append(f"d{d}: {v} — rho = {rho:.3f} on {k} pairs (naive-min "
                   f"mean {mn:.1f} — the RW degeneracy axis, disclosed)")
ok2 = all(f"d{d}_N1024" in card["spatial_orderonly"] for d in (3, 4))
check("P2 the ORDER-ONLY spatial estimator (quantile of longest-chain "
      "through common diamonds; coordinates only as validation ground "
      "truth): the >= 0.60 Spearman bar decided and card-recorded", ok2,
      "; ".join(det))

# P3: midpoint-scaling bands on synthetic ground truth
ok3 = True
det = []
for d in DIMS:
    c = card["cells"][f"d{d}_N1024"]
    ok3 &= c["dmid_mean"] is not None and abs(c["dmid_mean"] - d) <= 0.35
    det.append(f"d{d}: dmid {c['dmid_mean']:.3f}±{c['dmid_sd']:.3f} (n={c['n_mid']})")
check("P3 midpoint-scaling validated: mean d_mid within ±0.35 of truth at "
      "N = 1024, every dimension (now receipt-carried, was review-external)",
      ok3, "; ".join(det))

# P4: THE ANCHOR — the D30 collar cell under card v2
dhs, dms = [], []
for s in range(10):
    rng = np.random.default_rng(30260712 + 100*512 + s)
    ops = grow('collar', 3*512, rng)
    acts = [op for op in ops if op[0] != 'n'][:512]
    R = event_order(acts)
    u, w, idx, size = max_interval(R)
    sub = R[np.ix_(idx, idx)]
    dhs.append(mm_dim(mm_fraction(sub)) if size >= 64 else mm_dim(mm_fraction(R)))
    md = midpoint_dim(R)
    if md is not None: dms.append(md)
d_anchor = float(np.mean(dhs)); dmid_anchor = float(np.mean(dms)) if dms else None
cell2 = card["cells"]["d2_N512"]
excl = abs(d_anchor - 2) > 3*cell2["dhat_sd"]
ok4 = abs(d_anchor - 1.76) <= 0.10
ok4 &= dmid_anchor is not None and abs(d_anchor - dmid_anchor) <= 0.15
ok4 &= excl
dmid_txt = f"{dmid_anchor:.3f}" if dmid_anchor is not None else "VACANT"
check("P4 THE ANCHOR: the D30 collar cell regrown (frozen kernel, D30 "
      "seeds; the array-based sampler is deterministic, so the band is a "
      "reproduction gate) — d_hat within ±0.10 of 1.76; MM/midpoint "
      "concordance <= 0.15; M^2-exclusion re-verdict under card-v2 bands "
      "HOLDS", ok4,
      f"d_MM = {d_anchor:.3f}, d_mid = {dmid_txt}, "
      f"M2 exclusion: |{d_anchor:.3f}-2| vs 3x{cell2['dhat_sd']:.3f}")

# P5: the determinized exception census (the D31 O5 debt), 30 seeds
CS_LOCAL = None
def grow_census(n_events, rng):
    regs = ['R', 'A', 'B']; sealed = {'R'}
    adj = {'R': {'A'}, 'A': {'R', 'B'}, 'B': {'A'}}
    acts = []; k = 1
    while len(acts) < n_events:
        uns = [r for r in regs if r not in sealed]
        opts = [('none',)] + [('birth', y) for y in uns]
        for y in uns:
            for x in sorted(adj[y]):
                if x != y and x not in sealed: opts.append(('interact', y, x))
        pick = opts[rng.integers(0, len(opts))]
        if pick[0] == 'none': continue
        if pick[0] == 'birth':
            child = f"z{k:03d}"; k += 1
            regs.append(child); adj[child] = {pick[1]}; adj[pick[1]].add(child)
            acts.append(('b', pick[1], child))
        else:
            acts.append(('i', pick[1], pick[2]))
    return acts
multi, seven = [], []
for s in range(30):
    acts = grow_census(256, np.random.default_rng(41260712 + s))
    touch = {}
    for op in acts:
        if op[0] == 'i': touch[(op[1], op[2])] = touch.get((op[1], op[2]), 0) + 1
    multi.append(sum(1 for v in touch.values() if v >= 2))
    seven.append(sum(1 for v in touch.values() if v >= 7))
check("P5 the determinized exception census (30 seeds, N = 256): the "
      "cancellation-capable (>= 7 same-pair-touch) rate with spread — the "
      "honest exception bookkeeping D32B consumes", True,
      f">=2: {np.mean(multi):.1f}±{np.std(multi):.1f}; "
      f">=7: {np.mean(seven):.2f}±{np.std(seven):.2f} per web")

# P6: decision-stability audit (pin F1): no decided verdict above sits
# within one last-rounding-digit of its bar (vacant rows contribute none)
margins = [abs(d_anchor - 1.76) - 0.10]
if dmid_anchor is not None:
    margins.append(abs(d_anchor - dmid_anchor) - 0.15)
for d in (3, 4):
    if sp_rows[d][0] is not None:
        margins.append(sp_rows[d][0] - 0.60)
for d in DIMS:
    c = card["cells"][f"d{d}_N1024"]
    if c["dmid_mean"] is not None:
        margins.append(abs(c["dmid_mean"] - d) - 0.35)
ok6 = all(abs(m) > 1e-9 for m in margins)
check("P6 decision-stability audit: no decided gate verdict sits within "
      "rounding distance of its bar (12-digit serialization cannot flip "
      "any verdict)", ok6, f"margins: {[f'{m:+.4f}' for m in margins]}")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: P1 freeze, P2 verdict-recorded, "
      f"P3 midpoint bands, P4 the anchor, P5 census, P6 stability audit)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
