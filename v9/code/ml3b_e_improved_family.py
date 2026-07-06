#!/usr/bin/env python3
"""
ml3b_e_improved_family.py — v9 round 19: THE IMPROVED FAMILY'S ONE SHOT
(note-ml3b-e; pin committed at 3ce7fc3 strictly before this receipt).

The chirally-consistent assignment: improved bilinears psi-bar Gamma
(1 - D/2) psi (the covariant densities of the exact GW symmetry; the
SAME operator content step (a)'s gap equation prices, Tr[(1 - D/2) S]).
Implementation: K = (1 - D/2) S replaces S in every bubble (source,
vertex, sink).  Everything else verbatim from ml3b-d: sectors (1, 2),
step-(a) masses, the principled estimator pair E1/E2, the 8-way
protocol, joint-complex zero-mode subtraction then improvement.

PINNED (note-ml3b-e SS3):
  Ge1  all eight |E{1,2}_xy| > 1e-14 at (4, 1/2) subtracted.
  Ge2  THE FAMILY'S ONE SHOT: 8-way unanimity {E1,E2} x {1/4,1/2} x
       {sub,full} => SELECTED-ODD / SELECTED-EVEN (the harder kill);
       any split => FAILS-AT-THIS-ORDER for this family (irrevocable).
  Ge3  [directional, printed]: (i) convention fragility narrows vs the
       naive family; (ii) free point + (4,-1/2) root reproduce anchor.
INFO: distance tables BOTH conventions (round-18 MINOR-1 lesson); the
naive-family cells alongside.  Exit 1 by design on refusal.
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

Lx = 6; V = Lx * Lx
sites = [(x, y) for x in range(Lx) for y in range(Lx)]
def torc(a):
    a = np.abs(a)
    return np.minimum(a, Lx - a)
X1 = np.array([s[0] for s in sites]); X2 = np.array([s[1] for s in sites])
D1m = torc(X1[:, None] - X1[None, :]); D2m = torc(X2[:, None] - X2[None, :])
Dm = D1m + D2m
OFF = ~np.eye(V, dtype=bool)
W2 = 0.5 * (np.cos(2 * np.pi * D1m / Lx) + np.cos(2 * np.pi * D2m / Lx))

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

def cellmats(QA, QB, MA, MB, gx, subtract=True, improve=True):
    """Improved family: K = (1 - D/2) S in every bubble; improve=False
    reproduces the naive family (INFO only)."""
    G = {"S": ID2, "P": gam5}
    out = {}
    imax = 0.0
    legs = {}
    for tag, Q, Ms in (("A", QA, MA), ("B", QB, MB)):
        S = propagator(Q, float(Ms), subtract)
        if improve:
            D = sector_D(Q)[0]
            S = (np.eye(2 * V) - D / 2) @ S
        legs[tag] = S
    PiA, PiB = {}, {}
    for x in G:
        PiA[x], i1 = bubble(legs["A"], G[x], ID2)
        PiB[x], i2 = bubble(legs["B"], ID2, G[x])
        imax = max(imax, i1, i2)
    C = {(x, y): float(gx) * (PiA[x] @ PiB[y]) for x in G for y in G}
    return C, imax

def estimators(C):
    E1 = {xy: float(C[xy][OFF].sum() / V) for xy in C}
    E2 = {xy: float((W2 * C[xy])[OFF].sum() / V) for xy in C}
    return E1, E2

def par(E):
    if any(abs(v) <= 1e-14 for v in E.values()):
        return None
    return "odd" if np.prod([np.sign(v) for v in E.values()]) < 0 else "even"

def cellrow(E):
    return "  ".join(f"E_{x}{y}={E[(x, y)]:+.3e}" for x in "SP" for y in "SP")

print("[ml3b-e: THE IMPROVED FAMILY'S ONE SHOT — chirally-consistent bilinears]")
QA, QB = 1, 2
SAf, nzA, _ = build_sigma_extended(Lx, QA)
SBf, nzB, _ = build_sigma_extended(Lx, QB)
print(f"      sectors ({QA}, {QB}); K = (1 - D/2) S in all bubbles; "
      "E1/E2 per note-ml3b-d SS2 (carried)")

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

readings = {}
anchorE = None
fragility = {}
for gxs in ("0.5", "0.25"):
    MA, MB, ok = solve(4, gxs)
    print(f"      masses (g2=4, gx={gxs}): M_A = {MA:.6f}, M_B = {MB:.6f}")
    Erow = {}
    for conv, sub in (("sub", True), ("full", False)):
        C, imax = cellmats(QA, QB, MA, MB, float(gxs), sub)
        E1, E2 = estimators(C)
        readings[("E1", gxs, conv)] = par(E1)
        readings[("E2", gxs, conv)] = par(E2)
        Erow[conv] = E1
        print(f"      (4, {gxs}) {conv}:  E1[{cellrow(E1)}] => {par(E1)}")
        print(f"                    E2[{cellrow(E2)}] => {par(E2)}")
        if gxs == "0.5" and conv == "sub":
            anchorE = (E1, E2, imax)
        if gxs == "0.5":
            print(f"      per-distance signed means ({conv}), d = 0..6:")
            for xy in C:
                row = "  ".join(f"d{d}:{float(C[xy][Dm == d].mean()):+.2e}"
                                for d in range(7))
                print(f"        C_{xy[0]}{xy[1]}: {row}")
    fragility[gxs] = sum(1 for xy in Erow["sub"]
                         if np.sign(Erow["sub"][xy]) != np.sign(Erow["full"][xy]))

E1a, E2a, imaxa = anchorE
print(f"      bubble max|imag| at anchor = {imaxa:.2e}")
ge1 = all(abs(v) > 1e-14 for v in list(E1a.values()) + list(E2a.values()))
check("Ge1 (cells exist): all eight |E{1,2}_xy| > 1e-14 at (4, 1/2) sub",
      ge1, "min = %.3e" % min(abs(v) for v in list(E1a.values()) + list(E2a.values())))

vals = list(readings.values())
if None in vals:
    verdict = "NULL-LEG — FAILS-AT-THIS-ORDER for this family"
elif len(set(vals)) == 1:
    branch = vals[0]
    verdict = ("SELECTED-ODD" if branch == "odd" else
               "SELECTED-EVEN (THE HARDER KILL: the locus refuted at its "
               "own consistent operator content)")
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
    verdict = "+".join(axes) + "-SPLIT — FAILS-AT-THIS-ORDER for this family"
check("Ge2 (THE FAMILY'S ONE SHOT): 8-way unanimity; the world's branch "
      "is ODD; irrevocable per family",
      verdict == "SELECTED-ODD",
      f"readings {[(k, v) for k, v in readings.items()]} => {verdict}")

print(f"      Ge3-i [directional]: E1 sub-vs-full sign flips per gx: "
      f"gx=1/2: {fragility['0.5']}/4 cells, gx=1/4: {fragility['0.25']}/4 "
      f"(naive family had 1/4 — the deciding PP cell)")
MAf, MBf, okf = solve(4, "0")
Cf, _ = cellmats(QA, QB, MAf, MBf, 0.5, True)
E1f, E2f = estimators(Cf)
MAn, MBn, okn = solve(4, "-0.5")
line = f"      Ge3-ii free point: E1 {par(E1f)}, E2 {par(E2f)}"
if okn:
    Cn, _ = cellmats(QA, QB, MAn, MBn, -0.5, True)
    E1n, E2n = estimators(Cn)
    line += f"; (4, -1/2) root ({MAn:.6f}, {MBn:.6f}): E1 {par(E1n)}, E2 {par(E2n)}"
else:
    line += "; (4, -1/2): no residual-verified positive root"
print(line + "   [directional: anchor pattern expected to persist]")
# INFO: the naive family alongside (the record's cross-reference)
MA5, MB5, _ = solve(4, "0.5")
Cnv, _ = cellmats(QA, QB, MA5, MB5, 0.5, True, improve=False)
E1nv, E2nv = estimators(Cnv)
print(f"      INFO naive family at (4, 1/2) sub: E1 => {par(E1nv)}, "
      f"E2 => {par(E2nv)} (round-18 record: even / odd)")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Ge1 cells; "
      f"Ge2 THE ONE SHOT ({verdict}); Ge3 printed")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
