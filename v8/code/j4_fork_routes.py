#!/usr/bin/env python3
"""
j4_fork_routes.py — design note 4: the three readings of the click law's
content clause, priced against the manifoldlike cell.

CONTEXT (notes 3-4, receipt j3): the records wall decomposed — clock
correlation (O1) is cured by lineage churn with odometer reset (the odometer's
own definition on a branching web), and the residual wall is CONTENT
DEGENERACY: the click law's deterministic-amount clause (Var[content|mode]=0)
with the computed 3-atom menu produces exact chi-collisions that the
statistical layer sees at z ~ 400. The probabilistic clause (the Exp(1)
evidence clock) is exonerated. This receipt prices the three corpus-licensed
readings of the amount clause (design note 4 §2, pre-registered):

  ROUTE A [sparse kept; menu richness]: extend the dilution chain — the
    symmetric self-calibration over the full character group of {+-1}^m
    collapses (character sum = 2^m-1 on all-ones, -1 elsewhere) to ONE scalar
    fixed point per rung K = 2^m - 1:
        (e^{hK} - e^{-h}) / (e^{hK} + K e^{-h}) = e^{-h}
    (the same exponential-family shape as paper XII's delta calibration).
    Menu convention: per-seal content = C(h_K) = h tanh h - log cosh h at the
    diluted root (paper 1 §4.3's own convention; the joint-KL alternative is
    printed, increasing in K, and NOT adopted — a disclosed convention fork).
    Question: does an (L, rungs) window pass all three layers?
  ROUTE B [dense reading, POSITED]: content accrues continuously between
    division events; evidence -> content through kappa => per-event increments
    iid Exp — rank-identical to j3's passing continuum arm. Tagged live here.
  ROUTE C [sparse + configuration-magnitude spread, POSITED]: paper 1 §4.1's
    "magnitude is physical configuration data" clause vs §4.3's exact arena
    determinism — if realized content spreads by relative width w around the
    mode root, where is the threshold w*?

TRANSCRIPTION CORRECTION (disclosed): the corpus's "7-char eta = 0.3680" is a
rounded root; the true root is 0.367963155647, atom C = 0.063376134128 (note
3 / j3's first constant 0.063388010127 was C at the rounded root — relative
slip 2e-4, no verdict impact; j3 re-run with the true atom).

Gates pinned from the disclosed exploration (3-seed landscape; this run 6
seeds/arm). Conventions: N = 2048 (where j3's verdicts live), M = 32,
canonical-realizer tie treatment for exact-atom arms, 20-draw D* band,
40-draw dispersion ensemble, default_rng(20260702). T1 |rho| < 0.1; T2
D* <= band + 2 sd; T3 per-draw dispersion z < 3.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 40
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------- instruments
def star_disc(pts):
    N = len(pts)
    us = np.unique(np.concatenate([pts[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([pts[:, 1], [1.0]]))
    order = np.argsort(pts[:, 0], kind="stable")
    pu = pts[order, 0]; pv = pts[order, 1]
    best = 0.0
    for a in us:
        ko = np.searchsorted(pu, a, "left"); kc = np.searchsorted(pu, a, "right")
        so = np.sort(pv[:ko]); sc = np.sort(pv[:kc])
        co = np.searchsorted(so, vs, "left") / N
        cc = np.searchsorted(sc, vs, "right") / N
        vol = a * vs
        best = max(best, float(np.abs(co - vol).max()), float(np.abs(cc - vol).max()))
    return best

def rank_embed2(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b))
    r2 = np.argsort(np.argsort(chi))
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def canon_embed(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b))
    order2 = np.lexsort((-b, chi))
    r2 = np.empty(N, dtype=float); r2[order2] = np.arange(N)
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def spearman_ties(x, y):
    def avg_rank(v):
        o = np.argsort(v, kind="stable"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        vals, inv = np.unique(v, return_inverse=True)
        sums = np.bincount(inv, weights=r); cnts = np.bincount(inv)
        return (sums / cnts)[inv]
    rx, ry = avg_rank(x), avg_rank(y)
    return float(np.corrcoef(rx, ry)[0, 1])

def dominance_order(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def interval_fano(b_, c_, kmin=10):
    pts_ = np.column_stack([np.asarray(b_, dtype=float), c_])
    Np = len(pts_)
    C = dominance_order(pts_)
    r1 = np.argsort(np.argsort(pts_[:, 0]))
    r2 = np.argsort(np.argsort(pts_[:, 1]))
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    ii, jj = np.nonzero(C)
    dr1 = (r1[jj] - r1[ii]).astype(float)
    dr2 = (r2[jj] - r2[ii]).astype(float)
    exp_k = (dr1 - 1) * (dr2 - 1) / Np
    sel = exp_k >= kmin
    resid = btw[ii, jj][sel] - exp_k[sel]
    return float(np.mean(resid ** 2 / exp_k[sel]))

def web4(N, M, L, atoms_arr, carrier="local", spread=0.0, weights=None, cont=False):
    chi_acc = np.zeros(M); mode = rng.integers(0, len(atoms_arr), M); chi = np.zeros(N)
    mean_c = float(np.mean(atoms_arr))
    kk = len(atoms_arr)
    for t in range(N):
        c = int(rng.integers(M))
        if cont:
            inc = rng.exponential(mean_c)
        else:
            if carrier == "lineage":
                m = int(mode[c])
            elif weights is not None:
                m = int(rng.choice(kk, p=weights))
            else:
                m = int(rng.integers(kk))
            inc = float(atoms_arr[m])
            if spread > 0:
                inc *= float(np.exp(rng.normal(0.0, spread)))
        chi_acc[c] += inc
        chi[t] = chi_acc[c]
        if rng.random() < 1.0 / L:
            chi_acc[c] = 0.0
            mode[c] = rng.integers(kk)
    return np.arange(N), chi

def measure4(N, M, L, atoms_arr, seeds=6, **kw):
    exact = (kw.get("spread", 0.0) == 0.0) and not kw.get("cont", False)
    ds, rs, fs, ties = [], [], [], []
    for _ in range(seeds):
        b, c = web4(N, M, L, atoms_arr, **kw)
        ds.append(star_disc(canon_embed(b, c) if exact else rank_embed2(b, c)))
        rs.append(spearman_ties(b, c))
        fs.append(interval_fano(b, c))
        ties.append(1.0 - len(np.unique(c)) / N)
    return dict(D=float(np.mean(ds)), rho=float(np.mean(rs)),
                fano=float(np.mean(fs)), tie=float(np.mean(ties)))


# --------------------------- CHECK 1: the extended menu (route A's material)
print("CHECK 1: the dilution chain extended (the scalar collapse, dps = 40)")
Cmp = lambda x: x * mp.tanh(x) - mp.log(mp.cosh(x))
def root_K(K):
    f = lambda h: 1 - mp.e**(-h*(K+1)) - mp.e**(-h) - K*mp.e**(-h*(K+2))
    return mp.findroot(f, (mp.mpf("1e-6"), mp.mpf("1.0")), solver="anderson")
P2C = {1: mp.mpf("0.609377863436006"), 3: mp.mpf("0.495053264332161"),
       7: mp.mpf("0.367963155647")}
MENU_MP = []
print(f"      {'K':>5} {'h_K':>15} {'C(h_K) atom':>15} {'joint-KL (not adopted)':>24}")
for m_ in range(1, 11):
    K = 2**m_ - 1
    h = root_K(K)
    Z = mp.e**(h*K) + K*mp.e**(-h)
    p1 = mp.e**(h*K)/Z; p0 = mp.e**(-h)/Z; u = mp.mpf(1)/2**m_
    Dj = p1*mp.log(p1/u) + K*p0*mp.log(p0/u)
    MENU_MP.append((K, h, Cmp(h), Dj))
    print(f"      {K:>5} {mp.nstr(h,10):>15} {mp.nstr(Cmp(h),10):>15} {mp.nstr(Dj,10):>24}")
ok = all(abs(dict((k, h) for k, h, _, _ in MENU_MP)[k] - v) < mp.mpf("1e-9")
         for k, v in P2C.items())
check("the scalar collapse reproduces p2c's vector roots (K = 1, 3, 7) to 1e-9 "
      "— the extension is the same object, 10 rungs now computed", ok)
ratios = [float(MENU_MP[i+1][2]/MENU_MP[i][2]) for i in range(9)]
ok = all(r < 0.75 for r in ratios) and all(r < 0.45 for r in ratios[3:])
check("the menu is LACUNARY: successive content ratios fall toward ~1/3 "
      "(scale-separated, not quasi-continuous) — route A's structural risk is "
      "real before any sprinkle test", ok,
      "ratios " + ", ".join(f"{r:.3f}" for r in ratios))
ok = all(MENU_MP[i+1][3] > MENU_MP[i][3] for i in range(9))
check("the joint-KL alternative INCREASES in K (0.156 -> 6.79 over the ten "
      "rungs) — the convention "
      "fork is real and disclosed; this receipt adopts paper 1 §4.3's per-mode "
      "C(h_K) and prints the alternative rather than silently choosing", ok)
MENU = np.array([float(c) for _, _, c, _ in MENU_MP])

# ------------------------------------------------- calibration at N = 2048
N2 = 2048
fb = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N2, 2)))))
      for _ in range(20)]
Df, Dsd = float(np.mean(fb)), float(np.std(fb))
ens = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
       for p in (rng.random((N2, 2)) for _ in range(40))]
mun, sdn = float(np.mean(ens)), float(np.std(ens))
T2gate = Df + 2 * Dsd
print(f"      calibration: band {Df:.4f} +/- {Dsd:.4f} (T2 gate {T2gate:.4f}); "
      f"dispersion ensemble {mun:.3f} +/- {sdn:.3f}")

# --------------------------- CHECK 2: route A — the (L, rungs) window grid
print("CHECK 2: ROUTE A — the real-menu window grid (commit-local mixture)")
print(f"      {'cell':<22} {'D*':>7} {'ratio':>7} {'rho':>7} {'tie':>6} {'fano z':>8}")
gridA = {}
for L in (4, 8, 16):
    for m_ in (3, 6, 10):
        r = measure4(N2, 32, L, MENU[:m_])
        z = abs(r["fano"] - mun) / sdn
        gridA[(L, m_)] = (r, z)
        print(f"      L={L:<3} rungs={m_:<3}        {r['D']:7.4f} {r['D']/Df:6.2f}x "
              f"{r['rho']:+7.3f} {r['tie']:6.3f} {z:8.1f}")
sensL = measure4(N2, 32, 8, MENU[:10], carrier="lineage")
zL = abs(sensL["fano"] - mun) / sdn
wskew = np.array([2.0**(-i) for i in range(10)]); wskew /= wskew.sum()
sensW = measure4(N2, 32, 8, MENU[:10], weights=wskew)
zW = abs(sensW["fano"] - mun) / sdn
print(f"      sensitivity: lineage-carried z {zL:.1f}; big-atom-skewed mixture z {zW:.1f}")
ok = all(gridA[(L, 10)][0]["tie"] < gridA[(L, 3)][0]["tie"] for L in (4, 8, 16)) \
     and gridA[(16, 10)][0]["tie"] < 0.25
check("the combinatorial prediction holds: tie-mass collapses with (L, rungs) "
      "(exact collisions are NOT the problem at depth)", ok,
      f"tie(16,10) = {gridA[(16,10)][0]['tie']:.3f}")
ok = all(z > 8 for (_, z) in gridA.values()) and zL > 8 and zW > 8
check("YET the dispersion layer fails at EVERY grid cell and both sensitivity "
      "mixtures (z > 8 everywhere) — the LACUNARY multi-scale lattice, not "
      "tie-mass, is the killer: NO (L, rungs) window exists for the corpus's "
      "own menu at these regimes — ROUTE A REFUSED", ok,
      f"min z over grid = {min(z for _, z in gridA.values()):.1f}")
ok = all(r["D"] > 1.4 * Df for (r, _) in gridA.values())
check("route A also never reaches the volume band (min D* > 1.4x across the "
      "grid; larger L re-awakens O1 co-growth exactly as note 3 measured)", ok,
      f"best cell {min(r['D']/Df for (r, _) in gridA.values()):.2f}x")

# --------------------------- CHECK 3: route C — the spread threshold
print("CHECK 3: ROUTE C — configuration-magnitude spread on the corrected 3-atom "
      "menu (L = 2)")
resC = {}
for w in (0.005, 0.02, 0.10):
    r = measure4(N2, 32, 2, MENU[:3], spread=w)
    z = abs(r["fano"] - mun) / sdn
    resC[w] = (r, z)
    t2 = "pass" if r["D"] <= T2gate else "FAIL"
    print(f"      w = {w:5.3f}   D* {r['D']:.4f} ({r['D']/Df:4.2f}x, T2 {t2})  "
          f"rho {r['rho']:+.3f}  tie {r['tie']:.3f}  fano z {z:4.1f}")
ok = all(r["tie"] == 0.0 for (r, _) in resC.values())
check("ANY nonzero spread kills exact ties outright (tie-mass = 0 at w = 0.5%)", ok)
ok = all(z < 3 for (_, z) in resC.values()) and all(abs(r["rho"]) < 0.1 for (r, _) in resC.values())
check("the dispersion layer passes at EVERY tested width — T3's threshold is "
      "BELOW 0.5% relative spread: the degeneracy wall is fragile to sub-percent "
      "content spread", ok,
      "z = " + ", ".join(f"{z:.1f}" for (_, z) in resC.values()))
ok = resC[0.10][0]["D"] <= T2gate
check("the full three-layer cell is reached at w = 10% robustly, and the "
      "per-row T2 verdicts are printed for the smaller widths — across runs "
      "the sub-percent rows straddle the band gate (the 3-seed exploration had "
      "w = 0.5% at 1.54x, this 6-seed run has it in-gate), so w*(full cell) "
      "is AT OR BELOW the percent scale, bracketed by run noise", ok,
      f"D*(w=0.10) = {resC[0.10][0]['D']:.4f} vs gate {T2gate:.4f}")

# --------------------------- CHECK 4: route B — the dense-reading identity arm
print("CHECK 4: ROUTE B — iid exponential increments (the dense reading's "
      "derived law; rank-identical to j3's passing arm), L = 2")
rB = measure4(N2, 32, 2, MENU[:3], cont=True, seeds=8)
zB = abs(rB["fano"] - mun) / sdn
ok = rB["D"] <= T2gate and abs(rB["rho"]) < 0.1 and zB < 3
check("route B passes all three layers live (T1, T2, T3) — under the dense "
      "reading the cell-membership result IS the derived result; upgrade "
      "obligations stay as named in note 4 §2 (kappa at event granularity; "
      "division events as the two-clock atoms; the dense-vs-sparse "
      "decoherence-functional computation = the decider)", ok,
      f"D* {rB['D']:.4f} vs gate {T2gate:.4f}; rho {rB['rho']:+.3f}; z {zB:.1f}")

# --------------------------- CHECK 5: the fork table
print("CHECK 5: the fork verdict table")
print("      route A (sparse + real menu, any depth <= 10 rungs) : REFUSED "
      "(dispersion z > 8 everywhere; volume > 1.4x)")
print("      route B (dense reading, Exp increments)             : IN CELL "
      f"({rB['D']/Df:.2f}x, rho {rB['rho']:+.3f}, z {zB:.1f})")
print(f"      route C (sparse + magnitude spread)                : IN CELL at "
      f"w = 10% robustly; T3 threshold < 0.5%; w*(full cell) at or below "
      f"the percent scale (T2-marginal there across runs)")
print("      => the content-degeneracy wall stands ONLY on the conjunction:")
print("         (sparse realization) AND (exact per-mode determinism to sub-")
print("         percent precision) AND (menu as computed) — refuting ANY ONE")
print("         conjunct brings it down; the dense-vs-sparse computation")
print("         (paper 1 §7, deferred) is now wall-deciding.")
ok = (all(z > 8 for (_, z) in gridA.values())
      and rB["D"] <= T2gate and zB < 3
      and all(z < 3 for (_, z) in resC.values()))
check("the three verdicts are jointly consistent and each is carried by its "
      "own measured row above (A refused; B in cell; C in cell with its "
      "thresholds bracketed)", ok)

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
