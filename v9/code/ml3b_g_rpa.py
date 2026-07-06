#!/usr/bin/env python3
"""
ml3b_g_rpa.py — v9 round 21: THE RPA DRESSING — this route's one shot
(note-ml3b-g; pin committed at 0c1495f strictly before this receipt).

Dressed cells C^{xy}_RPA = Pi_A^{x,S} [D_sigma]_AB Pi_B^{S,y} with
D_sigma = (I - G Pi)^-1 G, G = [[g2 I, gx I],[gx I, g2 I]],
Pi = blockdiag(P_A, P_B), P_s = the improved scalar bubble (FULL
propagator — the r20 principled content).  Leading order = tree exactly.

PINNED (note-ml3b-g SS2):
  Gr1  wiring (truncated D_sigma = gx I reproduces tree to machine
       precision) + convergence (G/8 closed form vs K = 40 partial sum,
       rel 1e-12, masses fixed).
  Gr2  min Re eig(I - G Pi) > 0 at ALL four points ({gx 1/4,1/2} x
       {L 8,10}).  REFUSED => RPA-INVALID (terminal for this route).
  Gr3  THE DRESSED ADJUDICATION: 8 legs = {E1,E2} x {gx} x {L} on
       C_RPA.  Unanimous => SELECTED-{ODD,EVEN}-DRESSED; any split =>
       FAILS-AT-RPA (the sign exits the resummed reach).
INFO: sigma spectrum; anchor distance tables; subtracted row; E1/E2
spread dressed vs tree; L = 6 continuity row.  Exit 1 on refusal.
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
        DC[(L, Q)] = D
    return DC[(L, Q)]

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

def legs_and_bubbles(L, QA, QB, MA, MB, subtract=False):
    """Improved-family K-legs (FULL propagator default per r20) and the
    three bubble families per species."""
    g = geo(L); V = g["V"]
    out = {}
    for tag, Q, Ms in (("A", QA, MA), ("B", QB, MB)):
        D = sector_D(L, Q)
        S = np.linalg.inv(D + float(Ms) * (np.eye(2 * V) - D / 2))
        if subtract:
            ev, W = np.linalg.eig(D)
            Winv = np.linalg.inv(W)
            nz = int(np.sum(np.abs(ev) < 1e-8))
            order = np.argsort(np.abs(ev))
            P = np.zeros((2 * V, 2 * V), complex)
            for j in order[:nz]:
                P += np.outer(W[:, j], Winv[j, :])
            S = S - S @ P
        K = (np.eye(2 * V) - D / 2) @ S
        out[tag] = K
    PiA = {x: bubble(out["A"], G_, ID2, V) for x, G_ in (("S", ID2), ("P", gam5))}
    PiB = {y: bubble(out["B"], ID2, G_, V) for y, G_ in (("S", ID2), ("P", gam5))}
    return PiA, PiB

def dressed_cells(L, g2, gx, PiA, PiB, mode="rpa"):
    """C^{xy} = PiA^{x,S} [D_sigma]_AB PiB^{S,y}; mode 'tree' truncates
    D_sigma to gx I (Gr1 wiring)."""
    V = geo(L)["V"]
    PA, PB = PiA["S"], PiB["S"]
    if mode == "tree":
        DAB = gx * np.eye(V)
        info = None
    else:
        Gm = np.block([[g2 * np.eye(V), gx * np.eye(V)],
                       [gx * np.eye(V), g2 * np.eye(V)]])
        Pi = np.block([[PA, np.zeros((V, V))],
                       [np.zeros((V, V)), PB]])
        A = np.eye(2 * V) - Gm @ Pi
        ev = np.linalg.eigvals(A)
        Dsig = np.linalg.solve(A, Gm)
        DAB = Dsig[:V, V:]
        info = float(np.min(ev.real))
    C = {(x, y): PiA[x] @ DAB @ PiB[y] for x in "SP" for y in "SP"}
    return C, info

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

print("[ml3b-g: THE RPA DRESSING — the sigma-pole sign object]")
QA, QB = 1, 2
readings = {}
minevs = {}
spread = {}
anchor_pack = None
for L in (8, 10):
    SAf, nzA, _ = build_sigma_extended(L, QA)
    SBf, nzB, _ = build_sigma_extended(L, QB)
    V = L * L
    def solve(g2, gx):
        starts = [("0.7", "0.7")] + [(str(a), str(b))
                  for a in (0.1, 0.3, 0.5, 0.9) for b in (0.1, 0.3, 0.5, 0.9)]
        for st in starts:
            MA, MB, r = solve_coupled(mp.mpf(g2), mp.mpf(gx), SAf, SBf,
                                      nzA, nzB, V, st)
            fa, fb = float(MA), float(MB)
            if (r < mp.mpf("1e-40") and 0.02 < fa < 5 and 0.02 < fb < 5):
                return fa, fb
        raise SystemExit("no root")
    for gxs in ("0.5", "0.25"):
        MA, MB = solve(4, gxs)
        PiA, PiB = legs_and_bubbles(L, QA, QB, MA, MB)
        C, mev = dressed_cells(L, 4.0, float(gxs), PiA, PiB)
        minevs[(L, gxs)] = mev
        E1, E2 = estimators(C, L)
        readings[("E1", gxs, L)] = par(E1)
        readings[("E2", gxs, L)] = par(E2)
        print(f"      L={L} (4, {gxs}) RPA: masses {MA:.6f}/{MB:.6f}; "
              f"min Re eig(I-GPi) = {mev:+.4f}")
        print(f"        E1[{cellrow(E1)}] => {par(E1)}")
        print(f"        E2[{cellrow(E2)}] => {par(E2)}")
        if L == 8 and gxs == "0.5":
            anchor_pack = (L, MA, MB, PiA, PiB, C, E1, E2)

# Gr1: wiring + convergence at the anchor
L8, MA8, MB8, PiA8, PiB8, C8, E1a, E2a = anchor_pack
Ctree, _ = dressed_cells(8, 4.0, 0.5, PiA8, PiB8, mode="tree")
Ctree_direct = {xy: 0.5 * (PiA8[xy[0]] @ PiB8[xy[1]]) for xy in Ctree}
w1 = max(np.abs(Ctree[xy] - Ctree_direct[xy]).max() for xy in Ctree)
V8 = 64
Gm = np.block([[4.0 * np.eye(V8), 0.5 * np.eye(V8)],
               [0.5 * np.eye(V8), 4.0 * np.eye(V8)]]) / 8.0
Pi8 = np.block([[PiA8["S"], np.zeros((V8, V8))],
                [np.zeros((V8, V8)), PiB8["S"]]])
closed = np.linalg.solve(np.eye(2 * V8) - Gm @ Pi8, Gm)
part = np.zeros_like(Gm); term = Gm.copy()
for _ in range(40):
    part += term
    term = Gm @ Pi8 @ term
conv = np.abs(closed - part).max() / max(np.abs(closed).max(), 1e-300)
check("Gr1 (wiring + convergence): truncated D_sigma reproduces tree "
      "exactly; G/8 closed form vs K = 40 partial sum rel < 1e-12",
      w1 == 0.0 and conv < 1e-12, f"wiring {w1:.1e}; conv {conv:.2e}")

gr2 = all(v > 0 for v in minevs.values())
check("Gr2 (RPA validity): min Re eig(I - G Pi) > 0 at ALL four points",
      gr2, "; ".join(f"(L={l},gx={g}): {v:+.4f}" for (l, g), v in minevs.items()))

vals = list(readings.values())
if None in vals:
    verdict = "NULL-LEG — FAILS-AT-RPA"
elif len(set(vals)) == 1:
    verdict = ("SELECTED-ODD-DRESSED" if vals[0] == "odd" else
               "SELECTED-EVEN-DRESSED (THE KILL at the dressed order)")
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
    verdict = "+".join(axes) + "-SPLIT — FAILS-AT-RPA"
gr2v = verdict if gr2 else "RPA-INVALID (Gr2 refused — terminal for this route)"
check("Gr3 (THE DRESSED ADJUDICATION — this route's one shot): 8-way "
      "unanimity on C_RPA; the world's branch is ODD",
      gr2 and verdict == "SELECTED-ODD-DRESSED",
      f"readings {[(k, v) for k, v in readings.items()]} => {gr2v}")

# INFO
print("      [INFO — unpinned]")
g8 = geo(8)
print("      anchor per-distance signed means (RPA, full), d = 0..6:")
for xy in C8:
    row = "  ".join(f"d{d}:{float(C8[xy][g8['Dm'] == d].mean()):+.2e}"
                    for d in range(7))
    print(f"        C_{xy[0]}{xy[1]}: {row}")
E1t, E2t = estimators(Ctree_direct, 8)
sp_t = max(abs(E1t[xy] - E2t[xy]) / max(abs(E1t[xy]), 1e-300) for xy in E1t)
sp_d = max(abs(E1a[xy] - E2a[xy]) / max(abs(E1a[xy]), 1e-300) for xy in E1a)
print(f"      E1-vs-E2 max spread at anchor: tree {sp_t:.2f} vs dressed "
      f"{sp_d:.2f} [mechanistic registration: dressed < tree]")
PiAs, PiBs = legs_and_bubbles(8, QA, QB, MA8, MB8, subtract=True)
Cs, _ = dressed_cells(8, 4.0, 0.5, PiAs, PiBs)
E1s, E2s = estimators(Cs, 8)
print(f"      subtracted-convention row (anchor): E1 {par(E1s)} / E2 {par(E2s)}")
SA6, nz6a, _ = build_sigma_extended(6, QA)
SB6, nz6b, _ = build_sigma_extended(6, QB)
MA6, MB6, _ = solve_coupled(mp.mpf(4), mp.mpf("0.5"), SA6, SB6, nz6a, nz6b, 36)
PiA6, PiB6 = legs_and_bubbles(6, QA, QB, float(MA6), float(MB6))
C6, mev6 = dressed_cells(6, 4.0, 0.5, PiA6, PiB6)
E16, E26 = estimators(C6, 6)
print(f"      L = 6 continuity row: E1 {par(E16)} / E2 {par(E26)} "
      f"(min eig {mev6:+.4f})")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gr1 wiring; "
      f"Gr2 validity; Gr3 ({gr2v})")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
