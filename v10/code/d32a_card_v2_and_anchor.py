#!/usr/bin/env python3
"""
d32a_card_v2_and_anchor.py — v10 D32A: the deterministic card, the
validated order-only estimators, the 1.76 anchor, and the exception
census. Pin: note-d32-dimension-map.md §1 (committed pre-run) + §6
round-1 repairs + §7 delta-2 (external review #2 adoptions; both
committed pre-rerun; reports reviews/d32a-round1-...md and
reviews/d31-d32-external-user-review-2.md).
Card v2.2: %.12g fixed-significant serialization, sorted keys,
recorded numerical environment + generator sha, per-cell SDs INCLUDING
the controls at every N and the chain constants. P2 conventions
DECLARED per round-1 M1 + §7: canonical tie-averaged Spearman vs
INVARIANT proper distance, pooled over 12 FRESH sprinklings x 10
pairs, CLUSTER-AWARE uncertainty (sprinkling-level bootstrap +
jackknife SE — the pair-level bootstrap of v2.1 treated clustered
pairs as independent and is superseded); bar 0.60 unchanged; the
attempt-2 stream replayed to the 12-digit freeze as a guard; vacancy
admissible; the certification is rank MONOTONICITY only (an order-only
RANKING instrument — no calibrated distance, no scaling law). The
anchor deliverable is THE SIGNATURE PAIR (d_MM, d_mid) per §7.
Float64 MC + numpy (declared); all seeds fixed.
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

def fmt(x, nd=3):
    return f"{x:.{nd}f}" if x is not None else "VACANT"

DIMS = (2, 3, 4)
SIZES = (256, 512, 1024)
SEEDS = 20
BASE = 20260712
GEN_SHA = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()[:16]

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

def spatial_pairs(ts, xs, M, rng, npairs, q=0.10):
    """Order-only distance proxy: 0.10-quantile over common-diamond (u, w)
    of the LONGEST-CHAIN length through [u, w]. Pairs pre-filtered by the
    ORDER-ONLY domain condition (a common diamond exists). The estimator
    column is built from M alone; ts/xs feed ONLY the two ground-truth
    columns. Draw structure identical to attempt 2 (bitwise-replay guard).
    Returns (est, truth_invariant, truth_frame, naive_mins)."""
    N = M.shape[0]
    comp = (M + M.T) > 0
    pairs = []; tries = 0
    while len(pairs) < npairs and tries < 20000:
        i, j = rng.integers(0, N, 2); tries += 1
        if i == j or comp[i, j]: continue
        if not (M[:, i] & M[:, j]).any(): continue   # order-only: common past
        if not (M[i, :] & M[j, :]).any(): continue   # order-only: common future
        pairs.append((min(i, j), max(i, j)))
    est, t_inv, t_frame, mins = [], [], [], []
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
        dx = xs[i] - xs[j]; dt = float(ts[i] - ts[j])
        r2 = float((dx*dx).sum())
        t_frame.append(math.sqrt(r2))
        t_inv.append(math.sqrt(max(r2 - dt*dt, 0.0)))   # spacelike: dx^2 > dt^2
    return est, t_inv, t_frame, mins

def ranks_index(a):
    """Attempt-2 legacy ranking (index tie-breaking) — replay audit ONLY."""
    a = np.asarray(a)
    idx = np.argsort(a); rk = np.empty(len(a)); rk[idx] = np.arange(len(a))
    return rk
def spearman_index(e, t):
    return float(np.corrcoef(ranks_index(e), ranks_index(t))[0, 1])

def avranks(v):
    """Average ranks over ties — canonical Spearman [DECLARED, round-1 M1]."""
    v = np.asarray(v, dtype=float)
    order = np.argsort(v, kind='mergesort')
    rk = np.empty(len(v)); rk[order] = np.arange(1, len(v) + 1, dtype=float)
    for val in np.unique(v):
        m = (v == val)
        if m.sum() > 1: rk[m] = rk[m].mean()
    return rk
def spearman_canonical(e, t):
    return float(np.corrcoef(avranks(e), avranks(t))[0, 1])

def cluster_bootstrap(clusters, rng, nboot=10000, bar=0.60):
    """SPRINKLING-level bootstrap (§7: pairs cluster within sprinklings —
    resample the 12 clusters with replacement, pool, recompute the deciding
    statistic). clusters = list of (est_list, truth_list).
    Returns (lo95, hi95, P(<bar))."""
    K = len(clusters)
    vals = np.empty(nboot)
    for b in range(nboot):
        ids = rng.integers(0, K, K)
        e = [v for i in ids for v in clusters[i][0]]
        t = [v for i in ids for v in clusters[i][1]]
        vals[b] = spearman_canonical(e, t)
    lo, hi = np.quantile(vals, [0.025, 0.975])
    return float(lo), float(hi), float(np.mean(vals < bar))

def cluster_jackknife(clusters):
    """Leave-one-sprinkling-out jackknife SE of the pooled statistic (§7)."""
    K = len(clusters)
    rhos = []
    for i in range(K):
        e = [v for j in range(K) if j != i for v in clusters[j][0]]
        t = [v for j in range(K) if j != i for v in clusters[j][1]]
        rhos.append(spearman_canonical(e, t))
    rhos = np.array(rhos); m = float(rhos.mean())
    return math.sqrt((K - 1) / K * float(((rhos - m)**2).sum()))

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

print("[d32a card v2.2 + anchor — §6 round-1 + §7 delta-2 repairs applied]")
print(f"      env: python {sys.version.split()[0]}, numpy {np.__version__},")
print(f"      {platform.platform()}; base seed {BASE}; generator {GEN_SHA}.")

# ---- build the card -------------------------------------------------------
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

card = {"schema": "v2.2", "base_seed": BASE, "sig_digits": 12,
        "generator_sha256_16": GEN_SHA,
        "env": {"python": sys.version.split()[0], "numpy": np.__version__,
                "platform": platform.platform()},
        "cells": {}, "controls": {}}
def build_cell(d, N):
    mats = []
    for s in range(SEEDS):
        rng = np.random.default_rng(BASE + 1000*d + 10*N + s)
        ts, xs = sprinkle_interval(d, N, rng)
        mats.append(causal_matrix(ts, xs))
    st = cell_stats(mats)
    st["chain_c"] = st["L_mean"] / N**(1.0/d)
    st["chain_c_sd"] = st["L_sd"] / N**(1.0/d)   # = SD of per-seed L/N^(1/d)
    return st
for d in DIMS:
    for N in SIZES:
        card["cells"][f"d{d}_N{N}"] = build_cell(d, N)
for N in SIZES:
    for name, gen in (("box4", lambda s: box_matrix(4, N, np.random.default_rng(BASE + 8000 + 10*N + s))),
                      ("perc", lambda s: perc_matrix(N, 0.05, np.random.default_rng(BASE + 9000 + 10*N + s)))):
        mats = [gen(s) for s in range(SEEDS)]
        st = cell_stats(mats)
        st["chain_c4"] = st["L_mean"] / N**0.25
        st["chain_c4_sd"] = st["L_sd"] / N**0.25
        card["controls"][f"{name}_N{N}"] = st

# ---- the spatial estimator (round-1 M1 conventions; §7 cluster-aware) -----
FROZEN_LEGACY = {3: 0.858646616541, 4: 0.717293233083}   # attempt-2 card rows
# v2.1's 3x40 pooled readings (card 0d33f81d67486a29) — PROVENANCE citations:
# the pair-level bootstrap under them treated clustered pairs as independent
# and is superseded by the cluster-aware certification below (§7).
FROZEN_V21_POOL = {3: 0.814058559751, 4: 0.786629123194}
sp = {}
for d in (3, 4):
    # (A) replay of the attempt-2 stream (npairs = 20) + 2x2 audit; the
    # guard compares to the 12-digit freeze (|delta| < 1e-9)
    rng = np.random.default_rng(BASE + 777*d)
    ts, xs = sprinkle_interval(d, 1024, rng)
    M = causal_matrix(ts, xs)
    e0, ti0, tf0, mn0 = spatial_pairs(ts, xs, M, rng, npairs=20)
    legacy = spearman_index(e0, tf0)
    audit = {"receipt_tie_frame": legacy,
             "canonical_frame": spearman_canonical(e0, tf0),
             "receipt_tie_invariant": spearman_index(e0, ti0),
             "canonical_invariant": spearman_canonical(e0, ti0)}
    replay_ok = abs(legacy - FROZEN_LEGACY[d]) < 1e-9
    # (B) the deciding validation (§7 delta-2): 12 FRESH sprinklings x 10
    # pairs, pooled; uncertainty at the SPRINKLING level
    clusters, MN, per_s = [], [], []
    for k in range(12):
        rng = np.random.default_rng(BASE + 20000 + 100*d + k)
        ts, xs = sprinkle_interval(d, 1024, rng)
        M = causal_matrix(ts, xs)
        e, ti, tf, mn = spatial_pairs(ts, xs, M, rng, npairs=10)
        clusters.append((e, ti, tf))
        per_s.append(spearman_canonical(e, ti) if len(e) >= 5 else None)
        MN += mn
    E = [v for c in clusters for v in c[0]]
    TI = [v for c in clusters for v in c[1]]
    TF = [v for c in clusters for v in c[2]]
    inv_clusters = [(c[0], c[1]) for c in clusters]
    if len(E) >= 60:    # §7-silent domain floor; immaterial at full yield
        rho = spearman_canonical(E, TI)
        lo, hi, pbar = cluster_bootstrap(inv_clusters,
                                         np.random.default_rng(BASE + 555*d))
        jk_se = cluster_jackknife(inv_clusters)
        rho_frame = spearman_canonical(E, TF)
    else:
        rho = lo = hi = pbar = jk_se = rho_frame = None
    sp[d] = dict(replay_ok=replay_ok, audit=audit, rho=rho, ci=(lo, hi),
                 p_below=pbar, jk_se=jk_se, rho_frame=rho_frame, n=len(E),
                 per_s=per_s, naive_min=(float(np.mean(MN)) if MN else None))

# (C) the naive-min drift row across N (round-1 m3; feeds F2)
drift = {}
for d in (3, 4):
    row = {}
    for N in SIZES:
        rng = np.random.default_rng(BASE + 777*d + 10*N)
        ts, xs = sprinkle_interval(d, N, rng)
        M = causal_matrix(ts, xs)
        _, _, _, mn = spatial_pairs(ts, xs, M, rng, npairs=20)
        row[f"N{N}"] = float(np.mean(mn)) if mn else None
    drift[f"d{d}"] = row

card["spatial_orderonly"] = {}
for d in (3, 4):
    s = sp[d]
    verdict = ("CARD-CARRIED" if (s["rho"] is not None and s["rho"] >= 0.60)
               else "VACANT")
    card["spatial_orderonly"][f"d{d}_N1024"] = {
        "certifies": ("rank MONOTONICITY over common-diamond pairs — an "
                      "order-only spatial RANKING instrument; no absolute "
                      "scale, no calibrated distance, no scaling law (§7)"),
        "domain": "common-diamond pairs (order-only pre-filter)",
        "tie_convention": "average-ranks (canonical Spearman)",
        "truth_convention": "invariant proper distance sqrt(dx^2-dt^2)",
        "rho_pooled": s["rho"],
        "cluster_bootstrap_ci95": [s["ci"][0], s["ci"][1]],
        "cluster_p_below_bar": s["p_below"],
        "jackknife_se": s["jk_se"],
        "n_pairs": s["n"], "n_sprinklings": 12,
        "rho_per_sprinkling": s["per_s"],
        "rho_pooled_frame_disclosed": s["rho_frame"],
        "audit_20pair_2x2": s["audit"],
        "naive_min_mean": s["naive_min"],
        "v2_1_provenance": {
            "rho_pooled_3x40": FROZEN_V21_POOL[d],
            "card_sha256_16": "0d33f81d67486a29",
            "note": ("pair-level bootstrap superseded per §7 — pairs "
                     "cluster within sprinklings")},
        "advisory_rule": "advisory-only if cluster_p_below_bar > 0.10 (§7)",
        "verdict": verdict}
card["f2_naive_min_drift"] = drift

# ---- P1: freeze -----------------------------------------------------------
blob1 = json.dumps(round12(card), sort_keys=True, indent=1)
blob2 = json.dumps(round12(json.loads(blob1)), sort_keys=True, indent=1)
idem_ok = (blob1 == blob2)
# state-leakage recompute (round-1 m4): rebuild one cell from scratch
# in-process, byte-compare its serialized block. Catches rng-state/global
# leakage; cross-process byte-identity is credited to the round-1
# independent rerun (a within-process regeneration cannot see hash-salt
# nondeterminism, so the gate is labeled for what it tests).
releak_ok = (json.dumps(round12(build_cell(2, 256)), sort_keys=True)
             == json.dumps(round12(card["cells"]["d2_N256"]), sort_keys=True))
h2 = hashlib.sha256(blob1.encode()).hexdigest()[:16]
ok1 = idem_ok and releak_ok
ok1 &= all(f"d{d}_N{N}" in card["cells"] for d in DIMS for N in SIZES)
ok1 &= all(f"box4_N{N}" in card["controls"] and f"perc_N{N}" in card["controls"]
           for N in SIZES)
ok1 &= all("ratio3_sd" in v and ("chain_c_sd" in v or "chain_c4_sd" in v)
           for v in list(card["cells"].values()) + list(card["controls"].values()))
if ok1:
    with open("v10/data/d32_instrument_card_v2.json", "w") as f:
        f.write(blob1)
check("P1 card v2.2 built and frozen (file written only on pass): %.12g "
      "fixed-significant sorted-key serialization; in-process "
      "serialization-idempotence gate + state-leakage recompute (d2_N256 "
      "rebuilt byte-equal); environment AND generator sha recorded; per-cell "
      "SDs for every carded statistic incl. chain constants and the "
      "controls at every N; cross-process byte-identity credited to the "
      "round-1 independent rerun", ok1,
      f"sha256/16 = {h2}, generator {GEN_SHA}")

# ---- P2 -------------------------------------------------------------------
print("      F2 naive-min drift (order-only mins, 20 pairs/cell): "
      + "; ".join(f"d{d}: " + "/".join(fmt(drift[f'd{d}'][f'N{N}'], 2)
                                       for N in SIZES) for d in (3, 4))
      + f"  [N = {SIZES[0]}/{SIZES[1]}/{SIZES[2]}]")
ok2 = True
det = []
for d in (3, 4):
    s = sp[d]; row = card["spatial_orderonly"][f"d{d}_N1024"]
    ok2 &= s["replay_ok"]
    ok2 &= (s["rho"] is not None) or (s["n"] < 60)   # decision reached
    a = s["audit"]
    piece = f"d{d}: {row['verdict']} — pooled rho = {fmt(s['rho'])}"
    if s["rho"] is not None:
        pers = [p for p in s["per_s"] if p is not None]
        piece += (f" [cluster CI95 {s['ci'][0]:.3f},{s['ci'][1]:.3f}; "
                  f"cluster P(<bar) = {s['p_below']:.3f}; jk SE = "
                  f"{s['jk_se']:.3f}] on {s['n']} pairs / 12 sprinklings "
                  f"(per-sprinkling rho {min(pers):.3f}..{max(pers):.3f}); "
                  f"frame reading {fmt(s['rho_frame'])} (disclosed); v2.1 "
                  f"3x40 provenance {FROZEN_V21_POOL[d]:.3f}")
    piece += (f"; replay-to-freeze OK = {s['replay_ok']}; 20-pair 2x2 "
              f"(tie x truth) = {a['receipt_tie_frame']:.3f}/"
              f"{a['canonical_frame']:.3f}/{a['receipt_tie_invariant']:.3f}/"
              f"{a['canonical_invariant']:.3f}")
    det.append(piece)
check("P2 spatial (order-only, certifies RANKING only — §7): canonical "
      "tie-averaged Spearman vs INVARIANT proper distance, pooled over 12 "
      "FRESH sprinklings x 10 pairs; CLUSTER-AWARE uncertainty "
      "(sprinkling-level bootstrap + jackknife SE — v2.1's pair-level "
      "bootstrap superseded); bar 0.60 unchanged; the attempt-2 20-pair "
      "stream replayed to the 12-digit freeze (|delta| < 1e-9; guard); the "
      ">= 0.60 bar decides CARD-CARRIED vs VACANT — either outcome recorded "
      "(pin (b))", ok2, "; ".join(det))

# ---- P3: midpoint-scaling bands on synthetic ground truth -----------------
ok3 = True
det = []
for d in DIMS:
    c = card["cells"][f"d{d}_N1024"]
    ok3 &= c["dmid_mean"] is not None and abs(c["dmid_mean"] - d) <= 0.35
    det.append(f"d{d}: dmid {fmt(c['dmid_mean'])}±{fmt(c['dmid_sd'])} (n={c['n_mid']})")
check("P3 midpoint-scaling validated: mean d_mid within ±0.35 of truth at "
      "N = 1024, every dimension (receipt-carried)", ok3, "; ".join(det))

# ---- P4: THE ANCHOR — the D30 collar cell ---------------------------------
dhs, dms, diffs = [], [], []
for s in range(10):
    rng = np.random.default_rng(30260712 + 100*512 + s)
    ops = grow('collar', 3*512, rng)
    acts = [op for op in ops if op[0] != 'n'][:512]
    R = event_order(acts)
    u, w, idx, size = max_interval(R)
    sub = R[np.ix_(idx, idx)]
    dhs.append(mm_dim(mm_fraction(sub)) if size >= 64 else mm_dim(mm_fraction(R)))
    md = midpoint_dim(R)
    if md is not None:
        dms.append(md); diffs.append(dhs[-1] - md)
d_anchor = float(np.mean(dhs)); sd_mm = float(np.std(dhs))
dmid_anchor = float(np.mean(dms)) if dms else None
sd_mid = float(np.std(dms)) if dms else None
diff_m = float(np.mean(diffs)) if diffs else None
diff_sd = float(np.std(diffs, ddof=1)) if len(diffs) > 1 else None
diff_se = (diff_sd / math.sqrt(len(diffs))) if diff_sd is not None else None
cell2 = card["cells"]["d2_N512"]
excl = abs(d_anchor - 2) > 3*cell2["dhat_sd"]
ok4 = abs(d_anchor - 1.76) <= 0.10
ok4 &= dmid_anchor is not None and abs(d_anchor - dmid_anchor) <= 0.15
ok4 &= excl
frag = ((0.15 - diff_m) / diff_se) if (diff_m is not None and diff_se) else None
check("P4 THE ANCHOR — deliverable: THE SIGNATURE PAIR (d_MM, d_mid), a "
      "multi-exponent, decisively non-M^2 order geometry (§7 — no single "
      "dimension claimed that every manifold estimator must recover): the "
      "D30 collar cell regrown (frozen kernel, D30 seeds; "
      "array-deterministic sampler, so the band is a reproduction gate) — "
      "d_MM within ±0.10 of 1.76; MM/midpoint concordance <= 0.15 "
      "(deterministic on the frozen seeds; replication fragility stated per "
      "§6); M^2-exclusion re-verdict under card bands HOLDS", ok4,
      f"SIGNATURE PAIR (d_MM, d_mid) = ({fmt(d_anchor)}±{fmt(sd_mm)}, "
      f"{fmt(dmid_anchor)}±{fmt(sd_mid)}); paired diff {fmt(diff_m)}"
      f"±{fmt(diff_sd)} (SE {fmt(diff_se)}; concordance margin = "
      f"{fmt(frag, 2)} SE — the 0.126 gap is a real 2.66-SE property per "
      f"§6, NOT the small-|I| bias); M2 exclusion: |{fmt(d_anchor)}-2| vs "
      f"3x{fmt(cell2['dhat_sd'])}")

# ---- P5: the exception census (round-1 M2 record; note §6 ensemble) -------
def grow_census(n_events, rng):
    """D32B's PINNED ensemble: grown-acts-only N, z-padded names, ordered
    pairs, family 41260712+s. A RE-IMPLEMENTATION of the d31b B4 grower —
    same seed family, DIFFERENT webs at shared seeds (disclosed, note §6)."""
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
multi, seven, seven_un = [], [], []
for s in range(30):
    acts = grow_census(256, np.random.default_rng(41260712 + s))
    touch = {}
    for op in acts:
        if op[0] == 'i': touch[(op[1], op[2])] = touch.get((op[1], op[2]), 0) + 1
    un = {}
    for (y, x), v in touch.items():
        key = tuple(sorted((y, x))); un[key] = un.get(key, 0) + v
    multi.append(sum(1 for v in touch.values() if v >= 2))
    seven.append(sum(1 for v in touch.values() if v >= 7))
    seven_un.append(sum(1 for v in un.values() if v >= 7))
check("P5 the exception census (30 seeds, N = 256; the ensemble D32B is "
      "pinned to — grown-acts-only, padded names, ORDERED pairs "
      "(composition-relevant); non-commensurable with d31b B4 at shared "
      "seeds, disclosed): >= 7 same-pair-touch = cancellation-capable at "
      "the grown single-angle alphabet; the necessary count drops to 6 (5 "
      "with birth) if the 576/625 gate enters (note §6)", True,
      f">=2: {np.mean(multi):.1f}±{np.std(multi):.1f}; >=7 ordered: "
      f"{np.mean(seven):.2f}±{np.std(seven):.2f} per web, per-web range "
      f"{min(seven)}-{max(seven)}; >=7 unordered (disclosed): "
      f"{np.mean(seven_un):.2f}±{np.std(seven_un):.2f}")

# ---- P6: decision-stability audit (pin F1; round-1 completeness repair) ---
margins = [abs(d_anchor - 1.76) - 0.10,
           abs(d_anchor - 2) - 3*cell2["dhat_sd"]]   # the disclosed omission
if dmid_anchor is not None:
    margins.append(abs(d_anchor - dmid_anchor) - 0.15)
for d in (3, 4):
    if sp[d]["rho"] is not None:
        margins.append(sp[d]["rho"] - 0.60)
for d in DIMS:
    c = card["cells"][f"d{d}_N1024"]
    if c["dmid_mean"] is not None:
        margins.append(abs(c["dmid_mean"] - d) - 0.35)
ok6 = all(abs(m) > 1e-9 for m in margins)
check("P6 decision-stability audit (ALL decided verdicts incl. the "
      "M^2-exclusion): no verdict sits within rounding distance of its bar "
      "(12-digit serialization cannot flip any decision)", ok6,
      f"margins: {[f'{m:+.4f}' for m in margins]}")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: P1 record-freeze + idempotence; "
      f"P2, P3, P4, P6 substantive; P5 census bookkeeping)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
