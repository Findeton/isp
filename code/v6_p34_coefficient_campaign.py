# Paper 34 campaign: computing the neutrino-step coefficient C instead of
# leaving it free.
#
# Setup: the program's undressed spectrum point is m1:m2:m3 = eps:sqrt(eps):1
# (registered, expected ~5.6 sigma dead at JUNO).  The publishable-campaign
# referees proved the FREE-coefficient form is unfalsifiable (covers the
# exponent axis).  The only honest escape: make C COMPUTABLE.  This campaign:
#   N1  no-universal-dressing lemma (numeric demo): rung-multiplicative
#       dressing cancels in ratios -> C != 1 needs matrix/sector structure.
#   A   ladder-seesaw enumeration: if the ladder lives on the SEAM entries
#       (Dirac Yukawa Y, Majorana M) with unit coefficients (signs allowed),
#       the physical coefficient C is a COMPUTABLE function of the discrete
#       texture.  Enumerate all 2x2 sector textures (exponents on the
#       half-integer ladder, 0..2, plus exact zeros), filter by (i) the
#       step lands on the sqrt(eps) rung, (ii) the 2-3 mixing is large
#       (observed 40-50 deg), and report the attainable C set, the
#       minimal-cost selections, and the look-elsewhere menu count.
#   B   charged-sector test: required charged dressings from measured
#       exponents; can the same unit-seam mechanism produce them?
#   C   JUNO separability of the discrete C candidates.
# Canonical: /tmp/v6_p34_campaign.out (bit-identical rerun required)

import itertools
import numpy as np

EPS = 0.0318
SQE = np.sqrt(EPS)

# ---------- target: what C does the data need? ----------
S_MEAS, S_ERR = 0.17179, 0.00260
C2 = (S_MEAS**2 * (1 - EPS**2) + EPS**2) / EPS
C_NEED = np.sqrt(C2)
DCDS = S_MEAS * (1 - EPS**2) / (C_NEED * EPS)
C_ERR = DCDS * S_ERR
S_JUNO_ERR = 0.5 * np.hypot(0.006, 0.005) * S_MEAS
C_JUNO_ERR = DCDS * S_JUNO_ERR
print("== TARGET ==")
print(f"  C_needed = {C_NEED:.5f} +- {C_ERR:.5f} (today)"
      f"  +- {C_JUNO_ERR:.5f} (JUNO-class)")
print(f"  bare point C = 1: {(1-C_NEED)/C_ERR:+.2f} sigma today,"
      f" {(1-C_NEED)/C_JUNO_ERR:+.2f} sigma at JUNO (centrals held)")

# ---------- N1: universal dressing cancels ----------
print("\n== N1: no-universal-dressing (numeric demo) ==")
rng = np.random.default_rng(34)
for g in rng.uniform(-2, 2, 3):
    m = np.array([EPS, SQE, 1.0]) * np.exp(g)        # common factor
    print(f"  common dressing e^g, g={g:+.3f}:"
          f" m2/m3 = {m[1]/m[2]:.6f} = sqrt(eps) exactly"
          f" ({abs(m[1]/m[2]-SQE):.1e})")
# rung-dependent smooth dressing D(x)=e^{g x} shifts the ratio by e^{g/2}:
# one FREE parameter again unless g is derived -> fitting g is not allowed.

# ---------- A: ladder-seesaw enumeration (2x2 sector) ----------
# Y = [[s1 e^a, s2 e^b],[s3 e^c, s4 e^d]], M = [[e^p, s5 e^r],[s5 e^r, e^q]]
# (overall mass scales drop out of the ratio; e^x means EPS**x; exponent
# None = exact zero = absent seam).  m_nu = Y M^-1 Y^T; masses = |eigs|;
# C = (lam_small/lam_big)/sqrt(eps); mixing from the diagonalizing angle.
EXPOS = [0.0, 0.5, 1.0, 1.5, 2.0, None]


def val(x):
    return 0.0 if x is None else EPS**x


def cost(xs):
    return sum(x for x in xs if x is not None)


def nseams(xs):
    return sum(1 for x in xs if x is not None)


results = []
sign_sets = list(itertools.product([1, -1], repeat=3))  # s2, s3, s5 (s1=s4=+1 wlog)
for a, b, c, d in itertools.product(EXPOS, repeat=4):
    for p, q, r in itertools.product(EXPOS, repeat=3):
        if p is None or q is None:
            continue                     # need invertible M (diagonal present)
        for s2, s3, s5 in sign_sets:
            Y = np.array([[val(a), s2 * val(b)],
                          [s3 * val(c), val(d)]])
            M = np.array([[val(p), s5 * val(r)],
                          [s5 * val(r), val(q)]])
            det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
            if abs(det) < 1e-300:
                continue
            Minv = np.array([[M[1, 1], -M[0, 1]],
                             [-M[1, 0], M[0, 0]]]) / det
            m = Y @ Minv @ Y.T
            # symmetric by construction; eigendecompose
            w, V = np.linalg.eigh(m)
            lam = np.abs(w)
            if lam.max() < 1e-300 or lam.min() < 1e-300:
                continue
            ratio = lam.min() / lam.max()
            Cval = ratio / SQE
            if not (0.5 <= Cval <= 2.0):
                continue                 # not on the sqrt(eps) rung
            # mixing angle of the heavy eigenvector
            k = int(np.argmax(lam))
            th = np.degrees(np.arctan2(abs(V[0, k]), abs(V[1, k])))
            th = min(th, 90 - th) + min(45.0, 45.0)  # fold to [0,45]; keep angle to closest axis
            th = np.degrees(np.arctan2(abs(V[0, k]), abs(V[1, k])))
            th = th if th <= 45 else 90 - th
            results.append((Cval, th, cost((a, b, c, d, p, q, r)),
                            nseams((a, b, c, d, p, q, r)),
                            (a, b, c, d, p, q, r, s2, s3, s5)))

results.sort(key=lambda t: (t[3], t[2], abs(t[0] - 1)))
print(f"\n== A: ladder-seesaw enumeration ==")
print(f"  textures on the sqrt(eps) rung (C in [0.5,2]): {len(results)}")

big = [t for t in results if 35.0 <= t[1] <= 55.0]
print(f"  ... with LARGE 2-3 mixing (35-55 deg, as observed): {len(big)}")

# distinct C values (rounded) attainable with large mixing
import collections
Cset = collections.Counter(round(t[0], 4) for t in big)
print(f"  distinct C values (1e-4 grid) with large mixing: {len(Cset)}")

# minimal-cost selections under two minimality readings
for label, key in [("fewest seams, then cheapest", lambda t: (t[3], t[2])),
                   ("cheapest total exponent", lambda t: (t[2], t[3]))]:
    bigs = sorted(big, key=key)
    k0 = key(bigs[0])
    mins = [t for t in bigs if key(t) == k0]
    Cs = sorted(set(round(t[0], 4) for t in mins))
    print(f"  minimality = {label}: {len(mins)} minimal textures,"
          f" C in {Cs[:8]}{'...' if len(Cs) > 8 else ''}")
    for t in mins[:4]:
        a, b, c, d, p, q, r, s2, s3, s5 = t[4]
        print(f"     C = {t[0]:.4f}  theta = {t[1]:.1f} deg  cost {t[2]}"
              f"  seams {t[3]}  Y-expo ({a},{b},{c},{d})"
              f" M-expo ({p},{q},{r}) signs ({s2},{s3},{s5})")

# look-elsewhere: how much of the C in [0.5,2] axis do large-mixing
# textures cover within +-2 sigma(today) of ANY attainable value?
grid = np.linspace(0.5, 2.0, 30001)
cov = np.zeros_like(grid, bool)
for cval in Cset:
    cov |= np.abs(grid - cval) < 2 * C_ERR
print(f"  menu coverage of C in [0.5,2] within 2 sigma(today): "
      f"{cov.mean()*100:.0f}%  (within 2 sigma(JUNO): ", end="")
covJ = np.zeros_like(grid, bool)
for cval in Cset:
    covJ |= np.abs(grid - cval) < 2 * C_JUNO_ERR
print(f"{covJ.mean()*100:.0f}%)")

# the candidates near the needed value, with their sigma distances
near = sorted({round(t[0], 4) for t in big if abs(t[0] - C_NEED) < 3 * C_ERR})
print(f"  attainable C within 3 sigma(today) of C_needed: {len(near)} values")
hits = {}
for t in big:
    cv = round(t[0], 4)
    if abs(t[0] - C_NEED) < 2 * C_ERR:
        if cv not in hits or (t[3], t[2]) < (hits[cv][3], hits[cv][2]):
            hits[cv] = t
for cv in sorted(hits):
    t = hits[cv]
    print(f"     C = {cv:.4f}: {((cv-C_NEED)/C_ERR):+.2f} sigma today,"
          f" {((cv-C_NEED)/C_JUNO_ERR):+.2f} sigma JUNO;"
          f" min seams {t[3]}, min cost {t[2]}")

# closed-form anchors for the writeup
Cvals = np.array(sorted(Cset))
for k in (0, 1, 2, 3):
    Ck = np.sqrt(max(1 - k * EPS, 0))
    dmin = float(np.min(np.abs(Cvals - Ck)))
    print(f"  anchor sqrt(1-{k}eps) = {Ck:.5f}:"
          f" {((Ck-C_NEED)/C_ERR):+.2f} sigma today,"
          f" {((Ck-C_NEED)/C_JUNO_ERR):+.2f} sigma JUNO;"
          f" nearest attainable {dmin:.4f} away")

# the attainable values closest to C_needed, with JUNO verdicts
print("  five attainable C closest to C_needed:")
best = {}
for t in big:
    cv = round(t[0], 4)
    if cv not in best or (t[3], t[2]) < (best[cv][3], best[cv][2]):
        best[cv] = t
for cv in sorted(best, key=lambda c: abs(c - C_NEED))[:5]:
    t = best[cv]
    print(f"     C = {cv:.4f}: {((cv-C_NEED)/C_ERR):+.2f} s(today),"
          f" {((cv-C_NEED)/C_JUNO_ERR):+.2f} s(JUNO);"
          f" seams {t[3]} cost {t[2]}"
          f"  Y ({t[4][0]},{t[4][1]},{t[4][2]},{t[4][3]})"
          f" M ({t[4][4]},{t[4][5]},{t[4][6]})"
          f" signs ({t[4][7]},{t[4][8]},{t[4][9]})")
n_in = sum(1 for c in Cvals if abs(c - C_NEED) < 2 * C_JUNO_ERR)
print(f"  attainable values within 2 sigma(JUNO) of C_needed: {n_in}")
print(f"  -> if JUNO confirms today's centrals, the texture class"
      f" {'RETAINS' if n_in else 'is EXCLUDED:'}"
      f" {'candidates' if n_in else 'no attainable C within 2 sigma'}")

# ---------- B: charged-sector test ----------
print("\n== B: charged-sector dressing requirement ==")
me, mmu, mtau = 0.51099895e-3, 105.6583755e-3, 1.77686
for name, ratio, rungs in [("m_e/m_mu", me / mmu, (1.5,)),
                           ("m_mu/m_tau", mmu / mtau, (0.5, 1.0))]:
    x = np.log(ratio) / np.log(EPS)
    for rung in rungs:
        Creq = ratio / EPS**rung
        keq = (1 - Creq**2) / EPS
        dmin = float(np.min(np.abs(Cvals - Creq)))
        cb = float(Cvals[int(np.argmin(np.abs(Cvals - Creq)))])
        print(f"  {name}: x = {x:.3f}; vs rung {rung}:"
              f" C_req = {Creq:.4f} (sqrt(1-k eps) k = {keq:+.1f});"
              f" nearest attainable {cb:.4f} (off by {dmin/Creq*100:.1f}%)")
print("  charged masses are measured to <1e-4 relative, so a texture")
print("  'hit' must match C_req essentially exactly; the gaps above are")
print("  percent-level or worse -> within this texture class (2x2,")
print("  exponents <= 2, unit coefficients) the charged steps are NOT")
print("  reproduced.  The sector criterion is therefore a NAMED")
print("  HYPOTHESIS, not a derivation: charged masses pass through EWSB")
print("  seams (additional uncomputed dressing); the seesaw step is")
print("  pre-EWSB ('D-shield').  Until the EWSB dressing is computed,")
print("  the charged sector neither confirms nor calibrates the")
print("  mechanism - counted against the program, not for it.")

# ---------- C: JUNO separability of the candidate menu ----------
print("\n== C: JUNO separability ==")
anchors = [1.0, np.sqrt(1 - EPS), np.sqrt(1 - 2 * EPS)]
names = ["bare C=1", "sqrt(1-eps)", "sqrt(1-2eps)"]
for (n1, c1), (n2, c2) in itertools.combinations(zip(names, anchors), 2):
    print(f"  {n1} vs {n2}: |dC| = {abs(c1-c2):.4f}"
          f" = {abs(c1-c2)/C_JUNO_ERR:.1f} JUNO sigma")
S_pred = {n: float(np.sqrt(EPS * (c**2 - EPS) / (1 - EPS**2)))
          for n, c in zip(names, anchors)}
for n, s in S_pred.items():
    print(f"  S_pred[{n}] = {s:.5f}  (today: {(s-S_MEAS)/S_ERR:+.2f} sigma)")

# ---------- D: the m1-coefficient smearing (3x3 honesty bound) ----------
# S^2 = (C^2 eps - C1^2 eps^2) / (1 - C1^2 eps^2) with m1 = C1 eps m3.
# The 2x2 analysis pins C; C1 (the m1 coefficient) is NOT pinned by it.
print("\n== D: m1-coefficient smearing of the JUNO exclusion ==")
def S_of(C, C1):
    return float(np.sqrt((C**2 * EPS - C1**2 * EPS**2) /
                         (1 - C1**2 * EPS**2)))
S_ref = S_of(1.0, 1.0)
for C1 in (0.0, 0.5, 1.0, 1.5, 2.0):
    s = S_of(1.0, C1)
    print(f"  C1 = {C1}: S(C=1) = {s:.5f}  shift {100*(s-S_ref)/S_ref:+.2f}%"
          f" = {(s-S_ref)/S_JUNO_ERR:+.2f} JUNO sigma")
# effective widening of the C band if C1 is only known to [0, 2]
dS_lo, dS_hi = S_of(1, 2.0) - S_ref, S_of(1, 0.0) - S_ref
widen = max(abs(dS_lo), abs(dS_hi)) * DCDS
print(f"  C1 in [0,2] smears the inferred 2-3 coefficient by +-{widen:.4f}")
n_in_w = sum(1 for c in Cvals
             if abs(c - C_NEED) < 2 * C_JUNO_ERR + widen)
print(f"  attainable C within (2 sigma_JUNO + smear) of C_needed: {n_in_w}")
print("  -> the JUNO-era class exclusion is CONDITIONAL on pinning C1;")
print("     the full 3x3 enumeration is the named next receipt.")

# ---------- E: 3x3 joint (C, C1) sampling with PMNS constraints ----------
# Full exhaustion is 6^15 x signs (infeasible); we SAMPLE (seeded, 2M draws)
# and report attainability LOWER bounds, with the exhaustive 3x3 as the
# named next receipt.  Premise (named): charged-lepton rotation ~ diagonal,
# so the PMNS matrix is the neutrino diagonalizer.  NO spectrum ordering.
print("\n== E: 3x3 joint (C, C1) sampled campaign ==")
rng3 = np.random.default_rng(3434)
N_DRAW = 2_000_000
GRID = np.array([0.0, 0.5, 1.0, 1.5, 2.0, np.inf])   # inf = absent seam
CHUNK = 100_000
kept = []          # (C, C1, S_pred, th23, th12, Ue3, cost, seams)
for start in range(0, N_DRAW, CHUNK):
    n = min(CHUNK, N_DRAW - start)
    ey = GRID[rng3.integers(0, 6, (n, 3, 3))]
    em_d = GRID[rng3.integers(0, 5, (n, 3))]          # M diagonal: finite
    em_o = GRID[rng3.integers(0, 6, (n, 3))]          # M off-diag (12,13,23)
    sy = rng3.choice([1.0, -1.0], (n, 3, 3))
    sm = rng3.choice([1.0, -1.0], (n, 3))
    Y = sy * EPS**ey
    Y[ey == np.inf] = 0.0
    M = np.zeros((n, 3, 3))
    M[:, 0, 0], M[:, 1, 1], M[:, 2, 2] = (EPS**em_d[:, 0],
                                          EPS**em_d[:, 1],
                                          EPS**em_d[:, 2])
    off = sm * EPS**em_o
    off[em_o == np.inf] = 0.0
    M[:, 0, 1] = M[:, 1, 0] = off[:, 0]
    M[:, 0, 2] = M[:, 2, 0] = off[:, 1]
    M[:, 1, 2] = M[:, 2, 1] = off[:, 2]
    dets = np.linalg.det(M)
    ok = np.abs(dets) > 1e-200
    if not ok.any():
        continue
    Yk, Mk = Y[ok], M[ok]
    eyk, emdk, emok = ey[ok], em_d[ok], em_o[ok]
    mnu = Yk @ np.linalg.inv(Mk) @ np.transpose(Yk, (0, 2, 1))
    w, V = np.linalg.eigh(mnu)
    lam = np.abs(w)
    order = np.argsort(lam, axis=1)
    l1 = np.take_along_axis(lam, order[:, 0:1], 1)[:, 0]
    l2 = np.take_along_axis(lam, order[:, 1:2], 1)[:, 0]
    l3 = np.take_along_axis(lam, order[:, 2:3], 1)[:, 0]
    good = l3 > 1e-200
    Cv = np.where(good, l2 / np.maximum(l3, 1e-300) / SQE, 0)
    C1v = np.where(good, l1 / np.maximum(l3, 1e-300) / EPS, 0)
    v3 = np.take_along_axis(V, order[:, None, 2:3], 2)[:, :, 0]
    v2 = np.take_along_axis(V, order[:, None, 1:2], 2)[:, :, 0]
    Ue3 = np.abs(v3[:, 0])
    th23 = np.degrees(np.arctan2(np.abs(v3[:, 1]), np.abs(v3[:, 2])))
    th12 = np.degrees(np.arctan2(np.abs(v2[:, 0]), np.abs(v2[:, 1])))
    th23 = np.where(th23 > 90, 180 - th23, th23)
    sel = (good & (Cv > 0.5) & (Cv < 2.0) & (C1v < 3.0)
           & (th23 > 35) & (th23 < 55)
           & (th12 > 25) & (th12 < 40) & (Ue3 < 0.3))
    if not sel.any():
        continue
    cost3 = (np.where(np.isinf(eyk), 0, eyk).sum((1, 2))
             + emdk.sum(1) + np.where(np.isinf(emok), 0, emok).sum(1))
    seams3 = ((~np.isinf(eyk)).sum((1, 2)) + 3
              + (~np.isinf(emok)).sum(1))
    Sp = np.sqrt(np.maximum(
        (Cv**2 * EPS - C1v**2 * EPS**2) / (1 - C1v**2 * EPS**2), 0))
    for i in np.where(sel)[0]:
        kept.append((float(Cv[i]), float(C1v[i]), float(Sp[i]),
                     float(th23[i]), float(th12[i]), float(Ue3[i]),
                     float(cost3[i]), int(seams3[i])))
print(f"  draws {N_DRAW:,}; PMNS-compatible NO-spectrum textures on the"
      f" rung: {len(kept):,}")
today_ok = [k for k in kept if abs(k[2] - S_MEAS) < 2 * S_ERR]
juno_ok = [k for k in kept if abs(k[2] - S_MEAS) < 2 * S_JUNO_ERR]
print(f"  consistent with S today (2 sigma): {len(today_ok):,}")
print(f"  would SURVIVE a confirmed-central JUNO (2 sigma_JUNO):"
      f" {len(juno_ok):,}")
for label, pool in [("cheapest today-consistent", today_ok),
                    ("cheapest JUNO survivor", juno_ok)]:
    if pool:
        t = min(pool, key=lambda k: (k[7], k[6]))
        print(f"  {label}: C = {t[0]:.4f} C1 = {t[1]:.4f}"
              f" S_pred = {t[2]:.5f} ({(t[2]-S_MEAS)/S_ERR:+.2f} s today)"
              f" th23 {t[3]:.0f} th12 {t[4]:.0f} |Ue3| {t[5]:.2f}"
              f" seams {t[7]} cost {t[6]:.1f}")
# is the (C ~ 1, C1 ~ 1.5) degeneracy realized?
deg = [k for k in kept if abs(k[0] - 1) < 0.02 and 1.3 < k[1] < 1.7]
print(f"  textures realizing the bare-rung + heavy-m1 degeneracy"
      f" (C ~ 1, C1 in [1.3, 1.7]): {len(deg):,}")
if deg:
    t = min(deg, key=lambda k: (k[7], k[6]))
    print(f"     cheapest: C = {t[0]:.4f} C1 = {t[1]:.4f}"
          f" S_pred = {t[2]:.5f} ({(t[2]-S_MEAS)/S_ERR:+.2f} s today,"
          f" {(t[2]-S_MEAS)/S_JUNO_ERR:+.2f} s JUNO)"
          f" seams {t[7]} cost {t[6]:.1f}")

# ---------- F: STATUS UPDATE with JUNO first data (2026-06-11) ----------
# JUNO first measurement (arXiv:2511.14593; Nature 654, 343 (2026)):
# dm21 = (7.50 +- 0.12) e-5 (NO), 59.1 days.  dm31 still global-fit.
print("\n== F: JUNO-first-data update ==")
dm21, e21 = 7.50e-5, 0.12e-5
dm31, e31 = 2.511e-3, 0.027e-3
S_J = float(np.sqrt(dm21 / dm31))
sS_J = 0.5 * float(np.hypot(e21 / dm21, e31 / dm31)) * S_J
print(f"  S = {S_J:.5f} +- {sS_J:.5f}  (was 0.17179 +- 0.00260)")
S_pred0 = float(np.sqrt(EPS / (1 + EPS)))
print(f"  registered point {S_pred0:.5f}: {(S_pred0-S_J)/sS_J:+.2f} sigma"
      f"  (was +1.45); needed dm21 = {S_pred0**2*dm31*1e5:.3f}e-5 ->"
      f" {(S_pred0**2*dm31-dm21)/e21:+.2f} sigma from JUNO's value")
C2_J = (S_J**2 * (1 - EPS**2) + EPS**2) / EPS
C_NEED_J = float(np.sqrt(C2_J))
C_ERR_J = float(S_J * (1 - EPS**2) / (C_NEED_J * EPS) * sS_J)
print(f"  C_needed = {C_NEED_J:.5f} +- {C_ERR_J:.5f}  (was 0.97924 +- 0.01433)")
for cv, tag in [(1.0, "bare C=1 (minimal texture)"),
                (0.9919, "nearest attainable 2x2"),
                (float(np.sqrt(1-EPS)), "sqrt(1-eps) anchor (NOT attainable)")]:
    print(f"    {tag}: C = {cv:.4f} -> {(cv-C_NEED_J)/C_ERR_J:+.2f} sigma vs JUNO-now")
# m1 degeneracy: C1 needed to reconcile bare rung with JUNO-now central
lo, hi = 0.0, 2.0
for _ in range(60):
    mid = 0.5 * (lo + hi)
    s = float(np.sqrt((EPS - mid**2 * EPS**2) / (1 - mid**2 * EPS**2)))
    if s > S_J:
        lo = mid
    else:
        hi = mid
print(f"  C1 reconciling bare rung with JUNO-now central: C1 = {0.5*(lo+hi):.3f}"
      f"  (was ~1.52 against the old central)")
