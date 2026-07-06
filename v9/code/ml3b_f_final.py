#!/usr/bin/env python3
"""
ml3b_f_final.py — v9 round 20: THE FINAL TREE-LEVEL ADJUDICATION
(note-ml3b-f; pin committed at 26e2adb strictly before this receipt).

The zero-mode fork resolved on principle (note SS1): FULL propagator —
exact spectral content of the record operator carries no deletion
license at O(1) mass; the gap-side subtraction was a bulk-condensate
definition in a scalar equation.  Operators: the improved family
K = (1 - D/2) S (round-19 certified); sectors (1, 2); estimators E1/E2
verbatim; masses re-solved per L.  Direction disclosed in-note (8/8 full
legs odd at L = 6); live content = the improved family at L = 8/10
(never run) + the V-scaling discriminator.

PINNED (note-ml3b-f SS3):
  Gf1  all eight |E{1,2}_xy| > 1e-14 at (4, 1/2) full, at L = 8 AND 10.
  Gf2  THE FINAL ADJUDICATION: 8 legs = {E1, E2} x {gx 1/4, 1/2} x
       {L 8, 10}, full convention.  Unanimous => SELECTED-ODD /
       SELECTED-EVEN; any split => FAILS-AT-TREE-LEVEL, the line ENDS.
  Gf3  [REGISTERED] V-scaling: max-over-cells |E_sub - E_full|/|E_full|
       at (4, 1/2) DECREASES L = 6 -> 10 per estimator (L = 8 printed).
       REFUSED => any SELECTED downgrades to CONVENTION-CONDITIONAL.
INFO: sub parities; the S - P zero-mode cancellation check; distance
tables both L, both conventions.  Exit 1 by design on refusal.
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

# ---------------- per-L infrastructure ----------------
GEO = {}
def geo(L):
    if L not in GEO:
        V = L * L
        X1 = np.repeat(np.arange(L), L); X2 = np.tile(np.arange(L), L)
        def torc(a):
            a = np.abs(a)
            return np.minimum(a, L - a)
        D1m = torc(X1[:, None] - X1[None, :])
        D2m = torc(X2[:, None] - X2[None, :])
        GEO[L] = dict(V=V, Dm=D1m + D2m, OFF=~np.eye(V, dtype=bool),
                      W2=0.5 * (np.cos(2 * np.pi * D1m / L)
                                + np.cos(2 * np.pi * D2m / L)))
    return GEO[L]

DC = {}
def sector_D(L, Q):
    if (L, Q) not in DC:
        U = flux_links(L, L, Q)
        D, _, _ = overlap_float(L, L, U)
        ev, W = np.linalg.eig(D)
        Winv = np.linalg.inv(W)
        nz = int(np.sum(np.abs(ev) < 1e-8))
        order = np.argsort(np.abs(ev))
        DC[(L, Q)] = (D, ev, W, Winv, nz, order)
    return DC[(L, Q)]

def propagator(L, Q, M, subtract):
    D, ev, W, Winv, nz, order = sector_D(L, Q)
    V2 = D.shape[0]
    S = np.linalg.inv(D + M * (np.eye(V2) - D / 2))
    if subtract and nz > 0:
        P = np.zeros((V2, V2), complex)
        for j in order[:nz]:
            P += np.outer(W[:, j], Winv[j, :])
        S = S - S @ P
    return S

def bubble(S, G1, G2, V):
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
    return Pi.real

def cellmats(L, QA, QB, MA, MB, gx, subtract):
    """Improved family K = (1 - D/2) S; full or subtracted propagator."""
    g = geo(L); V = g["V"]
    G = {"S": ID2, "P": gam5}
    legs = {}
    for tag, Q, Ms in (("A", QA, MA), ("B", QB, MB)):
        S = propagator(L, Q, float(Ms), subtract)
        D = sector_D(L, Q)[0]
        legs[tag] = (np.eye(2 * V) - D / 2) @ S
    PiA = {x: bubble(legs["A"], G[x], ID2, V) for x in G}
    PiB = {x: bubble(legs["B"], ID2, G[x], V) for x in G}
    return {(x, y): float(gx) * (PiA[x] @ PiB[y]) for x in G for y in G}

def estimators(C, L):
    g = geo(L); V, OFF, W2 = g["V"], g["OFF"], g["W2"]
    E1 = {xy: float(C[xy][OFF].sum() / V) for xy in C}
    E2 = {xy: float((W2 * C[xy])[OFF].sum() / V) for xy in C}
    return E1, E2

def par(E):
    if any(abs(v) <= 1e-14 for v in E.values()):
        return None
    return "odd" if np.prod([np.sign(v) for v in E.values()]) < 0 else "even"

def cellrow(E):
    return "  ".join(f"E_{x}{y}={E[(x, y)]:+.3e}" for x in "SP" for y in "SP")

def dtable(C, L, tag):
    g = geo(L)
    print(f"      per-distance signed means ({tag}), d = 0..{2*(L//2)}:")
    for xy in C:
        row = "  ".join(f"d{d}:{float(C[xy][g['Dm'] == d].mean()):+.2e}"
                        for d in range(0, min(2 * (L // 2), 6) + 1))
        print(f"        C_{xy[0]}{xy[1]}: {row}")

print("[ml3b-f: THE FINAL TREE-LEVEL ADJUDICATION — full convention, L = 8/10]")
QA, QB = 1, 2
readings = {}
disc = {}          # (L, est) -> max rel sub-vs-full discrepancy at (4, 1/2)
cells_ok = {}
for L in (6, 8, 10):
    SAf, nzA, _ = build_sigma_extended(L, QA)
    SBf, nzB, _ = build_sigma_extended(L, QB)
    V = L * L
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
    for gxs in (("0.5", "0.25") if L > 6 else ("0.5",)):
        MA, MB, ok = solve(4, gxs)
        print(f"      L = {L}, masses (g2=4, gx={gxs}): "
              f"M_A = {MA:.6f}, M_B = {MB:.6f} (n_zero = {nzA}, {nzB})")
        Cfull = cellmats(L, QA, QB, MA, MB, float(gxs), subtract=False)
        E1f, E2f = estimators(Cfull, L)
        if L > 6:
            readings[("E1", gxs, L)] = par(E1f)
            readings[("E2", gxs, L)] = par(E2f)
            print(f"      L={L} (4, {gxs}) FULL:  E1[{cellrow(E1f)}] => {par(E1f)}")
            print(f"                        E2[{cellrow(E2f)}] => {par(E2f)}")
        if gxs == "0.5":
            Csub = cellmats(L, QA, QB, MA, MB, 0.5, subtract=True)
            E1s, E2s = estimators(Csub, L)
            d1 = max(abs(E1s[xy] - E1f[xy]) / max(abs(E1f[xy]), 1e-300)
                     for xy in E1f)
            d2 = max(abs(E2s[xy] - E2f[xy]) / max(abs(E2f[xy]), 1e-300)
                     for xy in E2f)
            disc[(L, "E1")], disc[(L, "E2")] = d1, d2
            print(f"      L={L} Gf3 data: max rel sub-vs-full discrepancy "
                  f"E1 = {d1:.3f}, E2 = {d2:.3f}; sub parities "
                  f"E1 {par(E1s)} / E2 {par(E2s)} [INFO]")
            if L > 6:
                cells_ok[L] = all(abs(v) > 1e-14
                                  for v in list(E1f.values()) + list(E2f.values()))
                dtable(Cfull, L, f"L={L} full")
                dtable(Csub, L, f"L={L} sub")

gf1 = cells_ok.get(8, False) and cells_ok.get(10, False)
check("Gf1 (cells exist): all eight |E{1,2}_xy| > 1e-14 at (4, 1/2) full, "
      "L = 8 AND 10", gf1)

vals = list(readings.values())
if None in vals:
    verdict = "NULL-LEG — FAILS-AT-TREE-LEVEL"
elif len(set(vals)) == 1:
    verdict = ("SELECTED-ODD" if vals[0] == "odd" else
               "SELECTED-EVEN (THE KILL at the principled convention)")
else:
    axes = []
    if any(readings[("E1", g, l)] != readings[("E2", g, l)]
           for g in ("0.5", "0.25") for l in (8, 10)):
        axes.append("ESTIMATOR")
    if any(readings[(e, g, 8)] != readings[(e, g, 10)]
           for e in ("E1", "E2") for g in ("0.5", "0.25")):
        axes.append("L")
    if any(readings[(e, "0.5", l)] != readings[(e, "0.25", l)]
           for e in ("E1", "E2") for l in (8, 10)):
        axes.append("GX")
    verdict = "+".join(axes) + "-SPLIT — FAILS-AT-TREE-LEVEL, the line ENDS"
check("Gf2 (THE FINAL ADJUDICATION): 8-way unanimity {E1,E2} x {1/4,1/2} "
      "x {L=8,10}, FULL convention; the world's branch is ODD",
      verdict == "SELECTED-ODD",
      f"readings {[(k, v) for k, v in readings.items()]} => {verdict}")

g3_1 = disc[(10, "E1")] < disc[(6, "E1")]
g3_2 = disc[(10, "E2")] < disc[(6, "E2")]
gf3 = g3_1 and g3_2
check("Gf3 [REGISTERED] V-scaling: max rel sub-vs-full discrepancy "
      "decreases L = 6 -> 10 for BOTH estimators (else any SELECTED "
      "downgrades to CONVENTION-CONDITIONAL)", gf3,
      f"E1: {disc[(6,'E1')]:.3f} -> {disc[(8,'E1')]:.3f} -> {disc[(10,'E1')]:.3f}; "
      f"E2: {disc[(6,'E2')]:.3f} -> {disc[(8,'E2')]:.3f} -> {disc[(10,'E2')]:.3f}")

# INFO: the S - P zero-mode cancellation check at (6, Q=2)
D, ev, W, Winv, nz, order = sector_D(6, 2)
Sfull = propagator(6, 2, 0.8205, False)
Ssub = propagator(6, 2, 0.8205, True)
Z = Sfull - Ssub
Vs = 36
K = (np.eye(2 * Vs) - D / 2)
Zi = K @ Z
pp = bubble(Zi, gam5, gam5, Vs)
ss = bubble(Zi, ID2, ID2, Vs)
print(f"      INFO S-P zero-mode cancellation: max|Pi_Z^PP - Pi_Z^SS| = "
      f"{np.abs(pp - ss).max():.2e} (chirality: Z x Z pieces equal)")

final = verdict if not (verdict == "SELECTED-ODD" and not gf3) else \
    "SELECTED-ODD-CONVENTION-CONDITIONAL (Gf3 refused — the pinned downgrade)"
print(f"      FINAL: {final}")
print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gf1; Gf2 "
      f"({verdict}); Gf3 V-scaling")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
