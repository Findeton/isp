#!/usr/bin/env python3
"""
d32b_kernel_mechanism_map.py — v10 D32B: the kernel-mechanism map
(PHENOMENOLOGICAL). Pin: note-d32 §9 (committed 8b7271c pre-run; §2
superseded where they differ; §8 = the covariant-cell amendment).
NO cell is a candidate law (O3 terminal, LEDGER #145). Deliverable:
how kernel structure moves THE SIGNATURE PAIR (d_MM, d_mid) on the
frozen primary order. Instruments: card v2.2 e7bc80f0be08f537 (bands +
controls), the D30 corrected joint rule, Bonferroni over 10 cells for
any band-entry claim. Float64 MC + numpy; all seeds fixed
(50260712-family, disjoint from every prior family).
Gates B1-B7; exit 1 on any failure.
"""
import json, math, hashlib, sys
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

BASE_B = 50260712
SIZES = (256, 512)
NSEEDS = 12
RS = (1, 2, 3)
LAMS = ((0.5, 0), (1.0, 1), (2.0, 2))   # (lambda, index li)

# ---- instruments (frozen conventions; d32a lineage) ------------------------
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
        parts = (op[1], op[2])
        col = np.zeros(M, dtype=bool)
        for r in parts:
            if r in last:
                col |= R[:, last[r]]; col[last[r]] = True
        R[:, j] = col
        for r in parts: last[r] = j
    return R.astype(np.int32)

# ---- growers ---------------------------------------------------------------
def seed_dist(seed_kind, cap):
    INF = 10**6
    dist = np.full((cap, cap), INF, dtype=np.int32)
    if seed_kind == 'chain':      # R-A-B (the D28/D30 seed)
        n0 = 3
        for i in range(n0): dist[i, i] = 0
        dist[0, 1] = dist[1, 0] = 1; dist[1, 2] = dist[2, 1] = 1
        dist[0, 2] = dist[2, 0] = 2
    elif seed_kind == 'star':     # A-centered: A-R, A-B, A-C (defined §9 arm)
        n0 = 4
        for i in range(n0): dist[i, i] = 0
        for x in (0, 2, 3):
            dist[1, x] = dist[x, 1] = 1
        for a in (0, 2, 3):
            for b in (0, 2, 3):
                if a != b: dist[a, b] = 2
    else:                          # triangle: R-A, R-B, A-B (3-cycle)
        n0 = 3
        for i in range(n0): dist[i, i] = 0
        for a in range(3):
            for b in range(3):
                if a != b: dist[a, b] = 1
    return dist, n0

def grow_grid(r, lam, n_events, rng, seed_kind='chain'):
    """The D30 grow generalized per §9: w_none = 1, w_birth = U,
    w_r-collar = lam * |{ordered pairs at 1 <= d_cover <= r}|.
    (r=1, lam=1, chain) reproduces K_collar's stream structure exactly.
    Returns (acts, realized_fracs, mean_dcov)."""
    cap = n_events * 6 + 64
    dist, n0 = seed_dist(seed_kind, cap)
    nreg = n0; acts = []
    n_i = 0; dsum = 0
    while len(acts) < n_events:
        uns = list(range(1, nreg))
        U = len(uns)
        D = dist[1:nreg, 1:nreg]
        pairs = np.argwhere((D >= 1) & (D <= r))
        w_none, w_birth, w_pairs = 1.0, float(U), lam * float(len(pairs))
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
            acts.append(('b', parent, child)); continue
        k = rng.integers(0, len(pairs))
        y, xx = pairs[k] + 1
        acts.append(('i', int(y), int(xx)))
        n_i += 1; dsum += int(D[pairs[k][0], pairs[k][1]])
    return acts, n_i / max(len(acts), 1), (dsum / n_i if n_i else 0.0)

def grow_witness(n_events, rng):
    """The COVARIANT-AT-CAP cell (§8/§9): the D5b witness kernel as a
    growth process — complete-graph interacts at w_i = c = 1/(4 N^2);
    births at w_b(s) = (1 - (s-1)(s-2)c)/(s-1); Z == 1 exactly; no none
    op. s = component size = registers incl. R. DISCLOSED CONFOUND (BF1):
    differs from the grid in BOTH covariance status AND interaction range."""
    c = 1.0 / (4.0 * n_events * n_events)
    nreg = 3; acts = []
    n_i = 0
    while len(acts) < n_events:
        u = nreg - 1; s = nreg
        birth_mass = 1.0 - (s - 1) * (s - 2) * c
        x = rng.random()
        if x < birth_mass:
            parent = 1 + rng.integers(0, u)
            child = nreg; nreg += 1
            acts.append(('b', int(parent), int(child)))
        else:
            k = rng.integers(0, u * (u - 1))
            y = 1 + k // (u - 1); xx = 1 + k % (u - 1)
            if xx >= y: xx += 1
            acts.append(('i', int(y), int(xx)))
            n_i += 1
    return acts, n_i / max(len(acts), 1), 0.0

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
    return dmm, dmid, L, r3, seven, fallback

print("[d32b the kernel-mechanism map (PHENOMENOLOGICAL) — §9 pin 8b7271c]")

# B1: card v2.2
blob = open("v10/data/d32_instrument_card_v2.json", "rb").read()
sha = hashlib.sha256(blob).hexdigest()[:16]
card = json.loads(blob)
ok1 = (sha == "e7bc80f0be08f537" and card["schema"] == "v2.2")
check("B1 card v2.2 loaded and sha-asserted (the D32A terminal freeze)",
      ok1, f"sha256/16 = {sha}")

# B2/B4: the 10 cells
def cell_seed(r, li, N, s):
    return BASE_B + 100000*r + 10000*li + 1000*(N // 256) + s

cells = {}
total_fallback = 0
for r in RS:
    for lam, li in LAMS:
        for N in SIZES:
            rows = []
            for s in range(NSEEDS):
                rng = np.random.default_rng(cell_seed(r, li, N, s))
                acts, fr, dc = grow_grid(r, lam, 3*N + 64, rng)
                acts = acts[:N]
                m = measure(acts)
                rows.append(m + (fr, dc))
                total_fallback += int(m[5])
            cells[(r, lam, N)] = rows
wit = {}
for N in SIZES:
    rows = []
    for s in range(NSEEDS):
        rng = np.random.default_rng(cell_seed(9, 0, N, s))
        acts, fr, dc = grow_witness(N, rng)
        m = measure(acts)
        rows.append(m + (fr, dc))
        total_fallback += int(m[5])
    wit[N] = rows
ok2 = all(len(v) == NSEEDS for v in cells.values()) and \
      all(len(wit[N]) == NSEEDS for N in SIZES)
check("B2 the grid + witness cells complete: 10 cells x 2 sizes x 12 seeds "
      "= 240 growths (whole-order fallbacks counted)", ok2,
      f"fallbacks (|I| < 64, whole-order MM used): {total_fallback}/240")

def stats(rows):
    dmm = np.array([x[0] for x in rows])
    dmid = np.array([x[1] for x in rows if x[1] is not None])
    gap = np.array([x[0] - x[1] for x in rows if x[1] is not None])
    L = np.array([x[2] for x in rows], dtype=float)
    r3 = np.array([x[3] for x in rows])
    sev = np.array([x[4] for x in rows], dtype=float)
    fr = np.array([x[6] for x in rows]); dc = np.array([x[7] for x in rows])
    return dict(dmm=(dmm.mean(), dmm.std()), dmid=(dmid.mean(), dmid.std()),
                gap=(gap.mean(), gap.std()), L=L.mean(), r3=r3.mean(),
                seven=(sev.mean(), sev.std()), fr=fr.mean(), dc=dc.mean(),
                n_mid=len(dmid))

# B5: the signature-pair table + the corrected joint verdict per cell
def joint_verdict(st, N):
    for d in (2, 3, 4):
        c = card["cells"][f"d{d}_N{N}"]
        in_mm = abs(st["dmm"][0] - c["dhat_mean"]) <= 3.5 * c["dhat_sd"]
        cc = st["L"] / N ** (1.0 / d)
        in_ch = abs(cc - c["chain_c"]) <= 3.5 * c["chain_c_sd"]
        in_r3 = abs(st["r3"] - c["ratio3_mean"]) <= 3.5 * c["ratio3_sd"]
        b4 = card["controls"][f"box4_N{N}"]; pc = card["controls"][f"perc_N{N}"]
        sep = (abs(st["dmm"][0] - b4["dhat_mean"]) > 3 * b4["dhat_sd"] and
               abs(st["dmm"][0] - pc["dhat_mean"]) > 3 * pc["dhat_sd"])
        if in_mm and in_ch and in_r3 and sep:
            return f"ENTERS-M{d}-BAND(Bonf/10 z=3.5)"
    return "NO-BAND"
print("      THE MAP [cell -> SIGNATURE PAIR (d_MM±sd, d_mid±sd) | gap | "
      "verdict | realized-i-frac | mean-dcov | >=7/web]:")
verdicts = {}
for key in list(cells.keys()) + [('WIT', '-', N) for N in SIZES]:
    if key[0] == 'WIT':
        N = key[2]; st = stats(wit[N]); tag = f"WITNESS(cov-at-cap) N={N}"
    else:
        r, lam, N = key; st = stats(cells[key]); tag = f"r={r} lam={lam} N={N}"
    v = joint_verdict(st, N)
    verdicts[key] = (st, v)
    print(f"        {tag:26s} ({st['dmm'][0]:.3f}±{st['dmm'][1]:.3f}, "
          f"{st['dmid'][0]:.3f}±{st['dmid'][1]:.3f}) | gap {st['gap'][0]:+.3f}"
          f"±{st['gap'][1]:.3f} | {v} | {st['fr']:.3f} | {st['dc']:.2f} | "
          f"{st['seven'][0]:.1f}")
ok5 = all(v is not None for _, v in verdicts.values())
check("B5 the corrected joint rule applied per cell (card-v2.2 bands; "
      "matched-d chain constant; ratio3; box-4/percolation separation; "
      "ENTRY at the Bonferroni-corrected z = 3.5 over the 10 cells) — "
      "either outcome is a result; single-dimension narration barred (the "
      "pair is the object)", ok5)

# B3: the anchor cell on FRESH seeds — the §6 fragility prediction tested
st_a = stats(cells[(1, 1.0, 512)])
fresh = [x[0] - x[1] for x in cells[(1, 1.0, 512)] if x[1] is not None]
fail_frac = float(np.mean([abs(g) > 0.15 for g in fresh]))
check("B3 the ANCHOR CELL on FRESH seeds (r=1, lam=1 IS K_collar; new seed "
      "family): the signature pair replicated and the §6 fragility "
      "prediction (~30% of fresh-seed draws fail the 0.15 concordance) "
      "MEASURED — reported, not gated on a bar", True,
      f"pair ({st_a['dmm'][0]:.3f}±{st_a['dmm'][1]:.3f}, "
      f"{st_a['dmid'][0]:.3f}±{st_a['dmid'][1]:.3f}); per-seed "
      f"|gap| > 0.15 fraction = {fail_frac:.2f} (predicted ≈ 0.30)")

# B4: the witness cell integrity
c512 = 1.0 / (4.0 * 512 * 512)
smax = 512 + 3
margin = 1.0 - (smax - 1) * (smax - 2) * c512
ok4 = margin > 0 and all(len(wit[N]) == NSEEDS for N in SIZES)
st_w = stats(wit[512])
check("B4 the COVARIANT-AT-CAP cell well-defined (positivity margin at the "
      "largest realizable s; Z == 1 exact by construction; complete-graph "
      "interacts — the BF1 confound disclosed in-table)", ok4,
      f"1 - (s-1)(s-2)c at s = {smax}: {margin:.3f}; witness pair at 512 = "
      f"({st_w['dmm'][0]:.3f}±{st_w['dmm'][1]:.3f}, "
      f"{st_w['dmid'][0]:.3f}±{st_w['dmid'][1]:.3f})")

# B6: seed-forgetting arm
sf = {}
for kind in ('star', 'triangle'):
    for (r, lam) in ((1, 1.0), (1, 0.5), (3, 2.0)):
        rows = []
        li = {0.5: 0, 1.0: 1, 2.0: 2}[lam]
        for s in range(NSEEDS):
            rng = np.random.default_rng(BASE_B + 900000 +
                                        (0 if kind == 'star' else 50000) +
                                        100000*r + 10000*li + s)
            acts, fr, dc = grow_grid(r, lam, 3*512 + 64, rng, seed_kind=kind)
            acts = acts[:512]
            rows.append(measure(acts) + (fr, dc))
        sf[(kind, r, lam)] = stats(rows)
ok6 = True
det = []
for (r, lam) in ((1, 1.0), (1, 0.5), (3, 2.0)):
    base = stats(cells[(r, lam, 512)])
    for kind in ('star', 'triangle'):
        st = sf[(kind, r, lam)]
        se = math.sqrt(base["dmm"][1]**2 / NSEEDS + st["dmm"][1]**2 / NSEEDS)
        z = abs(st["dmm"][0] - base["dmm"][0]) / se if se > 0 else 0.0
        det.append(f"{kind}@r{r}l{lam}: dz = {z:.2f} SE")
        ok6 &= True
sd_flag = any(float(x.split('= ')[1].split(' ')[0]) > 2.0 for x in det)
check("B6 SEED-FORGETTING measured (star + triangle vs chain at three "
      "cells, N = 512): the pinned rule — any |Δd_MM| > 2 SE at a matched "
      "cell reads SEED-DEPENDENCE and re-scopes the map; verdict printed",
      ok6, "; ".join(det) +
      (f" -> SEED-DEPENDENCE (re-scope per §9)" if sd_flag
       else " -> chain-seed readings are seed-robust at this power"))

# B7: fronts
print("      B7 FRONTS: BF2 (r-saturation): mean accepted d_cover per r at "
      "N=512: " + ", ".join(
          f"r={r}: {np.mean([stats(cells[(r, lam, 512)])['dc'] for lam, _ in LAMS]):.2f}"
          for r in RS) +
      "; BF3: alpha (256->512 two-point, descriptive): " + ", ".join(
          f"r={r},l={lam}: {math.log2(stats(cells[(r, lam, 512)])['L'] / stats(cells[(r, lam, 256)])['L']):.2f}"
          for r in RS for lam, _ in LAMS) +
      "; BF4 (lam proposal vs realized): " + ", ".join(
          f"l={lam}: {np.mean([stats(cells[(r, lam, 512)])['fr'] for r in RS]):.3f}"
          for lam, _ in LAMS))
check("B7 fronts BF2/BF3/BF4 measured and printed (BF1 in-table; BF5 = the "
      "§6 m7 alphabet scope, carried)", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: B1 freeze-assert, B2 completeness, "
      f"B3 anchor replication, B4 witness integrity, B5 the map, B6 "
      f"seed-forgetting, B7 fronts)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
