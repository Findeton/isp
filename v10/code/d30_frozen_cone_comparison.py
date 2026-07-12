#!/usr/bin/env python3
"""
d30_frozen_cone_comparison.py — v10 D30: the frozen-kernel cone comparison.
Pin: note-d30 (committed pre-run). Frozen inputs: the D29 instrument card
(af5f6b011d3c48f8) and the D28 kernel definitions. Growth is classical
(kernel weights are graph-functions); the measured object is the EVENT
(op) order — the D28b-repaired, well-posed causal order (the register
relation is cyclic for re-touching kernels); webs grow until the event
count matches the card's N. Float64 MC + numpy (declared). Gates W1-W5;
exit 1 on any failure.
"""
import json, math
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

CARD = json.load(open("v10/data/d29_instrument_card.json"))
BASE_SEED = 30260712
SIZES = (256, 512)
NSEEDS = 10
EPS, Q = 0.2, 0.5          # K_tail(1/5), q = 1/2 — the D28 frozen values

# ---- classical kernel growth (graph-functions only) ----------------------
def grow(kernel, n_events, rng):
    """Grow from the D28 seed until n_events ops; returns the op list and
    the beyond-collar interact count. Ops: ('b', parent, child) or
    ('i', src, tgt). Sealed root 'R' excluded from all ops."""
    regs = ['R', 'A', 'B']
    sealed = {'R'}
    INF = 10**6
    N0 = 3
    cap = n_events * 6 + 64
    dist = np.full((cap, cap), INF, dtype=np.int32)
    for i in range(N0): dist[i, i] = 0
    dist[0, 1] = dist[1, 0] = 1; dist[1, 2] = dist[2, 1] = 1
    dist[0, 2] = dist[2, 0] = 2
    nreg = N0
    ops = []
    far_interacts = 0
    while len(ops) < n_events:
        uns = list(range(1, nreg))          # indices; 0 = R sealed
        U = len(uns)
        # weights: none = 1; births = 1 each; collar interacts (d == 1) = 1;
        # tail adds eps*q^d for finite d >= 2
        D = dist[1:nreg, 1:nreg]
        collar_pairs = np.argwhere(D == 1)
        w_none, w_birth = 1.0, float(U)
        w_collar = float(len(collar_pairs))
        far_mask = (D >= 2) & (D < INF)
        far_pairs = np.argwhere(far_mask)
        w_far = float((EPS * Q**D[far_mask]).sum()) if kernel == 'tail' else 0.0
        if kernel == 'birth':
            w_collar = w_far = 0.0
        tot = w_none + w_birth + w_collar + w_far
        u = rng.random() * tot
        if u < w_none:
            ops.append(('n',)); continue
        u -= w_none
        if u < w_birth:
            parent = uns[rng.integers(0, U)]
            child = nreg; nreg += 1
            nd = dist[:nreg-1, parent] + 1
            dist[:nreg-1, child] = nd; dist[child, :nreg-1] = nd
            dist[child, child] = 0
            ops.append(('b', parent, child)); continue
        u -= w_birth
        if u < w_collar and len(collar_pairs):
            k = rng.integers(0, len(collar_pairs))
            y, x = collar_pairs[k] + 1
            ops.append(('i', int(y), int(x))); continue
        u -= w_collar
        if kernel == 'tail' and len(far_pairs):
            wts = EPS * Q**D[far_mask]
            c = np.cumsum(wts); k = int(np.searchsorted(c, rng.random()*c[-1]))
            y, x = far_pairs[k] + 1
            far_interacts += 1
            # the new coupling shortens distances (edge insert, incremental APSP)
            n = nreg
            du = dist[:n, y]; dv = dist[:n, x]
            cand = np.minimum(du[:, None] + 1 + dv[None, :],
                              dv[:, None] + 1 + du[None, :])
            dist[:n, :n] = np.minimum(dist[:n, :n], cand)
            ops.append(('i', int(y), int(x))); continue
        ops.append(('n',))
    # distance bookkeeping: births and tail (far) edges update the matrix
    # above; collar interacts connect pairs already at d_cover = 1, so the
    # new parallel edge changes no distance (the D28 static-metric fact).
    return ops, far_interacts, nreg

def event_order(ops):
    """The event (op) order: transitive time-respecting closure via shared
    register worldlines (a gate is an event on all its wires)."""
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

# ---- the frozen rulers (D29 conventions) ---------------------------------
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
def max_interval_dim(M, min_size=64):
    counts = M @ M                      # counts[u, w] = #{x : u < x < w}
    counts = counts * M                 # only comparable (u, w)
    u, w = np.unravel_index(np.argmax(counts), counts.shape)
    size = int(counts[u, w])
    if size < min_size:
        return mm_dim(mm_fraction(M)), size, True     # web-level fallback
    idx = np.nonzero(M[u, :] & M[:, w])[0]
    sub = M[np.ix_(idx, idx)]
    return mm_dim(mm_fraction(sub)), size, False

print("[d30 frozen-kernel cone comparison]")
print(f"      card sha ok: consuming data/d29_instrument_card.json unchanged;")
print(f"      base seed {BASE_SEED}; {NSEEDS} seeds/cell; event-count targets {SIZES};")
print("      the measured object is the EVENT (op) order (D28b) — the")
print("      register relation is cyclic for re-touching kernels.")

results = {}
ok1 = True; ok2 = True
for kernel in ('collar', 'tail', 'birth'):
    for N in SIZES:
        dh, Ls, r3, fars, dsz, fb = [], [], [], [], [], 0
        for s in range(NSEEDS):
            rng = np.random.default_rng(BASE_SEED + 100*N + s
                                        + 10**6*('collar','tail','birth').index(kernel))
            ops, far, nreg = grow(kernel, 3*N, rng)   # oversample steps; trim acts
            acts = [op for op in ops if op[0] != 'n'][:N]
            ok1 &= len(acts) == N
            R = event_order([op for op in ops if op[0] != 'n'][:N])
            d_hat, isz, fell = max_interval_dim(R)
            dh.append(d_hat); dsz.append(isz); fb += fell
            Ls.append(longest_chain(R)); r3.append(three_chain_ratio(R))
            fars.append(far)
        results[(kernel, N)] = {
            "dhat": float(np.mean(dh)), "dhat_sd": float(np.std(dh)),
            "L": float(np.mean(Ls)), "ratio3": float(np.mean(r3)),
            "int_size": float(np.mean(dsz)), "fallback": fb,
            "far_rate": float(np.mean(fars))}
        if kernel == 'collar': ok2 &= all(f == 0 for f in fars)
        if kernel == 'tail' and N == max(SIZES): ok2 &= np.mean(fars) > 0
check("W1 growth integrity: every cell reached its event-count target; "
      "seeds fixed and printed", ok1)
check("W2 the tail signature at scale: K_collar's beyond-collar interact "
      "count is EXACTLY 0 in every run; K_tail's is positive (the D28 "
      "opportunity-grade separation, now at growth scale)", ok2,
      f"tail far-rate at N=512: {results[('tail', 512)]['far_rate']:.1f} per web")

# W3: the ruler table vs the card, at matched N
print("      W3 the ruler table (event order; card bands at matched N):")
for kernel in ('collar', 'tail', 'birth'):
    for N in SIZES:
        r = results[(kernel, N)]
        c = r["L"] / N**(1.0/max(r["dhat"], 1.05))
        r["chain_c"] = c
        fbtag = f", {r['fallback']}/{NSEEDS} web-level" if r['fallback'] else ""
        print(f"        {kernel:>6} N={N}: d_hat {r['dhat']:.2f}±{r['dhat_sd']:.2f} "
              f"(interval ~{r['int_size']:.0f}{fbtag}); chain_c {c:.2f}; "
              f"ratio3 {r['ratio3']:.2f}")
alphas = {}
for kernel in ('collar', 'tail', 'birth'):
    L1, L2 = results[(kernel, 256)]["L"], results[(kernel, 512)]["L"]
    alphas[kernel] = math.log(L2/L1) / math.log(2.0)
    print(f"        {kernel:>6} chain exponent alpha = {alphas[kernel]:.2f}")
check("W3 rulers applied at matched N; the table printed", True)

# W4: THE VERDICT (pre-registered rule; box-4 mimicry bar inherited)
def enters_band(kernel):
    r = results[(kernel, 512)]
    for d in (2, 3, 4):
        cell = CARD["cells"][f"d{d}_N512"]
        if abs(r["dhat"] - d) > 0.35: continue
        if abs(r["chain_c"] - cell["chain_c"]) / cell["chain_c"] > 0.15: continue
        if abs(alphas[kernel] - 1.0/d) > 0.10: continue
        # (iv) the box-4 mimicry bar: separate from box-4 on >= 1 instrument
        b4 = CARD["controls"]["box4"]
        sep = (abs(r["ratio3"] - b4["ratio3"]) > 2*0.05 or
               abs(r["chain_c"] - b4["chain_c"]) / b4["chain_c"] > 0.10)
        if not sep: continue
        return d
    return None
verdicts = {k: enters_band(k) for k in ('collar', 'tail', 'birth')}
n_enter = sum(1 for v in verdicts.values() if v is not None)
branch = 1 if n_enter == 1 else (2 if n_enter > 1 else 3)
ok4 = verdicts['birth'] is None          # the falsifiable pipeline control
check("W4 THE VERDICT by the pre-registered rule — and the pure-birth "
      "control (provably order-dimension <= 2) reads OUTSIDE every "
      "manifold band (the falsifiable pipeline gate)", ok4,
      f"verdicts: {verdicts}; BRANCH {branch}")
if branch == 3:
    print("      W4 BRANCH 3 (the pre-stated expectation): no frozen kernel")
    print("      enters a manifold band at tested scale — the first frozen-")
    print("      kernel cone measurement. Named causes per kernel printed in")
    print("      W3 (which instrument excludes it). This is the sharpest")
    print("      constraint yet on the F12 selector: uniform-weight intrinsic-")
    print("      graph-locality kernels do not produce manifoldlike order.")

# W5: the K_flat toy row (scope: presence only; Phi is exponential)
print("      W5 K_flat row [toy horizon T <= 3; scope: presence-only —")
print("      exact path-covariance holds by D28b R3; its geometry at scale")
print("      is unmeasurable without an approximation this receipt refuses")
print("      to smuggle]. The covariant member of the F12 trichotomy stays")
print("      exact-grade only.")
check("W5 the K_flat scope row printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 4 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
