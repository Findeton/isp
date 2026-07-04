"""
v8 Paper 7 (manifoldlikeness flanks), receipt g1 -- THE ESTIMATOR-CONCORDANCE BATTERY.

Paper 4 Section 5 established the ESTIMATOR TRAP: a Kleitman-Rothschild 3-layer order
returns a manifold-plausible Myrheim-Meyer dimension (d_MM = 2.38), unmasked only by a
SECOND estimator (height 3 vs a sprinkling's ~2*sqrt(N)), and stated that certification
needs AGREEING estimators.  This receipt makes that quantitative:

  A FOUR-AXIS CERTIFICATE C(d):
    axis 1  d_MM        : Myrheim-Meyer ordering-fraction inversion (order-only),
    axis 2  height      : longest chain vs the reference band for dimension d,
    axis 3  d_mid       : midpoint-scaling dimension (largest interval halving),
    axis 4  abundance   : total-variation distance of the (N0..N5) interval-abundance
                          profile against reference sprinkling profiles at the same N.
  PASS(d) := all four axes land in the reference band for a COMMON d in {2, 3}.

  Bands are CONTROL-CALIBRATED: reference diamond sprinklings at the same N (the same
  held-out-coordinates methodology as receipts r1/r3: coordinates generate the controls
  and score the answers; every candidate is analyzed from its ORDER alone).

TESTED POPULATIONS (all order-only after generation):
  P1  2D diamond sprinklings          (positive control; must PASS at d=2)
  P2  3D diamond sprinklings          (positive control; must PASS at d=3)
  A1  KR 3-layer orders               (the paper-4 trap; fools axis 1, caught by 2)
  A2  THE DESIGNED ADVERSARY: KR-with-spine -- a KR block density-tuned to push d_MM
      toward 2 PLUS a disjoint chain of length ~2*sqrt(N) to fake the 2D height.
      Fools axes 1 AND 2 SIMULTANEOUSLY; the claim under test is that axes 3/4 catch it.
  A3  random bipartite 2-layer order  (layered negative control)

HONEST SCOPE: passing C is finite-N *evidence*, never sufficiency (the Hauptvermutung
and the faithfulness question remain open; paper 7 Section 2 states the limits, and the
existence of a designed adversary against ANY finite battery is left open, not denied).
A verdict either way on A2 is reportable; we do not manufacture a catch.

CALIBRATION HONESTY (review round 1): bands are min/max envelopes of 8 calibration
draws, widened (half-width x1.5, floor 0.15 for axes 1-2; x1.8, floor 0.4 for axis 3);
the axis-4 threshold is 3*max(tvmax, 0.01) and at d=2 the FLOOR dominates (calibrated
tvmax=0.0046 < 0.01).  Population verdicts are single-draw and seed-pinned
(default_rng(20260702)); a different seed or N could shift a band edge by ~1 unit.
The OPERATIVE (widened) bands are printed below alongside the raw envelopes.

Estimator provenance: Myrheim (1978)/Meyer (1988) ordering fraction, exact
f(d) = Gamma(d+1)Gamma(d/2)/(2 Gamma(3d/2)); midpoint scaling per Bombelli's thesis
line; height law in 2D = longest increasing subsequence ~ 2 sqrt(N)
(Vershik-Kerov / Logan-Shepp -- an IMPORT used only as commentary; the certificate
uses control bands, not the constant); interval abundances per Glaser-Surya.
"""

import os
import time
import numpy as np
import mpmath as mp

mp.mp.dps = int(os.environ.get("G1_DPS", "60"))
rng = np.random.default_rng(20260702)

CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))

def head(s):
    print("\n" + "=" * 80); print(s); print("=" * 80)

# ------------------------------------------------------------------ generators
def sprinkle_2d(N):
    """Diamond sprinkling of M^2 in lightcone coordinates: N iid uniform (u,v).
    Causal order = coordinatewise dominance."""
    uv = rng.random((N, 2))
    C = (uv[None, :, 0] > uv[:, None, 0]) & (uv[None, :, 1] > uv[:, None, 1])
    return C  # C[i,j] = True iff i < j in the order

def sprinkle_3d(N):
    """Diamond sprinkling of M^3 (causal diamond between (-1,0,0) and (1,0,0))."""
    pts = []
    while len(pts) < N:
        t = rng.uniform(-1, 1); x = rng.uniform(-1, 1); y = rng.uniform(-1, 1)
        if np.hypot(x, y) <= 1 - abs(t):
            pts.append((t, x, y))
    P = np.array(pts)
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.hypot(P[None, :, 1] - P[:, None, 1], P[None, :, 2] - P[:, None, 2])
    return (dt > 0) & (dt >= dr)

def kr_3layer(N, p=0.5):
    """Kleitman-Rothschild-type 3-layer order: layers N/4, N/2, N/4; each adjacent-layer
    pair related independently with probability p; transitive closure."""
    n1, n2 = N // 4, N // 2
    n3 = N - n1 - n2
    C = np.zeros((N, N), dtype=bool)
    L1 = np.arange(0, n1); L2 = np.arange(n1, n1 + n2); L3 = np.arange(n1 + n2, N)
    C[np.ix_(L1, L2)] = rng.random((n1, n2)) < p
    C[np.ix_(L2, L3)] = rng.random((n2, n3)) < p
    # transitive closure (one step suffices for 3 layers)
    C[np.ix_(L1, L3)] = (C[np.ix_(L1, L2)].astype(int) @ C[np.ix_(L2, L3)].astype(int)) > 0
    return C

def kr_with_spine(N, p, spine_len):
    """THE DESIGNED ADVERSARY: KR block (density p, tuned so d_MM ~ 2) plus a DISJOINT
    chain whose length is tuned to the DEFENDER'S calibrated 2D height band (the
    strongest form: the adversary knows the bands)."""
    m = int(spine_len)
    Nk = N - m
    C = np.zeros((N, N), dtype=bool)
    C[:Nk, :Nk] = kr_3layer(Nk, p)
    for i in range(Nk, N):
        C[i, i + 1:N] = True   # the chain
    return C

def bipartite_2layer(N, p=0.5):
    n1 = N // 2
    C = np.zeros((N, N), dtype=bool)
    C[:n1, n1:] = rng.random((n1, N - n1)) < p
    return C

# ------------------------------------------------------------------ estimators
def f_mm(d):
    d = mp.mpf(d)
    return mp.gamma(d + 1) * mp.gamma(d / 2) / (2 * mp.gamma(3 * d / 2))

def d_mm(C):
    """Myrheim-Meyer dimension from the ordering fraction (order-only)."""
    N = C.shape[0]
    r = 2.0 * C.sum() / (N * (N - 1))
    if r <= 0:
        return float("inf")
    try:
        return float(mp.findroot(lambda d: f_mm(d) - r, mp.mpf(2.0)))
    except Exception:
        # fallback scan
        ds = np.linspace(1.05, 6.0, 2000)
        vals = [abs(float(f_mm(d)) - r) for d in ds]
        return float(ds[int(np.argmin(vals))])

def height(C):
    """Longest chain (number of elements) by DP over a topological order."""
    N = C.shape[0]
    indeg = C.sum(axis=0).copy()          # Kahn-style topological order
    stack = [i for i in range(N) if indeg[i] == 0]
    topo = []
    indeg = indeg.astype(int)
    Clist = [np.nonzero(C[i])[0] for i in range(N)]
    while stack:
        v = stack.pop()
        topo.append(v)
        for w in Clist[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    L = np.ones(N, dtype=int)
    for v in topo:
        for w in Clist[v]:
            if L[v] + 1 > L[w]:
                L[w] = L[v] + 1
    return int(L.max())

def d_mid(C):
    """Midpoint-scaling dimension: take the comparable pair (x,y) with the largest
    order-interval I(x,y); the halving element m maximizes min(|I(x,m)|,|I(m,y)|);
    d = log2(|I(x,y)| / |I_half|).  Order-only."""
    N = C.shape[0]
    Ci = C.astype(np.int32)
    between = Ci @ Ci            # between[x,y] = sum_z C[x,z] C[z,y] = #{z: x<z<y}
    sizes = np.where(C, between, -1)
    x, y = np.unravel_index(np.argmax(sizes), sizes.shape)
    big = sizes[x, y]
    if big < 8:
        return float("nan")
    inner = np.nonzero(C[x] & C[:, y])[0]
    best = 0
    for m in inner:
        a = int((C[x] & C[:, m]).sum())
        b = int((C[m] & C[:, y]).sum())
        best = max(best, min(a, b))
    if best < 1:
        return float("nan")
    return float(np.log2((big + 2) / (best + 2)))   # +2: count inclusive endpoints, standard offset

def abundance_profile(C, kmax=5):
    """Normalized interval-abundance profile (N_0..N_kmax)/pairs, order-only."""
    Ci = C.astype(np.int32)
    between = Ci @ Ci
    pairs = C.sum()
    prof = np.array([np.sum(C & (between == k)) for k in range(kmax + 1)], dtype=float)
    return prof / max(pairs, 1)

def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())

# ------------------------------------------------------------------ battery
def analyze(C):
    return {"d_mm": d_mm(C), "H": height(C), "d_mid": d_mid(C),
            "prof": abundance_profile(C)}

def calibrate(N, n_ref=8):
    """Reference bands for d = 2, 3 at size N from fresh sprinklings."""
    bands = {}
    for d, gen in ((2, sprinkle_2d), (3, sprinkle_3d)):
        rows = [analyze(gen(N)) for _ in range(n_ref)]
        dmm = [r["d_mm"] for r in rows]; hh = [r["H"] for r in rows]
        dm = [r["d_mid"] for r in rows if r["d_mid"] == r["d_mid"]]
        prof = np.mean([r["prof"] for r in rows], axis=0)
        # in-family TV spread (each ref vs the mean profile)
        tvs = [tv(r["prof"], prof) for r in rows]
        bands[d] = {
            "dmm": (min(dmm), max(dmm)), "H": (min(hh), max(hh)),
            "dmid": (min(dm), max(dm)) if dm else (float("nan"),) * 2,
            "prof": prof, "tvmax": max(tvs),
        }
    return bands

def widen(lo, hi, frac=0.5, floor=0.15):
    mid, half = (lo + hi) / 2, (hi - lo) / 2
    half = max(half * (1 + frac), floor)
    return mid - half, mid + half

def certify(res, bands):
    """PASS(d) for d in {2,3}: all four axes inside (widened) reference bands."""
    verdicts = {}
    for d, b in bands.items():
        lo, hi = widen(*b["dmm"])
        ok1 = lo <= res["d_mm"] <= hi
        lo, hi = widen(*b["H"])
        ok2 = lo <= res["H"] <= hi
        if res["d_mid"] == res["d_mid"] and b["dmid"][0] == b["dmid"][0]:
            lo, hi = widen(*b["dmid"], frac=0.8, floor=0.4)
            ok3 = lo <= res["d_mid"] <= hi
        else:
            ok3 = False
        ok4 = tv(res["prof"], b["prof"]) <= 3.0 * max(b["tvmax"], 0.01)
        verdicts[d] = {"axes": (ok1, ok2, ok3, ok4), "pass": ok1 and ok2 and ok3 and ok4}
    return verdicts

def show(name, res, verdicts):
    v2, v3 = verdicts[2], verdicts[3]
    print(f"   {name:<26} d_MM={res['d_mm']:6.3f}  H={res['H']:4d}  "
          f"d_mid={res['d_mid'] if res['d_mid']==res['d_mid'] else float('nan'):6.3f}  "
          f"axes(d=2)={''.join('Y' if a else 'n' for a in v2['axes'])} "
          f"axes(d=3)={''.join('Y' if a else 'n' for a in v3['axes'])}  "
          f"PASS2={v2['pass']} PASS3={v3['pass']}")

# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    N = int(os.environ.get("G1_N", "480"))
    head(f"g1 -- ESTIMATOR-CONCORDANCE BATTERY (N = {N}; order-only after generation)")
    print("axes: d_MM inversion | height band | midpoint-scaling band | abundance-TV band")
    print("bands control-calibrated from fresh reference sprinklings (held-out coordinates)")

    # exact MM fractions (paper-4 anchors)
    head("CHECK 1 -- exact Myrheim-Meyer fractions (anchors of receipt r3)")
    vals = {1: mp.mpf(1), 2: mp.mpf(1) / 2, 3: mp.mpf(8) / 35, 4: mp.mpf(1) / 10}
    ok = all(abs(f_mm(d) - v) < mp.mpf(10) ** (-40) for d, v in vals.items())
    check("f(1)=1, f(2)=1/2, f(3)=8/35, f(4)=1/10 to 1e-40", ok)

    bands = calibrate(N)
    print(f"\n   raw bands:       d=2: dmm={tuple(round(x,3) for x in bands[2]['dmm'])} "
          f"H={bands[2]['H']} tvmax={bands[2]['tvmax']:.4f}")
    print(f"                    d=3: dmm={tuple(round(x,3) for x in bands[3]['dmm'])} "
          f"H={bands[3]['H']} tvmax={bands[3]['tvmax']:.4f}")
    for d in (2, 3):
        print(f"   operative bands: d={d}: dmm={tuple(round(x,3) for x in widen(*bands[d]['dmm']))} "
              f"H={tuple(round(x,2) for x in widen(*bands[d]['H']))} "
              f"TV_thresh={3*max(bands[d]['tvmax'],0.01):.4f} (floor-dominated: {bands[d]['tvmax']<0.01})")

    head("THE POPULATIONS")
    # positive controls (fresh, not the calibration draws)
    r_p1 = analyze(sprinkle_2d(N)); v_p1 = certify(r_p1, bands); show("P1 2D sprinkling", r_p1, v_p1)
    r_p2 = analyze(sprinkle_3d(N)); v_p2 = certify(r_p2, bands); show("P2 3D sprinkling", r_p2, v_p2)
    # the paper-4 trap
    r_a1 = analyze(kr_3layer(N)); v_a1 = certify(r_a1, bands); show("A1 KR 3-layer", r_a1, v_a1)
    # the designed adversary: tune p to push d_MM toward 2
    spine_len = int(round((bands[2]["H"][0] + bands[2]["H"][1]) / 2))
    best = None
    for p in np.linspace(0.15, 0.9, 16):
        Ct = kr_with_spine(N, p, spine_len)
        dm = d_mm(Ct)
        if best is None or abs(dm - 2.0) < abs(best[1] - 2.0):
            best = (p, dm, Ct)
    p_star, dmm_star, C_a2 = best
    r_a2 = analyze(C_a2); v_a2 = certify(r_a2, bands)
    show(f"A2 KR+spine (p={p_star:.2f})", r_a2, v_a2)
    r_a3 = analyze(bipartite_2layer(N)); v_a3 = certify(r_a3, bands); show("A3 bipartite 2-layer", r_a3, v_a3)

    head("CHECKS 2-9 -- the battery verdicts")
    check("P1 (2D sprinkling) certified at d=2", v_p1[2]["pass"],
          f"d_MM={r_p1['d_mm']:.3f}, H={r_p1['H']}")
    check("P2 (3D sprinkling) certified at d=3", v_p2[3]["pass"],
          f"d_MM={r_p2['d_mm']:.3f}, H={r_p2['H']}")
    check("P1 NOT certified at d=3 and P2 NOT at d=2 (bands separate dimensions)",
          (not v_p1[3]["pass"]) and (not v_p2[2]["pass"]))
    check("A1 (KR): d_MM alone is manifold-plausible (within [2,3.2] -- the trap)",
          2.0 <= r_a1["d_mm"] <= 3.2, f"d_MM={r_a1['d_mm']:.3f} (paper-4 anchor 2.38)")
    check("A1 (KR) REJECTED by the battery at both d=2 and d=3",
          not v_a1[2]["pass"] and not v_a1[3]["pass"],
          f"height axis: H={r_a1['H']} vs 2D band {bands[2]['H']}")
    fooled_two = (widen(*bands[2]["dmm"])[0] <= r_a2["d_mm"] <= widen(*bands[2]["dmm"])[1]) and \
                 (widen(*bands[2]["H"])[0] <= r_a2["H"] <= widen(*bands[2]["H"])[1])
    check("A2 (KR+spine) fools axis 1 AND axis 2 for d=2 simultaneously",
          fooled_two, f"d_MM={r_a2['d_mm']:.3f}, H={r_a2['H']} vs band {bands[2]['H']}")
    check("A2 (KR+spine) REJECTED by the full battery (axes 3/4 catch it)",
          not v_a2[2]["pass"] and not v_a2[3]["pass"],
          f"TV(d=2)={tv(r_a2['prof'], bands[2]['prof']):.4f} vs "
          f"TV_thresh(=3*max(tvmax,0.01))={3*max(bands[2]['tvmax'],0.01):.4f}; d_mid={r_a2['d_mid']:.3f}")
    check("A3 (bipartite) rejected at both dimensions",
          not v_a3[2]["pass"] and not v_a3[3]["pass"])

    head("CHECK 10 -- height law commentary (2D longest chain ~ 2 sqrt(N), import)")
    Hs = [height(sprinkle_2d(N)) for _ in range(4)]
    ratio = np.mean(Hs) / (2 * np.sqrt(N))
    check("2D height within 20% of the Vershik-Kerov 2*sqrt(N) (commentary anchor)",
          0.8 <= ratio <= 1.2, f"mean H={np.mean(Hs):.1f}, 2*sqrt(N)={2*np.sqrt(N):.1f}, ratio={ratio:.3f}")

    head("VERDICT")
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{'ALL CHECKS PASS' if npass == len(CHECKS) else 'CHECKS'} ({npass}/{len(CHECKS)})")
    for name, ok, _ in CHECKS:
        if not ok:
            print(f"   FAILED: {name}")
    print(f"[runtime {time.time()-t0:.1f}s; N={N}; dps={mp.mp.dps}]")

if __name__ == "__main__":
    main()
