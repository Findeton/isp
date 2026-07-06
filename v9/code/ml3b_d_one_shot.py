#!/usr/bin/env python3
"""
ml3b_d_one_shot.py — v9 round 18: THE ONE-SHOT ADJUDICATION
(note-ml3b-d; pins committed at bfe793b BEFORE this receipt existed).

The principled two-party estimator pair (seals join DISTINCT threads; the
d = 0 contact cell is not a seal — the separated correlator is the
physical two-point content), window-free and cutoff-free:
  E1_xy = (1/V) sum_{u != v} C^{xy}(u,v)                    (p = 0 mode)
  E2_xy = (1/2) sum_axes (1/V) sum_{u != v}
              cos(2*pi*Delta_a/L) C^{xy}(u,v)      (p_min star-averaged)
Machinery VERBATIM from the corrected ml3b-c receipt (80f3f8b): sectors
(1, 2), joint COMPLEX zero-mode projector, bubbles, multi-start Newton.

PINNED GATES (note-ml3b-d SS3):
  Gd1  all eight |E{1,2}_xy| > 1e-14 at (4, 1/2) subtracted.
       REFUSED => SEPARATION-NULL (redesign, not a locus kill).
  Gd2  THE ONE-SHOT: parity 8 ways = {E1, E2} x {gx 1/4, 1/2} x
       {subtracted, full}.  Unanimous => SELECTED-ODD (success) /
       SELECTED-EVEN (the locus+assignment KILL).  Any split =>
       FAILS-AT-THIS-ORDER (named axis).  IRREVOCABLE at tree/L = 6.
  Gd3  [directional, printed]: free point + the (4, -1/2) positive root
       reproduce the anchor parities.
Registered expectation [directional]: SELECTED-ODD via d = 1 dominance
(the d = 1 component is public, LEDGER #70; the d >= 2 re-weighting and
the 8-way unanimity are the live content).
INFO: full per-distance signed table (d = 0..6, both conventions); the
demoted (0, 1) row.  Exit 1 by design on refusal.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

gam1 = np.array([[0, 1], [1, 0]], complex)
gam2 = np.array([[0, -1j], [1j, 0]], complex)
gam5 = np.array([[1, 0], [0, -1]], complex)
ID2  = np.eye(2, dtype=complex)

def flux_links(L1, L2, Q):
    x2 = np.arange(L2)
    U1 = np.exp(-2j * np.pi * Q * x2 / (L1 * L2))[None, :] * np.ones((L1, 1))
    U2 = np.ones((L1, L2), complex)
    U2[:, L2 - 1] = np.exp(2j * np.pi * Q * np.arange(L1) / L1)
    return [U1, U2]

def hop(L1, L2, U, mu):
    V = L1 * L2
    T = np.zeros((V, V), complex)
    for x1 in range(L1):
        for x2 in range(L2):
            s = x1 * L2 + x2
            t = (((x1 + 1) % L1) * L2 + x2) if mu == 0 else (x1 * L2 + (x2 + 1) % L2)
            T[s, t] = U[mu][x1, x2]
    return T

def wilson(L1, L2, U, m0=-1.0, r=1.0):
    V = L1 * L2
    D = (m0 + 2 * r) * np.eye(2 * V, dtype=complex)
    for mu, g in ((0, gam1), (1, gam2)):
        T = hop(L1, L2, U, mu)
        D -= 0.5 * (np.kron(r * np.eye(2) - g, T)
                    + np.kron(r * np.eye(2) + g, T.conj().T))
    return D

def overlap_float(L1, L2, U):
    V = L1 * L2
    G5 = np.kron(gam5, np.eye(V))
    H = G5 @ wilson(L1, L2, U)
    ev, P = np.linalg.eigh(H)
    s = (P * np.sign(ev)) @ P.conj().T
    return np.eye(2 * V) + G5 @ s, G5, s

def build_sigma_extended(L, Q):
    """Luscher-subtracted condensate as a closed eigenvalue sum (verbatim)."""
    U = flux_links(L, L, Q)
    D, G5, s = overlap_float(L, L, U)
    V = L * L
    evD = np.linalg.eigvals(D)
    n_zero = int(np.sum(np.abs(evD) < 1e-8))
    order = np.argsort(np.abs(evD))
    lam = [mp.mpc(z.real, z.imag) for z in evD]
    for j in order[:n_zero]:
        lam[j] = mp.mpc(0)
    def Sigma(Mval):
        Mv = mp.mpf(Mval) if not isinstance(Mval, mp.mpf) else Mval
        tot = mp.mpf(0)
        for l in lam:
            num = 1 - l / 2
            den = l + Mv * (1 - l / 2)
            tot += num / den
        return (tot / V).real
    return Sigma, n_zero, evD

def solve_coupled(g2, gx, SA, SB, nzA, nzB, V, start=("0.7", "0.7")):
    def bulkA(M): return SA(M) - mp.mpf(nzA) / (mp.mpf(M) * V)
    def bulkB(M): return SB(M) - mp.mpf(nzB) / (mp.mpf(M) * V)
    MA, MB = mp.mpf(start[0]), mp.mpf(start[1])
    for _ in range(200):
        fA = MA - g2 * bulkA(MA) - gx * bulkB(MB)
        fB = MB - g2 * bulkB(MB) - gx * bulkA(MA)
        h = mp.mpf("1e-20")
        dAA = 1 - g2 * (bulkA(MA + h) - bulkA(MA)) / h
        dAB = -gx * (bulkB(MB + h) - bulkB(MB)) / h
        dBA = -gx * (bulkA(MA + h) - bulkA(MA)) / h
        dBB = 1 - g2 * (bulkB(MB + h) - bulkB(MB)) / h
        det = dAA * dBB - dAB * dBA
        dMA = (fA * dBB - fB * dAB) / det
        dMB = (fB * dAA - fA * dBA) / det
        MA, MB = MA - dMA, MB - dMB
        if abs(dMA) + abs(dMB) < mp.mpf("1e-50"):
            break
    res = (abs(MA - g2 * bulkA(MA) - gx * bulkB(MB))
           + abs(MB - g2 * bulkB(MB) - gx * bulkA(MA))
           if MA > 0 and MB > 0 else mp.mpf(1))
    return MA, MB, res

# ---------------- geometry ----------------
Lx = 6; V = Lx * Lx
sites = [(x, y) for x in range(Lx) for y in range(Lx)]
def torc(a):
    a = np.abs(a)
    return np.minimum(a, Lx - a)
X1 = np.array([s[0] for s in sites]); X2 = np.array([s[1] for s in sites])
D1m = torc(X1[:, None] - X1[None, :]); D2m = torc(X2[:, None] - X2[None, :])
Dm = D1m + D2m                                   # L1 torus distance
OFF = ~np.eye(V, dtype=bool)                     # u != v mask
# E2 weights: cos(2 pi Delta_a / L) star-averaged over the two axes
W2 = 0.5 * (np.cos(2 * np.pi * D1m / Lx) + np.cos(2 * np.pi * D2m / Lx))

# ---------------- operators (corrected ml3b-c, verbatim) ----------------
DC = {}
def sector_D(Q):
    if Q not in DC:
        U = flux_links(Lx, Lx, Q)
        D, _, _ = overlap_float(Lx, Lx, U)
        ev, W = np.linalg.eig(D)
        Winv = np.linalg.inv(W)
        nz = int(np.sum(np.abs(ev) < 1e-8))
        order = np.argsort(np.abs(ev))
        DC[Q] = (D, ev, W, Winv, nz, order)
    return DC[Q]

def propagator(Q, M, subtract=True):
    D, ev, W, Winv, nz, order = sector_D(Q)
    S = np.linalg.inv(D + M * (np.eye(2 * V) - D / 2))
    if subtract and nz > 0:
        P = np.zeros((2 * V, 2 * V), complex)
        for j in order[:nz]:
            P += np.outer(W[:, j], Winv[j, :])
        S = S - S @ P
    return S

def bubble(S, G1, G2):
    Pi = np.zeros((V, V), complex)
    for a in range(2):
        for b in range(2):
            if abs(G1[a, b]) < 1e-30: continue
            for c in range(2):
                for d in range(2):
                    if abs(G2[c, d]) < 1e-30: continue
                    Pi -= G1[a, b] * G2[c, d] * (
                        S[b*V:(b+1)*V, c*V:(c+1)*V]
                        * S[d*V:(d+1)*V, a*V:(a+1)*V].T)
    return Pi.real, float(np.abs(Pi.imag).max())

def cellmats(QA, QB, MA, MB, gx, subtract=True):
    """The four C^{xy} matrices under the S/P assignment (as pinned)."""
    G = {"S": ID2, "P": gam5}
    SA = propagator(QA, float(MA), subtract)
    SB = propagator(QB, float(MB), subtract)
    imax = 0.0
    PiA, PiB = {}, {}
    for x in G:
        PiA[x], i1 = bubble(SA, G[x], ID2)
        PiB[x], i2 = bubble(SB, ID2, G[x])
        imax = max(imax, i1, i2)
    C = {(x, y): float(gx) * (PiA[x] @ PiB[y]) for x in G for y in G}
    return C, imax

def estimators(C):
    """The pinned pair: E1 (p = 0 separated) and E2 (p_min star)."""
    E1 = {xy: float(C[xy][OFF].sum() / V) for xy in C}
    E2 = {xy: float((W2 * C[xy])[OFF].sum() / V) for xy in C}
    return E1, E2

def par(E):
    if any(abs(v) <= 1e-14 for v in E.values()):
        return None
    return "odd" if np.prod([np.sign(v) for v in E.values()]) < 0 else "even"

def cellrow(E):
    return "  ".join(f"E_{x}{y}={E[(x, y)]:+.3e}" for x in "SP" for y in "SP")

# ================= the run =================
print("[ml3b-d: THE ONE-SHOT ADJUDICATION — the principled estimator pair]")
QA, QB = 1, 2
SAf, nzA, _ = build_sigma_extended(Lx, QA)
SBf, nzB, _ = build_sigma_extended(Lx, QB)
print(f"      sectors ({QA}, {QB}); n_zero = ({nzA}, {nzB}); L = {Lx}; "
      "estimators E1 (p=0 separated) / E2 (p_min star), per note SS2")

def solve(g2, gx):
    starts = [("0.7", "0.7")] + [(str(a), str(b))
              for a in (0.1, 0.3, 0.5, 0.9) for b in (0.1, 0.3, 0.5, 0.9)]
    fa = fb = float("nan")
    for st in starts:
        MA, MB, r = solve_coupled(mp.mpf(g2), mp.mpf(gx), SAf, SBf,
                                  nzA, nzB, V, st)
        fa, fb = float(MA), float(MB)
        if (r < mp.mpf("1e-40") and np.isfinite(fa) and np.isfinite(fb)
                and 0.02 < fa < 5 and 0.02 < fb < 5):
            return fa, fb, True
    return fa, fb, False

readings = {}   # (est, gx, conv) -> parity
anchorE = None
for gxs in ("0.5", "0.25"):
    MA, MB, ok = solve(4, gxs)
    print(f"      masses (g2=4, gx={gxs}): M_A = {MA:.6f}, M_B = {MB:.6f}")
    for conv, sub in (("sub", True), ("full", False)):
        C, imax = cellmats(QA, QB, MA, MB, float(gxs), sub)
        E1, E2 = estimators(C)
        readings[("E1", gxs, conv)] = par(E1)
        readings[("E2", gxs, conv)] = par(E2)
        print(f"      (4, {gxs}) {conv}:  E1[{cellrow(E1)}] => {par(E1)}")
        print(f"                    E2[{cellrow(E2)}] => {par(E2)}")
        if gxs == "0.5" and conv == "sub":
            anchorE = (E1, E2, imax)
        if gxs == "0.5":
            # INFO: per-distance signed table, BOTH conventions as pinned
            # (review MINOR-1: the first run under-delivered, sub only)
            print(f"      per-distance signed means ({conv}), d = 0..6:")
            for xy in C:
                row = "  ".join(f"d{d}:{float(C[xy][Dm == d].mean()):+.2e}"
                                for d in range(7))
                print(f"        C_{xy[0]}{xy[1]}: {row}")

E1a, E2a, imaxa = anchorE
print(f"      bubble max|imag| at anchor = {imaxa:.2e}")
gd1 = all(abs(v) > 1e-14 for v in list(E1a.values()) + list(E2a.values()))
check("Gd1 (cells exist at separation): all eight |E{1,2}_xy| > 1e-14 at "
      "(4, 1/2) subtracted", gd1,
      "min = %.3e" % min(abs(v) for v in list(E1a.values()) + list(E2a.values())))

vals = list(readings.values())
if None in vals:
    verdict = "NULL-LEG (a reading lost a cell) — FAILS-AT-THIS-ORDER"
elif len(set(vals)) == 1:
    branch = vals[0]
    verdict = ("SELECTED-ODD" if branch == "odd" else
               "SELECTED-EVEN (THE KILL: the GW-flow locus under the S/P "
               "assignment is REFUTED as the sign's origin)")
else:
    axes = []
    if any(readings[("E1", g, c)] != readings[("E2", g, c)]
           for g in ("0.5", "0.25") for c in ("sub", "full")):
        axes.append("ESTIMATOR")
    if any(readings[(e, g, "sub")] != readings[(e, g, "full")]
           for e in ("E1", "E2") for g in ("0.5", "0.25")):
        axes.append("CONVENTION")
    if any(readings[(e, "0.5", c)] != readings[(e, "0.25", c)]
           for e in ("E1", "E2") for c in ("sub", "full")):
        axes.append("GX")
    verdict = "+".join(axes) + "-SPLIT — FAILS-AT-THIS-ORDER"
check("Gd2 (THE ONE-SHOT ADJUDICATION): 8-way unanimity {E1,E2} x "
      "{1/4,1/2} x {sub,full}; the world's branch is ODD; IRREVOCABLE "
      "at tree level/L = 6",
      verdict == "SELECTED-ODD",
      f"readings {[(k, v) for k, v in readings.items()]} => {verdict}")

# Gd3 [directional, printed]: free point + the (4, -1/2) positive root
MAf, MBf, okf = solve(4, "0")
Cf, _ = cellmats(QA, QB, MAf, MBf, 0.5, True)
E1f, E2f = estimators(Cf)
MAn, MBn, okn = solve(4, "-0.5")
line = f"      Gd3 free point (masses {MAf:.6f}/{MBf:.6f}): E1 {par(E1f)}, E2 {par(E2f)}"
if okn:
    Cn, _ = cellmats(QA, QB, MAn, MBn, -0.5, True)
    E1n, E2n = estimators(Cn)
    line += (f"; (4, -1/2) root ({MAn:.6f}, {MBn:.6f}): "
             f"E1 {par(E1n)}, E2 {par(E2n)}")
else:
    line += "; (4, -1/2): no residual-verified positive root (disclosed)"
print(line + "   [directional: anchor parities expected to persist]")

# INFO: the demoted (0, 1) row under the principled estimators
SA0, nz0, _ = build_sigma_extended(Lx, 0)
SB1, nz1, _ = build_sigma_extended(Lx, 1)
MA01, MB01, _ = solve_coupled(mp.mpf(4), mp.mpf("0.5"), SA0, SB1, nz0, nz1, V)
QA, QB = 0, 1
DC.clear()
C01, _ = cellmats(0, 1, float(MA01), float(MB01), 0.5, True)
E101, E201 = estimators(C01)
print(f"      demoted (0, 1) row: E1[{cellrow(E101)}]")
print("        (A-side P-cells identically zero at Q = 0 — the SS5 "
      "kinematic kill, now at separation)")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gd1 cells; "
      f"Gd2 THE ONE-SHOT ({verdict}); Gd3 printed")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
