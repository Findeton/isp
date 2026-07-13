#!/usr/bin/env python3
"""
d32c_s2_mechanism_test.py — v10 D32C: the S²-mechanism test. Pin:
note-d32 §10 (committed b6d8a9e pre-run). Hypothesis [POSITED,
mechanism-level]: DIRECTIONAL opportunity structure lifts effective
dimension where radius/weight/covariance do not (D32B #146-#148).
Family: the D32B (r=1, λ=1) collar kernel + 12-vertex icosahedral
directions (inherit + scatter-p to a neighbor vertex), interact
weights w = ((1 - u·u')/2)^κ (κ = 0 = the direction-blind CONTROL;
direction draws consumed identically in EVERY cell so κ is the only
axis at fixed seed). 7 cells × 12 seeds × N ∈ {256, 512}; the D32B
measurement/verdict machinery verbatim (card v2.2, z = 3.5 entry,
per-cell fallbacks + minima). THE PRE-REGISTERED LIFT BAR: a live
cell's d̂_MM mean above the control's by > 2× pooled SE WITH
κ-monotonicity at fixed p; any lift requires fresh-family replication
(family 61260712+, touched only on a fire) before the record carries
it; NO-LIFT is a result. Gates C1-C6; exit 1 on any failure.
"""
import json, math, hashlib
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

BASE_C = 60260712
CONF_C = 61260712
SIZES = (256, 512)
NSEEDS = 12
PHI = (1 + math.sqrt(5)) / 2
_raw = []
for a in (1.0, -1.0):
    for b in (PHI, -PHI):
        _raw += [(0.0, a, b), (a, b, 0.0), (b, 0.0, a)]
ICO = np.array(_raw) / math.sqrt(1 + PHI * PHI)
NBR = [sorted(range(12), key=lambda j: -float(ICO[i] @ ICO[j]))[1:6]
       for i in range(12)]

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
def max_interval(M):
    counts = (M @ M) * M
    u, w = np.unravel_index(np.argmax(counts), counts.shape)
    size = int(counts[u, w])
    idx = np.nonzero(M[u, :] & M[:, w])[0]
    return idx, size
def midpoint_dim(M):
    counts = (M @ M) * M
    u, w = np.unravel_index(np.argmax(counts), counts.shape)
    big = int(counts[u, w])
    if big < 16: return None
    idx = np.nonzero(M[u, :] & M[:, w])[0]
    best_m, best_val = None, -1
    for m in idx:
        v = min(int(counts[u, m]), int(counts[m, w]))
        if v > best_val: best_val, best_m = v, m
    ratio = (int(counts[u, best_m]) + 1) / (big + 1)
    if ratio <= 0 or ratio >= 1: return None
    return -math.log2(ratio)
def event_order(acts):
    M = len(acts)
    R = np.zeros((M, M), dtype=bool)
    last = {}
    for j, op in enumerate(acts):
        col = np.zeros(M, dtype=bool)
        for r in (op[1], op[2]):
            if r in last:
                col |= R[:, last[r]]; col[last[r]] = True
        R[:, j] = col
        for r in (op[1], op[2]): last[r] = j
    return R.astype(np.int32)

def grow_s2(kappa, p, n_events, rng):
    """The r=1 collar kernel + icosahedral directions. Direction draws
    (seed dirs; per-birth scatter decision + hop target) are consumed
    IDENTICALLY in every cell (κ enters only the interact WEIGHTS)."""
    cap = n_events * 6 + 64
    INF = 10**6
    dist = np.full((cap, cap), INF, dtype=np.int32)
    for i in range(3): dist[i, i] = 0
    dist[0, 1] = dist[1, 0] = 1; dist[1, 2] = dist[2, 1] = 1
    dist[0, 2] = dist[2, 0] = 2
    dirs = np.zeros(cap, dtype=np.int64)
    for i in range(3): dirs[i] = rng.integers(0, 12)
    nreg = 3; acts = []
    align_sum = 0.0; n_i = 0
    while len(acts) < n_events:
        uns = list(range(1, nreg))
        U = len(uns)
        D = dist[1:nreg, 1:nreg]
        pairs = np.argwhere(D == 1)
        if kappa == 0:
            wts = np.ones(len(pairs))
        else:
            dots = np.array([float(ICO[dirs[a+1]] @ ICO[dirs[b+1]])
                             for a, b in pairs])
            wts = ((1.0 - dots) / 2.0) ** kappa
        w_none, w_birth, w_pairs = 1.0, float(U), float(wts.sum())
        tot = w_none + w_birth + w_pairs
        x = rng.random() * tot
        if x < w_none: continue
        x -= w_none
        if x < w_birth:
            parent = uns[rng.integers(0, U)]
            child = nreg; nreg += 1
            nd = dist[:nreg-1, parent] + 1
            dist[:nreg-1, child] = nd; dist[child, :nreg-1] = nd
            dist[child, child] = 0
            d = dirs[parent]
            if rng.random() < p:
                d = NBR[d][rng.integers(0, 5)]
            dirs[child] = d
            acts.append(('b', parent, child)); continue
        x -= w_birth
        cum = np.cumsum(wts)
        k = int(np.searchsorted(cum, x, side='right'))
        k = min(k, len(pairs) - 1)
        a, b = pairs[k] + 1
        acts.append(('i', int(a), int(b)))
        align_sum += float(ICO[dirs[a]] @ ICO[dirs[b]]); n_i += 1
    return acts, (align_sum / n_i if n_i else 0.0), n_i / max(len(acts), 1)

def measure(acts):
    R = event_order(acts)
    idx, size = max_interval(R)
    fallback = size < 64
    sub = R if fallback else R[np.ix_(idx, idx)]
    dmm = mm_dim(mm_fraction(sub))
    dmid = midpoint_dim(R)
    L = longest_chain(R)
    r3 = three_chain_ratio(R)
    touch = {}
    for op in acts:
        if op[0] == 'i':
            touch[(op[1], op[2])] = touch.get((op[1], op[2]), 0) + 1
    seven = sum(1 for v in touch.values() if v >= 7)
    return dmm, dmid, L, r3, seven, fallback, size

def run_cell(kappa, p, p_idx, N, base):
    rows = []
    for s in range(NSEEDS):
        rng = np.random.default_rng(base + 100000*kappa + 10000*p_idx
                                    + 1000*(N // 256) + s)
        acts, al, fr = grow_s2(kappa, p, 3*N + 64, rng)
        rows.append(measure(acts[:N]) + (al, fr))
    return rows

def stats(rows):
    dmm = np.array([x[0] for x in rows])
    dmid = np.array([x[1] for x in rows if x[1] is not None])
    gaps = np.array([x[0] - x[1] for x in rows if x[1] is not None])
    return dict(dmm=(dmm.mean(), dmm.std()), dmid=(dmid.mean(), dmid.std()),
                gap=(gaps.mean(), gaps.std()),
                L=float(np.mean([x[2] for x in rows])),
                r3=float(np.mean([x[3] for x in rows])),
                seven=float(np.mean([x[4] for x in rows])),
                fb=sum(1 for x in rows if x[5]),
                mn=float(min(x[0] for x in rows)),
                al=float(np.mean([x[7] for x in rows])),
                fr=float(np.mean([x[8] for x in rows])), dmms=dmm,
                n_mid=len(dmid))   # round-1 M2: the D32B field, restored

print("[d32c the S2-mechanism test — §10 pin b6d8a9e]")
blob = open("v10/data/d32_instrument_card_v2.json", "rb").read()
sha = hashlib.sha256(blob).hexdigest()[:16]
card = json.loads(blob)
check("C1 card v2.2 loaded and sha-asserted", sha == "e7bc80f0be08f537",
      f"sha256/16 = {sha}")

CELLS = [(0, 0.0, 0)] + [(k, pv, pi) for k in (1, 2)
                         for pi, pv in enumerate((0.0, 0.25, 0.5))]
data = {}
for (k, pv, pi) in CELLS:
    for N in SIZES:
        data[(k, pv, N)] = run_cell(k, pv, pi, N, BASE_C)
ok2 = all(len(v) == NSEEDS for v in data.values())
fbtxt = ", ".join(f"k={k},p={pv},N={N}: {stats(data[(k,pv,N)])['fb']}/12"
                  for (k, pv, pi) in CELLS for N in SIZES
                  if stats(data[(k, pv, N)])['fb'])
check("C2 the 7 cells complete (168 growths); per-cell fallbacks + minima "
      "disclosed (the D32B M1 discipline)", ok2,
      (f"fallbacks: {fbtxt or 'none'}; global min d_MM = "
       f"{min(stats(data[key])['mn'] for key in data):.4f}"))

def joint_verdict(st, N):
    for d in (2, 3, 4):
        c = card["cells"][f"d{d}_N{N}"]
        if (abs(st["dmm"][0] - c["dhat_mean"]) <= 3.5 * c["dhat_sd"]
            and abs(st["L"] / N**(1.0/d) - c["chain_c"]) <= 3.5 * c["chain_c_sd"]
            and abs(st["r3"] - c["ratio3_mean"]) <= 3.5 * c["ratio3_sd"]
            and abs(st["dmm"][0] - card["controls"][f"box4_N{N}"]["dhat_mean"])
                > 3 * card["controls"][f"box4_N{N}"]["dhat_sd"]
            and abs(st["dmm"][0] - card["controls"][f"perc_N{N}"]["dhat_mean"])
                > 3 * card["controls"][f"perc_N{N}"]["dhat_sd"]):
            return f"ENTERS-M{d}(z3.5,Bonf/7)"
    return "NO-BAND"
print("      THE S2 MAP [cell -> pair | gap | verdict | n_mid/12 | "
      "mean-align | fr | >=7]  (round-1 M2: the midpoint column is a "
      "SUBSET MEAN where n_mid < 12 — the starved regime shrinks the "
      "maximal interval below the midpoint floor on some seeds; cells "
      "with fb > 0 or n_mid < 12 are estimator MIXTURES, flagged *):")
zmin = None
for (k, pv, pi) in CELLS:
    for N in SIZES:
        st = stats(data[(k, pv, N)])
        for d in (2, 3, 4):
            c = card["cells"][f"d{d}_N{N}"]
            zs = [abs(st["dmm"][0] - c["dhat_mean"]) / c["dhat_sd"],
                  abs(st["L"] / N**(1.0/d) - c["chain_c"]) / c["chain_c_sd"],
                  abs(st["r3"] - c["ratio3_mean"]) / c["ratio3_sd"]]
            zmin = min(zmin, max(zs)) if zmin is not None else max(zs)
        tag = ("CONTROL k=0" if k == 0 else f"k={k} p={pv}") + f" N={N}"
        mix = "*" if (st["fb"] > 0 or st["n_mid"] < 12) else " "
        print(f"        {tag:22s}{mix}({st['dmm'][0]:.3f}±{st['dmm'][1]:.3f}, "
              f"{st['dmid'][0]:.3f}±{st['dmid'][1]:.3f}) | "
              f"{st['gap'][0]:+.3f}±{st['gap'][1]:.3f} | "
              f"{joint_verdict(st, N):22s} | {st['n_mid']}/12 | "
              f"{st['al']:+.3f} | {st['fr']:.3f} | {st['seven']:.1f}")
ok3 = zmin is not None and zmin > 3.5
check("C3 the map printed with verdicts (card-v2.2 joint rule, z = 3.5, "
      "Bonferroni/7), per-cell alignment (CF2), census column, n_mid, and "
      "mixture flags; the MINIMUM JOINT ENTRY THRESHOLD carried (round-1: "
      "NO-BAND is bar-independent)", ok3,
      f"min over cells x d of the max leg-z = {zmin:.1f} sigma")

st0 = {N: stats(data[(0, 0.0, N)]) for N in SIZES}
b512 = (1.908, 0.215)   # the D32B anchor cell, fresh family (LEDGER #147)
zc = abs(st0[512]["dmm"][0] - b512[0]) / math.sqrt(
    st0[512]["dmm"][1]**2/NSEEDS + b512[1]**2/NSEEDS)
check("C4 CF3: the k = 0 control vs the D32B anchor cell (matched kernel, "
      "different rng consumption via the direction draws + different seed "
      "family) — REPORTED, not gated to equality", True,
      f"control 512 = ({st0[512]['dmm'][0]:.3f}±{st0[512]['dmm'][1]:.3f}) "
      f"vs D32B (1.908±0.215): z = {zc:.2f}")

# C5: THE PRE-REGISTERED LIFT TEST
lift_fired = []
for k in (1, 2):
    for pv in (0.0, 0.25, 0.5):
        st = stats(data[(k, pv, 512)])
        se = math.sqrt(st["dmm"][1]**2/NSEEDS + st0[512]["dmm"][1]**2/NSEEDS)
        dz = (st["dmm"][0] - st0[512]["dmm"][0]) / se
        if dz > 2.0:
            mono = all(stats(data[(2, pv, 512)])["dmm"][0]
                       >= stats(data[(1, pv, 512)])["dmm"][0]
                       for _ in [0])
            lift_fired.append((k, pv, dz, mono))
if lift_fired:
    conf_txt = []
    all_conf = True
    for (k, pv, dz, mono) in lift_fired:
        pi = (0.0, 0.25, 0.5).index(pv)
        rows_c = run_cell(k, pv, pi, 512, CONF_C)
        rows_0 = run_cell(0, 0.0, 0, 512, CONF_C)
        stc, stz = stats(rows_c), stats(rows_0)
        sec = math.sqrt(stc["dmm"][1]**2/NSEEDS + stz["dmm"][1]**2/NSEEDS)
        dzc = (stc["dmm"][0] - stz["dmm"][0]) / sec
        ok_rep = dzc > 2.0 and mono
        all_conf &= ok_rep
        mixnote = ("" if (stats(data[(k, pv, 512)])["fb"] == 0
                          and stc["fb"] == 0)
                   else " [ESTIMATOR-MIXTURE cell — round-1 M2: the "
                        "discovery/confirmation pair may mix whole-order "
                        "and interval readings; interpret via the map's "
                        "flags]")
        conf_txt.append(f"k={k},p={pv}: discovery dz = {dz:.2f}, "
                        f"confirmation dz = {dzc:.2f}, kappa-monotone = "
                        f"{mono} -> {'CONFIRMED-LIFT' if ok_rep else 'UNREPLICATED'}"
                        + mixnote)
    check("C5 THE LIFT TEST (pre-registered bar: > 2x pooled SE above the "
          "control + kappa-monotonicity + FRESH-FAMILY replication per the "
          "45e/48d discipline)", True, "; ".join(conf_txt))
else:
    dzs = []
    for k in (1, 2):
        for pv in (0.0, 0.25, 0.5):
            st = stats(data[(k, pv, 512)])
            se = math.sqrt(st["dmm"][1]**2/NSEEDS
                           + st0[512]["dmm"][1]**2/NSEEDS)
            dzs.append(f"k={k},p={pv}: {(st['dmm'][0]-st0[512]['dmm'][0])/se:+.2f}")
    check("C5 THE LIFT TEST (pre-registered bar: > 2x pooled SE above the "
          "control + kappa-monotonicity + fresh-family replication): "
          "NO-LIFT — a result: the S2-mechanism hypothesis is CLOSED "
          "NEGATIVE at this family (anti-aligned icosahedral compatibility "
          "on the r = 1 collar; the confirmation family untouched)", True,
          "dz vs control at 512: " + ", ".join(dzs))

print("      C6 FRONTS: CF1 the 12-vertex coarseness (48-point refinement "
      "named, not run); CF2 in-table (mean-align column); CF3 reported at "
      "C4; CF4 the anti-aligned sign is the pinned posit (aligned variant "
      "named, not run).")
check("C6 fronts printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: C1 freeze-assert; C2 completeness "
      f"[record]; C3 the map [substantive]; C4 CF3 [record]; C5 the lift "
      f"test [substantive]; C6 fronts [record])"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
